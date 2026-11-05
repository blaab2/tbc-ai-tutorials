# Testlauf: Übung 3 / Station D Für Schnelle – Bereinigung selbst in Excel

**Herkunft:** [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md), Station D, Abschnitt „Für Schnelle“, dritter Punkt („Lass dir erklären, wie du die Bereinigung **selbst in Excel** machen würdest (z. B. Duplikate entfernen, Text in Spalten)“). Dazu [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md), Station D („Zusatzaufgaben für Schnelle: Erstelle eine Excel-Anleitung, wie ich Dubletten selbst finde“). Material: [lieferantenliste_unsortiert.csv](../07_Beispielmaterial/lieferantenliste_unsortiert.csv).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf:** Im selben Gespräch kam zuerst der Basis-Prompt von Station D (Analyse ohne Änderung), danach die Excel-Frage. Das Übungsblatt gibt für diese Aufgabe **keinen fertigen Prompt** vor. Er wurde aus der Aufgabenbeschreibung abgeleitet:

```text
Erkläre mir, wie ich die Bereinigung selbst in Excel machen würde, z. B. Duplikate entfernen und Text in Spalten. Schritt für Schritt für die deutsche Excel-Version.
```

**Was herauskommen soll (Prüfmaßstab):**

- Verständliche Schritt-für-Schritt-Anleitung mit **deutschen** Menüpfaden und Funktionsnamen: Daten → Aus Text/CSV, Daten → Text in Spalten, Daten → Duplikate entfernen, GLÄTTEN, GROSS2/GROSS/KLEIN, WECHSELN, DATUM, ggf. Bedingte Formatierung → Doppelte Werte.
- Hinweis: CSV über **Daten → Aus Text/CSV** mit Semikolon und UTF-8 importieren, **nicht per Doppelklick** öffnen (Excel deutet Datumsangaben um, z. B. „März 2024“ → 01.03.2024; die Datei hat außerdem kein BOM, Umlaute werden beim Doppelklick falsch angezeigt). Das Übungsblatt warnt selbst davor („Excel verändert beim Öffnen gern Datumsformate“).
- Hinweis, dass **Duplikate entfernen** nur exakt gleiche Werte erkennt: Müller/Mueller, „&“/„und“, ELEKTRO KRAUSE/Elektro Krause werden **nicht** gefunden, solange man über den Firmennamen geht.

**Eigene Prüfung der Quelle (python3/awk):** 27 Datenzeilen + Kopfzeile, Datei endet mit einem Zeilenumbruch (keine zusätzliche Leerzeile), Kodierung UTF-8 **ohne BOM**. Dubletten = Datenzeilen 1/7, 2/10, 3/14, 4/18 (Excel-Zeilen 2/8, 3/11, 4/15, 5/19). Wichtig für die Excel-Anleitungen:

- Müller/Mueller haben **dieselbe E-Mail**, aber **unterschiedlich geschriebene Telefonnummern** (`0000 111201` vs. `0000-111201`).
- **Zwei Zeilen haben eine leere E-Mail** (Hoffmann Logistik, Krüger Gummiwaren). „Duplikate entfernen“ wertet leere Zellen untereinander als gleich. Wer nur die Spalte E-Mail anhakt, verliert dabei **auch Krüger Gummiwaren** (5 statt 4 Zeilen entfernt, 22 statt 23 übrig). Die bedingte Formatierung „Doppelte Werte“ markiert leere Zellen dagegen nicht. *(Verhalten von Excel; vor dem Kurs einmal in der eigenen Excel-Version nachstellen.)*

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Analyse: 27 Zeilen, 4 richtige Paare, 23 Lieferanten | ja | ja | ja |
| Zeilennummern korrekt | **nein** – fast alle um 1 verschoben, „Zeile 29“ gibt es nicht | ja (Datenzeilen) | ja (Datenzeilen) |
| Import über Daten → Aus Text/CSV, Semikolon | ja | ja, plus UTF-8 | ja, plus UTF-8 |
| Warnung vor Doppelklick wegen **Datumsumdeutung** | nein (nur Import empfohlen, ohne Grund) | **nein** – nennt nur Umlaute, Doppelklick „funktioniert oft auch“ | **ja** („macht aus Zahlen und Datumsangaben ungefragt etwas Falsches“) |
| Text in Spalten (Menüpfad, Dialogschritte) | ja | ja | ja, zusätzlich als Rettung bei „alles in Spalte A“ |
| Duplikate entfernen (Menüpfad, Spaltenauswahl) | ja | ja | ja |
| Hinweis: Duplikate entfernen scheitert an Schreibweisen | **nur indirekt** („egal wie der Firmenname geschrieben ist“) | **ja**, schon in Antwort 1 und erneut in Schritt 6 | **ja**, mit Müller/Mueller als Beispiel |
| Vorgeschlagene Duplikat-Spalten finden genau die 4 Paare | **nein** – E-Mail + Telefon findet Müller/Mueller nicht (3 statt 4) | **nein** – nur E-Mail löscht auch Krüger (5 statt 4), behauptet 27 → 23 | **nein** – nur E-Mail löscht auch Krüger, behauptet „sollten es 4 sein“ |
| Erst markieren, dann löschen (Bedingte Formatierung) | ja | ja | ja, plus „Excel behält die erste Zeile“ |
| Funktionen: GLÄTTEN / GROSS2 / GROSS / WECHSELN / DATUM | GLÄTTEN; WECHSELN, ZÄHLENWENN nur als Tipp | GLÄTTEN, GROSS2 | GLÄTTEN, GROSS2, GROSS, WECHSELN, WERT, DATUM |
| Mehrdeutige Daten (03/02/2024, „März 2024“) als Handarbeit markiert | ja | ja | ja, mit Spalte „Bemerkung“ |
| Falsche oder unsinnige Bedienschritte | 3 | 1 kleiner | 1 kleiner |
| Verständlich für Nicht-Entwickler | gut | gut, etwas lang | gut, am längsten, aber am besten gegliedert |

**Gesamturteil:** Die Aufgabe funktioniert. Alle drei Modelle liefern brauchbare deutsche Anleitungen mit korrekten Hauptmenüpfaden. Opus erfüllt die Prüfkriterien am vollständigsten, Sonnet knapp dahinter, Haiku enthält mehrere falsche Bedienschritte. **Alle drei** übersehen aber eine Falle, die in genau dieser Datei steckt: Ihre Spaltenwahl bei „Duplikate entfernen“ liefert nicht die behaupteten 4 Treffer. Das ist ein sehr guter Prüfmoment für die Auswertung.

---

## Gefundene Fehler mit Beleg

**Alle drei Modelle – Spaltenwahl bei „Duplikate entfernen“**
- Haiku: „Nur die Spalten auswählen, … z. B. **E-Mail** und **Telefon**. Dubletten mit gleicher E-Mail und Telefon werden dann erkannt“. In der CSV stehen bei Müller `0000 111201` und bei Mueller `0000-111201`. Ohne vorheriges Vereinheitlichen der Telefonnummern (schlägt Haiku nicht vor) bleibt dieses Paar stehen. Ergebnis: 3 statt 4 Zeilen entfernt.
- Sonnet: „hier **E-Mail** … aus 27 Zeilen würden 23“. Opus: „Setzen Sie dann nur den Haken bei **E-Mail** … Bei dieser Liste sollten es **4** sein.“ Hoffmann Logistik (Datenzeile 6) und Krüger Gummiwaren (Datenzeile 23) haben beide eine leere E-Mail. „Duplikate entfernen“ behandelt diese als doppelt und löscht Krüger. Ergebnis: 5 entfernt, 22 übrig, ein echter Lieferant ist weg. Beide Modelle erwähnen die leeren E-Mails sogar, aber nur für die bedingte Formatierung (dort stimmt der Hinweis). Opus’ Alternative „E-Mail und Telefon“ würde funktionieren, weil Opus vorher in Schritt 3 „0000-“ durch „0000 “ ersetzen lässt.

