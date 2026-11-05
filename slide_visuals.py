"""Grafiken der Präsentation als SVG – eine je Folie, alle im selben Stil.

``VISUALS`` ordnet dem Folien-Label aus 04_Folien.md eine Grafik zu. build_html.py
bettet sie in die Präsentation ein und legt sie zusätzlich unter
``html/assets/folien/`` ab, damit man sie auch in PowerPoint oder Google Präsentationen
einfügen kann.

Layouts: "side" (Grafik rechts), "narrow" (schmale Grafik rechts), "bottom" (Grafik
unter dem Text), "hero" (Titel- und Abschnittsfolien, dunkel).

Animationen: Die Klassen a-* und l-* sind in DECK_CSS definiert. Ohne dieses CSS (Druck,
PowerPoint, Miniaturen) zeigt jede Grafik ihren fertigen Endzustand. Deshalb gilt: Ein
Element mit Animationsklasse darf kein eigenes transform-Attribut tragen – dafür um
at(...) herum animieren. Eckige Platzhalter wie [KI-TOOL] gehören nicht in die Grafiken.
"""

from __future__ import annotations

import math
from html import escape

BLUE, PURPLE, GREEN, ORANGE, PINK = "#0071e3", "#8e5cf7", "#28a745", "#f08a00", "#e0457b"
RED, YELLOW, INK, GRAY, LINE, SOFT = "#e5342b", "#ffcc00", "#1d1d1f", "#6e6e73", "#d2d2d7", "#f5f5f7"
WHITE, TINT = "#ffffff", "#e8f2fd"
# Dieselben Farben wie die Baustein-Chips auf Folie 14 (DECK_CSS)
BLOCKS = [("Rolle", BLUE), ("Kontext", PURPLE), ("Aufgabe", GREEN), ("Format", ORANGE), ("Beispiel", PINK)]


def t(x, y, s, size=22, fill=INK, weight=500, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" '
            f'text-anchor="{anchor}">{escape(s)}</text>')


def rect(x, y, w, h, fill=SOFT, r=12, stroke=None, sw=2, extra=""):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{st} {extra}/>'


def circle(x, y, r, fill=SOFT, stroke=None, sw=2, extra=""):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"{st} {extra}/>'


def path(d, stroke=INK, sw=4, fill="none", cls="", d_=None):
    c = f' class="{cls}" pathLength="1"' if cls else ""
    return (f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" '
            f'stroke-linejoin="round"{c}{delay(d_)}/>')


def delay(d):
    return f' style="--d:{d}s"' if d is not None else ""


def a(cls, d, *inner):
    """Animierte Gruppe: a("a-pop", .4, ...) erscheint nach 0,4 Sekunden."""
    return f'<g class="{cls}"{delay(d)}>{"".join(inner)}</g>'


def at(x, y, *inner, s=None):
    sc = f" scale({s})" if s else ""
    return f'<g transform="translate({x} {y}){sc}">{"".join(inner)}</g>'


def svg(w, h, *inner, label=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}" '
            f'font-family="Inter, Helvetica, Arial, sans-serif">{"".join(inner)}</svg>')


def lines(x, y, widths, gap=20, fill=LINE, h=9):
    return "".join(rect(x, y + i * gap, w, h, fill, h / 2) for i, w in enumerate(widths))


def arrow(x1, y1, x2, y2, color=GRAY, d=None, sw=5):
    """Gerader Pfeil, der sich aufzeichnet; die Spitze erscheint danach."""
    ang = math.atan2(y2 - y1, x2 - x1)
    lx, ly = x2 - 16 * math.cos(ang - .5), y2 - 16 * math.sin(ang - .5)
    rx, ry = x2 - 16 * math.cos(ang + .5), y2 - 16 * math.sin(ang + .5)
    head = path(f"M{lx:.1f} {ly:.1f}L{x2} {y2}L{rx:.1f} {ry:.1f}", color, sw)
    return (path(f"M{x1} {y1}L{x2} {y2}", color, sw, cls="a-draw", d_=d)
            + a("a-fade", (d or 0) + .45, head))


def timer(x, y, minutes, r=56, d=.5):
    """Uhr-Plakette mit der Dauer einer Übung."""
    return at(x, y, a("a-pop", d, circle(0, 0, r, WHITE, LINE, 9),
                      f'<circle r="{r}" fill="none" stroke="{BLUE}" stroke-width="9" stroke-linecap="round" '
                      f'pathLength="1" class="a-draw a-slow" transform="rotate(-90)"{delay(d + .1)}/>',
                      t(0, 8, str(minutes), 38, INK, 700, "middle"), t(0, 32, "Min.", 18, GRAY, 600, "middle")))


# ---- kleine Symbole, jeweils ungefähr 80 × 80 um (0, 0) ----------------------------- #
def ic_bubble(c=BLUE):
    return rect(-38, -32, 76, 50, c, 16) + path("M-14 16L-22 36L4 18", c, 2, c) + lines(-24, -20, [48, 32], 14, WHITE, 6)


def ic_doc(c=WHITE, black=False):
    body = rect(-28, -36, 56, 72, c, 7, LINE) + lines(-18, -24, [36, 28, 36, 20], 13)
    return body + (rect(-18, -11, 26, 10, INK, 2) if black else "")


