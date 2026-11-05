# Testlauf: Demo 4B – Buchstaben zählen

**Herkunft:** [Demo: Typische KI-Schwächen live zeigen](../07_Beispielmaterial/demo_fehler_zeigen.md), Abschnitt „Demo 4: Rechnen und Zählen“, Prompt B (Zählen).
Zugehörige Trainer-Hinweise: [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md) (Bezug zur Demo bei der Zeilenzählung in Übung 3: „Sprachmodelle zählen unzuverlässig – Brücke zur Demo aus Block 1“).

> **Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Getesteter Prompt (unverändert aus dem Material):**

```
Wie oft kommt der Buchstabe „e“ in diesem Satz vor: „Die Nordlicht Technik GmbH liefert Steuergehäuse an Kunden in ganz Europa.“
```

**Richtige Lösung (laut Material, per Python nachgeprüft):** 9 kleine „e“ (Die 1, Technik 1, liefert 2, Steuergehäuse 4, Kunden 1); 10, wenn das große „E“ in „Europa“ mitgezählt wird.

Nachprüfung:

```
python3 -c "s='Die Nordlicht Technik GmbH liefert Steuergehäuse an Kunden in ganz Europa.'; print(s.count('e'), s.lower().count('e'))"
9 10
```

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Ergebnis korrekt (9 bzw. 10) | ja | ja | ja |
| Unterscheidet klein / inkl. großem „E“ | ja | ja | ja |
| Rechenweg Wort für Wort nachvollziehbar | ja (nur Wörter mit „e“) | ja (alle Wörter) | ja (alle Wörter, Tabelle mit Hervorhebung) |
| Einzelwerte pro Wort korrekt | ja | ja | ja |
| Hinweis auf eigene Unzuverlässigkeit / Prüfen | nein | ja (Strg+F empfohlen) | nein |
| Zusätzliche Aspekte | – | – | Umlaut „ä“ vs. „ae“ (dann 11) – korrekt |
| Erfundenes / Fehler | keine | keine | keine |
| **Gezeigter Demo-Fehler tritt auf?** | **nein** | **nein** | **nein** |

---

## Gefundene Fehler mit Beleg

**Keine sachlichen Fehler.** Alle drei Modelle liefern 9 (klein) bzw. 10 (inkl. „E“). Die Einzelwerte pro Wort stimmen mit der Nachzählung überein:

| Wort | „e“ klein | inkl. „E“ |
|---|---|---|
| Die | 1 | 1 |
| Nordlicht | 0 | 0 |
| Technik | 1 | 1 |
| GmbH | 0 | 0 |
| liefert | 2 | 2 |
| Steuergehäuse | 4 | 4 |
| an, in, ganz | 0 | 0 |
| Kunden | 1 | 1 |
| Europa | 0 | 1 |
| **Summe** | **9** | **10** |

Kleinere Beobachtungen (keine Fehler):

- **Sonnet** zerlegt „Steuergehäuse“ ungewöhnlich als „Ste-u-e-rg-e-häus-e“. Zusammengesetzt ergibt das korrekt „Steuergehäuse“ mit 4 „e“, wirkt für Laien aber verwirrend.
- **Sonnet** empfiehlt Strg+F. Achtung: Die Suche in Browser und Word unterscheidet standardmäßig **nicht** zwischen Groß- und Kleinschreibung und meldet daher **10** Treffer, nicht 9. Das ist kein Fehler, sollte der Trainer aber wissen, falls jemand nachprüft.
- **Opus** ergänzt: Bei Schreibweise „Steuergehaeuse“ wären es 11. Nachgeprüft: richtig (`'...Steuergehaeuse...'.lower().count('e')` = 11).
- **Haiku** nennt die Wörter ohne „e“ nicht, das Ergebnis stimmt trotzdem.

---

## Lehren für die Auswertung

1. **Der Demo-Fehler tritt bei aktuellen Modellen mit diesem Prompt nicht auf.** Alle drei zählen von sich aus Wort für Wort und kommen auf das richtige Ergebnis. Das Material rechnet damit („Auch ‚Die KI hat es richtig gemacht‘ ist eine gute Lehre“). Die Botschaft lautet dann: „Diesmal stimmt es – aber nur, weil die KI den Rechenweg aufgeschrieben hat. Woher wisst ihr ohne Nachzählen, dass es stimmt?“
2. **Der Rechenweg ist der Schlüssel.** Hier zeigt sich gut, was der Abschnitt „Was du zeigen willst“ meint: Wenn das Modell Schritt für Schritt vorgeht, wird es zuverlässiger, und man kann es leichter prüfen. Teilnehmende können die Tabelle von Opus in 30 Sekunden selbst nachzählen.
3. **Mehrdeutige Fragen sind eine eigene Lehre.** Die Frage sagt nicht, ob das große „E“ zählt. Alle Modelle haben das erkannt und beide Zahlen genannt. Opus bringt zusätzlich die Umlaut-Frage auf. Gute Überleitung: „Unklare Frage, unklare Antwort – sagt genau, was ihr wollt.“
4. **Werkzeuge zählen anders als man denkt.** Strg+F meldet 10 (ohne Unterscheidung von Groß/Klein). Auch das Prüfwerkzeug muss man verstehen. In Excel zählt `=LÄNGE(A1)-LÄNGE(WECHSELN(A1;"e";""))` genau die kleinen „e“ (9), weil WECHSELN Groß-/Kleinschreibung beachtet.
5. **Nur Sonnet weist selbst auf seine Grenzen hin.** Das lässt sich zeigen: Ein Modell, das zur Prüfung rät, ist vertrauenswürdiger als eins, das nur eine Zahl liefert.
6. **Wenn der Fehler live gezeigt werden soll:** Den Prompt verschärfen (siehe Korrekturvorschlag unten) und vorher testen. Ein Screenshot als Backup bleibt wichtig.

