# Testlauf: Übung 3 / Station D Basis – Lieferantenliste analysieren ohne Änderung

**Herkunft:** Station D, Abschnitt „Basis“ aus [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#station-d-unordentliche-tabelle-bereinigen). Sollergebnis aus [Trainer-Loesungshinweise.md – Station D](../06_Uebungen/Trainer-Loesungshinweise.md#station-d-lieferantenliste-bereinigen). Material: [lieferantenliste_unsortiert.csv](../07_Beispielmaterial/lieferantenliste_unsortiert.csv).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt (Vorlage aus dem Übungsblatt, CSV als Anhang):**

```text
Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.
```

**Was laut Material herauskommen soll:** 27 Datenzeilen, eine vollständige Problemliste und genau die 4 echten Dubletten-Paare mit Begründung, ohne falsche Treffer.

**Nachgeprüft (per `wc -l` und Python-`csv`):**

- Die Datei hat 28 Zeilen (Kopfzeile + **27 Datenzeilen**). Alle Zeilen haben 9 Felder. Die Datei endet mit einem Zeilenumbruch.
- Dubletten (Datenzeile / Dateizeile): Müller Stahlhandel GmbH / Mueller Stahlhandel (1 & 7 / 2 & 8), Schmidt & Söhne KG / Schmidt und Söhne KG (2 & 10 / 3 & 11), Elektro Krause / ELEKTRO KRAUSE GmbH (3 & 14 / 4 & 15), Weber Kunststofftechnik / Weber Kunststoff-Technik GmbH (4 & 18 / 5 & 19).
- Leere Felder (Dateizeile): Lackierwerk Ost Ansprechpartner (6), Hoffmann E-Mail (7), Bauer Bewertung (9), Becker Telefon (13), Keller Datum + Bewertung (17), Schwarz Ansprechpartner (21), Krüger E-Mail (24), Koch Umsatz (27). Dazu „n/a“ im Umsatz bei Richter (18).

**Wichtig für die Auswertung:** Alle drei Modelle geben **Dateizeilen** an (Kopfzeile = Zeile 1, Daten in 2–28). Die Trainer-Lösungshinweise nennen **Datenzeilen** ohne Kopfzeile (z. B. „1 und 7“). Beides ist richtig, nur um eins verschoben. Das sollte man vorher wissen, sonst wirkt eine richtige Antwort falsch.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Zeilenzahl 27 richtig? | ja | ja | ja |
| Alle 4 Dubletten-Paare gefunden? | ja | ja | ja |
| Keine falschen Dubletten? | ja (nennt keine) | ja | ja |
| Ähnliche Nicht-Dubletten ausdrücklich abgegrenzt? | nein | ja (Keller/Krüger, Hoffmann/Braun, Fischer/Koch, Beispielstadt-Ost) | ja (genau die drei Fälle aus den Lösungshinweisen) |
| Begründung der Dubletten (E-Mail, Telefon, Werte) | gut | sehr gut, Tabelle | sehr gut, Tabelle |
| Datumsformate inkl. 03/02/2024 mehrdeutig | ja | ja (auch: 15/01 spricht für TT/MM) | ja |
| „März 2024“ als unvollständig erkannt | ja | ja | ja |
| Weber-Datum (März 2024 vs. 2024-03-01) vorsichtig bewertet | nein, als „=“ gleichgesetzt | ja („passt zu“) | ja („passt zusammen“), aber später „keine abweichenden Informationen“ |
| 12.300 als Tausenderpunkt-Problem benannt | ja | ja | nicht ausdrücklich |
| Fehlende Werte vollständig | ja | ja | ja |
| Bewertung a/b klein, Anrede, Warengruppen, Telefon | ja (Elektronik fehlt bei Warengruppen) | ja | ja |
| Sachliche Fehler | 1 (falsche Spalte bei „n/a“) | keine echten, eine verwirrende Formulierung | keine echten, eine Überverallgemeinerung |
| Hält sich an „OHNE etwas zu ändern“ | ja | ja | ja |

**Ergebnis:** Alle drei Modelle lösen die Basis-Aufgabe im Kern richtig. Sonnet und Opus sind am vollständigsten. Die in den Lösungshinweisen erwarteten Stolpersteine (falsche Zeilenzahl, falsche Dubletten) traten in diesem Lauf **nicht** auf.

---

## Gefundene Fehler mit Beleg

1. **Haiku – falsche Spalte:** „Bei Richter Glas & Optik steht `n/a` in der Spalte „Letzte Bestellung“ (Zeile 18)“. Laut Datei, Zeile 18: `Richter Glas & Optik;…;Optik;09.02.2024;n/a;B`. Das Datum ist vorhanden (09.02.2024), „n/a“ steht in **Jahresumsatz EUR**. Die Überschrift des Punkts („Ungültige Werte im Umsatz“) stimmt, die Spaltenangabe nicht. Ein guter Fall für die Stichprobe.
2. **Haiku – Gleichsetzung ohne Vorbehalt:** „Datum März 2024 = 2024-03-01“. Die Lösungshinweise nennen das ausdrücklich „vereinbar, aber nicht eindeutig“. Aus „März 2024“ lässt sich kein Tag ableiten.
3. **Haiku – erfundene Leerzeile:** „Die letzte Zeile der Datei ist leer und zählt nicht.“ Die Datei endet nur mit einem Zeilenumbruch nach Zeile 28 (`…;8.900;b\n`), eine echte Leerzeile gibt es nicht. Das ist harmlos und deckt sich mit dem, was ein Editor anzeigt (siehe Material-Hinweis unten).
4. **Sonnet – verwirrende Formulierung:** „Wagner Hydraulik, Keller Dichtungstechnik und Krüger Gummiwaren: Gleiche Warengruppe `Dichtungen` (Keller, Krüger)…“. Wagner hat die Warengruppe „Hydraulik“ (Zeile 16) und gehört nicht in diese Gruppe. Kein falscher Dubletten-Treffer, aber unsauber. Ebenso „`Dichtungen` kommt zweimal vor … bei Zeile 17 ist es aber ein eigener Lieferant“: Das ist missverständlich formuliert.
5. **Opus – Überverallgemeinerung:** „Die doppelten Einträge haben bei Umsatz, Datum und Bewertung jeweils dieselben Werte. Beim Zusammenführen gehen also keine abweichenden Informationen verloren.“ Beim Weber-Paar steht „März 2024“ gegen „2024-03-01“. Das ist nur vereinbar, nicht gleich. Außerdem unterscheiden sich Warengruppe, Ortsschreibweise und Ansprechpartner (mit/ohne Vorname). Opus sagt das zwar in der Tabelle, das Fazit ist aber zu glatt.
6. **Opus – Lücke:** Die Mehrdeutigkeit von „12.300“ (Tausenderpunkt oder Dezimalpunkt) wird nicht ausdrücklich als Problem genannt. In der Dubletten-Tabelle ist der Wert aber richtig gedeutet.

Nicht gefunden: erfundene Werte, falsche Zeilenzahl, falsche Dubletten, verschluckte Lieferanten.

---

## Lehren für die Auswertung

- **„Die KI zählt falsch“ ist hier nicht garantiert.** Bei 27 Zeilen kamen alle drei Modelle auf die richtige Zahl. Die Lehre sollte deshalb nicht lauten „die KI liegt immer daneben“, sondern: „Du weißt es erst, wenn du selbst gezählt hast.“ Wenn ein Teilnehmer doch 26 oder 28 bekommt: ideal zum Zeigen.
- **Die Fehler stecken im Kleingedruckten.** Haikus Antwort sieht vollständig und sauber aus, nennt aber bei Richter die falsche Spalte. Das findet nur, wer eine Stichprobe macht. Genau dafür ist der Prüfschritt da.
- **Annahmen klingen wie Fakten.** „März 2024 = 2024-03-01“ (Haiku) oder „keine abweichenden Informationen“ (Opus) sind stille Annahmen. Gut, um die Frage aus den Musterprompts einzusetzen: „Liste alle Stellen auf, an denen du eine Annahme getroffen hast.“
- **Zeilennummern abgleichen.** Die Modelle zählen die Kopfzeile als Zeile 1 mit. Teilnehmende, die mit den Lösungshinweisen vergleichen, sollten das wissen (Müller: Datenzeile 1 = Dateizeile 2).
- **Unterschiede zwischen Modellen zeigen.** Sonnet und Opus grenzen ähnliche Nicht-Dubletten ausdrücklich ab, Haiku nicht. Gute Brücke: „Frag nach, was die KI bewusst *nicht* als Dublette gewertet hat.“
- **Der eigentliche Härtetest kommt im Schritt „Weiter“.** Bei der Analyse arbeiten die Modelle zuverlässig. Zeilen verschwinden, Beträge werden verfälscht oder Daten still ergänzt eher, wenn die bereinigte Tabelle vollständig ausgegeben werden soll.

---

## Probleme im Material

1. **Zeilen zählen mit Strg + Ende ergibt 29, nicht 28.** Die CSV endet mit einem Zeilenumbruch. In gängigen Editoren (Windows-Editor, Notepad++, VS Code) springt Strg + Ende dann in eine leere Zeile 29. Wer der Anleitung im Prüfschritt folgt („Zeilennummer … Kopfzeile nicht mitzählen“), kommt auf 28 statt 27 und hält die richtige KI-Antwort für falsch.
2. **Zeilennummern in den Lösungshinweisen sind Datenzeilen.** Die Tabelle „Zeilen (ohne Kopfzeile) 1 und 7“ passt nicht zu dem, was Modelle und Editoren anzeigen (2 und 8). Das ist korrekt beschriftet, aber leicht zu übersehen.
3. Zeit: Die Basis-Aufgabe ist in wenigen Minuten erledigt. Das Lesen der langen Antworten und die Stichprobe brauchen mehr Zeit als der Prompt. Das passt in die ca. 27 Minuten Arbeitszeit, auch mit „Weiter“.

**Korrekturvorschläge:**

- [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md), Station D, Prüfschritt „Zeilen zählen“: ergänzen um „Steht der Cursor danach in einer leeren Zeile, zählt diese nicht mit. Also: letzte Zeile mit Text minus 1 (Kopfzeile).“
- [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md), Station D, Dubletten-Tabelle: Spalte „Zeilen (ohne Kopfzeile)“ ergänzen um die Dateizeilen, z. B. „1 und 7 (in der Datei: Zeile 2 und 8)“. Dazu einen Satz: „KI-Assistenten und Editoren zählen meist die Kopfzeile als Zeile 1 mit.“
- Trainer-Loesungshinweise, „Typische Stolpersteine (Station D)“: ergänzen um „Falsche Spaltenzuordnung (z. B. ‚n/a‘ bei Richter einer falschen Spalte zugeordnet)“ und um den Hinweis, dass die Zeilenzahl im Test meist stimmt.

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

Ich habe die Datei nur gelesen und nichts verändert.

**1. Anzahl der Zeilen**
Die Liste hat **27 Datenzeilen** (Zeilen 2 bis 28), ohne Kopfzeile. Die letzte Zeile der Datei ist leer und zählt nicht.

**2. Probleme**

- **Datumsformate uneinheitlich:** `12.03.2024`, `2024-02-28`, `5.1.24` (zweistellige Jahreszahl), `März 2024`, `Dez. 2023`, `April 2024`, `15/01/2024`, `03/02/2024`, `7.4.2024`. Besonders `03/02/2024` ist mehrdeutig (3. Februar oder 2. März?). Bei Monatsangaben ohne Tag fehlt das genaue Datum.
- **Zahlenformate uneinheitlich:** `48.500,00`, `12.300`, `31 200 €`, `9800`, `22750,5`, `48500`, `63.200 €`, `1.200`. Tausendertrennzeichen, Dezimalkomma und Währungssymbole sind gemischt. Teils steht „EUR“ oder „€“ im Feld, teils nicht. Der Punkt bei `12.300` kann als Dezimaltrennzeichen oder als Tausenderpunkt gelesen werden.
- **Ungültige Werte im Umsatz:** Bei Richter Glas & Optik steht `n/a` in der Spalte „Letzte Bestellung“ (Zeile 18), bei Koch Elektronik fehlt der Jahresumsatz (Zeile 27).
- **Ortsnamen uneinheitlich geschrieben:** `Musterhausen`, `musterhausen`, `MUSTERHAUSEN`. `Neustadt a. d. Probe`, `Neustadt a.d. Probe`, `neustadt a. d. probe`, `Neustadt an der Probe`. `Fiktivhausen` und `fiktivhausen`.
- **Warengruppen uneinheitlich:** `Schrauben/Normteile` und `Normteile`, `Elektrokomponenten` und `Elektro`, `Kunststoffteile` und `Kunststoff`.
- **Telefonnummern uneinheitlich:** `0000 111201` gegenüber `0000-111201`. Bei Becker Werkzeugbau fehlt die Telefonnummer.
- **Fehlende Werte:**
  - Ansprechpartner fehlt bei Lackierwerk Ost GmbH (Zeile 6) und Schwarz Gießerei (Zeile 21).
  - E-Mail fehlt bei Hoffmann Logistik (Zeile 7) und Krüger Gummiwaren (Zeile 24).
  - Telefon fehlt bei Becker Werkzeugbau (Zeile 13).
  - Letzte Bestellung fehlt bei Keller Dichtungstechnik (Zeile 17).
  - Jahresumsatz fehlt bei Koch Elektronik (Zeile 27).
  - Bewertung fehlt bei Bauer Präzisionsteile (Zeile 9) und Keller Dichtungstechnik (Zeile 17).
- **Bewertung uneinheitlich:** Die Werte `a` (Zeile 25) und `b` (Zeile 28) sind klein geschrieben. Die übrigen sind groß (A, B, C).
- **Anrede uneinheitlich:** `Hr. Krause`, `Herr Krause`, `Frau Dr. Weber`, `Dr. Weber`, `Herr Dr. Wolf`.
- **Firmennamen mit Abweichungen:** `Mueller` statt `Müller`, `Schmidt und Söhne KG` statt `Schmidt & Söhne KG`, `ELEKTRO KRAUSE GmbH` in Großbuchstaben.

**3. Mögliche Dubletten**

Vier Paare sind sehr wahrscheinlich dieselbe Firma:

- **Müller Stahlhandel GmbH (Zeile 2) und Mueller Stahlhandel (Zeile 8):** gleiche E-Mail (brandt@stahl-mueller.example.com), gleiche Telefonnummer (nur anders formatiert), gleicher Ansprechpartner (Brandt), gleicher Ort, gleiches Datum (12.03.2024 = 2024-03-12) und gleicher Umsatz (48.500,00 = 48500).
- **Schmidt & Söhne KG (Zeile 3) und Schmidt und Söhne KG (Zeile 11):** gleiche E-Mail (l.schmidt@schmidt-soehne.example.com), gleiche Telefonnummer, gleiche Person (Lea Schmidt), gleicher Ort, gleiches Datum (28.02.2024), gleicher Umsatz (12.300 = 12300,00).
- **Elektro Krause (Zeile 4) und ELEKTRO KRAUSE GmbH (Zeile 15):** gleiche E-Mail (info@elektro-krause.example.com), gleiche Telefonnummer, gleicher Ort, Datum 5.1.24 = 05.01.2024 und gleicher Umsatz (31 200 € = 31.200,00).
- **Weber Kunststofftechnik (Zeile 5) und Weber Kunststoff-Technik GmbH (Zeile 19):** gleiche E-Mail (weber@weber-kunststoff.example.com), gleiche Telefonnummer, gleiche Person (Dr. Weber), gleicher Ort, Datum März 2024 = 2024-03-01 und gleicher Umsatz (22.750,50 = 22750,5).

Bei diesen Paaren stimmen E-Mail und Telefonnummer überein, das sind die stärksten Hinweise. Die Abweichungen liegen nur in Schreibweise und Format. Ich würde jedes Paar vor dem Zusammenführen kurz prüfen. Zusammen mit den Dubletten ergeben sich etwa **23 eindeutige Lieferanten**.

Sag mir, wenn ich als Nächstes einen Vorschlag für die Bereinigung machen soll, zum Beispiel einheitliche Datumsformate, Zahlen und Ortsnamen.

---

### Sonnet

#### Nutzer 1

Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.

#### Assistent 1

Ich habe nichts verändert, nur gelesen und analysiert.

**1. Anzahl der Zeilen**
Die Liste hat **27 Datenzeilen** ohne Kopfzeile. Es gibt 9 Spalten: Lieferant, Ansprechpartner, Ort, Telefon, E-Mail, Warengruppe, Letzte Bestellung, Jahresumsatz EUR, Bewertung.

**2. Probleme**

*a) Datumsformate (Spalte „Letzte Bestellung“)*
- Es sind mindestens fünf Schreibweisen gemischt:
  - `12.03.2024` (TT.MM.JJJJ)
  - `2024-02-28` (ISO)
  - `5.1.24` und `7.4.2024` (ohne führende Nullen, teils zweistelliges Jahr)
  - `15/01/2024` und `03/02/2024` (mit Schrägstrich)
  - `März 2024`, `Dez. 2023`, `April 2024` (nur Monat, kein Tag)
