# Testlauf: Übung 3 / Station A Trainer-Prüfprompts – Fundstellen und Messwerttabelle nachrechnen

**Herkunft:** [Trainer-Lösungshinweise, Übung 3, Station A – Musterprompts „Zusätzlich gut für die Prüfung“](../06_Uebungen/Trainer-Loesungshinweise.md), Übungsblatt [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md) (Station A, Basis-Prompt), Material [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md)

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompts (im selben Chat, Bericht mit Turn 1 angehängt):**

1. Basis-Prompt aus dem Übungsblatt („… in genau 5 Sätzen für die Geschäftsführung …“)
2. `Nenne zu jeder Aussage deiner Zusammenfassung den Abschnitt im Bericht, aus dem sie stammt.`
3. `Überprüfe die Messwerttabelle in Abschnitt 4: Liegen alle Abweichungen wirklich innerhalb der Toleranz? Rechne jede Zeile einzeln nach.`

**Ziel laut Material:** Jede Aussage der Zusammenfassung ist einem Abschnitt zugeordnet. Beim Nachrechnen der Messwerttabelle wird der versteckte Widerspruch gefunden: Prüfteil B, Schlitzbreite, Toleranz ±0,10 mm, größte Abweichung 0,13 mm, trotzdem „i. O.“. Das widerspricht Abschnitt 7.

**Nachgerechnet (per Python-Skript, alle 12 Zeilen):** Nur die Zeile „B – Seitenwand 3 mm | Schlitzbreite“ liegt außerhalb (0,13 > 0,10). Alle Mittelwert-Abweichungen (+0,03, −0,02, +0,01, +0,04, +0,04, +0,02, +0,07, +0,01, +0,06, −0,05, −0,09, +0,08) liegen innerhalb. Verfügbarkeit: (4.800 − 185) / 4.800 = 96,146 %. Auf eine Nachkommastelle gerundet sind das **96,1 %**. Der Bericht nennt „rund 96,2 %“ (siehe Fehler 5).

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Turn 1: genau 5 Sätze | ja | **nein** – 5 Nummern, aber 7 Sätze | **nein** – 5 Nummern, aber 8 Sätze |
| Turn 1: Abnahme unter Vorbehalt + 5 % Einbehalt | ja | ja | ja |
| Turn 1: drei Bedingungen des Vorbehalts | nein | ja | ja |
| Turn 1: Schlusszahlung 30 % / Gefahrübergang | ja | ja | ja |
| Turn 1: offene Punkte (Taktzeit C, Leistung, Staub, Wartungsplan, Update, Schulung) | 5 von 6 (Wartungsplan fehlt) | 5 von 6 (Schulung weiterer Bediener fehlt, nur als Kostenposten) | 6 von 6 |
| Turn 1: Schutzglas-Lieferzeit (Bonus) | nein | nein | ja |
| Turn 1: Schlitzbreite schon erwähnt | ja (siehe Hinweis zum Testaufbau) | nein – „Maßhaltigkeit innerhalb der Toleranz“ übernommen | nein – übernommen, aber vorsichtig („sollen … liegen“) |
| Turn 1: kein erfundener Eurobetrag/Termin | ja | ja | ja |
| Turn 2: jede Aussage einem Abschnitt zugeordnet | ja | ja | ja |
| Turn 2: Abschnittsangaben stimmen (Stichprobe) | fast – „Bewertung“ der Maßhaltigkeit fälschlich auch 3.1 zugeordnet | fast – „Messwerte in Abschnitt 3.1“ (dort steht nur die Toleranzregel) | ja, alle geprüften Angaben korrekt |
| Turn 2: Vorgriff auf Turn 3 („siehe Antwort 3“) | ja (Artefakt) | nein | ja (Artefakt) |
| Turn 3: Schlitzbreite B als außerhalb erkannt | ja | ja | ja |
| Turn 3: Widerspruch zu Abschnitt 7 benannt | ja | ja | ja |
| Turn 3: übrige 11 Zeilen korrekt | ja | ja | ja |
| Turn 3: Rechenweg sichtbar | Ergebnisspalten | ja (Soll − Ist ausgeschrieben) | ja (inkl. „0,13 > 0,10“) |
| Turn 3: Zusammenfassung selbst korrigiert | ja | ja | ja |
| Turn 3: Folge für Entscheidung benannt | ja | ja (Nachmessung vorschlagen) | ja, am besten (fehlt im Vorbehalt, konkrete Rückfragen) |
| Zusatzbeobachtung | weist auf unklare Spalte „Größte Abweichung“ hin | rechnet Verfügbarkeit nach, rundet aber falsch (96,2 statt 96,1 %) | – |
| **Gesamt** | gut; Turn 3 sehr gut, Turn 1 lückenhaft | gut; Satzvorgabe verletzt | **sehr gut**; Satzvorgabe verletzt |