def ic_news():
    return rect(-34, -32, 68, 64, WHITE, 7, LINE) + rect(-24, -22, 48, 12, INK, 3) + lines(-24, -2, [48, 48, 30], 12)


def ic_lock(c=RED):
    return path("M-16 -6V-16A16 16 0 0 1 16 -16V-6", c, 7) + rect(-26, -6, 52, 38, c, 8) + circle(0, 12, 6, WHITE)


def ic_card():
    return (rect(-36, -24, 72, 48, WHITE, 7, LINE) + circle(-18, -4, 9, GRAY)
            + path("M-30 16A12 11 0 0 1 -6 16", GRAY, 5) + lines(4, -10, [22, 22, 14], 11))


def ic_gear(c=GRAY):
    teeth = "".join(f'<rect x="-6" y="-34" width="12" height="14" rx="3" fill="{c}" transform="rotate({i * 45})"/>'
                    for i in range(8))
    return teeth + circle(0, 0, 24, c) + circle(0, 0, 10, WHITE)


def ic_check(c=GREEN, r=26):
    return circle(0, 0, r, c) + path(f"M{-r * .42} 0L{-r * .1} {r * .34}L{r * .46} {-r * .34}", WHITE, r * .2)


def ic_cross(c=RED, r=26):
    k = r * .36
    return circle(0, 0, r, c) + path(f"M{-k} {-k}L{k} {k}M{k} {-k}L{-k} {k}", WHITE, r * .2)


def ic_stack():
    return "".join(rect(-34, 16 - i * 17, 68, 15, BLOCKS[i][1], 4) for i in range(5))


def ic_light():
    return (rect(-20, -40, 40, 80, INK, 12) + circle(0, -23, 9, RED) + circle(0, 0, 9, YELLOW) + circle(0, 23, 9, GREEN))


def ic_cycle(c=BLUE):
    return (path("M-28 -8A30 30 0 0 1 26 -14", c, 7) + path("M28 -30L27 -12L9 -15", c, 7)
            + path("M28 8A30 30 0 0 1 -26 14", c, 7) + path("M-28 30L-27 12L-9 15", c, 7))


def ic_loupe():
    return (circle(-6, -6, 24, WHITE, INK, 7) + path("M12 12L32 32", INK, 9) + path("M-16 -6L-8 3L5 -13", GREEN, 6))


def tower(x, y, w=170, h=62, gap=6, names=True, base_d=.2):
    """Der Prompt-Baukasten: fünf Klötze, Rolle unten – fallen nacheinander herein."""
    out = []
    for i, (name, color) in enumerate(BLOCKS):
        yy = y - i * (h + gap)
        label = t(x + w / 2, yy + h / 2 + 8, name, 24, WHITE, 700, "middle") if names else ""
        out.append(a("a-drop", base_d + i * .22, rect(x, yy, w, h, color, 11), label))
    return "".join(out)


def _takeaways(extra=""):
    items = [("Textmaschine", ic_bubble()), ("Daten-Ampel", ic_light()), ("Baukasten", ic_stack()),
             ("Nachsteuern", ic_cycle()), ("Gegenlesen", ic_loupe())]
    return "".join(a("a-pop", .35 + i * .15, at(136 + i * 272, 50, g, s=1.05),
                     t(136 + i * 272, 122, name, 22, GRAY, 600, "middle"))
                   for i, (name, g) in enumerate(items)) + extra


# ---- Folien ------------------------------------------------------------------------ #
def f01():
    bubbles = (a("a-rise", .5, rect(250, 124, 244, 44, BLUE, 16), lines(268, 136, [190, 120], 12, WHITE, 6))
               + a("a-rise", 1.0, rect(106, 182, 300, 88, WHITE, 16), lines(124, 197, [260, 240, 180, 220], 15))
               + a("a-rise", 1.5, rect(300, 284, 194, 44, BLUE, 16), lines(318, 296, [150, 90], 12, WHITE, 6)))
    steam = "".join(path(f"M{x} 412q-12 -18 0 -36q12 -18 0 -36", "#a1a1a6", 5, cls="l-steam", d_=i * .7)
                    for i, x in enumerate((528, 556, 584)))
    return svg(640, 560,
               rect(70, 90, 440, 300, "#2c2c2e", 20, "#48484a"), rect(86, 106, 408, 268, SOFT, 8), bubbles,
               path("M70 390H510L560 432H20Z", "#48484a", 2, "#636366"), rect(20, 432, 540, 14, "#a1a1a6", 7),
               steam, rect(510, 424, 92, 76, WHITE, 12), path("M602 442h12a16 16 0 0 1 0 34h-12", WHITE, 8),
               rect(490, 498, 134, 10, "#a1a1a6", 5),
               label="Laptop mit Chatfenster, daneben eine dampfende Kaffeetasse")