- Bei `03/02/2024` ist unklar, ob der 3. Februar oder der 2. März gemeint ist. `15/01/2024` spricht für TT/MM/JJJJ, sicher ist das aber nicht.
- Bei den Monatsangaben fehlt der Tag. Sie lassen sich nicht exakt in ein Datum umwandeln.
- Bei Keller Dichtungstechnik (Zeile 17) fehlt das Datum ganz.

*b) Umsatzformate (Spalte „Jahresumsatz EUR“)*
- Die Formate sind uneinheitlich:
  - `48.500,00`
  - `12.300` (Punkt als Tausendertrenner, ohne Dezimalstellen)
  - `31 200 €` (Leerzeichen und Währungszeichen)
  - `22.750,50`
  - `9800` (ohne Trenner)
  - `18.400,00 €`
  - `41.000 EUR`
  - `12300,00`
  - `22750,5`
- Die Währung steht teils im Wert, obwohl sie schon im Spaltennamen steht („€“, „EUR“).
- Bei `12.300` kann man nicht sicher sagen, ob 12.300 oder 12,3 gemeint ist. Aus dem Kontext sind 12.300 am wahrscheinlichsten.
- Fehlende oder ungültige Werte: Richter Glas & Optik hat `n/a` (Zeile 18), Koch Elektronik hat einen leeren Wert (Zeile 27).
- Beim Sortieren oder Summieren funktioniert die Spalte so nicht, weil alles Text ist.

