# Testlauf: Übung 3 / Station D Für Schnelle – Fehlende Spalten für Lieferantenverwaltung

**Herkunft:** [Übung 3: Dokumente und Tabellen](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md), Station D „Unordentliche Tabelle bereinigen“, Abschnitt „Für Schnelle“, erster Punkt:

```
Welche Spalten fehlen in dieser Liste, die man für eine ordentliche Lieferantenverwaltung bräuchte?
```

**Material:** [lieferantenliste_unsortiert.csv](../07_Beispielmaterial/lieferantenliste_unsortiert.csv)
**Trainer-Hinweise:** [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md), Abschnitt „Station D: Lieferantenliste bereinigen“. Zu den „Für Schnelle“-Aufgaben stehen dort **keine** erwarteten Ergebnisse.

> **Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Testaufbau:** Wie im Kurs: Zuerst der Basis-Prompt von Station D (Analyse ohne Änderung), danach im **selben Chat** die Frage nach den fehlenden Spalten. Der „Weiter“-Prompt (Bereinigung) wurde in diesem Lauf übersprungen.

**Vorhandene Spalten (dürfen nicht als „fehlend“ genannt werden):** Lieferant; Ansprechpartner; Ort; Telefon; E-Mail; Warengruppe; Letzte Bestellung; Jahresumsatz EUR; Bewertung. Die Datei hat 27 Datenzeilen (per `python3`/`csv` nachgezählt).

**Erwartbare sinnvolle Vorschläge:** Lieferantennummer/ID (Kreditorennummer), Straße/PLZ/Land, USt-IdNr./Steuernummer, Zahlungs- und Lieferbedingungen, Zertifizierungen (z. B. ISO 9001), Datum der letzten Bewertung/Audit, Status aktiv/gesperrt, Bankverbindung – idealerweise mit Hinweis auf Vertraulichkeit/Datenschutz.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Keine vorhandene Spalte als „fehlend“ genannt | ja | ja | ja |
| Lieferantennummer / eindeutige ID | ja (als wichtigste) | ja (als wichtigste) | ja (inkl. Kreditorennummer) |
| Straße / PLZ / Land | ja | ja | ja |
| USt-IdNr. / Steuernummer | ja | ja | ja |
| Zahlungs- und Lieferbedingungen | ja | ja | ja |
| Zertifizierungen (ISO 9001) mit Gültigkeit | ja | ja | ja |
| Bewertungsdatum / Bewertungskriterien | ja | ja | ja |
| Status aktiv / gesperrt | ja | ja | ja |
| Bankverbindung | ja, mit Hinweis Zugriffsschutz | ja, **ohne** Hinweis (sogar Priorität 4) | ja, mit Hinweis Betrug/Datenschutz, besser ins Buchhaltungssystem |
| Datenschutz-Hinweis zu personenbezogenen Kontaktdaten | nein | nein | ja (DSGVO, Zugriff beschränken) |
| Bezug zu den vorher gefundenen Problemen (ID gegen Dubletten, Bezugsjahr Umsatz, Auswahllisten) | ja | ja | ja |
| Priorisierung für den Einstieg | ja (5 Spalten) | ja (6 Punkte) | ja (Gruppe „Unbedingt nötig“) |
| Länge / Verdaulichkeit für Nicht-Entwickler | ca. 20 Vorschläge, gut gegliedert | ca. 22 Vorschläge, gut gegliedert | 22 nummerierte Vorschläge, am längsten |
| Sachfehler in der Antwort zu den Spalten | keiner (kleine Unschärfe, s. u.) | keiner | keiner |
| Vorlauf (Analyse aus dem Basis-Prompt) korrekt: 27 Zeilen, 4 Dubletten-Paare | ja | ja (+ 23 Lieferanten) | ja (+ 23 Lieferanten, inkl. „keine Dubletten“-Fallen) |

**Fazit:** Die Übung funktioniert wie gedacht. Alle drei Modelle liefern praxisnahe, plausible Vorschläge und nennen keine bereits vorhandene Spalte als fehlend. Die Unterschiede liegen in der Tiefe der Hinweise (Datenschutz, Bankdaten) und in der Länge der Antwort, nicht in der Richtigkeit.

---

## Gefundene Fehler mit Beleg

Bei der eigentlichen Frage nach den fehlenden Spalten gibt es **keine echten Sachfehler**. Folgende kleinere Punkte fallen auf:

1. **Haiku, Antwort 2 – „Währung (die Umsatzspalte ist nur implizit in EUR)“:** Ungenau. Die Kopfzeile lautet ausdrücklich `Jahresumsatz EUR`, die Währung ist also explizit im Spaltennamen genannt. Sonnet formuliert es richtig („nur indirekt über ‚EUR‘ in der Spaltenüberschrift erkennbar“), Opus begründet die Währungsspalte sinnvoller („falls auch Lieferanten außerhalb des Euro-Raums dazukommen“).
2. **Sonnet, Antwort 2 – Bankverbindung ohne Schutzhinweis:** IBAN/BIC wird als Priorität 4 zur Aufnahme in die Liste empfohlen, ohne zu erwähnen, dass Bankdaten in einer frei kursierenden Tabelle ein Betrugs- und Vertraulichkeitsrisiko sind. Kein Fehler, aber ein fehlender Praxishinweis (Haiku: „mit Zugriffsschutz“; Opus: „gehört meist besser ins Buchhaltungssystem“).
3. **Sonnet, Antwort 2 – „Zuordnung von Warengruppe über eine feste Auswahlliste“** steht unter den fehlenden Spalten, ist aber keine neue Spalte, sondern eine Pflegeregel für die vorhandene Spalte „Warengruppe“. Unscharf eingeordnet, inhaltlich sinnvoll. Opus trennt das sauber („Zwei Hinweise zur bestehenden Struktur“).
4. **Haiku, Antwort 1 – unvollständige Betragsliste:** Bei den Betragsformaten fehlt `63.200 €` (Schwarz Gießerei, Zeile 21 der Datei). Die übrigen Formate stimmen. Für die Spaltenfrage ohne Folgen.
5. **Unterschiedliche Zeilennummerierung (kein Fehler, aber Verwirrungsgefahr):** Haiku zählt Dateizeilen (Kopfzeile = Zeile 1, Müller = Zeile 2, Dubletten 2/8, 3/11, 4/15, 5/19), Opus zählt Datenzeilen (Müller = Zeile 1, Dubletten 1/7, 2/10, 3/14, 4/18 – wie in den Trainer-Hinweisen). Beide sind in sich korrekt (per `python3` nachgeprüft), Opus und Haiku sagen ausdrücklich, wie sie zählen. Sonnet nennt keine Zeilennummern.

Nachgeprüft: 27 Datenzeilen, alle von den Modellen genannten fehlenden Werte (Ansprechpartner Lackierwerk/Schwarz, Telefon Becker, E-Mail Hoffmann/Krüger, Datum Keller, Umsatz Richter „n/a“/Koch leer, Bewertung Bauer/Keller) und alle vier Dubletten-Paare stimmen mit der Datei und den Trainer-Hinweisen überein. Erfundene Spalten oder erfundene Inhalte gibt es nicht.

---

## Lehren für die Auswertung

- **Hier glänzt die KI:** Die Frage nach fehlenden Spalten ist eine typische „Checklisten-/Fachwissen“-Aufgabe ohne Zählen und Rechnen. Alle drei Modelle liefern brauchbare Ergebnisse. Guter Kontrast zum Basis-Teil von Station D, wo Zählen und Beträge die Fehlerquellen sind: Bei „Was fehlt / woran sollte ich denken?“ ist die KI stark, bei „Zähl genau nach“ muss man prüfen.
- **Kontext macht den Unterschied:** Weil die Frage im selben Chat nach der Analyse kommt, begründen die Modelle ihre Vorschläge mit der konkreten Liste (Lieferantennummer gegen die vier Dubletten, Bezugsjahr für „Jahresumsatz“, getrennte Anrede/Vorname/Nachname gegen „Hr. Krause“/„Herr Krause“, Auswahllisten gegen „Elektro“/„Elektrokomponenten“). Zeigen: Das ist mehr als eine allgemeine Internet-Checkliste.
- **Zu viel des Guten:** 20+ Vorschläge sind für eine echte Excel-Liste zu viel. Gute Nachfrage für die Auswertung: „Welche 5 davon würdest du in deiner Abteilung wirklich einführen – und wer pflegt sie?“ Alternativ-Prompt: „Nenne die 5 wichtigsten fehlenden Spalten, jeweils mit einem Satz Begründung.“
- **Datenschutz-Moment:** Nur Opus weist auf personenbezogene Daten (DSGVO) hin, nur Haiku und Opus auf die Sensibilität von Bankdaten. Brücke zur [Daten-Ampel](../03_Daten-Ampel.md): Eine Lieferantenliste mit IBAN und Namen von Ansprechpartnern wäre im echten Betrieb nicht mehr „grün“.
- **Kein „richtig/falsch“, sondern „passt es zu uns?“:** Die Teilnehmenden können die Vorschläge der drei Gruppen vergleichen – die Kerne (ID, Adresse, USt-IdNr., Zahlungsbedingungen, Status, Zertifikate) tauchen überall auf, der Rest ist Geschmack und Branche. Das zeigt gut, wie man KI-Vorschläge als Ideenliste nutzt und selbst auswählt.
- **Fachbegriffe erklären lassen:** Incoterms, Kreditorennummer, IATF 16949 tauchen ungefragt auf. Wer sie nicht kennt, sollte nachfragen („Erkläre Incoterms in zwei Sätzen“) statt sie zu übernehmen.

---

## Gesprächsprotokolle

### Modell: Haiku

#### Nutzer 1

```
Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.
```

(Anhang: lieferantenliste_unsortiert.csv)

#### Assistent 1

Ich habe die Datei gelesen, ohne sie zu verändern.

**1. Anzahl der Zeilen**
Die Liste hat **27 Datenzeilen** (Zeilen 2 bis 28 der Datei, ohne Kopfzeile).

**2. Probleme**

