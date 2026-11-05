# Testlauf: Übung 3 / Station A Für Schnelle – Drei Fragen der GF an die Autoren

**Herkunft:** [Übung 3 – Dokumente und Tabellen, Station A, „Für Schnelle“](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md) (zweiter Spiegelstrich: „Welche drei Fragen sollte die Geschäftsführung den Autoren des Berichts stellen?“), Material [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md), Abgleich mit [Trainer-Lösungshinweise, Station A](../06_Uebungen/Trainer-Loesungshinweise.md)

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf (ein Chat, Bericht mit Turn 1 angehängt):**

1. Basis-Prompt der Station A (Zusammenfassung in genau 5 Sätzen)
2. `Welche drei Fragen sollte die Geschäftsführung den Autoren des Berichts stellen?`

**Ziel laut Material:** Drei kritische, sinnvolle Rückfragen, die auf echte Lücken des Berichts zielen. Gute Kandidaten: verbindlicher Termin für Update 4.3; ob 31 kW die Zusage „unter 30 kW“ erfüllt / Messung ohne Absaugung; Taktzeit C; Schutzglas-Bevorratung und Lieferzeit; Kosten zusätzlicher Schulungen; Schlitzbreite Prüfteil B.

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Formal 3 nummerierte Fragen | ja | ja | ja |
| Tatsächlich 3 Fragen (Fragezeichen) | 3, aber Frage 3 ist eine Doppelfrage | **6**, Fragenbündel | **8**, Fragenbündel |
| Länge Turn 2 | ca. 90 Wörter | ca. 170 Wörter | ca. 270 Wörter |
| Termin Update 4.3 / manuelle Übertragung | ja (Frage 1) | ja (in Frage 3) | ja (in Frage 3) |
| 31 kW gegen „unter 30 kW“ / Messung ohne Absaugung | **ja (Frage 2)** | nein | nur erwähnt (Teil des Vorbehalts) |
| Taktzeit C (41 s statt 40 s) | nein | ja (fehlt im Vorbehalt) | ja (fehlt im Vorbehalt) |
| Schutzglas: 2 auf Lager, 3–6 Wochen | nur als Kostenposten | ja | ja |
| Kosten zusätzlicher Schulungen | nur als Kostenposten | ja | ja („für welchen Betrag“) |
| Belastbarkeit 85.000 € / Amortisation „geringfügig“ | ja | ja | ja (dazu: Einschicht nur „nach aktueller Auftragslage“) |
| Staub 92 %, Wiederholungsmessung | ja (vermischt mit Kostenfrage) | ja, sehr gut („Warum Abnahme vor der Messung?“) | ja („Wer zahlt die Absaugung nach Abnahme?“) |
| Vorbehalt / 5 % Einbehalt hinterfragt | nein | ja | ja („welcher Betrag das ist“) |
| Altanlage ohne Wartungsvertrag (Bonus) | nein | nein | **ja** |
| Widerspruch Schlitzbreite 0,13 mm > ±0,10 mm (Bonus) | nein | nein | nein |
| Kein erfundener Betrag/Termin | ja | ja | ja |
| Sachlich korrekt | ja (Frage 3 unlogisch verknüpft) | ein Fehler (Update angeblich nicht im Vorbehalt) | ja |
| **Gesamt** | knapp, präzise, aber dünn | kritisch und gut, ein Sachfehler | **am besten**, aber sehr lang |

Nebenbefund Turn 1 (Basis-Prompt): Haiku liefert **6 statt 5 Sätze**; Sonnet und Opus halten die 5 Sätze formal ein (Opus mit Bandwurmsätzen über je 40–60 Wörter). Alle drei übernehmen „Maßhaltigkeit bei allen drei Prüfteilen innerhalb der Toleranz“ ungeprüft.

## Gefundene Fehler mit Beleg

