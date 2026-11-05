# Testlauf: Übung 3 / Station D Trainer-Kontrollwert – Summe der Jahresumsätze

**Herkunft:** [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md), Übung 3, Station D, Absatz „Kontrollwert für Schnelle (falls jemand die Summe der Jahresumsätze bildet)“. Übungsblatt: [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md), Station D. Material: [lieferantenliste_unsortiert.csv](../07_Beispielmaterial/lieferantenliste_unsortiert.csv).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf:** Im selben Gespräch kam zuerst der Basis-Prompt von Station D (Analyse ohne Änderung), danach ein Summen-Prompt. Das Übungsblatt enthält **keinen** eigenen Summen-Prompt, er wurde aus dem Trainer-Hinweis abgeleitet:

```text
Bilde die Summe der Jahresumsätze nach Entfernen der Dubletten. Lieferanten ohne Umsatzangabe lässt du weg und nennst sie.
```

Der Weiter-Prompt (Bereinigung) wurde **nicht** vorgeschaltet. Gerechnet wurde also auf der Originaldatei.

**Was herauskommen soll (Prüfmaßstab, laut Lösungshinweisen):**

- Summe **461.001,25 €** aus **21** Beträgen (23 Lieferanten nach Dublettenentfernung, ohne Richter „n/a“ und Koch leer).
- Mit Dubletten käme man fälschlich auf **575.751,75 €** (Differenz 114.750,50 € = 48.500 + 12.300 + 31.200 + 22.750,50).
- Weggelassen und genannt: Richter Glas & Optik (`n/a`), Koch Elektronik (leer).

**Eigene Nachrechnung (python3, Decimal, Punkt als Tausendertrenner, Komma als Dezimaltrenner):** 27 Datenzeilen, Dubletten = Datenzeilen 7, 10, 14, 18. Summe ohne Dubletten **461.001,25 €** (21 Beträge), mit Dubletten **575.751,75 €**. Beide Kontrollwerte der Lösungshinweise stimmen. Zum Vergleich typischer Fehler: Wird „12.300“ als 12,30 € gelesen, ergibt sich 448.713,55 €.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Zeilenzahl 27 / 23 Lieferanten | ja | ja | ja |
| 4 richtige Dubletten-Paare, keine falschen | ja | ja | ja |
| Summe 461.001,25 € | **ja** | **ja** | **ja** |
| 21 Beträge, Richter und Koch genannt | ja | ja | ja |
| Einzelwerte offengelegt (nachprüfbar) | **nein** – nur Endsumme | ja, Tabelle mit 21 Werten | ja, Tabelle mit 21 Werten |
| Alle 21 Einzelwerte korrekt aus CSV übernommen | nicht prüfbar | ja | ja |
| Annahme zu „12.300“ / Tausenderpunkt genannt | ja | ja | ja |
| Vergleichswert mit Dubletten (575.751,75 €) | nein | ja (richtig) | ja (richtig, mit Differenz) |
| Empfehlung, in Excel nachzurechnen | nein | nein (nur Vorbehalt Dubletten) | **ja**, ausdrücklich |
| Kleinere sachliche Ungenauigkeiten in Antwort 1 | 2 | 1 | 1 |

**Gesamturteil:** Alle drei Modelle liefern die richtige Summe. Der im Trainer-Hinweis erhoffte „wunderbare Moment“ (KI-Summe weicht ab) trat in diesem Test **nicht** auf. Didaktisch trägt der Kontrollwert trotzdem – aber mit anderer Lehre (siehe unten).

---

## Gefundene Fehler mit Beleg

Alle Fehler betreffen die Analyse (Antwort 1), nicht die Summe.

