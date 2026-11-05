# Testlauf: Übung 3 / Trainer-Zusatz – Station A + C kombiniert: Fr. Yilmaz' Zusammenfassung für den Jour fixe

**Herkunft:** Zusatzaufgabe für Schnelle in [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md), Übung 3, „Zusatzaufgaben für Schnelle“: „Station A + C kombinieren: ‚Schreib Fr. Yilmaz' Zusammenfassung für den Jour fixe' (Aufgabe 3 aus den Notizen) – verbindet beide Materialien.“ Übungsblatt: [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md). Material: [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt) (Station C) und [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md) (Station A).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Verwendeter Prompt** (aus dem Trainer-Hinweis ausformuliert, beide Dateien angehängt):

```text
Hier sind meine Notizen aus der letzten Teambesprechung und der Prüfbericht zur Laserschneidanlage LS-3015.
Schreib Fr. Yilmaz' Zusammenfassung für den Jour fixe (Aufgabe 3 aus den Notizen): kurz, für die Geschäftsführung, mit Empfehlung und offenen Punkten. Schreib nichts, was nicht im Bericht steht.
```

**Was laut Material herauskommen soll** (Lösungstabelle Station A und Aufgabe 3 aus Station C):

- Der KI-Assistent erkennt in den Notizen die Aufgabe „Fr. Yilmaz liest + fasst zusammen für GF, bis zum nächsten Jour fixe“ und erledigt sie mit dem Bericht.
- Enthalten: Empfehlung **Abnahme unter Vorbehalt** mit den drei Bedingungen, **Einbehalt 5 %** des Kaufpreises, **Schlusszahlung 30 %**, offene Punkte Taktzeit C, Leistungsaufnahme/Energie, Staubmessung, Wartungsplan/Schutzglas, Software-Update 4.3, Schulung.
- Nicht enthalten: Eurobetrag für Einbehalt oder Schlusszahlung (der Kaufpreis steht nicht im Bericht), ein ausgerechnetes Jour-fixe-Datum (die Notizen sagen nur „in 2 Wo“, das Besprechungsdatum ist „Di (?)“).
- Bonus laut „Versteckte Prüfpunkte“: Schutzglas als Stillstandsrisiko (2 Stück Lager, 3–6 Wochen Lieferzeit), Altanlage ohne Wartungsvertrag, Widerspruch Schlitzbreite (0,13 mm bei ±0,10 mm, trotzdem „i. O.“).

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Aufgabe 3 aus den Notizen richtig erkannt | ja (stillschweigend) | ja | ja |
| Empfehlung „Abnahme unter Vorbehalt“ mit allen 3 Bedingungen | ja | ja | ja |
| Einbehalt 5 % des Kaufpreises | ja | ja | ja |
| Schlusszahlung 30 % | ja | ja | ja |
| Offene Punkte: Taktzeit C, Energie, Staub, Update 4.3, Schulung, Schutzglas | alle 6 | alle 6 | alle 6 |
| Schutzglas mit Lagerbestand und Lieferzeit | ja | ja | ja |
| Altanlage ohne Wartungsvertrag (Bonus) | nein | nein | ja |
| Widerspruch Schlitzbreite erkannt (Bonus) | nein – übernimmt „innerhalb der Toleranz“ | nein – übernimmt „innerhalb der Toleranz“ | nein – übernimmt „alle i. O.“ |
| Kein Eurobetrag für Einbehalt | ja | ja | ja, und sagt ausdrücklich, dass der Kaufpreis fehlt |
| Kein erfundenes Jour-fixe-Datum / keine erfundenen Fristen | ja | ja | ja, und weist auf fehlende Termine hin |
| Hinweis auf Status „Entwurf zur Freigabe“ | nur in der Überschrift | ja, eigener Hinweis | nur in der Überschrift |
| „Kurz“ eingehalten | eher nein (ca. 1 Seite, inkl. aller Punkte aus Abschnitt 6) | mittel (ca. 1 Seite) | eher nein (längste Fassung, aber mit „Benötigte Entscheidung“) |
| Sachliche Fehler | keine echten, kleine Zuspitzung („verlangt“) | keine echten, kleine Unschärfen | keine echten, eine Zuspitzung („verpflichtet sich“) |
| Gesamt | **bestanden** | **bestanden** | **bestanden, beste Fassung** |