*Datumsformate uneinheitlich:*
- Deutsch mit Punkt: `12.03.2024`, `14.11.2023`, `01.04.2024`
- ISO: `2024-02-28`, `2024-03-01`
- Kurzform ohne führende Nullen: `5.1.24`, `7.4.2024`
- Mit Schrägstrich: `15/01/2024`, `03/02/2024` (bei `03/02/2024` ist unklar, ob 3. Februar oder 2. März)
- Ausgeschrieben: `März 2024`, `April 2024`, `Dez. 2023`
- Nur Monat/Jahr, kein Tag, daher nicht exakt datierbar
- Leer: Keller Dichtungstechnik (Zeile 17)

*Umsatz uneinheitlich:*
- Tausendertrennzeichen und Dezimalkomma gemischt: `48.500,00`, `22.750,50`
- Ohne Dezimalstellen und ohne Trennzeichen: `48500`, `9800`
- Mit Währungszeichen oder -code an unterschiedlichen Stellen: `31 200 €`, `18.400,00 €`, `41.000 EUR`, `11.300 EUR`
- Mehrdeutig: `12.300` und `14.900` könnten 12.300 bzw. 12,30 sein (wahrscheinlich 12.300 gemeint)
- Dezimalkomma ohne Nullen: `22750,5`
- Nicht vorhanden oder nicht verwertbar: `n/a` (Richter Glas & Optik, Zeile 18), leer (Koch Elektronik, Zeile 27)

*Schreibweisen von Firmen- und Ortsnamen:*
- Firma: `Müller Stahlhandel GmbH` vs. `Mueller Stahlhandel`; `Schmidt & Söhne KG` vs. `Schmidt und Söhne KG`; `Elektro Krause` vs. `ELEKTRO KRAUSE GmbH`; `Weber Kunststofftechnik` vs. `Weber Kunststoff-Technik GmbH`
- Ort: `Musterhausen`, `musterhausen`, `MUSTERHAUSEN`; `Neustadt a. d. Probe`, `Neustadt a.d. Probe`, `Neustadt an der Probe`, `neustadt a. d. probe`; `Fiktivhausen` vs. `fiktivhausen`

*Ansprechpartner uneinheitlich:*
- Anrede und Vorname wechseln: `Herr K. Brandt` vs. `K. Brandt`, `Frau Lea Schmidt` vs. `Lea Schmidt`, `Herr Krause` vs. `Hr. Krause`, `Frau Dr. Weber` vs. `Dr. Weber`

*Warengruppe uneinheitlich:*
- `Schrauben/Normteile` vs. `Normteile`; `Elektrokomponenten` vs. `Elektro` vs. `Elektronik`; `Kunststoffteile` vs. `Kunststoff`

*Bewertung uneinheitlich:*
- Kleinbuchstaben `a` (Zeile 25) und `b` (Zeile 28) statt `A`/`B`
- Leer: Bauer Präzisionsteile (Zeile 9), Keller Dichtungstechnik (Zeile 17)
- Zusätzlich fehlt eine Skala (z. B. A = gut, C = schlecht), die aus der Liste nicht hervorgeht

*Telefonnummern uneinheitlich:*
- `0000 111201` vs. `0000-111201` (Zeile 8)

*Fehlende Werte:*
- Kein Ansprechpartner: Lackierwerk Ost GmbH (Zeile 6), Schwarz Gießerei (Zeile 21)
- Keine E-Mail: Hoffmann Logistik (Zeile 7), Krüger Gummiwaren (Zeile 24)
- Keine Telefonnummer: Becker Werkzeugbau (Zeile 13)
- Kein Datum der letzten Bestellung: Keller Dichtungstechnik (Zeile 17)
- Keine Bewertung: Bauer Präzisionsteile (Zeile 9), Keller Dichtungstechnik (Zeile 17)

**3. Mögliche Dubletten**

1. **Müller Stahlhandel GmbH (Zeile 2) und Mueller Stahlhandel (Zeile 8)**
   Gleiche E-Mail (`brandt@stahl-mueller.example.com`), gleiche Telefonnummer (nur Trennzeichen anders), gleicher Ort, gleicher Umsatz (48.500), gleiche Warengruppe (Stahl) und gleiche Bewertung (A). Sehr wahrscheinlich dieselbe Firma.

2. **Schmidt & Söhne KG (Zeile 3) und Schmidt und Söhne KG (Zeile 11)**
   Gleiche E-Mail (`l.schmidt@schmidt-soehne.example.com`), gleiche Telefonnummer, gleicher Ort (Musterhausen/musterhausen), gleicher Umsatz (12.300 bzw. 12300,00), Bewertung B in beiden Zeilen. Sehr wahrscheinlich dieselbe Firma.

3. **Elektro Krause (Zeile 4) und ELEKTRO KRAUSE GmbH (Zeile 15)**
   Gleiche E-Mail (`info@elektro-krause.example.com`), gleiche Telefonnummer, gleicher Ort (Neustadt), gleicher Umsatz (31.200), Bewertung A in beiden Zeilen. Sehr wahrscheinlich dieselbe Firma.

4. **Weber Kunststofftechnik (Zeile 5) und Weber Kunststoff-Technik GmbH (Zeile 19)**
   Gleiche E-Mail (`weber@weber-kunststoff.example.com`), gleiche Telefonnummer, gleicher Ort (Fiktivhausen), gleicher Umsatz (22.750,50 bzw. 22750,5), Bewertung B in beiden Zeilen. Sehr wahrscheinlich dieselbe Firma.