**Haiku**
- „Andere Paare ähneln sich nur im Namen (z. B. Elektro Krause und Fischer Kabelkonfektion)“ – die Namen ähneln sich nicht. Gemeinsam sind laut CSV Ort (Neustadt a. d. Probe / a.d. Probe) und Warengruppe „Elektrokomponenten“. Die Lösungshinweise nennen genau diese Ähnlichkeit („gleiche Gegend, ähnliche Warengruppe“).
- Warengruppen-Beispiel „`Dichtungen` / `Kunststoff`“ ist keine Schreibvariante derselben Gruppe (Keller/Krüger = „Dichtungen“, Weber = „Kunststoffteile“/„Kunststoff“). Die richtige Variante wäre „Kunststoffteile / Kunststoff“.
- Zeilennummern zählen die Dateizeilen (Müller = Zeile 2), die Lösungshinweise zählen Datenzeilen ohne Kopfzeile (Müller = 1). Das ist kein Fehler, Haiku sagt es aber nur indirekt („Zeilen 2 bis 28 der Datei“). Beim Abgleich mit der Tabelle in den Lösungshinweisen verschiebt sich alles um 1.
- Summe ohne Einzelwerte: richtig, aber für Teilnehmende nicht nachprüfbar.

**Sonnet**
- Weber-Paar: „gleiches Datum März 2024 (01.03.2024)“ – die CSV hat „März 2024“ und „2024-03-01“. Das ist laut Lösungshinweisen „vereinbar, aber nicht eindeutig“. Sonnet setzt den Tag still als gleich an (stille Annahme, Stolperstein laut Lösungshinweisen).
- Bei den Ort-Varianten steht auch „Beispielstadt“. In der CSV gibt es „Beispielstadt“ und „Beispielstadt-Ost“ – das sind verschiedene Orte, keine Schreibvarianten. Kleinigkeit.

**Opus**
- „Kurzform mit zweistelligem Jahr: `5.1.24`, `7.4.2024`“ – `7.4.2024` (Lange Büroservice) hat ein vierstelliges Jahr, es fehlen nur die führenden Nullen.

**Summenteil:** Bei Sonnet und Opus stimmt jeder der 21 Einzelwerte mit der CSV überein (abgeglichen mit python3). Nichts erfunden, kein Wert vertauscht, „12.300“, „1.200“ und „7.400“ richtig als Tausender gelesen, „22750,5“ richtig als 22.750,50.

---

## Lehren für die Auswertung

1. **Die Summe stimmt – das ist nicht die Lehre, auf die man sich verlassen kann.** Bei 21 Beträgen schaffen aktuelle Modelle das oft fehlerfrei. Der Trainer-Hinweis „Weicht die KI-Summe ab …“ greift dann nicht. Bessere Lehre: *Woher weißt du, dass sie stimmt?* Nur wer nachrechnet (Excel `=SUMME`) weiß es.
2. **Nachprüfbarkeit vergleichen:** Haiku nennt nur „461.001,25 EUR“. Sonnet und Opus legen alle 21 Einzelwerte offen. Gute Frage an die Gruppe: „Welche Antwort könnt ihr in zwei Minuten prüfen?“ Daraus folgt die Prompt-Regel: **„Liste jeden Einzelwert auf, bevor du summierst.“**
3. **Opus empfiehlt von sich aus Excel** („Bitte prüfen Sie die Summe in Excel nach …“). Das ist das gewünschte Verhalten und ein gutes Vorzeigebeispiel. Haiku tut das nicht.
4. **Kontrollwerte nutzen:** 461.001,25 € (richtig), 575.751,75 € (Dubletten mitgezählt), 448.713,55 € („12.300“ als 12,30 gelesen). Teilnehmende mit einer dieser Zahlen wissen sofort, welcher Fehler passiert ist.
5. **Stille Annahmen tauchen trotzdem auf**, nur nicht in der Summe: Sonnet macht aus „März 2024“ den 01.03.2024. Hinweis an die Gruppe: Auch wenn die Endzahl stimmt, enthält die Antwort Deutungen, die man prüfen muss.
6. **Zeilennummern:** Ein Modell zählt Dateizeilen, die anderen Datenzeilen. Beim Abgleich mit den Lösungshinweisen kurz klären, sonst entsteht Verwirrung („Zeile 8 ist bei mir nicht Mueller“).

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