Nachgerechnet mit `python3`: Verfügbarkeit (80 h × 60 − 35 − 130 − 20 min) / (80 h × 60) = 96,15 % ≈ 96,2 %. Alle in den Antworten genannten Zahlen (82/95 s, 64/70 s, 41/40 s, 96,2 %, 31 kW, 92 %, 60 €, 2 Stück, 3–6 Wochen, 45 %, 60 %, 85.000 €, 5 %, 30 %) stimmen mit dem Bericht überein.

## Gefundene Fehler mit Beleg

Keine erfundenen Zahlen, Beträge, Termine oder Namen. Die Abweichungen sind klein, eignen sich aber gut für die Auswertung.

1. **Alle drei: Widerspruch Schlitzbreite übernommen.** Haiku und Sonnet schreiben „Schnittqualität und Maßhaltigkeit [liegen] bei allen drei Prüfteilen innerhalb der Toleranz“, Opus „Alle Prüfmaße der drei Prüfteile sind ‚in Ordnung‘“. Beleg Abschnitt 4: „B – Seitenwand 3 mm | Schlitzbreite | 4,00 | ±0,10 | 4,07 | 0,13 | i. O.“ – 0,13 mm liegt außerhalb von ±0,10 mm. Die Modelle glauben dem Fazit aus Abschnitt 7, statt nachzurechnen. Genau das sagen die Lösungshinweise voraus.
2. **Opus: „Im schriftlichen Vorbehalt verpflichtet sich der Hersteller zu drei Punkten.“** Der Bericht schlägt das nur vor: „Der Vorbehalt soll schriftlich festhalten, dass der Hersteller …“ (Abschnitt 7). Ob der Hersteller zustimmt, ist offen. Für eine Entscheidungsvorlage ist das eine relevante Zuspitzung.
3. **Haiku: Die Fachkraft für Arbeitssicherheit hat die Wiederholungsmessung „verlangt“.** Im Bericht: „hat […] darum gebeten, die Messung nach drei Monaten zu wiederholen“ (3.4). Kleine Verschärfung im Ton.
4. **Sonnet: „Das liegt am optimierten Parametersatz“** (Taktzeit C). Im Bericht ist das die Begründung des Herstellers: „Die Abweichung […] wurde vom Hersteller mit dem geänderten Parametersatz begründet“ (3.2). Haiku und Opus schreiben richtig „laut Hersteller“. Aus einer Behauptung des Lieferanten wird bei Sonnet eine Tatsache.
5. **Sonnet: „Die Wiederholungsmessung (Sommerbetrieb, nach drei Monaten) steht aus.“** Der Bericht nennt beides getrennt: Die Wiederholungsmessung im Sommerbetrieb steht aus, und die Fachkraft bittet um eine Messung nach drei Monaten (3.4). Wahrscheinlich ist dieselbe Messung gemeint, der Bericht sagt das aber nicht. Kleine Unschärfe.
6. **Haiku: „kurz“ nicht umgesetzt.** Haiku nimmt alle vier Anmerkungen aus Abschnitt 6 (Ablagefläche, Fernwartung, Erstmusterprüfung, Hallenplan) mit auf. Das ist nicht falsch, für die Geschäftsführung aber zu viel. Opus lässt sie bewusst weg und sagt das auch.

Keins der Modelle rechnet aus den Notizen ein Jour-fixe-Datum aus („in 2 Wo“, Besprechungstag „Di (?)“). Keins nennt einen Eurobetrag für Einbehalt oder Schlusszahlung. Keins vermischt Inhalte aus den Notizen (Brenner, SG-40-Lieferung, Messe) mit der Zusammenfassung.

## Lehren für die Auswertung