def f02():
    parts = [("Verstehen", 110, "#a1a1a6"), ("Regeln", 110, "#a1a1a6"), ("Texte", 221, BLUE), ("Prompts", 221, BLUE),
             ("", 73, ORANGE), ("Dokumente & Tabellen", 294, BLUE), ("Deine Aufgabe", 221, BLUE), ("Abschluss", 110, "#a1a1a6")]
    out, x = [], 0
    times = ["0:00", "0:15", "0:30", "1:00", "1:30", "1:40", "2:20", "2:50", "3:05"]
    for i, (name, w, color) in enumerate(parts):
        size = 21 if w > 100 else 18
        lab = t(x + w / 2, 83, name, size, WHITE, 650, "middle") if name else ""
        cup = "" if name else (rect(x + 22, 58, 26, 28, WHITE, 5) + path(f"M{x + 48} 64h4a7 7 0 0 1 0 15h-4", WHITE, 4))
        out.append(a("a-grow", .15 + i * .13, rect(x + 2, 44, w - 4, 62, color, 12), lab, cup))
        out.append(a("a-fade", .15 + i * .13, t(x + 3, 134, times[i], 18, GRAY, 500)))
        x += w
    out.append(a("a-fade", 1.3, t(1357, 134, times[-1], 18, GRAY, 500, "end")))
    out.append(a("a-fade", 1.4, rect(0, 6, 22, 22, BLUE, 6), t(32, 25, "selbst machen: der größte Teil", 22, INK, 600)))
    return svg(1360, 145, *out, label="Zeitstrahl des Tages mit Pause; der größte Teil ist Selbermachen")


def f03():
    clock = circle(0, 0, 34, WHITE, BLUE, 7) + path("M0 -18V0L13 9", BLUE, 6)
    bulb = (circle(0, -6, 28, YELLOW) + rect(-13, 22, 26, 12, GRAY, 4) + path("M-8 -6L0 4L8 -6M0 4V20", INK, 3))
    beam = (rect(70, 120, 500, 14, INK, 7) + path("M100 130L50 300M100 130L170 300", GRAY, 3)
            + path("M540 130L470 300M540 130L590 300", GRAY, 3)
            + path("M30 300H190A80 44 0 0 1 30 300Z", BLUE, 2, TINT) + path("M450 300H610A80 44 0 0 1 450 300Z", YELLOW, 2, "#fff6cc")
            + at(110, 250, clock) + at(530, 246, bulb)
            + t(110, 386, "Zeit sparen", 25, BLUE, 700, "middle") + t(530, 386, "Kopf einschalten", 25, "#8a6d00", 700, "middle"))
    return svg(640, 540, path("M320 128V470", INK, 14), rect(220, 468, 200, 22, INK, 11),
               circle(320, 124, 18, BLUE), f'<g class="l-balance">{beam}</g>',
               label="Waage im Gleichgewicht zwischen Zeit sparen und Kopf einschalten")


def f04():
    keys = "".join(rect(40 + c * 34, 318 + r * 30, 28, 24, WHITE, 5) for r in range(3) for c in range(5))
    chips = (a("a-pop", .7, rect(32, 260, 78, 40, BLUE, 11), t(71, 286, "später", 18, WHITE, 700, "middle"))
             + a("a-pop", .85, rect(114, 260, 66, 40, WHITE, 11), t(147, 286, "früher", 16, GRAY, 600, "middle"))
             + a("a-pop", 1.0, rect(184, 260, 46, 40, WHITE, 11), t(207, 286, "spät", 16, GRAY, 600, "middle")))
    words = ("Sehr geehrte Frau Weber,|vielen Dank für Ihre|Nachricht. Ihre Bestellung|trifft voraussichtlich|"
             "am Freitag bei Ihnen|ein. Bei Fragen melden|Sie sich gern.").split("|")
    para, n = [], 0
    for li, row in enumerate(words):
        spans = []
        for w in row.split(" "):
            spans.append(f'<tspan class="a-word" style="--d:{1.5 + n * .14:.2f}s">{escape(w)} </tspan>')
            n += 1
        para.append(f'<text x="322" y="{104 + li * 40}" font-size="20" font-weight="500" fill="{INK}">{"".join(spans)}</text>')
    return svg(640, 540,
               rect(16, 16, 228, 430, INK, 34), rect(26, 30, 208, 402, SOFT, 26),
               a("a-rise", .2, rect(40, 66, 180, 90, BLUE, 18), t(56, 102, "Ich komme", 22, WHITE, 600),
                 t(56, 130, "heute etwas …", 22, WHITE, 600)),
               t(32, 246, "Vorschläge:", 16, GRAY, 600), chips, keys,
               rect(306, 44, 320, 330, WHITE, 18, LINE), *para,
               arrow(254, 210, 298, 210, BLUE, 1.2),
               a("a-rise", 2.6, t(320, 420, "Gleiches Prinzip,", 28, BLUE, 700), t(320, 456, "viel, viel größer", 28, BLUE, 700)),
               label="Smartphone mit Wortvorschlägen; daneben ein Absatz, der Wort für Wort entsteht")