**1. Anzahl Zeilen**
Die Liste hat **27 Datensätze** (Zeilen 2 bis 28 der Datei, ohne Kopfzeile).

**2. Probleme**

*Datumsformate (uneinheitlich):*
- `12.03.2024` (TT.MM.JJJJ)
- `2024-02-28` (ISO-Format)
- `5.1.24` (zweistellige Jahreszahl, ohne führende Nullen)
- `15/01/2024` und `03/02/2024` (Schrägstriche; `03/02/2024` ist mehrdeutig: 3. Februar oder 2. März)
- `März 2024`, `Dez. 2023`, `April 2024` (ausgeschriebene Monate, ohne Tag)
- `7.4.2024` (ohne führende Nullen)
- Leer bei Keller Dichtungstechnik (Zeile 17)

*Zahlenformate und Beträge:*
- Tausendertrennzeichen uneinheitlich: `48.500,00`, `12300,00`, `22750,5`, `48500`, `9800`
- `12.300` und `1.200` und `7.400` sind im deutschen Format als Tausender zu lesen, können aber auch als Dezimalzahl missverstanden werden.
- Währungsangaben uneinheitlich: `€`, `EUR`, ohne Währung, oder `31 200 €` mit Leerzeichen als Trenner
- Umsatz fehlt oder ist nicht verwertbar: `n/a` (Richter Glas & Optik, Zeile 18) und leer (Koch Elektronik, Zeile 27)

*Schreibweisen:*
- Firmennamen: `Müller` / `Mueller`, `Schmidt & Söhne KG` / `Schmidt und Söhne KG`, `Weber Kunststofftechnik` / `Weber Kunststoff-Technik GmbH`, `Elektro Krause` / `ELEKTRO KRAUSE GmbH`
- Orte: `MUSTERHAUSEN`, `musterhausen`, `Musterhausen`; `fiktivhausen`; `Neustadt a. d. Probe`, `Neustadt a.d. Probe`, `Neustadt an der Probe`, `neustadt a. d. probe`
- Telefonnummern: `0000 111201` und `0000-111201` (gleiche Nummer, andere Schreibweise)
- Anrede: `Herr`, `Frau`, `Hr.`, `Dr.` uneinheitlich, teils mit Vorname, teils nur Nachname
- Warengruppen: `Schrauben/Normteile` / `Normteile`, `Elektrokomponenten` / `Elektro` / `Elektronik`, `Dichtungen` / `Kunststoff`
- Bewertung: Großbuchstaben `A`, `B`, `C` und Kleinbuchstaben `a`, `b` gemischt

*Fehlende Werte:*
- Ansprechpartner: Lackierwerk Ost GmbH (Zeile 6), Schwarz Gießerei (Zeile 21)
- E-Mail: Hoffmann Logistik (Zeile 7), Krüger Gummiwaren (Zeile 24)
- Telefon: Becker Werkzeugbau (Zeile 13)
- Bewertung: Bauer Präzisionsteile (Zeile 9), Keller Dichtungstechnik (Zeile 17)
- Letzte Bestellung: Keller Dichtungstechnik (Zeile 17)
- Jahresumsatz: Richter (Zeile 18), Koch (Zeile 27)

**3. Mögliche Dubletten**

Die Begründung stützt sich auf übereinstimmende E-Mail-Adresse und Telefonnummer, dazu passende Stadt, Warengruppe und Umsatz.