**Haiku**
- **Zeilennummern um 1 verschoben**, obwohl Haiku ausdrücklich „Excel-Zeilen 2 bis 28“ ansagt. Belege (Excel-Zeile laut CSV in Klammern): Lackierwerk Ost „Zeile 7“ (6), Hoffmann „8“ (7), Bauer „10“ (9), Becker „14“ (13), Keller „18“ (17), Richter „19“ (18), Schwarz „22“ (21), Krüger „25“ (24), Wolf „26“ (25), Koch „28“ (27), Schäfer „**29**“ (28, eine Zeile 29 gibt es nicht). Dubletten „2 und 9“ (2 und 8), „3 und 12“ (3 und 11), „4 und 16“ (4 und 15), „5 und 20“ (5 und 19).
- Unklarer Satz: „Keine Dublette ist dagegen Zeile 6 (Lackierwerk Ost) oder Zeile 15 (Elektro Krause ist eine andere Firma als Fischer Kabelkonfektion)“ – vermischt zwei Aussagen, Lackierwerk hat kein ähnliches Gegenstück.
- Schritt 5: „Danach `,` (Komma) durch `,` ersetzen (Dezimalkomma bleibt)“ – ein Ersetzen durch sich selbst ist ein sinnloser Schritt.
- Schritt 5: „Mit **Format > Zelle > Zahl**“ – diesen Menüpfad gibt es in der deutschen Excel-Version nicht. Richtig: Strg + 1 bzw. Start → Format → Zellen formatieren.
- Schritt 7: „Im Filter **Leerzeichen** abwählen, damit nur leere Zellen übrig bleiben“ – falsch und widersprüchlich. Der Eintrag heißt „(Leere)“, und man muss **nur diesen auswählen**, nicht abwählen.
- Kleinigkeit: Nach „Daten > Aus Text/CSV > Laden“ liegt bereits eine Tabelle vor, „Strg + T“ ist dann überflüssig. „Datei als Kopie speichern“ steht vor dem Import (Reihenfolge holprig).

**Sonnet**
- Doppelklick: „Ein Doppelklick auf die CSV-Datei funktioniert bei einer deutschen Excel-Version oft auch, zeigt Umlaute aber manchmal falsch an.“ Der Umlaut-Hinweis stimmt (Datei ohne BOM), aber die Datumsumdeutung fehlt. Das widerspricht dem Übungsblatt („**nicht** in Excel – Excel verändert beim Öffnen gern Datumsformate“) und verharmlost den Doppelklick.
- „Die Datei hat am Ende eine leere Zeile.“ – Die Datei endet mit einem normalen Zeilenumbruch nach der letzten Datenzeile (`…;8.900;b\n`), es gibt keine zusätzliche Leerzeile. Im Texteditor steht der Cursor nach Strg + Ende allerdings tatsächlich in Zeile 29 (siehe „Probleme im Material“).
- Kleinigkeit: „Rechtsklick auf Spaltenkopf > Zellen einfügen“ – im Kontextmenü des Spaltenkopfs heißt der Eintrag „Einfügen“. „Spaltendatenformat“ heißt im Dialog „Datenformat der Spalten“ (auch bei Haiku).
- Kleinigkeit: Schritt 7 füllt leere Zellen mit „k. A.“. Die Station D verlangt „FEHLT“. Würde man das vor Schritt 6 machen, wären die beiden leeren E-Mails erst recht identisch.

**Opus**
- Siehe oben („sollten es 4 sein“).
- Lücke: Opus warnt richtig, dass GROSS2 „Neustadt A. D. Probe“ erzeugt, die Ersetzungsliste in Schritt 3 deckt aber nur „a.d.“ und „an der“ ab. Die Zellen, die ursprünglich „Neustadt a. d. Probe“ bzw. „neustadt a. d. probe“ hießen, bleiben als „Neustadt A. D. Probe“ stehen, wenn man die Liste wörtlich abarbeitet.
- Kleinigkeit: „Wenn Sie die CSV per Doppelklick öffnen, landet oft alles in Spalte A“ – bei deutscher Ländereinstellung ist das Semikolon das Listentrennzeichen, die Spalten werden beim Doppelklick meist richtig getrennt. Der Datumshinweis im selben Satz stimmt.

**Nicht erfunden:** Keine erfundenen Werte oder Lieferanten. Alle Firmennamen, Datums- und Betragsbeispiele stimmen mit der CSV überein (abgeglichen mit awk/python3). Die Hauptmenüpfade (Daten → Aus Text/CSV, Daten → Text in Spalten, Daten → Duplikate entfernen, Start → Bedingte Formatierung → Regeln zum Hervorheben von Zellen → Doppelte Werte) sind bei allen drei richtig.

---

## Lehren für die Auswertung

1. **Auch eine gute Anleitung ausprobieren.** Alle drei Anleitungen klingen kompetent. Wer sie in Excel ausführt, merkt: Mit „nur E-Mail“ verschwindet Krüger Gummiwaren, mit „E-Mail + Telefon“ bleibt Müller/Mueller stehen. Die Lehre aus Station D („Prüfe besonders genau“) gilt also auch für Anleitungen, nicht nur für Tabellen. Gute Frage an die Gruppe: „Wie viele Zeilen hat Excel bei euch entfernt? Und welche?“
2. **Die Zählregel greift wieder:** Vorher 27, Dubletten 4, nachher müssen es 23 sein. Wer 22 hat, sucht den fehlenden Lieferanten. Wer 24 hat, sucht das übersehene Paar. So wird der Prüfschritt der Station direkt in Excel geübt.
3. **Excel ist nicht automatisch schlauer.** „Duplikate entfernen“ findet nur exakt Gleiches. Sonnet und Opus sagen das deutlich, Haiku nur zwischen den Zeilen. Gute Kombination: KI für die Analyse (erkennt Müller/Mueller als gleich), Excel für das sichere, nachvollziehbare Ausführen.
4. **Erst markieren, dann löschen.** Alle drei empfehlen die bedingte Formatierung „Doppelte Werte“ vor dem Löschen. Das ist das sicherste Vorgehen und lässt sich gut vorzeigen.
5. **Doppelklick-Falle:** Nur Opus begründet den Import mit der Datumsumdeutung. Sonnet verharmlost den Doppelklick. Brücke zum Übungsblatt: „Warum sollte man die CSV nicht per Doppelklick öffnen?“
6. **Modellunterschied bei Bedienschritten:** Haiku nennt Menüs, die es nicht gibt („Format > Zelle > Zahl“), und einen widersprüchlichen Filterschritt. Daran lässt sich zeigen, dass auch Anleitungen erfundene Details enthalten können. Rückfrage-Tipp: „Ich finde den Menüpunkt nicht. Wo genau steht er in Excel 365?“
7. **Zeitbedarf:** Lesen der Anleitung 3–5 Minuten, Ausprobieren in Excel 10–15 Minuten. Passt für Schnelle, wenn die Basis schon fertig ist.