---

## Probleme im Material und Vorschläge

- **Prompt B löst den Fehler kaum aus.** Ohne „Antworte nur mit der Zahl“ zählen moderne Modelle von selbst Wort für Wort und liegen richtig. Prompt A hat diesen Zusatz, Prompt B nicht. Der Text „vor allem, wenn es ‚ohne Rechenweg‘ antworten soll“ passt deshalb nur zu Prompt A.
- **Vorschlag für eine fehleranfälligere Variante (nicht mitgetestet, vorher prüfen):**
  ```
  Wie oft kommt der Buchstabe „e“ in diesem Satz vor? Antworte nur mit der Zahl, ohne Erklärung: „Die Nordlicht Technik GmbH liefert Steuergehäuse an Kunden in ganz Europa.“
  ```
  Noch fehleranfälliger ist ein längerer Absatz (z. B. 4–5 Sätze aus [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md)). Die richtige Zahl dann vorher per Excel-Formel ermitteln.
- **Merksatz ergänzen:** „Taschenrechner oder Tabellenkalkulation“ passt gut zum Rechnen. Fürs Zählen hilft ein konkreter Hinweis: „Suchfunktion (Strg+F) oder Excel-Formel – und dabei auf Groß-/Kleinschreibung achten.“
- **Lösungshinweis ergänzen:** In der Klammer zur richtigen Lösung den Satz ergänzen: „Strg+F in Word/Browser zeigt 10, weil es Groß-/Kleinschreibung ignoriert.“

---

## Gesprächsprotokolle

### Modell: Claude Haiku

**Nutzer 1**

Wie oft kommt der Buchstabe „e“ in diesem Satz vor: „Die Nordlicht Technik GmbH liefert Steuergehäuse an Kunden in ganz Europa.“

**Assistent 1**

Der Buchstabe „e“ kommt **10-mal** vor, wenn man das große „E“ in „Europa“ mitzählt. Klein geschrieben sind es 9 „e“:

- Die: 1
- Technik: 1
- liefert: 2
- Steuergehäuse: 4
- Kunden: 1
- Europa: 1 (großes „E“)

---

### Modell: Claude Sonnet

**Nutzer 1**

Wie oft kommt der Buchstabe „e“ in diesem Satz vor: „Die Nordlicht Technik GmbH liefert Steuergehäuse an Kunden in ganz Europa.“

**Assistent 1**

Ich habe Wort für Wort gezählt:

- Die: 1
- Nordlicht: 0
- Technik: 1
- GmbH: 0
- liefert: 2
- Steuergehäuse: 4 (Ste-u-e-rg-e-häus-e)
- an: 0
- Kunden: 1
- in: 0
- ganz: 0
- Europa: 0 als kleines „e“. Das große „E“ am Anfang kommt dazu, wenn man die Groß-/Kleinschreibung ignoriert.

Das ergibt **9 kleine „e“**. Zählt man das große „E“ in „Europa“ mit, sind es **10**.

Ich bin ein Sprachmodell und zähle Buchstaben nicht immer fehlerfrei. Wenn die Zahl wichtig ist, prüfen Sie sie mit der Suchfunktion (Strg+F) in Word oder im Browser.

---

### Modell: Claude Opus

**Nutzer 1**

Wie oft kommt der Buchstabe „e“ in diesem Satz vor: „Die Nordlicht Technik GmbH liefert Steuergehäuse an Kunden in ganz Europa.“

**Assistent 1**

Im Satz steht das „e“ **10-mal**, wenn man das große „E“ mitzählt. Nur kleine „e“ sind es **9**.

So habe ich Wort für Wort gezählt:

| Wort | Anzahl „e“ |
|---|---|
| Die | 1 |
| Nordlicht | 0 |
| Technik | 1 |
| GmbH | 0 |
| liefert | 2 (li**e**f**e**rt) |
| Steuergehäuse | 4 (St**e**u**e**rg**e**häus**e**) |
| an | 0 |
| Kunden | 1 |
| in | 0 |
| ganz | 0 |
| Europa | 1 (großes **E**) |
| **Summe** | **10** |

Das „ä“ in „Steuergehäuse“ habe ich nicht als „e“ gezählt. Wenn Sie es als „ae“ schreiben, also „Steuergehaeuse“, kommt ein „e“ dazu und es sind 11.

---

Zurück zur [Demo-Sammlung](../07_Beispielmaterial/demo_fehler_zeigen.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md)
