# Testlauf: Folie 18 – Live-Demo: Prüfbericht hochladen und zusammenfassen

**Herkunft:** [Folie 18 – Die KI liest für dich mit](../04_Folien.md) (Sprechernotiz „Live-Demo“), Material [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md), Abgleich mit [Trainer-Lösungshinweise, Station A](../06_Uebungen/Trainer-Loesungshinweise.md)

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompts (im selben Chat, Datei mit Turn 1 hochgeladen):**

1. `Fasse den Bericht in 5 Stichpunkten zusammen. Nenne danach die 3 wichtigsten Risiken oder Fristen.`
2. `Auf welcher Seite / in welchem Abschnitt steht das?`

**Ziel laut Material:** Datei hochladen, Zusammenfassung erhalten, dann Kontrollfrage nach der Fundstelle und im Original nachsehen. Botschaft: „Zusammenfassungen sind meistens gut. Aber manchmal lässt die KI etwas Wichtiges weg oder vermischt Details.“

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Genau 5 Stichpunkte + 3 Risiken | ja | ja | ja (plus ungefragter Zusatzhinweis) |
| Empfehlung „Abnahme unter Vorbehalt“ | ja | ja | ja |
| Drei Bedingungen des Vorbehalts | ja | ja | ja |
| Einbehalt 5 % | ja | ja | ja |
| Schlusszahlung 30 % / Gefahrübergang | **nein** – fehlt | ja | ja |
| Taktzeit C 41 s (≤ 40 s) | ja | ja | ja |
| Leistungsaufnahme 31 kW vs. < 30 kW, inkl. Absaugung | ja | ja | ja |
| Staub 92 %, Wiederholungsmessung | ja | ja | ja |
| Update 4.3 ohne Termin | ja | ja (zitiert „im Laufe des Quartals“) | ja |
| Schulung nur 2 Bediener | **nein** – fehlt | ja | ja |
| Schutzglas: 2 auf Lager, 3–6 Wochen Lieferzeit | ja | ja | ja |
| Altanlage ohne Wartungsvertrag (Bonus) | nein | nein | ja |
| Widerspruch Schlitzbreite 0,13 mm > ±0,10 mm (Bonus) | nein – übernimmt „alle Maße in Toleranz“ | nein – übernimmt „alle Prüfmaße in Toleranz“ | **ja, von selbst gefunden** |
| Kein erfundener Termin für Update 4.3 | ja | ja | ja |
| Kein Eurobetrag für Einbehalt/Kaufpreis | ja | ja | ja |
| Turn 2: sagt ehrlich „keine Seitenzahlen“ | ja | ja | ja |
| Turn 2: Abschnittsangaben stimmen | ja | fast – ein Absatz falsch | ja, sehr genau (Absatz-Ebene) |
| Länge für Live-Demo (3–4 Min.) | passend | passend | lang (Tabellen, Zusatzhinweis) |
| **Gesamt** | gut, aber lückenhaft | **sehr gut** | sehr gut, findet sogar den Tabellenfehler |

## Gefundene Fehler mit Beleg

