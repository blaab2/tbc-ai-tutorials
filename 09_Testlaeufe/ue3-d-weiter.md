# Testlauf: Übung 3 / Station D Weiter – Liste bereinigen und als CSV ausgeben

**Herkunft:** Station D, Stufen „Basis“ und „Weiter“ (inkl. Folgeprompt „als CSV“) aus [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#station-d-unordentliche-tabelle-bereinigen). Material: [lieferantenliste_unsortiert.csv](../07_Beispielmaterial/lieferantenliste_unsortiert.csv). Zugehörige Lösungshinweise: [Trainer-Loesungshinweise.md – Station D](../06_Uebungen/Trainer-Loesungshinweise.md#station-d-lieferantenliste-bereinigen) („Eckdaten zum Abgleichen“, „Typische Datenprobleme“, „Woran du ein gutes Ergebnis erkennst“, „Typische Stolpersteine“).

> **Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf (jeweils ein Chat, drei Nachrichten, CSV angehängt bzw. eingefügt):**

1. Basis-Prompt (Analyse ohne Änderung: Zeilen, Probleme, Dubletten)
2. Weiter-Prompt (Bereinigung nach fünf Regeln, Tabelle, Zeilen vorher/nachher, zusammengeführte Zeilen)
3. Folgeprompt „Gib mir die bereinigte Liste noch einmal als CSV mit Semikolon …“

**Was laut Material herauskommen soll:** 27 Datenzeilen → 23 Zeilen (27 − 4 = 23); genau die Paare 1+7, 2+10, 3+14, 4+18 (Datenzeilen, ohne Kopfzeile gezählt) zusammengeführt; fehlende Werte als „FEHLT“ (Ansprechpartner Lackierwerk Ost und Schwarz Gießerei, Telefon Becker, E-Mail Hoffmann und Krüger, Datum Keller, Umsatz Richter „n/a“ und Koch leer, Bewertung Bauer und Keller); in „Hinweis“: Braun „03/02/2024“ mehrdeutig, „März 2024“ / „Dez. 2023“ / „April 2024“ ohne Tag (kein still erfundener 1.), Weber „März 2024“ vs. „2024-03-01“; Beträge wertgleich; vollständige Semikolon-CSV mit Kopf + 23 Datenzeilen und Spalte „Hinweis“.

**Nachprüfung per Python:**

```
python3: Datenzeilen im Original = 27
Datenzeilen ohne die Dubletten (7, 10, 14, 18) = 23
Summe der 21 vorhandenen Beträge nach Bereinigung = 461.001,25 (mit Dubletten 575.751,75)
```

Die drei CSV-Ausgaben (Turn 3) wurden aus diesem Protokoll extrahiert und Zelle für Zelle gegen eine aus dem Original berechnete Soll-Liste (Lieferant, Telefon-Ziffern, E-Mail, Datum, Betrag, Bewertung, FEHLT-Stellen) verglichen. Ergebnis: **bei allen drei Modellen 23 Datenzeilen + Kopf, 10 Spalten je Zeile, alle 23 Beträge wertgleich, alle eindeutigen Daten korrekt umgerechnet, alle 11 FEHLT-Stellen richtig, keine erfundenen Werte, keine ausgelassenen Zeilen.** Die Lösungshinweise (Eckdaten, Kontrollsumme) stimmen.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Zeilen vorher 27 (Basis + Weiter) | ja | ja | ja |
| Zeilen nachher 23, Rechnung 27 − 4 = 23 | ja | ja | ja |
| Genau die 4 richtigen Paare, keine falschen | ja | ja | ja |
| Zeilennummern der Paare konsistent | ja (1+7, 2+10, 3+14, 4+18) | **nein** – Basis und Hinweis-Spalte: 2+8, 3+11, 4+15, 5+19 (Datei-Zeilen mit Kopf), Zusammenfassung: 1+7 usw. | ja |
| Falsche Treffer ausdrücklich ausgeschlossen | ja (Keller/Krüger, Krause/Fischer/Koch) | ja (Fischer, Hoffmann/Braun) | ja (alle drei Gruppen aus den Lösungshinweisen) |
| Alle 11 FEHLT-Stellen korrekt | ja | ja | ja |
| Datum ohne Tag nicht erfunden (Becker, Wolf) | ja, FEHLT + Hinweis | ja, FEHLT + Hinweis | ja, „FEHLT (nur Monat bekannt: …)“ + Hinweis |
| Weber 01.03.2024 als Übernahme markiert | ja | ja | ja |
| Braun 03/02/2024 als mehrdeutig markiert | ja | ja | ja |
| Beträge wertgleich (12.300 → 12.300,00; 22750,5 → 22.750,50) | ja (23/23) | ja (23/23) | ja (23/23) |
| Warengruppen-Widerspruch: beide Werte behalten + markiert | ja („bzw.“) | ja („/“) | ja („\|“ + [WIDERSPRUCH]) |
| CSV vollständig (Kopf + 23, Spalte Hinweis) | ja | ja | ja (nennt selbst „1 Kopfzeile, 23 Datenzeilen“) |
| CSV inhaltsgleich zur Tabelle aus Turn 2 | ja | **nein** – Hinweise gekürzt (u. a. „Bewertung a/b → A/B“, „Ort korrigiert“, „Datum aus 7.4.2024“ weggefallen) | ja (nur Anführungszeichen entfernt) |
| Excel-Tipps sachlich richtig | ja | teilweise (Telefon „verliert führende Nullen“ trifft hier nicht zu) | ja |
| Erfundenes | nein | nein | nein |
| **Stolpersteine aus den Lösungshinweisen treten auf?** (verschluckte Zeilen, falsche Zählung, stille Annahmen, verfälschte Beträge) | **nein** | **nein** (nur Nummerierungs-Mix) | **nein** |

---

## Gefundene Fehler mit Beleg

Keine inhaltlichen Datenfehler bei allen drei Modellen. Gefunden wurden nur Folgendes:

1. **Sonnet – widersprüchliche Zeilennummern.** In der Basis-Antwort nennt Sonnet die Paare „2 und 8“, „3 und 11“, „4 und 15“, „5 und 19“ und „Fischer Kabelkonfektion (Zeile 12)“. Das sind die Zeilennummern der Datei *mit* Kopfzeile (Original: Zeile 2 = Müller, Zeile 8 = Mueller, Zeile 12 = Fischer). In der Weiter-Antwort steht in der Hinweis-Spalte weiterhin „Zusammengeführt aus Zeile 2 und 8“ usw., in der Zusammenfassung darunter aber „Müller Stahlhandel (Zeile 1 und 7)“ mit dem Zusatz „Zählung beginnt bei der ersten Datenzeile“. Dieselbe Antwort nennt also für dasselbe Paar zwei verschiedene Nummern; in die CSV wandert die Datei-Zählung („Zeile 2 und 8“). Kein Datenfehler, aber genau die Verwirrung, die beim Prüfschritt „Zeilen zählen“ im Texteditor entsteht (dort steht Müller in Zeile 2).
2. **Sonnet – CSV nicht identisch zur Tabelle.** Gefragt war „die bereinigte Liste noch einmal“. In der CSV fehlen gegenüber der Tabelle mehrere Hinweise: Wolf „Bewertung "a" zu "A"“, Schäfer „Bewertung "b" zu "B"“ (Hinweis-Zelle jetzt leer), Lange „Datum aus 7.4.2024 umgewandelt“ (leer), Schmidt „Ort "musterhausen" korrigiert“, Hoffmann/Becker/Neumann „Ort korrigiert“. Datenwerte sind unverändert; nur die Prüfspur ist dünner geworden – unangekündigt.
3. **Sonnet – Excel-Tipp passt nicht.** „Die Telefonnummern können führende Nullen verlieren.“ Alle Nummern stehen als „0000 123456“ mit Leerzeichen; Excel liest das als Text, die Nullen bleiben erhalten. Allgemein richtiger Tipp, hier aber nicht zutreffend.
4. **Kleinigkeiten (kein Fehler im engeren Sinn):**
   - Opus, Hinweis Müller: „Alle Angaben gleich“ – inhaltlich ja, formal unterschieden sich Rechtsform, Anrede, Telefon-Bindestrich, Datums- und Betragsformat.
   - Opus, Hinweis Krause: „Vorname des Ansprechpartners fehlt“ – gilt ebenso für Becker, Schulz, Keller, Richter, Lange u. a., wird dort aber nicht vermerkt (uneinheitlich).
   - Haiku, Hinweis Lackierwerk: „Ort 'Beispielstadt-Ost' mit 'Beispielstadt' abgleichen“ – Vermutung ohne Anlass in den Daten; harmlos, weil als Prüfhinweis formuliert.
   - Haiku und Sonnet nennen die übernommene Rechtsform „GmbH“ bei Weber nicht (Haiku) bzw. nur bei Krause und Weber (Sonnet); Opus regt „Offizielle Schreibweise prüfen“ an. Alle drei bilden „Weber Kunststofftechnik GmbH“ – eine Mischform aus beiden Einträgen, die so in keiner Zeile stand.
   - Die Regel „wenn sich Angaben widersprechen, beide Werte behalten“ wird beim Weber-Datum von keinem Modell wörtlich umgesetzt: in der Zelle steht 01.03.2024, „März 2024“ nur im Hinweis. Das ist vertretbar (die Angaben sind vereinbar) und entspricht den Lösungshinweisen.

---

## Lehren für die Auswertung

- **Die angekündigten Stolpersteine traten nicht auf.** Keine verschluckten Zeilen, kein „… weitere Zeilen“, keine falsche Zählung, „12.300“ wurde nie zu 12,30, „22750,5“ nie zu 2.275.050, keine still erfundenen Tage. Bei 27 Zeilen × 9 Spalten sind aktuelle Modelle offenbar sicher genug. Der Trainer sollte das nicht als „KI macht immer Fehler“ verkaufen, sondern ehrlich sagen: *Bei dieser Größe klappt es oft – bei 500 Zeilen oder mit älteren/kleineren Tools nicht. Der Prüfschritt bleibt Pflicht, weil man vorher nicht weiß, welcher Fall eintritt.*
- **Lehrstück „Wie zählt die KI?“ (Sonnet):** Die KI kann Datei-Zeilen (mit Kopfzeile, so wie der Texteditor sie anzeigt) oder Datenzeilen zählen – und mischt das sogar innerhalb einer Antwort. Gute Brücke zum Prüfschritt: „Welche Zeile ist bei dir Zeile 1?“ Vorschlag für eine Nachfrage: *„Welche Zählweise verwendest du für die Zeilennummern – mit oder ohne Kopfzeile? Bitte einheitlich.“*
- **„Noch einmal“ heißt nicht „identisch“:** Sonnet hat beim Umformatieren zur CSV still Hinweise gekürzt. Daten blieben richtig, aber genau diese Art Veränderung übersieht man. Lehre: Auch eine Umformatierung ist eine neue Ausgabe und braucht eine (kurze) Stichprobe – z. B. Zeilenzahl und zwei, drei Hinweis-Zellen.
- **Gute Praxis zum Zeigen:** Alle drei Modelle haben Annahmen offengelegt (Braun 03/02, Weber-Tag aus der Dublette, Tausenderpunkt-Lesart). Opus' Format „FEHLT (nur Monat bekannt: 12.2023)“ und „Wert 1 | Wert 2 [WIDERSPRUCH]“ ist besonders gut filterbar – ein schönes Beispiel, wie man Markierungen *vorgibt*.
- **Stichprobe lohnt sich trotzdem:** Für den Prüfschritt eignen sich Weber (Datum, Betrag 22750,5, Rechtsform), Braun (mehrdeutiges Datum) und Schmidt (12.300, Warengruppen-Widerspruch). Bei allen drei Modellen stimmen sie – Teilnehmende sollen das *selbst* feststellen.
- **Unterschiede zwischen den Modellen sind gering;** Opus liefert die sorgfältigste Prüfspur und die korrekteste Excel-Anleitung, Haiku ist knapp und vollständig, Sonnet ist inhaltlich richtig, aber mit Nummerierungs- und Konsistenzmängeln.
- **Zeit:** Drei lange Antworten (eine Tabelle mit 23 × 11 Zellen, dann noch einmal als CSV) plus Prüfschritt passen in die 27 Minuten nur, wenn die Teilnehmenden beim Lesen nicht Zeile für Zeile prüfen, sondern gezielt die Checkliste abarbeiten. Wer zusätzlich die CSV in Excel öffnet, braucht mehr Zeit (Umlaute/Import).

---

## Gesprächsprotokolle

### Haiku

#### Nutzer 1

Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon). [Anhang: lieferantenliste_unsortiert.csv]
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.