1. **Sonnet, Frage 3 – Update 4.3 angeblich nicht im Vorbehalt.** Sonnet zählt Update 4.3, Schutzglas-Lieferzeit und Schulung auf und fragt dann: „Warum sind diese Punkte, die Staubmessung und die Taktzeit bei Prüfteil C nicht im Vorbehalt enthalten?“ Abschnitt 7 nennt aber ausdrücklich als Vorbehalt „(1) das Software-Update 4.3 bis zu einem verbindlichen Termin“. Auch das Schutzglas ist teilweise enthalten („(2) den Wartungsplan um das Wechselintervall des Schutzglases ergänzt“), nur Bevorratung und Lieferzeit fehlen. Sonnet widerspricht damit sogar seiner eigenen Zusammenfassung aus Turn 1. Die Frage würde die Autoren in eine falsche Richtung schicken.
2. **Haiku, Frage 3 – zwei Themen unlogisch verknüpft.** „Wie belastbar ist die Staubmessung bei geschlossener Hallentür, **wenn** die Folgekosten (Schulungen, Absaugung, Schutzgläser) noch nicht eingerechnet sind?“ Die Belastbarkeit der Staubmessung hängt nicht von den eingerechneten Kosten ab (Abschnitt 3.4 gegen Abschnitt 5). Inhaltlich ist es eine Doppelfrage, die nur grammatisch zu einer verbunden wurde.
3. **Alle drei – Schlitzbreite übersehen.** Nachgerechnet über alle 12 Zeilen der Tabelle in Abschnitt 4: Nur Zeile „B – Seitenwand 3 mm | Schlitzbreite“ überschreitet die Toleranz (größte Abweichung 0,13 mm bei ±0,10 mm, trotzdem „i. O.“). Gerade das wäre die naheliegendste Frage an die Autoren: „Warum ist das i. O.?“ Kein Modell stellt sie. Das ist kein Halluzinationsfehler, sondern eine Lücke, die den Effekt aus den Lösungshinweisen bestätigt: Die KI glaubt dem Fazit, statt nachzurechnen.
4. **Formal: „drei Fragen“ werden zu Fragenbündeln.** Sonnet stellt 6 Fragen (mit Fragezeichen), Opus 8 (je eine fette Leitfrage plus Unterfragen). Haiku hält die Zahl am ehesten ein, bündelt aber in Frage 3 ebenfalls zwei Themen.
5. **Keine Erfindungen.** Kein Modell nennt einen Termin für Update 4.3 oder einen Eurobetrag für Einbehalt oder Kaufpreis. Opus fragt ausdrücklich, „welcher Betrag das ist“, statt ihn zu schätzen. Die Angaben „Herrn Albers“, „nach aktueller Auftragslage“, „geringfügig“, „zwei Stück auf Lager“ und „drei bis sechs Wochen“ stehen so im Bericht.

## Lehren für die Auswertung

- **Die Übung funktioniert:** Alle Modelle liefern brauchbare, kritische Rückfragen, die sich auf echte Stellen im Bericht beziehen. Für Schnelle ist der Zeitbedarf passend (unter 5 Minuten inkl. Lesen).
- **Kritische Fragen stellt die KI gut, kontrollieren muss man trotzdem.** Sonnets Frage 3 klingt scharf, beruht aber auf einer falschen Annahme. Gute Kontrollfrage für die Gruppe: „Steht das Update wirklich nicht im Vorbehalt? Schaut in Abschnitt 7.“
- **„Drei Fragen“ heißt für die KI nicht drei Fragen.** Die stärkeren Modelle packen viel in jede Frage. Für den Einsatz bei der GF ist das zu lang. Nachsteuern: „Genau drei Fragen, je ein Satz, mit Abschnitt.“
- **Was alle übersehen, ist die beste Frage:** Die Schlitzbreite (0,13 mm bei ±0,10 mm) taucht nirgends auf. Gut als Abschluss: „Welche Frage hätte die KI stellen müssen, wenn sie die Tabelle nachgerechnet hätte?“
- **Modellvergleich:** Das kleinste Modell ist knapp und trifft mit der Leistungsaufnahme einen Punkt, den die großen auslassen. Die großen finden mehr Zusammenhänge (Vorbehalt unvollständig, Altanlage ohne Wartungsvertrag). Mehr Text bedeutet aber nicht automatisch weniger Fehler.
- **Adressat beachten:** Einige Fragen (Termin für Update 4.3, Bestand an Schutzgläsern) können nur der Hersteller oder die GF selbst beantworten, nicht die Autoren. Guter Diskussionspunkt: „An wen richtet sich diese Frage eigentlich?“

---

## Gesprächsprotokoll: Haiku

### Nutzer 1
Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.

### Assistent 1
Die Laserschneidanlage LS-3015 erfüllt laut Prüfbericht PB-2024-017 die wesentlichen Anforderungen aus Lastenheft und Kaufvertrag, Schnittqualität und Maßhaltigkeit liegen bei allen drei Prüfteilen innerhalb der Toleranz. Die Taktzeiten der Hauptteile unterschreiten die zugesicherten Werte (Frontblende 82 s statt max. 95 s, Seitenwand 64 s statt 70 s), beim Montagewinkel wird mit 41 s der Sollwert von 40 s knapp verfehlt, und die technische Verfügbarkeit im Dauerlauf liegt mit 96,2 % über der geforderten 95 %. Laut überschlägiger Rechnung ergibt sich eine jährliche Ersparnis von etwa 85.000 Euro, nicht enthalten sind Zusatzschulungen, eine mögliche Verstärkung der Absaugung und ein höherer Verbrauch an Schutzgläsern (rund 60 Euro je Stück, Lieferzeit drei bis sechs Wochen). Offen sind ein verbindlicher Termin für das Software-Update 4.3 (bisher nur „im Laufe des Quartals“), die Ergänzung des Wartungsplans, eine getrennte Messung der Leistungsaufnahme (31 kW inkl. Absaugung statt der angebotenen unter 30 kW), die Wiederholung der Staubmessung nach drei Monaten sowie die Schulung weiterer Bediener. Die Fertigungstechnik empfiehlt, die Anlage unter Vorbehalt abzunehmen und 5 % des Kaufpreises als Einbehalt von der Schlusszahlung zurückzuhalten. Die Geschäftsführung muss daher über die formale Abnahme und den Einbehalt entscheiden.