1. **„Alle Maße in Toleranz“ ungeprüft übernommen** (Haiku, Sonnet). Haiku: „Bei allen drei Prüfteilen liegen die Maße innerhalb der Toleranz.“ Sonnet: „Alle Prüfmaße der drei Prüfteile liegen innerhalb der Toleranz.“ Laut Tabelle in Abschnitt 4 (Zeile „B – Seitenwand 3 mm | Schlitzbreite“) beträgt die größte Abweichung **0,13 mm** bei einer Toleranz von **±0,10 mm** – trotzdem „i. O.“. Nachgerechnet per Skript über alle 12 Zeilen: nur diese Zeile überschreitet die Toleranz. Die Modelle glauben dem Text (Abschnitt 7), statt die Tabelle nachzurechnen – genau der in den Lösungshinweisen beschriebene Effekt. Opus dagegen meldet den Widerspruch ungefragt und korrekt (Mittelwert 4,07 mm liegt in der Toleranz, die Einzelabweichung nicht).
2. **Wichtiges weggelassen** (Haiku). Die Schlusszahlung von 30 % und der Gefahrübergang mit der Abnahme (Abschnitt 1, 2. Absatz) fehlen. Haiku erwähnt den 5-%-Einbehalt „von der Schlusszahlung“, sagt aber nicht, dass und in welcher Höhe sie mit der Abnahme fällig wird. Ebenso fehlt die Schulungslücke (nur 2 Bediener, mind. 2 weitere nötig, nicht im Vertrag – Abschnitt 3.6, 3. Absatz). Das ist genau die Lehre der Folie: „lässt manchmal etwas Wichtiges weg“.
3. **Falsche Fundstelle** (Sonnet, Turn 2): „Software-Update 4.3: Abschnitt 3.6 (vorletzter Absatz)“. Abschnitt 3.6 hat vier Absätze (Bedienoberfläche, Betriebsanleitung/Wartungsplan, Herstellerschulung, Steuerungssoftware); das Update steht im **letzten** Absatz. Kleiner Fehler, aber ein schönes Beispiel dafür, dass auch Fundstellen nachgeprüft werden müssen. Opus nennt hier korrekt „letzter Absatz“.
4. **Ungenauigkeit „45 % schneller“** (Opus): „Insgesamt geht die Bearbeitung etwa 45 % schneller als bisher.“ Im Bericht (3.2) steht „Verkürzung der Bearbeitungszeit um rund 45 %“. 45 % weniger Zeit entspricht rechnerisch dem 1,82-fachen Tempo (1/0,55), also rund 82 % schneller. Umgangssprachlich verständlich, fachlich aber nicht dasselbe. Sonnet formuliert korrekt „rund 45 % kürzere Bearbeitungszeit“.
5. **Eigene Schlussfolgerung als Risiko** (Opus): „Vorbehalt und 5 % Einbehalt müssen deshalb **vor** der Abnahme schriftlich vereinbart sein, sonst gibt es kaum noch ein Druckmittel.“ Im Bericht steht nur, der Vorbehalt solle schriftlich festgehalten werden (Abschnitt 7). Die Einschätzung zum Zeitpunkt und zum „Druckmittel“ ist plausibel, aber eine Interpretation des Modells (quasi Rechtsrat), nicht Inhalt des Berichts – beim Vorlesen als solche kennzeichnen.
6. Kleinigkeit (Opus): „Stillstände kamen vor allem von verschmutzten Schutzgläsern und einem falsch justierten Endschalter“ – nach Dauer war der Endschalter (2 h 10 min) die größere Ursache als die Schutzgläser (35 + 20 = 55 min). Nicht falsch, aber die Reihenfolge suggeriert eine andere Gewichtung.

**Geprüft und korrekt:** Alle Zahlen stimmen mit dem Bericht überein (82/95 s, 64/70 s, 41/40 s, 96,2 %/95 %, 31 kW/< 30 kW, 92 %, 60 % weniger Energie, 85.000 €/Jahr, 2 Schutzgläser, 3–6 Wochen, 3 Monate). Haikus „zwei Stillstände … insgesamt 55 Minuten“ ist richtig (35 + 20). Verfügbarkeit nachgerechnet: (80 h − 185 min) / 80 h = 96,15 % ≈ 96,2 %. **Kein Modell erfindet einen Termin für Update 4.3 oder einen Eurobetrag für Kaufpreis/Einbehalt.** Auf die Seitenfrage reagieren alle drei ehrlich („keine Seitenzahlen, nur Abschnitte“) – keine erfundenen Seitenzahlen.

## Lehren für die Auswertung