---

## Probleme im Material

- **Kein fertiger Prompt:** Der dritte „Für Schnelle“-Punkt ist nur beschrieben. Für Nicht-Entwickler wäre ein kopierbarer Prompt hilfreich, ebenso der Hinweis „und probiere es in Excel aus“.
- **Lösungshinweise ohne Erwartung für diese Aufgabe:** Die Trainer-Lösungshinweise nennen die Zusatzaufgabe („Erstelle eine Excel-Anleitung, wie ich Dubletten selbst finde“ und ausprobieren), beschreiben aber nicht, was ein gutes Ergebnis ist. Es fehlt der Hinweis auf die leeren E-Mail-Zellen (Hoffmann, Krüger) und die abweichende Telefonnummer Müller/Mueller. Genau daran scheitern alle drei Modelle.
- **Prüfschritt „Zeilen zählen“ (Übungsblatt):** „Im Texteditor mit Strg + Ende ans Dateiende springen – unten in der Statusleiste steht die Zeilennummer. Die Kopfzeile … nicht mitzählen.“ Da die Datei mit einem Zeilenumbruch endet, zeigen Editor/Notepad nach Strg + Ende **Zeile 29**. Minus Kopfzeile käme man auf 28 statt 27. (Gilt auch für die Basis-Aufgabe, nicht nur für diese Teilaufgabe.)

---

## Gesprächsprotokolle

### Haiku

#### Nutzer 1
Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.

#### Assistent 1
**1. Anzahl Zeilen:** Die Liste hat 27 Datenzeilen (Excel-Zeilen 2 bis 28), ohne Kopfzeile.

**2. Probleme**

- **Datumsformate uneinheitlich:** `12.03.2024`, `2024-02-28`, `5.1.24` (zweistelliges Jahr), `März 2024`, `Dez. 2023`, `April 2024`, `15/01/2024`, `03/02/2024`, `7.4.2024`. Besonders heikel ist `03/02/2024` (Braun Transporte): Das kann 3. Februar oder 2. März sein. Bei `15/01/2024` ist nur TT/MM/JJJJ sinnvoll. Bei Monatsangaben ohne Tag (`März 2024`, `Dez. 2023`, `April 2024`) fehlt der Tag ganz.
- **Zahlenformate uneinheitlich:** `48.500,00`, `12.300`, `31 200 €`, `22750,5`, `9800`, `6.250`, `41.000 EUR`, `63.200 €`, `11.300 EUR`. Mal Punkt als Tausendertrennzeichen, mal Leerzeichen, mal Komma als Dezimaltrennzeichen, mal Währungszeichen. `6.250` (Zimmermann) ist ohne Kontext mehrdeutig: 6250 oder 6,25.
- **Fehlende oder ungültige Werte:**
  - Ansprechpartner fehlt: Zeile 7 (Lackierwerk Ost), Zeile 22 (Schwarz Gießerei)
  - E-Mail fehlt: Zeile 8 (Hoffmann Logistik), Zeile 25 (Krüger Gummiwaren)
  - Telefon fehlt: Zeile 14 (Becker Werkzeugbau)
  - Letzte Bestellung fehlt: Zeile 18 (Keller Dichtungstechnik)
  - Jahresumsatz fehlt: Zeile 28 (Koch Elektronik)
  - Jahresumsatz `n/a`: Zeile 19 (Richter Glas & Optik)
  - Bewertung fehlt: Zeile 10 (Bauer Präzisionsteile), Zeile 18 (Keller Dichtungstechnik)
- **Bewertung uneinheitlich:** Meist `A`, `B`, `C`, aber Zeile 26 (Wolf Messtechnik) hat `a` und Zeile 29 (Schäfer Schweißtechnik) hat `b`.
- **Telefonnummern:** `0000 111201` und `0000-111201` werden unterschiedlich geschrieben.
- **Ortsangaben uneinheitlich:** `Beispielstadt`/`MUSTERHAUSEN`/`musterhausen`/`Musterhausen`, `Neustadt a. d. Probe`/`Neustadt a.d. Probe`/`Neustadt an der Probe`/`neustadt a. d. probe`, `fiktivhausen`/`Fiktivhausen`.
- **Warengruppen uneinheitlich:** `Elektrokomponenten` vs. `Elektro` vs. `Elektronik`, `Schrauben/Normteile` vs. `Normteile`, `Kunststoffteile` vs. `Kunststoff`.
- **Firmennamen und Anreden uneinheitlich:** `Schmidt & Söhne KG` vs. `Schmidt und Söhne KG`, `ELEKTRO KRAUSE GmbH` (Großschreibung), `Hr. Krause` statt `Herr Krause`, `Dr. Weber` / `Frau Dr. Weber`.
- **Leerzeichen und Sonstiges:** Vermutlich überflüssige Leerzeichen oder unsichtbare Zeichen, die ich aus dem Text nicht sicher erkennen kann. Das prüft man am besten in Excel mit `GLÄTTEN`.

**3. Mögliche Dubletten**

- **Zeile 2 und Zeile 9 – Müller Stahlhandel GmbH / Mueller Stahlhandel:** Gleiche E-Mail (`brandt@stahl-mueller.example.com`), gleiche Telefonnummer (nur anders formatiert), gleicher Ort, gleiche Warengruppe (Stahl), gleiches Datum (12.03.2024) und gleicher Umsatz (48.500). Der Ansprechpartner ist derselbe (Herr K. Brandt). Sehr wahrscheinlich eine Dublette, wobei `Müller` und `Mueller` die gleiche Firma sind.
- **Zeile 3 und Zeile 12 – Schmidt & Söhne KG / Schmidt und Söhne KG:** Gleiche E-Mail, gleiche Telefonnummer, gleicher Ort, gleiche Warengruppe (Normteile), gleiches Datum (28.02.2024), gleicher Umsatz (12.300). Sehr wahrscheinlich eine Dublette.
- **Zeile 4 und Zeile 16 – Elektro Krause / ELEKTRO KRAUSE GmbH:** Gleiche E-Mail, gleiche Telefonnummer, gleiches Datum (5.1.24 = 05.01.2024), gleicher Umsatz (31 200 € = 31.200,00), gleiche Bewertung (A). Sehr wahrscheinlich eine Dublette.
- **Zeile 5 und Zeile 20 – Weber Kunststofftechnik / Weber Kunststoff-Technik GmbH:** Gleiche E-Mail, gleiche Telefonnummer, gleicher Ort, gleicher Umsatz (22.750,50 = 22750,5), gleiche Bewertung (B). Das Datum März 2024 und 2024-03-01 passen zusammen. Sehr wahrscheinlich eine Dublette.

Keine Dublette ist dagegen Zeile 6 (Lackierwerk Ost) oder Zeile 15 (Elektro Krause ist eine andere Firma als Fischer Kabelkonfektion). Die Dubletten-Einschätzung beruht auf der E-Mail-Adresse und der Telefonnummer. Für eine sichere Aussage sollte man die Paare kurz mit dem Einkauf abgleichen.

Ergebnis: 4 wahrscheinliche Dublettenpaare. Nach dem Entfernen wären es 23 eindeutige Lieferanten.

Ich habe die Datei nicht verändert.

