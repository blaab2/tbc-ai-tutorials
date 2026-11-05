# Testlauf: Übung 3 / Station D Für Schnelle – Anleitung zur einheitlichen Pflege

**Herkunft:** [Übung 3, Station D, Abschnitt „Für Schnelle“](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#station-d-unordentliche-tabelle-bereinigen), zweiter Punkt: „Lass dir eine kurze **Anleitung** schreiben, wie die Liste künftig einheitlich gepflegt werden soll (Regeln für Schreibweisen, Datumsformat, Pflichtfelder).“ Material: [lieferantenliste_unsortiert.csv](../07_Beispielmaterial/lieferantenliste_unsortiert.csv). Abgleich mit [Trainer-Lösungshinweise, Station D](../06_Uebungen/Trainer-Loesungshinweise.md#station-d-lieferantenliste-bereinigen). Zur Anleitung selbst gibt es dort **keinen eigenen Abschnitt**.

**Testdatum:** Montag, 2. November 2026

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

Ablauf je Modell: neuer Chat, CSV angehängt, zuerst der Basis-Prompt aus dem Übungsblatt (Analyse), danach als zweite Nachricht der Prompt „Schreib mir eine kurze Anleitung, wie die Liste künftig einheitlich gepflegt werden soll: Regeln für Schreibweisen, Datumsformat und Pflichtfelder.“ (aus der Aufgabenbeschreibung abgeleitet, ein wörtlicher Prompt steht nicht im Material). Die Analyse-Antworten wurden mitgeprüft, weil die Anleitung auf ihnen aufbaut.

Nachgeprüft per Python: 27 Datenzeilen; 23 verschiedene Warengruppen-Einträge (vor dem Vereinheitlichen); Bewertungen in der Datei: A, B, C, a, b und leer (**kein D**); leere Zellen: Ansprechpartner (Zeile 6, 21 der Datei), E-Mail (7, 24), Bewertung (9, 17), Telefon (13), Letzte Bestellung (17), Jahresumsatz (27), dazu „n/a“ in Zeile 18.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Analyse: 27 Zeilen, 4 richtige Dubletten-Paare, keine falschen | ja (nennt auch 23 Lieferanten) | ja (23 nicht ausdrücklich genannt) | ja (nennt 23) |
| Analyse: fehlende Werte vollständig und richtig zugeordnet | ja | ja, aber mit sichtbarer Selbstkorrektur bei der Bewertung | ja, als Tabelle |
| Datum TT.MM.JJJJ mit Verbot der anderen Formate | ja | ja | ja (mit führenden Nullen) |
| Umgang mit „nur Monat bekannt“ | trägt den 1. ein + Notiz (Annahme, aber markiert) | klären oder leer lassen, nicht raten | im Bestellsystem nachsehen |
| Firmenname offiziell inkl. Rechtsform, Umlaute, keine Großbuchstaben | ja | ja | ja |
| Regel „&“ / „und“ | „immer und“ – widerspricht „exakt wie im Handelsregister“ | „immer &“ | „wie im offiziellen Namen“ (am saubersten) |
| Orte einheitlich | Regel, keine feste Liste | Regel, keine feste Liste | Regel, keine feste Liste |
| Warengruppen als feste Auswahlliste | ja (5 Beispiele) | ja (19 Gruppen ausgeschrieben) | ja (19 Gruppen + Excel-Datenüberprüfung) |
| Betragsformat (Zahl, ohne €, 48.500,00) | ja | ja | ja (+ Excel-Tipp) |
| Bewertung nur Großbuchstaben | ja (A–C) | ja (A–C) | ja (A–C) |
| Pflichtfelder klar benannt | ja, aber in sich widersprüchlich (s. u.) | ja, Pflicht/Soll getrennt | ja, als Tabelle; zwei fragwürdige Vorbelegungen |
| Platzhalter wie „n/a“ verboten | ja | ja | ja |
| Dublettenprüfung vor Neuanlage | ja (E-Mail, Telefon) + Lieferanten-Nummer | ja (Name, E-Mail, Telefon) | ja (Name, E-Mail, Telefon) |
| Regelmäßige Kontrolle / Verantwortliche Person | quartalsweise | quartalsweise + Person | quartalsweise + Person |
| Kurz (≈ 1 Seite) | ja, am kürzesten | gut 1 Seite | knapp 2 Seiten (längste) |
| Erfundene Fakten über die Daten | keine | keine (Beispielzeile korrekt aus Zeile 3/11) | keine |

**Gesamturteil:** Die Aufgabe funktioniert mit allen drei Modellen. Alle liefern eine brauchbare, verständliche Pflegeanleitung, die die in der Analyse gefundenen Probleme direkt aufgreift. Sachliche Fehler über die Daten gibt es praktisch keine. Die Unterschiede liegen in **Regelqualität** (Widersprüche, stille Festlegungen) und Länge. Sonnet trifft „kurz und konkret“ am besten, Opus ist am gründlichsten, aber länger als „kurz“, Haiku ist knapp, enthält aber zwei Widersprüche.

---

## Gefundene Fehler und Schwächen (mit Beleg)

### Haiku

- **Widerspruch Firmenname:** „Firmenname exakt wie im Handelsregister“ und gleich danach „„&“ oder „und“: … z. B. immer „und““. Steht „&“ im Registernamen (z. B. „Schmidt & Söhne KG“, Zeile 3 der CSV), lassen sich beide Regeln nicht gleichzeitig einhalten.
- **Widerspruch Pflichtfelder:** „Letzte Bestellung“ und „Jahresumsatz EUR“ sind Pflichtfelder, gleichzeitig heißt es „Unbekannt bedeutet leer, mit Vermerk“. Ein neuer Lieferant ohne Bestellung kann so gar nicht korrekt angelegt werden.
- **Tag wird ergänzt:** „Ist nur der Monat bekannt, wird der erste Tag eingetragen und das in einer Notiz vermerkt.“ Das ist genau die Annahme, vor der die Lösungshinweise warnen („Erfindet der KI-Assistent ‚01.03.2024‘, ist das eine Annahme, die markiert sein muss“). Sie ist hier zwar markiert, aber eine Notiz-Spalte gibt es in der Liste nicht.
- **Telefon nicht eindeutig:** „einheitlich im Format `+49 …` oder `0000 111201`“ – zwei Formate sind keine einheitliche Regel.
- **Ungenau:** „Keine Abkürzungen wie „Mueller““ – „Mueller“ ist eine Umschreibung des Umlauts, keine Abkürzung (inhaltlich richtig gemeint).
- Analyse: Bei den Datumsformaten fehlt „April 2024“ (Wolf, Zeile 25), bei den Warengruppen fehlt „Kunststoffteile / Kunststoff“. Bei Schmidt fehlt der Hinweis auf die abweichende Warengruppe. Sonst alles korrekt, Zeilennummern zählen ab Dateizeile 2 (so auch angegeben).

### Sonnet

- **Sichtbare Selbstkorrektur in der Analyse:** „bei Bauer Präzisionsteile, Keller Dichtungstechnik und Koch Elektronik fehlt der Wert (Koch: nur Umsatz leer, Bewertung vorhanden, siehe oben). Korrekt gilt: …“ Das Ergebnis stimmt am Ende (Bewertung fehlt nur in Zeile 9 und 17), wirkt aber unsauber.
- **Übertreibung:** „Eine Zeile ist komplett in Großbuchstaben geschrieben.“ In Zeile 15 ist nur der Firmenname „ELEKTRO KRAUSE GmbH“ großgeschrieben, nicht die Zeile.
- **Stille Festlegung bei Warengruppen:** Die Auswahlliste hat 19 Gruppen. In der Datei stehen 23 Varianten. Neben den drei echten Varianten (Elektro, Kunststoff, Schrauben/Normteile) ist auch **„Elektronik“ (Koch Elektronik, Zeile 27) stillschweigend weggefallen**, also in „Elektrokomponenten“ aufgegangen. Das kann richtig sein, ist aber eine fachliche Entscheidung, die der Einkauf treffen muss.
- Regel „Statt „und“ schreibt man „&““ ist eindeutig, kann aber mit „Offizieller Name“ kollidieren (gleiches Problem wie bei Haiku, nur in die andere Richtung).
- Beispielzeile korrekt aus Zeile 3/11 der CSV zusammengesetzt (Telefon, E-Mail, Datum 28.02.2024, Umsatz 12.300,00, B – alles nachgeprüft).

### Opus

- **Erfundene Vorbelegungen:** „Bewertung … neue Lieferanten zunächst mit „B““ und „Jahresumsatz … bei neuen Lieferanten: 0“. Beides widerspricht der eigenen Regel „Was unbekannt ist, bleibt leer“. Ein vorbelegtes „B“ sieht aus wie eine echte Bewertung.
- **Gleiche stille Festlegung bei Warengruppen** wie Sonnet (19 Gruppen, „Elektronik“ fehlt).
- **Länge:** knapp zwei Seiten, mit Tabelle und Excel-Tipps. Für „kurze Anleitung“ zu lang, inhaltlich aber am vollständigsten.
- Excel-Tipp „Formatieren Sie die Spalte als Datum. Dann wird jedes eingegebene Datum gleich angezeigt.“ stimmt nur für Eingaben, die Excel als Datum erkennt. Ein deutsches Excel wandelt z. B. „März 2024“ eventuell selbst in den 01.03.2024 um – genau die Excel-Falle aus den Lösungshinweisen.
- Analyse: korrekt und am übersichtlichsten (Tabelle der fehlenden Werte). Zeilennummern zählen ab erster Datenzeile wie in den Lösungshinweisen (1/7, 2/10, 3/14, 4/18), das wird auch ausdrücklich gesagt. Erkennt zusätzlich „Beispielstadt-Ost“ als Prüffall.

### Alle drei

- **Keine feste Ortsliste.** Alle geben nur eine Schreibregel für Orte. Die Modelle wählen unterschiedliche Normformen: Haiku und Sonnet „Neustadt an der Probe“, Opus „Neustadt a. d. Probe“. Beides geht, aber es zeigt: Die KI legt etwas fest, was eigentlich die Firma entscheiden muss.
- **Bewertungsskala A–C** wird aus den Daten abgeleitet. Ob es intern auch D gibt, weiß kein Modell, und keines fragt nach. Das Material definiert die Skala nicht.

---

## Lehren für die Auswertung

1. **Gute Stelle, um KI-Stärken zu zeigen:** Aus einer Fehleranalyse Regeln abzuleiten, gelingt allen Modellen gut und schnell. Das ist echter Mehrwert, auch für Leute, die keine Tabellen bereinigen.
2. **Regeln auf Widersprüche lesen lassen:** Teilnehmende sollen ihre Anleitung gegen die eigene Analyse halten. Typische Funde: „Pflichtfeld“ und „darf leer bleiben“ gleichzeitig (Haiku), Vorbelegung „B“ und „0“ (Opus), „&“-Regel gegen „offizieller Name“. Nachfrage-Prompt: „Prüfe deine Anleitung auf Widersprüche zwischen den Regeln.“
3. **Die KI trifft Firmenentscheidungen, ohne zu fragen:** Welche Warengruppen es gibt (Elektronik weg?), welche Ortsschreibweise gilt, welche Bewertungsstufen es gibt. Gute Frage an die Gruppe: „Wer in eurer Firma müsste das eigentlich festlegen?“
4. **Länge steuern:** „Kurz“ wird unterschiedlich ausgelegt (Haiku ½ Seite, Opus fast 2 Seiten). Ergänzung wie „maximal eine Seite“ oder „als Merkblatt mit höchstens 10 Regeln“ hilft.
5. **Umgang mit unvollständigen Daten** (nur Monat bekannt) ist ein schöner Vergleich zwischen den Modellen: raten und markieren (Haiku), leer lassen (Sonnet), nachschlagen (Opus). Brücke zum Prüfschritt „Erfundenes?“.
6. **Weiterführung:** Opus und Haiku bieten Excel-Datenüberprüfung an. Daraus lässt sich gut die dritte „Für Schnelle“-Aufgabe (Bereinigung selbst in Excel) anschließen.

---

## Gesprächsprotokolle

### Modell: Haiku

#### Nutzer 1

Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.

#### Assistent 1

Ich habe die Datei nur gelesen und nichts verändert.

**1. Anzahl Zeilen**
Die Liste hat **27 Datenzeilen** (ohne Kopfzeile, Zeilen 2 bis 28).

**2. Probleme**

- **Datumsformate:** Mindestens sieben Varianten sind im Einsatz:
  - `12.03.2024` (TT.MM.JJJJ)
  - `2024-02-28` (ISO)
  - `5.1.24` (ohne führende Nullen, zweistelliges Jahr)
  - `März 2024` und `Dez. 2023` (nur Monat, ohne Tag)
  - `15/01/2024` und `03/02/2024` (Schrägstriche)
  - `7.4.2024`
  - Das Datum `03/02/2024` (Zeile 26) ist nicht eindeutig: Es kann 3. Februar oder 2. März sein.
- **Zahlenformate beim Jahresumsatz:** Es gibt Tausenderpunkt und Dezimalkomma (`48.500,00`), Punkt ohne Komma (`12.300`, das auch 12,3 bedeuten könnte), Leerzeichen als Tausendertrennzeichen (`31 200 €`), Komma als Dezimaltrennzeichen ohne Tausenderpunkt (`12300,00`), Währungszeichen mal mit EUR, mal mit €, mal ohne. Außerdem stehen dort `n/a` (Zeile 18) und ein leerer Wert (Zeile 27).
- **Schreibweisen Firmennamen:** `Müller` / `Mueller`, `Schmidt & Söhne KG` / `Schmidt und Söhne KG`, `Elektro Krause` / `ELEKTRO KRAUSE GmbH`, `Weber Kunststofftechnik` / `Weber Kunststoff-Technik GmbH`. Rechtsformen fehlen teilweise.
- **Orte:** `musterhausen` / `Musterhausen` / `MUSTERHAUSEN`, `fiktivhausen` / `Fiktivhausen`, `Neustadt a. d. Probe` / `Neustadt a.d. Probe` / `neustadt a. d. probe` / `Neustadt an der Probe`, `Beispielstadt` / `Beispielstadt-Ost`.
- **Telefonnummern:** Mal `0000 111201`, mal `0000-111201`. Bei Zeile 13 fehlt die Nummer.
- **Ansprechpartner:** Anreden und Namensformen wechseln (`Herr K. Brandt`, `Hr. Krause`, `Frau Dr. Weber`, `Dr. Weber`, `Krause` ohne Vorname). Bei Zeile 6 und 21 fehlt der Ansprechpartner.
- **Warengruppen:** Uneinheitlich, z. B. `Schrauben/Normteile` und `Normteile`, `Elektrokomponenten` / `Elektro` / `Elektronik`.
- **Bewertung:** Kleinbuchstaben `a` (Zeile 25) und `b` (Zeile 28). Bei Zeile 9 und 17 fehlt die Bewertung.
- **Weitere fehlende Werte:**
  - E-Mail: Zeile 7 und 24
  - Letzte Bestellung: Zeile 17
  - Jahresumsatz: Zeile 27
- **Keine eindeutige Lieferanten-ID:** Der Firmenname dient als Schlüssel, und der ist uneinheitlich.

**3. Mögliche Dubletten**

| Gruppe | Zeilen | Begründung |
|---|---|---|
| Müller Stahlhandel | 2 und 8 | Gleiche E-Mail (brandt@stahl-mueller.example.com), gleicher Ansprechpartner (Brandt), gleicher Ort, gleiche Warengruppe (Stahl), gleiches Datum (12.03.2024) und gleicher Umsatz (48.500). Nur Name (Müller / Mueller) und Telefon-Schreibweise weichen ab. **Sehr wahrscheinlich dieselbe Firma.** |
| Schmidt & Söhne KG | 3 und 11 | Gleiche E-Mail, gleiche Telefonnummer, gleicher Ort, gleiches Datum (28.02.2024 = 2024-02-28) und gleicher Umsatz (12.300 = 12300,00). Ansprechpartner ist identisch (Lea Schmidt). **Sehr wahrscheinlich dieselbe Firma.** |
| Elektro Krause | 4 und 15 | Gleiche E-Mail, gleiche Telefonnummer, gleicher Ansprechpartner (Krause), gleicher Ort, gleicher Umsatz (31.200) und gleiche Bewertung (A). Das Datum weicht nur im Format ab (5.1.24 = 05.01.2024). **Sehr wahrscheinlich dieselbe Firma.** |
| Weber Kunststoff | 5 und 19 | Gleiche E-Mail, gleiche Telefonnummer, gleicher Ansprechpartner (Dr. Weber), gleicher Ort, gleiche Bewertung (B) und gleicher Umsatz (22.750,50 = 22750,5). Das Datum passt (März 2024 = 2024-03-01). **Sehr wahrscheinlich dieselbe Firma.** |

Ergebnis: 4 Dublettengruppen mit 8 betroffenen Zeilen. Nach dem Bereinigen blieben **23 eindeutige Lieferanten**.

Keine Dublette ist bei Hoffmann Logistik und Braun Transporte (beide Spedition), bei Keller Dichtungstechnik und Krüger Gummiwaren (beide Dichtungen) oder bei den Elektro-Lieferanten Krause und Fischer. Die Firmen sind verschieden, sie teilen nur die Warengruppe.

#### Nutzer 2

Schreib mir eine kurze Anleitung, wie die Liste künftig einheitlich gepflegt werden soll: Regeln für Schreibweisen, Datumsformat und Pflichtfelder.

#### Assistent 2

**Pflegeanleitung für die Lieferantenliste**

**1. Schreibweisen**
- Firmenname exakt wie im Handelsregister, mit Rechtsform (GmbH, KG usw.). Keine Abkürzungen wie „Mueller“ für „Müller“.
- „&“ oder „und“: Einheitlich eine Form festlegen, z. B. immer „und“.
- Umlaute als ä, ö, ü schreiben, nicht ae, oe, ue.
- Großschreibung nur am Wortanfang, also nicht „ELEKTRO KRAUSE“.
- Orte mit Großbuchstaben am Anfang, Ortsnamen einheitlich schreiben (z. B. „Neustadt an der Probe“).
- Ansprechpartner als „Vorname Nachname“, Anrede getrennt (Herr / Frau). Akademische Titel stehen vor dem Namen (z. B. „Dr.“). Keine Abkürzungen wie „Hr.“.
- Telefon einheitlich im Format `+49 …` oder `0000 111201`, ohne Bindestriche.
- E-Mail komplett in Kleinbuchstaben.
- Warengruppe nur aus einer festen Auswahlliste (z. B. Stahl, Normteile, Elektrokomponenten, Dichtungen, Spedition). Neue Gruppen werden zuerst in der Liste ergänzt.
- Bewertung nur A, B oder C (Großbuchstaben).

**2. Zahlen und Datum**
- Datum immer im Format **TT.MM.JJJJ** (z. B. 05.01.2024). Keine Monatsnamen, keine Schrägstriche, keine ISO-Formate, keine zweistelligen Jahre.
- Ist nur der Monat bekannt, wird der erste Tag eingetragen und das in einer Notiz vermerkt.
- Jahresumsatz als reine Zahl mit Dezimalkomma und Tausenderpunkt (z. B. 48.500,00). Kein Währungszeichen im Feld, denn die Spalte heißt bereits „Jahresumsatz EUR“.
- Keine Texte wie „n/a“ im Zahlenfeld. Unbekannt bedeutet leer, mit Vermerk.

**3. Pflichtfelder**
Diese Felder müssen ausgefüllt sein:
- Lieferant (amtlicher Name)
- Ort
- E-Mail
- Warengruppe (aus der Auswahlliste)
- Letzte Bestellung (TT.MM.JJJJ)
- Jahresumsatz EUR
- Bewertung (A, B oder C)

Ansprechpartner und Telefon sind empfohlen, aber nicht zwingend.

**4. Dubletten vermeiden**
- Jeder Lieferant bekommt eine eindeutige Lieferanten-Nummer. Sie ist der Schlüssel, nicht der Firmenname.
- Vor dem Anlegen eines neuen Lieferanten wird die E-Mail-Adresse und die Telefonnummer gesucht. Bei Treffer wird der bestehende Eintrag aktualisiert.
- Die Liste wird einmal im Quartal auf Dubletten geprüft.

**5. Technische Umsetzung**
Wenn die Liste in Excel oder einem ähnlichen Programm gepflegt wird, kann man Datenprüfungen (Auswahlliste für Warengruppe und Bewertung, Datumsprüfung, Pflichtfeldkontrolle) einrichten. Das verhindert die meisten Fehler schon bei der Eingabe.

---

### Modell: Sonnet

#### Nutzer 1

Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.

#### Assistent 1

Ich habe nichts verändert, das ist nur eine Analyse.

**1. Anzahl der Zeilen**
Die Liste hat **27 Datenzeilen** ohne Kopfzeile. Es gibt 9 Spalten: Lieferant, Ansprechpartner, Ort, Telefon, E-Mail, Warengruppe, Letzte Bestellung, Jahresumsatz EUR und Bewertung.

**2. Probleme**

*Datumsformate (Spalte "Letzte Bestellung")*
- Es gibt mindestens sieben Schreibweisen:
  - `12.03.2024` (TT.MM.JJJJ)
  - `2024-02-28` (ISO)
  - `5.1.24` und `7.4.2024` (ohne führende Nullen, teils zweistelliges Jahr)
  - `15/01/2024` und `03/02/2024` (Schrägstriche)
  - `März 2024`, `Dez. 2023` und `April 2024` (nur Monat, kein Tag)
- `03/02/2024` ist mehrdeutig. Es kann der 3. Februar oder der 2. März sein. Wegen `15/01/2024` in derselben Spalte vermute ich TT/MM/JJJJ, sicher ist das nicht.
- In Zeile 17 (Keller Dichtungstechnik) fehlt das Datum ganz.

*Beträge (Spalte "Jahresumsatz EUR")*
- Die Formate sind sehr unterschiedlich:
  - `48.500,00`
  - `12.300`
  - `31 200 €`
  - `9800`
  - `18.400,00 €`
  - `41.000 EUR`
  - `22750,5`
  - `63.200 €`
- Währungszusätze stehen teils im Wert, obwohl die Spalte schon "EUR" heißt.
- `12.300` kann ein Tausenderpunkt sein (12300) oder eine Dezimalzahl (12,3). Der Zusammenhang spricht für 12300, aber eindeutig ist es nicht.
- Bei Richter Glas & Optik steht `n/a`, bei Koch Elektronik ist der Wert leer.
- Beim Import in Excel werden diese Werte zum Teil als Text erkannt und lassen sich nicht summieren.

*Schreibweisen bei Orten*
- Groß- und Kleinschreibung ist uneinheitlich: `musterhausen`, `MUSTERHAUSEN`, `fiktivhausen`, `neustadt a. d. probe`.
- "Neustadt a. d. Probe" kommt in vier Varianten vor: `Neustadt a. d. Probe`, `Neustadt a.d. Probe`, `Neustadt an der Probe` und kleingeschrieben.

*Firmennamen und Rechtsformen*
- Die Rechtsform fehlt mal, mal steht sie da: `Elektro Krause` und `ELEKTRO KRAUSE GmbH`, `Weber Kunststofftechnik` und `Weber Kunststoff-Technik GmbH`.
- `&` steht neben `und`: `Schmidt & Söhne KG` und `Schmidt und Söhne KG`.
- `Müller` steht neben `Mueller`.
- Eine Zeile ist komplett in Großbuchstaben geschrieben.

*Ansprechpartner*
- Anrede und Namensform sind uneinheitlich: `Herr K. Brandt`, `K. Brandt`, `Hr. Krause`, `Frau Dr. Weber`, `Dr. Weber`, `Herr Dr. Wolf`.
- Bei Lackierwerk Ost und Schwarz Gießerei fehlt der Ansprechpartner.

*Telefon*
- Meist steht ein Leerzeichen im Wert (`0000 111201`), einmal ein Bindestrich (`0000-111201`).
- Bei Becker Werkzeugbau fehlt die Nummer.

*E-Mail*
- Bei Hoffmann Logistik und Krüger Gummiwaren fehlt die Adresse.

*Warengruppe*
- Dieselbe Gruppe heißt unterschiedlich:
  - `Elektrokomponenten`, `Elektro` und `Elektronik`
  - `Schrauben/Normteile` und `Normteile`
  - `Kunststoffteile` und `Kunststoff`
- `Dichtungen` kommt zweimal vor, das ist korrekt.
- Insgesamt gibt es keine feste Kategorienliste.

*Bewertung*
- Es gibt Kleinbuchstaben (`a`, `b`), und bei Bauer Präzisionsteile, Keller Dichtungstechnik und Koch Elektronik fehlt der Wert (Koch: nur Umsatz leer, Bewertung vorhanden, siehe oben).
- Korrekt gilt: Bei Bauer Präzisionsteile und Keller Dichtungstechnik fehlt die Bewertung. Bei Koch Elektronik fehlt der Umsatz, nicht die Bewertung.

*Fehlende Werte insgesamt*
- Es fehlen Ansprechpartner (2), E-Mail (2), Telefon (1), Datum (1, dazu 3 nur mit Monat), Umsatz (2 inkl. `n/a`) und Bewertung (2).

**3. Mögliche Dubletten**

| Zeilen | Einträge | Begründung |
|---|---|---|
| 2 und 8 | Müller Stahlhandel GmbH / Mueller Stahlhandel | Gleiche E-Mail (`brandt@stahl-mueller...`), gleiche Telefonnummer (nur anders geschrieben), gleicher Ort, gleiches Datum (12.03.2024), gleicher Umsatz 48.500, gleiche Bewertung A. Fast sicher dieselbe Firma. |
| 3 und 11 | Schmidt & Söhne KG / Schmidt und Söhne KG | Gleiche E-Mail, Telefon, Datum (28.02.2024), Umsatz (12.300) und Bewertung B. Nur "&" gegen "und" und die Warengruppe unterscheiden sich. Fast sicher dieselbe Firma. |
| 4 und 15 | Elektro Krause / ELEKTRO KRAUSE GmbH | Gleiche E-Mail, Telefon, Datum (5.1.24 gleich 05.01.2024), Umsatz 31.200 und Bewertung A. Ort und Warengruppe sind nur anders geschrieben. Fast sicher dieselbe Firma. |
| 5 und 19 | Weber Kunststofftechnik / Weber Kunststoff-Technik GmbH | Gleiche E-Mail, Telefon und Umsatz (22.750,50). Das Datum ist einmal "März 2024", einmal 01.03.2024 und passt zusammen. Gleiche Bewertung B. Sehr wahrscheinlich dieselbe Firma. |

**Keine Dubletten, aber ähnlich**
- Elektro Krause (Elektrokomponenten) und Fischer Kabelkonfektion (Elektrokomponenten) haben dieselbe Warengruppe, aber andere Kontaktdaten. Das ist kein Duplikat.
- Weber Kunststofftechnik und Wolf Messtechnik haben nur ähnlich klingende Namen. Sie gehören nicht zusammen.

**Empfehlung für den nächsten Schritt**
- Pro Dublettenpaar sollte ein Datensatz bleiben. Ich würde den vollständigeren behalten, also den mit Rechtsform und sauber geschriebenem Namen.
- Bei Dubletten würde ich den Umsatz nicht addieren, denn die Werte sind identisch und sehen nach demselben Betrag doppelt erfasst aus.
- Wenn du möchtest, bereinige ich die Liste im nächsten Schritt und zeige dir vorher eine Änderungsübersicht.

#### Nutzer 2

Schreib mir eine kurze Anleitung, wie die Liste künftig einheitlich gepflegt werden soll: Regeln für Schreibweisen, Datumsformat und Pflichtfelder.

#### Assistent 2

# Anleitung zur Pflege der Lieferantenliste

**Grundsatz:** Eine Zeile steht für genau einen Lieferanten. Vor jedem neuen Eintrag wird geprüft, ob der Lieferant schon vorhanden ist (Suche nach Name, E-Mail oder Telefonnummer).

## 1. Pflichtfelder
Diese Felder müssen immer ausgefüllt sein:
- Lieferant (vollständiger Firmenname)
- Ort
- Telefon oder E-Mail (mindestens eines von beiden)
- Warengruppe
- Bewertung

Diese Felder sollen ausgefüllt werden, sobald die Information vorliegt:
- Ansprechpartner
- Letzte Bestellung
- Jahresumsatz EUR

Wenn ein Wert fehlt, wird die Zelle **leer** gelassen. Kein "n/a", "-" oder "0". Wer etwas bewusst nicht kennt, vermerkt das in einer separaten Spalte "Bemerkung".

## 2. Schreibweisen
- **Firmenname:** Offizieller Name inklusive Rechtsform (GmbH, KG usw.), in normaler Groß- und Kleinschreibung, also nicht in Großbuchstaben. Umlaute bleiben erhalten (Müller, nicht Mueller). Statt "und" schreibt man "&", also immer "Schmidt & Söhne KG".
- **Ort:** Normale Schreibweise mit großem Anfangsbuchstaben, ausgeschrieben, keine Abkürzungen, also "Neustadt an der Probe". Ein Ort wird immer gleich geschrieben.
- **Ansprechpartner:** Immer in der Form "Anrede Vorname Nachname" (z. B. "Frau Lea Schmidt"). Titel stehen nach der Anrede ("Herr Dr. Wolf"). Keine "Hr."-Abkürzung.
- **Telefon:** Ein einheitliches Format mit Leerzeichen, ohne Bindestrich, z. B. `0000 111201`.
- **E-Mail:** Alles klein geschrieben, keine Leerzeichen.
- **Warengruppe:** Nur Werte aus einer festen Auswahlliste, z. B. Stahl, Normteile, Elektrokomponenten, Kunststoffteile, Oberflächen, Spedition, Drehteile, Verpackung, Werkzeuge, Verbrauchsmaterial, Hydraulik, Dichtungen, Optik, Sensoren, Gussteile, Büromaterial, Antriebe, Messtechnik, Schweißzubehör. Freie Eigenbezeichnungen sind nicht erlaubt. Brauchst du eine neue Gruppe, wird sie zuerst in die Liste aufgenommen.
- **Bewertung:** Nur ein **großer** Buchstabe A, B oder C.

## 3. Datumsformat
- Immer **TT.MM.JJJJ**, also zum Beispiel `05.01.2024`.
- Immer mit Tag, Monat und vierstelligem Jahr. Keine Schrägstriche, keine Monatsnamen, kein zweistelliges Jahr.
- Ist nur der Monat bekannt, wird der Eintrag geklärt oder die Zelle bleibt leer. Der Tag wird nicht geraten.
- In Excel die Spalte als Datum formatieren, damit sich sortieren und filtern lässt.

## 4. Jahresumsatz
- Nur die Zahl, ohne "€" oder "EUR", denn die Währung steht schon in der Spaltenüberschrift.
- Tausenderpunkt und zwei Nachkommastellen, also `48.500,00`. Die Spalte wird in Excel als Zahl formatiert, nicht als Text.

## 5. Dubletten vermeiden
- Vor dem Anlegen prüfen: Gibt es die E-Mail-Adresse oder Telefonnummer schon?
- Bei einer Namensänderung wird der bestehende Eintrag angepasst, es wird kein neuer angelegt.
- Einmal pro Quartal wird die Liste auf Dubletten und fehlende Pflichtfelder geprüft. Dafür ist eine Person verantwortlich, die im Team festgelegt wird.

## 6. Beispielzeile
`Schmidt & Söhne KG;Frau Lea Schmidt;Musterhausen;0000 222301;l.schmidt@schmidt-soehne.example.com;Normteile;28.02.2024;12.300,00;B`

---

### Modell: Opus

#### Nutzer 1

Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.

#### Assistent 1

Ich habe die Liste nur gelesen und nichts daran geändert. Das ist mir aufgefallen:

**1. Anzahl der Zeilen**

Die Liste hat **27 Datenzeilen** ohne Kopfzeile. Sie hat 9 Spalten: Lieferant, Ansprechpartner, Ort, Telefon, E-Mail, Warengruppe, Letzte Bestellung, Jahresumsatz EUR, Bewertung.
Vier Lieferanten stehen vermutlich doppelt drin (siehe Punkt 3). Dann wären es nur **23 verschiedene Lieferanten**.

**2. Gefundene Probleme**

**a) Datumsformate (Spalte „Letzte Bestellung")**: In einer Spalte stehen mindestens sieben verschiedene Formate:
- TT.MM.JJJJ: z. B. 12.03.2024, 14.11.2023 (das häufigste Format)
- JJJJ-MM-TT (ISO): z. B. 2024-02-28, 2024-04-08, 2024-03-01
- Kurzformen ohne führende Null: 5.1.24 (Elektro Krause), 7.4.2024 (Lange Büroservice)
- Schrägstriche: 15/01/2024 (Zimmermann), 03/02/2024 (Braun Transporte). **Achtung:** 03/02/2024 ist mehrdeutig. Es kann der 3. Februar sein oder, im US-Format, der 2. März.
- Nur Monat und Jahr: „März 2024" (Weber), „Dez. 2023" (Becker), „April 2024" (Wolf). Hier fehlt der genaue Tag.
- Leer: Keller Dichtungstechnik

**b) Umsatzformate (Spalte „Jahresumsatz EUR")**:
- Mal mit Tausenderpunkt und Komma (48.500,00), mal ohne (48500, 9800, 22750,5)
- Mal mit Leerzeichen als Tausendertrennzeichen (31 200 €)
- Mal steht eine Währung dabei („€", „EUR"), obwohl die Spalte schon „EUR" heißt
- „12.300" ohne Nachkommastellen kann ein Programm mit englischer Einstellung als 12,3 lesen
- Fehlende Werte: „n/a" bei Richter Glas & Optik, leer bei Koch Elektronik
- Mit diesen Mischformaten kann man in Excel nicht zuverlässig summieren oder sortieren

**c) Schreibweisen bei Orten**:
- Musterhausen / musterhausen / MUSTERHAUSEN
- Fiktivhausen / fiktivhausen
- Neustadt a. d. Probe / Neustadt a.d. Probe / Neustadt an der Probe / neustadt a. d. probe
- „Beispielstadt-Ost" (Lackierwerk Ost): Bitte prüfen, ob das ein eigener Ort ist oder ein Stadtteil von Beispielstadt