### Nutzer 2
Welche drei Fragen sollte die Geschäftsführung den Autoren des Berichts stellen?

### Assistent 2
1. Bis wann genau wird das Software-Update 4.3 bereitgestellt, und wie stark belastet die manuelle Übertragung der Schneidprogramme bis dahin den Betrieb?
2. Warum wurde die Leistungsaufnahme nicht getrennt ohne Absaugung gemessen, und wie groß ist die tatsächliche Abweichung von den angebotenen unter 30 kW?
3. Worauf beruhen die geschätzten 85.000 Euro Ersparnis, und wie belastbar ist die Staubmessung bei geschlossener Hallentür, wenn die Folgekosten (Schulungen, Absaugung, Schutzgläser) noch nicht eingerechnet sind?

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1
Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.

### Assistent 1
Die Laserschneidanlage LS-3015 erfüllt die wesentlichen Anforderungen: Schnittqualität und Maßhaltigkeit liegen bei allen Prüfteilen in der Toleranz, die Verfügbarkeit im Dauerlauf beträgt 96,2 % (gefordert: 95 %), und die Taktzeiten sind bei zwei von drei Prüfteilen besser als zugesichert. Knapp verfehlt wurden die Taktzeit bei Prüfteil C (41 statt 40 Sekunden) und die zugesagte Leistungsaufnahme (31 statt unter 30 kW, wobei die Absaugung mitgemessen wurde und eine getrennte Messung fehlt). Die Fertigungstechnik rechnet überschlägig mit rund 85.000 Euro Ersparnis pro Jahr gegenüber der Altanlage, ohne Kosten für zusätzliche Schulungen, eine mögliche Verstärkung der Absaugung und den höheren Schutzglasverbrauch. Offen sind unter anderem die Wiederholungsmessung der Staubkonzentration beim verzinkten Blech (aktuell 92 % des Richtwerts, Wiederholung nach drei Monaten erbeten), das Software-Update 4.3 (angekündigt für dieses Quartal, aber ohne konkreten Termin) und die Schulung weiterer Bediener, die nicht im Kaufvertrag enthalten ist. Ja, es ist eine Entscheidung nötig: Empfohlen wird die Abnahme unter Vorbehalt (Update 4.3 mit verbindlichem Termin, ergänztes Wartungsintervall für das Schutzglas, getrennte Leistungsmessung) sowie ein Einbehalt von 5 % des Kaufpreises von der Schlusszahlung, die 30 % des Kaufpreises beträgt.

### Nutzer 2
Welche drei Fragen sollte die Geschäftsführung den Autoren des Berichts stellen?

### Assistent 2
1. Wie belastbar sind die 85.000 Euro jährliche Ersparnis, und wie hoch wäre die Amortisationszeit, wenn man die nicht enthaltenen Posten (Schulung weiterer Bediener, mögliche Verstärkung der Absaugung, häufigerer Schutzglaswechsel) realistisch einrechnet? Der Bericht sagt nur, sie verlängere sich "geringfügig", nennt aber keine Zahlen.
2. Reicht der Arbeitsschutz beim verzinkten Blech wirklich aus? Der Messwert liegt bei 92 % des Richtwerts, gemessen bei geschlossener Hallentür, und die Wiederholungsmessung unter anderen Luftströmungen steht aus. Was passiert, wenn sie über dem Richtwert liegt, und ist dafür eine Verstärkung der Absaugung samt Kosten einzuplanen? Warum soll die Abnahme vor dieser Messung erfolgen?
3. Ist der vorgeschlagene Vorbehalt vollständig und durchsetzbar? Das Software-Update 4.3 hat noch keinen Termin, solange müssen Schneidprogramme teilweise manuell übertragen werden. Das Schutzglas hat eine Lieferzeit von drei bis sechs Wochen bei nur zwei Stück auf Lager und häufigen Wechseln. Die Schulung weiterer Bediener ist nicht im Vertrag enthalten. Warum sind diese Punkte, die Staubmessung und die Taktzeit bei Prüfteil C nicht im Vorbehalt enthalten, und reichen 5 % Einbehalt dafür aus?

---

## Gesprächsprotokoll: Opus