#### Assistent 1

1. Die Liste hat **27 Datenzeilen** (ohne Kopfzeile), 28 Zeilen insgesamt. Zeilen werden im Folgenden nach Datenzeile 1 bis 27 gezählt.

2. **Probleme**
- **Datumsformate uneinheitlich:** TT.MM.JJJJ, JJJJ-MM-TT, "5.1.24", "7.4.2024", "15/01/2024", "03/02/2024" (Tag/Monat hier nicht eindeutig), "März 2024", "April 2024", "Dez. 2023" (nur Monat, kein Tag).
- **Zahlenformate uneinheitlich:** "48.500,00", "48500", "12.300" (Tausenderpunkt oder Dezimalpunkt?), "12300,00", "31 200 €", "22750,5", "63.200 €", "9800".
- **Telefonnummern:** "0000 111201" vs. "0000-111201".
- **Firmennamen:** "Müller" vs. "Mueller"; "Schmidt & Söhne KG" vs. "Schmidt und Söhne KG"; "Elektro Krause" vs. "ELEKTRO KRAUSE GmbH"; "Weber Kunststofftechnik" vs. "Weber Kunststoff-Technik GmbH".
- **Orte:** "musterhausen" / "MUSTERHAUSEN"; "Neustadt a.d. Probe" / "neustadt a. d. probe" / "Neustadt an der Probe"; "Beispielstadt-Ost" unklar.
- **Anreden:** "Herr", "Hr.", "Frau", "Dr." oder gar keine.
- **Bewertung:** Kleinbuchstaben "a" (Zeile 24) und "b" (Zeile 27), sowie leer (Zeilen 8 und 16).
- **Fehlende Werte:**
  - E-Mail: Zeilen 6 und 23
  - Ansprechpartner: Zeilen 5 und 20
  - Telefon: Zeile 12
  - Letzte Bestellung: Zeile 16
  - Bewertung: Zeilen 8 und 16
  - Jahresumsatz: Zeile 26 leer, Zeile 17 "n/a"

3. **Mögliche Dubletten**
- **Zeilen 1 und 7** (Müller Stahlhandel GmbH / Mueller Stahlhandel): gleiche E-Mail, gleiche Telefonnummer, gleicher Ansprechpartner (K. Brandt), gleicher Ort, gleiche Warengruppe, gleicher Umsatz (48.500) und gleiches Datum (12.03.2024 = 2024-03-12). Sehr wahrscheinlich dieselbe Firma.
- **Zeilen 2 und 10** (Schmidt & Söhne KG / Schmidt und Söhne KG): gleiche E-Mail und Telefonnummer, gleicher Umsatz (12.300 = 12300,00), gleiches Datum (28.02.2024), gleiche Bewertung (B). Sehr wahrscheinlich dieselbe Firma.
- **Zeilen 3 und 14** (Elektro Krause / ELEKTRO KRAUSE GmbH): gleiche E-Mail und Telefonnummer, gleicher Umsatz (31.200), Datum 5.1.24 = 05.01.2024, gleiche Bewertung (A). Sehr wahrscheinlich dieselbe Firma.
- **Zeilen 4 und 18** (Weber Kunststofftechnik / Weber Kunststoff-Technik GmbH): gleiche E-Mail und Telefonnummer, gleicher Umsatz (22.750,50), Datum März 2024 passt zu 2024-03-01, gleiche Bewertung (B). Sehr wahrscheinlich dieselbe Firma.
- **Ähnlich, aber nach meiner Einschätzung verschiedene Firmen:** Keller Dichtungstechnik (Zeile 16) und Krüger Gummiwaren (Zeile 23) beide Dichtungen, aber andere Adressen und Mailadressen. Elektro Krause und Fischer Kabelkonfektion bzw. Koch Elektronik haben unterschiedliche Kontakte.

#### Nutzer 2

Bereinige jetzt die Liste nach diesen Regeln:
- Datumsformat überall TT.MM.JJJJ
- Firmennamen einheitlich schreiben (gleiche Firma = gleiche Schreibweise)
- Dubletten zusammenführen; wenn sich Angaben widersprechen, beide Werte behalten und markieren
- Fehlende Werte NICHT erfinden, sondern als "FEHLT" kennzeichnen
- Neue Spalte "Hinweis" für alles, was ich manuell prüfen sollte

Gib das Ergebnis als Tabelle aus. Nenne danach: Anzahl Zeilen vorher, Anzahl Zeilen nachher, und welche Zeilen zusammengeführt wurden.

#### Assistent 2

Bereinigte Liste (23 Zeilen):