- **Die Kombination funktioniert.** Alle drei Modelle finden die richtige Aufgabe in den Notizen und erledigen sie nur mit dem Bericht. Die Zusatzaufgabe zeigt gut, wie man vom Protokoll direkt zum nächsten Arbeitsschritt kommt.
- **„Schreib nichts, was nicht im Bericht steht“ wirkt.** Keine erfundenen Beträge oder Termine. Opus sagt sogar von sich aus, dass Kaufpreis und Fristen fehlen und woher sie kommen müssten (Kaufvertrag, Fertigungstechnik). Diese Stelle eignet sich zum Vorlesen: Gute Antworten sagen auch, was **nicht** drinsteht.
- **Trotzdem ist die Zusammenfassung „zu gläubig“.** Alle drei übernehmen „alle Maße in Toleranz“, obwohl die Tabelle etwas anderes zeigt. Der Zusatz im Prompt verhindert Erfindungen, aber keine übernommenen Fehler aus der Quelle. Als Nachfrage zeigen: „Überprüfe die Messwerttabelle in Abschnitt 4: Liegen alle Abweichungen wirklich innerhalb der Toleranz? Rechne jede Zeile einzeln nach.“
- **Kleine Verschiebungen in der Bedeutung beachten:** „gebeten“ wird zu „verlangt“ (Haiku), „laut Hersteller“ wird zur Tatsache (Sonnet), „soll festhalten“ wird zu „verpflichtet sich“ (Opus). Bei einer Vorlage für die Geschäftsführung zählen solche Feinheiten. Gute Übung: drei Sätze im Original nachschlagen.
- **„Kurz“ ist zu unscharf.** Alle drei liefern rund eine Seite. Wer wirklich eine kurze Fassung will, muss es messbar machen, z. B. „höchstens 10 Zeilen“ oder „eine halbe Seite“. Sonnet fragt selbst nach, ob es kürzer sein soll.
- **Modellunterschiede:** Opus ist am vollständigsten (Altanlage, Arbeitssicherheit, Einschichtbetrieb, „Benötigte Entscheidung“) und erklärt, was weggelassen wurde. Sonnet weist als einziges deutlich auf den Entwurfsstatus hin. Haiku ist inhaltlich richtig, gewichtet aber nicht (alles drin, auch Kleinkram).

## Hinweise zum Material

- Der Trainer-Hinweis besteht nur aus einer Zeile. Es fehlt eine kurze Erwartung, woran man ein gutes Ergebnis erkennt. Die Kriterien lassen sich aus Station A übernehmen (Lösungstabelle und „Versteckte Prüfpunkte“). Vorschlag siehe Ergebnis dieses Testlaufs.
- Der Prompt „Schreib Fr. Yilmaz' Zusammenfassung“ funktioniert nur, wenn beide Dateien im selben Gespräch sind. Das sollte im Hinweis stehen.

---

## Gesprächsprotokoll: Haiku

### Nutzer 1
Hier sind meine Notizen aus der letzten Teambesprechung und der Prüfbericht zur Laserschneidanlage LS-3015.
Schreib Fr. Yilmaz' Zusammenfassung für den Jour fixe (Aufgabe 3 aus den Notizen): kurz, für die Geschäftsführung, mit Empfehlung und offenen Punkten. Schreib nichts, was nicht im Bericht steht.

[Anhang: notizen_besprechung.txt, pruefbericht_lang.md]

### Assistent 1
**Zusammenfassung Abnahmeprüfung Laserschneidanlage LS-3015** (Prüfbericht PB-2024-017, Version 1.0, Status: Entwurf zur Freigabe)

**Kurz gefasst:** Die Anlage erfüllt nach dem Bericht die wesentlichen Anforderungen aus Lastenheft und Kaufvertrag. Schnittqualität und Maßhaltigkeit sind bei allen drei Prüfteilen innerhalb der Toleranz, die Verfügbarkeit im Dauerlauf liegt bei 96,2 % (Anforderung: mindestens 95 %). Bei zwei Kennwerten gibt es Abweichungen bzw. ungeklärte Punkte (siehe unten).

**Ergebnisse im Überblick**
- **Schnittqualität:** Bei Edelstahl und Verzinktem sehr gut, gratfrei. Bei 8 mm Baustahl trat leichte Bartbildung auf, die durch optimierte Parameter deutlich reduziert wurde.
- **Taktzeiten:** Prüfteil A 82 s (zugesichert: max. 95 s), Prüfteil B 64 s (max. 70 s), Prüfteil C 41 s (max. 40 s, knapp verfehlt).
- **Wirtschaftlich:** Geschätzte jährliche Ersparnis von rund 85.000 Euro gegenüber der Altanlage. Der Energieverbrauch liegt rund 60 % darunter, die Bearbeitungszeit rund 45 %. Nicht enthalten sind zusätzliche Schulungen, eine eventuell nötige Verstärkung der Absaugung und ein höherer Verbrauch an Schutzgläsern.