### Nutzer 1
Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.

### Assistent 1
Laut Abnahmeprüfbericht erfüllt die neue Laserschneidanlage LS-3015 die wesentlichen Anforderungen aus Lastenheft und Kaufvertrag: Bei allen drei Prüfteilen liegen die Maße innerhalb der Toleranz, die beiden wichtigsten Serienteile sind deutlich schneller als zugesagt (82 statt max. 95 s bzw. 64 statt max. 70 s), und die Verfügbarkeit im Dauerlauf lag bei 96,2 % (gefordert waren mindestens 95 %).

Die Bearbeitungszeit sinkt gegenüber der Altanlage um rund 45 %, daher reicht voraussichtlich eine Schicht statt bisher zwei, und die Fertigungstechnik schätzt grob eine Ersparnis von etwa 85.000 Euro pro Jahr; darin fehlen die Kosten für weitere Schulungen, eine eventuell nötige stärkere Absaugung und den höheren Verbrauch an Schutzgläsern.

Einige Punkte sind knapp verfehlt oder noch offen: Prüfteil C braucht 41 statt 40 s, die Anlage nimmt 31 kW statt der zugesagten „unter 30 kW“ auf (gemessen zusammen mit der Absaugung), beim verzinkten Blech erreicht der Staub 92 % des internen Richtwerts, im Wartungsplan fehlt das kürzere Wechselintervall für das Schutzglas, und mindestens zwei weitere Bediener müssen geschult werden, was gesondert beauftragt werden muss.

Zu den Terminen: Das Software-Update 4.3, das einen Fehler bei der Übergabe der Auftragsdaten aus dem ERP-System behebt, ist für dieses Quartal angekündigt, aber ohne festen Termin, die Staubmessung soll nach drei Monaten wiederholt werden, und Schutzgläser haben derzeit drei bis sechs Wochen Lieferzeit bei nur zwei Stück auf Lager.

Eine Entscheidung der Geschäftsführung ist nötig, nämlich über die formale Abnahme, mit der das Risiko auf uns übergeht und die Schlusszahlung von 30 % des Kaufpreises fällig wird: Die Fertigungstechnik empfiehlt eine Abnahme unter Vorbehalt (fester Termin für das Update, ergänzter Wartungsplan, getrennte Messung der Leistungsaufnahme ohne Absaugung) und bis dahin einen Einbehalt von 5 % des Kaufpreises.

### Nutzer 2
Welche drei Fragen sollte die Geschäftsführung den Autoren des Berichts stellen?

### Assistent 2
Diese drei Fragen würde ich Herrn Albers und seinem Team stellen:

1. **Wie hoch sind die nicht eingerechneten Folgekosten, und wie belastbar sind die 85.000 Euro Ersparnis?**
   Laut Bericht ist die Ersparnis nur grob gerechnet. Kosten für weitere Schulungen, eine mögliche Verstärkung der Absaugung und mehr Schutzgläser fehlen, und der Bericht sagt nur, dass sich die Amortisation „geringfügig“ verlängert. Die Geschäftsführung sollte wenigstens eine Spanne dieser Kosten kennen, besonders für die Absaugung, die teuer werden könnte. Außerdem setzt die Ersparnis voraus, dass eine Schicht reicht. Das stimmt nur „nach aktueller Auftragslage“.

2. **Reichen der Vorbehalt und der Einbehalt von 5 %, oder fehlen wichtige Punkte?**
   Der Vorbehalt umfasst nur das Update, den Wartungsplan und die Messung der Leistungsaufnahme. Zwei Punkte fehlen darin. Erstens Prüfteil C, das mit 41 statt 40 s die vertragliche Taktzeit verfehlt. Zweitens der Staubwert bei verzinktem Blech, der mit 92 % knapp ist und noch im Sommerbetrieb gemessen werden muss. Was passiert, wenn diese Messung den Richtwert überschreitet? Wer zahlt dann eine stärkere Absaugung, wenn die Anlage schon abgenommen ist? Offen ist auch, warum gerade 5 % angemessen sind und welcher Betrag das ist.

3. **Wie sichern wir den laufenden Betrieb in der Übergangszeit ab?**
   Mehrere Punkte hängen hier zusammen. Es gibt nur zwei geschulte Bediener und noch keine Vertretung. Es liegen nur zwei Schutzgläser auf Lager, die Lieferzeit beträgt drei bis sechs Wochen und das Glas muss häufiger gewechselt werden. Bis zum Update werden Programme teilweise von Hand übertragen. Und die Altanlage hat als Reserve keinen Wartungsvertrag. Die Fragen dazu: Wann und für welchen Betrag wird die Schulung beauftragt? Wie viele Schutzgläser sollen auf Lager gehen? Soll die Altanlage verkauft werden, bevor diese Punkte geklärt sind?