| Lieferant | Ansprechpartner | Ort | Telefon | E-Mail | Warengruppe | Letzte Bestellung | Jahresumsatz EUR | Bewertung | Hinweis |
|---|---|---|---|---|---|---|---|---|---|
| Müller Stahlhandel GmbH | Herr K. Brandt | Beispielstadt | 0000 111201 | brandt@stahl-mueller.example.com | Stahl | 12.03.2024 | 48.500,00 | A | Dublette aus Zeilen 1 und 7 zusammengeführt - Name 'Mueller' in Zeile 7 zu 'Müller' vereinheitlicht |
| Schmidt & Söhne KG | Frau Lea Schmidt | Musterhausen | 0000 222301 | l.schmidt@schmidt-soehne.example.com | Schrauben/Normteile bzw. Normteile | 28.02.2024 | 12.300,00 | B | Dublette aus Zeilen 2 und 10 zusammengeführt - Warengruppe widerspricht sich, bitte prüfen |
| Elektro Krause GmbH | Herr Krause | Neustadt a. d. Probe | 0000 333401 | info@elektro-krause.example.com | Elektrokomponenten bzw. Elektro | 05.01.2024 | 31.200,00 | A | Dublette aus Zeilen 3 und 14 zusammengeführt - Warengruppe widerspricht sich, bitte prüfen - GmbH nur in Zeile 14 angegeben |
| Weber Kunststofftechnik GmbH | Frau Dr. Weber | Fiktivhausen | 0000 444501 | weber@weber-kunststoff.example.com | Kunststoffteile bzw. Kunststoff | 01.03.2024 | 22.750,50 | B | Dublette aus Zeilen 4 und 18 zusammengeführt - Warengruppe widerspricht sich, bitte prüfen - Datum in Zeile 4 nur als März 2024, Tag aus Zeile 18 übernommen |
| Lackierwerk Ost GmbH | FEHLT | Beispielstadt-Ost | 0000 555601 | kontakt@lackierwerk-ost.example.com | Oberflächen | 14.11.2023 | 9.800,00 | C | Ansprechpartner FEHLT - Ort 'Beispielstadt-Ost' mit 'Beispielstadt' abgleichen |
| Hoffmann Logistik | Herr Tim Hoffmann | Musterhausen | 0000 666701 | FEHLT | Spedition | 01.04.2024 | 18.400,00 | A | E-Mail FEHLT |
| Bauer Präzisionsteile | Herr S. Bauer | Probeheim | 0000 777801 | s.bauer@bauer-praezision.example.com | Drehteile | 20.02.2024 | 27.100,00 | FEHLT | Bewertung FEHLT |
| Zimmermann Verpackung | Frau Nina Zimmermann | Musterhausen | 0000 888901 | n.zimmermann@zv-verpackung.example.com | Verpackung | 15.01.2024 | 6.250,00 | B | Datum 15/01/2024 umgeschrieben |
| Fischer Kabelkonfektion | Herr Jan Fischer | Neustadt a. d. Probe | 0000 999001 | fischer@kabel-fischer.example.com | Elektrokomponenten | 03.03.2024 | 14.900,00 | A | |
| Becker Werkzeugbau | Frau Becker | Fiktivhausen | FEHLT | info@becker-werkzeug.example.com | Werkzeuge | FEHLT | 41.000,00 | B | Telefon FEHLT - Letzte Bestellung nur als Dez. 2023 angegeben |
| Schulz Industriebedarf | Herr Schulz | Beispielstadt | 0000 121314 | schulz@schulz-ib.example.com | Verbrauchsmaterial | 08.04.2024 | 3.150,75 | C | |
| Wagner Hydraulik | Frau Eva Wagner | Probeheim | 0000 141516 | e.wagner@wagner-hydraulik.example.com | Hydraulik | 22.01.2024 | 19.800,00 | B | |
| Keller Dichtungstechnik | Herr Keller | Musterhausen | 0000 161718 | keller@dichtung-keller.example.com | Dichtungen | FEHLT | 7.400,00 | FEHLT | Letzte Bestellung FEHLT, Bewertung FEHLT |
| Richter Glas & Optik | Frau Richter | Beispielstadt | 0000 181920 | richter@richter-optik.example.com | Optik | 09.02.2024 | FEHLT | B | Jahresumsatz war 'n/a' - FEHLT |
| Neumann Sensorik | Herr Paul Neumann | Neustadt a. d. Probe | 0000 202122 | p.neumann@neumann-sensorik.example.com | Sensoren | 18.03.2024 | 55.600,00 | A | |
| Schwarz Gießerei | FEHLT | Gießdorf | 0000 222324 | info@giesserei-schwarz.example.com | Gussteile | 30.10.2023 | 63.200,00 | C | Ansprechpartner FEHLT |
| Lange Büroservice | Frau Lange | Beispielstadt | 0000 242526 | lange@buero-lange.example.com | Büromaterial | 07.04.2024 | 1.200,00 | A | |
| Hartmann Motoren | Herr Hartmann | Probeheim | 0000 262728 | hartmann@hartmann-motoren.example.com | Antriebe | 30.01.2024 | 37.450,00 | B | |
| Krüger Gummiwaren | Frau Krüger | Gummidorf | 0000 282930 | FEHLT | Dichtungen | 12.12.2023 | 4.800,00 | C | E-Mail FEHLT |
| Wolf Messtechnik | Herr Dr. Wolf | Musterhausen | 0000 303132 | wolf@wolf-messtechnik.example.com | Messtechnik | FEHLT | 16.000,00 | A | Letzte Bestellung nur als April 2024 angegeben - Bewertung von 'a' zu 'A' korrigiert |
| Braun Transporte | Herr Braun | Beispielstadt | 0000 323334 | braun@braun-transporte.example.com | Spedition | 03.02.2024 | 11.300,00 | B | Datum 03/02/2024 als 03.02.2024 gelesen - bitte prüfen, auch 02.03.2024 möglich |
| Koch Elektronik | Frau Koch | Neustadt a. d. Probe | 0000 343536 | koch@koch-elektronik.example.com | Elektronik | 14.02.2024 | FEHLT | B | Jahresumsatz FEHLT |
| Schäfer Schweißtechnik | Herr Schäfer | Fiktivhausen | 0000 363738 | schaefer@schaefer-schweiss.example.com | Schweißzubehör | 19.03.2024 | 8.900,00 | B | Bewertung von 'b' zu 'B' korrigiert |

**Anzahl Zeilen vorher:** 27 Datenzeilen
**Anzahl Zeilen nachher:** 23 Datenzeilen

**Zusammengeführte Zeilen:**
- Zeilen 1 + 7: Müller Stahlhandel GmbH
- Zeilen 2 + 10: Schmidt & Söhne KG
- Zeilen 3 + 14: Elektro Krause GmbH
- Zeilen 4 + 18: Weber Kunststofftechnik GmbH

Hinweise zur Bereinigung: Zahlen mit Punkt wurden als Tausendertrennzeichen gelesen (z. B. "14.900" = 14.900,00). Bei "FEHLT" bei Datumsangaben ohne Tag ist der Originalwert im Hinweis vermerkt. Widersprüchliche Warengruppen wurden beide übernommen und markiert.

#### Nutzer 3

Gib mir die bereinigte Liste noch einmal als CSV mit Semikolon als Trennzeichen, damit ich sie in Excel öffnen kann.

#### Assistent 3

Hier ist die bereinigte Liste als CSV (Trennzeichen Semikolon). Falls Umlaute in Excel falsch angezeigt werden, die Datei über Daten > Aus Text/CSV mit Codierung UTF-8 importieren.