*c) Schreibweisen bei Orten*
- Groß- und Kleinschreibung ist uneinheitlich: `musterhausen`, `MUSTERHAUSEN`, `Musterhausen`, `fiktivhausen` und `Fiktivhausen`.
- Auch `neustadt a. d. probe` gehört dazu.
- Für Neustadt gibt es mehrere Varianten: `Neustadt a. d. Probe`, `Neustadt a.d. Probe` und `Neustadt an der Probe`.
- `Beispielstadt` und `Beispielstadt-Ost` sind vermutlich zwei verschiedene Orte oder Ortsteile. Das sollte man bewusst entscheiden.

*d) Schreibweisen bei Firmennamen und Ansprechpartnern*
- Firmennamen: `Müller` und `Mueller`, `Schmidt & Söhne KG` und `Schmidt und Söhne KG`, `Weber Kunststofftechnik` und `Weber Kunststoff-Technik GmbH`, `Elektro Krause` und `ELEKTRO KRAUSE GmbH`. Die Rechtsform fehlt teils (GmbH ja oder nein).
- Ansprechpartner haben unterschiedliche Anreden und Namensformen: `Herr K. Brandt` und `K. Brandt`, `Frau Lea Schmidt` und `Lea Schmidt`, `Herr Krause` und `Hr. Krause`, `Frau Dr. Weber` und `Dr. Weber`.
- Manche haben Vornamen, manche nur Initialen oder gar keinen Vornamen.