- **Die Demo funktioniert, aber der „Fehler“ ist subtil.** Die Zusammenfassungen sind durchweg gut und zahlengenau. Der Lerneffekt entsteht erst beim Vergleich: Was fehlt (Haiku: 30 %, Schulung) und was wurde dem Text geglaubt (Haiku/Sonnet: „alle Maße in Toleranz“)? Trainer sollte die Kernfakten-Tabelle aus den Lösungshinweisen bereithalten und gezielt einen Punkt im Original zeigen.
- **Beste Live-Kontrolle:** Nicht nur nach der Fundstelle fragen, sondern eine Aussage tatsächlich im Original aufschlagen. Ideal: Sonnets „vorletzter Absatz“ – im Original zeigen, dass es der letzte ist. Oder die Zeile Schlitzbreite in Abschnitt 4 zeigen: „Hier steht 0,13 bei ±0,10 – und die KI sagt ‚alles in Toleranz‘.“
- **Die Seitenfrage führt bei einer .md-Datei ins Leere.** Alle Modelle antworten korrekt „keine Seiten“. Für den Halluzinationseffekt ist die Frage hier also kaum geeignet; gute Tools erfinden keine Seitenzahlen. Das ist selbst eine schöne Lehre („die KI sagt ehrlich, was sie nicht weiß“) – aber nicht die angekündigte.
- **Stärkere Modelle prüfen mehr:** Opus findet den Tabellenwiderspruch von selbst. Das kann man zeigen, sollte aber betonen: Darauf verlassen kann man sich nicht – zwei von drei Modellen haben es übernommen.
- **Interpretation vs. Inhalt:** Opus ergänzt eigene Ratschläge („vor der Abnahme vereinbaren“). Gut für die Frage: „Steht das im Bericht oder denkt die KI weiter?“
- **Zeit:** Opus' Antwort (Tabellen + Zusatzhinweis) ist für 3–4 Minuten zu lang zum Vorlesen; nur überfliegen und zwei Stellen gezielt prüfen.
- **Bonus-Prompt, falls der Fehler nicht auftritt:** „Überprüfe die Messwerttabelle in Abschnitt 4: Liegen alle Abweichungen wirklich innerhalb der Toleranz? Rechne jede Zeile einzeln nach.“ (steht bereits in den Lösungshinweisen) – oder „Wie viel Euro behalten wir ein?“ als Halluzinations-Test (Kaufpreis steht nicht im Bericht).

## Gesprächsprotokolle

### Haiku

#### Nutzer 1
Fasse den Bericht in 5 Stichpunkten zusammen. Nenne danach die 3 wichtigsten Risiken oder Fristen.

#### Assistent 1
**Zusammenfassung in 5 Stichpunkten**

- **Gegenstand:** Die Faserlaser-Schneidanlage LS-3015 in Halle 3 ersetzt die CO₂-Altanlage. Der Bericht (PB-2024-017, Entwurf) bewertet, ob die Anlage Lastenheft und Kaufvertrag erfüllt.
- **Schnittqualität und Maße:** Bei allen drei Prüfteilen liegen die Maße innerhalb der Toleranz. Die Kanten sind gratfrei, bei Baustahl (8 mm) gab es Bartbildung, die sich durch Parameteranpassung reduzieren ließ.
- **Taktzeiten:** Teil A (82 s, Grenze 95 s) und Teil B (64 s, Grenze 70 s) sind erfüllt. Teil C liegt mit 41 s knapp über der Vorgabe von 40 s.
- **Verfügbarkeit und Energie:** Die Verfügbarkeit im Dauerlauf beträgt 96,2 % (gefordert 95 %). Die Leistungsaufnahme im Schneidbetrieb liegt bei 31 kW inklusive Absaugung und damit knapp über der Angebotsgrenze von unter 30 kW.
- **Empfehlung:** Die Fertigungstechnik empfiehlt, die Anlage unter Vorbehalt abzunehmen. Der Vorbehalt umfasst das Software-Update 4.3, die Ergänzung des Wartungsplans und eine separate Leistungsmessung. Vorgeschlagen wird ein Einbehalt von 5 % des Kaufpreises von der Schlusszahlung. Die geschätzte Ersparnis liegt bei rund 85.000 Euro pro Jahr.