**Empfehlung der Fertigungstechnik:** Die Anlage unter Vorbehalt abnehmen. Der Vorbehalt soll schriftlich festhalten, dass der Hersteller
1. das Software-Update 4.3 bis zu einem verbindlichen Termin bereitstellt,
2. den Wartungsplan um das Wechselintervall des Schutzglases bei verzinktem Material ergänzt,
3. eine getrennte Messung der Leistungsaufnahme ohne Absaugung durchführt.

Vorgeschlagen wird, bis zur Erledigung dieser Punkte einen Einbehalt von 5 % des Kaufpreises von der Schlusszahlung (30 %) zu vereinbaren.

**Offene Punkte**
- **Taktzeit Prüfteil C:** 41 s statt max. 40 s. Der Hersteller begründet die Abweichung mit dem Parametersatz, der die Kantenqualität verbessert.
- **Leistungsaufnahme Schneidbetrieb:** 31 kW statt unter 30 kW. Die Messung enthielt die Absaugung, eine getrennte Messung fehlt.
- **Staub beim Schneiden von verzinktem Blech:** 92 % des Richtwerts, also knapp unter der Grenze. Die Messung erfolgte bei geschlossener Hallentür. Eine Wiederholungsmessung nach drei Monaten hat die Fachkraft für Arbeitssicherheit verlangt. Die Anlage ist bis dahin vorläufig freigegeben.
- **Schutzglas:** Bei verzinktem Material muss es häufiger gewechselt werden als im Standardplan vorgesehen. Ein Stück kostet rund 60 Euro, zwei sind auf Lager, die Lieferzeit beträgt laut Hersteller drei bis sechs Wochen.
- **Software:** Version 4.3 ist angekündigt, ein Termin fehlt. Bis dahin müssen Schneidprogramme teilweise manuell übertragen werden.
- **Schulung:** Bisher haben zwei Bediener die Herstellerschulung absolviert. Für Vertretung und eine mögliche zweite Schicht sind mindestens zwei weitere nötig. Das ist im Kaufvertrag nicht enthalten und müsste gesondert beauftragt werden.
- **Weitere Hinweise der Beteiligten:** zusätzliche Ablagefläche für Restgitter, Fernwartungs-Zugangsdaten auf sicherem Weg statt per E-Mail, eine Erstmusterprüfung für Prüfteil C nach jedem Parameterwechsel (Vorschlag der Qualitätssicherung), und der neue Materialfluss in Halle 3 ist noch nicht im Hallenplan eingezeichnet.

## Gesprächsprotokoll: Sonnet

### Nutzer 1
Hier sind meine Notizen aus der letzten Teambesprechung und der Prüfbericht zur Laserschneidanlage LS-3015.
Schreib Fr. Yilmaz' Zusammenfassung für den Jour fixe (Aufgabe 3 aus den Notizen): kurz, für die Geschäftsführung, mit Empfehlung und offenen Punkten. Schreib nichts, was nicht im Bericht steht.

[Anhang: notizen_besprechung.txt, pruefbericht_lang.md]

### Assistent 1
Hier ist der Entwurf für den Jour fixe. Er stützt sich nur auf den Prüfbericht PB-2024-017 (Version 1.0, Status Entwurf zur Freigabe).

**Zusammenfassung Abnahmeprüfbericht Laserschneidanlage LS-3015**
*Für die Geschäftsführung, Jour fixe*

**Worum es geht**
Die neue Faserlaser-Schneidanlage LS-3015 ersetzt die CO₂-Anlage von 2009 in Halle 3. Die Geschäftsführung soll über die formale Abnahme entscheiden. Mit der Abnahme geht die Gefahr auf uns über, und die Schlusszahlung von 30 % des Kaufpreises wird fällig.

**Ergebnis**
- Schnittqualität und Maßhaltigkeit liegen bei allen drei Prüfteilen innerhalb der Toleranz.
- Die Taktzeiten bei den Prüfteilen A (82 s, zugesichert 95 s) und B (64 s, zugesichert 70 s) sind besser als zugesichert.
- Die Verfügbarkeit im Dauerlauf beträgt 96,2 % (gefordert: mindestens 95 %).
- Gegenüber der Altanlage ist die Bearbeitungszeit rund 45 % kürzer und der Energieverbrauch rund 60 % niedriger. Die Fertigungstechnik schätzt die Ersparnis auf etwa 85.000 Euro pro Jahr. Schulungen, eine eventuell nötige stärkere Absaugung und der höhere Schutzglasverbrauch sind dabei nicht eingerechnet.