#### Nutzer 2
Erkläre mir, wie ich die Bereinigung selbst in Excel machen würde, z. B. Duplikate entfernen und Text in Spalten. Schritt für Schritt für die deutsche Excel-Version.

#### Assistent 2
Hier ist ein Vorgehen für die deutsche Excel-Version (Windows, sinngemäß auch Excel für Mac). Arbeite am besten mit einer Kopie der Datei.

**Vorbereitung**

1. Datei als Kopie speichern, z. B. `lieferantenliste_bereinigt.xlsx`.
2. CSV öffnen über **Daten > Aus Text/CSV**. Als Trennzeichen **Semikolon** wählen und mit **Laden** bestätigen. So bleiben die Spalten sauber getrennt.
3. Die Daten als Tabelle formatieren: **Strg + T**, Haken bei „Tabelle hat Überschriften“.

**Schritt 1: Leerzeichen entfernen**

Damit Vergleiche funktionieren, zuerst überflüssige Leerzeichen entfernen.

1. Freie Spalte rechts neben den Daten anlegen, z. B. Spalte K.
2. In K2 eingeben: `=GLÄTTEN(A2)` und nach unten kopieren.
3. Werte kopieren und mit **Einfügen > Werte** (Strg + Alt + V, dann W) über die Originalspalte einfügen.

**Schritt 2: Duplikate entfernen**

1. Auf eine Zelle in der Tabelle klicken.
2. **Daten > Datentools > Duplikate entfernen**.
3. Nur die Spalten auswählen, die zur Identifikation taugen, z. B. **E-Mail** und **Telefon**. Dubletten mit gleicher E-Mail und Telefon werden dann erkannt, egal wie der Firmenname geschrieben ist.
4. Mit **OK** bestätigen. Excel zeigt, wie viele Zeilen entfernt wurden.

Achtung: Diese Funktion löscht Zeilen endgültig. Vorher unbedingt die Kopie haben. Besser ist oft, die Dubletten zuerst zu markieren (siehe unten) und sie vor dem Löschen zu prüfen.

**Alternative: Dubletten nur markieren**

1. Markierung der Spalte E-Mail.
2. **Start > Bedingte Formatierung > Regeln zum Hervorheben von Zellen > Doppelte Werte**.
3. Doppelte E-Mail-Adressen werden farbig angezeigt. So siehst du, welche Zeilen zusammengehören, und entscheidest selbst.

**Schritt 3: Text in Spalten (z. B. Telefonnummern oder Datum)**

Beispiel: Ein Feld enthält „Vorname Nachname“ und soll getrennt werden.

1. Spalte markieren.
2. **Daten > Datentools > Text in Spalten**.
3. **Getrennt** wählen, dann **Weiter**.
4. Trennzeichen **Leerzeichen** oder **Semikolon** auswählen.
5. Ziel festlegen, z. B. eine leere Spalte rechts davon, und mit **Fertig stellen** bestätigen.

**Schritt 4: Datumsformate vereinheitlichen**

Bei Datumswerten, die als Text vorliegen, hilft **Text in Spalten** mit Datumsformat:

1. Datumsspalte markieren, dann **Daten > Text in Spalten > Getrennt > Weiter > Weiter**.
2. Bei **Spaltendatenformat** auf **Datum** stellen und die Reihenfolge wählen, z. B. **TMJ** für Tag.Monat.Jahr.
3. Fertig stellen.

Bei Einträgen wie `März 2024` funktioniert das nicht automatisch. Solche Zellen manuell auf den ersten des Monats setzen (z. B. `01.03.2024`) oder in einer Hilfsspalte mit `=DATWERT()` umrechnen. Bei `03/02/2024` musst du selbst entscheiden, ob es der 3. Februar oder der 2. März ist.

**Schritt 5: Zahlen vereinheitlichen (Umsatz)**

1. Den Bereich markieren und **Strg + H** (Suchen und Ersetzen) öffnen.
2. Zuerst `€` durch nichts ersetzen. Dann `EUR` durch nichts ersetzen. Dann Leerzeichen durch nichts ersetzen.
3. Danach `.` (Punkt) durch nichts ersetzen, also den Tausenderpunkt entfernen.
4. Danach `,` (Komma) durch `,` ersetzen (Dezimalkomma bleibt). Mit **Format > Zelle > Zahl** die Spalte auf Zahl mit zwei Dezimalstellen setzen.

Achtung: Bei `6.250` muss man entscheiden, ob es 6250 oder 6,25 meint. In dieser Datei ist 6250 sinnvoll. Vorher Stichprobe machen.

**Schritt 6: Schreibweisen vereinheitlichen**

- Für Orte und Warengruppen Filter nutzen: **Daten > Filter**, dann die Spalte aufklappen. Excel zeigt alle Varianten an. Bei Abweichungen mit **Strg + H** ersetzen, z. B. `MUSTERHAUSEN` durch `Musterhausen`.
- Bewertung: Filter nutzen und `a` durch `A` und `b` durch `B` ersetzen.
- Für Dubletten in Firmennamen wie `Müller` vs. `Mueller` nicht automatisch ersetzen. Die Entscheidung trifft man besser selbst.

**Schritt 7: Fehlende Werte prüfen**

1. Filter auf die Spalte setzen.
2. Im Filter **Leerzeichen** abwählen, damit nur leere Zellen übrig bleiben.
3. Diese Zeilen von Hand prüfen oder ergänzen.

**Tipp:** Wenn du mit Formeln arbeiten willst, helfen `=WECHSELN()`, `=GLÄTTEN()` und `=ZÄHLENWENN()`. Mit `=ZÄHLENWENN(E:E;E2)>1` markierst du doppelte E-Mail-Adressen in einer Hilfsspalte.

Wenn du möchtest, kann ich dir als Nächstes für eine bestimmte Spalte die passende Formel oder die genauen Menüschritte für deine Excel-Version aufschreiben.

### Sonnet

#### Nutzer 1
Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.

#### Assistent 1
Ich habe die Datei gelesen und nichts verändert.

**1. Anzahl der Zeilen**
Die Liste hat **27 Datenzeilen** ohne Kopfzeile. Sie hat 9 Spalten: Lieferant, Ansprechpartner, Ort, Telefon, E-Mail, Warengruppe, Letzte Bestellung, Jahresumsatz EUR, Bewertung.

**2. Probleme**

*Datumsformate (Spalte "Letzte Bestellung")*
- Deutsches Format mit Punkten: `12.03.2024`, `01.04.2024`.
- ISO-Format: `2024-02-28`, `2024-03-12`, `2024-04-08`.
- Nicht eindeutig oder ohne Tag: `5.1.24`, `7.4.2024`, `15/01/2024`, `03/02/2024`. Der letzte Wert kann der 3. Februar oder der 2. März sein. Bei Slash-Formaten ist unklar, ob Tag/Monat oder Monat/Tag gemeint ist.
- Nur Monat: `März 2024`, `Dez. 2023`, `April 2024`. Der Tag fehlt.
- Leer: Keller Dichtungstechnik.

*Umsatzwerte (Spalte "Jahresumsatz EUR")*
- Verschiedene Schreibweisen: `48.500,00`, `12.300`, `31 200 €`, `9800`, `18.400,00 €`, `48500`, `12300,00`, `41.000 EUR`, `22750,5`, `63.200 €`, `11.300 EUR`.
- Der Punkt ist teils Tausendertrenner (`12.300`), teils fehlt er (`9800`). Das Komma ist teils Dezimaltrenner, teils fehlt es.
- Währungszusätze (`€`, `EUR`) stehen im Zahlenfeld, obwohl die Spaltenüberschrift die Währung schon nennt. Excel erkennt solche Werte als Text.
- Platzhalter statt Zahl: `n/a` (Richter Glas & Optik).
- Leer: Koch Elektronik.