## Gefundene Fehler mit Beleg

1. **Satzvorgabe „genau 5 Sätze“ verletzt** (Sonnet, Opus). Beide nummerieren fünf Punkte, packen aber mehrere Sätze hinein. Sonnet Punkt 1: „… (gefordert: 95 %). Knapp verfehlt bzw. ungeklärt sind …“, Punkt 2 hat ebenfalls zwei Sätze, macht zusammen 7 Sätze. Opus: Punkte 2, 4 und 5 haben je zwei Sätze, macht zusammen 8 Sätze. Haiku hält die Vorgabe exakt ein (5 sehr lange Schachtelsätze). Das ist der Stolperstein aus den Lösungshinweisen („Mehr als 5 Sätze oder sehr lange Schachtelsätze“). Beide Varianten kommen vor.
2. **„Maßhaltigkeit innerhalb der Toleranz“ aus Abschnitt 7 übernommen** (Sonnet, Opus in Turn 1). Sonnet: „Die Maßhaltigkeit wird im Bericht als innerhalb der Toleranz bewertet“. Opus: „Schnittqualität und Maßhaltigkeit sollen bei allen drei Prüfteilen innerhalb der Toleranz liegen“. Laut Tabelle in Abschnitt 4 stimmt das für die Schlitzbreite (0,13 mm bei ±0,10 mm) nicht. Beide schwächen ab („im Bericht bewertet“, „sollen“), korrigieren sich aber erst in Turn 3.
3. **Abschnittszuordnung leicht ungenau** (Haiku, Sonnet). Haiku schreibt in Turn 2: „Abschnitt 3.1 (Bewertung und Toleranzregel)“ und „Die Aussage über die Toleranz stammt aus 3.1 und 7“. In 3.1 steht aber nur die Toleranzregel und der Verweis auf die Tabelle, keine Bewertung „innerhalb der Toleranz“. Die steht nur in Abschnitt 7 (und als „i. O.“ in der Tabelle). Sonnet schreibt: „Messwerte in Abschnitt 3.1 und 4“. In 3.1 stehen keine Messwerte, nur in 4. Alle anderen geprüften Angaben stimmen (z. B. Verfügbarkeit 3.3/4, Ersparnis 5, Gefahrübergang und 30 % in Abschnitt 1, Empfehlung und 5 % in Abschnitt 7, Update 4.3 und Schulung in 3.6, Schutzglas 3.3, Energie −60 % in 3.5).
4. **Unvollständige offene Punkte in Turn 1.** Haiku nennt den Wartungsplan nicht und auch nicht die drei Bedingungen des Vorbehalts. Sonnet erwähnt die Schulung weiterer Bediener nicht als offenen Punkt (nur „Kosten für zusätzliche Schulungen“ aus Abschnitt 5). Opus deckt alle sechs Pflichtpunkte ab.
5. **Rundungsfehler bei der Verfügbarkeit** (Sonnet, Nebenbemerkung Turn 3, und Bericht selbst). Sonnet: „(4.800 − 185) / 4.800 ≈ 96,2 %“. Tatsächlich sind es 96,146 %, also auf eine Nachkommastelle **96,1 %**. Der Fehler steckt schon im Bericht (Abschnitt 3.3: „rund 96,2 %“). Sonnet hat beim Nachrechnen die Zahl des Berichts bestätigt statt sie zu prüfen. Inhaltlich ist das ohne Folgen (≥ 95 % bleibt erfüllt). Es ist aber ein hübsches Beispiel für „die KI rechnet nach und kommt zufällig auf die Zahl, die im Text steht“.
6. **Unbelegte Einschätzung** (Haiku, Turn 3): „Die Empfehlung zur Abnahme unter Vorbehalt bleibt davon unberührt“. Das steht nicht im Bericht, sondern ist eine eigene Wertung. Unkritisch, weil Haiku direkt danach empfiehlt, die Schlitzbreite vor der Abnahme zu klären.
7. **Kein Fehler, aber berechtigter Einwand** (Haiku, Turn 3): Die Spalte „Größte Abweichung“ ist im Bericht nicht definiert (Abweichung vom Sollmaß oder vom Mittelwert?). Haiku legt die naheliegende Lesart offen. Die Lösungshinweise setzen stillschweigend „vom Sollmaß“ voraus.