```csv
Lieferant;Ansprechpartner;Ort;Telefon;E-Mail;Warengruppe;Letzte Bestellung;Jahresumsatz EUR;Bewertung;Hinweis
Müller Stahlhandel GmbH;Herr K. Brandt;Beispielstadt;0000 111201;brandt@stahl-mueller.example.com;Stahl;12.03.2024;48.500,00;A;Dublette aus Zeilen 1 und 7 zusammengeführt - Name 'Mueller' in Zeile 7 zu 'Müller' vereinheitlicht
Schmidt & Söhne KG;Frau Lea Schmidt;Musterhausen;0000 222301;l.schmidt@schmidt-soehne.example.com;Schrauben/Normteile bzw. Normteile;28.02.2024;12.300,00;B;Dublette aus Zeilen 2 und 10 zusammengeführt - Warengruppe widerspricht sich, bitte prüfen
Elektro Krause GmbH;Herr Krause;Neustadt a. d. Probe;0000 333401;info@elektro-krause.example.com;Elektrokomponenten bzw. Elektro;05.01.2024;31.200,00;A;Dublette aus Zeilen 3 und 14 zusammengeführt - Warengruppe widerspricht sich, bitte prüfen - GmbH nur in Zeile 14 angegeben
Weber Kunststofftechnik GmbH;Frau Dr. Weber;Fiktivhausen;0000 444501;weber@weber-kunststoff.example.com;Kunststoffteile bzw. Kunststoff;01.03.2024;22.750,50;B;Dublette aus Zeilen 4 und 18 zusammengeführt - Warengruppe widerspricht sich, bitte prüfen - Datum in Zeile 4 nur als März 2024, Tag aus Zeile 18 übernommen
Lackierwerk Ost GmbH;FEHLT;Beispielstadt-Ost;0000 555601;kontakt@lackierwerk-ost.example.com;Oberflächen;14.11.2023;9.800,00;C;Ansprechpartner FEHLT - Ort 'Beispielstadt-Ost' mit 'Beispielstadt' abgleichen
Hoffmann Logistik;Herr Tim Hoffmann;Musterhausen;0000 666701;FEHLT;Spedition;01.04.2024;18.400,00;A;E-Mail FEHLT
Bauer Präzisionsteile;Herr S. Bauer;Probeheim;0000 777801;s.bauer@bauer-praezision.example.com;Drehteile;20.02.2024;27.100,00;FEHLT;Bewertung FEHLT
Zimmermann Verpackung;Frau Nina Zimmermann;Musterhausen;0000 888901;n.zimmermann@zv-verpackung.example.com;Verpackung;15.01.2024;6.250,00;B;Datum 15/01/2024 umgeschrieben
Fischer Kabelkonfektion;Herr Jan Fischer;Neustadt a. d. Probe;0000 999001;fischer@kabel-fischer.example.com;Elektrokomponenten;03.03.2024;14.900,00;A;
Becker Werkzeugbau;Frau Becker;Fiktivhausen;FEHLT;info@becker-werkzeug.example.com;Werkzeuge;FEHLT;41.000,00;B;Telefon FEHLT - Letzte Bestellung nur als Dez. 2023 angegeben
Schulz Industriebedarf;Herr Schulz;Beispielstadt;0000 121314;schulz@schulz-ib.example.com;Verbrauchsmaterial;08.04.2024;3.150,75;C;
Wagner Hydraulik;Frau Eva Wagner;Probeheim;0000 141516;e.wagner@wagner-hydraulik.example.com;Hydraulik;22.01.2024;19.800,00;B;
Keller Dichtungstechnik;Herr Keller;Musterhausen;0000 161718;keller@dichtung-keller.example.com;Dichtungen;FEHLT;7.400,00;FEHLT;Letzte Bestellung FEHLT, Bewertung FEHLT
Richter Glas & Optik;Frau Richter;Beispielstadt;0000 181920;richter@richter-optik.example.com;Optik;09.02.2024;FEHLT;B;Jahresumsatz war 'n/a' - FEHLT
Neumann Sensorik;Herr Paul Neumann;Neustadt a. d. Probe;0000 202122;p.neumann@neumann-sensorik.example.com;Sensoren;18.03.2024;55.600,00;A;
Schwarz Gießerei;FEHLT;Gießdorf;0000 222324;info@giesserei-schwarz.example.com;Gussteile;30.10.2023;63.200,00;C;Ansprechpartner FEHLT
Lange Büroservice;Frau Lange;Beispielstadt;0000 242526;lange@buero-lange.example.com;Büromaterial;07.04.2024;1.200,00;A;
Hartmann Motoren;Herr Hartmann;Probeheim;0000 262728;hartmann@hartmann-motoren.example.com;Antriebe;30.01.2024;37.450,00;B;
Krüger Gummiwaren;Frau Krüger;Gummidorf;0000 282930;FEHLT;Dichtungen;12.12.2023;4.800,00;C;E-Mail FEHLT
Wolf Messtechnik;Herr Dr. Wolf;Musterhausen;0000 303132;wolf@wolf-messtechnik.example.com;Messtechnik;FEHLT;16.000,00;A;Letzte Bestellung nur als April 2024 angegeben - Bewertung von 'a' zu 'A' korrigiert
Braun Transporte;Herr Braun;Beispielstadt;0000 323334;braun@braun-transporte.example.com;Spedition;03.02.2024;11.300,00;B;Datum 03/02/2024 als 03.02.2024 gelesen - bitte prüfen, auch 02.03.2024 möglich
Koch Elektronik;Frau Koch;Neustadt a. d. Probe;0000 343536;koch@koch-elektronik.example.com;Elektronik;14.02.2024;FEHLT;B;Jahresumsatz FEHLT
Schäfer Schweißtechnik;Herr Schäfer;Fiktivhausen;0000 363738;schaefer@schaefer-schweiss.example.com;Schweißzubehör;19.03.2024;8.900,00;B;Bewertung von 'b' zu 'B' korrigiert
```

### Sonnet

#### Nutzer 1

Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.

#### Assistent 1

**1. Anzahl Zeilen**
Die Liste hat **27 Datenzeilen** ohne Kopfzeile. Die Kopfzeile hat 9 Spalten: Lieferant, Ansprechpartner, Ort, Telefon, E-Mail, Warengruppe, Letzte Bestellung, Jahresumsatz EUR, Bewertung.

**2. Probleme**

- **Datumsformate in "Letzte Bestellung"** sind uneinheitlich:
  - TT.MM.JJJJ, z. B. 12.03.2024
  - ISO, z. B. 2024-02-28
  - Kurzform, z. B. 5.1.24 und 7.4.2024
  - Schrägstrich, z. B. 15/01/2024 und 03/02/2024
  - nur Monat und Jahr: "März 2024", "Dez. 2023", "April 2024"
  - Bei 03/02/2024 ist unklar, ob es der 3. Februar oder der 2. März ist.
- **Jahresumsatz** steht in vielen Formaten:
  - mit und ohne Tausenderpunkt: 48.500,00 / 48500 / 9800
  - mit Leerzeichen: "31 200 €"
  - mit Währung: "€" oder "EUR"
  - mit Dezimalstellen unterschiedlicher Länge: 22750,5 / 22.750,50 / 12300,00 / 12.300
  - Die Spalte heißt schon "EUR", daher sind die Währungszusätze überflüssig.
- **Firmennamen** sind uneinheitlich: "Müller" und "Mueller", "Schmidt & Söhne" und "Schmidt und Söhne", "Elektro Krause" und "ELEKTRO KRAUSE GmbH", "Weber Kunststofftechnik" und "Weber Kunststoff-Technik GmbH". Rechtsformen (GmbH) fehlen teils.
- **Ortsnamen** sind uneinheitlich: musterhausen / MUSTERHAUSEN / Musterhausen, fiktivhausen / Fiktivhausen, "Neustadt a. d. Probe" / "Neustadt a.d. Probe" / "Neustadt an der Probe" / "neustadt a. d. probe".
- **Ansprechpartner** sind uneinheitlich: "Herr K. Brandt" und "K. Brandt", "Frau Lea Schmidt" und "Lea Schmidt", "Hr. Krause" und "Herr Krause", "Frau Dr. Weber" und "Dr. Weber".
- **Telefonnummern** haben unterschiedliche Formate: "0000 111201" und "0000-111201".
- **Warengruppen** sind uneinheitlich: "Schrauben/Normteile" und "Normteile", "Elektrokomponenten" und "Elektro", "Kunststoffteile" und "Kunststoff". Außerdem sind "Elektrokomponenten" und "Elektronik" ähnlich.
- **Bewertung** hat Kleinbuchstaben ("a", "b" statt "A", "B").
- **Fehlende Werte:**
  - Ansprechpartner: Lackierwerk Ost, Schwarz Gießerei
  - E-Mail: Hoffmann Logistik, Krüger Gummiwaren
  - Telefon: Becker Werkzeugbau
  - Bewertung: Bauer Präzisionsteile, Keller Dichtungstechnik
  - Letzte Bestellung: Keller Dichtungstechnik
  - Jahresumsatz: Koch Elektronik (leer), Richter Glas & Optik ("n/a")
- **Dubletten:** siehe Punkt 3.

**3. Mögliche Dubletten**

| Zeilen | Firma | Begründung |
|---|---|---|
| 2 und 8 | Müller Stahlhandel GmbH / Mueller Stahlhandel | Gleiche E-Mail (brandt@stahl-mueller...), gleiche Telefonnummer (nur anderes Format), gleicher Ort, gleiches Datum (12.03.2024), gleicher Umsatz (48.500), gleiche Bewertung. Sehr sicher. |
| 3 und 11 | Schmidt & Söhne KG / Schmidt und Söhne KG | Gleiche Telefonnummer und E-Mail, gleicher Ort, gleiches Datum (28.02.2024), gleicher Umsatz (12.300), gleiche Bewertung. Widerspruch bei der Warengruppe ("Schrauben/Normteile" gegenüber "Normteile"). |
| 4 und 15 | Elektro Krause / ELEKTRO KRAUSE GmbH | Gleiche Telefonnummer und E-Mail, gleiches Datum (5.1.24 = 05.01.2024), gleicher Umsatz (31.200), gleiche Bewertung. Widerspruch bei der Warengruppe ("Elektrokomponenten" gegenüber "Elektro") und bei der Schreibweise des Orts. |
| 5 und 19 | Weber Kunststofftechnik / Weber Kunststoff-Technik GmbH | Gleiche Telefonnummer und E-Mail, gleicher Ort, gleicher Umsatz (22.750,50), gleiche Bewertung. Datum "März 2024" gegenüber 2024-03-01 passt zusammen. Warengruppe "Kunststoffteile" gegenüber "Kunststoff". |

Ähnlich, aber **keine** Dubletten: Fischer Kabelkonfektion (Zeile 12) ist wie Elektro Krause in "Neustadt a. d. Probe" und liefert Elektrokomponenten, hat aber andere Kontaktdaten und andere Zahlen. Hoffmann Logistik und Braun Transporte sind beide Spedition, aber verschiedene Firmen.

Wenn alle vier Paare Dubletten sind, bleiben **23 eindeutige Lieferanten** übrig.

---

#### Nutzer 2

Bereinige jetzt die Liste nach diesen Regeln:
- Datumsformat überall TT.MM.JJJJ
- Firmennamen einheitlich schreiben (gleiche Firma = gleiche Schreibweise)
- Dubletten zusammenführen; wenn sich Angaben widersprechen, beide Werte behalten und markieren
- Fehlende Werte NICHT erfinden, sondern als "FEHLT" kennzeichnen
- Neue Spalte "Hinweis" für alles, was ich manuell prüfen sollte

Gib das Ergebnis als Tabelle aus. Nenne danach: Anzahl Zeilen vorher, Anzahl Zeilen nachher, und welche Zeilen zusammengeführt wurden.

#### Assistent 2