*Schreibweisen und Groß-/Kleinschreibung*
- Orte:
  - Groß-/Kleinschreibung: `musterhausen`, `MUSTERHAUSEN`, `fiktivhausen`, `neustadt a. d. probe`.
  - Abkürzung: `Neustadt a. d. Probe`, `Neustadt a.d. Probe` und `Neustadt an der Probe` meinen denselben Ort.
- Firmennamen: `Schmidt & Söhne KG` und `Schmidt und Söhne KG`, `Müller` und `Mueller`, `Weber Kunststofftechnik` und `Weber Kunststoff-Technik GmbH`, `Elektro Krause` und `ELEKTRO KRAUSE GmbH`.
- Ansprechpartner: Anreden und Formen sind uneinheitlich (`Herr K. Brandt` und `K. Brandt`, `Frau Lea Schmidt` und `Lea Schmidt`, `Herr Krause` und `Hr. Krause`, `Frau Dr. Weber` und `Dr. Weber`).
- Telefon: `0000 111201` und `0000-111201` haben unterschiedliche Trennzeichen.
- Warengruppen: Dieselbe Gruppe heißt unterschiedlich, z. B. `Schrauben/Normteile` und `Normteile`, `Kunststoffteile` und `Kunststoff`, `Elektrokomponenten` und `Elektro`.
- Bewertung: Kleinbuchstaben `a` (Wolf Messtechnik) und `b` (Schäfer Schweißtechnik) statt `A` und `B`.

*Fehlende Werte*
- Ansprechpartner fehlt: Lackierwerk Ost, Schwarz Gießerei.
- E-Mail fehlt: Hoffmann Logistik, Krüger Gummiwaren.
- Telefon fehlt: Becker Werkzeugbau.
- Bewertung fehlt: Bauer Präzisionsteile, Keller Dichtungstechnik.
- Letzte Bestellung fehlt: Keller Dichtungstechnik.
- Umsatz fehlt oder ist `n/a`: Koch Elektronik, Richter Glas & Optik.

*Sonstiges*
- Die Datei hat am Ende eine leere Zeile.
- Zeichensatz: Umlaute und ß (Müller, Söhne, Gießerei) werden in Excel nur richtig angezeigt, wenn die Datei als UTF-8 importiert wird.

**3. Mögliche Dubletten**
Ich sehe vier Paare:

| Paar | Zeilen (Datenzeile) | Begründung |
|---|---|---|
| Müller Stahlhandel GmbH / Mueller Stahlhandel | 1 und 7 | Gleiche E-Mail (`brandt@stahl-mueller...`), gleiche Telefonnummer (nur anderes Trennzeichen), gleiche Warengruppe, gleiches Datum (12.03.2024), gleicher Umsatz 48.500, gleiche Bewertung A. Der Name ist nur anders geschrieben (ü gegen ue, GmbH fehlt). |
| Schmidt & Söhne KG / Schmidt und Söhne KG | 2 und 10 | Gleiche E-Mail und Telefonnummer, gleiche Ansprechpartnerin, gleiches Datum (28.02.2024), gleicher Umsatz 12.300, gleiche Bewertung B. Nur "&" gegen "und", die Warengruppe und die Ortsschreibung weichen ab. |
| Elektro Krause / ELEKTRO KRAUSE GmbH | 3 und 14 | Gleiche E-Mail und Telefonnummer, gleiches Datum (5.1.24 gleich 05.01.2024), gleicher Umsatz 31.200, gleiche Bewertung A. Nur Groß-/Kleinschreibung, Rechtsform und Ortsschreibung weichen ab. |
| Weber Kunststofftechnik / Weber Kunststoff-Technik GmbH | 4 und 18 | Gleiche E-Mail und Telefonnummer, gleicher Ort, gleicher Umsatz 22.750,50, gleiche Bewertung B. Beim Datum lautet das eine "März 2024", das andere 01.03.2024. Das passt zusammen. |

Wegen der vielen Übereinstimmungen halte ich alle vier Paare für sehr wahrscheinliche Dubletten. Dass dieselbe E-Mail und Telefonnummer vorkommen, ist ein stärkeres Indiz als der Firmenname.

Keine Dubletten sind Fischer Kabelkonfektion und Elektro Krause. Sie liegen zwar im selben Ort und in derselben Warengruppe, haben aber andere Kontaktdaten.

Wichtig: Excel würde diese Paare mit der Funktion "Duplikate entfernen" **nicht** finden. Die Namen und Schreibweisen sind nie exakt gleich. Erst nach dem Vereinheitlichen, oder über eine Spalte wie die E-Mail-Adresse, wird es möglich. Ich würde bei jedem Paar vor dem Löschen prüfen, welche Zeile die vollständigeren Daten hat.

#### Nutzer 2
Erkläre mir, wie ich die Bereinigung selbst in Excel machen würde, z. B. Duplikate entfernen und Text in Spalten. Schritt für Schritt für die deutsche Excel-Version.

#### Assistent 2
Hier ist eine Anleitung für die deutsche Excel-Version (Microsoft 365 oder Excel 2019/2021). Arbeite immer an einer Kopie der Datei.

**Schritt 0: CSV richtig öffnen**
1. Öffne Excel mit einer leeren Arbeitsmappe.
2. Wähle **Daten > Aus Text/CSV**. Falls du das Menü nicht findest: **Daten > Daten abrufen > Aus Datei > Aus Text/CSV**.
3. Wähle die Datei aus. Im Vorschaufenster stellst du **Dateiursprung: 65001: Unicode (UTF-8)** und **Trennzeichen: Semikolon** ein.
4. Klicke auf **Laden**.

Ein Doppelklick auf die CSV-Datei funktioniert bei einer deutschen Excel-Version oft auch, zeigt Umlaute aber manchmal falsch an.

**Schritt 1: Kopie und Hilfsspalten**
1. Speichere die Datei sofort als **.xlsx** unter einem neuen Namen, z. B. `Lieferanten_bereinigt.xlsx`.
2. Lege vor jeder Bearbeitung ein Blatt "Original" an. Dafür **Rechtsklick auf den Blattnamen > Verschieben oder kopieren > Kopie erstellen**.
3. Formatiere die Kopfzeile fett und friere sie ein: **Ansicht > Fenster fixieren > Oberste Zeile fixieren**.

**Schritt 2: Text vereinheitlichen (Groß-/Kleinschreibung, Leerzeichen)**
Dafür brauchst du eine Hilfsspalte. Beispiel für die Spalte "Ort" (Spalte C), Formel in einer neuen Spalte J:
```
=GLÄTTEN(GROSS2(C2))
```
- `GLÄTTEN` entfernt doppelte und überflüssige Leerzeichen.
- `GROSS2` schreibt jedes Wort mit großem Anfangsbuchstaben, also "musterhausen" und "MUSTERHAUSEN" werden zu "Musterhausen".