| Zeilen | Namen | Begründung |
|---|---|---|
| 2 und 8 | Müller Stahlhandel GmbH / Mueller Stahlhandel | Gleiche E-Mail, gleiche Telefonnummer (nur anders geschrieben), gleicher Ansprechpartner (K. Brandt), gleicher Ort, Umsatz 48.500 |
| 3 und 11 | Schmidt & Söhne KG / Schmidt und Söhne KG | Gleiche E-Mail und Telefonnummer, gleicher Ansprechpartner (Lea Schmidt), gleiche Bestelldaten (28.02.2024), Umsatz 12.300 |
| 4 und 15 | Elektro Krause / ELEKTRO KRAUSE GmbH | Gleiche E-Mail und Telefonnummer, gleicher Ort (Neustadt), Umsatz 31.200, Bewertung A |
| 5 und 19 | Weber Kunststofftechnik / Weber Kunststoff-Technik GmbH | Gleiche E-Mail und Telefonnummer, gleicher Ansprechpartner (Dr. Weber), gleicher Ort (Fiktivhausen), Umsatz 22.750,50 |

Ich würde jeweils einen Eintrag behalten und die Schreibweise vereinheitlichen. Ob es sich wirklich um dieselbe Firma handelt, sollte vor dem Löschen kurz geprüft werden. Andere Paare ähneln sich nur im Namen (z. B. Elektro Krause und Fischer Kabelkonfektion), haben aber unterschiedliche Kontaktdaten und sind daher keine Dubletten.

Nach Entfernen der Dubletten bleiben **23 eindeutige Lieferanten**.

#### Nutzer 2

Bilde die Summe der Jahresumsätze nach Entfernen der Dubletten. Lieferanten ohne Umsatzangabe lässt du weg und nennst sie.

#### Assistent 2

**Ergebnis: 461.001,25 EUR**

Grundlage sind 21 Lieferanten mit Umsatzangabe. Bei den vier Dubletten habe ich jeweils den ersten Eintrag behalten: Zeile 2 (Müller), Zeile 3 (Schmidt & Söhne), Zeile 4 (Elektro Krause) und Zeile 5 (Weber Kunststofftechnik). Die Einträge in Zeile 8, 11, 15 und 19 sind dann nicht mehr enthalten.

**Ohne Umsatzangabe (weggelassen):**
- Richter Glas & Optik (Zeile 18): Umsatz "n/a"
- Koch Elektronik (Zeile 27): Umsatz leer

**Annahme:** Zahlen wie `12.300`, `1.200` und `7.400` habe ich als Tausenderangaben im deutschen Format gelesen (also 12.300 EUR usw.). Wenn sie anders gemeint sind, ändert sich die Summe entsprechend.

---

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
Die Liste hat **27 Datenzeilen** ohne Kopfzeile. Es gibt 9 Spalten: Lieferant, Ansprechpartner, Ort, Telefon, E-Mail, Warengruppe, Letzte Bestellung, Jahresumsatz EUR und Bewertung.

**2. Probleme**

- **Datumsformate (Spalte "Letzte Bestellung")** sind uneinheitlich:
  - `12.03.2024` (TT.MM.JJJJ)
  - `2024-02-28` (ISO)
  - `5.1.24` und `7.4.2024` (ohne führende Nullen, teils zweistellige Jahre)
  - `März 2024`, `Dez. 2023`, `April 2024` (nur Monat, kein Tag)
  - `15/01/2024` und `03/02/2024` (Schrägstriche)
  - Bei `03/02/2024` ist unklar, ob 3. Februar oder 2. März gemeint ist. Bei `15/01/2024` ist es eindeutig der 15. Januar.
  - Bei `Keller Dichtungstechnik` fehlt das Datum ganz.
- **Zahlenformate (Spalte "Jahresumsatz EUR")** sind sehr uneinheitlich:
  - `48.500,00` (deutsch)
  - `12.300` (Punkt als Tausendertrenner)
  - `31 200 €` (Leerzeichen und Eurozeichen)
  - `9800` (ohne Trennzeichen)
  - `18.400,00 €` und `41.000 EUR` (mit Währung)
  - `48500`, `12300,00` und `22750,5` (ohne Tausenderpunkt, mit Komma oder ohne Nachkommastellen)
  - Teilweise steht die Währung im Wert, obwohl sie schon im Spaltennamen steht.
  - Ein Wert wie `7.400` ist formal mehrdeutig, kann aber nur 7.400 € bedeuten.