**Hinweis zum Testaufbau:** Haiku (Turn 2: „Details in Antwort 3“) und Opus (Turn 2: „Diese Aussage halte ich nach dem Nachrechnen nicht mehr für richtig, siehe meine Antwort zur Messwerttabelle“) verweisen schon in Turn 2 auf eine Antwort, die erst in Turn 3 kommt. Die Antworten wurden offenbar mit Kenntnis der späteren Prompts erzeugt. In einem echten Chat passiert das nicht. Deshalb ist auch Haikus frühe Erwähnung der Schlitzbreite in Turn 1 kein belastbarer Beleg dafür, dass Haiku den Fehler von selbst findet. Belastbar ist das Ergebnis von Turn 3. Zum Vergleich: Im Testlauf [demo-f18-pruefbericht.md](demo-f18-pruefbericht.md) übernahmen Haiku und Sonnet ohne Nachfrage „alle Maße in Toleranz“, Opus fand den Widerspruch von selbst.

## Lehren für die Auswertung

- **Der Prüfprompt wirkt zuverlässig.** Mit „Rechne jede Zeile einzeln nach“ haben alle drei Modelle den Widerspruch gefunden, alle 12 Zeilen richtig bewertet und ihre eigene Zusammenfassung korrigiert. Kernbotschaft: Die KI kann nachrechnen, tut es aber erst, wenn man sie ausdrücklich darum bittet.
- **Aber: Der Prompt ist suggestiv.** „Liegen alle Abweichungen *wirklich* innerhalb …?“ verrät schon, dass etwas faul ist. In der Auswertung offen ansprechen: „Hätten wir den Fehler auch ohne das Wort ‚wirklich‘ gefunden?“ Als neutralere Variante zum Vergleich: `Prüfe jede Zeile der Messwerttabelle in Abschnitt 4 gegen die Toleranzregel aus Abschnitt 3.1. Gib pro Zeile „in Toleranz“ oder „außerhalb“ an.`
- **Fundstellen sind nützlich, aber nicht fehlerfrei.** Zwei von drei Modellen haben eine Aussage einem Abschnitt zugeordnet, in dem sie nicht steht (3.1 statt 7 bzw. 4). Die Lehre: Fundstellen als Wegweiser nutzen und **im Original nachsehen**, nicht als Beleg akzeptieren.
- **„Genau 5 Sätze“ wird gern umgangen.** Nummerierte Punkte sehen aus wie 5 Sätze, enthalten aber 7–8. Gute Übung für Teilnehmende: Sätze zählen lassen.
- **Bonus für Fortgeschrittene:** Die Verfügbarkeit nachrechnen lassen (96,1 % statt „rund 96,2 %“). Selbst ein Modell, das „nachrechnet“, bestätigt die Zahl des Berichts. Das zeigt: Auch eine vorgeführte Rechnung muss man selbst kurz prüfen.
- **Opus liefert die beste Handlungsempfehlung:** Die Schlitzbreite fehlt in den Vorbehalten. Opus formuliert konkrete Rückfragen (Tabellenfehler? Wie viele der 10 Teile außerhalb? In den Vorbehalt aufnehmen?). Das ist ein schönes Beispiel dafür, wie eine Prüfung in eine Entscheidungsvorlage übergeht.
- **Zeitbedarf:** Drei Prompts plus Stichprobe im Original passen gut in die Stationszeit (ca. 10–15 Minuten). Die Antworten auf Turn 3 sind lang (Tabelle mit 12 Zeilen). Für die Auswertung reicht es, die Zeile Schlitzbreite und den Absatz „Was das bedeutet“ zu zeigen.

---

## Gesprächsprotokoll: Haiku

### Nutzer 1

Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers. Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen. Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details. Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist. Schreib nichts, was nicht im Bericht steht.

### Assistent 1

Laut Prüfbericht erfüllt die Laserschneidanlage LS-3015 die wesentlichen Anforderungen aus Lastenheft und Kaufvertrag, und die technische Verfügbarkeit im Dauerlauf liegt mit 96,2 % über der geforderten Mindestverfügbarkeit von 95 %. Schnittqualität und Maßhaltigkeit werden im Bericht als innerhalb der Toleranz bewertet, die Messwerttabelle zeigt jedoch für die Schlitzbreite bei Prüfteil B eine größte Abweichung von 0,13 mm bei einer Toleranz von ±0,10 mm. Offen sind die knapp verfehlte Taktzeit bei Prüfteil C (41 s statt 40 s), eine Leistungsaufnahme von 31 kW inklusive Absaugung gegenüber der Zusage „unter 30 kW“ ohne getrennte Messung, die Wiederholungsmessung der Staubkonzentration bei verzinktem Blech (92 % des Richtwerts) sowie das Software-Update 4.3, für das kein Termin genannt wurde. Die Fertigungstechnik empfiehlt, die Anlage unter Vorbehalt abzunehmen und 5 % des Kaufpreises (von der Schlusszahlung von 30 %) einzubehalten, und rechnet mit einer jährlichen Ersparnis von etwa 85.000 Euro gegenüber der Altanlage, ohne Schulungs-, Absaugungs- und Schutzglaskosten. Die Geschäftsführung muss über die formale Abnahme entscheiden, denn mit ihr geht die Gefahr auf die Nordlicht Technik GmbH über und die Schlusszahlung wird fällig, und für weitere Bediener ist eine nicht im Kaufvertrag enthaltene Schulung nötig.