| # | Lieferant | Ansprechpartner | Ort | Telefon | E-Mail | Warengruppe | Letzte Bestellung | Jahresumsatz EUR | Bewertung | Hinweis |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Müller Stahlhandel GmbH | Herr K. Brandt | Beispielstadt | 0000 111201 | brandt@stahl-mueller.example.com | Stahl | 12.03.2024 | 48.500,00 | A | Zusammengeführt aus Zeile 2 und 8. Schreibweise "Mueller" zu "Müller" vereinheitlicht. |
| 2 | Schmidt & Söhne KG | Frau Lea Schmidt | Musterhausen | 0000 222301 | l.schmidt@schmidt-soehne.example.com | Schrauben/Normteile / Normteile | 28.02.2024 | 12.300,00 | B | Zusammengeführt aus Zeile 3 und 11. **Widerspruch Warengruppe**, bitte entscheiden. Ort "musterhausen" korrigiert. |
| 3 | Elektro Krause GmbH | Herr Krause | Neustadt a. d. Probe | 0000 333401 | info@elektro-krause.example.com | Elektrokomponenten / Elektro | 05.01.2024 | 31.200,00 | A | Zusammengeführt aus Zeile 4 und 15. **Widerspruch Warengruppe**. "GmbH" steht nur in Zeile 15, bitte Rechtsform prüfen. |
| 4 | Weber Kunststofftechnik GmbH | Frau Dr. Weber | Fiktivhausen | 0000 444501 | weber@weber-kunststoff.example.com | Kunststoffteile / Kunststoff | 01.03.2024 | 22.750,50 | B | Zusammengeführt aus Zeile 5 und 19. **Widerspruch Warengruppe**. Datum: Zeile 5 hatte nur "März 2024", der Tag 01 stammt aus Zeile 19, bitte prüfen. Rechtsform GmbH nur in Zeile 19. |
| 5 | Lackierwerk Ost GmbH | FEHLT | Beispielstadt-Ost | 0000 555601 | kontakt@lackierwerk-ost.example.com | Oberflächen | 14.11.2023 | 9.800,00 | C | Ansprechpartner fehlt. |
| 6 | Hoffmann Logistik | Herr Tim Hoffmann | Musterhausen | 0000 666701 | FEHLT | Spedition | 01.04.2024 | 18.400,00 | A | E-Mail fehlt. Ort von "MUSTERHAUSEN" korrigiert. |
| 7 | Bauer Präzisionsteile | Herr S. Bauer | Probeheim | 0000 777801 | s.bauer@bauer-praezision.example.com | Drehteile | 20.02.2024 | 27.100,00 | FEHLT | Bewertung fehlt. |
| 8 | Zimmermann Verpackung | Frau Nina Zimmermann | Musterhausen | 0000 888901 | n.zimmermann@zv-verpackung.example.com | Verpackung | 15.01.2024 | 6.250,00 | B | Datum aus 15/01/2024 umgewandelt. |
| 9 | Fischer Kabelkonfektion | Herr Jan Fischer | Neustadt a. d. Probe | 0000 999001 | fischer@kabel-fischer.example.com | Elektrokomponenten | 03.03.2024 | 14.900,00 | A | |
| 10 | Becker Werkzeugbau | Frau Becker | Fiktivhausen | FEHLT | info@becker-werkzeug.example.com | Werkzeuge | FEHLT | 41.000,00 | B | Telefon fehlt. Datum war nur "Dez. 2023", der Tag fehlt. Ort korrigiert. |
| 11 | Schulz Industriebedarf | Herr Schulz | Beispielstadt | 0000 121314 | schulz@schulz-ib.example.com | Verbrauchsmaterial | 08.04.2024 | 3.150,75 | C | |
| 12 | Wagner Hydraulik | Frau Eva Wagner | Probeheim | 0000 141516 | e.wagner@wagner-hydraulik.example.com | Hydraulik | 22.01.2024 | 19.800,00 | B | |
| 13 | Keller Dichtungstechnik | Herr Keller | Musterhausen | 0000 161718 | keller@dichtung-keller.example.com | Dichtungen | FEHLT | 7.400,00 | FEHLT | Datum und Bewertung fehlen. |
| 14 | Richter Glas & Optik | Frau Richter | Beispielstadt | 0000 181920 | richter@richter-optik.example.com | Optik | 09.02.2024 | FEHLT | B | Umsatz war "n/a". |
| 15 | Neumann Sensorik | Herr Paul Neumann | Neustadt a. d. Probe | 0000 202122 | p.neumann@neumann-sensorik.example.com | Sensoren | 18.03.2024 | 55.600,00 | A | Ort korrigiert. |
| 16 | Schwarz Gießerei | FEHLT | Gießdorf | 0000 222324 | info@giesserei-schwarz.example.com | Gussteile | 30.10.2023 | 63.200,00 | C | Ansprechpartner fehlt. |
| 17 | Lange Büroservice | Frau Lange | Beispielstadt | 0000 242526 | lange@buero-lange.example.com | Büromaterial | 07.04.2024 | 1.200,00 | A | Datum aus 7.4.2024 umgewandelt. |
| 18 | Hartmann Motoren | Herr Hartmann | Probeheim | 0000 262728 | hartmann@hartmann-motoren.example.com | Antriebe | 30.01.2024 | 37.450,00 | B | |
| 19 | Krüger Gummiwaren | Frau Krüger | Gummidorf | 0000 282930 | FEHLT | Dichtungen | 12.12.2023 | 4.800,00 | C | E-Mail fehlt. |
| 20 | Wolf Messtechnik | Herr Dr. Wolf | Musterhausen | 0000 303132 | wolf@wolf-messtechnik.example.com | Messtechnik | FEHLT | 16.000,00 | A | Datum war nur "April 2024", der Tag fehlt. Bewertung "a" zu "A". |
| 21 | Braun Transporte | Herr Braun | Beispielstadt | 0000 323334 | braun@braun-transporte.example.com | Spedition | 03.02.2024 | 11.300,00 | B | **Datum prüfen.** 03/02/2024 kann 3. Februar oder 2. März heißen. Ich habe TT/MM angenommen, wie bei 15/01/2024. |
| 22 | Koch Elektronik | Frau Koch | Neustadt a. d. Probe | 0000 343536 | koch@koch-elektronik.example.com | Elektronik | 14.02.2024 | FEHLT | B | Umsatz fehlt. |
| 23 | Schäfer Schweißtechnik | Herr Schäfer | Fiktivhausen | 0000 363738 | schaefer@schaefer-schweiss.example.com | Schweißzubehör | 19.03.2024 | 8.900,00 | B | Bewertung "b" zu "B". |

**Zusammenfassung**
- Zeilen vorher: **27**
- Zeilen nachher: **23**
- Zusammengeführt wurden (Zeilennummern der Originaldatei ohne Kopfzeile, die Zählung beginnt bei der ersten Datenzeile):
  - Müller Stahlhandel (Zeile 1 und 7)
  - Schmidt & Söhne (Zeile 2 und 10)
  - Elektro Krause (Zeile 3 und 14)
  - Weber Kunststofftechnik (Zeile 4 und 18)

Weitere Hinweise:
- Bei widersprüchlichen Warengruppen habe ich beide Werte mit " / " getrennt behalten.
- Rechtsformen (GmbH) habe ich nur dort ergänzt, wo sie in einer der doppelten Zeilen stand. Bitte prüfen.
- Umsätze sind einheitlich als Zahl mit Tausenderpunkt und zwei Dezimalstellen geschrieben, ohne Währungszeichen.
- Bei Datumsangaben nur mit Monat habe ich keinen Tag erfunden, sondern "FEHLT" eingetragen.

---

#### Nutzer 3

Gib mir die bereinigte Liste noch einmal als CSV mit Semikolon als Trennzeichen, damit ich sie in Excel öffnen kann.

#### Assistent 3