- **Fehlende Werte:**
  - Umsatz fehlt bei `Koch Elektronik` (leer) und `Richter Glas & Optik` (`n/a`).
  - Bewertung fehlt bei `Bauer Präzisionsteile` und `Keller Dichtungstechnik`.
  - Ansprechpartner fehlt bei `Lackierwerk Ost GmbH` und `Schwarz Gießerei`.
  - E-Mail fehlt bei `Hoffmann Logistik` und `Krüger Gummiwaren`.
  - Telefon fehlt bei `Becker Werkzeugbau`.
  - Bestelldatum fehlt bei `Keller Dichtungstechnik`.
- **Schreibweisen Ort:** `Beispielstadt`, `musterhausen`, `MUSTERHAUSEN`, `fiktivhausen`, `neustadt a. d. probe`, `Neustadt a.d. Probe`, `Neustadt an der Probe` und `Neustadt a. d. Probe` kommen jeweils in verschiedenen Varianten vor (Groß-/Kleinschreibung, Abkürzungen).
- **Schreibweisen Firmennamen:**
  - `Müller` und `Mueller`
  - `Schmidt & Söhne` und `Schmidt und Söhne`
  - `Elektro Krause` und `ELEKTRO KRAUSE GmbH`
  - `Weber Kunststofftechnik` und `Weber Kunststoff-Technik GmbH`
  - Rechtsformen (GmbH, KG) sind mal angegeben, mal nicht.
- **Anreden und Namen:** `Herr K. Brandt` und `K. Brandt`, `Frau Lea Schmidt` und `Lea Schmidt`, `Herr Krause` und `Hr. Krause`, `Frau Dr. Weber` und `Dr. Weber`. Die Anreden sind uneinheitlich.
- **Telefon:** `0000 111201` und `0000-111201` haben unterschiedliche Trennzeichen.
- **Warengruppen** sind nicht einheitlich: `Schrauben/Normteile` und `Normteile`, `Elektrokomponenten` und `Elektro`, `Kunststoffteile` und `Kunststoff`. Außerdem werden `Elektronik` und `Elektrokomponenten` ähnlich verwendet.
- **Bewertung:** `a` und `b` stehen in Kleinbuchstaben, sonst steht A, B oder C.
- **Sortierung:** Die Liste ist weder alphabetisch noch nach Umsatz oder Datum sortiert.

**3. Mögliche Dubletten**

| Zeilen | Einträge | Begründung |
|---|---|---|
| 1 und 7 | Müller Stahlhandel GmbH / Mueller Stahlhandel | Gleiche E-Mail (brandt@stahl-mueller...), gleiche Telefonnummer (nur anderes Trennzeichen), gleicher Ansprechpartner K. Brandt, gleiche Warengruppe, gleiches Datum 12.03.2024, gleicher Umsatz 48.500. |
| 2 und 10 | Schmidt & Söhne KG / Schmidt und Söhne KG | Gleiche E-Mail, gleiche Telefonnummer, gleiche Ansprechpartnerin, gleiches Datum 28.02.2024, gleicher Umsatz 12.300. |
| 3 und 14 | Elektro Krause / ELEKTRO KRAUSE GmbH | Gleiche E-Mail, gleiche Telefonnummer, gleiches Datum 05.01.2024, gleicher Umsatz 31.200. |
| 4 und 18 | Weber Kunststofftechnik / Weber Kunststoff-Technik GmbH | Gleiche E-Mail, gleiche Telefonnummer, gleiches Datum März 2024 (01.03.2024), gleicher Umsatz 22.750,50. |

(Die Zeilennummern zählen ab den Datenzeilen, also ohne Kopfzeile.)