### Nutzer 2

Nenne zu jeder Aussage deiner Zusammenfassung den Abschnitt im Bericht, aus dem sie stammt.

### Assistent 2

Aussage 1 (Anforderungen erfüllt, Verfügbarkeit 96,2 % gegenüber 95 %): Abschnitt 3.3, Abschnitt 4 (Kennwerttabelle), Abschnitt 7.

Aussage 2 (Maßhaltigkeit laut Bericht innerhalb Toleranz; Schlitzbreite Prüfteil B mit 0,13 mm bei ±0,10 mm): Abschnitt 3.1 (Bewertung und Toleranzregel) und Abschnitt 4 (Tabellenzeile „B – Seitenwand 3 mm, Schlitzbreite“). Die Aussage über die Toleranz stammt aus 3.1 und 7, die Zahlen für die Schlitzbreite aus Abschnitt 4.

Aussage 3 (offene Punkte: Taktzeit Prüfteil C, Leistungsaufnahme, Staubmessung, Software-Update, Schulung): Taktzeit Prüfteil C in Abschnitt 3.2 und 4; Leistungsaufnahme in Abschnitt 3.5 und 4; Staubkonzentration in Abschnitt 3.4 und 4; Software-Update 4.3 in Abschnitt 3.6; Schulung in Abschnitt 3.6. Die Zusammenfassung dieser Punkte steht in Abschnitt 7.

Aussage 4 (Empfehlung zur Abnahme unter Vorbehalt, Einbehalt von 5 %, Ersparnis von etwa 85.000 Euro): Empfehlung und Einbehalt in Abschnitt 7; Ersparnis und nicht enthaltene Kosten in Abschnitt 5.

Aussage 5 (Entscheidung der Geschäftsführung, Gefahrübergang, Fälligkeit der Schlusszahlung, zusätzliche Schulung): Abschnitt 1 (Entscheidung, Gefahrübergang, Schlusszahlung von 30 %); Schulung weiterer Bediener in Abschnitt 3.6.

Korrektur zu meiner Antwort 1: Die Aussage, Maßhaltigkeit sei innerhalb der Toleranz, übernimmt die Bewertung aus Abschnitt 3.1 und 7. Die Tabelle in Abschnitt 4 stützt sie für die Schlitzbreite bei Prüfteil B nicht (Details in Antwort 3).

### Nutzer 3

Überprüfe die Messwerttabelle in Abschnitt 4: Liegen alle Abweichungen wirklich innerhalb der Toleranz? Rechne jede Zeile einzeln nach.

### Assistent 3

Ich habe jede Zeile der Tabelle aus Abschnitt 4 nachgerechnet. Die Abweichung ist Mittelwert minus Sollmaß. Geprüft wird außerdem die Spalte „Größte Abweichung“ gegen die Toleranz. Die Toleranzen stimmen mit der Regel aus Abschnitt 3.1 überein (Prüfteil B mit 3 mm: ±0,10 mm; Prüfteil C mit 8 mm: ±0,20 mm).

| Nr. | Prüfteil / Prüfmaß | Soll (mm) | Tol. (mm) | Mittelwert (mm) | Abw. Mittelwert | Größte Abw. (mm) | Ergebnis |
|---|---|---|---|---|---|---|---|
| 1 | A Breite | 180,00 | ±0,10 | 180,03 | +0,03 | 0,06 | innerhalb |
| 2 | A Höhe | 120,00 | ±0,10 | 119,98 | −0,02 | 0,05 | innerhalb |
| 3 | A Lochabstand | 40,00 | ±0,10 | 40,01 | +0,01 | 0,04 | innerhalb |
| 4 | A Ausschnitt Anzeige | 62,50 | ±0,10 | 62,54 | +0,04 | 0,08 | innerhalb |
| 5 | B Breite | 300,00 | ±0,10 | 300,04 | +0,04 | 0,07 | innerhalb |
| 6 | B Höhe | 210,00 | ±0,10 | 210,02 | +0,02 | 0,06 | innerhalb |
| 7 | B Schlitzbreite | 4,00 | ±0,10 | 4,07 | +0,07 | 0,13 | **nicht innerhalb** |
| 8 | B Schlitzabstand | 12,00 | ±0,10 | 12,01 | +0,01 | 0,05 | innerhalb |
| 9 | C Schenkellänge 1 | 80,00 | ±0,20 | 80,06 | +0,06 | 0,14 | innerhalb |
| 10 | C Schenkellänge 2 | 60,00 | ±0,20 | 59,95 | −0,05 | 0,11 | innerhalb |
| 11 | C Bohrung Ø | 10,50 | ±0,20 | 10,41 | −0,09 | 0,17 | innerhalb |
| 12 | C Bohrungsabstand | 45,00 | ±0,20 | 45,08 | +0,08 | 0,15 | innerhalb |