**Die 3 wichtigsten Risiken oder Fristen**

1. **Software-Update 4.3 ohne Termin:** Das Update behebt einen Fehler bei der Übergabe von Auftragsdaten aus dem ERP-System. Bis dahin müssen Schneidprogramme teils manuell übertragen werden. Ein verbindlicher Termin fehlt noch und ist Teil des Vorbehalts (Abschnitt 3.6 und Abschnitt 7).
2. **Staubkonzentration bei verzinktem Blech:** Der Messwert liegt bei 92 % des internen Richtwerts. Die Messung erfolgte bei geschlossener Hallentür. Die Wiederholungsmessung soll nach drei Monaten stattfinden, die Fachkraft für Arbeitssicherheit hat die Anlage nur vorläufig freigegeben (Abschnitt 3.4).
3. **Schutzglas-Verschleiß und Ersatzteile:** Bei verzinktem Material muss das Schutzglas häufiger gewechselt werden als im Standardplan vorgesehen. Es gab zwei Stillstände wegen verschmutzter Schutzgläser (insgesamt 55 Minuten). Auf Lager sind nur zwei Stück, die Lieferzeit beträgt laut Hersteller drei bis sechs Wochen (Abschnitt 3.3).

#### Nutzer 2
Auf welcher Seite / in welchem Abschnitt steht das?

#### Assistent 2
Das Dokument hat keine Seitenzahlen, daher verweise ich auf die Abschnittsnummern im Bericht:

- **Software-Update 4.3 und fehlender Termin:** Abschnitt 3.6 (Bedienung, Dokumentation und Schulung). Die Empfehlung dazu steht in Abschnitt 7.
- **Staubkonzentration (92 %) und Wiederholungsmessung:** Abschnitt 3.4 (Arbeitssicherheit und Absaugung).
- **Schutzglas-Wechsel und Lieferzeit:** Abschnitt 3.3 (Verfügbarkeit im Dauerlauf). Der fehlende Hinweis im Wartungsplan steht in Abschnitt 3.6.

Die Zahlen für die Taktzeit von Prüfteil C stehen in Abschnitt 3.2 und in der Tabelle in Abschnitt 4. Die Leistungsaufnahme steht in Abschnitt 3.5 und in der Tabelle in Abschnitt 4.

### Sonnet

#### Nutzer 1
Fasse den Bericht in 5 Stichpunkten zusammen. Nenne danach die 3 wichtigsten Risiken oder Fristen.

#### Assistent 1
**Zusammenfassung in 5 Stichpunkten**

- **Zweck:** Der Abnahmeprüfbericht PB-2024-017 (Entwurf) bewertet die neue Faserlaser-Schneidanlage LS-3015 in Halle 3, die die alte CO₂-Anlage von 2009 ersetzt. Die Geschäftsführung soll auf dieser Basis über die Abnahme entscheiden. Mit der Abnahme geht die Gefahr über, und die Schlusszahlung von 30 % des Kaufpreises wird fällig.
- **Qualität und Takt:** Alle Prüfmaße der drei Prüfteile liegen innerhalb der Toleranz. Die Kanten sind sehr gut. Bei Prüfteil C (8 mm) gab es leichte Bartbildung, die mit einem optimierten Parametersatz deutlich reduziert wurde. Die Taktzeiten von Teil A (82 s) und Teil B (64 s) sind besser als zugesichert. Teil C liegt mit 41 s knapp über den zugesicherten 40 s.
- **Verfügbarkeit:** Im fünftägigen Dauerlauf lag die technische Verfügbarkeit bei 96,2 % (gefordert: 95 %). Die ungeplanten Stillstände waren ein falsch justierter Endschalter am Palettenwechsler und zweimal ein verschmutztes Schutzglas.
- **Sicherheit und Energie:** Laserschutz und Not-Halt sind in Ordnung. Beim Schneiden von verzinktem Blech lag die Staubkonzentration bei 92 % des Richtwerts, und die Wiederholungsmessung steht noch aus. Die Leistungsaufnahme beträgt 31 kW statt "unter 30 kW" im Angebot, wobei die Absaugung mitgemessen wurde. Gegenüber der Altanlage ist der Verbrauch rund 60 % niedriger.
- **Wirtschaftlichkeit und Empfehlung:** Die Fertigungstechnik erwartet etwa 85.000 Euro Ersparnis pro Jahr und rund 45 % kürzere Bearbeitungszeit. Sie empfiehlt eine Abnahme unter Vorbehalt. Der Hersteller soll Software-Update 4.3 liefern, den Wartungsplan ergänzen und die Leistung ohne Absaugung getrennt messen. Bis dahin soll 5 % des Kaufpreises einbehalten werden.