Das sind **4 Dublettenpaare**. Bei allen stimmen Kontaktdaten und Umsatz überein, sodass sie sehr wahrscheinlich derselbe Lieferant sind. Nach dem Entfernen bleiben **23 eindeutige Lieferanten**.

Keine Dubletten sind aus meiner Sicht `Braun Transporte` und `Hoffmann Logistik`. Beide sind Speditionen, haben aber andere Kontakte, Orte und Telefonnummern. `Fischer Kabelkonfektion` und `Koch Elektronik` sind ebenfalls eigenständige Firmen.

#### Nutzer 2

Bilde die Summe der Jahresumsätze nach Entfernen der Dubletten. Lieferanten ohne Umsatzangabe lässt du weg und nennst sie.

#### Assistent 2

Ich habe jeweils den ersten Eintrag eines Dublettenpaars behalten und den zweiten entfernt. Bei allen vier Paaren sind die Umsätze identisch, die Wahl ändert die Summe also nicht.

**Weggelassen wegen fehlender Umsatzangabe:**
- Richter Glas & Optik (Wert `n/a`)
- Koch Elektronik (Feld leer)

Damit fließen **21 von 23** eindeutigen Lieferanten in die Summe ein.

**Einzelwerte (in EUR):**

| Lieferant | Umsatz |
|---|---|
| Müller Stahlhandel GmbH | 48.500,00 |
| Schmidt & Söhne KG | 12.300,00 |
| Elektro Krause | 31.200,00 |
| Weber Kunststofftechnik | 22.750,50 |
| Lackierwerk Ost GmbH | 9.800,00 |
| Hoffmann Logistik | 18.400,00 |
| Bauer Präzisionsteile | 27.100,00 |
| Zimmermann Verpackung | 6.250,00 |
| Fischer Kabelkonfektion | 14.900,00 |
| Becker Werkzeugbau | 41.000,00 |
| Schulz Industriebedarf | 3.150,75 |
| Wagner Hydraulik | 19.800,00 |
| Keller Dichtungstechnik | 7.400,00 |
| Neumann Sensorik | 55.600,00 |
| Schwarz Gießerei | 63.200,00 |
| Lange Büroservice | 1.200,00 |
| Hartmann Motoren | 37.450,00 |
| Krüger Gummiwaren | 4.800,00 |
| Wolf Messtechnik | 16.000,00 |
| Braun Transporte | 11.300,00 |
| Schäfer Schweißtechnik | 8.900,00 |

**Summe: 461.001,25 EUR**

**Hinweise:**
- Ich habe die verschiedenen Zahlenformate vereinheitlicht. Dabei habe ich Punkte als Tausendertrenner gelesen, zum Beispiel `12.300` als 12.300 und `7.400` als 7.400.
- Die Summe ist nur so zuverlässig wie die Annahme, dass die vier Paare tatsächlich Dubletten sind. Ohne Dublettenbereinigung wären es 461.001,25 + 48.500 + 12.300 + 31.200 + 22.750,50 = **575.751,75 EUR**.
- Die zwei fehlenden Umsätze (Richter, Koch) sind in der Summe nicht enthalten. Die tatsächliche Gesamtsumme ist daher vermutlich höher.

---

### Opus

#### Nutzer 1

Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.

#### Assistent 1

Ich habe die Liste nur gelesen und nichts daran geändert. Das sind die Ergebnisse:

**1. Anzahl der Zeilen**

Ohne Kopfzeile hat die Liste **27 Datenzeilen**. Weil es Dubletten gibt (siehe Punkt 3), stecken darin aber nur **23 verschiedene Lieferanten**.

**2. Probleme**