Ergebnis: Nein, nicht alle Abweichungen liegen innerhalb der Toleranz. 11 von 12 Zeilen sind innerhalb. Zeile 7 (Schlitzbreite, Prüfteil B) hat eine größte Abweichung von 0,13 mm, die Toleranz beträgt ±0,10 mm. Die Bewertung „i. O.“ in dieser Zeile ist daher nicht haltbar. Der Mittelwert liegt mit +0,07 mm noch innerhalb, die Einzelmessung nicht.

Hinweis zur Interpretation: Die Spalte „Größte Abweichung“ ist nicht näher definiert. Ich habe sie als Abweichung vom Sollmaß gelesen, weil das der naheliegende Bezug ist. Bezieht sie sich stattdessen auf den Mittelwert, lässt sich Zeile 7 aus der Tabelle allein nicht entscheiden, und der Bericht müsste die Messreihe nachliefern.

Folge für den Bericht: Die Aussagen „Maßhaltigkeit bei allen drei Prüfteilen innerhalb der Toleranz“ (Abschnitt 3.1 und 7) sind so nicht belegt. Die Empfehlung zur Abnahme unter Vorbehalt bleibt davon unberührt, die Schlitzbreite sollte aber vor der Abnahme geklärt werden.

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1

Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.

### Assistent 1

1. Die Laserschneidanlage LS-3015 erfüllt laut Fertigungstechnik die wesentlichen Anforderungen: Die Maßhaltigkeit wird im Bericht als innerhalb der Toleranz bewertet, die Taktzeiten für Prüfteil A (82 s) und B (64 s) liegen unter den zugesicherten Werten, und die Verfügbarkeit beträgt 96,2 % (gefordert: 95 %). Knapp verfehlt bzw. ungeklärt sind die Taktzeit bei Prüfteil C (41 statt 40 s) und die Leistungsaufnahme (31 kW inkl. Absaugung statt "unter 30 kW").
2. Die Fertigungstechnik rechnet mit einer jährlichen Ersparnis von etwa 85.000 Euro gegenüber der Altanlage. Nicht enthalten sind Kosten für zusätzliche Schulungen, eine eventuell nötige Verstärkung der Absaugung und höheren Schutzglasverbrauch.
3. Offen sind außerdem die Wiederholungsmessung der Staubkonzentration bei verzinktem Blech (92 % des Richtwerts, Wiederholung nach drei Monaten gewünscht), das Software-Update 4.3 (angekündigt "im Laufe des Quartals", ohne konkreten Termin) und die Ergänzung des Wartungsplans.
4. Es ist eine Entscheidung der Geschäftsführung nötig: die formale Abnahme, mit der die Gefahr auf Nordlicht Technik übergeht und die Schlusszahlung von 30 % des Kaufpreises fällig wird.
5. Empfohlen wird die Abnahme unter schriftlichem Vorbehalt (Update 4.3 mit verbindlichem Termin, Wartungsplan ergänzen, getrennte Leistungsmessung ohne Absaugung) sowie ein Einbehalt von 5 % des Kaufpreises von der Schlusszahlung, bis diese Punkte erledigt sind.

### Nutzer 2

Nenne zu jeder Aussage deiner Zusammenfassung den Abschnitt im Bericht, aus dem sie stammt.

### Assistent 2

**Satz 1**
- Wesentliche Anforderungen erfüllt, Maßhaltigkeit innerhalb der Toleranz: Abschnitt 7 (Zusammenfassung), Messwerte in Abschnitt 3.1 und 4.
- Taktzeiten A (82 s) und B (64 s): Abschnitt 3.2 und die Kennwerttabelle in Abschnitt 4.
- Verfügbarkeit 96,2 % gegenüber 95 % gefordert: Abschnitt 3.3 und Abschnitt 4.
- Taktzeit C 41 statt 40 s: Abschnitt 3.2 und Abschnitt 4.
- Leistungsaufnahme 31 kW inkl. Absaugung, "unter 30 kW" angeboten: Abschnitt 3.5 und Abschnitt 4.

**Satz 2**
- 85.000 Euro Ersparnis pro Jahr und die nicht enthaltenen Kosten (Schulungen, Absaugung, Schutzgläser): Abschnitt 5.

**Satz 3**
- Staubkonzentration 92 % und Wiederholungsmessung nach drei Monaten: Abschnitt 3.4 (Wert auch in Abschnitt 4).
- Software-Update 4.3 ohne konkreten Termin: Abschnitt 3.6.
- Wartungsplan ohne Wechselintervall des Schutzglases: Abschnitt 3.6 (Verweis auf 3.3) und Abschnitt 7.

