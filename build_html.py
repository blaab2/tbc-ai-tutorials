#!/usr/bin/env python3
"""Wandelt alle Markdown-Dateien des Tutorials in HTML um.

Ergebnis im Ordner ``html/``:
  * index.html                     – Startseite mit allen Materialien
  * <datei>.html                   – jede .md-Datei als lesbare/druckbare Seite
  * 04_Folien_Praesentation.html   – Folien als Vollbild-Präsentation
                                     (Pfeiltasten, N = Notizen, P = Referentenansicht)
  * Beispielmaterial (.txt/.csv) wird mitkopiert, damit alle Links funktionieren.

Aufruf:
  uv run build_html.py            # einmal bauen
  uv run build_html.py --serve    # bauen, unter http://localhost:8000 anzeigen
                                  # und bei Änderungen automatisch neu bauen
"""

from __future__ import annotations

import argparse
import functools
import html
import http.server
import re
import shutil
import threading
import time
from pathlib import Path

import markdown

from slide_visuals import VISUALS

ROOT = Path(__file__).resolve().parent
FONT_DIR = ROOT / "assets" / "fonts"
OUT = ROOT / "html"
SLIDES_MD = "04_Folien.md"
SLIDES_HTML = "04_Folien_Praesentation.html"
BRAND = "KI im Arbeitsalltag"
SKIP_DIRS = {"assets", "html", ".venv", ".tools", ".git", "node_modules"}
COPY_SUFFIXES = {".txt", ".csv", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".pdf"}
FONTS = ""  # Schrift liegt lokal unter assets/fonts (offline-fest)

MD_EXTENSIONS = ["extra", "sane_lists", "toc", "pymdownx.tasklist", "pymdownx.tilde", "pymdownx.magiclink"]
MD_CONFIG = {
    "toc": {"permalink": False, "toc_depth": "2-3"},
    "pymdownx.tasklist": {"custom_checkbox": True, "clickable_checkbox": True},
}

# Bereiche (Reihenfolge = Reihenfolge auf Startseite und in der Navigation)
SECTIONS = [
    ("start", "Start"),
    ("trainer", "Für dich als Trainer"),
    ("teilnehmende", "Für die Teilnehmenden"),
    ("beispiele", "Beispielmaterial"),
    ("tests", "Testläufe"),
    ("weitere", "Weitere Dokumente"),
]
# Bekannte Dateien: (Bereich, Icon, Kurztitel, Beschreibung, Farbverlauf)
META = {
    "README.md": ("start", "🧭", "Überblick", "Ablauf, Dateien, Start-Checkliste und Druckliste.", "blue"),
    "01_Trainer-Leitfaden.md": ("trainer", "🎤", "Trainer-Leitfaden", "Block für Block: was du sagst, zeigst und tust.", "indigo"),
    "02_Einladung_und_Vorbereitung.md": ("trainer", "✉️", "Einladung & Vorbereitung", "Einladung, Erinnerung, Einrichtung und Vorab-Umfrage.", "teal"),
    "04_Folien.md": ("trainer", "🖥️", "Folien & Sprechernotizen", "Alle Folien als Text – zum Lesen und Anpassen.", "purple"),
    "06_Uebungen/Trainer-Loesungshinweise.md": ("trainer", "🗝️", "Lösungshinweise", "Musterprompts, Lösungsschlüssel und Stolpersteine.", "orange"),
    "06_Uebungen/Erwartete_Ergebnisse.md": ("trainer", "🔬", "Erwartete Ergebnisse", "Was die KI bei jeder Übung tatsächlich liefert.", "pink"),
    "08_Nachbereitung.md": ("trainer", "🔁", "Nachbereitung", "Feedback, Follow-up-Mail, Tipps-Kanal und Folgetermin.", "green"),
    "03_Daten-Ampel.md": ("teilnehmende", "🚦", "Daten-Ampel", "Was darf in den KI-Assistenten – und was nicht.", "red"),
    "05_Spickzettel.md": ("teilnehmende", "📝", "Spickzettel", "Eine Seite mit Prompt-Baukasten und Vorlagen.", "yellow"),
    "05b_Modellauswahl.md": ("teilnehmende", "🧠", "Modellauswahl", "Welches Modell für welche Aufgabe?", "indigo"),
    "06_Uebungen/Uebung_1_Texte_schreiben.md": ("teilnehmende", "✍️", "Übung 1 · Texte schreiben", "Mail beantworten, Ton ändern, übersetzen.", "blue"),
    "06_Uebungen/Uebung_2_Gute_Prompts.md": ("teilnehmende", "🧩", "Übung 2 · Gute Prompts", "Vom Minimal-Prompt zum Prompt-Baukasten.", "purple"),
    "06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md": ("teilnehmende", "📄", "Übung 3 · Dokumente & Tabellen", "Zusammenfassen, vergleichen, aufräumen.", "teal"),
    "06_Uebungen/Uebung_4_Eigene_Aufgabe.md": ("teilnehmende", "🚀", "Übung 4 · Eigene Aufgabe", "Deine lästige Aufgabe – im Zweierteam.", "orange"),
    "07_Beispielmaterial/demo_fehler_zeigen.md": ("beispiele", "⚠️", "Demo: KI-Schwächen", "Prompts, die typische Fehler live zeigen.", "red"),
    "07_Beispielmaterial/pruefbericht_lang.md": ("beispiele", "📊", "Prüfbericht", "Langer Bericht zum Zusammenfassen.", "gray"),
    "07_Beispielmaterial/richtlinie_reisekosten_v1.md": ("beispiele", "🧾", "Reisekosten-Richtlinie v1", "Ausgangsversion für den Vergleich.", "gray"),
    "07_Beispielmaterial/richtlinie_reisekosten_v2.md": ("beispiele", "🧾", "Reisekosten-Richtlinie v2", "Neue Version – mit 7 Änderungen.", "gray"),
    "09_Testlaeufe/README.md": ("tests", "🧪", "Alle Testläufe", "Protokolle: jede Übung mit drei Modellen durchgespielt.", "green"),
}
AGENDA = [
    ("0:00", "Was ist KI eigentlich?"), ("0:15", "Spielregeln"), ("0:30", "Texte schreiben"),
    ("1:00", "Gute Prompts"), ("1:30", "Pause"), ("1:40", "Dokumente & Tabellen"),
    ("2:20", "Deine eigene Aufgabe"), ("2:50", "Ergebnisse & Abschluss"),
]


# --------------------------------------------------------------------------- #
#  Hilfsfunktionen
# --------------------------------------------------------------------------- #
def md_to_html(text: str, breaks: bool = False) -> tuple[str, str]:
    exts = MD_EXTENSIONS + (["nl2br"] if breaks else [])
    md = markdown.Markdown(extensions=exts, extension_configs=MD_CONFIG)
    body = md.convert(text)
    return body, getattr(md, "toc", "")


def rewrite_links(body: str) -> str:
    """Relative Links auf .md-Dateien zeigen danach auf die .html-Version."""
    def repl(m: re.Match) -> str:
        href = m.group(2)
        if re.match(r"^[a-z]+:", href) or href.startswith("#"):
            return m.group(0)
        return f'{m.group(1)}"{re.sub(r"\.md(#|$)", r".html\1", href)}"'
    return re.sub(r'(href=)"([^"]+)"', repl, body)


def source_files() -> list[Path]:
    return [p for p in sorted(ROOT.rglob("*"))
            if p.is_file() and not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)]