```csv
Lieferant;Ansprechpartner;Ort;Telefon;E-Mail;Warengruppe;Letzte Bestellung;Jahresumsatz EUR;Bewertung;Hinweis
Müller Stahlhandel GmbH;Herr K. Brandt;Beispielstadt;0000 111201;brandt@stahl-mueller.example.com;Stahl;12.03.2024;48.500,00;A;Zusammengeführt aus Zeile 2 und 8. Schreibweise Mueller zu Müller vereinheitlicht.
Schmidt & Söhne KG;Frau Lea Schmidt;Musterhausen;0000 222301;l.schmidt@schmidt-soehne.example.com;Schrauben/Normteile / Normteile;28.02.2024;12.300,00;B;Zusammengeführt aus Zeile 3 und 11. Widerspruch Warengruppe bitte entscheiden.
Elektro Krause GmbH;Herr Krause;Neustadt a. d. Probe;0000 333401;info@elektro-krause.example.com;Elektrokomponenten / Elektro;05.01.2024;31.200,00;A;Zusammengeführt aus Zeile 4 und 15. Widerspruch Warengruppe. GmbH nur in Zeile 15 bitte Rechtsform prüfen.
Weber Kunststofftechnik GmbH;Frau Dr. Weber;Fiktivhausen;0000 444501;weber@weber-kunststoff.example.com;Kunststoffteile / Kunststoff;01.03.2024;22.750,50;B;Zusammengeführt aus Zeile 5 und 19. Widerspruch Warengruppe. Tag 01 nur aus Zeile 19 (Zeile 5 hatte nur März 2024) bitte prüfen.
Lackierwerk Ost GmbH;FEHLT;Beispielstadt-Ost;0000 555601;kontakt@lackierwerk-ost.example.com;Oberflächen;14.11.2023;9.800,00;C;Ansprechpartner fehlt.
Hoffmann Logistik;Herr Tim Hoffmann;Musterhausen;0000 666701;FEHLT;Spedition;01.04.2024;18.400,00;A;E-Mail fehlt.
Bauer Präzisionsteile;Herr S. Bauer;Probeheim;0000 777801;s.bauer@bauer-praezision.example.com;Drehteile;20.02.2024;27.100,00;FEHLT;Bewertung fehlt.
Zimmermann Verpackung;Frau Nina Zimmermann;Musterhausen;0000 888901;n.zimmermann@zv-verpackung.example.com;Verpackung;15.01.2024;6.250,00;B;Datum aus 15/01/2024 umgewandelt.
Fischer Kabelkonfektion;Herr Jan Fischer;Neustadt a. d. Probe;0000 999001;fischer@kabel-fischer.example.com;Elektrokomponenten;03.03.2024;14.900,00;A;
Becker Werkzeugbau;Frau Becker;Fiktivhausen;FEHLT;info@becker-werkzeug.example.com;Werkzeuge;FEHLT;41.000,00;B;Telefon fehlt. Datum war nur Dez. 2023 Tag fehlt.
Schulz Industriebedarf;Herr Schulz;Beispielstadt;0000 121314;schulz@schulz-ib.example.com;Verbrauchsmaterial;08.04.2024;3.150,75;C;
Wagner Hydraulik;Frau Eva Wagner;Probeheim;0000 141516;e.wagner@wagner-hydraulik.example.com;Hydraulik;22.01.2024;19.800,00;B;
Keller Dichtungstechnik;Herr Keller;Musterhausen;0000 161718;keller@dichtung-keller.example.com;Dichtungen;FEHLT;7.400,00;FEHLT;Datum und Bewertung fehlen.
Richter Glas & Optik;Frau Richter;Beispielstadt;0000 181920;richter@richter-optik.example.com;Optik;09.02.2024;FEHLT;B;Umsatz war n/a.
Neumann Sensorik;Herr Paul Neumann;Neustadt a. d. Probe;0000 202122;p.neumann@neumann-sensorik.example.com;Sensoren;18.03.2024;55.600,00;A;
Schwarz Gießerei;FEHLT;Gießdorf;0000 222324;info@giesserei-schwarz.example.com;Gussteile;30.10.2023;63.200,00;C;Ansprechpartner fehlt.
Lange Büroservice;Frau Lange;Beispielstadt;0000 242526;lange@buero-lange.example.com;Büromaterial;07.04.2024;1.200,00;A;
Hartmann Motoren;Herr Hartmann;Probeheim;0000 262728;hartmann@hartmann-motoren.example.com;Antriebe;30.01.2024;37.450,00;B;
Krüger Gummiwaren;Frau Krüger;Gummidorf;0000 282930;FEHLT;Dichtungen;12.12.2023;4.800,00;C;E-Mail fehlt.
Wolf Messtechnik;Herr Dr. Wolf;Musterhausen;0000 303132;wolf@wolf-messtechnik.example.com;Messtechnik;FEHLT;16.000,00;A;Datum war nur April 2024 Tag fehlt.
Braun Transporte;Herr Braun;Beispielstadt;0000 323334;braun@braun-transporte.example.com;Spedition;03.02.2024;11.300,00;B;Datum prüfen: 03/02/2024 kann 3. Februar oder 2. März sein. TT/MM angenommen.
Koch Elektronik;Frau Koch;Neustadt a. d. Probe;0000 343536;koch@koch-elektronik.example.com;Elektronik;14.02.2024;FEHLT;B;Umsatz fehlt.
Schäfer Schweißtechnik;Herr Schäfer;Fiktivhausen;0000 363738;schaefer@schaefer-schweiss.example.com;Schweißzubehör;19.03.2024;8.900,00;B;
```

Hinweise zum Öffnen in Excel:
- Speichere den Text in einer Datei mit der Endung **.csv**, Kodierung **UTF-8 mit BOM**, damit Umlaute richtig angezeigt werden.
- In der deutschen Excel-Version öffnet ein Doppelklick die Datei mit Semikolon als Trennzeichen.
- Umsätze wie 48.500,00 werden als Zahlen erkannt. Die Telefonnummern können führende Nullen verlieren. Importiere die Spalte dann über "Daten, Aus Text/CSV" als Text.
- Beim Zusammenführen und Bereinigen habe ich nichts erfunden. Alle Stellen mit "FEHLT" und die Hinweise solltest du manuell prüfen.

### Opus

#### Nutzer 1

Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.

#### Assistent 1

Ich habe die Liste nur gelesen und nichts geändert. Die Zeilennummern unten zählen die Datenzeilen, also ohne Kopfzeile.

**1. Anzahl Zeilen**
Die Liste hat **27 Datenzeilen** und 9 Spalten (Lieferant, Ansprechpartner, Ort, Telefon, E-Mail, Warengruppe, Letzte Bestellung, Jahresumsatz EUR, Bewertung).

**2. Gefundene Probleme**

*Datumsformate (Spalte „Letzte Bestellung“)* – Die Daten stehen in mindestens sechs verschiedenen Formaten:
- TT.MM.JJJJ, z. B. 12.03.2024
- ISO-Format JJJJ-MM-TT, z. B. 2024-02-28 (Zeilen 2, 7, 13, 18, 22, 26)
- Kurzform ohne führende Null oder mit zweistelligem Jahr: 5.1.24 (Zeile 3), 7.4.2024 (Zeile 21)
- Schrägstriche: 15/01/2024 (Zeile 9) und 03/02/2024 (Zeile 25). Die zweite Angabe ist **mehrdeutig**: 3. Februar oder 2. März?
- Nur Monat und Jahr, ohne Tag: „März 2024“ (Zeile 4), „Dez. 2023“ (Zeile 12), „April 2024“ (Zeile 24)
- Leer: Zeile 16 (Keller Dichtungstechnik)

*Schreibweisen*
- Firmennamen: dieselbe Firma steht in verschiedenen Schreibweisen in der Liste (Müller/Mueller, „&“/„und“, GROSSBUCHSTABEN, mit und ohne Bindestrich, mit und ohne Rechtsform GmbH). Details siehe Punkt 3.
- Orte: „Musterhausen“, „musterhausen“, „MUSTERHAUSEN“; „Neustadt a. d. Probe“, „Neustadt a.d. Probe“, „Neustadt an der Probe“, „neustadt a. d. probe“; „fiktivhausen“ kleingeschrieben.
- Telefon: „0000 111201“ und „0000-111201“ (Leerzeichen bzw. Bindestrich).
- Ansprechpartner: uneinheitlich mit „Herr/Frau“, „Hr.“ oder ganz ohne Anrede.
- Warengruppen: ähnliche Begriffe für dasselbe, z. B. „Elektro“, „Elektrokomponenten“, „Elektronik“; „Kunststoff“ und „Kunststoffteile“; „Normteile“ und „Schrauben/Normteile“.
- Jahresumsatz: viele Formate: 48.500,00 / 48500 / 12300,00 / 22750,5 / „31 200 €“ / „18.400,00 €“ / „41.000 EUR“ / „11.300 EUR“. Excel erkennt viele davon nicht als Zahl.
- Bewertung: neben A/B/C auch kleingeschrieben „a“ (Zeile 24) und „b“ (Zeile 27).

*Fehlende oder ungültige Werte*
- Ansprechpartner fehlt: Zeile 5 (Lackierwerk Ost GmbH), Zeile 20 (Schwarz Gießerei)
- Telefon fehlt: Zeile 12 (Becker Werkzeugbau)
- E-Mail fehlt: Zeile 6 (Hoffmann Logistik), Zeile 23 (Krüger Gummiwaren)
- Datum fehlt: Zeile 16 (Keller Dichtungstechnik)
- Jahresumsatz fehlt: Zeile 26 (Koch Elektronik, leer), Zeile 17 (Richter Glas & Optik, „n/a“)
- Bewertung fehlt: Zeile 8 (Bauer Präzisionsteile), Zeile 16 (Keller Dichtungstechnik)

**3. Mögliche Dubletten**