**Satz 4**
- Entscheidung über die formale Abnahme, Gefahrübergang und Schlusszahlung von 30 %: Abschnitt 1. Dass die Geschäftsführung entscheidet, steht auch in Abschnitt 7.

**Satz 5**
- Abnahme unter Vorbehalt mit den drei Punkten und 5 % Einbehalt: Abschnitt 7 (Empfehlung).

### Nutzer 3

Überprüfe die Messwerttabelle in Abschnitt 4: Liegen alle Abweichungen wirklich innerhalb der Toleranz?
Rechne jede Zeile einzeln nach.

### Assistent 3

Nein. Eine Zeile liegt außerhalb der Toleranz, obwohl sie mit "i. O." bewertet ist.

Ich habe jeweils die Abweichung des Mittelwerts vom Sollmaß berechnet und die angegebene "Größte Abweichung" mit der Toleranz verglichen. Die Toleranzen laut Abschnitt 3.1 sind ±0,10 mm für Teile bis 3 mm und ±0,20 mm für Teile über 3 mm.

| Teil / Maß | Mittelwert minus Soll | Größte Abw. | Toleranz | Ergebnis |
|---|---|---|---|---|
| A Breite | 180,03 − 180,00 = +0,03 | 0,06 | ±0,10 | in Toleranz |
| A Höhe | 119,98 − 120,00 = −0,02 | 0,05 | ±0,10 | in Toleranz |
| A Lochabstand | 40,01 − 40,00 = +0,01 | 0,04 | ±0,10 | in Toleranz |
| A Ausschnitt Anzeige | 62,54 − 62,50 = +0,04 | 0,08 | ±0,10 | in Toleranz |
| B Breite | 300,04 − 300,00 = +0,04 | 0,07 | ±0,10 | in Toleranz |
| B Höhe | 210,02 − 210,00 = +0,02 | 0,06 | ±0,10 | in Toleranz |
| **B Schlitzbreite** | 4,07 − 4,00 = +0,07 | **0,13** | ±0,10 | **außerhalb (0,03 mm drüber)** |
| B Schlitzabstand | 12,01 − 12,00 = +0,01 | 0,05 | ±0,10 | in Toleranz |
| C Schenkellänge 1 | 80,06 − 80,00 = +0,06 | 0,14 | ±0,20 | in Toleranz |
| C Schenkellänge 2 | 59,95 − 60,00 = −0,05 | 0,11 | ±0,20 | in Toleranz |
| C Bohrung Ø | 10,41 − 10,50 = −0,09 | 0,17 | ±0,20 | in Toleranz |
| C Bohrungsabstand | 45,08 − 45,00 = +0,08 | 0,15 | ±0,20 | in Toleranz |

**Befund**
- Bei Prüfteil B, Schlitzbreite, liegt der Mittelwert mit +0,07 mm noch innerhalb der Toleranz. Die größte Einzelabweichung beträgt aber 0,13 mm und überschreitet die zulässigen ±0,10 mm (Prüfteil B hat 3 mm Materialstärke, gilt also als "bis 3 mm"). Mindestens ein gemessenes Teil ist damit nicht in Toleranz. Die Bewertung "i. O." ist für diese Zeile nicht korrekt.
- Die anderen 11 Zeilen sind in Ordnung. Bei Prüfteil C liegen sie mit 0,11 bis 0,17 mm deutlich unter ±0,20 mm. Bei Prüfteil A ist der Ausschnitt Anzeige mit 0,08 mm gegenüber ±0,10 mm am knappsten.
- Der Bericht ist an dieser Stelle widersprüchlich. Abschnitt 7 sagt, die Maßhaltigkeit sei bei allen drei Prüfteilen innerhalb der Toleranz. Das stimmt für Prüfteil B nicht uneingeschränkt.

**Korrektur zu meiner Zusammenfassung:** Mein erster Satz hat die Aussage des Berichts zur Maßhaltigkeit übernommen. Das war nach dieser Nachrechnung nicht korrekt. Richtig ist: Die Maßhaltigkeit ist bis auf die Schlitzbreite bei Prüfteil B in Toleranz. Dort ist die Toleranz bei der größten Einzelabweichung überschritten, und die Bewertung sollte vor der Abnahme geklärt werden (zum Beispiel durch Nachmessung oder eine Anpassung beim Hersteller).

**Nebenbemerkung:** Die Verfügbarkeit stimmt. 80 h sind 4.800 min, die Stillstände summieren sich auf 35 + 130 + 20 = 185 min, und (4.800 − 185) / 4.800 ≈ 96,2 %.

---

## Gesprächsprotokoll: Opus