def first_heading(text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else fallback


def first_paragraph(text: str) -> str:
    for block in re.split(r"\n\s*\n", text):
        b = block.strip()
        if b and not b.startswith(("#", "|", "-", "*", ">", "`", "<", "---")):
            b = re.sub(r"[*_`\[\]]", "", re.sub(r"\]\([^)]*\)", "]", b))
            return (b[:140] + "…") if len(b) > 140 else b
    return ""


def rel_prefix(rel: Path) -> str:
    return "../" * (len(rel.parts) - 1)


class Doc:
    def __init__(self, path: Path):
        self.path = path
        self.rel = path.relative_to(ROOT)
        self.key = self.rel.as_posix()
        self.href = self.rel.with_suffix(".html").as_posix()
        self.text = path.read_text(encoding="utf-8")
        self.heading = first_heading(self.text, path.stem)
        meta = META.get(self.key)
        if meta:
            self.section, self.icon, self.short, self.desc, self.color = meta
        else:
            top = self.rel.parts[0] if len(self.rel.parts) > 1 else ""
            self.section = {"09_Testlaeufe": "tests", "07_Beispielmaterial": "beispiele",
                            "06_Uebungen": "teilnehmende"}.get(top, "weitere")
            self.icon = {"tests": "🧪", "beispiele": "📁"}.get(self.section, "📘")
            self.short = re.sub(r"^Testlauf:\s*", "", self.heading)
            self.desc = first_paragraph(self.text)
            self.color = "gray"


def load_docs() -> list[Doc]:
    docs = [Doc(p) for p in source_files() if p.suffix.lower() == ".md"]
    order = {k: i for i, k in enumerate(META)}
    sec_order = {k: i for i, (k, _) in enumerate(SECTIONS)}
    docs.sort(key=lambda d: (sec_order[d.section], order.get(d.key, 999), d.key))
    return docs


def esc(s: str) -> str:
    return html.escape(s, quote=True)


# --------------------------------------------------------------------------- #
#  Dokumentseiten
# --------------------------------------------------------------------------- #
FONT_FACE = r"""
@font-face{font-family:"Inter";font-style:normal;font-weight:100 900;font-display:swap;
 src:url(fonts/inter-latin-wght-normal.woff2) format("woff2");
 unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Inter";font-style:normal;font-weight:100 900;font-display:swap;
 src:url(fonts/inter-latin-ext-wght-normal.woff2) format("woff2");
 unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
"""

DOC_CSS = FONT_FACE + r"""
:root{
 --bg:#ffffff;--bg-alt:#f5f5f7;--fg:#1d1d1f;--fg2:#424245;--muted:#6e6e73;--line:#d2d2d7;--line-soft:#e8e8ed;
 --accent:#0071e3;--accent-hover:#0077ed;--link:#0066cc;--card:#ffffff;--code:#f5f5f7;
 --ph:#fff4c2;--ph-fg:#6b5200;--shadow:0 2px 12px rgba(0,0,0,.06),0 1px 2px rgba(0,0,0,.04);
 --shadow-hover:0 12px 32px rgba(0,0,0,.10),0 2px 6px rgba(0,0,0,.05);--bar:rgba(255,255,255,.72);
 --radius:18px;--font:"Inter",-apple-system,BlinkMacSystemFont,"SF Pro Text","SF Pro Display","Helvetica Neue","Segoe UI",Arial,sans-serif;
}
@media (prefers-color-scheme:dark){:root{
 --bg:#000;--bg-alt:#161617;--fg:#f5f5f7;--fg2:#d2d2d7;--muted:#a1a1a6;--line:#424245;--line-soft:#2c2c2e;
 --accent:#0a84ff;--accent-hover:#409cff;--link:#2997ff;--card:#1c1c1e;--code:#1c1c1e;
 --ph:#4a3b00;--ph-fg:#ffe58a;--shadow:0 1px 2px rgba(0,0,0,.5);--shadow-hover:0 12px 32px rgba(0,0,0,.6);--bar:rgba(22,22,23,.72)}}
*{box-sizing:border-box}
html{font-size:17px;-webkit-text-size-adjust:100%;scroll-padding-top:72px}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--font);line-height:1.6;
 -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;letter-spacing:-.011em}
a{color:var(--link);text-decoration:none}
a:hover{text-decoration:underline}

/* Kopfleiste */
.bar{position:sticky;top:0;z-index:20;height:52px;display:flex;align-items:center;gap:24px;padding:0 22px;
 background:var(--bar);backdrop-filter:saturate(180%) blur(20px);-webkit-backdrop-filter:saturate(180%) blur(20px);
 border-bottom:1px solid var(--line-soft)}
.bar .brand{font-weight:600;color:var(--fg);font-size:.95rem;letter-spacing:-.02em}
.bar .brand:hover{text-decoration:none}
.bar nav{display:flex;gap:22px;margin-left:auto;align-items:center}
.bar nav a{color:var(--fg2);font-size:.8rem}
.bar nav a:hover{color:var(--fg);text-decoration:none}
.pill{display:inline-flex;align-items:center;gap:6px;background:var(--accent);color:#fff!important;border:0;
 border-radius:980px;padding:6px 14px;font:500 .8rem var(--font);cursor:pointer;white-space:nowrap}
.pill:hover{background:var(--accent-hover);text-decoration:none}
.pill.ghost{background:transparent;color:var(--link)!important;border:1px solid var(--line)}
.pill.ghost:hover{background:var(--bg-alt)}
.menu-btn{display:none;background:none;border:0;font-size:1.2rem;color:var(--fg);cursor:pointer;padding:4px}

/* Layout */
.layout{display:grid;grid-template-columns:270px minmax(0,1fr) 230px;max-width:1440px;margin:0 auto}
aside.side{position:sticky;top:52px;height:calc(100vh - 52px);overflow:auto;padding:28px 14px 40px 22px;font-size:.82rem}
aside.side details{margin-bottom:14px}
aside.side summary{list-style:none;cursor:pointer;font-weight:600;color:var(--fg);padding:4px 10px;font-size:.78rem;
 display:flex;justify-content:space-between}
aside.side summary::-webkit-details-marker{display:none}
aside.side summary::after{content:"›";color:var(--muted);transition:transform .2s}
aside.side details[open] summary::after{transform:rotate(90deg)}
aside.side a{display:flex;gap:8px;align-items:baseline;padding:5px 10px;border-radius:8px;color:var(--fg2);line-height:1.35}
aside.side a:hover{background:var(--bg-alt);text-decoration:none}
aside.side a.active{background:var(--bg-alt);color:var(--fg);font-weight:600}
aside.side a .i{width:1.2em;flex:none;text-align:center}
main{padding:48px 56px 96px;min-width:0}
.content{max-width:760px;margin:0 auto}
.eyebrow{color:var(--muted);font-size:.8rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em;margin:0 0 10px}
.toc{position:sticky;top:52px;height:calc(100vh - 52px);overflow:auto;padding:48px 22px 40px 0;font-size:.78rem}
.toc .t{font-weight:600;color:var(--fg);margin-bottom:10px}
.toc ul{list-style:none;margin:0;padding:0}
.toc ul ul{padding-left:12px}
.toc a{display:block;color:var(--muted);padding:3px 0 3px 10px;border-left:2px solid var(--line-soft);line-height:1.35}
.toc a:hover{color:var(--fg);text-decoration:none}
.toc a.on{color:var(--fg);border-left-color:var(--accent)}

/* Typografie */
.content h1{font-size:2.9rem;line-height:1.08;font-weight:700;letter-spacing:-.035em;margin:0 0 28px}
.content h2{font-size:1.75rem;line-height:1.15;font-weight:700;letter-spacing:-.025em;margin:64px 0 18px}
.content h3{font-size:1.25rem;font-weight:600;letter-spacing:-.018em;margin:40px 0 12px}
.content h4{font-size:1.02rem;font-weight:600;margin:28px 0 8px}
.content p,.content li{color:var(--fg2)}
.content strong{color:var(--fg);font-weight:600}
.content ul,.content ol{padding-left:1.3em}
.content li{margin:.35em 0}
.content li::marker{color:var(--muted)}
.content hr{border:0;height:1px;background:var(--line-soft);margin:56px 0}
.content img{max-width:100%;border-radius:12px}

/* Tabellen */
.tbl{overflow-x:auto;margin:24px 0;border:1px solid var(--line-soft);border-radius:14px;background:var(--card)}
.content table{border-collapse:collapse;width:100%;font-size:.88rem}
.content th,.content td{padding:12px 16px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line-soft)}
.content tr:last-child td{border-bottom:0}
.content th{font-weight:600;color:var(--fg);background:var(--bg-alt);font-size:.8rem}
.content td{color:var(--fg2)}

/* Code & Prompts */
.content code{font:500 .86em "SF Mono",ui-monospace,Menlo,Consolas,monospace;background:var(--code);padding:.15em .4em;border-radius:6px}
.content pre{position:relative;background:var(--code);border-radius:14px;padding:20px 22px;margin:20px 0;
 white-space:pre-wrap;word-wrap:break-word;border:1px solid var(--line-soft)}
.content pre code{background:none;padding:0;font-size:.85rem;line-height:1.6;color:var(--fg)}
.copy{position:absolute;top:10px;right:10px;opacity:0;transition:opacity .2s}
.content pre:hover .copy,.copy:focus{opacity:1}
@media (hover:none){.copy{opacity:1}}

/* Hinweise */
.content blockquote{margin:24px 0;padding:18px 22px;background:var(--bg-alt);border-radius:14px;border:0}
.content blockquote p{margin:.3em 0}
.content blockquote::before{content:"ⓘ";color:var(--accent);font-weight:700;margin-right:6px;float:left}
mark.ph{background:var(--ph);color:var(--ph-fg);padding:.05em .4em;border-radius:6px;font-weight:500;font-size:.92em}
.task-list-item{list-style:none;margin-left:-1.3em}
.task-list-item input{accent-color:var(--accent);margin-right:8px;transform:scale(1.15)}

/* Weiter / zurück */
.pager{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:80px}
.pager a{display:block;padding:18px 22px;border-radius:var(--radius);background:var(--bg-alt);color:var(--fg)}
.pager a:hover{text-decoration:none;background:var(--line-soft)}
.pager small{display:block;color:var(--muted);font-size:.75rem;margin-bottom:2px}
.pager .next{text-align:right;grid-column:2}

/* Startseite */
.home main{padding:0}
.hero{text-align:center;padding:96px 22px 64px;background:var(--bg)}
.hero .eyebrow{color:var(--accent);text-transform:none;letter-spacing:0;font-size:1.05rem;font-weight:600}
.hero h1{font-size:clamp(2.8rem,7vw,5.6rem);line-height:1.02;font-weight:800;letter-spacing:-.045em;margin:6px 0 18px;
 background:linear-gradient(90deg,#1d1d1f 10%,#0071e3 55%,#a259ff 90%);-webkit-background-clip:text;background-clip:text;color:transparent}
@media (prefers-color-scheme:dark){.hero h1{background-image:linear-gradient(90deg,#f5f5f7 10%,#2997ff 55%,#bf8bff 90%)}}
.hero .sub{font-size:clamp(1.15rem,2.2vw,1.6rem);color:var(--muted);max-width:760px;margin:0 auto 34px;line-height:1.35;font-weight:500;letter-spacing:-.02em}
.hero .cta{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.hero .cta .pill{font-size:1rem;padding:12px 24px}
.band{background:var(--bg-alt);padding:72px 22px}
.band.white{background:var(--bg)}
.wrap{max-width:1100px;margin:0 auto}
.band h2{font-size:clamp(1.8rem,3.5vw,2.6rem);font-weight:700;letter-spacing:-.035em;margin:0 0 8px;line-height:1.1}
.band .lead{color:var(--muted);font-size:1.1rem;margin:0 0 36px}
.agenda{display:grid;grid-template-columns:repeat(auto-fit,minmax(125px,1fr));gap:12px}
.agenda div{background:var(--card);border-radius:16px;padding:18px 16px;box-shadow:var(--shadow)}
.agenda b{display:block;font-size:1.35rem;letter-spacing:-.03em;color:var(--accent);font-variant-numeric:tabular-nums}
.agenda span{font-size:.85rem;color:var(--fg2);line-height:1.3;display:block;margin-top:4px}
.agenda .pause b{color:var(--muted)}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:18px}
.tile{display:flex;flex-direction:column;background:var(--card);border-radius:var(--radius);padding:26px 24px 22px;
 box-shadow:var(--shadow);color:var(--fg);transition:transform .25s cubic-bezier(.2,.8,.2,1),box-shadow .25s;min-height:190px}
.band.white .tile{background:var(--bg-alt);box-shadow:none}
.tile:hover{transform:translateY(-4px);box-shadow:var(--shadow-hover);text-decoration:none}
.ico{width:46px;height:46px;border-radius:12px;display:grid;place-items:center;font-size:1.4rem;margin-bottom:18px;
 box-shadow:inset 0 0 0 1px rgba(255,255,255,.25)}
.tile strong{font-size:1.1rem;letter-spacing:-.02em;font-weight:600;line-height:1.25}
.tile p{margin:6px 0 0;color:var(--muted);font-size:.88rem;line-height:1.45;flex:1}
.tile .more{margin-top:14px;color:var(--link);font-size:.85rem}
.g-blue{background:linear-gradient(135deg,#5ac8fa,#0071e3)}.g-indigo{background:linear-gradient(135deg,#7d7aff,#3634a3)}
.g-purple{background:linear-gradient(135deg,#da8fff,#8944ab)}.g-teal{background:linear-gradient(135deg,#6ee7d8,#0a9396)}
.g-orange{background:linear-gradient(135deg,#ffc56b,#ff7a00)}.g-pink{background:linear-gradient(135deg,#ff8fb1,#e0245e)}
.g-green{background:linear-gradient(135deg,#7ee08a,#1f9d55)}.g-red{background:linear-gradient(135deg,#ff8a80,#d70015)}
.g-yellow{background:linear-gradient(135deg,#fff176,#f5b400)}.g-gray{background:linear-gradient(135deg,#d1d1d6,#8e8e93)}
.downloads{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
.downloads a{background:var(--card);border-radius:980px;padding:8px 16px;font-size:.85rem;box-shadow:var(--shadow)}
.foot{text-align:center;color:var(--muted);font-size:.78rem;padding:40px 22px 60px}
.feature{display:grid;grid-template-columns:1.1fr 1fr;gap:40px;align-items:center;background:#000;color:#f5f5f7;
 border-radius:28px;padding:56px;overflow:hidden}
.feature h2{color:#f5f5f7}
.feature p{color:#a1a1a6;font-size:1.05rem}
.feature .mock{aspect-ratio:16/9;border-radius:14px;background:linear-gradient(160deg,#1d1d1f,#000);border:1px solid #333;
 display:flex;flex-direction:column;justify-content:center;padding:8% 9%;box-shadow:0 30px 80px rgba(0,113,227,.25)}
.feature .mock b{font-size:clamp(1.2rem,2.6vw,2rem);letter-spacing:-.03em;line-height:1.1;
 background:linear-gradient(90deg,#fff,#2997ff);-webkit-background-clip:text;background-clip:text;color:transparent}
.feature .mock span{color:#86868b;font-size:.8rem;margin-top:10px}
.keys{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0 28px}
.keys kbd{font:500 .75rem var(--font);color:#f5f5f7;background:#1d1d1f;border:1px solid #424245;border-radius:7px;padding:4px 9px}

/* Responsiv */
@media (max-width:1240px){.layout{grid-template-columns:260px minmax(0,1fr)}.toc{display:none}}
@media (max-width:860px){
 .layout{grid-template-columns:1fr}
 aside.side{position:fixed;top:52px;left:0;bottom:0;width:290px;height:auto;z-index:15;background:var(--bg);
  transform:translateX(-100%);transition:transform .25s;border-right:1px solid var(--line-soft)}
 body.nav-open aside.side{transform:none}
 .menu-btn{display:block}
 .bar nav a.hide-sm{display:none}
 main{padding:32px 16px 72px}
 .content h1{font-size:2.1rem}
 .feature{grid-template-columns:1fr;padding:32px 24px}
 .pager{grid-template-columns:1fr}.pager .next{grid-column:1}
}
@media print{
 html{font-size:10.5pt}
 .bar,aside.side,.toc,.copy,.pager{display:none!important}
 .layout{display:block}main{padding:0}
 body{background:#fff;color:#000}
 .content{max-width:none}
 .content h1{font-size:22pt}.content h2{font-size:15pt;margin-top:24pt;break-after:avoid}
 .content p,.content li,.content td{color:#000}
 pre,.tbl,blockquote,tr{break-inside:avoid}
 a{color:#000}
 mark.ph{background:none;color:#000;font-weight:700}
}
"""

DOC_JS = r"""
(function(){
 const re=/\[[A-ZÄÖÜ][A-ZÄÖÜ0-9 \/.,\-–_&:…]{2,}\]/g, root=document.querySelector('.content');
 if(root){const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);const ns=[];while(w.nextNode())ns.push(w.currentNode);
  ns.forEach(n=>{if(n.parentElement.closest('code,pre')&&!/\[[A-ZÄÖÜ ]+\]/.test(n.nodeValue))return;
   if(!re.test(n.nodeValue))return;re.lastIndex=0;const s=document.createElement('span');
   s.innerHTML=n.nodeValue.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(re,m=>`<mark class="ph">${m}</mark>`);
   n.replaceWith(...s.childNodes);});
  root.querySelectorAll('table').forEach(t=>{const d=document.createElement('div');d.className='tbl';t.replaceWith(d);d.appendChild(t);});
  root.querySelectorAll('pre').forEach(pre=>{const b=document.createElement('button');b.className='pill ghost copy';b.textContent='Kopieren';
   b.onclick=()=>{navigator.clipboard.writeText((pre.querySelector('code')||pre).innerText).then(()=>{b.textContent='✓ Kopiert';setTimeout(()=>b.textContent='Kopieren',1500)});};
   pre.appendChild(b);});}
 const mb=document.querySelector('.menu-btn');if(mb)mb.addEventListener('click',()=>document.body.classList.toggle('nav-open'));
 const links=[...document.querySelectorAll('.toc a')];
 if(links.length&&'IntersectionObserver' in window){
  const map=new Map(links.map(a=>[decodeURIComponent(a.hash.slice(1)),a]));
  const io=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){links.forEach(l=>l.classList.remove('on'));
   const a=map.get(e.target.id);if(a)a.classList.add('on');}});},{rootMargin:'-60px 0px -70% 0px'});
  document.querySelectorAll('.content h2[id],.content h3[id]').forEach(h=>io.observe(h));}
})();
"""


def bar(prefix: str) -> str:
    return (f'<header class="bar"><button class="menu-btn" aria-label="Menü">☰</button>'
            f'<a class="brand" href="{prefix}index.html">{BRAND}</a><nav>'
            f'<a class="hide-sm" href="{prefix}index.html">Übersicht</a>'
            f'<a class="hide-sm" href="{prefix}01_Trainer-Leitfaden.html">Leitfaden</a>'
            f'<a class="hide-sm" href="{prefix}05_Spickzettel.html">Spickzettel</a>'
            f'<a class="hide-sm" href="#" onclick="window.print();return false">Drucken</a>'
            f'<a class="pill" href="{prefix}{SLIDES_HTML}">▶ Präsentieren</a></nav></header>')


def sidebar(docs: list[Doc], current: Doc | None, prefix: str) -> str:
    out = ['<aside class="side">']
    for key, label in SECTIONS:
        group = [d for d in docs if d.section == key]
        if not group:
            continue
        is_open = key != "tests" or (current is not None and current.section == "tests")
        out.append(f'<details{" open" if is_open else ""}><summary>{esc(label)}</summary>')
        for d in group:
            cls = ' class="active"' if current is d else ""
            out.append(f'<a{cls} href="{prefix}{d.href}"><span class="i">{d.icon}</span><span>{esc(d.short)}</span></a>')
        out.append("</details>")
    out.append("</aside>")
    return "".join(out)


def shell(title: str, inner: str, prefix: str, body_cls: str = "") -> str:
    return f"""<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{esc(title)} · {BRAND}</title>{FONTS}
<link rel="stylesheet" href="{prefix}assets/style.css"></head>
<body class="{body_cls}">{inner}
<script src="{prefix}assets/doc.js"></script></body></html>"""


def doc_page(d: Doc, docs: list[Doc]) -> str:
    prefix = rel_prefix(d.rel)
    body, toc = md_to_html(d.text)
    body = rewrite_links(body)
    if d.key == SLIDES_MD:
        body = (f'<p><a class="pill" style="font-size:.95rem;padding:10px 20px" href="{prefix}{SLIDES_HTML}">'
                f'▶ Als Präsentation öffnen</a></p>') + body
    section_label = dict(SECTIONS)[d.section]
    i = docs.index(d)
    prev_, next_ = (docs[i - 1] if i > 0 else None), (docs[i + 1] if i + 1 < len(docs) else None)
    pager = '<nav class="pager">'
    if prev_:
        pager += f'<a href="{prefix}{prev_.href}"><small>‹ Zurück</small>{esc(prev_.short)}</a>'
    if next_:
        pager += f'<a class="next" href="{prefix}{next_.href}"><small>Weiter ›</small>{esc(next_.short)}</a>'
    pager += "</nav>"
    toc_html = f'<div class="toc"><div class="t">Auf dieser Seite</div>{toc}</div>' if "<li>" in toc else '<div class="toc"></div>'
    inner = (bar(prefix) + '<div class="layout">' + sidebar(docs, d, prefix)
             + f'<main><article class="content"><p class="eyebrow">{esc(section_label)}</p>{body}{pager}</article></main>'
             + toc_html + "</div>")
    return shell(d.short, inner, prefix)


def tile(d: Doc) -> str:
    return (f'<a class="tile" href="{d.href}"><div class="ico g-{d.color}">{d.icon}</div>'
            f'<strong>{esc(d.short)}</strong><p>{esc(d.desc)}</p><span class="more">Öffnen ›</span></a>')


def index_page(docs: list[Doc], n_slides: int) -> str:
    agenda = "".join(f'<div class="{"pause" if t == "Pause" else ""}"><b>{z}</b><span>{esc(t)}</span></div>'
                     for z, t in AGENDA)
    bands, white = [], True
    for key, label in SECTIONS:
        if key in ("start", "tests"):
            continue
        group = [d for d in docs if d.section == key]
        if not group:
            continue
        extra = ""
        if key == "beispiele":
            dl = "".join(f'<a href="{p.relative_to(ROOT).as_posix()}" download>⬇ {esc(p.name)}</a>'
                         for p in source_files() if p.suffix.lower() in {".txt", ".csv"})
            extra = f'<div class="downloads">{dl}</div>'
        lead = {"trainer": "Alles, was du zum Vorbereiten, Durchführen und Nachbereiten brauchst.",
                "teilnehmende": "Zum Austeilen, Ausdrucken und Mitarbeiten.",
                "beispiele": "Fiktive Dateien der Nordlicht Technik GmbH – gefahrlos zum Üben.",
                "weitere": ""}.get(key, "")
        bands.append(f'<section class="band{" white" if white else ""}"><div class="wrap"><h2>{esc(label)}.</h2>'
                     f'<p class="lead">{esc(lead)}</p><div class="tiles">{"".join(tile(d) for d in group)}</div>{extra}</div></section>')
        white = not white
    tests = [d for d in docs if d.section == "tests"]
    if tests:
        idx = next((d for d in tests if d.key.endswith("README.md")), tests[0])
        n = len([d for d in tests if not d.key.endswith("README.md")])
        bands.append(f'<section class="band{" white" if white else ""}"><div class="wrap"><h2>Getestet.</h2>'
                     f'<p class="lead">{n} Aufgaben und Demos, jeweils mit drei KI-Modellen durchgespielt und bewertet.</p>'
                     f'<div class="tiles">{tile(idx)}'
                     + "".join(tile(d) for d in docs if d.key == "06_Uebungen/Erwartete_Ergebnisse.md")
                     + "</div></div></section>")
    readme = next((d for d in docs if d.key == "README.md"), None)
    inner = (bar("") + '<main>'
             '<section class="hero"><p class="eyebrow">Tutorial · ca. 3 Stunden · ohne Vorkenntnisse</p>'
             f'<h1>{BRAND}.</h1>'
             '<p class="sub">Praxisnah, mit dem eigenen Laptop. Jede Person erledigt echte Aufgaben aus ihrem Alltag – '
             'und weiß danach, welche Daten sie eingeben darf.</p><div class="cta">'
             f'<a class="pill" href="{SLIDES_HTML}">▶ Präsentation starten</a>'
             '<a class="pill ghost" href="01_Trainer-Leitfaden.html">Trainer-Leitfaden ›</a>'
             + (f'<a class="pill ghost" href="{readme.href}">Überblick ›</a>' if readme else "")
             + '</div></section>'
             f'<section class="band"><div class="wrap"><h2>Der Ablauf.</h2><p class="lead">Sieben Blöcke, 70 % selbst machen.</p>'
             f'<div class="agenda">{agenda}</div></div></section>'
             + "".join(bands[:1])
             + '<section class="band white"><div class="wrap"><div class="feature"><div>'
             f'<h2>Die Präsentation.</h2><p>{n_slides} Folien mit Sprechernotizen, Referentenansicht und Timer – direkt im Browser.</p>'
             '<div class="keys"><kbd>→ weiter</kbd><kbd>F Vollbild</kbd><kbd>N Notizen</kbd><kbd>P Referent</kbd>'
             '<kbd>O Übersicht</kbd><kbd>B Schwarz</kbd></div>'
             f'<a class="pill" href="{SLIDES_HTML}">▶ Jetzt starten</a></div>'
             f'<div class="mock"><b>{BRAND}</b><span>Folie 1 von {n_slides}</span></div></div></div></section>'
             + "".join(bands[1:])
             + '<p class="foot">Gelb markierte Stellen wie <mark class="ph">[KI-TOOL]</mark> sind Platzhalter – '
             'vor dem Termin ersetzen. Alle Seiten lassen sich ausdrucken oder als PDF speichern.</p></main>')
    return shell("Übersicht", inner, "", "home")


# --------------------------------------------------------------------------- #
#  Präsentation aus 04_Folien.md
# --------------------------------------------------------------------------- #
SLIDE_HEAD = re.compile(r"^##\s+((?:Folie\s+\d+|Anhang\s+[A-Z]).*)$")
BLOCK_MARK = re.compile(r"^`?\s*(⏱[^`]+?)\s*`?\s*$")
IMG_IDEA = re.compile(r"^\*\((.+)\)\*\s*$")
# "**(Rolle)**" im starken Prompt wird zum farbigen Chip, passend zu den Bauklötzen
BLOCK_TAG = re.compile(r"<strong>\(((Rolle|Kontext|Aufgabe|Format|Beispiel))\)</strong>")


def parse_slides(text: str) -> list[dict]:
    slides, cur, pending_block = [], None, None
    for line in text.splitlines():
        h = SLIDE_HEAD.match(line)
        if h:
            if cur:
                slides.append(cur)
            raw = h.group(1).strip()
            label, _, title = raw.partition("–")
            title = re.sub(r"\s*\*\(.*?\)\*\s*$", "", title or label).strip()
            cur = {"label": label.strip(), "title": title, "block": pending_block,
                   "appendix": raw.startswith("Anhang"), "lines": []}
            pending_block = None
            continue
        b = BLOCK_MARK.match(line)
        if b:
            pending_block = b.group(1).strip()
            continue
        if cur is not None:
            cur["lines"].append(line)
    if cur:
        slides.append(cur)

    for s in slides:
        lines = s.pop("lines")
        while lines and lines[-1].strip() in ("", "---"):
            lines.pop()
        content, notes, ideas, in_notes = [], [], [], False
        for line in lines:
            if line.strip().startswith("**Sprechernotiz"):
                in_notes = True
                rest = re.sub(r"^\*\*Sprechernotiz:?\*\*:?\s*", "", line.strip())
                if rest:
                    notes.append(rest)
                continue
            m = IMG_IDEA.match(line.strip())
            if m and not in_notes:
                ideas.append(m.group(1))
                continue
            (notes if in_notes else content).append(line)
        # Hat die Folie eine fertige Grafik, ist die Bildidee aus dem Markdown erledigt.
        if ideas and s["label"] not in VISUALS:
            notes.append("\n\n**Bildidee:** " + " ".join(ideas))
        # Erste Zeile weglassen, wenn sie nur den Folientitel fett wiederholt
        while content and not content[0].strip():
            content.pop(0)
        if content and content[0].strip().strip("*").strip() == s["title"]:
            content.pop(0)
        s["content"] = BLOCK_TAG.sub(r'<span class="chip \1">\2</span>',
                                     rewrite_links(md_to_html("\n".join(content), breaks=True)[0]))
        s["notes"] = rewrite_links(md_to_html("\n".join(notes), breaks=True)[0])
        # Blockname ohne Uhrzeit, z. B. "Block 3 · Übung 1: Texte schreiben"
        if s["block"]:
            parts = [p.strip() for p in s["block"].lstrip("⏱ ").split("·")]
            s["block_name"] = parts[-1] if len(parts) > 1 else s["block"]
            s["block_time"] = next((p for p in parts if re.match(r"\d:\d\d", p)), "")
            s["block_no"] = parts[0].title() if parts else ""
    return slides


DECK_CSS = FONT_FACE + r"""
:root{--font:"Inter",-apple-system,BlinkMacSystemFont,"SF Pro Display","Helvetica Neue","Segoe UI",Arial,sans-serif;
 --fg:#1d1d1f;--fg2:#424245;--muted:#86868b;--line:#e8e8ed;--accent:#0071e3;--alt:#f5f5f7}
*{box-sizing:border-box}
html,body{margin:0;height:100%;background:#000;overflow:hidden;font-family:var(--font);
 -webkit-font-smoothing:antialiased;letter-spacing:-.015em}
#stage{position:absolute;left:50%;top:50%;width:1600px;height:900px;transform-origin:center center}
.slide{position:absolute;inset:0;display:flex;flex-direction:column;background:#fff;color:var(--fg);
 padding:96px 120px 100px;opacity:0;visibility:hidden;transition:opacity .45s ease,visibility .45s,transform .45s ease;
 transform:scale(.985)}
.slide.active{opacity:1;visibility:visible;transform:none}
.slide .eyebrow{font-size:22px;font-weight:600;color:var(--accent);margin:0 0 14px;letter-spacing:0}
.slide h2{font-size:68px;line-height:1.05;font-weight:700;letter-spacing:-.04em;margin:0 0 44px;color:var(--fg)}
.slide .body{flex:1;min-height:0;display:flex;gap:56px}
.slide .content{font-size:34px;line-height:1.45;color:var(--fg2);flex:1;min-width:0;overflow:hidden}
.slide .visual{flex:none;width:600px;display:flex;align-items:center;justify-content:center}
.slide .visual svg{display:block;width:100%;height:100%;max-height:100%;overflow:visible}
.slide.v-narrow .visual{width:360px}
.slide.v-bottom .body{flex-direction:column;gap:18px}
.slide.v-bottom .visual{width:100%;height:150px}
/* Titel-, Pausen- und Dankefolie: Text links, Bild rechts */
.slide.first.v-hero,.slide.dark.v-hero{flex-direction:row;align-items:center;text-align:left;gap:56px;justify-content:flex-start}
.slide.v-hero .text{flex:1;min-width:0}
.slide.v-hero .visual{width:600px;height:640px}
.slide.first.v-hero h2,.slide.dark.v-hero h2{font-size:92px;line-height:1.08}
.slide.first.v-hero .content,.slide.dark.v-hero .content{font-size:30px}
.slide .content.dense{font-size:28px}
.slide .content.xdense{font-size:23px}
.slide .content strong{color:var(--fg);font-weight:600}
.slide .content p{margin:.3em 0 .55em}
.slide .content ul,.slide .content ol{margin:.2em 0;padding-left:0;list-style:none}
.slide .content ol{counter-reset:n}
.slide .content li{position:relative;padding-left:1.15em;margin:.38em 0}
.slide .content ul>li::before{content:"";position:absolute;left:.1em;top:.62em;width:.32em;height:.32em;border-radius:50%;background:var(--accent)}
.slide .content ol>li{counter-increment:n}
.slide .content ol>li::before{content:counter(n);position:absolute;left:0;top:.05em;font-weight:700;color:var(--accent);font-size:.85em}
.slide .content li li::before{background:var(--muted)}
.slide table{border-collapse:separate;border-spacing:0;width:100%;font-size:.8em;border-radius:20px;overflow:hidden;
 box-shadow:0 0 0 1px var(--line)}
.slide th,.slide td{padding:.5em .8em;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}
.slide tr:last-child td{border-bottom:0}
.slide th{background:var(--alt);color:var(--fg);font-weight:600}
.slide pre{background:var(--alt);border-radius:20px;padding:.7em .9em;font-size:.7em;white-space:pre-wrap;margin:.4em 0;line-height:1.45}
.slide code{font-family:"SF Mono",ui-monospace,Menlo,Consolas,monospace;font-size:.88em}
.slide blockquote{margin:.5em 0;padding:.5em .9em;background:var(--alt);border-radius:20px}
.slide blockquote p{margin:.2em 0}
.footer{position:absolute;bottom:40px;left:120px;right:120px;display:flex;justify-content:space-between;
 font-size:18px;color:var(--muted);font-weight:500}
/* Titel- und Abschnittsfolien */
.slide.first,.slide.dark{background:radial-gradient(120% 120% at 50% 0%,#1d1d1f 0%,#000 60%);color:#f5f5f7;
 justify-content:center;align-items:center;text-align:center}
.slide.first h2,.slide.dark h2{font-size:112px;letter-spacing:-.05em;margin-bottom:28px;
 background:linear-gradient(90deg,#fff 20%,#2997ff 60%,#bf8bff);-webkit-background-clip:text;background-clip:text;color:transparent}
.slide.first .content,.slide.dark .content{flex:none;color:#a1a1a6;font-size:36px;max-width:1150px}
.slide.first .content strong,.slide.dark .content strong{color:#f5f5f7}
.slide.first .content li,.slide.dark .content li{padding-left:0}
.slide.first .content li::before,.slide.dark .content li::before{display:none}
.slide.first .eyebrow,.slide.dark .eyebrow{color:#2997ff}
.slide.first .footer,.slide.dark .footer{color:#6e6e73}
.slide.appendix{background:var(--alt)}
/* Folie 5: grün und orange */
.slide.s-5 th:first-child{background:#dcf5e3;color:#14622b}.slide.s-5 th:last-child{background:#ffead1;color:#8a4e00}
.slide.s-5 td:first-child{background:#f4fbf6}.slide.s-5 td:last-child{background:#fff9f1}
/* Folie 13: Tabellenzeilen in den Farben der Bauklötze */
.slide.s-13 tbody td:first-child{border-left:10px solid var(--c);white-space:nowrap}
.slide.s-13 tbody tr:nth-child(1){--c:#0071e3}.slide.s-13 tbody tr:nth-child(2){--c:#8e5cf7}
.slide.s-13 tbody tr:nth-child(3){--c:#28a745}.slide.s-13 tbody tr:nth-child(4){--c:#f08a00}.slide.s-13 tbody tr:nth-child(5){--c:#e0457b}
/* Folie 14: schwach gegen stark, Bausteine als Chips */
.slide.s-14 th:first-child,.slide.s-14 td:first-child{background:#fbf1f0;width:30%}
.slide.s-14 th:last-child,.slide.s-14 td:last-child{background:#f1faf3}
.chip{display:inline-block;color:#fff;font-weight:600;font-size:.72em;padding:.08em .55em;border-radius:980px;white-space:nowrap}
.chip.Rolle{background:#0071e3}.chip.Kontext{background:#8e5cf7}.chip.Aufgabe{background:#28a745}.chip.Format{background:#f08a00}.chip.Beispiel{background:#e0457b}
/* Animationen. Sie laufen nur auf der aktiven Folie; überall sonst zeigt die Grafik ihren Endzustand. */
@keyframes rise{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}
@keyframes fade{from{opacity:0}to{opacity:1}}
@keyframes pop{0%{opacity:0;transform:scale(.55)}70%{opacity:1;transform:scale(1.07)}100%{transform:none}}
@keyframes drop{0%{opacity:0;transform:translateY(-120px)}70%{opacity:1;transform:translateY(5px)}100%{transform:none}}
@keyframes slide-l{from{opacity:0;transform:translateX(-36px)}to{opacity:1;transform:none}}
@keyframes slide-r{from{opacity:0;transform:translateX(36px)}to{opacity:1;transform:none}}
@keyframes grow{from{opacity:.2;transform:scaleX(0)}to{opacity:1;transform:none}}
@keyframes draw{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}
@keyframes light{0%{opacity:0}40%{opacity:1;filter:brightness(1.35)}100%{opacity:1}}
@keyframes door{from{transform:scaleX(2.4)}to{transform:none}}
@keyframes stamp{0%{opacity:0;transform:scale(2.2) rotate(-14deg)}60%{opacity:1;transform:scale(.94)}100%{transform:none}}
@keyframes tilt{0%{opacity:0;transform:rotate(-7deg) translateY(30px)}100%{opacity:1;transform:rotate(-1.5deg)}}
@keyframes countdown{from{stroke-dashoffset:0}to{stroke-dashoffset:1}}
@keyframes steam{0%{opacity:0;transform:translateY(16px)}40%{opacity:.85}100%{opacity:0;transform:translateY(-22px)}}
@keyframes balance{0%,100%{transform:rotate(-2.2deg)}50%{transform:rotate(2.2deg)}}
@keyframes pulse{0%,100%{transform:none;filter:none}50%{transform:scale(1.035);filter:brightness(1.15)}}
@keyframes pen{0%,100%{transform:translateY(0)}50%{transform:translateY(264px)}}
@keyframes blink{0%,92%,100%{transform:none}96%{transform:scaleY(.1)}}
@keyframes sweep{0%,100%{transform:rotate(-4deg)}50%{transform:rotate(4deg)}}
@keyframes clap{0%,100%{transform:none}50%{transform:scale(.86)}}
@keyframes attn{0%,100%{filter:none}50%{filter:brightness(1.25)}}
.slide svg g[class],.slide svg rect[class]{transform-box:fill-box;transform-origin:center}
.slide.active>h2,.slide.active>.eyebrow,.slide.active .text>h2,.slide.active .text>.eyebrow{animation:rise .55s cubic-bezier(.2,.7,.2,1) both}
.slide.active .step{animation:rise .55s cubic-bezier(.2,.7,.2,1) both;animation-delay:calc(.12s + var(--i,0)*.11s)}
.slide.active .a-rise{animation:rise .6s cubic-bezier(.2,.7,.2,1) both;animation-delay:var(--d,0s)}
.slide.active .a-fade{animation:fade .5s ease both;animation-delay:var(--d,0s)}
.slide.active .a-word{animation:fade .25s ease both;animation-delay:var(--d,0s)}
.slide.active .a-pop{animation:pop .55s cubic-bezier(.2,.7,.2,1) both;animation-delay:var(--d,0s)}
.slide.active .a-drop{animation:drop .6s cubic-bezier(.3,.7,.3,1) both;animation-delay:var(--d,0s)}
.slide.active .a-left{animation:slide-l .55s ease-out both;animation-delay:var(--d,0s)}
.slide.active .a-right{animation:slide-r .55s ease-out both;animation-delay:var(--d,0s)}
.slide.active .a-grow{transform-origin:left center;animation:grow .6s ease-out both;animation-delay:var(--d,0s)}
.a-draw,.a-countdown{stroke-dasharray:1}
.slide.active .a-draw{animation:draw .6s ease-out both;animation-delay:var(--d,0s)}
.slide.active .a-draw.a-slow{animation-duration:1.4s}
.slide.active .a-countdown{animation:countdown 600s linear both}
.slide.active .a-light{animation:light 1s ease both;animation-delay:var(--d,0s)}
.slide.active .a-door{transform-origin:left center;animation:door .9s cubic-bezier(.3,.7,.3,1) both;animation-delay:var(--d,0s)}
.slide.active .a-stamp{animation:stamp .5s cubic-bezier(.3,.7,.3,1) both;animation-delay:var(--d,0s)}
.slide.active .a-tilt{animation:tilt .7s ease-out both;animation-delay:var(--d,0s)}
.slide.active .l-steam{animation:steam 2.8s ease-in-out infinite;animation-delay:var(--d,0s)}
.slide svg g.l-balance{transform-box:view-box;transform-origin:320px 124px}
.slide.active .l-balance{animation:balance 6s ease-in-out infinite}
.slide.active .l-pulse{animation:pulse 2s ease-in-out infinite}
.slide.active .l-pen{animation:pen 3s ease-in-out .7s 1 both}
.slide.active .l-blink{animation:blink 5s ease-in-out infinite}
.slide.active .l-sweep{transform-box:view-box;animation:sweep 7s ease-in-out infinite;animation-delay:var(--d,0s)}
.slide.active .l-clap{animation:clap .9s ease-in-out infinite;animation-delay:var(--d,0s)}
.slide.active .l-attn>rect{animation:attn 1.6s ease-in-out 1.2s 3}
.thumb .slide *,.slide.measuring *{animation:none!important}
@media (prefers-reduced-motion:reduce){.slide,.slide *{animation:none!important;transition:none!important}}
mark.ph{background:#fff4c2;color:#6b5200;padding:0 .2em;border-radius:8px}
.slide.first mark.ph,.slide.dark mark.ph{background:#4a3b00;color:#ffe58a}
body.hide-ph mark.ph{background:none;color:inherit;padding:0}
/* Bedienelemente */
#notes{position:fixed;left:16px;right:16px;bottom:16px;max-height:36vh;overflow:auto;display:none;z-index:5;
 background:rgba(29,29,31,.82);backdrop-filter:blur(24px) saturate(180%);-webkit-backdrop-filter:blur(24px) saturate(180%);
 color:#f5f5f7;border-radius:18px;padding:18px 26px;font-size:17px;line-height:1.55;box-shadow:0 20px 60px rgba(0,0,0,.4)}
body.show-notes #notes{display:block}
#notes h4{margin:0 0 6px;font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:#2997ff}
#notes mark.ph{background:#4a3b00;color:#ffe58a}
#notes a,#pv-notes a{color:#2997ff}
#notes p,#pv-notes p{margin:0 0 .6em}
#help{position:fixed;top:16px;left:50%;transform:translateX(-50%);background:rgba(29,29,31,.82);color:#f5f5f7;
 backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);font-size:14px;padding:14px 22px;border-radius:16px;
 z-index:6;line-height:1.8;display:none;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,.4)}
#help kbd{font:600 12px var(--font);background:#424245;border-radius:6px;padding:2px 7px;margin:0 2px}
#help a{color:#2997ff}
body.show-help #help{display:block}
#progress{position:fixed;left:0;bottom:0;height:3px;background:linear-gradient(90deg,#0071e3,#bf8bff);z-index:4;transition:width .35s ease}
#overview{position:fixed;inset:0;background:rgba(0,0,0,.92);backdrop-filter:blur(20px);overflow:auto;display:none;z-index:7;padding:48px}
body.show-overview #overview{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:18px;align-content:start}
.thumb{position:relative;aspect-ratio:16/9;overflow:hidden;border-radius:12px;background:#fff;box-shadow:0 8px 30px rgba(0,0,0,.35)}
.thumb .inner{position:absolute;left:0;top:0;width:1600px;height:900px;transform-origin:0 0;pointer-events:none}
.thumb .inner .slide{transition:none}
#overview a{color:#f5f5f7;text-decoration:none;font-size:14px;transition:transform .2s;display:block}
#overview a:hover{transform:scale(1.03)}
#overview a .cap{padding:10px 4px 0;line-height:1.3}
#overview a small{display:block;color:#86868b;margin-bottom:2px}
#overview a.cur .thumb{box-shadow:0 0 0 4px #0a84ff}
/* Referentenansicht */
body.presenter{overflow:auto;background:#000;color:#f5f5f7}
body.presenter #stage,body.presenter #progress{display:none}
#pv{display:none}
body.presenter #pv{display:grid;grid-template-columns:1.15fr 1fr;grid-template-rows:auto 1fr;gap:16px;padding:20px;height:100vh}
#pv .row{display:grid;grid-template-columns:1fr 1fr;gap:16px}
#pv .thumb{margin-bottom:14px}
#pv .box{background:#1c1c1e;border-radius:18px;padding:20px 24px}
#pv h3{margin:0 0 10px;font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:#86868b;font-weight:600}
#pv-now{font-size:26px;font-weight:700;letter-spacing:-.03em;line-height:1.15}
#pv-block{color:#2997ff;margin-top:8px;font-weight:500}
#pv-next{font-size:20px;color:#a1a1a6}
#pv-notes{font-size:20px;line-height:1.6;grid-column:2;grid-row:1/span 2;overflow:auto}
#pv-notes p{margin:0 0 .7em}
#pv-notes mark.ph{background:#4a3b00;color:#ffe58a}
#pv-clock{font-size:56px;font-weight:700;font-variant-numeric:tabular-nums;letter-spacing:-.03em}
#pv-clock small{font-size:16px;color:#86868b;display:block;font-weight:500;letter-spacing:0}
#pv button{font:500 15px var(--font);margin:14px 8px 0 0;padding:9px 18px;border-radius:980px;border:0;cursor:pointer;
 background:#2c2c2e;color:#f5f5f7}
#pv button.primary{background:#0a84ff}
@media print{
 html,body{overflow:visible;height:auto;background:#fff}
 #stage{position:static;transform:none!important;width:auto;height:auto}
 .slide{position:relative;opacity:1!important;visibility:visible!important;transform:none!important;width:1600px;height:900px;
  page-break-after:always;zoom:.55;margin-bottom:10px;-webkit-print-color-adjust:exact;print-color-adjust:exact}
 .slide *{animation:none!important}
 #notes,#help,#progress,#overview{display:none!important}
 @page{size:landscape;margin:8mm}
}
"""

DECK_JS = r"""
document.querySelectorAll('template.n').forEach(t=>{const d=document.createElement('div');
 d.id=t.id;d.className='n';d.hidden=true;d.appendChild(t.content.cloneNode(true));t.replaceWith(d);});
const slides=[...document.querySelectorAll('.slide')];
const N=slides.length, notes=document.getElementById('notes'), stage=document.getElementById('stage');
const presenter=location.hash.includes('presenter')||new URLSearchParams(location.search).has('presenter');
let idx=0; let chan=null; try{chan=new BroadcastChannel('ki-tutorial-folien')}catch(e){}

(function(){const re=/\[[A-ZÄÖÜ][A-ZÄÖÜ0-9 \/.,\-–_&:…]{2,}\]/g;
 document.querySelectorAll('.slide, div.n').forEach(r=>{
  const w=document.createTreeWalker(r,NodeFilter.SHOW_TEXT);const ns=[];while(w.nextNode())ns.push(w.currentNode);
  ns.forEach(n=>{re.lastIndex=0;if(n.parentElement.closest('svg')||!re.test(n.nodeValue))return;re.lastIndex=0;const s=document.createElement('span');
   s.innerHTML=n.nodeValue.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(re,m=>`<mark class="ph">${m}</mark>`);
   n.replaceWith(...s.childNodes);});});})();

// Text erscheint Zeile für Zeile: alles Oberste im Inhalt bekommt eine laufende Nummer
slides.forEach(s=>{let i=0;s.querySelectorAll('.content>p,.content>blockquote,.content>pre,.content>ul>li,.content>ol>li,.content tr')
 .forEach(el=>{el.classList.add('step');el.style.setProperty('--i',i++);});});
function fit(s){const c=s.querySelector('.content');if(!c||s.classList.contains('first')||s.classList.contains('dark'))return;
 s.classList.add('measuring');c.classList.remove('dense','xdense');
 if(c.scrollHeight>c.clientHeight+2)c.classList.add('dense');
 if(c.scrollHeight>c.clientHeight+2){c.classList.remove('dense');c.classList.add('xdense');}
 s.classList.remove('measuring');}
function scale(){const k=Math.min(innerWidth/1600,innerHeight/900);stage.style.transform=`translate(-50%,-50%) scale(${k})`;}
addEventListener('resize',scale);scale();
const fitAll=()=>slides.forEach(fit);
(document.fonts?document.fonts.ready:Promise.resolve()).then(fitAll);

function thumb(i,box){box.innerHTML='';if(i<0||i>=N)return;box.className='thumb';
 const inner=document.createElement('div');inner.className='inner';const c=slides[i].cloneNode(true);
 c.classList.add('active');inner.appendChild(c);box.appendChild(inner);
 const sc=()=>{inner.style.transform=`scale(${box.clientWidth/1600})`};sc();requestAnimationFrame(sc);}
addEventListener('resize',()=>{document.querySelectorAll('.thumb .inner').forEach(n=>{n.style.transform=`scale(${n.parentElement.clientWidth/1600})`})});
function noteHTML(i){return document.getElementById('n'+i).innerHTML.trim()||'<em>Keine Notizen</em>';}
function show(i,from){
 idx=Math.max(0,Math.min(N-1,i));
 fit(slides[idx]);
 slides.forEach((s,k)=>s.classList.toggle('active',k===idx));
 notes.innerHTML='<h4>Sprechernotiz</h4>'+noteHTML(idx);
 document.getElementById('progress').style.width=((idx+1)/N*100)+'%';
 history.replaceState(null,'',(presenter?'#presenter-':'#')+(idx+1));
 document.querySelectorAll('#overview a').forEach((a,k)=>a.classList.toggle('cur',k===idx));
 if(presenter)renderPresenter();
 if(chan&&from!=='remote')chan.postMessage({idx});
}
if(chan)chan.onmessage=e=>show(e.data.idx,'remote');

let t0=null;
function renderPresenter(){
 const s=slides[idx], nx=slides[idx+1];
 document.getElementById('pv-now').textContent=`${idx+1} / ${N} · ${s.dataset.title}`;
 document.getElementById('pv-block').textContent=s.dataset.block||'';
 document.getElementById('pv-next').textContent=nx?`${idx+2} · ${nx.dataset.title}`:'— Ende —';
 thumb(idx,document.getElementById('pv-thumb-now'));
 const tn=document.getElementById('pv-thumb-next');if(nx)thumb(idx+1,tn);else{tn.innerHTML='';tn.className='';}
 document.getElementById('pv-notes').innerHTML='<h3>Sprechernotiz</h3>'+noteHTML(idx);
}
function tick(){const now=new Date();
 const clock=now.toLocaleTimeString('de-DE',{hour:'2-digit',minute:'2-digit'});
 let sub='Timer noch nicht gestartet';
 if(t0){const d=Math.floor((now-t0)/1000);sub=`${Math.floor(d/3600)}:${String(Math.floor(d/60)%60).padStart(2,'0')}:${String(d%60).padStart(2,'0')} seit Start`;}
 document.getElementById('pv-clock').innerHTML=`${clock}<small>${sub}</small>`;}
if(presenter){document.body.classList.add('presenter');setInterval(tick,1000);tick();
 document.getElementById('pv-start').onclick=()=>{t0=new Date();tick();};
 document.getElementById('pv-prev').onclick=()=>show(idx-1);
 document.getElementById('pv-nxt').onclick=()=>show(idx+1);}

const ov=document.getElementById('overview');
slides.forEach((s,k)=>{const a=document.createElement('a');a.href='#'+(k+1);
 a.innerHTML=`<div></div><div class="cap"><small>${k+1} · ${s.dataset.blockname||''}</small><strong>${s.dataset.title}</strong></div>`;
 a.onclick=e=>{e.preventDefault();document.body.classList.remove('show-overview');show(k);};ov.appendChild(a);});
function fillOverview(){[...ov.children].forEach((a,k)=>thumb(k,a.firstElementChild));}

addEventListener('keydown',e=>{
 if(e.ctrlKey||e.metaKey||e.altKey)return;
 const k=e.key, B=document.body.classList;
 if(['ArrowRight','ArrowDown','PageDown',' ','Enter'].includes(k)){e.preventDefault();show(idx+1);}
 else if(['ArrowLeft','ArrowUp','PageUp','Backspace'].includes(k)){e.preventDefault();show(idx-1);}
 else if(k==='Home')show(0); else if(k==='End')show(N-1);
 else if(k==='n'||k==='N')B.toggle('show-notes');
 else if(k==='h'||k==='H')B.toggle('hide-ph');
 else if(k==='o'||k==='O'||(k==='Escape'&&B.contains('show-overview'))){B.toggle('show-overview');if(B.contains('show-overview'))fillOverview();}
 else if(k==='?')B.toggle('show-help');
 else if(k==='f'||k==='F'){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();}
 else if(k==='p'||k==='P'){window.open(location.pathname+'#presenter-'+(idx+1),'referent','width=1280,height=800');}
 else if(k==='b'||k==='B'||k==='.'){stage.style.visibility=stage.style.visibility==='hidden'?'':'hidden';}
});
let tx=null;addEventListener('touchstart',e=>tx=e.touches[0].clientX);
addEventListener('touchend',e=>{if(tx===null)return;const d=e.changedTouches[0].clientX-tx;if(Math.abs(d)>50)show(idx+(d<0?1:-1));tx=null;});
stage.addEventListener('click',e=>{if(e.target.closest('a'))return;show(idx+(e.clientX>innerWidth/3?1:-1));});

const m=location.hash.match(/(\d+)$/);show(m?parseInt(m[1])-1:0);
if(!presenter){let seen=false;try{seen=sessionStorage.getItem('helpShown')}catch(e){}
 if(!seen){const cl=document.body.classList;cl.add('show-help');setTimeout(()=>cl.remove('show-help'),5000);
  try{sessionStorage.setItem('helpShown','1')}catch(e){}}}
"""


def build_deck(slides: list[dict], deck_title: str) -> str:
    sec, tpl = [], []
    for i, s in enumerate(slides):
        cls = ["slide", f"s-{esc(s['label'].split()[-1])}"]
        layout, graphic = VISUALS.get(s["label"], (None, ""))
        if layout:
            cls += ["has-visual", f"v-{layout}"]
        if i == 0:
            cls.append("first")
        elif re.search(r"\bPause\b|Danke", s["title"]):
            cls.append("dark")
        if s["appendix"]:
            cls.append("appendix")
        eyebrow = s.get("block_name", "") if s["block"] else ""
        if s["appendix"]:
            eyebrow = s["label"]
        if i == 0:
            eyebrow = ""
        head = (f'<p class="eyebrow">{esc(eyebrow)}</p>' if eyebrow else "") + f'<h2>{esc(s["title"])}</h2>'
        visual = f'<div class="visual">{graphic}</div>' if graphic else ""
        content = f'<div class="content">{s["content"]}</div>'
        inner = (f'<div class="text">{head}{content}</div>{visual}' if layout == "hero"
                 else f'{head}<div class="body">{content}{visual}</div>')
        sec.append(
            f'<section class="{" ".join(cls)}" data-title="{esc(s["title"])}" data-block="{esc(s["block"] or "")}"'
            f' data-blockname="{esc(s.get("block_name", ""))}">{inner}'
            f'<div class="footer"><span>{esc(deck_title)}</span><span>{i + 1}</span></div></section>')
        tpl.append(f'<template class="n" id="n{i}">{s["notes"]}</template>')
    # Blocknamen auch auf Folgefolien durchreichen (für Übersicht)
    return f"""<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(deck_title)} · Präsentation</title>{FONTS}
<link rel="stylesheet" href="assets/deck.css"></head>
<body>
<div id="stage">{''.join(sec)}</div>
{''.join(tpl)}
<div id="notes"></div><div id="progress"></div><div id="overview"></div>
<div id="help"><kbd>→</kbd> weiter <kbd>←</kbd> zurück <kbd>F</kbd> Vollbild <kbd>N</kbd> Notizen
<kbd>P</kbd> Referentenansicht <kbd>O</kbd> Übersicht <kbd>B</kbd> Schwarz <kbd>H</kbd> Platzhalter <kbd>?</kbd> Hilfe
· <a href="index.html">Zur Übersicht</a></div>
<div id="pv">
 <div class="box"><h3>Aktuelle Folie</h3><div id="pv-thumb-now"></div><div id="pv-now"></div><div id="pv-block"></div>
  <button id="pv-prev">‹ Zurück</button><button id="pv-nxt" class="primary">Weiter ›</button></div>
 <div class="box" id="pv-notes"></div>
 <div class="row"><div class="box"><h3>Nächste Folie</h3><div id="pv-thumb-next"></div><div id="pv-next"></div></div>
 <div class="box"><h3>Uhrzeit</h3><div id="pv-clock"></div><button id="pv-start">⏱ Timer starten</button></div></div>
</div>
<script src="assets/deck.js"></script></body></html>"""


# --------------------------------------------------------------------------- #
#  Build
# --------------------------------------------------------------------------- #
def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    for name, data in (("style.css", DOC_CSS), ("doc.js", DOC_JS), ("deck.css", DECK_CSS), ("deck.js", DECK_JS)):
        (OUT / "assets" / name).write_text(data, encoding="utf-8")
    if FONT_DIR.exists():
        shutil.copytree(FONT_DIR, OUT / "assets" / "fonts")

    docs = load_docs()
    for d in docs:
        target = OUT / d.href
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(doc_page(d, docs), encoding="utf-8")

    for p in source_files():
        if p.suffix.lower() in COPY_SUFFIXES:
            target = OUT / p.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, target)

    # Grafiken zusätzlich als Dateien, zum Einfügen in PowerPoint oder Google Präsentationen
    (OUT / "assets" / "folien").mkdir()
    for label, (_, graphic) in VISUALS.items():
        (OUT / "assets" / "folien" / f"{label.lower().replace(' ', '-')}.svg").write_text(graphic, encoding="utf-8")

    n_slides = 0
    slides_src = ROOT / SLIDES_MD
    if slides_src.exists():
        text = slides_src.read_text(encoding="utf-8")
        slides = parse_slides(text)
        # Blockname für Übersicht auf alle Folien eines Blocks übertragen
        last = ""
        for s in slides:
            last = s.get("block_name", last)
            s.setdefault("block_name", last)
        n_slides = len(slides)
        deck_title = re.sub(r"^Folien:\s*", "", first_heading(text, BRAND))
        (OUT / SLIDES_HTML).write_text(build_deck(slides, deck_title), encoding="utf-8")

    (OUT / "index.html").write_text(index_page(docs, n_slides), encoding="utf-8")
    print(f"✓ {len(docs)} Seiten, {n_slides} Folien → {OUT}/index.html")