| # | Zeilen | Einträge | Begründung |
|---|---|---|---|
| 1 | 1 und 7 | „Müller Stahlhandel GmbH“ / „Mueller Stahlhandel“ | Telefonnummer, E-Mail, Ort, Ansprechpartner (K. Brandt), Warengruppe, Datum (12.03.2024), Umsatz (48.500) und Bewertung stimmen überein. Nur die Schreibweise unterscheidet sich. **Sehr sicher.** |
| 2 | 2 und 10 | „Schmidt & Söhne KG“ / „Schmidt und Söhne KG“ | Gleiche Telefonnummer, gleiche E-Mail, gleiche Ansprechpartnerin (Lea Schmidt), gleicher Ort, gleiches Datum (28.02.2024), gleicher Umsatz, gleiche Bewertung. Unterschied: Warengruppe „Schrauben/Normteile“ gegenüber „Normteile“. **Sehr sicher.** |
| 3 | 3 und 14 | „Elektro Krause“ / „ELEKTRO KRAUSE GmbH“ | Gleiche Telefonnummer, gleiche E-Mail, Herr Krause, gleicher Ort (anders geschrieben), Datum 5.1.24 = 05.01.2024, Umsatz 31.200, Bewertung A. Unterschied: Warengruppe „Elektrokomponenten“ gegenüber „Elektro“, Rechtsform nur einmal angegeben. **Sehr sicher.** |
| 4 | 4 und 18 | „Weber Kunststofftechnik“ / „Weber Kunststoff-Technik GmbH“ | Gleiche Telefonnummer, gleiche E-Mail, Dr. Weber, Fiktivhausen, Umsatz 22.750,50, Bewertung B. Datum „März 2024“ passt zu 2024-03-01. Unterschied: Warengruppe „Kunststoffteile“ gegenüber „Kunststoff“. **Sehr sicher.** |

Keine Dubletten, obwohl sie ähnlich aussehen:
- Fischer Kabelkonfektion und Koch Elektronik sitzen wie Elektro Krause in Neustadt und liefern Ähnliches. Telefon, E-Mail und Ansprechpartner sind aber verschieden, also sind es eigene Lieferanten.
- Hoffmann Logistik und Braun Transporte sind beide Speditionen, aber verschiedene Firmen.
- Keller Dichtungstechnik und Krüger Gummiwaren haben beide die Warengruppe „Dichtungen“, sind aber verschiedene Firmen.

Wenn die 4 Dubletten zusammengeführt werden, bleiben **23 Lieferanten**.

#### Nutzer 2

Bereinige jetzt die Liste nach diesen Regeln:
- Datumsformat überall TT.MM.JJJJ
- Firmennamen einheitlich schreiben (gleiche Firma = gleiche Schreibweise)
- Dubletten zusammenführen; wenn sich Angaben widersprechen, beide Werte behalten und markieren
- Fehlende Werte NICHT erfinden, sondern als "FEHLT" kennzeichnen
- Neue Spalte "Hinweis" für alles, was ich manuell prüfen sollte

Gib das Ergebnis als Tabelle aus. Nenne danach: Anzahl Zeilen vorher, Anzahl Zeilen nachher, und welche Zeilen zusammengeführt wurden.

#### Assistent 2

Hier ist die bereinigte Liste. Zusätzlich zu Ihren Regeln habe ich einige rein formale Dinge vereinheitlicht: die Schreibweise der Orte, Telefonnummern im Format „0000 123456“, Umsätze im Format 12.345,67 ohne Währungszeichen (die Spalte heißt ja schon „EUR“) und Bewertungen in Großbuchstaben. Inhalte habe ich dabei nicht verändert.

Widersprüche stehen so in der Zelle: **„Wert 1 | Wert 2 [WIDERSPRUCH]“**.

| Nr. | Lieferant | Ansprechpartner | Ort | Telefon | E-Mail | Warengruppe | Letzte Bestellung | Jahresumsatz EUR | Bewertung | Hinweis |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Müller Stahlhandel GmbH | Herr K. Brandt | Beispielstadt | 0000 111201 | brandt@stahl-mueller.example.com | Stahl | 12.03.2024 | 48.500,00 | A | Zusammengeführt aus Zeilen 1 + 7 („Mueller Stahlhandel“). Alle Angaben gleich. |
| 2 | Schmidt & Söhne KG | Frau Lea Schmidt | Musterhausen | 0000 222301 | l.schmidt@schmidt-soehne.example.com | Schrauben/Normteile \| Normteile [WIDERSPRUCH] | 28.02.2024 | 12.300,00 | B | Zusammengeführt aus Zeilen 2 + 10 („Schmidt und Söhne KG“). Warengruppe festlegen. |
| 3 | Elektro Krause GmbH | Herr Krause | Neustadt a. d. Probe | 0000 333401 | info@elektro-krause.example.com | Elektrokomponenten \| Elektro [WIDERSPRUCH] | 05.01.2024 | 31.200,00 | A | Zusammengeführt aus Zeilen 3 + 14 („ELEKTRO KRAUSE GmbH“). Warengruppe festlegen. Rechtsform „GmbH“ steht nur in einem Eintrag, bitte prüfen. Vorname des Ansprechpartners fehlt. |
| 4 | Weber Kunststofftechnik GmbH | Frau Dr. Weber | Fiktivhausen | 0000 444501 | weber@weber-kunststoff.example.com | Kunststoffteile \| Kunststoff [WIDERSPRUCH] | 01.03.2024 | 22.750,50 | B | Zusammengeführt aus Zeilen 4 + 18 („Weber Kunststoff-Technik GmbH“). Datum aus Zeile 18 übernommen, passt zu „März 2024“. Warengruppe festlegen. Offizielle Schreibweise des Namens prüfen (mit oder ohne Bindestrich). |
| 5 | Lackierwerk Ost GmbH | FEHLT | Beispielstadt-Ost | 0000 555601 | kontakt@lackierwerk-ost.example.com | Oberflächen | 14.11.2023 | 9.800,00 | C | Ansprechpartner ergänzen. |
| 6 | Hoffmann Logistik | Herr Tim Hoffmann | Musterhausen | 0000 666701 | FEHLT | Spedition | 01.04.2024 | 18.400,00 | A | E-Mail ergänzen. |
| 7 | Bauer Präzisionsteile | Herr S. Bauer | Probeheim | 0000 777801 | s.bauer@bauer-praezision.example.com | Drehteile | 20.02.2024 | 27.100,00 | FEHLT | Bewertung ergänzen. |
| 8 | Zimmermann Verpackung | Frau Nina Zimmermann | Musterhausen | 0000 888901 | n.zimmermann@zv-verpackung.example.com | Verpackung | 15.01.2024 | 6.250,00 | B | Datum war 15/01/2024 (eindeutig). |
| 9 | Fischer Kabelkonfektion | Herr Jan Fischer | Neustadt a. d. Probe | 0000 999001 | fischer@kabel-fischer.example.com | Elektrokomponenten | 03.03.2024 | 14.900,00 | A | |
| 10 | Becker Werkzeugbau | Frau Becker | Fiktivhausen | FEHLT | info@becker-werkzeug.example.com | Werkzeuge | FEHLT (nur Monat bekannt: 12.2023) | 41.000,00 | B | Telefon ergänzen. Original „Dez. 2023“, Tag unbekannt. |
| 11 | Schulz Industriebedarf | Herr Schulz | Beispielstadt | 0000 121314 | schulz@schulz-ib.example.com | Verbrauchsmaterial | 08.04.2024 | 3.150,75 | C | |
| 12 | Wagner Hydraulik | Frau Eva Wagner | Probeheim | 0000 141516 | e.wagner@wagner-hydraulik.example.com | Hydraulik | 22.01.2024 | 19.800,00 | B | |
| 13 | Keller Dichtungstechnik | Herr Keller | Musterhausen | 0000 161718 | keller@dichtung-keller.example.com | Dichtungen | FEHLT | 7.400,00 | FEHLT | Datum und Bewertung ergänzen. |
| 14 | Richter Glas & Optik | Frau Richter | Beispielstadt | 0000 181920 | richter@richter-optik.example.com | Optik | 09.02.2024 | FEHLT | B | Umsatz war „n/a“, bitte ergänzen. |
| 15 | Neumann Sensorik | Herr Paul Neumann | Neustadt a. d. Probe | 0000 202122 | p.neumann@neumann-sensorik.example.com | Sensoren | 18.03.2024 | 55.600,00 | A | |
| 16 | Schwarz Gießerei | FEHLT | Gießdorf | 0000 222324 | info@giesserei-schwarz.example.com | Gussteile | 30.10.2023 | 63.200,00 | C | Ansprechpartner ergänzen. |
| 17 | Lange Büroservice | Frau Lange | Beispielstadt | 0000 242526 | lange@buero-lange.example.com | Büromaterial | 07.04.2024 | 1.200,00 | A | |
| 18 | Hartmann Motoren | Herr Hartmann | Probeheim | 0000 262728 | hartmann@hartmann-motoren.example.com | Antriebe | 30.01.2024 | 37.450,00 | B | |
| 19 | Krüger Gummiwaren | Frau Krüger | Gummidorf | 0000 282930 | FEHLT | Dichtungen | 12.12.2023 | 4.800,00 | C | E-Mail ergänzen. |
| 20 | Wolf Messtechnik | Herr Dr. Wolf | Musterhausen | 0000 303132 | wolf@wolf-messtechnik.example.com | Messtechnik | FEHLT (nur Monat bekannt: 04.2024) | 16.000,00 | A | Original „April 2024“, Tag unbekannt. Bewertung war kleingeschrieben „a“. |
| 21 | Braun Transporte | Herr Braun | Beispielstadt | 0000 323334 | braun@braun-transporte.example.com | Spedition | 03.02.2024 | 11.300,00 | B | Original „03/02/2024“ ist mehrdeutig. Als 3. Februar gelesen, könnte auch der 2. März sein. Bitte prüfen. |
| 22 | Koch Elektronik | Frau Koch | Neustadt a. d. Probe | 0000 343536 | koch@koch-elektronik.example.com | Elektronik | 14.02.2024 | FEHLT | B | Umsatz ergänzen. |
| 23 | Schäfer Schweißtechnik | Herr Schäfer | Fiktivhausen | 0000 363738 | schaefer@schaefer-schweiss.example.com | Schweißzubehör | 19.03.2024 | 8.900,00 | B | Bewertung war kleingeschrieben „b“. |