Dann:
1. Die Formel nach unten ziehen oder doppelklicken auf das Ausfüllkästchen unten rechts.
2. Spalte J markieren und **kopieren** (Strg+C).
3. Auf Spalte C klicken, **Rechtsklick > Einfügen-Optionen > Werte** (das Symbol mit "123").
4. Hilfsspalte J löschen.

Für Abkürzungen im Ort ("a. d.", "an der") nimmst du **Suchen und Ersetzen** (Strg+H), z. B. "a. d." durch "an der" und "a.d." durch "an der".

**Schritt 3: Text in Spalten**
Das brauchst du, wenn mehrere Informationen in einer Zelle stehen, z. B. bei "Herr K. Brandt", wenn du Anrede und Name trennen willst, oder wenn du eine CSV mit einer einzigen Spalte geöffnet hast.
1. Spalte markieren.
2. **Daten > Text in Spalten**.
3. Schritt 1: **Getrennt** wählen, **Weiter**.
4. Schritt 2: Trennzeichen **Leerzeichen** (oder Semikolon) anhaken, **Weiter**.
5. Schritt 3: Mit **Fertig stellen** übernehmen.

**Vorsicht:** Die rechts daneben liegenden Spalten werden überschrieben. Füge vorher leere Spalten ein: **Rechtsklick auf Spaltenkopf > Zellen einfügen**.

Beim Ansprechpartner geht es auch so: Einmal Anrede und Name trennen, dann Anreden vereinheitlichen mit Suchen und Ersetzen ("Hr." durch "Herr").

**Schritt 4: Datumsangaben vereinheitlichen**
1. Prüfe zuerst, welche Zellen Excel als echtes Datum erkannt hat. Echte Daten sind **rechtsbündig**, Text ist **linksbündig**.
2. Bei Textwerten wie `2024-02-28` hilft **Text in Spalten**: Spalte markieren, **Daten > Text in Spalten > Getrennt > Weiter > Weiter**, in Schritt 3 **Spaltendatenformat: Datum** mit **JMT** (Jahr-Monat-Tag) wählen, **Fertig stellen**.
3. Werte mit Slash (`15/01/2024`, `03/02/2024`) oder ohne Tag (`März 2024`, `Dez. 2023`) musst du **von Hand prüfen** oder beim Auftraggeber klären. Das Programm kann bei `03/02/2024` nicht wissen, welcher Monat gemeint ist.
4. Alle Zellen markieren und **Strg+1 > Zahl > Datum > 14.03.2012** wählen. Oder **Benutzerdefiniert** mit `TT.MM.JJJJ`.

**Schritt 5: Umsatz in echte Zahlen umwandeln**
1. Markiere die Spalte. Mit **Suchen und Ersetzen** (Strg+H) entfernst du nacheinander " €", " EUR", "€" und überflüssige Leerzeichen. Lass das Feld "Ersetzen durch" leer.
2. Achtung beim Punkt und Komma: `12.300` ist in der deutschen Excel-Version 12300 (Tausenderpunkt). `22750,5` ist 22750,50. Prüfe Werte wie `9800`, die gar kein Trennzeichen haben.
3. Text, der links in der Zelle steht, wandelst du in eine Zahl um: Klicke auf das gelbe Warnsymbol und wähle **In Zahl umwandeln**. Alternativ gibst du in eine leere Zelle `1` ein, kopierst sie, markierst die Werte und wählst **Rechtsklick > Inhalte einfügen > Multiplizieren**.
4. Formatiere die Spalte mit **Strg+1 > Zahl** (2 Dezimalstellen, 1000er-Trennzeichen).
5. `n/a` ersetzt du durch eine leere Zelle oder einen Hinweis.

**Schritt 6: Duplikate entfernen**
Wie in meiner ersten Antwort beschrieben, wird "Duplikate entfernen" die Paare nur finden, wenn die Werte exakt gleich sind. Gehe so vor:
1. **Vor** dem Entfernen die Daten wie oben vereinheitlichen.
2. Mache eine Kopie des Blattes.
3. Markiere den Datenbereich (Strg+A innerhalb der Tabelle).
4. **Daten > Duplikate entfernen**.
5. Im Dialog setzt du bei "Meine Daten haben Kopfzeilen" den Haken. Dann hakst du nur die Spalten an, die ein Duplikat eindeutig kennzeichnen, hier **E-Mail**. Mit "Alle auswählen" musst du rechnen, dass Zeilen mit leicht abweichender Warengruppe, wie bei Schmidt, stehen bleiben.
6. **OK**. Excel meldet, wie viele doppelte Werte entfernt wurden und wie viele eindeutige Werte bleiben.

Besser und sicherer: Erst prüfen, dann löschen.
1. Markiere die E-Mail-Spalte und wähle **Start > Bedingte Formatierung > Regeln zum Hervorheben von Zellen > Doppelte Werte**.
2. Excel färbt die doppelten Einträge ein. Du siehst, welche Zeilen zusammengehören.
3. Vergleiche die beiden Zeilen und lösche von Hand die unvollständige.
4. Zeilen ohne E-Mail (Hoffmann Logistik, Krüger Gummiwaren) werden durch die Spalte E-Mail nicht erfasst. Prüfe diese über den Namen.

Bei den vier gefundenen Paaren würde dir Excel nach dem Schritt "nur E-Mail" vier doppelte Einträge anzeigen. Das wäre das erwartete Ergebnis, und aus 27 Zeilen würden 23.

**Schritt 7: Fehlende Werte**
1. Markiere die Tabelle. **Start > Suchen und Auswählen > Gehe zu > Inhalte > Leerzellen > OK**. Excel markiert alle leeren Zellen.
2. Gib einen Platzhalter wie "k. A." ein und bestätige mit **Strg+Enter**, so füllst du alle markierten Zellen auf einmal. Du kannst die Zellen auch farbig markieren, um sie später nachzufragen.

**Schritt 8: Abschluss**
1. Sortiere nach Lieferant: **Daten > Sortieren**.
2. Formatiere als Tabelle: **Start > Als Tabelle formatieren**.
3. Speichere als .xlsx. Wenn du wieder eine CSV brauchst: **Datei > Speichern unter > CSV UTF-8 (durch Trennzeichen getrennt)**.

Tipp: Wenn du Schritte öfter brauchst, lohnt sich **Power Query** (**Daten > Aus Tabelle/Bereich**). Dort werden alle Bereinigungsschritte gespeichert und lassen sich bei der nächsten Liste mit einem Klick wiederholen.

### Opus

#### Nutzer 1
Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.

#### Assistent 1
Ich habe die Liste nur gelesen und nichts verändert. Das ist mir aufgefallen:

**1. Anzahl der Zeilen**

Ohne Kopfzeile hat die Liste **27 Datenzeilen**. Vier davon sind sehr wahrscheinlich Dubletten (siehe Punkt 3). Bereinigt bleiben also etwa **23 verschiedene Lieferanten**.

**2. Probleme in der Liste**

**a) Datumsformate (Spalte „Letzte Bestellung“)**
In der Spalte stehen mindestens sieben verschiedene Formate:
- TT.MM.JJJJ, z. B. `12.03.2024`
- ISO-Format JJJJ-MM-TT, z. B. `2024-02-28` (Schmidt & Söhne, Mueller, Schulz, Weber GmbH, Hartmann, Koch)
- Kurzform ohne führende Nullen, z. B. `5.1.24` (Elektro Krause) und `7.4.2024` (Lange)
- Schrägstriche, z. B. `15/01/2024` (Zimmermann) und `03/02/2024` (Braun). **Achtung:** `03/02/2024` ist mehrdeutig. Es kann der 3. Februar oder (amerikanisch gelesen) der 2. März sein.
- Nur Monat und Jahr: `März 2024` (Weber), `Dez. 2023` (Becker), `April 2024` (Wolf). Hier fehlt der Tag.
- Leer: Keller Dichtungstechnik

