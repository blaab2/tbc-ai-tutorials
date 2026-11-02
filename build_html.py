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

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "html"
SLIDES_MD = "04_Folien.md"
SLIDES_HTML = "04_Folien_Praesentation.html"
SKIP_DIRS = {"html", ".venv", ".tools", ".git", "node_modules"}
COPY_SUFFIXES = {".txt", ".csv", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".pdf"}

MD_EXTENSIONS = [
    "extra",            # Tabellen, Code-Blöcke, Fußnoten, attr_list …
    "sane_lists",
    "toc",
    "pymdownx.tasklist",
    "pymdownx.tilde",
    "pymdownx.magiclink",
]
MD_CONFIG = {
    "toc": {"permalink": False, "toc_depth": "2-3"},
    "pymdownx.tasklist": {"custom_checkbox": True, "clickable_checkbox": True},
}


# --------------------------------------------------------------------------- #
#  Hilfsfunktionen
# --------------------------------------------------------------------------- #
def md_to_html(text: str) -> tuple[str, str]:
    md = markdown.Markdown(extensions=MD_EXTENSIONS, extension_configs=MD_CONFIG)
    body = md.convert(text)
    return body, getattr(md, "toc", "")


def rewrite_links(body: str) -> str:
    """Relative Links auf .md-Dateien zeigen danach auf die .html-Version."""
    def repl(m: re.Match) -> str:
        href = m.group(2)
        if re.match(r"^[a-z]+:", href) or href.startswith("#"):
            return m.group(0)
        href = re.sub(r"\.md(#|$)", r".html\1", href)
        return f'{m.group(1)}"{href}"'
    return re.sub(r'(href=)"([^"]+)"', repl, body)


def source_files() -> list[Path]:
    files = []
    for p in sorted(ROOT.rglob("*")):
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        if p.is_file():
            files.append(p)
    return files