*e) Schreibweisen bei Telefon, Warengruppe und Bewertung*
- Telefonnummern: `0000 111201` und `0000-111201` (Leerzeichen oder Bindestrich).
- Warengruppen sind nicht einheitlich:
  - `Schrauben/Normteile` und `Normteile`
  - `Elektrokomponenten` und `Elektro`
  - `Kunststoffteile` und `Kunststoff`
  - `Dichtungen` kommt zweimal vor (Zeile 17 und 24), bei Zeile 17 ist es aber ein eigener Lieferant und keine Dublette.
  - `Elektronik` steht neben `Elektrokomponenten`.
- Bewertung: `a` und `b` stehen klein, sonst gilt A, B oder C.

*f) Fehlende Werte*
- Ansprechpartner fehlt: Lackierwerk Ost, Schwarz Gießerei.
- E-Mail fehlt: Hoffmann Logistik, Krüger Gummiwaren.
- Telefon fehlt: Becker Werkzeugbau.
- Bewertung fehlt: Bauer Präzisionsteile, Keller Dichtungstechnik.
- Letzte Bestellung fehlt: Keller Dichtungstechnik.
- Jahresumsatz fehlt oder ist `n/a`: Richter Glas & Optik, Koch Elektronik.

*g) Weitere Auffälligkeiten*
- Die Liste ist nicht sortiert. Das ist laut Dateiname gewollt, erschwert aber die Dublettenprüfung.
- Wolf Messtechnik hat als Datum nur `April 2024` und als Bewertung `a` (klein).
- Manche Daten liegen weit zurück (z. B. 30.10.2023, 14.11.2023). Bei einer Bereinigung kann das für die Prüfung relevant sein, ob der Lieferant noch aktiv ist.