**b) Jahresumsatz (Spalte „Jahresumsatz EUR“)**
- Die Zahlen sind unterschiedlich geschrieben: `48.500,00`, `48500`, `12300,00`, `22750,5`, `9800`, `31 200 €` (mit Leerzeichen als Tausendertrennung)
- Bei manchen Werten steht eine Einheit dabei, obwohl sie schon im Spaltennamen steht: `€`, `EUR`
- `12.300` und ähnliche Werte könnte Excel je nach Ländereinstellung falsch als 12,3 lesen
- Kein Zahlenwert: `n/a` (Richter Glas & Optik)
- Leer: Koch Elektronik

**c) Schreibweise der Orte**
- Musterhausen: `musterhausen`, `MUSTERHAUSEN`, `Musterhausen`
- Neustadt: `Neustadt a. d. Probe`, `Neustadt a.d. Probe`, `Neustadt an der Probe`, `neustadt a. d. probe`
- Fiktivhausen: `fiktivhausen` und `Fiktivhausen`

**d) Lieferantennamen**
- Die Rechtsform fehlt bei manchen Einträgen (z. B. „Elektro Krause“ und „ELEKTRO KRAUSE GmbH“)
- Umlaute sind uneinheitlich: „Müller“ und „Mueller“
- „&“ steht neben „und“, Großbuchstaben neben normaler Schreibweise

**e) Ansprechpartner**
- Die Anrede ist uneinheitlich: „Herr“, „Hr.“ oder gar keine Anrede („K. Brandt“, „Lea Schmidt“, „Dr. Weber“)
- Mal mit Vorname, mal nur mit Nachname
- Leer bei: Lackierwerk Ost GmbH, Schwarz Gießerei

**f) Telefon**
- Das Format ist uneinheitlich: `0000 111201` und `0000-111201`
- Leer bei: Becker Werkzeugbau

**g) E-Mail**
- Leer bei: Hoffmann Logistik, Krüger Gummiwaren

**h) Warengruppe**
Für die gleiche Sache stehen verschiedene Begriffe da:
- `Schrauben/Normteile` und `Normteile`
- `Elektrokomponenten`, `Elektro` und `Elektronik`
- `Kunststoffteile` und `Kunststoff`

**i) Bewertung**
- Kleinbuchstaben: `a` (Wolf Messtechnik), `b` (Schäfer Schweißtechnik)
- Leer bei: Bauer Präzisionsteile, Keller Dichtungstechnik

**j) Dubletten**
Siehe Punkt 3. Die Dubletten verfälschen jede Auswertung. Wer die Umsätze aufsummiert, zählt diese vier Lieferanten doppelt (zusammen rund 114.750 € zu viel).

**3. Mögliche Dubletten**

| # | Eintrag A (Zeile) | Eintrag B (Zeile) | Begründung |
|---|---|---|---|
| 1 | Müller Stahlhandel GmbH (1) | Mueller Stahlhandel (7) | Gleicher Ansprechpartner (K. Brandt), gleiche E-Mail, gleiche Telefonnummer (nur mit Bindestrich), gleicher Ort, gleiches Datum (12.03.2024 = 2024-03-12), gleicher Umsatz (48.500), gleiche Bewertung A |
| 2 | Schmidt & Söhne KG (2) | Schmidt und Söhne KG (10) | Gleiche Ansprechpartnerin (Lea Schmidt), gleiche E-Mail und Telefonnummer, gleiches Datum (28.02.2024), gleicher Umsatz (12.300), Bewertung B. Nur die Warengruppe ist anders benannt (Schrauben/Normteile und Normteile) |
| 3 | Elektro Krause (3) | ELEKTRO KRAUSE GmbH (14) | Gleiche E-Mail und Telefonnummer, gleicher Ort (anders geschrieben), gleiches Datum (5.1.24 = 05.01.2024), gleicher Umsatz (31.200), Bewertung A |
| 4 | Weber Kunststofftechnik (4) | Weber Kunststoff-Technik GmbH (18) | Gleiche E-Mail und Telefonnummer, Dr. Weber, Fiktivhausen, gleicher Umsatz (22.750,50), Bewertung B. Das Datum passt zusammen („März 2024“ und 2024-03-01) |

Die Zeilennummern zählen die Datenzeilen ohne Kopfzeile.

**Bei diesen Einträgen sehe ich keine Dubletten:**
- Hoffmann Logistik und Braun Transporte: beide Spedition, aber verschiedene Firmen
- Keller Dichtungstechnik und Krüger Gummiwaren: beide Dichtungen, aber verschiedene Firmen

Am zuverlässigsten erkennt man Dubletten an E-Mail-Adresse und Telefonnummer, nicht am Firmennamen.

Soll ich im nächsten Schritt eine bereinigte Fassung vorschlagen? Dann sollten Sie mir vorher sagen, welche Schreibweise jeweils gelten soll, z. B. ob mit oder ohne „GmbH“.

#### Nutzer 2
Erkläre mir, wie ich die Bereinigung selbst in Excel machen würde, z. B. Duplikate entfernen und Text in Spalten. Schritt für Schritt für die deutsche Excel-Version.

#### Assistent 2
Gern. So gehen Sie in der deutschen Excel-Version (Microsoft 365 / Excel 2016 und neuer) vor.

**Schritt 0: Sicherheitskopie**
Speichern Sie zuerst eine Kopie der Originaldatei. Arbeiten Sie dann nur in der Kopie.

---

**Schritt 1: CSV richtig öffnen (Text in Spalten)**

Wenn Sie die CSV per Doppelklick öffnen, landet oft alles in Spalte A. Oder Excel macht aus Zahlen und Datumsangaben ungefragt etwas Falsches. Es gibt zwei Wege:

*Variante A: Import (empfohlen)*
1. Öffnen Sie eine leere Arbeitsmappe.
2. Klicken Sie auf **Daten** → **Aus Text/CSV** und wählen Sie die Datei aus.
3. Stellen Sie im Vorschaufenster ein:
   - **Dateiursprung:** „65001: Unicode (UTF-8)“, damit Umlaute wie ä, ö, ü richtig angezeigt werden
   - **Trennzeichen:** „Semikolon“
4. Klicken Sie auf **Laden**.

*Variante B: Text in Spalten (wenn schon alles in Spalte A steht)*
1. Markieren Sie Spalte A.
2. Klicken Sie auf **Daten** → **Text in Spalten**.
3. Wählen Sie **Getrennt** → **Weiter**.
4. Setzen Sie den Haken bei **Semikolon** und entfernen Sie alle anderen Haken → **Weiter**.
5. Markieren Sie in der Vorschau die Spalten **Telefon** und **Jahresumsatz** und wählen Sie bei **Datenformat der Spalten** jeweils **Text**. So bleiben die Rohwerte erhalten, und Sie wandeln sie später gezielt um.
6. Klicken Sie auf **Fertig stellen**.

Dann machen Sie die Liste zu einer Tabelle: Klicken Sie in die Daten und drücken Sie **Strg + T** → „Tabelle hat Überschriften“ → OK. Damit haben Sie Filter und Formeln, die sich automatisch nach unten fortsetzen.