**Die 3 wichtigsten Risiken und Fristen**

1. **Software-Update 4.3 ohne Termin:** Bis zum Update müssen Schneidprogramme teilweise manuell vom ERP übertragen werden. Der Hersteller hat nur "im Laufe des Quartals" genannt. Deshalb fordert die Empfehlung einen verbindlichen Termin.
2. **Staubbelastung bei verzinktem Blech:** Der Wert liegt mit 92 % knapp unter dem Richtwert und wurde nur bei geschlossener Hallentür gemessen. Die Wiederholungsmessung im Sommer mit offenen Toren steht aus. Die Arbeitssicherheit hat die Anlage nur vorläufig freigegeben und verlangt eine Wiederholung nach drei Monaten. Eventuell muss die Absaugung verstärkt werden.
3. **Schutzglas-Ersatzteile und Personal:** Verzinktes Material verlangt häufigere Schutzglaswechsel als im Wartungsplan vorgesehen. Es liegen nur 2 Stück auf Lager, und die Lieferzeit beträgt 3 bis 6 Wochen. Zudem sind nur zwei Bediener geschult. Für Vertretung oder eine zweite Schicht braucht es mindestens zwei weitere, und diese Schulung ist nicht im Kaufvertrag enthalten.

#### Nutzer 2
Auf welcher Seite / in welchem Abschnitt steht das?

#### Assistent 2
Der Text ist eine Markdown-Datei ohne Seitenzahlen. Ich kann deshalb nur die Abschnitte nennen.

**Zusammenfassung**
- Zweck, Abnahme und Schlusszahlung: Abschnitt 1 (Anlass und Ziel der Prüfung)
- Qualität und Takt: Abschnitt 3.1 und 3.2, Messwerte in Abschnitt 4
- Verfügbarkeit: Abschnitt 3.3
- Sicherheit und Energie: Abschnitt 3.4 und 3.5, Kennwerte in der zweiten Tabelle in Abschnitt 4
- Wirtschaftlichkeit und Empfehlung: Abschnitt 5 (Wirtschaft) und Abschnitt 7 (Empfehlung, Vorbehalt, 5 % Einbehalt)

**Risiken und Fristen**
1. Software-Update 4.3: Abschnitt 3.6 (vorletzter Absatz). Die Forderung nach einem verbindlichen Termin steht in Abschnitt 7.
2. Staubkonzentration: Abschnitt 3.4. Die Zahl 92 % steht auch in der Tabelle in Abschnitt 4.
3. Schutzglas und Schulung: Schutzglas, Lagerbestand und Lieferzeit stehen in Abschnitt 3.3 (letzter Absatz). Der fehlende Eintrag im Wartungsplan steht in Abschnitt 3.6. Die Schulung steht ebenfalls in Abschnitt 3.6 (Absatz zur Herstellerschulung).

### Opus

#### Nutzer 1
Fasse den Bericht in 5 Stichpunkten zusammen. Nenne danach die 3 wichtigsten Risiken oder Fristen.

#### Assistent 1
**Zusammenfassung des Abnahmeprüfberichts LS-3015 (PB-2024-017, Entwurf)**