**3. Mögliche Dubletten**

| Gruppe | Zeilen | Begründung |
|---|---|---|
| Müller Stahlhandel | Zeile 2 `Müller Stahlhandel GmbH` und Zeile 8 `Mueller Stahlhandel` | Gleiche E-Mail (brandt@stahl-mueller...), gleiche Telefonnummer (nur anders geschrieben), gleicher Ort, gleiche Warengruppe, gleiches Datum (12.03.2024 = 2024-03-12), gleicher Umsatz (48.500) und gleiche Bewertung A. Fast sicher dieselbe Firma. |
| Schmidt & Söhne | Zeile 3 `Schmidt & Söhne KG` und Zeile 11 `Schmidt und Söhne KG` | Gleiche E-Mail, gleiche Telefonnummer, gleiche Ansprechpartnerin. Datum identisch (28.02.2024), Umsatz identisch (12.300), Bewertung B. Nur Schreibweise von „&“ und „und“ sowie Ort und Warengruppe unterscheiden sich. Sehr sicher. |
| Elektro Krause | Zeile 4 `Elektro Krause` und Zeile 15 `ELEKTRO KRAUSE GmbH` | Gleiche E-Mail, gleiche Telefonnummer, gleicher Ansprechpartner, gleiches Datum (5.1.24 = 05.01.2024), gleicher Umsatz (31.200), Bewertung A. Sehr sicher. |
| Weber Kunststoff | Zeile 5 `Weber Kunststofftechnik` und Zeile 19 `Weber Kunststoff-Technik GmbH` | Gleiche E-Mail, gleiche Telefonnummer, gleiche Ansprechpartnerin, gleicher Ort, gleicher Umsatz (22.750,50), Bewertung B. Datum „März 2024“ passt zu 2024-03-01. Sehr sicher. |