### Nutzer 1

Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.

### Assistent 1

Hier die Zusammenfassung des Abnahmeprüfberichts PB-2024-017 zur Laserschneidanlage LS-3015:

1. Laut Bericht erfüllt die neue Laserschneidanlage die wesentlichen Anforderungen: Schnittqualität und Maßhaltigkeit sollen bei allen drei Prüfteilen innerhalb der Toleranz liegen, die Taktzeiten der Prüfteile A und B liegen deutlich unter den Zusagen (82 s statt max. 95 s, 64 s statt max. 70 s), und die Verfügbarkeit im Dauerlauf liegt bei 96,2 % (gefordert: 95 %).
2. Gegenüber der Altanlage sinkt die Bearbeitungszeit um rund 45 % und der Energieverbrauch um rund 60 %; die Fertigungstechnik schätzt überschlägig eine Ersparnis von etwa 85.000 Euro pro Jahr. Nicht eingerechnet sind dabei Kosten für weitere Schulungen, eine eventuell nötige Verstärkung der Absaugung und den höheren Verbrauch an Schutzgläsern (ca. 60 Euro pro Stück, Lieferzeit drei bis sechs Wochen).
3. Offen sind die knapp verfehlte Taktzeit bei Prüfteil C (41 s statt 40 s), die Leistungsaufnahme (31 kW inklusive Absaugung statt zugesagt unter 30 kW, nicht getrennt gemessen), die Staubbelastung bei verzinktem Blech (92 % des internen Richtwerts) und das fehlende Schutzglas-Wechselintervall im Wartungsplan.
4. Zu den Terminen: Die Staubmessung soll nach drei Monaten wiederholt werden, und das Software-Update 4.3, das die fehlerhafte Übergabe der Auftragsdaten aus dem ERP behebt, ist für „im Laufe des Quartals“ angekündigt, aber ohne konkreten Termin. Außerdem werden mindestens zwei weitere Bediener gebraucht, deren Schulung gesondert beauftragt werden muss.
5. Eine Entscheidung der Geschäftsführung ist nötig, nämlich über die formale Abnahme, mit der die Gefahr übergeht und die Schlusszahlung von 30 % des Kaufpreises fällig wird. Die Fertigungstechnik empfiehlt eine Abnahme unter schriftlichem Vorbehalt (Update 4.3 bis zu einem verbindlichen Termin, Ergänzung des Wartungsplans, getrennte Messung der Leistungsaufnahme) und bis dahin einen Einbehalt von 5 % des Kaufpreises.

### Nutzer 2

Nenne zu jeder Aussage deiner Zusammenfassung den Abschnitt im Bericht, aus dem sie stammt.

### Assistent 2

Hier die Quellen zu jedem Satz:

**Satz 1 (Ergebnis):**
- Erfüllt die wesentlichen Anforderungen, Maßhaltigkeit innerhalb der Toleranz: Abschnitt 7 (Zusammenfassung und Empfehlung), Tabelle in Abschnitt 4. Hinweis: Diese Aussage halte ich nach dem Nachrechnen nicht mehr für richtig, siehe meine Antwort zur Messwerttabelle.
- Taktzeiten A und B (82 s / 95 s, 64 s / 70 s): Abschnitt 3.2 und die Kennwert-Tabelle in Abschnitt 4
- Verfügbarkeit 96,2 % bei geforderten 95 %: Abschnitt 3.3 und Abschnitt 4

**Satz 2 (Wirtschaftlichkeit und Kosten):**
- Bearbeitungszeit rund 45 % kürzer: Abschnitt 3.2
- Energieverbrauch rund 60 % niedriger: Abschnitt 3.5
- Ersparnis etwa 85.000 Euro pro Jahr und die nicht eingerechneten Kosten: Abschnitt 5 (Wirtschaftliche Betrachtung)
- Schutzglas ca. 60 Euro, Lieferzeit drei bis sechs Wochen: Abschnitt 3.3

**Satz 3 (offene Punkte):**
- Taktzeit Prüfteil C 41 s statt 40 s: Abschnitt 3.2 und Abschnitt 4
- Leistungsaufnahme 31 kW inklusive Absaugung, nicht getrennt gemessen: Abschnitt 3.5 und Abschnitt 4
- Staubbelastung 92 % des Richtwerts: Abschnitt 3.4 und Abschnitt 4
- Wechselintervall des Schutzglases fehlt im Wartungsplan: Abschnitt 3.6 (mit Verweis auf 3.3)

**Satz 4 (Termine und Aufwand):**
- Staubmessung nach drei Monaten wiederholen: Abschnitt 3.4
- Update 4.3 „im Laufe des Quartals“, ohne konkreten Termin, behebt den ERP-Fehler: Abschnitt 3.6
- Mindestens zwei weitere Bediener nötig, Schulung gesondert zu beauftragen: Abschnitt 3.6

