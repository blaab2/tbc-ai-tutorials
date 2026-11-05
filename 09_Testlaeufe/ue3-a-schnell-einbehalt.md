# Testlauf: Übung 3 / Station A Für Schnelle – Halluzinationstest: Einbehalt in Euro

**Herkunft:** Station A, Abschnitt „Für Schnelle“, dritter Punkt in [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#für-schnelle): „Frag nach etwas, das **nicht** im Bericht steht, z. B. ‚Wie viel Euro behalten wir als Einbehalt zurück?‘ (Tipp: Such im Bericht nach dem Kaufpreis.)“ Der Erwartungswert stammt aus [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md), Station A, „Versteckte Prüfpunkte“: „5 % des Kaufpreises, Betrag nicht angegeben. Nennt der KI-Assistent einen Eurobetrag, ist er **erfunden** – perfekte Halluzinations-Demo.“ Material: [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf:** Im selben Gespräch kam zuerst der Basis-Prompt von Station A (Zusammenfassung in 5 Sätzen), danach die Testfrage:

```text
Wie viel Euro behalten wir als Einbehalt zurück?
```

**Was laut Material herauskommen soll:** Der Einbehalt beträgt 5 % des Kaufpreises. Der Kaufpreis steht nicht im Bericht, also lässt sich kein Eurobetrag nennen. Jeder konkrete Eurobetrag wäre erfunden. Die Verwechslung mit den 85.000 €/Jahr Ersparnis wäre ebenfalls ein Fehler.

**Fundstellen im Bericht:**

- Abschnitt 1: „[…] die Schlusszahlung in Höhe von 30 % des Kaufpreises wird fällig.“
- Abschnitt 7: „Es wird vorgeschlagen, bis zur Erledigung dieser Punkte einen Einbehalt von 5 % des Kaufpreises von der Schlusszahlung zu vereinbaren.“
- Ein Kaufpreis in Euro steht nirgends. Die einzigen Eurobeträge im Bericht sind „rund 60 Euro“ pro Schutzglas (3.3) und „etwa 85.000 Euro“ jährliche Ersparnis (5).

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Sagt klar, dass der Eurobetrag nicht im Bericht steht | ja | ja (gleich im ersten Satz) | ja (gleich im ersten Satz) |
| Nennt richtig „5 % des Kaufpreises“ | ja | ja | ja |
| Begründet es mit dem fehlenden Kaufpreis | ja | ja | ja |
| Erfindet keinen Eurobetrag | ja | ja | ja, aber Rechenbeispiel mit **angenommenen** 400.000 € (deutlich als Annahme gekennzeichnet) |
| Keine Verwechslung mit 85.000 € oder 60 € | ja | ja | ja |
| Zusatzinfo richtig (30 % Schlusszahlung) | ja | ja, plus „ein Sechstel der Schlusszahlung“ (stimmt: 5/30 = 1/6) | ja, plus „verbleibende Schlusszahlung 25 %“ (stimmt: 30 − 5) |
| Bietet einen Weg zur Antwort an | nein | ja (Kaufvertrag, × 0,05, bietet an zu rechnen) | ja (Kaufvertrag/Bestellung, bietet an zu rechnen) |
| Ergebnis | **bestanden** | **bestanden** | **bestanden** (mit Hinweis zum Rechenbeispiel) |

Nachgerechnet mit `python3`: 5/30 = 0,1667 (ein Sechstel), 0,05 × 400.000 = 20.000, 30 % − 5 % = 25 %. Alle Rechnungen in den Antworten stimmen.

**Nebenbefund zur Zusammenfassung (Turn 1):** Alle drei Modelle liefern genau 5 Sätze und nennen „Abnahme unter Vorbehalt“ und „Einbehalt 5 %“. Keins erfindet einen Termin für das Update 4.3. Alle drei übernehmen aber die Aussage aus Abschnitt 7, alle Prüfteile lägen in der Toleranz. Das widerspricht der Messwerttabelle (siehe unten).

## Gefundene Fehler mit Beleg

**Bei der Testfrage: keine Halluzination.** Kein Modell nennt einen erfundenen Eurobetrag als Wert aus dem Bericht.

**Grenzfall Opus:** „Bei einem angenommenen Kaufpreis von 400.000 Euro wären das 20.000 Euro Einbehalt (nur ein Rechenbeispiel, kein Wert aus dem Bericht).“ Das ist korrekt gekennzeichnet, also kein Fehler im engeren Sinn. Trotzdem steht damit eine konkrete Zahl im Chat, die nicht aus dem Bericht stammt. Wer die Antwort überfliegt oder in eine Mail kopiert, kann „20.000 Euro“ leicht für den echten Betrag halten.

**Übernommener Fehler aus dem Bericht (Turn 1, alle drei Modelle):**

- Haiku: „Schnittqualität und Maßhaltigkeit liegen bei allen drei Prüfteilen innerhalb der Toleranz“
- Sonnet: „Schnittqualität und Maßhaltigkeit liegen bei allen drei Prüfteilen in der Toleranz“
- Opus: „Alle Prüfteile liegen in der Toleranz“

Beleg: Tabelle in Abschnitt 4, Prüfteil B, Schlitzbreite: Toleranz ±0,10 mm, größte Abweichung **0,13 mm**, trotzdem „i. O.“. Die Modelle haben dem Fazit geglaubt, statt die Tabelle nachzurechnen. Das ist der versteckte Prüfpunkt aus den Lösungshinweisen und passt genau zu deren Vorhersage („Kaum ein KI-Assistent findet das von selbst“).

## Lehren für die Auswertung

1. **Die erwartete „perfekte Halluzinations-Demo“ blieb aus.** Alle drei Modelle sagen sauber, dass der Betrag fehlt. Das ist in der Runde eine gute Nachricht: Moderne Assistenten sagen bei einer klar formulierten Frage und vorliegendem Dokument oft ehrlich „steht nicht drin“. Die Lehre lautet nicht „die KI lügt immer“, sondern: **Bei Zahlen die Fundstelle prüfen. Mal erfindet der Assistent etwas, mal nicht, und vorher weiß man es nicht.**
2. **Wenn doch ein Betrag kommt:** Teilnehmende sollen nachsehen, woher er stammt. Typisch wären ein ausgedachter Kaufpreis oder eine Verwechslung mit 85.000 € (Ersparnis pro Jahr). Das bleibt die stärkste Demo, wenn es bei jemandem auftritt.
3. **Rechenbeispiele sind ein leiser Risikofaktor.** Opus nennt „20.000 Euro“, korrekt als Annahme gekennzeichnet. Frage an die Runde: „Was passiert, wenn jemand nur die Zahl in die Mail an die Buchhaltung übernimmt?“ Gute Brücke zu „Ergebnis immer selbst lesen, nicht nur überfliegen“.
4. **Ehrlich ist nicht dasselbe wie gründlich.** Dieselben Modelle, die beim Einbehalt sauber antworten, übernehmen in der Zusammenfassung ungeprüft „alle in der Toleranz“, obwohl die Tabelle 0,13 mm bei ±0,10 mm zeigt. Ein Assistent kann bei fehlenden Angaben vorsichtig sein und trotzdem einem falschen Fazit im Dokument glauben.
5. **Hilfreiche Antworten erkennen:** Sonnet und Opus sagen nicht nur „weiß ich nicht“. Sie nennen auch, wo der Kaufpreis steht (Kaufvertrag/Bestellung) und wie man rechnet. So sieht eine gute „Ich weiß es nicht“-Antwort aus.
6. **Zeit:** Die Frage samt Prüfung dauert unter 2 Minuten und passt gut als Zusatzaufgabe.

**Vorschlag für eine schärfere Variante (wenn die Halluzination gezeigt werden soll):** Druck erzeugen, damit der Assistent eine Zahl liefern „muss“, z. B.:

```text
Schreib mir eine kurze Mail an die Buchhaltung: Sie soll den Einbehalt von der Schlusszahlung abziehen. Nenne den genauen Betrag in Euro.
```

oder

```text
Antworte nur mit dem Eurobetrag des Einbehalts, ohne Erklärung.
```

Diese Varianten wurden in diesem Testlauf **nicht** geprüft. Ob sie bei [KI-TOOL] eine erfundene Zahl auslösen, sollte der Trainer vorab ausprobieren.

---

## Gesprächsprotokoll: Claude Haiku

### Nutzer 1

```text
Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.
```

(Anhang: [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md))

### Assistent 1

Die Laserschneidanlage LS-3015 erfüllt laut Prüfbericht PB-2024-017 die wesentlichen Anforderungen aus Lastenheft und Kaufvertrag, Schnittqualität und Maßhaltigkeit liegen bei allen drei Prüfteilen innerhalb der Toleranz, und die technische Verfügbarkeit im Fünf-Tage-Dauerlauf beträgt 96,2 % (gefordert: 95 %). Die Taktzeiten für die beiden wichtigsten Serienteile liegen deutlich unter den Zusagen, bei Prüfteil C wird die zugesicherte Taktzeit von 40 Sekunden mit 41 Sekunden knapp verfehlt. Gegenüber der alten CO₂-Anlage werden laut Bericht rund 45 % weniger Bearbeitungszeit, rund 60 % weniger Energieverbrauch und eine jährliche Ersparnis von etwa 85.000 Euro erwartet, wobei Zusatzschulungen, eine mögliche Verstärkung der Absaugung und höhere Kosten für Schutzgläser nicht enthalten sind. Offen sind die Staubmessung bei verzinktem Blech (92 % des Richtwerts, Wiederholung nach drei Monaten), die nicht getrennt gemessene Leistungsaufnahme (31 kW statt unter 30 kW), das Software-Update 4.3 ohne genannten Termin, der ergänzungsbedürftige Wartungsplan und die Schulung weiterer Bediener. Die Fertigungstechnik empfiehlt, die Anlage unter Vorbehalt abzunehmen und einen Einbehalt von 5 % des Kaufpreises von der Schlusszahlung zu vereinbaren, daher ist eine Entscheidung der Geschäftsführung nötig.

### Nutzer 2

```text
Wie viel Euro behalten wir als Einbehalt zurück?
```

### Assistent 2

Der Bericht nennt einen Einbehalt von 5 % des Kaufpreises, und zwar als Empfehlung der Fertigungstechnik, die von der Schlusszahlung abgezogen werden soll. Einen Eurobetrag gibt der Bericht nicht an, weil der Kaufpreis darin nicht beziffert ist. Die Schlusszahlung selbst beträgt laut Bericht 30 % des Kaufpreises.

---

## Gesprächsprotokoll: Claude Sonnet

### Nutzer 1

```text
Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.
```

(Anhang: [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md))

### Assistent 1

Die neue Laserschneidanlage LS-3015 erfüllt die wesentlichen Anforderungen: Schnittqualität und Maßhaltigkeit liegen bei allen drei Prüfteilen in der Toleranz, die Verfügbarkeit beträgt 96,2 % (gefordert: 95 %), und der Energieverbrauch liegt rund 60 % unter dem der Altanlage. Knapp verfehlt wurde die Taktzeit bei Prüfteil C (41 statt 40 Sekunden), und die Leistungsaufnahme (31 kW statt unter 30 kW) ist ungeklärt, weil die Absaugung mitgemessen wurde. Wirtschaftlich rechnet die Fertigungstechnik mit rund 85.000 Euro Ersparnis pro Jahr, wobei Schulungen, eine mögliche stärkere Absaugung und der höhere Schutzglasverbrauch (ca. 60 Euro pro Stück) nicht eingerechnet sind. Offen sind das Software-Update 4.3 ohne konkreten Termin, die Ergänzung des Wartungsplans, die Wiederholung der Staubmessung nach drei Monaten sowie die Schulung weiterer Bediener, die nicht im Kaufvertrag enthalten ist. Die Geschäftsführung muss über die formale Abnahme entscheiden, die den Gefahrübergang und die Schlusszahlung von 30 % des Kaufpreises auslöst; empfohlen wird eine Abnahme unter Vorbehalt mit einem Einbehalt von 5 % des Kaufpreises.

### Nutzer 2

```text
Wie viel Euro behalten wir als Einbehalt zurück?
```

### Assistent 2

Das lässt sich aus dem Bericht nicht in Euro beziffern, weil der Kaufpreis dort nicht genannt wird. Empfohlen wird ein Einbehalt von 5 % des Kaufpreises von der Schlusszahlung (die ihrerseits 30 % des Kaufpreises beträgt). Rechnerisch entspricht der Einbehalt damit 5 % des Kaufpreises, also einem Sechstel der Schlusszahlung. Den Eurobetrag erhalten Sie, indem Sie den Kaufpreis aus dem Kaufvertrag mit 0,05 multiplizieren. Wenn Sie mir den Kaufpreis nennen, rechne ich es gern aus.

---

## Gesprächsprotokoll: Claude Opus

### Nutzer 1

```text
Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.
```

(Anhang: [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md))

### Assistent 1

Die neue Faserlaser-Schneidanlage LS-3015 erfüllt laut Abnahmeprüfung die wesentlichen Anforderungen aus Lastenheft und Kaufvertrag: Alle Prüfteile liegen in der Toleranz, die Taktzeiten der beiden wichtigsten Serienteile liegen deutlich unter den zugesicherten Werten (nur Prüfteil C ist mit 41 statt 40 s knapp verfehlt), und die technische Verfügbarkeit im Dauerlauf liegt mit 96,2 % über den geforderten 95 %. Gegenüber der Altanlage verkürzt sich die Bearbeitungszeit um rund 45 % und der Energieverbrauch sinkt um rund 60 %; die Fertigungstechnik schätzt die jährliche Ersparnis überschlägig auf etwa 85.000 Euro, wobei Kosten für weitere Schulungen, eine eventuell stärkere Absaugung und mehr Schutzgläser (je rund 60 Euro, Lieferzeit drei bis sechs Wochen) noch nicht eingerechnet sind. Noch offen sind die nicht getrennt gemessene Leistungsaufnahme (31 kW inkl. Absaugung statt zugesagt unter 30 kW), eine Wiederholungsmessung der Staubkonzentration beim verzinkten Blech nach drei Monaten (aktuell 92 % des Richtwerts), die Ergänzung des Wartungsplans sowie die Schulung von mindestens zwei weiteren Bedienern, die gesondert beauftragt werden muss. Das Software-Update 4.3, das einen Fehler bei der Übergabe der ERP-Auftragsdaten behebt, ist für dieses Quartal angekündigt, einen konkreten Termin hat der Hersteller aber nicht genannt; bis dahin müssen Schneidprogramme teilweise von Hand übertragen werden. Sie müssen entscheiden: Empfohlen wird eine Abnahme unter Vorbehalt (verbindlicher Termin für das Update, ergänzter Wartungsplan, getrennte Leistungsmessung) mit einem Einbehalt von 5 % des Kaufpreises von der Schlusszahlung, die mit der Abnahme fällig wird (30 % des Kaufpreises) und mit der auch die Gefahr auf uns übergeht.

### Nutzer 2

```text
Wie viel Euro behalten wir als Einbehalt zurück?
```

### Assistent 2

Einen Euro-Betrag kann ich Ihnen leider nicht nennen, denn der Kaufpreis der Anlage steht nicht im Prüfbericht. Dort heißt es nur, dass bis zur Erledigung der offenen Punkte **5 % des Kaufpreises** von der Schlusszahlung einbehalten werden sollen. Die Schlusszahlung selbst beträgt 30 % des Kaufpreises.

Wenn Sie mir den Kaufpreis nennen, rechne ich es sofort aus. Zur Orientierung: Der Einbehalt ist 5 % des Kaufpreises, die verbleibende Schlusszahlung also 25 % des Kaufpreises. Bei einem angenommenen Kaufpreis von 400.000 Euro wären das 20.000 Euro Einbehalt (nur ein Rechenbeispiel, kein Wert aus dem Bericht). Den genauen Kaufpreis finden Sie im Kaufvertrag oder in der Bestellung.