**Keine Dubletten, aber ähnlich**
- Fischer Kabelkonfektion und Koch Elektronik haben ähnliche Warengruppen, sind aber verschiedene Firmen (andere E-Mail und Telefonnummer).
- Wagner Hydraulik, Keller Dichtungstechnik und Krüger Gummiwaren: Gleiche Warengruppe `Dichtungen` (Keller, Krüger) heißt nicht Dublette. Andere Firma, anderer Ort.
- Hoffmann Logistik und Braun Transporte (beide Spedition): Verschiedene Firmen.
- `Beispielstadt` und `Beispielstadt-Ost`: Lackierwerk Ost ist ein eigener Lieferant.

**Fazit:** Es gibt 4 Dublettenpaare, also 8 Zeilen, von denen 4 überflüssig sind. Nach dem Zusammenführen blieben **23 eindeutige Lieferanten**. Bei den Dubletten sollte man vor dem Löschen prüfen, welche Zeile die vollständigere oder aktuellere ist. Dazu gehören zum Beispiel die Rechtsform (GmbH), die Warengruppe und die Ortsschreibweise.

Ich habe nichts verändert. Wenn du möchtest, kann ich als Nächstes die Daten bereinigen und vereinheitlichen.

---

### Opus

#### Nutzer 1

Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.

#### Assistent 1

Ich habe mir die Liste nur angesehen und nichts verändert.

**1. Anzahl der Zeilen**

Ohne die Kopfzeile hat die Liste **27 Datenzeilen**. Es gibt 9 Spalten: Lieferant, Ansprechpartner, Ort, Telefon, E-Mail, Warengruppe, Letzte Bestellung, Jahresumsatz EUR, Bewertung.