Nicht als Dublette gewertet: Fischer Kabelkonfektion (Zeile 12) und Koch Elektronik (Zeile 27) liegen beide in Neustadt und gehören zur Elektrobranche, haben aber unterschiedliche Namen, Telefonnummern und E-Mail-Adressen.

Ich habe nichts an der Datei geändert.

#### Nutzer 2

```
Welche Spalten fehlen in dieser Liste, die man für eine ordentliche Lieferantenverwaltung bräuchte?
```

#### Assistent 2

Die Liste enthält Stammdaten und Umsatz, aber für eine saubere Lieferantenverwaltung fehlen vor allem folgende Spalten:

**Identifikation und Stammdaten**
- **Lieferantennummer (eindeutige ID):** Damit Dubletten wie die vier oben gefundenen nicht mehr über Namensvarianten entstehen. Das ist die wichtigste Ergänzung.
- **Rechtsform:** Getrennt vom Firmennamen, damit `GmbH`, `KG` usw. einheitlich geführt werden.
- **Straße, PLZ, Land:** Eine vollständige Anschrift statt nur des Orts, mit normierten Orts- und Ländernamen.
- **USt-IdNr. bzw. Steuernummer:** Pflicht für Rechnungsprüfung und innergemeinschaftliche Geschäfte.
- **Website:** Hilft bei der Prüfung und Dublettenerkennung.

**Kontakt**
- **Funktion des Ansprechpartners** (z. B. Vertrieb, Buchhaltung) und **Abteilungs-E-Mail** getrennt von der persönlichen E-Mail.
- **Mobil- oder Durchwahl-Nummer** neben der Zentrale.

**Geschäftliche Konditionen**
- **Zahlungsbedingungen** (z. B. 30 Tage netto, 2 % Skonto).
- **Währung** (die Umsatzspalte ist nur implizit in EUR).
- **Bankverbindung (IBAN, BIC):** Wichtig für Zahlungsabwicklung, sollte aber mit Zugriffsschutz geführt werden.
- **Lieferbedingungen** (Incoterms) und **Mindestbestellmenge**.
- **Lieferzeit** in Tagen.

**Vertrag und Status**
- **Lieferantenstatus** (aktiv, inaktiv, gesperrt, in Prüfung). Die Liste kennt nur die letzte Bestellung, nicht den Status.
- **Vertragsbeginn und Vertragsende** bzw. Rahmenvertrag ja/nein, inklusive Kündigungsfrist.
- **Zertifizierungen** (z. B. ISO 9001) mit Gültigkeitsdatum.
- **Versicherungsnachweis** und Ablaufdatum, besonders bei Spedition und Dienstleistern.

**Bewertung und Steuerung**
- **Bewertungskriterien getrennt**, z. B. Qualität, Liefertreue, Preis, mit einer dokumentierten Skala. Die Gesamtbewertung A/B/C ist nicht nachvollziehbar.
- **Bewertungsdatum** bzw. Datum der letzten Überprüfung.
- **Risikoeinstufung** (z. B. Einzelquelle, kritische Warengruppe).
- **Zuständiger Einkäufer** intern.

**Zeitstempel und Nachvollziehbarkeit**
- **Angelegt am** und **zuletzt geändert am** (mit Kürzel des Bearbeiters).
- **Notizen oder Bemerkungen** für Besonderheiten.

**Zur Klarheit der Umsatzspalte:** Ergänzen Sie außerdem das **Bezugsjahr** bzw. Geschäftsjahr, denn `Jahresumsatz` ohne Jahresangabe ist nicht eindeutig.

Für den Start empfehle ich zuerst: Lieferantennummer, Rechtsform, Lieferantenstatus, Zahlungsbedingungen und Bewertungsdatum. Damit lassen sich Dubletten vermeiden und die Liste im Alltag nutzen.

---

### Modell: Sonnet

#### Nutzer 1

```
Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.
```

(Anhang: lieferantenliste_unsortiert.csv)

#### Assistent 1

Ich habe nichts verändert, sondern die Datei nur gelesen.

**1. Anzahl der Zeilen**
Die Liste hat **27 Datenzeilen** ohne Kopfzeile. Es gibt 9 Spalten: Lieferant, Ansprechpartner, Ort, Telefon, E-Mail, Warengruppe, Letzte Bestellung, Jahresumsatz EUR, Bewertung.

**2. Erkannte Probleme**

*Datumsformate (Spalte "Letzte Bestellung")*
- Die Formate sind uneinheitlich:
  - `12.03.2024` (TT.MM.JJJJ)
  - `2024-02-28` (ISO)
  - `5.1.24` und `7.4.2024` (ohne führende Nullen, teils zweistelliges Jahr)
  - `15/01/2024` und `03/02/2024` (Schrägstriche)
  - `März 2024`, `Dez. 2023` und `April 2024` (nur Monat und Jahr, ohne Tag)
- `03/02/2024` ist mehrdeutig. Es kann der 3. Februar oder der 2. März sein. Bei `15/01/2024` ist es eindeutig TT/MM.
- Bei `5.1.24` und `7.4.2024` ist die Lesart TT.MM nur wahrscheinlich.
- Bei den reinen Monatsangaben fehlt der Tag. Man kann ihn nicht sauber ergänzen, ohne zu raten.
- Zeile 17 (Keller Dichtungstechnik) hat gar kein Datum.