**d) Schreibweisen bei Firmennamen**:
- Umlaut gegen Umschreibung: „Müller" / „Mueller"
- „&" gegen „und": „Schmidt & Söhne KG" / „Schmidt und Söhne KG"
- Großschreibung: „ELEKTRO KRAUSE GmbH"
- Die Rechtsform fehlt mal und steht mal da (Müller Stahlhandel mit und ohne „GmbH", Weber mit und ohne „GmbH")
- Bindestrich: „Kunststofftechnik" / „Kunststoff-Technik"

**e) Ansprechpartner**:
- Anrede uneinheitlich: „Herr", „Hr.", „Frau" oder gar keine („K. Brandt", „Lea Schmidt", „Dr. Weber")
- Mal voller Name (Herr Tim Hoffmann), mal nur Nachname (Herr Krause), mal nur Initiale (Herr K. Brandt)
- Fehlt ganz: Lackierwerk Ost GmbH, Schwarz Gießerei

**f) Telefon**:
- Mal mit Leerzeichen getrennt (0000 111201), mal mit Bindestrich (0000-111201)
- Fehlt: Becker Werkzeugbau

**g) E-Mail**:
- Fehlt: Hoffmann Logistik, Krüger Gummiwaren

**h) Warengruppen**: Es gibt keinen festen Katalog, daher stehen gleiche Dinge unter verschiedenen Namen:
- Elektrokomponenten / Elektro / Elektronik
- Schrauben/Normteile / Normteile
- Kunststoffteile / Kunststoff
- Bei Keller und Krüger steht „Dichtungen". Das passt zusammen und ist richtig so.