*a) Datumsformate (Spalte „Letzte Bestellung")*. Es gibt mindestens sieben verschiedene Formate:
- TT.MM.JJJJ: `12.03.2024`
- ISO-Format JJJJ-MM-TT: `2024-02-28`
- Kurzform mit zweistelligem Jahr: `5.1.24`, `7.4.2024`
- Schrägstriche: `15/01/2024`, `03/02/2024`. Das zweite Datum ist mehrdeutig: 3. Februar oder 2. März?
- Nur Monat und Jahr: `März 2024`, `April 2024`, `Dez. 2023`. Hier fehlt der Tag.
- Leerer Wert: Keller Dichtungstechnik

*b) Beträge (Spalte „Jahresumsatz EUR")*
- Verschiedene Schreibweisen: `48.500,00`, `12.300`, `9800`, `22750,5`, `31 200 €`, `18.400,00 €`, `41.000 EUR`, `11.300 EUR`
- Teils steht ein Währungszeichen oder „EUR" im Feld, obwohl die Währung schon im Spaltennamen steht.
- Einmal steht Text statt einer Zahl: `n/a` (Richter Glas & Optik).
- Einmal ist das Feld leer (Koch Elektronik).

*c) Schreibweisen*
- **Ort:** `musterhausen`, `MUSTERHAUSEN` und `Musterhausen` kommen gemischt vor, ebenso `fiktivhausen` und `Fiktivhausen`. Für Neustadt gibt es mehrere Varianten: `Neustadt a. d. Probe`, `Neustadt a.d. Probe`, `Neustadt an der Probe` und `neustadt a. d. probe`.
- **Firmennamen:** mal mit und mal ohne Rechtsform (GmbH, KG). Außerdem `ü`/`ue`, `&`/`und` und Großschreibung (`ELEKTRO KRAUSE`).
- **Ansprechpartner:** mal mit Anrede, mal ohne (`Herr K. Brandt` / `K. Brandt`) und unterschiedliche Abkürzungen (`Herr` / `Hr.`).
- **Telefon:** mal mit Leerzeichen, mal mit Bindestrich (`0000 111201` / `0000-111201`).
- **Warengruppe:** Gleiches heißt unterschiedlich, z. B. `Elektrokomponenten` / `Elektro`, `Kunststoffteile` / `Kunststoff`, `Schrauben/Normteile` / `Normteile`.
- **Bewertung:** Kleinbuchstaben `a` (Wolf Messtechnik) und `b` (Schäfer Schweißtechnik) neben Großbuchstaben.

*d) Fehlende Werte*
- Ansprechpartner: Lackierwerk Ost GmbH, Schwarz Gießerei
- Telefon: Becker Werkzeugbau
- E-Mail: Hoffmann Logistik, Krüger Gummiwaren
- Letzte Bestellung: Keller Dichtungstechnik
- Jahresumsatz: Richter Glas & Optik (`n/a`), Koch Elektronik (leer)
- Bewertung: Bauer Präzisionsteile, Keller Dichtungstechnik

*e) Dubletten*: Es gibt 4 Paare, die Details stehen unter Punkt 3.

**3. Mögliche Dubletten**