*Jahresumsatz (Zahlen- und Währungsformate)*
- Die Schreibweisen sind gemischt:
  - `48.500,00`
  - `12.300`
  - `31 200 €`
  - `9800`
  - `18.400,00 €`
  - `11.300 EUR`
  - `41.000 EUR`
  - `22750,5`
  - `12300,00`
- Die Spalte heißt schon "EUR", trotzdem stehen teils "€" oder "EUR" im Wert.
- Bei `12.300` ist nicht ganz sicher, ob es Tausendertrennzeichen oder Dezimalpunkt ist. Wahrscheinlich ist es Tausender.
- Bei Richter Glas & Optik steht `n/a`. Bei Koch Elektronik ist der Wert leer.

*Schreibweisen und Konsistenz*
- **Firmennamen:** Rechtsformen und Schreibweisen weichen ab (Dubletten siehe Punkt 3).
  - "Müller" und "Mueller"
  - "&" und "und"
  - "Kunststofftechnik" und "Kunststoff-Technik GmbH"
  - "Elektro Krause" und "ELEKTRO KRAUSE GmbH"
  - Rechtsformen fehlen oder variieren (GmbH, KG, ohne).
- **Orte:** Groß- und Kleinschreibung sowie Abkürzungen sind uneinheitlich.
  - `musterhausen`, `MUSTERHAUSEN` und `Musterhausen`
  - `fiktivhausen` und `Fiktivhausen`
  - `neustadt a. d. probe`, `Neustadt a. d. Probe`, `Neustadt a.d. Probe` und `Neustadt an der Probe`
- **Anreden und Titel:** Es gibt "Herr", "Hr.", "Frau", "Frau Dr.", "Dr. Weber" und "Herr K. Brandt" neben "K. Brandt". Mal steht der Vorname dabei, mal nur der Nachname.
- **Telefon:** `0000 111201` und `0000-111201` sind unterschiedlich formatiert.
- **Warengruppen:** Sie sind nicht vereinheitlicht.
  - `Schrauben/Normteile` und `Normteile`
  - `Elektrokomponenten` und `Elektro`
  - `Kunststoffteile` und `Kunststoff`
  - `Elektronik` ist wohl eine eigene Gruppe, liegt aber nah an "Elektro".
- **Bewertung:** Es kommen `a` und `b` in Kleinbuchstaben vor, sonst Großbuchstaben (A, B, C).

*Fehlende Werte*
- Ansprechpartner fehlt bei Lackierwerk Ost GmbH und bei Schwarz Gießerei.
- E-Mail fehlt bei Hoffmann Logistik und bei Krüger Gummiwaren.
- Telefon fehlt bei Becker Werkzeugbau.
- Bewertung fehlt bei Bauer Präzisionsteile und bei Keller Dichtungstechnik.
- Letzte Bestellung fehlt bei Keller Dichtungstechnik.
- Jahresumsatz fehlt oder ist `n/a` bei Koch Elektronik und bei Richter Glas & Optik.

*Weitere Auffälligkeiten*
- Die Telefonnummern wirken wie Platzhalter (`0000 ...`). Die E-Mail-Domains sind `.example.com`. Es sind also offenbar Beispieldaten.
- Mehrere Lieferanten sind in demselben Ort ansässig. Das ist kein Fehler, hilft aber bei der Dublettenprüfung.

**3. Mögliche Dubletten**

| Zeilen (Lieferant) | Begründung |
|---|---|
| **Müller Stahlhandel GmbH** und **Mueller Stahlhandel** | Gleiche E-Mail (`brandt@stahl-mueller.example.com`), gleiche Telefonnummer (nur anders formatiert), gleicher Ansprechpartner K. Brandt, gleicher Ort, gleiche Warengruppe, gleiches Datum (12.03.2024 und 2024-03-12), gleicher Umsatz (48.500) und gleiche Bewertung A. Die Schreibweise von "Müller" weicht ab. |
| **Schmidt & Söhne KG** und **Schmidt und Söhne KG** | Gleiche E-Mail und Telefonnummer, gleiche Ansprechpartnerin Lea Schmidt, gleiches Datum (28.02.2024) und gleicher Umsatz (12.300). Nur "&" und "und" sowie die Warengruppe (`Schrauben/Normteile` und `Normteile`) und die Ortsschreibung unterscheiden sich. |
| **Elektro Krause** und **ELEKTRO KRAUSE GmbH** | Gleiche E-Mail und Telefonnummer, gleicher Ansprechpartner Krause, gleiches Datum (5.1.24 und 05.01.2024), gleicher Umsatz (31.200) und gleiche Bewertung A. Die Schreibweise von Firma, Ort und Warengruppe unterscheidet sich. |
| **Weber Kunststofftechnik** und **Weber Kunststoff-Technik GmbH** | Gleiche E-Mail und Telefonnummer, gleicher Ansprechpartner Weber, gleicher Ort, gleicher Umsatz (22.750,50), gleiche Bewertung B. Das Datum ist März 2024 und 2024-03-01, was zusammenpasst. |