---

**Schritt 2: Leerzeichen und Groß-/Kleinschreibung**

Für jede Spalte, die Sie bereinigen wollen, legen Sie eine Hilfsspalte an. Ein Beispiel für die Orte, wenn diese in Spalte C stehen:
- `=GLÄTTEN(C2)` entfernt überflüssige Leerzeichen
- `=GROSS2(GLÄTTEN(C2))` schreibt jedes Wort groß. Aus „MUSTERHAUSEN“ und „musterhausen“ wird dann „Musterhausen“.

*Hinweis:* Bei „Neustadt a. d. Probe“ macht GROSS2 daraus „Neustadt A. D. Probe“. Deshalb danach Suchen & Ersetzen verwenden (Schritt 3).

Für die Bewertung in Spalte I: `=GROSS(I2)` macht aus „a“ ein „A“.

Danach übertragen Sie die Ergebnisse als feste Werte: Hilfsspalte kopieren, auf die Originalspalte gehen, **Rechtsklick → Einfügen-Optionen → Werte**. Danach können Sie die Hilfsspalte löschen.

---

**Schritt 3: Schreibweisen vereinheitlichen (Suchen & Ersetzen)**

1. Markieren Sie die betroffene Spalte.
2. Drücken Sie **Strg + H**.
3. Ersetzen Sie zum Beispiel:
   - „Neustadt a.d. Probe“ → „Neustadt a. d. Probe“
   - „Neustadt an der Probe“ → „Neustadt a. d. Probe“
   - „Hr. “ → „Herr “
   - „0000-“ → „0000 “ (Telefonnummern)
4. Klicken Sie auf **Alle ersetzen**.

Bei den Warengruppen legen Sie am besten zuerst fest, welche Begriffe gelten sollen (z. B. nur „Elektrokomponenten“). Ersetzen Sie die anderen Begriffe dann ebenfalls mit Strg + H.

---

**Schritt 4: Umsatz in echte Zahlen umwandeln**

Hilfsspalte, wenn der Umsatz in Spalte H steht:
```
=WERT(WECHSELN(WECHSELN(WECHSELN(H2;"€";"");"EUR";"");" ";""))
```
Die Formel entfernt „€“, „EUR“ und Leerzeichen und macht aus dem Text eine Zahl. Bei deutschen Ländereinstellungen werden „48.500,00“, „12300,00“ und „22750,5“ richtig erkannt.

- Zeigt die Formel **#WERT!**, steht z. B. „n/a“ in der Zelle. Diese Zelle lassen Sie leer oder klären den Wert nach.
- Anschließend die Zellen markieren und über **Start → Zahlenformat** „Buchhaltung“ oder „Zahl mit 2 Dezimalstellen“ wählen.
- Zum Schluss wieder **als Werte einfügen** (siehe Schritt 2).

---

**Schritt 5: Datumsangaben vereinheitlichen**

- **TT.MM.JJJJ und T.M.JJ:** Spalte markieren → **Daten → Text in Spalten** → Getrennt → Weiter → alle Haken entfernen → Weiter → **Datum: TMJ** → Fertig stellen. Excel wandelt die Werte dann in echte Datumswerte um.
- **ISO-Format (2024-02-28):** Excel erkennt das meist automatisch. Falls nicht, hilft diese Formel:
  `=DATUM(LINKS(G2;4);TEIL(G2;6;2);RECHTS(G2;2))`
- **Mit Schrägstrich (15/01/2024):** mit Strg + H „/“ durch „.“ ersetzen, danach wie TT.MM.JJJJ behandeln. **Achtung bei „03/02/2024“:** Klären Sie, ob der 3. Februar gemeint ist.
- **„März 2024“, „Dez. 2023“, „April 2024“:** Hier fehlt der Tag. Tragen Sie die Werte von Hand ein, z. B. als 01.03.2024, und vermerken Sie in einer Spalte „Bemerkung“, dass der Tag geschätzt ist.
- Zum Schluss die Spalte markieren → **Strg + 1** → **Datum** → Format „TT.MM.JJJJ“.

---

**Schritt 6: Dubletten finden und entfernen**

**Wichtig:** Die Funktion „Duplikate entfernen“ findet nur **exakt gleiche** Einträge. „Müller Stahlhandel GmbH“ und „Mueller Stahlhandel“ erkennt sie nicht als gleich. Machen Sie deshalb zuerst die Schritte 2 bis 5 oder prüfen Sie über eine eindeutige Spalte wie die E-Mail.

*a) Dubletten sichtbar machen (empfohlen, bevor Sie etwas löschen)*
1. Markieren Sie die Spalte **E-Mail** (oder Telefon).
2. Klicken Sie auf **Start → Bedingte Formatierung → Regeln zum Hervorheben von Zellen → Doppelte Werte…** → OK.
3. Die doppelten Einträge werden farbig markiert. Mit **Daten → Sortieren** nach E-Mail stehen sie direkt untereinander.
4. Prüfen Sie jedes Paar. Entscheiden Sie, welcher Eintrag vollständiger ist, und übernehmen Sie bei Bedarf Angaben aus dem anderen Eintrag.

*Hinweis:* Leere E-Mail-Zellen (Hoffmann, Krüger) werden nicht als doppelt markiert. Diese beiden prüfen Sie über die Telefonnummer.

*b) Dubletten entfernen*
1. Klicken Sie in die Tabelle.
2. Klicken Sie auf **Daten → Duplikate entfernen** (Gruppe „Datentools“).
3. Entfernen Sie zuerst alle Haken mit **Auswahl aufheben**. Setzen Sie dann nur den Haken bei **E-Mail** (oder bei E-Mail und Telefon).
4. Klicken Sie auf **OK**. Excel meldet, wie viele Zeilen entfernt wurden. Bei dieser Liste sollten es **4** sein.

**Achtung:** Excel behält immer die **erste** Zeile und löscht die späteren. Sortieren Sie deshalb vorher so, dass der bessere Eintrag oben steht. Oder löschen Sie die Zeilen von Hand nach der Prüfung aus Schritt 6a.

---

**Schritt 7: Fehlende Werte prüfen**

1. Aktivieren Sie den Filter mit **Strg + Umschalt + L**, falls er nicht durch die Tabelle schon aktiv ist.
2. Klicken Sie in der Spaltenüberschrift auf den Filterpfeil und wählen Sie nur **(Leere)** aus.
3. So sehen Sie auf einen Blick, wo Ansprechpartner, Telefonnummer, E-Mail, Datum, Umsatz oder Bewertung fehlen. Diese Lücken klären Sie mit dem Einkauf oder dem Lieferanten.

---

**Schritt 8: Speichern**

Speichern Sie die bereinigte Datei als **Excel-Arbeitsmappe (.xlsx)**. In einer CSV gehen Formate und Formeln verloren. Wenn Sie wieder eine CSV brauchen: **Datei → Speichern unter → „CSV UTF-8 (durch Trennzeichen getrennt)“**.

**Tipp:** Wenn Sie solche Listen öfter bekommen, lohnt sich **Power Query** (Daten → Aus Text/CSV → **Daten transformieren** statt Laden). Dort zeichnet Excel die Bereinigungsschritte auf und wendet sie beim nächsten Mal mit einem Klick auf **Aktualisieren** wieder an.