Unten nenne ich für jeden Eintrag die Zeile in der Datei. Zeile 1 ist die Kopfzeile, die Daten stehen in den Zeilen 2 bis 28.

---

**2. Gefundene Probleme**

**a) Uneinheitliche Datumsformate (Spalte „Letzte Bestellung“)**
In der Spalte stehen mindestens sieben verschiedene Schreibweisen:
- TT.MM.JJJJ, z. B. `12.03.2024`, `14.11.2023`
- ISO-Format JJJJ-MM-TT, z. B. `2024-02-28`, `2024-04-08`, `2024-01-30`
- Kurzform ohne führende Null oder mit zweistelligem Jahr: `5.1.24` (Elektro Krause), `7.4.2024` (Lange Büroservice)
- Mit Schrägstrich: `15/01/2024` (Zimmermann), `03/02/2024` (Braun Transporte)
- Nur Monat und Jahr: `März 2024` (Weber), `Dez. 2023` (Becker), `April 2024` (Wolf)
- Ganz leer: Keller Dichtungstechnik

Bei `03/02/2024` ist nicht klar, was gemeint ist. Es kann der 3. Februar (deutsche Schreibweise) oder der 2. März (US-Schreibweise) sein. Das sollte jemand nachprüfen.

**b) Uneinheitliche Ortsangaben (Spalte „Ort“)**
- Groß- und Kleinschreibung: `Musterhausen`, `musterhausen`, `MUSTERHAUSEN`; `Fiktivhausen` und `fiktivhausen`
- Neustadt steht in vier Varianten da: `Neustadt a. d. Probe`, `Neustadt a.d. Probe`, `Neustadt an der Probe`, `neustadt a. d. probe`
- `Beispielstadt-Ost` (Lackierwerk Ost) kann ein eigener Ort sein oder nur ein Ortsteil von Beispielstadt. Das sollte man klären.

**c) Uneinheitliche Beträge (Spalte „Jahresumsatz EUR“)**
- Verschiedene Zahlenformate: `48.500,00`, `48500`, `12300,00`, `22750,5`, `9800`, `31 200 €` (Leerzeichen als Tausendertrenner)
- In manchen Zellen steht die Währung, obwohl sie schon im Spaltennamen steht: `€`, `EUR`
- Text statt Zahl: `n/a` (Richter Glas & Optik)
- Leer: Koch Elektronik

So wie die Spalte jetzt ist, kann Excel nicht zuverlässig mit ihr rechnen, also z. B. keine Summen oder Sortierungen nach Umsatz.

**d) Fehlende Werte**
- Ansprechpartner fehlt: Lackierwerk Ost GmbH, Schwarz Gießerei
- Telefon fehlt: Becker Werkzeugbau
- E-Mail fehlt: Hoffmann Logistik, Krüger Gummiwaren
- Letzte Bestellung fehlt: Keller Dichtungstechnik
- Jahresumsatz fehlt oder ist „n/a“: Koch Elektronik, Richter Glas & Optik
- Bewertung fehlt: Bauer Präzisionsteile, Keller Dichtungstechnik

**e) Uneinheitliche Bewertung**
Die Bewertungen sollten wohl in Großbuchstaben stehen (A/B/C). Zwei Einträge sind kleingeschrieben: `a` (Wolf Messtechnik) und `b` (Schäfer Schweißtechnik).

**f) Uneinheitliche Ansprechpartner**
Die Anrede ist mal ausgeschrieben, mal abgekürzt und mal gar nicht da: `Herr K. Brandt` und `K. Brandt`, `Herr Krause` und `Hr. Krause`, `Frau Dr. Weber` und `Dr. Weber`, `Frau Lea Schmidt` und `Lea Schmidt`. Außerdem steht der Vorname mal dabei und mal nicht.

**g) Uneinheitliche Telefonnummern**
Fast überall trennt ein Leerzeichen Vorwahl und Nummer (`0000 111201`). Einmal ist es ein Bindestrich (`0000-111201`).

**h) Uneinheitliche Warengruppen**
Gleiche Dinge haben verschiedene Namen:
- `Schrauben/Normteile` und `Normteile`
- `Elektrokomponenten` und `Elektro` (und vielleicht auch `Elektronik`)
- `Kunststoffteile` und `Kunststoff`