| # | Eintrag A | Eintrag B | Begründung |
|---|---|---|---|
| 1 | Müller Stahlhandel GmbH (Zeile 1) | Mueller Stahlhandel (Zeile 7) | Gleiche Telefonnummer (nur anders formatiert), gleiche E-Mail, gleicher Ansprechpartner (K. Brandt), gleicher Ort und gleiche Warengruppe. Das Datum ist gleich (12.03.2024 = 2024-03-12), der Umsatz auch (48.500). Unterschiede: nur ü/ue und die fehlende „GmbH". |
| 2 | Schmidt & Söhne KG (Zeile 2) | Schmidt und Söhne KG (Zeile 10) | Gleiche Telefonnummer, gleiche E-Mail, gleiche Ansprechpartnerin (Lea Schmidt). Das Datum ist gleich (28.02.2024), der Umsatz auch (12.300). Unterschiede: „&" statt „und", Schreibweise des Orts und die Warengruppe. |
| 3 | Elektro Krause (Zeile 3) | ELEKTRO KRAUSE GmbH (Zeile 14) | Gleiche Telefonnummer, gleiche E-Mail, gleicher Ansprechpartner (Herr/Hr. Krause). Das Datum ist gleich (5.1.24 = 05.01.2024), der Umsatz auch (31.200). |
| 4 | Weber Kunststofftechnik (Zeile 4) | Weber Kunststoff-Technik GmbH (Zeile 18) | Gleiche Telefonnummer, gleiche E-Mail, gleiche Ansprechpartnerin (Dr. Weber). Der Umsatz ist gleich (22.750,50). Die Daten passen zueinander („März 2024" und 01.03.2024). |

Die Zeilennummern zählen die Datenzeilen ohne Kopfzeile.

Diese Lieferanten sehen sich ähnlich, sind aber **keine Dubletten**:
- Elektro Krause, Fischer Kabelkonfektion und Koch Elektronik: gleicher Ort und ähnliche Warengruppe, aber andere Firma, Telefonnummer und E-Mail.
- Keller Dichtungstechnik und Krüger Gummiwaren: beide liefern Dichtungen, sind aber verschiedene Firmen.
- Hoffmann Logistik und Braun Transporte: beide sind Speditionen, aber verschiedene Firmen.

Ob die vier Paare wirklich dieselbe Firma sind, sollte am besten jemand im Einkauf oder im Lieferantenstamm bestätigen.

#### Nutzer 2

Bilde die Summe der Jahresumsätze nach Entfernen der Dubletten. Lieferanten ohne Umsatzangabe lässt du weg und nennst sie.

#### Assistent 2

Bei den vier Dubletten habe ich jeden Lieferanten nur einmal gezählt. Das geht ohne Abwägen, weil der Umsatz in beiden Einträgen eines Paars gleich ist. Ich habe alle Beträge so gelesen, wie man Zahlen in Deutschland schreibt: Punkt bzw. Leerzeichen trennen die Tausender, das Komma steht vor den Cent.

**Weggelassen, weil der Umsatz fehlt:**
- Richter Glas & Optik (Wert `n/a`)
- Koch Elektronik (Feld leer)

**Lieferanten in der Summe (21):**

| Lieferant | Jahresumsatz EUR |
|---|---:|
| Müller Stahlhandel GmbH | 48.500,00 |
| Schmidt & Söhne KG | 12.300,00 |
| Elektro Krause (GmbH) | 31.200,00 |
| Weber Kunststofftechnik (GmbH) | 22.750,50 |
| Lackierwerk Ost GmbH | 9.800,00 |
| Hoffmann Logistik | 18.400,00 |
| Bauer Präzisionsteile | 27.100,00 |
| Zimmermann Verpackung | 6.250,00 |
| Fischer Kabelkonfektion | 14.900,00 |
| Becker Werkzeugbau | 41.000,00 |
| Schulz Industriebedarf | 3.150,75 |
| Wagner Hydraulik | 19.800,00 |
| Keller Dichtungstechnik | 7.400,00 |
| Neumann Sensorik | 55.600,00 |
| Schwarz Gießerei | 63.200,00 |
| Lange Büroservice | 1.200,00 |
| Hartmann Motoren | 37.450,00 |
| Krüger Gummiwaren | 4.800,00 |
| Wolf Messtechnik | 16.000,00 |
| Braun Transporte | 11.300,00 |
| Schäfer Schweißtechnik | 8.900,00 |
| **Summe** | **461.001,25** |

**Ergebnis: Die bereinigte Summe der Jahresumsätze beträgt 461.001,25 €.**

Zum Vergleich: Zählt man die Dubletten doppelt, käme man auf 575.751,75 €. Das sind 114.750,50 € zu viel.

Bitte prüfen Sie die Summe in Excel nach, bevor Sie damit weiterarbeiten. Bei so vielen Zahlenformaten kann sich beim Lesen leicht ein Fehler einschleichen.