**Empfehlung der Fertigungstechnik**
Die Anlage soll **unter Vorbehalt abgenommen** werden. Der Vorbehalt soll schriftlich festhalten, dass der Hersteller
1. das Software-Update 4.3 bis zu einem verbindlichen Termin bereitstellt,
2. den Wartungsplan um das Wechselintervall des Schutzglases ergänzt und
3. die Leistungsaufnahme getrennt, ohne Absaugung, misst.

Bis diese Punkte erledigt sind, wird ein Einbehalt von 5 % des Kaufpreises von der Schlusszahlung vorgeschlagen.

**Offene Punkte**
- **Taktzeit Prüfteil C:** 41 s statt zugesichert 40 s. Das liegt am optimierten Parametersatz, der die Kantenqualität verbessert.
- **Leistungsaufnahme:** 31 kW im Schneidbetrieb, zugesichert war "unter 30 kW". Die Absaugung wurde mitgemessen, daher ist die Bewertung unklar.
- **Staubkonzentration bei verzinktem Blech:** 92 % des Richtwerts, also knapp unter der Grenze. Gemessen wurde bei geschlossener Hallentür. Die Wiederholungsmessung (Sommerbetrieb, nach drei Monaten) steht aus. Die Fachkraft für Arbeitssicherheit hat vorläufig freigegeben.
- **Schutzglas:** Bei verzinktem Material muss es häufiger gewechselt werden als im Wartungsplan vorgesehen. Es kostet rund 60 Euro, zwei Stück sind auf Lager, und die Lieferzeit beträgt 3 bis 6 Wochen.
- **Software:** Version 4.2 läuft derzeit. Das Update auf 4.3 soll im Laufe des Quartals kommen, einen konkreten Termin gibt es nicht. Bis dahin müssen Schneidprogramme teilweise manuell übertragen werden.
- **Schulung:** Geschult sind bisher zwei Bediener. Für Vertretung und eine mögliche zweite Schicht sind mindestens zwei weitere nötig. Das ist im Kaufvertrag nicht enthalten und müsste gesondert beauftragt werden.

**Hinweis:** Der Bericht ist noch ein Entwurf (Version 1.0, "zur Freigabe"). Die Zahlen können sich also noch ändern.

Möchten Sie eine noch kürzere Fassung, zum Beispiel eine halbe Seite oder nur die Entscheidungsvorlage?

## Gesprächsprotokoll: Opus

### Nutzer 1
Hier sind meine Notizen aus der letzten Teambesprechung und der Prüfbericht zur Laserschneidanlage LS-3015.
Schreib Fr. Yilmaz' Zusammenfassung für den Jour fixe (Aufgabe 3 aus den Notizen): kurz, für die Geschäftsführung, mit Empfehlung und offenen Punkten. Schreib nichts, was nicht im Bericht steht.

[Anhang: notizen_besprechung.txt, pruefbericht_lang.md]

### Assistent 1
Hier ist ein Entwurf für Fr. Yilmaz. Alle Angaben stammen aus dem Prüfbericht PB-2024-017.

---

**Zusammenfassung für die Geschäftsführung: Abnahmeprüfung Laserschneidanlage LS-3015**
(Grundlage: Prüfbericht PB-2024-017, Version 1.0, Status „Entwurf zur Freigabe“)

**Worum es geht**
Die Geschäftsführung muss über die formale Abnahme der neuen Faserlaser-Anlage in Halle 3 entscheiden. Mit der Abnahme geht die Gefahr auf uns über, und die Schlusszahlung von 30 % des Kaufpreises wird fällig.