Das sind also **4 Dublettenpaare**, 8 Zeilen. Nach dem Zusammenführen blieben 23 eindeutige Lieferanten.

Bei den übrigen Lieferanten sehe ich keine Dubletten. Keller Dichtungstechnik und Krüger Gummiwaren haben zwar beide die Warengruppe "Dichtungen", aber unterschiedliche Firmen, Orte und Kontakte. Das ist keine Dublette. Vor dem Zusammenführen sollte man die Paare kurz prüfen und entscheiden, welcher Datensatz der führende ist.

#### Nutzer 2

```
Welche Spalten fehlen in dieser Liste, die man für eine ordentliche Lieferantenverwaltung bräuchte?
```

#### Assistent 2

Für eine ordentliche Lieferantenverwaltung fehlen vor allem diese Spalten.

**Stammdaten und Identifikation**
- **Lieferantennummer (eindeutige ID).** Das ist die wichtigste fehlende Spalte. Mit ihr ließen sich Dubletten vermeiden und die Daten mit ERP und Buchhaltung verknüpfen.
- **Rechtsform** als eigene Spalte, statt sie im Firmennamen mitzuführen.
- **Straße, Hausnummer und PLZ.** Es gibt nur den Ort, damit lässt sich weder eine Bestellung noch eine Rechnung adressieren.
- **Land.**
- **Website.**

**Kontakt**
- **Anrede, Vorname und Nachname getrennt.** Aktuell stehen Anrede, Titel und Name in einem Feld.
- **Funktion oder Abteilung** des Ansprechpartners (z. B. Vertrieb, Einkauf).
- **Mobilnummer oder zentrale Nummer.**

**Kaufmännische und rechtliche Daten**
- **USt-IdNr. und Steuernummer.**
- **Bankverbindung (IBAN, BIC).**
- **Zahlungsbedingungen** (Zahlungsziel, Skonto).
- **Lieferbedingungen** (Incoterms, Lieferzeit, Mindestbestellmenge).
- **Währung.** Sie ist nur indirekt über "EUR" in der Spaltenüberschrift erkennbar.

**Qualität und Compliance**
- **Bewertungskriterien** zur Note A/B/C: Datum der Bewertung, Begründung, Liefertreue und Qualitätsquote.
- **Zertifizierungen** (z. B. ISO 9001) mit **Gültigkeitsdatum**.
- **Status:** aktiv, gesperrt oder in Prüfung.
- **Lieferantenselbstauskunft oder Vertrag** (vorhanden ja/nein, Datum, Ablauf).

**Verwaltung**
- **Zuständiger Einkäufer** im eigenen Haus.
- **Letzte Änderung und Pflegedatum.** Dann sieht man, wie aktuell der Datensatz ist.
- **Bemerkungen.**
- **Zuordnung von Warengruppe** über eine feste Auswahlliste statt Freitext.
- **Bezugsjahr des Jahresumsatzes.** Das Jahr, auf das sich der Wert bezieht, fehlt.

**Priorität**
Wenn man nur wenig ergänzen will, beginnt man mit:
1. Lieferantennummer
2. Vollständige Adresse (Straße, PLZ, Land)
3. Status
4. USt-IdNr. und Bankverbindung
5. Zahlungsbedingungen
6. Eine saubere Auswahlliste für die Warengruppe

Die Datums-, Zahlen- und Ortsangaben sollten außerdem einheitlich formatiert werden (z. B. Datum als JJJJ-MM-TT).

---

### Modell: Opus

#### Nutzer 1

```
Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.
```

(Anhang: lieferantenliste_unsortiert.csv)

#### Assistent 1

Ich habe die Liste nur gelesen und nichts verändert. Die Datenzeilen zähle ich ab der ersten Zeile nach der Kopfzeile: Zeile 1 ist „Müller Stahlhandel GmbH“, Zeile 27 ist „Schäfer Schweißtechnik“.

**1. Anzahl der Zeilen**

Ohne Kopfzeile hat die Liste **27 Datenzeilen** mit jeweils 9 Spalten: Lieferant, Ansprechpartner, Ort, Telefon, E-Mail, Warengruppe, Letzte Bestellung, Jahresumsatz EUR, Bewertung.
Vier Paare davon sind sehr wahrscheinlich Dubletten (siehe Punkt 3). Dann wären es tatsächlich nur **23 verschiedene Lieferanten**.

**2. Gefundene Probleme**

*a) Datumsformate (Spalte „Letzte Bestellung“)*
In der Spalte stehen mindestens sieben verschiedene Formate:
- TT.MM.JJJJ: 12.03.2024, 14.11.2023 usw.
- ISO-Format JJJJ-MM-TT: 2024-02-28, 2024-03-12, 2024-04-08 usw.
- Kurzform ohne führende Null: 5.1.24, 7.4.2024
- Schrägstriche: 15/01/2024, 03/02/2024. **Achtung:** „03/02/2024“ ist mehrdeutig. Es kann der 3. Februar sein (deutsche Lesart) oder der 2. März (US-Lesart).
- Nur Monat und Jahr, ausgeschrieben: „März 2024“, „April 2024“
- Abgekürzter Monat: „Dez. 2023“
- Leer: Keller Dichtungstechnik