**i) Bewertung**:
- Kleinbuchstaben: „a" (Wolf Messtechnik), „b" (Schäfer Schweißtechnik)
- Fehlt: Bauer Präzisionsteile, Keller Dichtungstechnik

**Übersicht der fehlenden Werte:**

| Spalte | fehlt bei |
|---|---|
| Ansprechpartner | Lackierwerk Ost GmbH, Schwarz Gießerei |
| Telefon | Becker Werkzeugbau |
| E-Mail | Hoffmann Logistik, Krüger Gummiwaren |
| Letzte Bestellung | Keller Dichtungstechnik |
| Jahresumsatz | Richter Glas & Optik („n/a"), Koch Elektronik (leer) |
| Bewertung | Bauer Präzisionsteile, Keller Dichtungstechnik |

**3. Mögliche Dubletten**

Diese vier Paare sind sehr wahrscheinlich derselbe Lieferant:

| # | Eintrag A | Eintrag B | Begründung |
|---|---|---|---|
| 1 | Müller Stahlhandel GmbH (Zeile 1) | Mueller Stahlhandel (Zeile 7) | Gleiche Telefonnummer (nur anders geschrieben), gleiche E-Mail, gleicher Ansprechpartner (K. Brandt), gleiches Datum (12.03.2024 = 2024-03-12), gleicher Umsatz (48.500), gleiche Bewertung A |
| 2 | Schmidt & Söhne KG (Zeile 2) | Schmidt und Söhne KG (Zeile 10) | Gleiche Telefonnummer und E-Mail, gleiche Ansprechpartnerin (Lea Schmidt), gleiches Datum (28.02.2024), gleicher Umsatz (12.300), Bewertung B. Nur die Warengruppe ist anders („Schrauben/Normteile" / „Normteile") |
| 3 | Elektro Krause (Zeile 3) | ELEKTRO KRAUSE GmbH (Zeile 14) | Gleiche Telefonnummer und E-Mail, gleicher Ort (anders geschrieben), gleiches Datum (5.1.24 = 05.01.2024), gleicher Umsatz (31.200), Bewertung A |
| 4 | Weber Kunststofftechnik (Zeile 4) | Weber Kunststoff-Technik GmbH (Zeile 18) | Gleiche Telefonnummer und E-Mail, Dr. Weber, Fiktivhausen, gleicher Umsatz (22.750,50), Bewertung B. Die Daten widersprechen sich nicht („März 2024" / 2024-03-01) |

(Zeilennummern zählen ab der ersten Datenzeile.)

**Keine Dubletten**, obwohl es auf den ersten Blick so aussehen kann:
- Elektro Krause, Fischer Kabelkonfektion und Koch Elektronik: ähnliche Warengruppe und gleicher Ort, aber verschiedene Firmen, Telefonnummern und E-Mails
- Hoffmann Logistik und Braun Transporte: beide „Spedition", aber verschiedene Firmen
- Keller Dichtungstechnik und Krüger Gummiwaren: beide „Dichtungen", aber verschiedene Firmen

**Empfehlung:** Bevor Sie die Dubletten zusammenführen, prüfen Sie bitte, welcher Eintrag aktuell ist, zum Beispiel im ERP-System. Bei Schmidt & Söhne sollten Sie außerdem festlegen, welche Warengruppe richtig ist. Wenn Sie möchten, mache ich Ihnen im nächsten Schritt einen Vorschlag für eine bereinigte Liste.

#### Nutzer 2

Schreib mir eine kurze Anleitung, wie die Liste künftig einheitlich gepflegt werden soll: Regeln für Schreibweisen, Datumsformat und Pflichtfelder.

#### Assistent 2

**Anleitung: Pflege der Lieferantenliste**

**1. Grundsätze**
- Jeder Lieferant steht **nur einmal** in der Liste. Suchen Sie vor jedem neuen Eintrag nach dem Namen, der Telefonnummer und der E-Mail-Adresse. So finden Sie auch Einträge, die anders geschrieben sind.
- Ändern Sie bestehende Einträge, statt neue anzulegen.
- Lassen Sie kein Feld mit Platzhaltern wie „n/a", „-" oder „?" stehen. Was unbekannt ist, bleibt leer und wird so bald wie möglich nachgetragen.

**2. Pflichtfelder**

Diese Felder müssen immer ausgefüllt sein:

| Feld | Pflicht? |
|---|---|
| Lieferant | **Ja** |
| Ort | **Ja** |
| Telefon | **Ja** |
| E-Mail | **Ja** (mindestens eine allgemeine Adresse, z. B. info@…) |
| Warengruppe | **Ja** |
| Bewertung | **Ja** (neue Lieferanten zunächst mit „B", bis die erste Bewertung vorliegt) |
| Ansprechpartner | Ja, sobald bekannt |
| Letzte Bestellung | Ja, sobald bestellt wurde |
| Jahresumsatz EUR | Ja, jährlich aktualisieren (bei neuen Lieferanten: 0) |

**3. Schreibweisen**

**Lieferant (Firmenname)**
- Schreiben Sie den offiziellen Namen mit Rechtsform, wie er auf Rechnung oder Briefbogen steht, z. B. „Müller Stahlhandel GmbH".
- Verwenden Sie Umlaute (ä, ö, ü, ß), keine Umschreibungen wie „ae" oder „ue".
- Normale Groß- und Kleinschreibung, nicht alles in Großbuchstaben.
- Übernehmen Sie „&" oder „und" so, wie es im offiziellen Namen steht.

**Ansprechpartner**
- Format: **Anrede Vorname Nachname**, z. B. „Frau Lea Schmidt", „Herr Dr. Paul Wolf".
- Als Anrede nur „Herr" oder „Frau" ausgeschrieben, nicht „Hr." oder „Fr.".
- Titel wie „Dr." stehen nach der Anrede.

**Ort**
- Den offiziellen Ortsnamen mit normaler Groß- und Kleinschreibung, z. B. „Musterhausen".
- Zusätze immer gleich abkürzen, mit Leerzeichen, z. B. „Neustadt a. d. Probe".
- Stadtteile nur, wenn das wirklich nötig ist, und dann einheitlich.

**Telefon**
- Format: **Vorwahl Leerzeichen Rufnummer**, z. B. „0000 111201".
- Keine Bindestriche, Schrägstriche oder Klammern.

**E-Mail**
- Nur Kleinbuchstaben, ohne Leerzeichen.

**Warengruppe**
- Wählen Sie nur aus einer festen Liste, z. B. Stahl, Normteile, Elektrokomponenten, Kunststoffteile, Oberflächen, Spedition, Drehteile, Verpackung, Werkzeuge, Verbrauchsmaterial, Hydraulik, Dichtungen, Optik, Sensoren, Gussteile, Büromaterial, Antriebe, Messtechnik, Schweißzubehör.
- Neue Warengruppen legt nur die verantwortliche Person (z. B. der Einkauf) fest.
- Tipp: In Excel können Sie die Liste als Auswahlfeld hinterlegen (Daten > Datenüberprüfung > Liste).

**Bewertung**
- Nur **A**, **B** oder **C**, immer als Großbuchstabe.

**4. Datumsformat**
- Einheitlich **TT.MM.JJJJ** mit führenden Nullen, z. B. „05.01.2024".
- Kein ISO-Format, keine Schrägstriche, keine Kurzformen wie „5.1.24", keine Monatsnamen wie „März 2024".
- Wenn nur der Monat bekannt ist, prüfen Sie das genaue Datum im Bestellsystem und tragen Sie es nach.
- Tipp: Formatieren Sie die Spalte in Excel als Datum. Dann wird jedes eingegebene Datum gleich angezeigt.

**5. Jahresumsatz**
- Nur die Zahl, ohne „€" oder „EUR". Die Währung steht schon im Spaltennamen.
- Format: Tausenderpunkt und zwei Nachkommastellen, z. B. „48.500,00".
- Tipp: Formatieren Sie die Spalte in Excel als Zahl mit 2 Dezimalstellen und Tausendertrennzeichen. Dann tippen Sie nur „48500" ein.

**6. Kontrolle**
- Prüfen Sie die Liste einmal im Quartal: Gibt es Dubletten? Sind Pflichtfelder leer? Sind Schreibweisen abgewichen?
- Legen Sie eine verantwortliche Person für die Liste fest.

Wenn Sie möchten, formuliere ich die Anleitung auch als einseitiges Merkblatt oder mache Ihnen eine Excel-Vorlage mit Auswahllisten.