**Ergebnis in Kürze**
Die Anlage erfüllt die wesentlichen Anforderungen aus Lastenheft und Kaufvertrag:
- **Maßhaltigkeit:** Alle Prüfmaße der drei Prüfteile sind „in Ordnung“. Schnittqualität bei Teil A und B sehr gut. Bei Teil C (8 mm) gab es leichte Bartbildung, die ein angepasster Parametersatz deutlich verringert hat.
- **Taktzeiten:** Teil A braucht 82 s (zugesichert ≤ 95 s), Teil B 64 s (≤ 70 s). Teil C braucht 41 s und verfehlt die zugesicherten 40 s damit knapp.
- **Verfügbarkeit im Dauerlauf:** 96,2 % (gefordert ≥ 95 %).
- **Arbeitssicherheit:** Laserschutz, Türverriegelungen und Not-Halt funktionieren einwandfrei. Die Fachkraft für Arbeitssicherheit hat die Anlage vorläufig freigegeben.
- **Wirtschaftlichkeit:** Gegenüber der Altanlage ist die Bearbeitung rund 45 % schneller und der Energieverbrauch rund 60 % niedriger. Voraussichtlich reicht künftig eine Schicht statt zwei. Die Fertigungstechnik schätzt die Ersparnis überschlägig auf ca. 85.000 € pro Jahr. Darin fehlen noch die Kosten für weitere Schulungen, eine eventuell nötige Verstärkung der Absaugung und den höheren Verbrauch an Schutzgläsern.

**Empfehlung der Fertigungstechnik: Abnahme unter Vorbehalt**
Im schriftlichen Vorbehalt verpflichtet sich der Hersteller zu drei Punkten:
1. Er liefert das Software-Update 4.3 bis zu einem verbindlichen Termin.
2. Er ergänzt den Wartungsplan um das Wechselintervall des Schutzglases bei verzinktem Material.
3. Er misst die Leistungsaufnahme getrennt, also ohne Absaugung.

Bis diese Punkte erledigt sind, sollen 5 % des Kaufpreises von der Schlusszahlung einbehalten werden.

**Offene Punkte**
- **Taktzeit Teil C:** 41 s statt 40 s. Laut Hersteller liegt das am langsameren Parametersatz, der die Kantenqualität verbessert.
- **Leistungsaufnahme:** Gemessen wurden 31 kW, zugesagt sind „unter 30 kW“. Der Wert enthält die Absaugung, eine getrennte Messung fehlt. Bewertung im Bericht: „unklar“.
- **Staub bei verzinktem Blech:** Der Messwert liegt bei 92 % des internen Richtwerts, gemessen bei geschlossener Hallentür. Die Wiederholungsmessung im Sommerbetrieb steht noch aus. Die Fachkraft für Arbeitssicherheit möchte nach drei Monaten erneut messen lassen.
- **Schutzglas:** Bei viel verzinktem Material muss es öfter gewechselt werden. Auf Lager sind 2 Stück (je ca. 60 €), die Lieferzeit beträgt laut Hersteller derzeit 3 bis 6 Wochen. Im Wartungsplan steht dazu noch nichts.
- **Software:** Bis zum Update 4.3 müssen Schneidprogramme wegen eines Fehlers bei der Übergabe aus dem ERP-System teilweise von Hand übertragen werden. Für das Update gibt es keinen konkreten Termin.
- **Schulung:** Bisher sind 2 Bediener geschult. Für Vertretung und eine mögliche zweite Schicht braucht es mindestens 2 weitere Personen. Diese Schulung ist nicht im Kaufvertrag enthalten und müsste extra beauftragt werden.
- **Altanlage:** Sie soll nach der Abnahme verkauft werden, ein Händler hat Interesse. Bis dahin steht sie als Reserve bereit, aber ohne Wartungsvertrag.

**Benötigte Entscheidung:** Freigabe der Abnahme unter Vorbehalt mit 5 % Einbehalt, wie oben beschrieben.

---

Zwei Hinweise dazu:
- Der Bericht nennt **weder den Kaufpreis noch Termine** für den Vorbehalt. Deshalb fehlen in der Zusammenfassung Euro-Beträge für den Einbehalt und konkrete Fristen. Diese Werte müssten aus dem Kaufvertrag oder von der Fertigungstechnik kommen.
- Die kleineren Anmerkungen aus Abschnitt 6 habe ich bewusst weggelassen, weil sie für die Abnahmeentscheidung nicht nötig sind. Gemeint sind die Ablagefläche, der sichere Weg für die Fernwartungs-Zugangsdaten, die Erstmusterprüfung für Teil C und der Hallenplan. Bei Bedarf kann ich sie als Anhang ergänzen.