**Zusammenfassung**
- **Zeilen vorher:** 27 (ohne Kopfzeile)
- **Zeilen nachher:** 23 (ohne Kopfzeile)
- **Zusammengeführt (Datenzeilen der Originalliste, ohne Kopfzeile gezählt):**
  1. Zeile 1 „Müller Stahlhandel GmbH“ + Zeile 7 „Mueller Stahlhandel“ → Müller Stahlhandel GmbH
  2. Zeile 2 „Schmidt & Söhne KG“ + Zeile 10 „Schmidt und Söhne KG“ → Schmidt & Söhne KG
  3. Zeile 3 „Elektro Krause“ + Zeile 14 „ELEKTRO KRAUSE GmbH“ → Elektro Krause GmbH
  4. Zeile 4 „Weber Kunststofftechnik“ + Zeile 18 „Weber Kunststoff-Technik GmbH“ → Weber Kunststofftechnik GmbH

**Bitte vor allem manuell prüfen:**
- Warengruppen mit Widerspruch: Nr. 2, 3 und 4
- Mehrdeutiges Datum: Nr. 21 (Braun Transporte)
- Datum nur als Monat bekannt: Nr. 10 und 20. Den Tag habe ich bewusst nicht erfunden.
- Die Warengruppen sind insgesamt noch nicht vereinheitlicht (z. B. Elektrokomponenten, Elektro, Elektronik). Wenn Sie möchten, kann ich einen Vorschlag für feste Warengruppen machen.

#### Nutzer 3

Gib mir die bereinigte Liste noch einmal als CSV mit Semikolon als Trennzeichen, damit ich sie in Excel öffnen kann.

#### Assistent 3

Hier ist die bereinigte Liste als CSV. Kopieren Sie den Block in einen Texteditor, speichern Sie ihn als `lieferantenliste_bereinigt.csv` mit Kodierung **UTF-8** und öffnen Sie ihn dann in Excel. Falls Umlaute falsch angezeigt werden, gehen Sie in Excel über *Daten → Aus Text/CSV*, wählen dort „UTF-8“ und als Trennzeichen „Semikolon“.

```
Lieferant;Ansprechpartner;Ort;Telefon;E-Mail;Warengruppe;Letzte Bestellung;Jahresumsatz EUR;Bewertung;Hinweis
Müller Stahlhandel GmbH;Herr K. Brandt;Beispielstadt;0000 111201;brandt@stahl-mueller.example.com;Stahl;12.03.2024;48.500,00;A;Zusammengeführt aus Zeilen 1 + 7 (Mueller Stahlhandel). Alle Angaben gleich.
Schmidt & Söhne KG;Frau Lea Schmidt;Musterhausen;0000 222301;l.schmidt@schmidt-soehne.example.com;Schrauben/Normteile | Normteile [WIDERSPRUCH];28.02.2024;12.300,00;B;Zusammengeführt aus Zeilen 2 + 10 (Schmidt und Söhne KG). Warengruppe festlegen.
Elektro Krause GmbH;Herr Krause;Neustadt a. d. Probe;0000 333401;info@elektro-krause.example.com;Elektrokomponenten | Elektro [WIDERSPRUCH];05.01.2024;31.200,00;A;Zusammengeführt aus Zeilen 3 + 14 (ELEKTRO KRAUSE GmbH). Warengruppe festlegen. Rechtsform GmbH nur in einem Eintrag - prüfen. Vorname Ansprechpartner fehlt.
Weber Kunststofftechnik GmbH;Frau Dr. Weber;Fiktivhausen;0000 444501;weber@weber-kunststoff.example.com;Kunststoffteile | Kunststoff [WIDERSPRUCH];01.03.2024;22.750,50;B;Zusammengeführt aus Zeilen 4 + 18 (Weber Kunststoff-Technik GmbH). Datum aus Zeile 18 (passt zu März 2024). Warengruppe festlegen. Offizielle Schreibweise prüfen.
Lackierwerk Ost GmbH;FEHLT;Beispielstadt-Ost;0000 555601;kontakt@lackierwerk-ost.example.com;Oberflächen;14.11.2023;9.800,00;C;Ansprechpartner ergänzen.
Hoffmann Logistik;Herr Tim Hoffmann;Musterhausen;0000 666701;FEHLT;Spedition;01.04.2024;18.400,00;A;E-Mail ergänzen.
Bauer Präzisionsteile;Herr S. Bauer;Probeheim;0000 777801;s.bauer@bauer-praezision.example.com;Drehteile;20.02.2024;27.100,00;FEHLT;Bewertung ergänzen.
Zimmermann Verpackung;Frau Nina Zimmermann;Musterhausen;0000 888901;n.zimmermann@zv-verpackung.example.com;Verpackung;15.01.2024;6.250,00;B;Datum war 15/01/2024 (eindeutig).
Fischer Kabelkonfektion;Herr Jan Fischer;Neustadt a. d. Probe;0000 999001;fischer@kabel-fischer.example.com;Elektrokomponenten;03.03.2024;14.900,00;A;
Becker Werkzeugbau;Frau Becker;Fiktivhausen;FEHLT;info@becker-werkzeug.example.com;Werkzeuge;FEHLT (nur Monat bekannt: 12.2023);41.000,00;B;Telefon ergänzen. Original Dez. 2023 - Tag unbekannt.
Schulz Industriebedarf;Herr Schulz;Beispielstadt;0000 121314;schulz@schulz-ib.example.com;Verbrauchsmaterial;08.04.2024;3.150,75;C;
Wagner Hydraulik;Frau Eva Wagner;Probeheim;0000 141516;e.wagner@wagner-hydraulik.example.com;Hydraulik;22.01.2024;19.800,00;B;
Keller Dichtungstechnik;Herr Keller;Musterhausen;0000 161718;keller@dichtung-keller.example.com;Dichtungen;FEHLT;7.400,00;FEHLT;Datum und Bewertung ergänzen.
Richter Glas & Optik;Frau Richter;Beispielstadt;0000 181920;richter@richter-optik.example.com;Optik;09.02.2024;FEHLT;B;Umsatz war n/a - ergänzen.
Neumann Sensorik;Herr Paul Neumann;Neustadt a. d. Probe;0000 202122;p.neumann@neumann-sensorik.example.com;Sensoren;18.03.2024;55.600,00;A;
Schwarz Gießerei;FEHLT;Gießdorf;0000 222324;info@giesserei-schwarz.example.com;Gussteile;30.10.2023;63.200,00;C;Ansprechpartner ergänzen.
Lange Büroservice;Frau Lange;Beispielstadt;0000 242526;lange@buero-lange.example.com;Büromaterial;07.04.2024;1.200,00;A;
Hartmann Motoren;Herr Hartmann;Probeheim;0000 262728;hartmann@hartmann-motoren.example.com;Antriebe;30.01.2024;37.450,00;B;
Krüger Gummiwaren;Frau Krüger;Gummidorf;0000 282930;FEHLT;Dichtungen;12.12.2023;4.800,00;C;E-Mail ergänzen.
Wolf Messtechnik;Herr Dr. Wolf;Musterhausen;0000 303132;wolf@wolf-messtechnik.example.com;Messtechnik;FEHLT (nur Monat bekannt: 04.2024);16.000,00;A;Original April 2024 - Tag unbekannt. Bewertung war kleingeschrieben (a).
Braun Transporte;Herr Braun;Beispielstadt;0000 323334;braun@braun-transporte.example.com;Spedition;03.02.2024;11.300,00;B;Original 03/02/2024 mehrdeutig - als 3. Februar gelesen, evtl. 2. März. Prüfen.
Koch Elektronik;Frau Koch;Neustadt a. d. Probe;0000 343536;koch@koch-elektronik.example.com;Elektronik;14.02.2024;FEHLT;B;Umsatz ergänzen.
Schäfer Schweißtechnik;Herr Schäfer;Fiktivhausen;0000 363738;schaefer@schaefer-schweiss.example.com;Schweißzubehör;19.03.2024;8.900,00;B;Bewertung war kleingeschrieben (b).
```

Hinweise für Excel:
- Die Datei hat 1 Kopfzeile und 23 Datenzeilen.
- In deutschem Excel werden Daten wie 12.03.2024 und Beträge wie 48.500,00 automatisch als Datum bzw. Zahl erkannt. Zellen mit „FEHLT“ bleiben Text. Wenn Sie mit den Spalten rechnen oder sortieren wollen, sollten Sie diese Zellen also vorher filtern.
- Ich kann Ihnen eine Variante ohne Tausenderpunkte (z. B. 48500,00) geben, falls Ihr Excel auf Englisch eingestellt ist.