def f04b():
    def part(x, name, what, d, w=128):
        return a("a-pop", d, rect(x, 196, w, 58, WHITE, 11, LINE), t(x + w / 2, 219, name, 15, GRAY, 600, "middle"),
                 t(x + w / 2, 242, what, 17, INK, 700, "middle"))

    wheel = lambda x: circle(x, 296, 35, INK) + circle(x, 296, 15, "#a1a1a6")
    car = (path("M26 296V218Q26 186 62 182L168 176L236 100Q246 90 262 90H420Q436 90 446 102L502 172L588 190Q622 198 622 232V296Z",
                LINE, 3, SOFT)
           + path("M186 172L244 108Q250 102 262 102H336V172Z", LINE, 2, WHITE)
           + path("M352 102H420Q430 102 436 110L484 172H352Z", LINE, 2, WHITE) + wheel(138) + wheel(510))
    engine = (f'<g class="l-pulse">{rect(466, 192, 148, 62, BLUE, 12)}</g>'
              + t(540, 218, "Motor", 17, "#cfe4fb", 600, "middle") + t(540, 241, "Sprachmodell", 19, WHITE, 700, "middle"))

    def stack(x, n, d, label):
        sheets = "".join(rect(x, 520 - i * 15, 104, 12, BLUE if i % 2 == 0 else "#a1a1a6", 4) for i in range(n))
        return a("a-rise", d, sheets, t(x, 554, label, 17, GRAY, 600), arrow(x + 112, 490, x + 150, 490, BLUE, d + .15),
                 circle(x + 170, 490, 18, BLUE), t(x + 170, 497, "M", 19, WHITE, 700, "middle"))

    return svg(640, 565, car, engine,
               part(32, "Kofferraum", "Dateien", .35), part(168, "Lenkrad", "Eingabefeld", .5),
               part(304, "Handschuhfach", "Rechner", .65, 148),
               a("a-pop", .8, rect(262, 116, 156, 48, WHITE, 10, LINE), t(340, 136, "Navi", 15, GRAY, 600, "middle"),
                 t(340, 156, "Websuche", 17, INK, 700, "middle")),
               t(0, 30, "Das Auto: das Tool um den Motor", 22, INK, 700),
               t(0, 362, "Der Motor vergisst: Jedes Mal kommt der ganze Chat mit", 21, INK, 700),
               stack(0, 1, 1.1, "1. Nachricht"), stack(215, 3, 1.7, "2. Nachricht"), stack(430, 5, 2.3, "3. Nachricht"),
               label="Auto im Querschnitt mit dem Motor Sprachmodell; bei jeder Nachricht wandert ein wachsender Stapel in den Motor")


def f06():
    return svg(640, 540,
               rect(10, 10, 620, 510, SOFT, 22, LINE),
               a("a-rise", .25, rect(330, 34, 270, 50, BLUE, 16), t(465, 66, "Drei Stichworte", 22, WHITE, 600, "middle")),
               a("a-rise", .65, rect(36, 98, 420, 130, WHITE, 16, LINE), lines(56, 118, [380, 350, 370, 240, 300], 19)),
               a("a-pop", 1.1, at(490, 164, ic_check(GREEN, 34)), t(490, 228, "Wow!", 28, GREEN, 700, "middle")),
               a("a-rise", 1.7, rect(280, 264, 320, 50, BLUE, 16), t(440, 296, "Etwas, das sie nicht weiß", 21, WHITE, 600, "middle")),
               a("a-rise", 2.1, rect(36, 328, 420, 130, WHITE, 16, LINE), lines(56, 348, [380, 360, 340, 370, 210], 19)),
               a("a-pop", 2.6, at(490, 394, circle(0, 0, 34, ORANGE), t(0, 16, "?", 46, WHITE, 700, "middle")),
                 t(490, 458, "Hoppla!", 28, ORANGE, 700, "middle")),
               a("a-fade", 3.0, t(320, 498, "Klingt beide Male gleich sicher", 24, INK, 700, "middle")),
               label="Chat mit zwei Antworten: einmal Wow, einmal Hoppla, beide klingen gleich sicher")


def f07():
    def row(y, color, d, icons):
        light = a("a-light", d, circle(100, y, 62, color))
        return light + "".join(a("a-pop", d + .15 + i * .1, at(240 + i * 92, y, g)) for i, g in enumerate(icons))

    return svg(440, 570, rect(24, 16, 152, 494, INK, 42), rect(84, 510, 32, 54, INK, 4),
               circle(100, 110, 62, "#3a3a3c"), circle(100, 263, 62, "#3a3a3c"), circle(100, 416, 62, "#3a3a3c"),
               row(110, "#34c759", .3, [ic_news(), ic_bubble(GREEN)]),
               row(263, YELLOW, 1.0, [ic_doc(WHITE, True)]),
               row(416, "#ff3b30", 1.7, [ic_lock(), ic_card(), ic_gear()]),
               label="Verkehrsampel: grün öffentliche Infos, gelb anonymisierte Dokumente, rot Geheimes und Personenbezogenes")


def f08():
    def door(x, name, sub, color):
        return (rect(x, 96, 240, 370, "#3a3a3c", 8) + rect(x + 12, 108, 216, 358, color, 4) + t(x + 120, 62, name, 27, INK, 700, "middle")
                + t(x + 120, 88, sub, 19, GRAY, 500, "middle"))

    glow = a("a-fade", .8, rect(30, 108, 216, 358, "#d6f5dd", 4), t(150, 240, "Grün", 25, GREEN, 700, "middle"),
             t(150, 280, "Gelb", 25, "#b08a00", 700, "middle"), t(150, 322, "nach Prüfung", 18, GRAY, 500, "middle"))
    leaf = a("a-door", .35, path("M30 108L118 126V450L30 466Z", LINE, 2, "#8e8e93"), circle(102, 288, 7, WHITE))
    closed = rect(342, 108, 216, 358, "#8e8e93", 4) + circle(528, 288, 7, WHITE)
    return svg(640, 500, door(18, "Firmenlizenz", "der richtige Eingang", "#d6f5dd"), glow, leaf,
               door(330, "Privat / Gratis", "für Firmendaten tabu", "#8e8e93"), closed,
               a("a-stamp", 1.3, at(450, 290, ic_cross(RED, 62))),
               a("a-pop", 1.0, at(250, 110, ic_check(GREEN, 34))),
               label="Zwei Türen: Firmenlizenz offen, Privat und Gratis für Firmendaten gesperrt")


