# Testlauf: Übung 3 / Station A Weiter – Risiken, Empfehlung zitieren, Widersprüche

**Herkunft:** Station A, Stufe „Weiter“ aus [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#station-a-langen-bericht-zusammenfassen) (Block 5). Material: [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md) (Abnahmeprüfbericht LS-3015, PB-2024-017). Zugehörige Lösungshinweise: [Trainer-Loesungshinweise.md – Station A](../06_Uebungen/Trainer-Loesungshinweise.md#station-a-prüfbericht-zusammenfassen). Die Basis-Stufe (Nutzer 1) ist separat ausgewertet in [ue3-a-basis.md](ue3-a-basis.md); hier geht es um die Nachfragen 2–4.

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf (je ein Chat, Bericht angehängt bzw. eingefügt):** Basis-Prompt (5 Sätze für die GF), dann nacheinander die drei Weiter-Prompts aus dem Übungsblatt:

```text
Welche Risiken oder offenen Punkte nennt der Bericht, die noch nicht gelöst sind?
Liste sie als Tabelle mit den Spalten: Risiko | Wie schlimm (laut Bericht) | Abschnitt im Bericht.
Wenn der Bericht zu einem Punkt keine Einschätzung enthält, schreib "keine Angabe".
```

```text
Was empfiehlt der Bericht als nächsten Schritt? Zitiere die entsprechende Stelle wörtlich.
```

```text
Gibt es Widersprüche oder Stellen, die unklar formuliert sind?
```

**Was laut Material herauskommen soll:** Eine vollständige Risikotabelle mit Abschnittsangaben, mindestens: Taktzeit C (41 s statt ≤ 40 s), Leistungsaufnahme (31 kW inkl. Absaugung statt „unter 30 kW“, unklar), Staub-Wiederholungsmessung (92 % des Richtwerts, Sommer/offene Tore, nach 3 Monaten), Wartungsplan Schutzglas, Software-Update 4.3 ohne Termin (ERP-Übergabe manuell), Schulung (nur 2 Bediener, nicht im Vertrag). Bonus: Schutzglas nur 2 auf Lager, Lieferzeit 3–6 Wochen; Altanlage ohne Wartungsvertrag. „keine Angabe“ statt erfundener Schweregrade. Das Zitat der Empfehlung muss wörtlich im Original auffindbar sein (Strg + F). Bonus bei den Widersprüchen: Prüfteil B, Schlitzbreite 0,13 mm bei ±0,10 mm als „i. O.“ bewertet, obwohl Abschnitt 7 „alle Maße in Toleranz“ behauptet; außerdem: ob „unter 30 kW“ mit oder ohne Absaugung gemeint ist, bleibt unklar.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| **Risikotabelle** | | | |
| Taktzeit C 41 s vs. ≤ 40 s | ja (3.2, 4) | ja (3.2, 4, 7) | ja (3.2, 4, 7) |
| Leistungsaufnahme 31 kW inkl. Absaugung, „unklar“ | ja | ja | ja |
| Staub 92 % / Sommer, offene Tore / nach 3 Monaten | 92 % ja, Sommer und 3 Monate **fehlen** in der Tabelle (3 Monate nur in der Zusammenfassung) | 92 % und Sommer/offene Tore ja, 3 Monate nur in der Zusammenfassung | 92 %, geschlossene Hallentür und Sommer ja, 3 Monate nur in Zusammenfassung und Widerspruchsliste |
| Wartungsplan Schutzglas | ja (3.6) | ja (zusammen mit Schutzglas-Verbrauch) | ja, eigene Zeile |
| Update 4.3 ohne Termin, ERP-Übergabe manuell | ja | ja („im Laufe des Quartals“) | ja |
| Schulung: nur 2 Bediener, nicht im Vertrag | ja | ja | ja |
| Bonus: Schutzglas 2 auf Lager, 3–6 Wochen | ja | ja, eigene Zeile | ja, eigene Zeile |
| Bonus: Altanlage ohne Wartungsvertrag | ja | ja | ja |
| Weitere Punkte (Abschnitt 6, Kosten, Bartbildung) | Abschnitt 6 vollständig, Kostenzeile aus 5 | Abschnitt 6 vollständig, Absaugungsverstärkung, Bartbildung C | Abschnitt 6 vollständig, Absaugungsverstärkung; Hinweis, dass Abschnitt 7 nur sechs Punkte nennt |
| „keine Angabe“ statt erfundener Schweregrade | ja, konsequent | teils: Spalte oft mit Fakten statt Schweregrad gefüllt („Abweichung von einer Sekunde“), aber nichts erfunden | ja, „keine Angabe“ plus wörtliche Belege in Klammern |
| Abschnittsangaben korrekt | ja (Abschnitt 7 nie mit angegeben, aber nichts falsch) | ja | ja |
| Erfundenes in der Tabelle? | nein | nein | nein |
| **Zitat der Empfehlung** | | | |
| Wörtlich im Original auffindbar (per `python3` geprüft) | **ja**, zeichengenau | **ja**, zeichengenau | **ja**, zeichengenau |
| Einordnung | nur Zitat | ein Satz Einordnung + Zitat | Einordnung + Zitat + nächster Schritt für die GF |
| **Widersprüche / Unklarheiten** | | | |
| Schlitzbreite B (0,13 mm bei ±0,10 mm, „i. O.“, vs. Abschnitt 7) | **ja** (Punkt 1 und 5) | **ja** (inkl. Mittelwert vs. Einzelwert) | **ja** (inkl. „vor der Abnahme klären“) |
| Energie „unter 30 kW“ mit/ohne Absaugung unklar | teilweise (Punkt 2) | teilweise (nur „Absaugung nicht getrennt gemessen“) | **ja**, genau benannt (Punkt 4) |
| Weitere gute Funde | Dokumentstatus „Entwurf“ | „wichtigste Serienteile“ nicht belegt, Kaufpreis fehlt, „im Laufe des Quartals“, Prüfumfang 10 Teile | Vorbehalt deckt nur 3 von 6 offenen Punkten ab, Staub „Sommer“ vs. „3 Monate“, kein Datum im Bericht, Richtwert nicht beziffert, nur Fertigungstechnik unterschreibt |
| Sachliche Fehler in der Antwort | **1** (Abschnitt 7 nenne die Leistungsaufnahme nicht – falsch) | **1** kleiner (Punkt „Sachfehler im Bericht“, der sich selbst widerlegt; 96,15 % als „stimmt“ für „96,2 %“) | keiner gefunden |
| **Gesamt** | gut, eine Falschaussage | gut, etwas unruhig | sehr gut |

**Kurz:** Die Weiter-Stufe funktioniert mit allen drei Modellen. Die Risikotabellen sind vollständig (inkl. beider Bonuspunkte), die Abschnittsangaben stimmen, kein Modell erfindet Schweregrade, und alle drei zitieren die Empfehlung zeichengenau. **Überraschend:** Alle drei finden den Widerspruch bei der Schlitzbreite, sobald explizit nach Widersprüchen gefragt wird – obwohl sie in der Basis-Zusammenfassung alle noch „bei allen drei Prüfteilen in der Toleranz“ übernommen hatten. Fehler gibt es nur im Kleingedruckten der Widerspruchsliste (Haiku, Sonnet).

---

## Gefundene Fehler mit Beleg

1. **Haiku – falsche Aussage über Abschnitt 7 (Widerspruchsliste, Punkt 2).** Haiku: „Die Zusammenfassung in Abschnitt 7 nennt die Leistungsaufnahme nicht.“ Abschnitt 7 sagt wörtlich: „Dazu gehören die knapp verfehlte Taktzeit bei Prüfteil C, **die nicht getrennt gemessene Leistungsaufnahme**, …“ und in der Empfehlung „(3) eine getrennte Messung der Leistungsaufnahme ohne Absaugung“. Ein schönes Beispiel für eine Halluzination **in der Prüf-Antwort selbst**: Ausgerechnet beim Suchen nach Widersprüchen erfindet das Modell einen.
2. **Haiku – kleine Ungenauigkeit (Punkt 2).** „Ob der Wert die Absaugung umfasst, ist nur über den Hinweis des Herstellers belegt.“ Der Bericht stellt selbst fest, dass die Absaugung „bei der Messung mit erfasst wurde“ (3.5) und schreibt in der Tabelle „31 kW (inkl. Absaugung)“ (4). Der Hersteller liefert nur die **Begründung** für die Überschreitung. Offen ist eigentlich, ob die Angebotsangabe „unter 30 kW“ mit oder ohne Absaugung gemeint war (so korrekt bei Opus, Punkt 4).
3. **Haiku – Überinterpretation (Punkt 7).** „Wer die Kosten [der Zusatzschulungen] trägt, wird nicht geregelt.“ Der Bericht sagt: „ist im Kaufvertrag nicht enthalten und müsste gesondert beauftragt werden“ (3.6) und zählt die Kosten als nicht eingerechnete eigene Kosten (5). Wer beauftragt, zahlt; die Unklarheit ist konstruiert.
4. **Sonnet – widersprüchlicher Punkt „Sachfehler im Bericht Abschnitt 3.3“.** Überschrift sagt „Sachfehler“, der Text kommt dann zum Ergebnis „was rechnerisch stimmt“. Nachgerechnet per `python3`: (4.800 − 185) / 4.800 = **96,146 %**, gerundet auf eine Stelle 96,1 %, nicht 96,2 %. Der Bericht rundet also leicht nach oben; „stimmt“ ist knapp daneben, die Aussage „≥ 95 % erfüllt“ bleibt richtig. Gleiches gilt für Opus („rund 96,2 % … schlüssig“). Für die Teilnehmenden irrelevant, für Trainer ein Detail, falls jemand nachrechnet.
5. **Sonnet – Meta-Hinweis als Unklarheit gewertet.** „Dokumentstatus … bei gleichzeitigem Hinweis, dass das Dokument fiktiv ist.“ Der Fiktiv-Hinweis ist Übungsmaterial, kein Inhalt des Berichts. Kein Fehler im engeren Sinn, aber ein Punkt, über den Teilnehmende stolpern könnten.
6. **Sonnet – „wichtigste Serienteile nirgends genannt“ (Punkt 1) ist nur halb richtig.** Abschnitt 1 nennt als Hauptzweck „Gehäuseteile … für die Produktlinien SG-40 und SG-60“, und A/B sind genau diese Teile (Abschnitt 2). Ausdrücklich „wichtigste“ steht dort zwar nicht, der Schluss liegt aber nahe. Opus formuliert das vorsichtiger (Punkt 10: „wird vorher nirgends gesagt“).
7. **Alle drei – Staub „nach 3 Monaten“ fehlt in der Tabelle.** Der Bericht nennt zwei Wiederholungsangaben (3.4: „im Sommerbetrieb mit geöffneten Toren“ und „nach drei Monaten“). In der Risikotabelle steht bei allen nur die erste (Haiku: keine von beiden). Alle drei hatten die 3 Monate aber in der Basis-Zusammenfassung genannt. Opus macht daraus sogar eine berechtigte Unklarheit (Punkt 3: fällt „Sommer“ mit „nach drei Monaten“ zusammen?).
8. **Keine Halluzinationen bei Beträgen, Terminen, Zitaten.** Kein Modell nennt einen Eurobetrag für Einbehalt oder Schlusszahlung, keinen Termin für Update 4.3. Alle drei Zitate sind per `python3` zeichengenau im Original enthalten (inkl. der Fettungen). Die wörtlich zitierten Kurzbelege bei Opus („ergänzungsbedürftig“, „mindestens zwei weitere geschulte Personen nötig“, „der Vollständigkeit halber“, „nur geringfügig“) stehen ebenfalls so im Bericht.

---

## Lehren für die Auswertung

- **Nachfragen schlagen Zusammenfassen.** Derselbe Chat, der in der Basis-Stufe „alle Maße in Toleranz“ übernimmt, findet auf „Gibt es Widersprüche?“ die Schlitzbreite. Lehre: Die KI glaubt beim Zusammenfassen dem Fazit des Dokuments. Erst eine gezielte Prüffrage bringt sie dazu, Tabelle und Text gegeneinander zu lesen. Gut zeigbar: Basis-Satz 1 neben Widerspruch Nr. 1 legen.
- **Die Lösungshinweise sind hier zu pessimistisch.** „Kaum ein KI-Assistent findet das von selbst; mit der Nachfrage ‚Gibt es Widersprüche?‘ manchmal.“ Im Test: 3 von 3. Das kann bei [KI-TOOL] anders sein, aber Trainer sollten nicht ankündigen, dass es „sicher nicht klappt“.
- **Auch die Prüf-Antwort braucht einen Prüfschritt.** Haiku behauptet, Abschnitt 7 nenne die Leistungsaufnahme nicht – Strg + F nach „Leistungsaufnahme“ findet sie in Abschnitt 7 zweimal. Perfekt für die Runde „Wo lag der KI-Assistent daneben?“: Auch eine Liste von „Widersprüchen“ kann erfundene Widersprüche enthalten.
- **Wörtlich zitieren klappt zuverlässig, wenn der Text im Chat ist.** Alle drei Zitate sind zeichengenau. Strg + F mit einem Satzteil (z. B. „Einbehalt von 5 %“) ist der schnellste Prüfschritt der ganzen Übung. Hinweis für Teilnehmende: Fettungen (`**`) im Zitat stammen aus dem Markdown des Originals, nicht von der KI.
- **„keine Angabe“ wirkt.** Die Anweisung verhindert erfundene Schweregrade bei allen Modellen. Sonnet füllt die Spalte trotzdem mit Fakten statt Bewertungen – Gesprächsanlass: „Was ist eine Einschätzung, was ist ein Messwert?“
- **Mehr Länge ist nicht mehr Fehler – aber mehr Prüfaufwand.** Opus liefert 13 Punkte, Sonnet 16, Haiku 7. Die langen Listen enthalten die wertvollsten Funde (Vorbehalt deckt nur 3 von 6 Punkten ab; kein Datum im Bericht), aber kein Teilnehmender prüft 16 Punkte in 27 Minuten. Tipp: „Nenne die drei wichtigsten Widersprüche, jeweils mit Abschnitt.“
- **Der stärkste inhaltliche Fund kommt nicht aus den Lösungshinweisen:** Opus' Punkt 2 (die Empfehlung sichert Taktzeit C, Staubmessung und Schulung nicht ab). Das ist eine echte Entscheidungsfrage für die GF und eignet sich als Abschluss der Auswertung.

---

## Gesprächsprotokolle

### Modell: Haiku

#### Nutzer 1

Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.

#### Assistent 1

Die Laserschneidanlage LS-3015 erfüllt laut Prüfbericht die wesentlichen Anforderungen aus Lastenheft und Kaufvertrag: Schnittqualität und Maßhaltigkeit liegen bei allen drei Prüfteilen innerhalb der Toleranz, und die technische Verfügbarkeit im Fünf-Tage-Dauerlauf liegt mit 96,2 % über der geforderten Mindestverfügbarkeit von 95 %. Die Taktzeiten der beiden wichtigsten Serienteile liegen deutlich unter den zugesicherten Werten, bei Prüfteil C (Montagewinkel) wird die Zusage mit 41 statt 40 Sekunden dagegen knapp verfehlt. Gegenüber der alten CO₂-Anlage erwartet die Fertigungstechnik eine jährliche Kostenersparnis von etwa 85.000 Euro, wobei Kosten für zusätzliche Schulungen, eine mögliche Verstärkung der Absaugung und einen höheren Verbrauch an Schutzgläsern nicht enthalten sind. Offen sind unter anderem das Software-Update auf Version 4.3 (ohne genannten Termin), die nicht getrennt gemessene Leistungsaufnahme (31 kW statt unter 30 kW) und eine Wiederholungsmessung der Staubkonzentration nach drei Monaten, die Schlusszahlung von 30 % des Kaufpreises wird mit der Abnahme fällig. Die Fertigungstechnik empfiehlt, die Anlage unter Vorbehalt abzunehmen und bis zur Erledigung der offenen Punkte 5 % des Kaufpreises von der Schlusszahlung einzubehalten, daher ist eine Entscheidung der Geschäftsführung nötig.

#### Nutzer 2

Welche Risiken oder offenen Punkte nennt der Bericht, die noch nicht gelöst sind?
Liste sie als Tabelle mit den Spalten: Risiko | Wie schlimm (laut Bericht) | Abschnitt im Bericht.
Wenn der Bericht zu einem Punkt keine Einschätzung enthält, schreib "keine Angabe".

#### Assistent 2

| Risiko | Wie schlimm (laut Bericht) | Abschnitt im Bericht |
|---|---|---|
| Taktzeit Prüfteil C: 41 s statt zugesicherter 40 s | knapp nicht erfüllt | 3.2, 4 |
| Leistungsaufnahme Schneidbetrieb: 31 kW statt unter 30 kW, nicht getrennt gemessen (inkl. Absaugung) | unklar | 3.5, 4 |
| Staubkonzentration beim Schneiden von verzinktem Blech: 92 % des Richtwerts, Wiederholungsmessung steht aus | erfüllt, knapp; Fachkraft für Arbeitssicherheit hat vorläufig freigegeben | 3.4, 4 |
| Schutzglas wird bei verzinktem Material häufiger gewechselt als im Wartungsplan vorgesehen; zwei Stück auf Lager, Lieferzeit "drei bis sechs Wochen" | keine Angabe | 3.3 |
| Wartungsplan enthält noch kein erhöhtes Wechselintervall für das Schutzglas | keine Angabe | 3.6 |
| Steuerungssoftware 4.2, Update auf 4.3 ausstehend, bis dahin manuelle Übertragung von Schneidprogrammen; kein Termin genannt | keine Angabe | 3.6 |
| Nur zwei geschulte Bediener, mindestens zwei weitere nötig; Schulung weiterer Mitarbeitender nicht im Kaufvertrag | keine Angabe | 3.6 |
| Kosten für Zusatzschulungen, Absaugungsverstärkung und Schutzgläser nicht in der Wirtschaftlichkeitsrechnung enthalten | keine Angabe | 5 |
| Zugangsdaten für die Fernwartung sollen nicht per E-Mail übermittelt werden | keine Angabe | 6 |
| Erstmusterprüfung nach jedem Parameterwechsel bei Prüfteil C (Anregung der Qualitätssicherung) | keine Angabe | 6 |
| Neuer Materialfluss in Halle 3 noch nicht im Hallenplan | keine Angabe | 6 |
| Ablagefläche für Restgitter fehlt (Wunsch der Bediener) | keine Angabe | 6 |
| Altanlage soll verkauft werden, bis dahin ohne Wartungsvertrag als Reserve | keine Angabe | 5 |

#### Nutzer 3

Was empfiehlt der Bericht als nächsten Schritt? Zitiere die entsprechende Stelle wörtlich.

#### Assistent 3

Der Bericht empfiehlt in Abschnitt 7 (Zusammenfassung und Empfehlung):

„**Empfehlung:** Die Fertigungstechnik empfiehlt der Geschäftsführung, die Anlage **unter Vorbehalt abzunehmen**. Der Vorbehalt soll schriftlich festhalten, dass der Hersteller (1) das Software-Update 4.3 bis zu einem verbindlichen Termin bereitstellt, (2) den Wartungsplan um das Wechselintervall des Schutzglases ergänzt und (3) eine getrennte Messung der Leistungsaufnahme ohne Absaugung durchführt. Es wird vorgeschlagen, bis zur Erledigung dieser Punkte einen Einbehalt von 5 % des Kaufpreises von der Schlusszahlung zu vereinbaren.“

#### Nutzer 4

Gibt es Widersprüche oder Stellen, die unklar formuliert sind?

#### Assistent 4

Ja, an folgenden Stellen:

1. **Widerspruch bei Prüfteil B (Schlitzbreite):** Laut Tabelle in Abschnitt 4 beträgt die Toleranz ±0,10 mm (Prüfteil B ist 3 mm stark, Abschnitt 3.1 nennt für Teile bis 3 mm ±0,10 mm). Die größte Abweichung liegt aber bei 0,13 mm, die Bewertung lautet trotzdem "i. O.". Das ist nach dem Bericht selbst nicht konsistent.
2. **Leistungsaufnahme:** Abschnitt 3.5 spricht von "knapp nicht erreicht", die Tabelle bewertet den Punkt als "unklar". Die Zusammenfassung in Abschnitt 7 nennt die Leistungsaufnahme nicht. Ob der Wert die Absaugung umfasst, ist nur über den Hinweis des Herstellers belegt, eine getrennte Messung fehlt.
3. **Staubmessung:** Der Text sagt, die Fachkraft für Arbeitssicherheit habe die Anlage "vorläufig" freigegeben, ohne zu erklären, was "vorläufig" bedeutet. Die Messung erfolgte außerdem bei geschlossener Hallentür, die Aussagekraft für den Sommerbetrieb ist daher offen.
4. **Einsparungen:** Die 85.000 Euro pro Jahr sind als "überschlägige Rechnung" bezeichnet, ohne dass Annahmen oder Rechenweg angegeben werden. Die 45 % Zeitersparnis und die rund 60 % geringere Energieaufnahme werden ebenfalls ohne Vergleichswerte der Altanlage genannt.
5. **Zusammenfassung vs. Detail:** Abschnitt 7 spricht von "erheblichen Einsparungen" und davon, dass die Maßhaltigkeit bei allen drei Prüfteilen innerhalb der Toleranz ist. Das deckt sich nicht vollständig mit der Schlitzbreite-Abweichung aus Punkt 1.
6. **Status des Dokuments:** Der Bericht trägt den Status "Entwurf zur Freigabe" (Version 1.0), ist aber als Grundlage für die formale Abnahme gedacht. Unklar bleibt, wer die Freigabe erteilt.
7. **Zuständigkeit für Zusatzschulungen:** Der Bericht sagt, zusätzliche Schulungen seien nicht im Kaufvertrag enthalten und müssten gesondert beauftragt werden. Wer die Kosten trägt, wird nicht geregelt.

---

### Modell: Sonnet

#### Nutzer 1

Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.

#### Assistent 1

Die Faserlaser-Schneidanlage LS-3015 erfüllt laut Abnahmeprüfung die wesentlichen Anforderungen: Schnittqualität und Maßhaltigkeit liegen bei allen drei Prüfteilen in der Toleranz, die Verfügbarkeit beträgt 96,2 % (gefordert: 95 %), und die Bearbeitungszeit sinkt gegenüber der Altanlage um rund 45 %. Knapp verfehlt wurden die Taktzeit bei Prüfteil C (41 statt 40 Sekunden) und, unklar wegen der mitgemessenen Absaugung, die Leistungsaufnahme (31 statt unter 30 kW). Die Fertigungstechnik beziffert die jährliche Ersparnis überschlägig auf etwa 85.000 Euro; nicht enthalten sind Kosten für zusätzliche Schulungen, eine mögliche Verstärkung der Absaugung und den höheren Schutzglas-Verbrauch (rund 60 Euro pro Stück). Offen sind außerdem die Wiederholungsmessung der Staubkonzentration beim Schneiden von verzinktem Blech (Messwert 92 % des Richtwerts, Wiederholung nach drei Monaten erbeten), das Software-Update 4.3 ohne konkreten Termin, ein noch zu ergänzender Wartungsplan und die Schulung von mindestens zwei weiteren Bedienern. Es ist eine Entscheidung nötig: Die Geschäftsführung soll über die formale Abnahme entscheiden (damit werden 30 % des Kaufpreises als Schlusszahlung fällig), und empfohlen wird eine Abnahme unter schriftlichem Vorbehalt mit einem Einbehalt von 5 % des Kaufpreises bis zur Erledigung der offenen Punkte.

#### Nutzer 2

Welche Risiken oder offenen Punkte nennt der Bericht, die noch nicht gelöst sind?
Liste sie als Tabelle mit den Spalten: Risiko | Wie schlimm (laut Bericht) | Abschnitt im Bericht.
Wenn der Bericht zu einem Punkt keine Einschätzung enthält, schreib "keine Angabe".

#### Assistent 2

| Risiko | Wie schlimm (laut Bericht) | Abschnitt im Bericht |
|---|---|---|
| Taktzeit Prüfteil C knapp verfehlt (41 s statt 40 s) | Abweichung von einer Sekunde; vom Hersteller mit dem kantenschonenden Parametersatz begründet; "knapp nicht erfüllt" | 3.2, 4, 7 |
| Leistungsaufnahme im Schneidbetrieb nicht getrennt gemessen (31 kW inkl. Absaugung statt unter 30 kW) | "knapp nicht erreicht", Bewertung "unklar" | 3.5, 4, 7 |
| Staubkonzentration bei verzinktem Blech, Wiederholungsmessung im Sommerbetrieb mit offenen Toren steht aus | 92 % des Richtwerts, "erfüllt, knapp"; vorläufige Freigabe durch die Fachkraft für Arbeitssicherheit | 3.4, 4, 7 |
| Mögliche Verstärkung der Absaugung nötig | keine Angabe zur Wahrscheinlichkeit; Kosten nicht enthalten | 5 |
| Schutzglas muss bei verzinktem Material häufiger gewechselt werden; Wartungsplan ohne entsprechendes Intervall | keine Angabe zur Häufigkeit; Kosten rund 60 Euro pro Stück, "höherer Verbrauch" nicht in der Ersparnis enthalten | 3.3, 3.6, 5, 7 |
| Ersatzteil-Lieferzeit 3 bis 6 Wochen bei nur 2 Schutzgläsern auf Lager | keine Angabe (keine Bewertung im Bericht) | 3.3 |
| Software-Update 4.3 ohne konkreten Termin, bis dahin teils manuelle Übertragung von Schneidprogrammen aus dem ERP | Fehler wird beim Update behoben; Termin "im Laufe des Quartals", kein konkretes Datum; sonst keine Bewertung | 3.6, 7 |
| Zu wenige geschulte Bediener (2 vorhanden, mindestens 2 weitere nötig; Schulung nicht im Kaufvertrag) | "nötig" für Vertretung und mögliche zweite Schicht; Kosten keine Angabe | 3.6, 5, 7 |
| Randwert Schnittqualität Prüfteil C: leichte Bartbildung an der Unterseite | "deutlich reduziert" durch optimierten Parametersatz; keine Angabe zur Restbartbildung | 3.1 |
| Altanlage nach Abnahme ohne Wartungsvertrag bis zum Verkauf | keine Angabe | 5 |
| Fernwartungs-Zugangsdaten sollen nicht per E-Mail übermittelt werden | keine Angabe | 6 |
| Erstmusterprüfung bei Prüfteil C nach Parameterwechsel (Anregung der QS) | keine Angabe | 6 |
| Materialfluss in Halle 3 nicht im Hallenplan eingezeichnet | keine Angabe | 6 |
| Zusätzliche Ablagefläche für Restgitter gewünscht | keine Angabe | 6 |

#### Nutzer 3

Was empfiehlt der Bericht als nächsten Schritt? Zitiere die entsprechende Stelle wörtlich.

#### Assistent 3

Der Bericht empfiehlt eine Abnahme unter Vorbehalt. Die Stelle im Abschnitt 7 lautet wörtlich:

> **Empfehlung:** Die Fertigungstechnik empfiehlt der Geschäftsführung, die Anlage **unter Vorbehalt abzunehmen**. Der Vorbehalt soll schriftlich festhalten, dass der Hersteller (1) das Software-Update 4.3 bis zu einem verbindlichen Termin bereitstellt, (2) den Wartungsplan um das Wechselintervall des Schutzglases ergänzt und (3) eine getrennte Messung der Leistungsaufnahme ohne Absaugung durchführt. Es wird vorgeschlagen, bis zur Erledigung dieser Punkte einen Einbehalt von 5 % des Kaufpreises von der Schlusszahlung zu vereinbaren.

#### Nutzer 4

Gibt es Widersprüche oder Stellen, die unklar formuliert sind?

#### Assistent 4

Ja, es gibt mehrere Stellen, die ich so im Bericht finde:

**Widersprüche bzw. Unstimmigkeiten**
1. **Taktzeiten:** Abschnitt 7 sagt, die Taktzeiten lägen "bei den beiden wichtigsten Serienteilen deutlich unter den zugesicherten Werten". Das stimmt für A (82 statt 95 s) und B (64 statt 70 s), aber der Bericht nennt nirgends, dass A und B die wichtigsten Serienteile sind. Außerdem ist B mit 6 s Abstand nur mäßig "deutlich" unter dem Wert.
2. **Maßhaltigkeit:** Abschnitt 7 sagt, alles sei "innerhalb der Toleranz". In der Tabelle liegt die größte Abweichung bei Schlitzbreite (Teil B) mit 0,13 mm über der Toleranz von ±0,10 mm, trotzdem steht "i. O.". Der Mittelwert (4,07 mm) liegt zwar innerhalb, die größte Abweichung aber außerhalb. Der Bericht erklärt nicht, ob nach Mittelwert oder Einzelwert bewertet wurde.
3. **Staubkonzentration:** In der Tabelle gilt sie als "erfüllt, knapp", in Abschnitt 3.4 steht jedoch, dass die Messung bei geschlossener Hallentür erfolgte und die Wiederholung unter anderen Bedingungen aussteht. Die Erfüllung ist also vorläufig, wird aber in der Zusammenfassung (Abschnitt 7) nur als "noch nicht vollständig geklärt" geführt.
4. **Gesamturteil vs. Einzelabweichungen:** Abschnitt 7 sagt, die Anlage "erfüllt die wesentlichen Anforderungen", nennt aber zugleich zwei nicht erfüllte bzw. ungeklärte Vertragswerte (Taktzeit C, Leistungsaufnahme). Was "wesentlich" bedeutet, definiert der Bericht nicht.
5. **Einschichtbetrieb:** Abschnitt 3.2 sagt, ein Einschichtbetrieb sei "voraussichtlich ausreichend", Abschnitt 3.6 verlangt aber Schulung für "eine mögliche spätere zweite Schicht". Das ist nicht zwingend widersprüchlich, wird aber nicht erläutert.
6. **Amortisation:** Abschnitt 5 sagt, die Amortisationszeit verlängere sich "nur geringfügig", nennt aber weder Kaufpreis noch Amortisationszeit noch die Höhe der nicht enthaltenen Kosten. Die Aussage ist nicht nachprüfbar.

**Unklar formulierte Stellen**
- **Bewertung "unklar"** bei der Leistungsaufnahme: Es ist offen, ob die Anforderung erfüllt ist, da die Absaugung nicht getrennt gemessen wurde.
- **"im Laufe des Quartals"** (Update 4.3): Welches Quartal gemeint ist, bleibt offen; die Empfehlung fordert zugleich einen "verbindlichen Termin".
- **"drei bis sechs Wochen"** Lieferzeit: Das ist eine Herstellerangabe in Anführungszeichen, ohne Verbindlichkeit.
- **"vorläufig freigegeben"** durch die Fachkraft für Arbeitssicherheit: Der Umfang und die Bedingungen der Vorläufigkeit sind nicht beschrieben.
- **Kaufpreis fehlt:** Die Schlusszahlung (30 %) und der Einbehalt (5 %) lassen sich in Euro nicht beziffern.
- **Einbehalt:** Unklar ist, ob die 5 % zusätzlich zur Schlusszahlung von 30 % oder als Teil davon gemeint sind. Der Text sagt "von der Schlusszahlung", also wohl als Teil.
- **"Abnahme unter Vorbehalt":** Der Bericht erwähnt nicht, ob dabei die Gefahr dennoch sofort übergeht (Abschnitt 1) und welche Folgen eine Nichterfüllung der drei Punkte hätte.
- **Prüfumfang:** "mindestens 50 Stück" geschnitten, aber Maßprüfung nur an 10 Teilen mit 4 Prüfmaßen, daher begrenzte Aussagekraft, ohne dass der Bericht das einordnet.
- **Dokumentstatus:** "Version 1.0 · Status: Entwurf zur Freigabe" bei gleichzeitigem Hinweis, dass das Dokument fiktiv ist.
- **Sachfehler im Bericht Abschnitt 3.3:** Gesamtstillstand 35 + 130 + 20 = 185 Minuten, also gut 3 Stunden, bei 80 Stunden Planzeit ergibt sich rund 96,2 % Verfügbarkeit, was rechnerisch stimmt (185/4800 = 3,85 %).

---

### Modell: Opus

#### Nutzer 1

Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.

#### Assistent 1

Die neue Faserlaser-Schneidanlage LS-3015 erfüllt laut Abnahmeprüfbericht (PB-2024-017, Status: Entwurf zur Freigabe) die wesentlichen Anforderungen aus Lastenheft und Kaufvertrag: Die Maßhaltigkeit liegt bei allen drei Prüfteilen in der Toleranz, die Taktzeiten der Frontblende SG-40 (82 s statt max. 95 s) und der Seitenwand SG-60 (64 s statt max. 70 s) liegen deutlich unter den Zusagen, und die technische Verfügbarkeit im Dauerlauf beträgt 96,2 % (gefordert: 95 %).

Offen oder knapp verfehlt sind die Taktzeit beim 8-mm-Montagewinkel (41 s statt 40 s), die Leistungsaufnahme (31 kW statt „unter 30 kW“, allerdings zusammen mit der Absaugung gemessen), die Staubkonzentration bei verzinktem Blech (92 % des internen Richtwerts, die Wiederholungsmessung steht noch aus), der Wartungsplan, in dem das häufigere Wechseln des Schutzglases fehlt, sowie die Schulung von mindestens zwei weiteren Bedienern, die nicht im Kaufvertrag enthalten ist.

Die Fertigungstechnik schätzt die jährliche Ersparnis gegenüber der Altanlage auf etwa 85.000 Euro, wobei die Kosten für zusätzliche Schulungen, eine eventuell nötige Verstärkung der Absaugung und den höheren Verbrauch an Schutzgläsern (je ca. 60 Euro) noch nicht eingerechnet sind.

Zu den Terminen: Die Fachkraft für Arbeitssicherheit bittet darum, die Staubmessung nach drei Monaten zu wiederholen, und das Software-Update 4.3, das einen Fehler bei der Übergabe von Auftragsdaten aus dem ERP-System behebt, ist nur „im Laufe des Quartals“ angekündigt, ohne konkreten Termin.

Die Geschäftsführung muss über die formale Abnahme entscheiden, mit der die Gefahr übergeht und die Schlusszahlung von 30 % fällig wird; empfohlen wird eine Abnahme unter Vorbehalt mit einem Einbehalt von 5 % des Kaufpreises, bis der Hersteller das Update bereitstellt, den Wartungsplan ergänzt und die Leistungsaufnahme getrennt misst.

#### Nutzer 2

Welche Risiken oder offenen Punkte nennt der Bericht, die noch nicht gelöst sind?
Liste sie als Tabelle mit den Spalten: Risiko | Wie schlimm (laut Bericht) | Abschnitt im Bericht.
Wenn der Bericht zu einem Punkt keine Einschätzung enthält, schreib "keine Angabe".

#### Assistent 2

| Risiko | Wie schlimm (laut Bericht) | Abschnitt im Bericht |
|---|---|---|
| Taktzeit Prüfteil C (8-mm-Winkel) mit 41 s über dem zugesicherten Wert von 40 s; der Hersteller begründet das mit dem langsameren Parametersatz für bessere Kantenqualität | „knapp nicht erfüllt“; Abweichung von einer Sekunde | 3.2, 4, 7 |
| Leistungsaufnahme im Schneidbetrieb 31 kW statt „unter 30 kW“; zusammen mit der Absaugung gemessen, keine getrennte Messung | „knapp nicht erreicht“ (3.5), Bewertung in der Tabelle: „unklar“ | 3.5, 4, 7 |
| Staubkonzentration bei verzinktem Blech bei 92 % des internen Richtwerts; nur bei geschlossener Hallentür gemessen, Wiederholungsmessung im Sommerbetrieb steht aus | „erfüllt, knapp“; von der Fachkraft für Arbeitssicherheit nur vorläufig freigegeben | 3.4, 4, 7 |
| Eventuell nötige Verstärkung der Absaugung, Kosten nicht beziffert | keine Angabe | 5 |
| Schutzglas muss bei viel verzinktem Material häufiger gewechselt werden als im Wartungsplan vorgesehen | keine Angabe (Mehrkosten nicht beziffert; laut Abschnitt 5 verlängert sich die Amortisation insgesamt „voraussichtlich nur geringfügig“) | 3.3, 5 |
| Wartungsplan enthält das erhöhte Wechselintervall des Schutzglases noch nicht | „ergänzungsbedürftig“; Teil des empfohlenen Vorbehalts | 3.6, 7 |
| Ersatzteilversorgung: nur zwei Schutzgläser auf Lager, Lieferzeit „drei bis sechs Wochen“ | keine Angabe | 3.3 |
| Steuerungssoftware 4.2 mit Fehler bei der ERP-Datenübergabe; Schneidprogramme müssen teilweise von Hand übertragen werden; kein Termin für Update 4.3 | keine Angabe (Teil des empfohlenen Vorbehalts) | 3.6, 7 |
| Nur zwei geschulte Bediener; für die Vertretung und eine mögliche zweite Schicht sind mindestens zwei weitere nötig; die Schulung ist nicht im Kaufvertrag und müsste gesondert beauftragt werden | keine Angabe („mindestens zwei weitere geschulte Personen nötig“) | 3.6, 5, 7 |
| Altanlage steht bis zum Verkauf als Reserve bereit, aber ohne Wartungsvertrag | keine Angabe | 5 |
| Zugangsdaten für die Fernwartung sollen nicht per E-Mail, sondern auf sicherem Weg übermittelt werden | keine Angabe („der Vollständigkeit halber“ aufgeführt) | 6 |
| Erstmusterprüfung für Prüfteil C nach jedem Parameterwechsel angeregt (Hintergrund: Bartbildung, inzwischen deutlich reduziert) | keine Angabe | 3.1, 6 |
| Neuer Materialfluss ist noch nicht im Hallenplan eingezeichnet | keine Angabe | 6 |
| Zusätzliche Ablagefläche für Restgitter gewünscht | keine Angabe | 6 |

Hinweis: Der Bericht selbst nennt in Abschnitt 7 als „noch nicht vollständig geklärt“ nur sechs Punkte: Taktzeit C, Leistungsaufnahme, Staubmessung, Wartungsanleitung, Software-Update und Schulung. Die übrigen Zeilen stammen aus den Einzelabschnitten.

#### Nutzer 3

Was empfiehlt der Bericht als nächsten Schritt? Zitiere die entsprechende Stelle wörtlich.

#### Assistent 3

Der Bericht empfiehlt, die Anlage unter Vorbehalt abzunehmen und bis zur Erledigung von drei Punkten einen Teil der Schlusszahlung einzubehalten. Die Stelle in Abschnitt 7 lautet wörtlich:

> „**Empfehlung:** Die Fertigungstechnik empfiehlt der Geschäftsführung, die Anlage **unter Vorbehalt abzunehmen**. Der Vorbehalt soll schriftlich festhalten, dass der Hersteller (1) das Software-Update 4.3 bis zu einem verbindlichen Termin bereitstellt, (2) den Wartungsplan um das Wechselintervall des Schutzglases ergänzt und (3) eine getrennte Messung der Leistungsaufnahme ohne Absaugung durchführt. Es wird vorgeschlagen, bis zur Erledigung dieser Punkte einen Einbehalt von 5 % des Kaufpreises von der Schlusszahlung zu vereinbaren.“

Der nächste Schritt liegt also bei der Geschäftsführung: Sie entscheidet über die Abnahme unter Vorbehalt und vereinbart den Vorbehalt und den Einbehalt schriftlich mit dem Hersteller.

#### Nutzer 4

Gibt es Widersprüche oder Stellen, die unklar formuliert sind?

#### Assistent 4

Ja, mir sind folgende Stellen aufgefallen:

**Widersprüche**

1. **Schlitzbreite bei Prüfteil B (Abschnitt 4):** Die größte Abweichung ist mit 0,13 mm angegeben, die Toleranz beträgt aber ±0,10 mm. Trotzdem steht dort „i. O.“. Abschnitt 7 sagt außerdem, die Maßhaltigkeit liege „bei allen drei Prüfteilen innerhalb der Toleranz“. Der Mittelwert (4,07 mm) liegt zwar innerhalb, mindestens ein gemessenes Teil aber nicht. Entweder ist der Wert falsch eingetragen oder die Bewertung stimmt nicht. Das sollte vor der Abnahme geklärt werden.
2. **Offene Punkte und Vorbehalt passen nicht zusammen:** Abschnitt 7 nennt sechs ungeklärte Punkte. Der empfohlene Vorbehalt deckt aber nur drei davon ab (Update, Wartungsplan, Leistungsmessung). Zur verfehlten Taktzeit C, zur ausstehenden Staubmessung und zur Schulung weiterer Bediener sagt die Empfehlung nichts. Unklar bleibt, ob man die Taktzeit C stillschweigend akzeptiert.
3. **Wann wird die Staubmessung wiederholt?** In Abschnitt 3.4 heißt es „im Sommerbetrieb mit geöffneten Toren“, die Fachkraft für Arbeitssicherheit bittet dagegen um eine Wiederholung „nach drei Monaten“. Ob beides zusammenfällt, hängt vom Prüfdatum ab, und das nennt der Bericht nicht.
4. **Leistungsaufnahme:** Im Text steht „knapp nicht erreicht“, in der Tabelle „unklar“. Offen bleibt auch, ob die Angebotsangabe „unter 30 kW“ mit oder ohne Absaugung gemeint war. Davon hängt ab, ob überhaupt eine Abweichung vorliegt.

**Unklare oder unvollständige Formulierungen**

5. **Schutzglas und Ersatzteile:** Im fünftägigen Dauerlauf wurde das Schutzglas zweimal getauscht (Tag 2 und Tag 4). Es sind nur noch zwei auf Lager, die Lieferzeit beträgt drei bis sechs Wochen. Wie viel „häufiger“ gewechselt werden muss, beziffert der Bericht nicht. Er bewertet auch nicht, ob dadurch ein Stillstand droht.
6. **Kosten und Amortisation:** Die Ersparnis von 85.000 Euro pro Jahr beruht nur auf einer „überschlägigen Rechnung“. Die Kosten für Schulungen, Absaugung und Schutzgläser sind nicht beziffert, trotzdem heißt es, die Amortisation verlängere sich „nur geringfügig“. Weder die Amortisationszeit noch der Kaufpreis werden genannt. Deshalb ist auch nicht erkennbar, welchem Betrag der Einbehalt von 5 % (bzw. die Schlusszahlung von 30 %) entspricht.
7. **„Im Laufe des Quartals“:** Welches Quartal gemeint ist, bleibt offen, weil der Bericht weder Prüf- noch Erstellungsdatum hat (nur die Dokumentnummer PB-2024-017).
8. **„Verbindlicher Termin“** für das Software-Update: Die Empfehlung nennt keinen Vorschlag für diesen Termin.
9. **Interner Richtwert für Staub:** Wie hoch der Richtwert ist und ob er einem gesetzlichen Grenzwert entspricht, steht nicht im Bericht.
10. **„Die beiden wichtigsten Serienteile“** (Abschnitt 7): Dass A und B die wichtigsten Teile sind, wird vorher nirgends gesagt.
11. **Schichtbetrieb:** Laut Abschnitt 3.2 reicht „voraussichtlich ein Einschichtbetrieb“, Abschnitt 3.6 spricht von einer „möglichen späteren zweiten Schicht“. Das ist kein echter Widerspruch, es ist aber unklar, womit geplant wird. Davon hängt ab, wie dringend die zusätzliche Schulung ist.
12. **Bartbildung bei Prüfteil C:** Sie wurde „deutlich reduziert“, aber nicht beseitigt. Ob das verbleibende Ergebnis akzeptabel ist, wird nicht ausdrücklich bewertet.
13. **Dokumentstatus:** Der Bericht ist als „Entwurf zur Freigabe“ gekennzeichnet. Wer ihn freigibt und ob QS und Instandhaltung ihm zugestimmt haben, steht nicht darin. Unterschrieben hat nur die Fertigungstechnik.

Nachgerechnet habe ich die Verfügbarkeit: 185 Minuten Stillstand bei 80 Stunden Planzeit ergeben rund 96,2 %. Dieser Wert ist also schlüssig.

---

Zurück zum [Übungsblatt Übung 3](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md) · Material: [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md)