Bei den Einträgen mit nur Monat und Jahr fehlt der genaue Tag. Eine korrekte Sortierung nach Datum ist so nicht möglich.

*b) Zahlenformate (Spalte „Jahresumsatz EUR“)*
- Tausenderpunkt mit Komma: 48.500,00
- Ohne Trennzeichen: 9800, 48500
- Leerzeichen als Tausendertrenner: 31 200 €
- Währung in der Zelle, obwohl sie schon im Spaltennamen steht: „€“ oder „EUR“ (18.400,00 €, 41.000 EUR, 63.200 €, 11.300 EUR)
- Uneinheitliche Nachkommastellen: 22.750,50 und 22750,5
- „12.300“ oder „6.250“ ohne Nachkommastellen kann Excel oder ein anderes Programm je nach Ländereinstellung als 12,3 bzw. 6,25 lesen.
- Kein Wert: „n/a“ (Richter Glas & Optik) und leer (Koch Elektronik)

Summen oder Sortierungen nach Umsatz wären so fehlerhaft.

*c) Schreibweisen bei Orten*
- Musterhausen / musterhausen / MUSTERHAUSEN
- Fiktivhausen / fiktivhausen
- Neustadt a. d. Probe / Neustadt a.d. Probe / Neustadt an der Probe / neustadt a. d. probe

Wer nach Ort filtert, bekommt dadurch unvollständige Ergebnisse.

*d) Schreibweisen bei Firmennamen*
- Umlaut gegen Umschreibung: Müller / Mueller
- „&“ gegen „und“: Schmidt & Söhne / Schmidt und Söhne
- Großbuchstaben: ELEKTRO KRAUSE GmbH
- Rechtsform mal vorhanden, mal nicht: Müller Stahlhandel GmbH / Mueller Stahlhandel; Elektro Krause / … GmbH; Weber Kunststofftechnik / Weber Kunststoff-Technik GmbH

*e) Warengruppen uneinheitlich*
- Elektrokomponenten / Elektro / Elektronik. Unklar ist, ob „Elektronik“ (Koch) eine eigene Gruppe ist.
- Schrauben/Normteile / Normteile
- Kunststoffteile / Kunststoff

*f) Ansprechpartner uneinheitlich*
- Mal mit Anrede, mal ohne: „Herr K. Brandt“ / „K. Brandt“, „Frau Lea Schmidt“ / „Lea Schmidt“
- Abkürzungen: „Hr. Krause“ neben „Herr Krause“
- Titel mal dabei, mal nicht: „Frau Dr. Weber“ / „Dr. Weber“
- Teils nur Nachname, teils mit Vorname oder Initiale

*g) Telefonnummern*
- Unterschiedliche Trennzeichen: „0000 111201“ / „0000-111201“

*h) Bewertung*
- Kleinbuchstaben statt Großbuchstaben: „a“ (Wolf Messtechnik), „b“ (Schäfer Schweißtechnik)

*i) Fehlende Werte (Übersicht)*

| Spalte | Betroffene Lieferanten |
|---|---|
| Ansprechpartner | Lackierwerk Ost GmbH, Schwarz Gießerei |
| Telefon | Becker Werkzeugbau |
| E-Mail | Hoffmann Logistik, Krüger Gummiwaren |
| Letzte Bestellung | Keller Dichtungstechnik |
| Jahresumsatz | Richter Glas & Optik („n/a“), Koch Elektronik (leer) |
| Bewertung | Bauer Präzisionsteile, Keller Dichtungstechnik |

*j) Dubletten*
Es gibt vier wahrscheinliche Dubletten-Paare (Details in Punkt 3).

**3. Mögliche Dubletten mit Begründung**

| # | Eintrag A | Eintrag B | Begründung |
|---|---|---|---|
| 1 | Zeile 1: Müller Stahlhandel GmbH | Zeile 7: Mueller Stahlhandel | Gleiche Telefonnummer (nur „-“ statt Leerzeichen), identische E-Mail, gleicher Ansprechpartner (K. Brandt), gleicher Ort und dieselbe Warengruppe. Das Datum ist gleich (12.03.2024 = 2024-03-12), ebenso Umsatz (48.500,00 = 48500) und Bewertung A. |
| 2 | Zeile 2: Schmidt & Söhne KG | Zeile 10: Schmidt und Söhne KG | Gleiche Telefonnummer, identische E-Mail, gleiche Ansprechpartnerin (Lea Schmidt). Datum (28.02.2024), Umsatz (12.300) und Bewertung B stimmen überein. Nur die Warengruppe ist einmal „Schrauben/Normteile“ und einmal „Normteile“. |
| 3 | Zeile 3: Elektro Krause | Zeile 14: ELEKTRO KRAUSE GmbH | Gleiche Telefonnummer, identische E-Mail, gleicher Ansprechpartner (Herr/Hr. Krause), gleicher Ort in anderer Schreibweise. Datum (5.1.24 = 05.01.2024), Umsatz (31.200) und Bewertung A sind gleich. Die Warengruppe heißt einmal „Elektrokomponenten“, einmal „Elektro“. |
| 4 | Zeile 4: Weber Kunststofftechnik | Zeile 18: Weber Kunststoff-Technik GmbH | Gleiche Telefonnummer, identische E-Mail, gleiche Ansprechpartnerin (Dr. Weber), gleicher Ort. Umsatz (22.750,50 = 22750,5) und Bewertung B sind gleich. Beim Datum steht einmal „März 2024“, einmal „2024-03-01“, was zusammenpasst. |