def f09():
    items = ["Zahlen", "Namen", "Termine", "Quellen", "Paragrafen"]
    rows = "".join(t(180, 150 + i * 66, n, 26, INK, 600)
                   + a("a-pop", .7 + i * .55, at(136, 142 + i * 66, ic_check(GREEN, 20))) for i, n in enumerate(items))
    pen = (path("M0 0L22 -40L44 -28L18 14Z", INK, 2, BLUE) + path("M0 0L-6 22L18 14Z", INK, 2, "#ffd9a8"))
    eye = lambda x: (path(f"M{x - 36} 44Q{x} 8 {x + 36} 44Q{x} 80 {x - 36} 44Z", INK, 4, WHITE)
                     + f'<g class="l-blink">{circle(x, 44, 13, BLUE)}</g>')
    return svg(640, 500, rect(92, 92, 330, 390, WHITE, 16, LINE), rows,
               f'<g class="l-pen">{at(330, 150, pen)}</g>',
               eye(480), eye(572), t(526, 112, "Deine zwei Augen", 24, BLUE, 700, "middle"), t(526, 142, "zählen", 24, BLUE, 700, "middle"),
               label="Prüfliste mit Haken, die ein Stift abhakt; dazu zwei Augen")


def f10():
    def typed(y, words, start):
        spans = "".join(f'<tspan class="a-word" style="--d:{start + i * .18:.2f}s">{escape(w)} </tspan>' for i, w in enumerate(words.split(" ")))
        return f'<text x="194" y="{y}" font-size="23" font-weight="500" fill="{INK}">{spans}</text>'

    models = [("⚡ schnell", 150, 2.6), ("⭐ stark", 310, 2.8), ("🧠 Nachdenken", 470, 3.0)]
    return svg(640, 540,
               rect(10, 10, 620, 470, WHITE, 18, LINE), f'<path d="M10 62V28a18 18 0 0 1 18 -18H612a18 18 0 0 1 18 18V62Z" fill="{SOFT}"/>',
               circle(40, 36, 8, "#ff5f57"), circle(66, 36, 8, "#febc2e"), circle(92, 36, 8, "#28c840"),
               rect(124, 20, 480, 32, WHITE, 16), t(144, 42, "Link zum Tool", 17, GRAY, 500),
               rect(10, 62, 150, 418, SOFT, 0), a("a-pop l-attn", .4, rect(24, 80, 122, 44, BLUE, 12), t(85, 108, "Neuer Chat", 17, WHITE, 700, "middle")),
               lines(30, 146, [100, 84, 96], 24),
               a("a-rise", 3.6, rect(420, 96, 186, 70, TINT, 14), t(513, 124, "Klappt's?", 20, BLUE, 700, "middle"), t(513, 150, "Daumen hoch!", 18, BLUE, 600, "middle")),
               rect(176, 210, 438, 118, WHITE, 16, BLUE, 3),
               typed(254, "Hallo! Erklär mir in zwei", .9), typed(290, "Sätzen, was du kannst.", 1.8),
               t(320, 382, "Wo wählst du das Modell?", 20, GRAY, 600, "middle"),
               "".join(a("a-pop", d, rect(x - 76, 396, 152, 44, SOFT, 12, LINE), t(x, 424, n, 18, INK, 600, "middle")) for n, x, d in models),
               t(320, 524, "Beispielansicht – dein Tool sieht anders aus", 19, GRAY, 500, "middle"),
               label="Beispielhaftes Chatfenster mit Neuer Chat, Eingabefeld und Modellauswahl")


def f11():
    env = (rect(-74, -50, 148, 100, WHITE, 10, INK, 4) + path("M-72 -46L0 8L72 -46", INK, 4))
    def card(y, label, d, color):
        return a("a-left", d, rect(372, y, 240, 82, WHITE, 14, color, 3), t(392, y + 34, label, 25, color, 700),
                 lines(392, y + 50, [190], 12))

    return svg(640, 500, a("a-pop", .2, at(120, 180, env), at(186, 124, circle(0, 0, 25, RED), t(0, 11, "!", 32, WHITE, 700, "middle"))),
               t(120, 266, "Verärgerte", 22, GRAY, 600, "middle"), t(120, 294, "Kundenmail", 22, GRAY, 600, "middle"),
               arrow(218, 170, 358, 74, BLUE, .7), arrow(218, 182, 358, 180, BLUE, .9), arrow(218, 194, 358, 286, BLUE, 1.1),
               card(32, "förmlich", 1.3, BLUE), card(140, "locker", 1.5, PURPLE), card(248, "Englisch", 1.7, GREEN),
               timer(120, 420, 20, d=2),
               label="Kundenmail wird zu drei Varianten: förmlich, locker, Englisch; 20 Minuten")