Wer nach Warengruppe filtert oder auswertet, bekommt deshalb falsche Ergebnisse.

**i) Uneinheitliche Firmennamen**
- Umlaute mal als Buchstabe, mal umschrieben: `Müller` und `Mueller`
- `&` und `und`
- Großschreibung: `ELEKTRO KRAUSE`
- Rechtsform mal angegeben, mal nicht (`GmbH`, `KG`)

**j) Dubletten**
Einige Lieferanten stehen doppelt in der Liste, siehe Punkt 3.

---

**3. Mögliche Dubletten**

| Nr. | Eintrag A (Zeile) | Eintrag B (Zeile) | Begründung |
|---|---|---|---|
| 1 | Müller Stahlhandel GmbH (Z. 2) | Mueller Stahlhandel (Z. 8) | Gleicher Name, nur „ü“ als „ue“ geschrieben und ohne GmbH. Gleicher Ansprechpartner (K. Brandt), gleicher Ort, gleiche Telefonnummer (nur Bindestrich statt Leerzeichen), **identische E-Mail**, gleiche Warengruppe, gleiches Datum (12.03.2024 = 2024-03-12), gleicher Umsatz (48.500) und gleiche Bewertung A. **Sehr sicher eine Dublette.** |
| 2 | Schmidt & Söhne KG (Z. 3) | Schmidt und Söhne KG (Z. 11) | „&“ statt „und“. Gleiche Ansprechpartnerin (Lea Schmidt), gleicher Ort (nur anders geschrieben), **gleiche Telefonnummer und E-Mail**, gleiches Datum (2024-02-28 = 28.02.2024), gleicher Umsatz (12.300), Bewertung B. Die Warengruppe ist nur anders benannt (Schrauben/Normteile bzw. Normteile). **Sehr sicher eine Dublette.** |
| 3 | Elektro Krause (Z. 4) | ELEKTRO KRAUSE GmbH (Z. 15) | Gleicher Name, nur anders groß geschrieben und mit GmbH. Herr bzw. Hr. Krause, Neustadt (zwei Schreibweisen), **gleiche Telefonnummer und E-Mail**, gleiches Datum (5.1.24 = 05.01.2024), gleicher Umsatz (31.200), Bewertung A. Die Warengruppe heißt einmal „Elektrokomponenten“, einmal „Elektro“. **Sehr sicher eine Dublette.** |
| 4 | Weber Kunststofftechnik (Z. 5) | Weber Kunststoff-Technik GmbH (Z. 19) | Gleicher Name, nur mit Bindestrich und GmbH. Dr. Weber, Fiktivhausen, **gleiche Telefonnummer und E-Mail**, gleicher Umsatz (22.750,50), Bewertung B. Das Datum passt zusammen: „März 2024“ und 2024-03-01. Die Warengruppe heißt „Kunststoffteile“ bzw. „Kunststoff“. **Sehr sicher eine Dublette.** |

**Ähnlich, aber nach meiner Einschätzung keine Dubletten:**
- Keller Dichtungstechnik und Krüger Gummiwaren haben beide die Warengruppe „Dichtungen“. Namen, Orte und Telefonnummern sind aber verschieden.
- Hoffmann Logistik und Braun Transporte sind beide unter „Spedition“ eingetragen. Auch hier gibt es sonst keine Übereinstimmungen.
- Elektro Krause, Fischer Kabelkonfektion und Koch Elektronik haben ähnliche Warengruppen und alle drei den Ort Neustadt. Es sind aber verschiedene Firmen mit eigenen Kontaktdaten.

**Zusammenfassung:** Es gibt 4 Dublettenpaare. Ohne sie bleiben **23 verschiedene Lieferanten** übrig. Die doppelten Einträge haben bei Umsatz, Datum und Bewertung jeweils dieselben Werte. Beim Zusammenführen gehen also keine abweichenden Informationen verloren. Man muss nur entscheiden, welche Schreibweise man behält.

Wenn Sie möchten, kann ich die Liste im nächsten Schritt bereinigen: einheitliches Datumsformat, einheitliche Orte und Beträge, Dubletten zusammengeführt. Die offenen Fragen (z. B. `03/02/2024`, die fehlenden Werte) markiere ich dabei, damit Sie sie selbst prüfen können.