Bei allen vier Paaren stimmen Telefonnummer und E-Mail-Adresse exakt überein. Das ist das stärkste Indiz. Die Unterschiede liegen nur in der Schreibweise.

**Keine Dubletten**, obwohl es auf den ersten Blick so wirken könnte:
- Keller Dichtungstechnik und Krüger Gummiwaren haben beide die Warengruppe „Dichtungen“. Name, Ort und Telefon sind aber verschieden.
- Hoffmann Logistik und Braun Transporte sind beide „Spedition“, aber verschiedene Firmen.
- Elektro Krause, Fischer Kabelkonfektion, Neumann Sensorik und Koch Elektronik sitzen alle in Neustadt a. d. Probe und sind im Elektro-Bereich tätig. Es sind aber verschiedene Firmen.

Ich würde die vier Dubletten-Paare vor dem Zusammenführen kurz von einer zuständigen Person bestätigen lassen. Danach kann ich die Daten vereinheitlichen, wenn Sie möchten: Datumsformat TT.MM.JJJJ, Zahlen ohne Währungszeichen, einheitliche Orte und Warengruppen.

#### Nutzer 2

```
Welche Spalten fehlen in dieser Liste, die man für eine ordentliche Lieferantenverwaltung bräuchte?
```

#### Assistent 2

Für eine ordentliche Lieferantenverwaltung fehlen vor allem diese Spalten, nach Wichtigkeit gruppiert:

**Unbedingt nötig**
1. **Lieferantennummer / Kreditorennummer**: eine eindeutige ID. Damit wären Dubletten wie oben leichter zu vermeiden, und die Verknüpfung mit Buchhaltung oder ERP wird möglich.
2. **Vollständige Anschrift**, aufgeteilt in Straße und Hausnummer, PLZ, Ort und Land. Bisher gibt es nur den Ort.
3. **Status**: aktiv, inaktiv, gesperrt oder in Prüfung.
4. **Bezugsjahr bzw. Zeitraum des Jahresumsatzes**. Sonst weiß niemand, auf welches Jahr sich „Jahresumsatz“ bezieht.

**Kaufmännisch und rechtlich wichtig**
5. **USt-IdNr.** (bei EU-Lieferanten) bzw. **Steuernummer**
6. **Zahlungsbedingungen**, z. B. „30 Tage netto, 2 % Skonto 10 Tage“
7. **Lieferbedingungen / Incoterms**, z. B. „frei Haus“ oder „DAP“
8. **Währung**, falls auch Lieferanten außerhalb des Euro-Raums dazukommen
9. **Rahmenvertrag ja/nein** mit Vertragsbeginn, Vertragsende und Kündigungsfrist
10. **Bankverbindung (IBAN/BIC)**. Diese gehört meist besser ins Buchhaltungssystem als in eine offene Liste, weil sonst ein Risiko für Betrug und Datenschutz entsteht.

**Einkauf und Qualität**
11. **Zertifizierungen** mit Ablaufdatum, z. B. ISO 9001, ISO 14001, IATF 16949
12. **Durchschnittliche Lieferzeit** und **Mindestbestellwert / Mindestmenge**
13. **Bewertungsdatum und Bewertungskriterien**. Eine Bewertung „A“ sagt wenig, wenn man nicht weiß, wann und wonach bewertet wurde, z. B. Qualität, Liefertreue, Preis.
14. **Strategische Einstufung**, z. B. Hauptlieferant / Ersatzlieferant oder „kritisch / nicht kritisch“
15. **Alternativlieferant**: Wer kann einspringen, wenn dieser Lieferant ausfällt?

**Kontakt**
16. Den Ansprechpartner **in einzelne Spalten aufteilen**: Anrede, Titel, Vorname, Nachname. Das hätte auch die uneinheitlichen Einträge wie „Hr. Krause“ und „Herr Krause“ verhindert.
17. **Funktion / Abteilung** des Ansprechpartners, z. B. Vertrieb oder Innendienst
18. **Mobilnummer** und ein **zweiter Ansprechpartner** als Vertretung
19. **Website**
20. **Interner Ansprechpartner**: Wer im eigenen Haus ist für den Lieferanten zuständig?

**Pflege und Nachvollziehbarkeit**
21. **Angelegt am / geändert am / geändert von**
22. **Bemerkungen / Notizen**

Zwei Hinweise zur bestehenden Struktur:
- Für **Warengruppe** und **Ort** sollte man feste Auswahllisten verwenden (z. B. per Dropdown in Excel). Dann entstehen keine Varianten wie „Elektro“ und „Elektrokomponenten“.
- Bei personenbezogenen Kontaktdaten sollte man darauf achten, dass die Liste nur für berechtigte Personen zugänglich ist (Datenschutz/DSGVO).

Wenn Sie möchten, kann ich Ihnen eine Vorlage mit allen Spalten als Kopfzeile im gleichen CSV-Format erstellen.