def f12():
    def face(x, y, happy, color, d):
        mouth = f"M{x - 18} {y + 12}Q{x} {y + 32} {x + 18} {y + 12}" if happy else f"M{x - 16} {y + 22}Q{x} {y + 10} {x + 16} {y + 22}"
        return a("a-pop", d, circle(x, y, 44, color), circle(x - 15, y - 10, 6, INK), circle(x + 15, y - 10, 6, INK), path(mouth, INK, 5))

    return svg(640, 520,
               a("a-rise", .25, rect(20, 42, 340, 66, "#a1a1a6", 18), t(190, 83, "„Schreib was über Lieferung“", 21, WHITE, 600, "middle")),
               face(490, 76, False, "#ffe08a", .7), a("a-pop", 1.0, t(555, 60, "?", 42, ORANGE, 700), t(590, 92, "?", 30, ORANGE, 700)),
               t(190, 142, "Die KI muss raten", 22, GRAY, 600, "middle"),
               a("a-rise", 1.4, rect(20, 190, 440, 268, BLUE, 18),
                 t(44, 232, "Rolle: Einkäuferin", 22, WHITE, 600), t(44, 272, "Kontext: zum zweiten Mal", 22, WHITE, 600),
                 t(44, 302, "verschoben, bis zum 15.", 22, WHITE, 600), t(44, 342, "Aufgabe: Termin erbitten", 22, WHITE, 600),
                 t(44, 382, "Format: 120 Wörter, Sie-Form", 22, WHITE, 600), t(44, 422, "Beispiel: So soll es klingen", 22, WHITE, 600)),
               face(550, 320, True, "#8ee0a0", 2.0), t(240, 494, "Die KI weiß, was du willst", 22, BLUE, 700, "middle"),
               label="Kurze Anweisung und ratloses Gesicht; ausführliche Anweisung und zufriedenes Gesicht")


def f13():
    return svg(300, 540, tower(50, 462, 200, 68, 8),
               a("a-pop", 1.5, at(150, 62, ic_check(GREEN, 40))),
               a("a-fade", 1.7, t(150, 124, "gute Antwort", 22, GREEN, 700, "middle")),
               label="Fünf Bauklötze: Rolle, Kontext, Aufgabe, Format, Beispiel, oben ein Häkchen")


def f15():
    nodes = [("Fragen", 250, 52, BLUE), ("Antwort", 412, 278, PURPLE), ("Schärfen", 88, 278, GREEN)]
    labels = "".join(a("a-pop", .3 + i * .3, circle(x, y, 56, c), t(x, y + 8, n, 20, WHITE, 700, "middle"))
                     for i, (n, x, y, c) in enumerate(nodes))
    return svg(640, 530,
               path("M322 86Q410 130 420 212", GRAY, 5, cls="a-draw", d_=.6), path("M342 268H158", GRAY, 5, cls="a-draw", d_=.9),
               path("M82 212Q92 130 178 86", GRAY, 5, cls="a-draw", d_=1.2),
               a("a-fade", 1.0, path("M404 200L420 214L432 196", GRAY, 5)), a("a-fade", 1.3, path("M172 256L156 268L172 282", GRAY, 5)),
               a("a-fade", 1.6, path("M162 78L180 84L176 104", GRAY, 5)),
               labels,
               a("a-tilt", 1.8, at(330, 390, rect(-250, -24, 540, 124, "#fff6cc", 18, YELLOW, 4),
                                 t(-226, 14, "JOKER", 22, "#8a6d00", 800),
                                 t(-226, 50, "„Stell mir erst bis zu 3 Fragen,", 25, INK, 600),
                                 t(-226, 82, "bevor du loslegst.“", 25, INK, 600))),
               label="Kreislauf aus Fragen, Antwort lesen und Nachschärfen, dazu die Joker-Karte")


def f16():
    return svg(420, 540, tower(40, 462, 150, 56, 6),
               a("a-fade", 1.5, t(115, 180, "Baukasten", 22, GRAY, 600, "middle")),
               a("a-pop", 1.4, rect(250, 448, 150, 70, "#a1a1a6", 11), t(325, 490, "Minimal", 23, WHITE, 700, "middle")),
               a("a-pop", 1.7, t(325, 420, "gegen", 21, GRAY, 600, "middle")),
               timer(325, 110, 18, r=66, d=1.9),
               label="Baukasten-Prompt gegen Minimal-Prompt; 18 Minuten")


def f17():
    steam = "".join(path(f"M{x} 200q-20 -30 0 -60q20 -30 0 -60", "#a1a1a6", 8, cls="l-steam", d_=i * .7) for i, x in enumerate((230, 290, 350)))
    return svg(640, 560,
               f'<circle cx="290" cy="290" r="250" fill="none" stroke="#2c2c2e" stroke-width="12"/>',
               f'<circle cx="290" cy="290" r="250" fill="none" stroke="#2997ff" stroke-width="12" stroke-linecap="round" pathLength="1" '
               f'class="a-countdown" transform="rotate(-90 290 290)"/>',
               steam, rect(170, 228, 240, 180, WHITE, 26), path("M410 262h22a36 36 0 0 1 0 74h-22", WHITE, 18),
               rect(130, 412, 320, 22, "#a1a1a6", 11), t(290, 332, "10 Min.", 42, INK, 700, "middle"),
               label="Dampfende Kaffeetasse in einem Ring, der zehn Minuten herunterzählt")