def snapshot() -> dict:
    return {str(p): p.stat().st_mtime for p in source_files()} | {"self": Path(__file__).stat().st_mtime,
                                                                 "visuals": (ROOT / "slide_visuals.py").stat().st_mtime}


def serve(port: int) -> None:
    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):  # keine Zeile pro Anfrage
            pass

    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(QuietHandler, directory=str(OUT)))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    print(f"→ Übersicht:     http://localhost:{port}/")
    print(f"→ Präsentation:  http://localhost:{port}/{SLIDES_HTML}")
    print("  Änderungen an den .md-Dateien werden automatisch übernommen (Seite neu laden). Strg+C beendet.")
    last = snapshot()
    try:
        while True:
            time.sleep(1)
            now = snapshot()
            if now != last:
                last = now
                try:
                    build()
                except Exception as exc:  # weiterlaufen, auch wenn eine Datei kaputt ist
                    print(f"✗ Fehler beim Bauen: {exc}")
    except KeyboardInterrupt:
        httpd.shutdown()


def main() -> None:
    ap = argparse.ArgumentParser(description="Markdown-Tutorial in HTML umwandeln")
    ap.add_argument("--serve", action="store_true", help="lokal anzeigen und bei Änderungen neu bauen")
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()
    build()
    if args.serve:
        serve(args.port)


if __name__ == "__main__":
    main()