**Satz 5 (Entscheidung):**
- Geschäftsführung entscheidet über die Abnahme, Gefahrübergang, Schlusszahlung 30 %: Abschnitt 1 (Anlass und Ziel der Prüfung)
- Empfehlung: Abnahme unter Vorbehalt mit drei Bedingungen und 5 % Einbehalt: Abschnitt 7 (Empfehlung)

### Nutzer 3

Überprüfe die Messwerttabelle in Abschnitt 4: Liegen alle Abweichungen wirklich innerhalb der Toleranz?
Rechne jede Zeile einzeln nach.

### Assistent 3

Nein, nicht alle. Eine Zeile liegt außerhalb der Toleranz, ist im Bericht aber trotzdem als „i. O.“ eingetragen.

Ich habe die Toleranz aus Abschnitt 3.1 verwendet: ±0,10 mm für Teile bis 3 mm Materialstärke (Teile A und B) und ±0,20 mm für Teile über 3 mm (Teil C). Für jede Zeile habe ich die Abweichung des Mittelwerts vom Sollmaß und die größte Einzelabweichung geprüft.

| Prüfteil | Prüfmaß | Toleranz | Mittelwert minus Soll | Größte Abweichung | Ergebnis |
|---|---|---|---|---|---|
| A | Breite | ±0,10 | 180,03 − 180,00 = +0,03 | 0,06 ≤ 0,10 | in Ordnung |
| A | Höhe | ±0,10 | 119,98 − 120,00 = −0,02 | 0,05 ≤ 0,10 | in Ordnung |
| A | Lochabstand | ±0,10 | 40,01 − 40,00 = +0,01 | 0,04 ≤ 0,10 | in Ordnung |
| A | Ausschnitt Anzeige | ±0,10 | 62,54 − 62,50 = +0,04 | 0,08 ≤ 0,10 | in Ordnung |
| B | Breite | ±0,10 | 300,04 − 300,00 = +0,04 | 0,07 ≤ 0,10 | in Ordnung |
| B | Höhe | ±0,10 | 210,02 − 210,00 = +0,02 | 0,06 ≤ 0,10 | in Ordnung |
| **B** | **Schlitzbreite** | **±0,10** | 4,07 − 4,00 = +0,07 | **0,13 > 0,10** | **außerhalb der Toleranz** |
| B | Schlitzabstand | ±0,10 | 12,01 − 12,00 = +0,01 | 0,05 ≤ 0,10 | in Ordnung |
| C | Schenkellänge 1 | ±0,20 | 80,06 − 80,00 = +0,06 | 0,14 ≤ 0,20 | in Ordnung |
| C | Schenkellänge 2 | ±0,20 | 59,95 − 60,00 = −0,05 | 0,11 ≤ 0,20 | in Ordnung |
| C | Bohrung Ø | ±0,20 | 10,41 − 10,50 = −0,09 | 0,17 ≤ 0,20 | in Ordnung (knapp) |
| C | Bohrungsabstand | ±0,20 | 45,08 − 45,00 = +0,08 | 0,15 ≤ 0,20 | in Ordnung |

**Ergebnis:**
- **Prüfteil B, Schlitzbreite:** Die größte Abweichung von 0,13 mm überschreitet die zulässigen ±0,10 mm um 0,03 mm. Das Blech ist 3 mm dick, also gilt die engere Toleranz von ±0,10 mm. Der Mittelwert liegt zwar innerhalb, aber mindestens ein gemessenes Teil war außerhalb der Toleranz. Die Bewertung „i. O.“ ist deshalb falsch.
- Die anderen 11 Zeilen stimmen. Am knappsten sind die Bohrung bei Teil C (0,17 von 0,20 mm) und der Ausschnitt Anzeige bei Teil A (0,08 von 0,10 mm).

**Was das bedeutet:**
- Die Aussage in Abschnitt 7, Maßhaltigkeit liege „bei allen drei Prüfteilen innerhalb der Toleranz“, stimmt so nicht. Deshalb ist auch Satz 1 meiner Zusammenfassung an dieser Stelle falsch, weil ich ihn aus dem Bericht übernommen habe. Richtig wäre: Bei Prüfteil B liegt die Schlitzbreite außerhalb der Toleranz.
- In den offenen Punkten des Berichts und in den Vorbehalten der Empfehlung kommt diese Abweichung nicht vor.
- Bevor die Geschäftsführung entscheidet, sollte die Fertigungstechnik oder die Qualitätssicherung das klären. Mögliche Fragen sind: Ist das ein Fehler in der Tabelle? Wie viele der 10 gemessenen Teile lagen außerhalb? Gehört die Schlitzbreite als weiterer Punkt in den Abnahmevorbehalt?