def first_heading(text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else fallback


def rel_prefix(rel: Path) -> str:
    return "../" * (len(rel.parts) - 1)


def nav_items(md_files: list[Path]) -> list[tuple[str, str, str]]:
    items = []
    for p in md_files:
        rel = p.relative_to(ROOT)
        group = rel.parts[0] if len(rel.parts) > 1 else ""
        title = first_heading(p.read_text(encoding="utf-8"), p.stem)
        items.append((group, str(rel.with_suffix(".html")), title))
    return items


def nav_html(items, current: str, prefix: str) -> str:
    out, last_group = [], None
    out.append(f'<a class="nav-home" href="{prefix}index.html">🏠 Übersicht</a>')
    out.append(f'<a class="nav-deck" href="{prefix}{SLIDES_HTML}">▶ Präsentation starten</a>')
    for group, href, title in items:
        if group != last_group:
            if group:
                label = re.sub(r"^\d+_", "", group).replace("_", " ").replace("Uebungen", "Übungen")
                out.append(f'<div class="nav-group">{html.escape(label)}</div>')
            last_group = group
        cls = ' class="active"' if href == current else ""
        out.append(f'<a{cls} href="{prefix}{href}">{html.escape(title)}</a>')
    return "\n".join(out)


# --------------------------------------------------------------------------- #
#  Dokumentseiten
# --------------------------------------------------------------------------- #
DOC_CSS = r"""
:root{--bg:#fbfaf7;--fg:#1f2328;--muted:#5d6670;--line:#e3e0d8;--accent:#1d5fa8;
--accent-bg:#e8f0fa;--code:#f3f1ec;--side:#f3f1ec;--ph:#fff1a8;--ph-fg:#5a4500}
@media (prefers-color-scheme:dark){:root{--bg:#16181c;--fg:#e6e6e3;--muted:#9aa1a9;
--line:#2c3036;--accent:#7fb2ee;--accent-bg:#1c2a3b;--code:#1f2227;--side:#1b1d22;
--ph:#5a4a00;--ph-fg:#fff3b0}}
*{box-sizing:border-box}
html{font-size:18px}
body{margin:0;background:var(--bg);color:var(--fg);
font:1rem/1.65 "Segoe UI",system-ui,-apple-system,Roboto,"Helvetica Neue",Arial,sans-serif}
.layout{display:grid;grid-template-columns:280px minmax(0,1fr);min-height:100vh}
aside{background:var(--side);border-right:1px solid var(--line);padding:1.2rem .9rem;
position:sticky;top:0;height:100vh;overflow:auto;font-size:.85rem}
aside a{display:block;padding:.35rem .6rem;border-radius:6px;color:var(--fg);text-decoration:none}
aside a:hover{background:var(--accent-bg)}
aside a.active{background:var(--accent);color:#fff}
.nav-home{font-weight:600}
.nav-deck{font-weight:600;color:var(--accent)!important;margin-bottom:.6rem}
.nav-group{margin:1rem .6rem .3rem;font-size:.72rem;text-transform:uppercase;
letter-spacing:.08em;color:var(--muted)}
main{max-width:900px;padding:2.5rem 3rem 5rem;width:100%}
h1{font-size:2rem;line-height:1.2;margin:.2rem 0 1.2rem}
h2{font-size:1.45rem;margin:2.4rem 0 .8rem;padding-top:.6rem;border-top:1px solid var(--line)}
h3{font-size:1.15rem;margin:1.8rem 0 .5rem}
a{color:var(--accent)}
table{border-collapse:collapse;width:100%;margin:1rem 0;font-size:.92rem;display:block;overflow-x:auto}
th,td{border:1px solid var(--line);padding:.45rem .65rem;text-align:left;vertical-align:top}
th{background:var(--accent-bg)}
code{background:var(--code);padding:.1em .35em;border-radius:4px;font-size:.88em}
pre{background:var(--code);padding:1rem 1.1rem;border-radius:8px;overflow:auto;position:relative;
border:1px solid var(--line);white-space:pre-wrap}
pre code{background:none;padding:0;font-size:.88rem}
.copy{position:absolute;top:.5rem;right:.5rem;font:inherit;font-size:.75rem;cursor:pointer;
border:1px solid var(--line);background:var(--bg);color:var(--fg);border-radius:6px;padding:.2rem .6rem}
blockquote{margin:1rem 0;padding:.6rem 1rem;border-left:4px solid var(--accent);
background:var(--accent-bg);border-radius:0 8px 8px 0}
blockquote p{margin:.3rem 0}
hr{border:0;border-top:1px solid var(--line);margin:2rem 0}
mark.ph{background:var(--ph);color:var(--ph-fg);padding:0 .2em;border-radius:3px}
.task-list-item{list-style:none}
.task-list-item input{margin-right:.4rem}
.toolbar{display:flex;gap:.6rem;justify-content:flex-end;margin-bottom:.5rem}
.toolbar button{font:inherit;font-size:.8rem;cursor:pointer;border:1px solid var(--line);
background:var(--bg);color:var(--fg);border-radius:6px;padding:.3rem .8rem}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1rem;margin:1.5rem 0}
.card{border:1px solid var(--line);border-radius:10px;padding:1rem 1.1rem;text-decoration:none;
color:var(--fg);background:var(--bg)}
.card:hover{border-color:var(--accent)}
.card small{color:var(--muted);display:block}
.card.big{background:var(--accent);color:#fff;border-color:var(--accent)}
.card.big small{color:#dfe9f7}
.menu-btn{display:none}
@media (max-width:900px){
 .layout{grid-template-columns:1fr}
 aside{position:fixed;inset:0 auto 0 0;width:280px;z-index:10;transform:translateX(-100%);transition:.2s}
 body.nav-open aside{transform:none}
 .menu-btn{display:inline-block}
 main{padding:1.5rem 16px 4rem}
}
@media print{
 html{font-size:11pt}
 aside,.toolbar,.copy{display:none!important}
 .layout{display:block}
 main{max-width:none;padding:0}
 body{background:#fff;color:#000}
 h2{break-after:avoid;border-top:0}
 pre,table,blockquote{break-inside:avoid}
 a{color:#000;text-decoration:none}
 mark.ph{background:none;color:#000;font-weight:600}
}
"""

DOC_JS = r"""
// Platzhalter wie [KI-TOOL] hervorheben, damit man sie vor dem Termin ersetzt
(function(){
  const re=/\[[A-ZÄÖÜ][A-ZÄÖÜ0-9 \/.\-–_&]{2,}\]/g;
  const walk=document.createTreeWalker(document.querySelector('main'),NodeFilter.SHOW_TEXT);
  const nodes=[];while(walk.nextNode())nodes.push(walk.currentNode);
  nodes.forEach(n=>{ if(!re.test(n.nodeValue))return; re.lastIndex=0;
    const span=document.createElement('span');
    span.innerHTML=n.nodeValue.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(re,m=>`<mark class="ph">${m}</mark>`);
    n.replaceWith(...span.childNodes);});
})();
// Kopier-Knopf an jedem Code-/Prompt-Block
document.querySelectorAll('main pre').forEach(pre=>{
  const b=document.createElement('button');b.className='copy';b.textContent='Kopieren';
  b.onclick=()=>{navigator.clipboard.writeText(pre.innerText.replace(/Kopieren$/,'').trim())
    .then(()=>{b.textContent='✓ Kopiert';setTimeout(()=>b.textContent='Kopieren',1500)});};
  pre.appendChild(b);});
document.querySelector('.menu-btn')?.addEventListener('click',()=>document.body.classList.toggle('nav-open'));
"""


def page(title: str, body: str, nav: str, prefix: str) -> str:
    return f"""<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{prefix}assets/style.css"></head>
<body><div class="layout"><aside>{nav}</aside>
<main><div class="toolbar"><button class="menu-btn">☰ Menü</button>
<button onclick="window.print()">🖨 Drucken / PDF</button></div>
{body}</main></div>
<script src="{prefix}assets/doc.js"></script></body></html>"""


def build_index(items, md_files) -> str:
    cards = [f'<a class="card big" href="{SLIDES_HTML}"><strong>▶ Präsentation starten</strong>'
             f'<small>Vollbild-Folien · ← → blättern · N Notizen · P Referentenansicht</small></a>']
    for (group, href, title), p in zip(items, md_files):
        hint = p.relative_to(ROOT).as_posix()
        cards.append(f'<a class="card" href="{href}"><strong>{html.escape(title)}</strong>'
                     f'<small>{html.escape(hint)}</small></a>')
    extras = []
    for p in source_files():
        if p.suffix.lower() in {".txt", ".csv"}:
            rel = p.relative_to(ROOT).as_posix()
            extras.append(f'<li><a href="{rel}" download>{html.escape(p.name)}</a></li>')
    body = ("<h1>KI im Arbeitsalltag – Tutorial-Materialien</h1>"
            "<p>Alle Materialien als Webseiten. Jede Seite lässt sich über „Drucken / PDF“ ausdrucken. "
            "Gelb markierte Stellen wie <mark class=\"ph\">[KI-TOOL]</mark> sind Platzhalter, "
            "die du vor dem Termin ersetzen solltest.</p>"
            f'<div class="cards">{"".join(cards)}</div>'
            "<h2>Beispieldateien zum Herunterladen</h2>"
            "<p>Für die Übungen: diese Dateien laden die Teilnehmenden im KI-Assistenten hoch.</p>"
            f"<ul>{''.join(extras)}</ul>")
    return body


# --------------------------------------------------------------------------- #
#  Präsentation aus 04_Folien.md
# --------------------------------------------------------------------------- #
SLIDE_HEAD = re.compile(r"^##\s+((?:Folie\s+\d+|Anhang\s+[A-Z]).*)$")
BLOCK_MARK = re.compile(r"^`?\s*(⏱[^`]+?)\s*`?\s*$")
IMG_IDEA = re.compile(r"^\*\((.+)\)\*\s*$")


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
        if ideas:
            notes.append("\n\n**Bildidee:** " + " ".join(ideas))
        s["content"] = rewrite_links(md_to_html("\n".join(content))[0])
        s["notes"] = rewrite_links(md_to_html("\n".join(notes))[0])
    return slides


DECK_CSS = r"""
:root{--bg:#10233f;--fg:#fff;--accent:#ffcc4d;--card:#fff;--card-fg:#1f2328;--muted:#5d6670;
--line:#e3e0d8;--accent-bg:#e8f0fa;--blue:#1d5fa8}
*{box-sizing:border-box}
html,body{margin:0;height:100%;background:#0b1626;overflow:hidden;
font-family:"Segoe UI",system-ui,-apple-system,Roboto,"Helvetica Neue",Arial,sans-serif}
#stage{position:absolute;left:50%;top:50%;width:1600px;height:900px;transform-origin:center center}
.slide{position:absolute;inset:0;display:none;background:var(--card);color:var(--card-fg);
padding:70px 100px 90px;flex-direction:column;border-radius:4px;overflow:hidden}
.slide.active{display:flex}
.slide.first{background:linear-gradient(135deg,#10233f,#1d5fa8);color:#fff;justify-content:center}
.slide.first h2{font-size:84px}
.slide.first .content{font-size:38px}
.slide h2{font-size:58px;line-height:1.15;margin:0 0 36px;color:var(--blue)}
.slide.first h2{color:#fff}
.slide .content{font-size:34px;line-height:1.45;flex:1;overflow:hidden}
.slide .content.dense{font-size:27px}
.slide .content.xdense{font-size:22px}
.slide ul,.slide ol{margin:.2em 0;padding-left:1.2em}
.slide li{margin:.3em 0}
.slide p{margin:.4em 0}
.slide table{border-collapse:collapse;width:100%;font-size:.85em}
.slide th,.slide td{border:2px solid var(--line);padding:.35em .6em;text-align:left;vertical-align:top}
.slide th{background:var(--accent-bg)}
.slide pre{background:#f3f1ec;border-radius:10px;padding:.6em .8em;font-size:.72em;white-space:pre-wrap;margin:.4em 0}
.slide code{font-size:.9em}
.slide blockquote{margin:.4em 0;padding:.3em .8em;border-left:8px solid var(--blue);background:var(--accent-bg)}
.block{position:absolute;top:24px;right:40px;font-size:20px;color:var(--muted);
background:#f3f1ec;padding:6px 16px;border-radius:30px}
.slide.first .block{background:rgba(255,255,255,.15);color:#fff}
.footer{position:absolute;bottom:24px;left:100px;right:40px;display:flex;justify-content:space-between;
font-size:20px;color:var(--muted)}
.slide.first .footer{color:#cfe0f5}
.slide.appendix{background:#f6f5f1}
mark.ph{background:#fff1a8;color:#5a4500;padding:0 .15em;border-radius:4px}
body.hide-ph mark.ph{background:none;color:inherit;padding:0}
#notes{position:fixed;left:0;right:0;bottom:0;max-height:38vh;overflow:auto;display:none;
background:#fffdf3;color:#222;border-top:4px solid var(--accent);padding:14px 28px;font-size:17px;line-height:1.5;z-index:5}
body.show-notes #notes{display:block}
#notes h4{margin:0 0 6px;font-size:14px;text-transform:uppercase;letter-spacing:.06em;color:#8a6d00}
#help{position:fixed;top:12px;left:12px;background:rgba(0,0,0,.75);color:#fff;font-size:14px;
padding:10px 14px;border-radius:8px;z-index:6;line-height:1.6;display:none}
body.show-help #help{display:block}
#progress{position:fixed;left:0;bottom:0;height:5px;background:var(--accent);z-index:4;transition:width .2s}
#overview{position:fixed;inset:0;background:#0b1626;overflow:auto;display:none;z-index:7;padding:30px}
body.show-overview #overview{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;align-content:start}
#overview a{background:#fff;color:#1f2328;text-decoration:none;border-radius:8px;padding:14px;font-size:15px}
#overview a small{display:block;color:#5d6670}
#overview a.cur{outline:4px solid var(--accent)}
/* Referentenansicht */
body.presenter{overflow:auto;background:#1b1d22;color:#eee}
body.presenter #stage,body.presenter #progress{display:none}
#pv{display:none}
body.presenter #pv{display:grid;grid-template-columns:1.1fr 1fr;gap:24px;padding:24px;min-height:100vh}
#pv .box{background:#25282e;border-radius:10px;padding:18px 22px}
#pv h3{margin:0 0 10px;font-size:13px;text-transform:uppercase;letter-spacing:.08em;color:#9aa1a9}
#pv-now{font-size:30px;font-weight:600}
#pv-next{font-size:20px;color:#bbb}
#pv-notes{font-size:20px;line-height:1.55;grid-row:span 3}
#pv-notes mark.ph{background:#5a4a00;color:#fff3b0}
#pv-clock{font-size:44px;font-variant-numeric:tabular-nums}
#pv-clock small{font-size:16px;color:#9aa1a9;display:block}
#pv button{font:inherit;font-size:15px;margin:6px 6px 0 0;padding:6px 14px;border-radius:6px;border:0;cursor:pointer}
@media print{
 html,body{overflow:visible;height:auto;background:#fff}
 #stage{position:static;transform:none!important;width:auto;height:auto}
 .slide{display:flex!important;position:relative;width:1600px;height:900px;page-break-after:always;
  zoom:.55;border:1px solid #ccc;margin-bottom:10px}
 #notes,#help,#progress,#overview{display:none!important}
 @page{size:landscape;margin:8mm}
}
"""

DECK_JS = r"""
const slides=[...document.querySelectorAll('.slide')];
const N=slides.length, notes=document.getElementById('notes'), stage=document.getElementById('stage');
const presenter=location.hash.includes('presenter')||new URLSearchParams(location.search).has('presenter');
let idx=0; let chan=null; try{chan=new BroadcastChannel('ki-tutorial-folien')}catch(e){}

// Platzhalter markieren
(function(){const re=/\[[A-ZÄÖÜ][A-ZÄÖÜ0-9 \/.\-–_&]{2,}\]/g;
 document.querySelectorAll('.slide, div.n').forEach(r=>{
  const w=document.createTreeWalker(r,NodeFilter.SHOW_TEXT);const ns=[];while(w.nextNode())ns.push(w.currentNode);
  ns.forEach(n=>{if(!re.test(n.nodeValue))return;re.lastIndex=0;const s=document.createElement('span');
   s.innerHTML=n.nodeValue.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(re,m=>`<mark class="ph">${m}</mark>`);
   n.replaceWith(...s.childNodes);});});})();

// Schriftgröße automatisch verkleinern, wenn eine Folie zu voll ist
function fit(s){const c=s.querySelector('.content');if(!c)return;
 c.classList.remove('dense','xdense');
 if(c.scrollHeight>c.clientHeight+2)c.classList.add('dense');
 if(c.scrollHeight>c.clientHeight+2){c.classList.remove('dense');c.classList.add('xdense');}}

function scale(){const k=Math.min(innerWidth/1600,innerHeight/900);
 stage.style.transform=`translate(-50%,-50%) scale(${k})`;}
addEventListener('resize',scale);scale();

function noteHTML(i){return document.getElementById('n'+i).innerHTML||'<em>Keine Notizen</em>';}
function show(i,from){
 idx=Math.max(0,Math.min(N-1,i));
 slides.forEach((s,k)=>s.classList.toggle('active',k===idx));
 fit(slides[idx]);
 notes.innerHTML='<h4>Sprechernotiz</h4>'+noteHTML(idx);
 document.getElementById('progress').style.width=((idx+1)/N*100)+'%';
 history.replaceState(null,'',(presenter?'#presenter-':'#')+(idx+1));
 document.querySelectorAll('#overview a').forEach((a,k)=>a.classList.toggle('cur',k===idx));
 if(presenter)renderPresenter();
 if(chan&&from!=='remote')chan.postMessage({idx});
}
if(chan)chan.onmessage=e=>show(e.data.idx,'remote');

// Referentenansicht
let t0=null;
function renderPresenter(){
 const s=slides[idx], nx=slides[idx+1];
 document.getElementById('pv-now').textContent=`${idx+1}/${N} · ${s.dataset.title}`;
 document.getElementById('pv-block').textContent=s.dataset.block||'';
 document.getElementById('pv-next').textContent=nx?`${idx+2} · ${nx.dataset.title}`:'— Ende —';
 document.getElementById('pv-notes').innerHTML='<h3>Sprechernotiz</h3>'+noteHTML(idx);
}
function tick(){const el=document.getElementById('pv-clock');const now=new Date();
 const clock=now.toLocaleTimeString('de-DE',{hour:'2-digit',minute:'2-digit'});
 let el2='Timer läuft nicht';
 if(t0){const d=Math.floor((now-t0)/1000);el2=`${Math.floor(d/3600)}:${String(Math.floor(d/60)%60).padStart(2,'0')}:${String(d%60).padStart(2,'0')} seit Start`;}
 el.innerHTML=`${clock}<small>${el2}</small>`;}
if(presenter){document.body.classList.add('presenter');setInterval(tick,1000);tick();
 document.getElementById('pv-start').onclick=()=>{t0=new Date();tick();};
 document.getElementById('pv-prev').onclick=()=>show(idx-1);
 document.getElementById('pv-nxt').onclick=()=>show(idx+1);}

// Übersicht
const ov=document.getElementById('overview');
slides.forEach((s,k)=>{const a=document.createElement('a');a.href='#'+(k+1);
 a.innerHTML=`<strong>${k+1}. ${s.dataset.title}</strong><small>${s.dataset.block||''}</small>`;
 a.onclick=e=>{e.preventDefault();document.body.classList.remove('show-overview');show(k);};ov.appendChild(a);});

addEventListener('keydown',e=>{
 if(e.ctrlKey||e.metaKey||e.altKey)return;
 const k=e.key;
 if(['ArrowRight','ArrowDown','PageDown',' ','Enter'].includes(k)){e.preventDefault();show(idx+1);}
 else if(['ArrowLeft','ArrowUp','PageUp','Backspace'].includes(k)){e.preventDefault();show(idx-1);}
 else if(k==='Home')show(0); else if(k==='End')show(N-1);
 else if(k==='n'||k==='N')document.body.classList.toggle('show-notes');
 else if(k==='h'||k==='H')document.body.classList.toggle('hide-ph');
 else if(k==='o'||k==='O'||k==='Escape'&&document.body.classList.contains('show-overview'))document.body.classList.toggle('show-overview');
 else if(k==='?')document.body.classList.toggle('show-help');
 else if(k==='f'||k==='F'){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();}
 else if(k==='p'||k==='P'){window.open(location.pathname+'#presenter-'+(idx+1),'referent','width=1200,height=800');}
 else if(k==='b'||k==='B'||k==='.'){stage.style.visibility=stage.style.visibility==='hidden'?'':'hidden';}
});
let tx=null;addEventListener('touchstart',e=>tx=e.touches[0].clientX);
addEventListener('touchend',e=>{if(tx===null)return;const d=e.changedTouches[0].clientX-tx;if(Math.abs(d)>50)show(idx+(d<0?1:-1));tx=null;});
stage.addEventListener('click',e=>{if(e.target.closest('a'))return;show(idx+(e.clientX>innerWidth/3?1:-1));});

const m=location.hash.match(/(\d+)$/);show(m?parseInt(m[1])-1:0);
if(!presenter&&!sessionStorage.getItem('helpShown')){document.body.classList.add('show-help');
 setTimeout(()=>document.body.classList.remove('show-help'),5000);try{sessionStorage.setItem('helpShown','1')}catch(e){}}
"""


def build_deck(slides: list[dict], deck_title: str) -> str:
    sec, tpl = [], []
    for i, s in enumerate(slides):
        cls = ["slide"]
        if i == 0:
            cls.append("first")
        if s["appendix"]:
            cls.append("appendix")
        block = html.escape(s["block"] or "")
        sec.append(
            f'<section class="{" ".join(cls)}" data-title="{html.escape(s["title"], quote=True)}"'
            f' data-block="{block}">'
            + (f'<div class="block">{block}</div>' if block else "")
            + f'<h2>{html.escape(s["title"])}</h2><div class="content">{s["content"]}</div>'
            f'<div class="footer"><span>{html.escape(deck_title)}</span><span>{html.escape(s["label"])}</span></div>'
            "</section>")
        tpl.append(f'<template class="n" id="n{i}">{s["notes"]}</template>')
    return f"""<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(deck_title)} – Präsentation</title>
<link rel="stylesheet" href="assets/deck.css"></head>
<body>
<div id="stage">{''.join(sec)}</div>
{''.join(tpl)}
<div id="notes"></div><div id="progress"></div><div id="overview"></div>
<div id="help"><strong>Tastatur</strong><br>
→ / Leertaste: weiter · ←: zurück · F: Vollbild<br>
N: Sprechernotizen ein/aus · P: Referentenansicht (2. Fenster)<br>
O: Folienübersicht · B: Bildschirm schwarz · H: Platzhalter-Markierung aus<br>
?: diese Hilfe · <a style="color:#ffcc4d" href="index.html">zurück zur Übersicht</a></div>
<div id="pv">
 <div class="box"><h3>Aktuelle Folie</h3><div id="pv-now"></div><div id="pv-block" style="color:#ffcc4d;margin-top:6px"></div>
  <button id="pv-prev">← Zurück</button><button id="pv-nxt">Weiter →</button></div>
 <div class="box" id="pv-notes"></div>
 <div class="box"><h3>Nächste Folie</h3><div id="pv-next"></div></div>
 <div class="box"><h3>Uhrzeit</h3><div id="pv-clock"></div><button id="pv-start">⏱ Timer starten</button></div>
</div>
<script>
// Notiz-Templates in lesbare Container umwandeln
document.querySelectorAll('template.n').forEach(t=>{{const d=document.createElement('div');
 d.id=t.id;d.className='n';d.hidden=true;d.appendChild(t.content.cloneNode(true));t.replaceWith(d);}});
</script>
<script src="assets/deck.js"></script></body></html>"""


# --------------------------------------------------------------------------- #
#  Build
# --------------------------------------------------------------------------- #
def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    (OUT / "assets/style.css").write_text(DOC_CSS, encoding="utf-8")
    (OUT / "assets/doc.js").write_text(DOC_JS, encoding="utf-8")
    (OUT / "assets/deck.css").write_text(DECK_CSS, encoding="utf-8")
    (OUT / "assets/deck.js").write_text(DECK_JS, encoding="utf-8")

    files = source_files()
    md_files = [p for p in files if p.suffix.lower() == ".md"]
    # README zuerst, danach nach Dateinamen sortiert
    md_files.sort(key=lambda p: (len(p.relative_to(ROOT).parts) > 1, "README" not in p.name.upper(), str(p)))
    items = nav_items(md_files)

    for p, (_, href, title) in zip(md_files, items):
        rel = p.relative_to(ROOT)
        prefix = rel_prefix(rel)
        body, _toc = md_to_html(p.read_text(encoding="utf-8"))
        body = rewrite_links(body)
        if rel.name == SLIDES_MD:
            body = (f'<p><a class="card big" style="display:inline-block" href="{prefix}{SLIDES_HTML}">'
                    f'▶ Als Präsentation öffnen</a></p>') + body
        target = OUT / rel.with_suffix(".html")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page(title, body, nav_html(items, href, prefix), prefix), encoding="utf-8")

    for p in files:
        if p.suffix.lower() in COPY_SUFFIXES:
            target = OUT / p.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, target)

    index_body = build_index(items, md_files)
    (OUT / "index.html").write_text(page("Übersicht", index_body, nav_html(items, "index.html", ""), ""),
                                    encoding="utf-8")

    slides_src = ROOT / SLIDES_MD
    n_slides = 0
    if slides_src.exists():
        text = slides_src.read_text(encoding="utf-8")
        slides = parse_slides(text)
        n_slides = len(slides)
        deck_title = re.sub(r"^Folien:\s*", "", first_heading(text, "Präsentation"))
        (OUT / SLIDES_HTML).write_text(build_deck(slides, deck_title), encoding="utf-8")

    print(f"✓ {len(md_files)} Seiten, {n_slides} Folien → {OUT}/index.html")


def snapshot() -> dict:
    return {str(p): p.stat().st_mtime for p in source_files()}


def serve(port: int) -> None:
    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):  # keine Zeile pro Anfrage
            pass

    handler = functools.partial(QuietHandler, directory=str(OUT))
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
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