def f18():
    docs = "".join(a("a-rise", .2 + i * .18, at(70 + i * 62, 80 + (i % 2) * 22, ic_doc(), s=1.1)) for i in range(4))
    funnel = path("M60 180H390L268 322V396H182V322Z", BLUE, 3, TINT)
    pts = "".join(a("a-left", 1.2 + i * .25, at(452, 234 + i * 76, ic_check(GREEN, 19)), rect(484, 222 + i * 76, 124 - i * 12, 24, LINE, 12))
                  for i in range(3))
    return svg(640, 510, docs, a("a-pop", .85, funnel, t(225, 268, "KI", 44, BLUE, 700, "middle")), arrow(306, 300, 428, 300, BLUE, 1.05),
               pts, t(530, 196, "Kernpunkte", 23, INK, 700, "middle"),
               a("a-pop", 2, at(540, 66, ic_light(), s=1.15)), t(450, 66, "Vorher", 21, GRAY, 600, "middle"), t(450, 92, "Ampel!", 21, GRAY, 600, "middle"),
               t(225, 442, "Trotzdem im Original prüfen", 23, RED, 700, "middle"),
               label="Dokumentenstapel, Trichter, drei saubere Kernpunkte")


def f19():
    scrawl = (path("M36 76q24 -14 50 0t48 -4 40 8", GRAY, 4) + path("M46 112q34 12 60 -2t56 6", GRAY, 4) + path("M34 150q40 -18 72 0t62 -6", GRAY, 4)
              + path("M60 194q30 10 58 -4", GRAY, 4) + path("M38 232q42 12 76 -6t56 6", GRAY, 4) + path("M60 272q20 -12 44 2", GRAY, 4))
    head = [("Wer", 356), ("Was", 450), ("Bis wann", 546)]
    rows = "".join(a("a-left", 1.2 + r * .3, *[rect(x - 42, 136 + r * 66, 84, 42, LINE if r % 2 else TINT, 8) for x in (356, 450, 546)]) for r in range(3))
    return svg(640, 420, f'<g transform="rotate(-3 110 180)">{rect(14, 40, 190, 280, "#fff6cc", 8, YELLOW, 2)}{scrawl}</g>',
               arrow(222, 190, 298, 190, BLUE, .6),
               a("a-rise", .9, rect(308, 84, 318, 42, BLUE, 8), *[t(x, 112, n, 19, WHITE, 700, "middle") for n, x in head]), rows,
               t(320, 386, "Immer: „Zeig mir, was du geändert hast.“", 22, BLUE, 700, "middle"),
               label="Krakeliger Notizzettel wird zu einer sauberen Tabelle mit Wer, Was, Bis wann")


def f20():
    def tile(x, y, letter, name, color, d, g):
        return a("a-pop", d, rect(x, y, 196, 176, WHITE, 18, color, 3), circle(x + 34, y + 34, 22, color),
                 t(x + 34, y + 43, letter, 25, WHITE, 700, "middle"), at(x + 130, y + 62, g), t(x + 98, y + 150, name, 21, INK, 650, "middle"))
    ver = at(-20, 0, ic_doc()) + t(30, 12, "≠", 34, RED, 700, "middle")
    tick = rect(-30, -38, 60, 76, "#fff6cc", 6, YELLOW) + "".join(at(-16, -22 + i * 22, ic_check(GREEN, 8)) + rect(-2, -26 + i * 22, 26, 7, GRAY, 3) for i in range(3))
    grid = "".join(rect(-36 + c * 25, -30 + r * 21, 22, 18, TINT if r else BLUE, 3) for r in range(3) for c in range(3))
    return svg(640, 540, tile(120, 10, "A", "Bericht", BLUE, .25, ic_doc()), tile(330, 10, "B", "Versionen", PURPLE, .45, ver),
               tile(120, 200, "C", "Notizen", GREEN, .65, tick), tile(330, 200, "D", "Tabelle", ORANGE, .85, grid),
               timer(325, 460, 27, r=62, d=1.2), t(120, 460, "Prüfschritt", 22, RED, 700), t(120, 490, "nicht weglassen!", 22, RED, 700),
               label="Vier Stationen A bis D; 27 Minuten")


def f21():
    blocks = "".join(a("a-drop", .7 + i * .16, rect(116 + i * 84, 190 - (i % 2) * 22, 76, 70, c, 9)) for i, (_, c) in enumerate(BLOCKS))
    return svg(640, 470, blocks, path("M220 178V120Q220 94 248 94H392Q420 94 420 120V178", INK, 16),
               rect(70, 248, 500, 190, "#c0392b", 22), rect(70, 248, 500, 40, "#962d22", 14), rect(292, 268, 56, 40, YELLOW, 7),
               t(320, 384, "Dein Alltag", 44, WHITE, 700, "middle"),
               label="Werkzeugkasten mit der Aufschrift Dein Alltag, darin die fünf Bauklötze")


def f22():
    def person(x, color, d):
        return a("a-rise", d, circle(x, 170, 44, color), path(f"M{x - 68} 300Q{x - 68} 226 {x} 226T{x + 68} 300Z", color, 2, color))

    return svg(640, 520, person(140, BLUE, .2), person(500, PURPLE, .4),
               a("a-pop", .7, rect(216, 56, 150, 66, BLUE, 16), t(291, 97, "Erzähl mal", 21, WHITE, 650, "middle")),
               a("a-pop", 1.0, rect(306, 136, 146, 66, PURPLE, 16), t(379, 177, "Und dann?", 21, WHITE, 650, "middle")),
               rect(214, 214, 212, 124, INK, 12), rect(226, 226, 188, 100, SOFT, 5), lines(242, 244, [150, 120, 140], 22), rect(184, 338, 272, 14, "#8e8e93", 7),
               rect(60, 430, 520, 18, LINE, 9), f'<rect x="60" y="430" width="520" height="18" rx="9" fill="{BLUE}" class="a-grow"{delay(1.2)}/>',
               a("a-pop", 2, circle(320, 439, 22, ORANGE), path("M311 433h17l-5 -5M329 445h-17l5 5", WHITE, 3)),
               t(320, 490, "Halbzeit: Rollen tauschen", 23, ORANGE, 700, "middle"), t(60, 416, "0 Min.", 18, GRAY, 500), t(580, 416, "27 Min.", 18, GRAY, 500, "end"),
               label="Zwei Personen an einem Laptop, Zeitstrahl mit Rollentausch zur Halbzeit")