1. **Worum es geht:** Die neue Faserlaser-Schneidanlage LS-3015 ersetzt in Halle 3 die alte CO₂-Anlage von 2009. Die Prüfung soll zeigen, ob die Zusagen aus Lastenheft und Kaufvertrag erfüllt sind. Auf dieser Grundlage entscheidet die Geschäftsführung über die Abnahme. Mit der Abnahme geht die Gefahr auf Nordlicht Technik über und die Schlusszahlung von 30 % des Kaufpreises wird fällig.
2. **Qualität und Tempo:** Alle Maße liegen laut Bericht innerhalb der Toleranz. Bei Prüfteil C (8 mm Baustahl) gab es leichte Bartbildung, die durch neue Parameter verringert wurde. Die Taktzeiten von A (82 s statt max. 95 s) und B (64 s statt max. 70 s) sind klar besser als zugesichert. C verfehlt die Zusage knapp (41 s statt 40 s). Insgesamt geht die Bearbeitung etwa 45 % schneller als bisher.
3. **Verfügbarkeit und Sicherheit:** Im Dauerlauf erreichte die Anlage 96,2 % Verfügbarkeit (gefordert sind mindestens 95 %). Die Stillstände kamen vor allem von verschmutzten Schutzgläsern und einem falsch justierten Endschalter. Laserschutz, Türverriegelungen und Not-Halt funktionieren. Beim Schneiden von verzinktem Blech erreicht der Staub aber 92 % des internen Richtwerts.
4. **Energie und Wirtschaftlichkeit:** Die Anlage verbraucht rund 60 % weniger Energie als die Altanlage. Im Schneidbetrieb wurden 31 kW gemessen, zugesagt waren unter 30 kW. Dabei wurde die Absaugung mitgemessen, eine getrennte Messung fehlt. Die geschätzte Ersparnis liegt bei etwa 85.000 € pro Jahr. Nicht eingerechnet sind Kosten für weitere Schulungen, eine stärkere Absaugung und den höheren Verbrauch an Schutzgläsern.
5. **Empfehlung:** Die Anlage soll **unter Vorbehalt abgenommen** werden. Der Hersteller soll (1) das Software-Update 4.3 zu einem verbindlichen Termin liefern, (2) den Wartungsplan um das Wechselintervall der Schutzgläser ergänzen und (3) die Leistungsaufnahme ohne Absaugung messen. Bis dahin sollen 5 % des Kaufpreises von der Schlusszahlung einbehalten werden.

**Die 3 wichtigsten Risiken bzw. Fristen**

1. **Abnahme und Zahlung:** Mit der Abnahme gehen die Gefahr und die Pflicht zur Schlusszahlung von 30 % über. Vorbehalt und 5 % Einbehalt müssen deshalb **vor** der Abnahme schriftlich vereinbart sein, sonst gibt es kaum noch ein Druckmittel. Dazu passt: Für das Update 4.3 gibt es bisher **keinen festen Termin**, nur „im Laufe des Quartals“. Bis dahin müssen Schneidprogramme wegen eines Fehlers in der ERP-Schnittstelle teilweise von Hand übertragen werden.
2. **Staub und Arbeitssicherheit (Frist: Wiederholungsmessung nach 3 Monaten):** Bei verzinktem Blech liegt der Staub schon bei 92 % des Richtwerts. Gemessen wurde nur bei geschlossener Hallentür, die Messung im Sommer mit offenen Toren fehlt noch. Die Freigabe durch die Fachkraft für Arbeitssicherheit ist nur vorläufig.
3. **Schutzgläser und Ausfallrisiko:** Bei verzinktem Material müssen die Schutzgläser öfter gewechselt werden als geplant. Es sind nur 2 Stück auf Lager, und die Lieferzeit beträgt 3 bis 6 Wochen. Das kann zu Stillständen führen. Die Altanlage dient zwar als Reserve, hat aber keinen Wartungsvertrag. Dazu kommt: Nur zwei Bediener sind geschult, für Vertretung und eine zweite Schicht fehlen mindestens zwei weitere.