def f23():
    beam = lambda x, d: (f'<g class="l-sweep" style="--d:{d}s;transform-origin:{x}px 0">'
                         f'<path d="M{x - 12} 0L{320 - 120} 410H{320 + 120}L{x + 12} 0Z" fill="#ffe58a" opacity=".55"/></g>')
    hands = "".join(a("l-clap", i * .25, at(120 + i * 200, 480, circle(-14, 0, 20, "#ffd9a8"), circle(14, 0, 20, "#ffc98a"))) for i in range(3))
    return svg(640, 530, rect(0, 0, 640, 410, INK, 18), beam(90, 0), beam(550, .8), rect(30, 404, 580, 34, "#8e5a2b", 8),
               a("a-pop", .3, t(320, 318, "Eure", 50, WHITE, 700, "middle"), t(320, 376, "Ergebnisse", 50, WHITE, 700, "middle")),
               hands, label="Bühne mit Scheinwerfern und dem Schriftzug Eure Ergebnisse, davor klatschende Hände")


def f24():
    return svg(1360, 135, _takeaways(), label="Fünf Symbole: Textmaschine, Daten-Ampel, Baukasten, Nachsteuern, Gegenlesen")


def f25():
    def sign(y, name, color, d, flip=False):
        pts = (f"M160 {y}H470L520 {y + 34}L470 {y + 68}H160Z" if not flip else f"M480 {y}H170L120 {y + 34}L170 {y + 68}H480Z")
        return a("a-left" if not flip else "a-right", d, path(pts, color, 2, color), t(320, y + 44, name, 30, WHITE, 700, "middle"))

    return svg(640, 530, rect(308, 40, 24, 450, "#8e5a2b", 8), sign(66, "Ausprobieren", BLUE, .3), sign(166, "Austauschen", PURPLE, .6, True),
               sign(266, "Nachfragen", GREEN, .9), path("M180 490H460", GREEN, 14),
               label="Wegweiser mit den Schildern Ausprobieren, Austauschen, Nachfragen")


def f26():
    stars = ""
    for i in range(5):
        x = 80 + i * 120
        d = "M0 -44L13 -14L46 -11L21 10L29 42L0 25L-29 42L-21 10L-46 -11L-13 -14Z"
        stars += at(x, 270, a("a-pop", .4 + i * .22, f'<path d="{d}" fill="{YELLOW}"/>'))
    return svg(640, 560, a("a-rise", .2, rect(40, 40, 560, 150, "#2c2c2e", 26), t(320, 106, "Was war hilfreich?", 34, WHITE, 700, "middle"),
                           t(320, 150, "Was soll anders werden?", 28, "#a1a1a6", 500, "middle")), path("M180 190L150 236L240 190", "#2c2c2e", 2, "#2c2c2e"),
               stars, rect(190, 344, 260, 190, "none", 18, "#6e6e73", 3, 'stroke-dasharray="10 10"'),
               t(320, 432, "QR-Code zum", 24, "#a1a1a6", 600, "middle"), t(320, 464, "Feedbackbogen", 24, "#a1a1a6", 600, "middle"),
               label="Sprechblase und fünf Sterne; Feld für den QR-Code zum Feedbackbogen")


def appendix_b():
    return svg(1360, 135, _takeaways(a("a-pop", 1.3, at(1330, 42, t(0, 18, "?", 60, ORANGE, 700, "middle")))),
               label="Die fünf Symbole aus Folie 24 mit einem Fragezeichen")


VISUALS: dict[str, tuple[str, str]] = {
    "Folie 1": ("hero", f01()), "Folie 2": ("bottom", f02()), "Folie 3": ("side", f03()), "Folie 4": ("side", f04()),
    "Folie 4b": ("side", f04b()), "Folie 6": ("side", f06()), "Folie 7": ("narrow", f07()), "Folie 8": ("side", f08()),
    "Folie 9": ("side", f09()), "Folie 10": ("side", f10()), "Folie 11": ("side", f11()), "Folie 12": ("side", f12()),
    "Folie 13": ("narrow", f13()), "Folie 15": ("side", f15()), "Folie 16": ("narrow", f16()), "Folie 17": ("hero", f17()),
    "Folie 18": ("side", f18()), "Folie 19": ("side", f19()), "Folie 20": ("side", f20()), "Folie 21": ("side", f21()),
    "Folie 22": ("side", f22()), "Folie 23": ("side", f23()), "Folie 24": ("bottom", f24()), "Folie 25": ("narrow", f25()),
    "Folie 26": ("hero", f26()), "Anhang B": ("bottom", appendix_b()),
}