**Hinweis zur Tabelle:** Bei Prüfteil B, Maß „Schlitzbreite“, steht als größte Abweichung 0,13 mm. Erlaubt sind aber ±0,10 mm. Trotzdem ist das Maß mit „i. O.“ bewertet. Der Mittelwert (4,07 mm) liegt zwar in der Toleranz, einzelne Teile offenbar aber nicht. Das sollte vor der Freigabe geklärt werden, weil der Bericht ausdrücklich sagt, alle Maße seien in Toleranz.

#### Nutzer 2
Auf welcher Seite / in welchem Abschnitt steht das?

#### Assistent 2
Seitenzahlen kann ich leider nicht nennen. Die hochgeladene Datei ist ein reines Textdokument ohne Seiteneinteilung. Die Seiten hängen davon ab, wie das Dokument gedruckt oder als PDF erzeugt wird. Die Abschnitte kann ich aber genau angeben:

**Zusammenfassung**

| Punkt | Fundstelle |
|---|---|
| 1. Anlass, Abnahme, Gefahrübergang, 30 % Schlusszahlung | Abschnitt 1 „Anlass und Ziel der Prüfung“ (2. Absatz) |
| 2. Schnittqualität, Bartbildung bei C | Abschnitt 3.1 |
| 2. Maße in Toleranz | Abschnitt 3.1 und Tabelle in Abschnitt 4 |
| 2. Taktzeiten A/B/C, rund 45 % schneller | Abschnitt 3.2 und Kennwerttabelle in Abschnitt 4 |
| 3. Verfügbarkeit 96,2 %, Stillstände | Abschnitt 3.3 |
| 3. Laserschutz, Not-Halt, Staub 92 % | Abschnitt 3.4 |
| 4. Energie (31 kW, rund 60 % weniger) | Abschnitt 3.5 |
| 4. Ersparnis 85.000 €/Jahr, nicht eingerechnete Kosten | Abschnitt 5 „Wirtschaftliche Betrachtung“ |
| 5. Empfehlung: Abnahme unter Vorbehalt, 3 Bedingungen, 5 % Einbehalt | Abschnitt 7 „Zusammenfassung und Empfehlung“ (Absatz „Empfehlung“) |

**Risiken und Fristen**

| Risiko/Frist | Fundstelle |
|---|---|
| Gefahrübergang und Schlusszahlung bei Abnahme | Abschnitt 1, 2. Absatz |
| Vorbehalt und 5 % Einbehalt | Abschnitt 7, Absatz „Empfehlung“ |
| Update 4.3 ohne festen Termin, Programme von Hand übertragen | Abschnitt 3.6, letzter Absatz |
| Staub 92 %, Sommermessung fehlt | Abschnitt 3.4, 2. Absatz; Kennwerttabelle in Abschnitt 4 |
| Wiederholungsmessung nach 3 Monaten | Abschnitt 3.4, letzter Satz |
| Schutzgläser: 2 auf Lager, Lieferzeit 3 bis 6 Wochen | Abschnitt 3.3, letzter Absatz |
| Wartungsplan ohne erhöhtes Wechselintervall | Abschnitt 3.6, 2. Absatz |
| Altanlage als Reserve ohne Wartungsvertrag | Abschnitt 5, letzter Absatz |
| Nur 2 Bediener geschult | Abschnitt 3.6, 3. Absatz |

**Hinweis zur Schlitzbreite:** Das steht in der Tabelle in Abschnitt 4, Zeile „B – Seitenwand 3 mm | Schlitzbreite“ (0,13 mm Abweichung bei ±0,10 mm Toleranz, trotzdem „i. O.“). Die Abweichung wird im Bericht selbst nicht erwähnt. Ich habe sie beim Vergleich der Tabellenwerte gefunden.

Für echte Seitenzahlen gleichen Sie die Abschnitte am besten mit Ihrer gedruckten oder PDF-Fassung ab. Wenn Sie die PDF hochladen, nenne ich Ihnen auch die Seiten.
