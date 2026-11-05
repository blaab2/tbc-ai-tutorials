# Testlauf: Übung 3 / Station B Für Schnelle – FAQ zur neuen Fassung

**Herkunft:** Station B, Abschnitt „Für Schnelle“, erster Punkt in [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#für-schnelle-1): „Lass dir eine **FAQ** mit den fünf Fragen erstellen, die Mitarbeitende zur neuen Fassung wahrscheinlich stellen – mit Antworten, die sich nur auf v2 stützen.“ Material: [richtlinie_reisekosten_v1.md](../07_Beispielmaterial/richtlinie_reisekosten_v1.md) und [richtlinie_reisekosten_v2.md](../07_Beispielmaterial/richtlinie_reisekosten_v2.md). Zum Abgleich: [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md), Station B (enthält zur FAQ selbst **keine** Hinweise, nur die Liste der 7 Änderungen und den Rechenfall).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf:** Im selben Gespräch kam zuerst der Basis-Prompt von Station B (Vergleichstabelle), danach der FAQ-Prompt, wörtlich aus dem Übungsblatt abgeleitet:

```text
Erstelle eine FAQ mit den fünf Fragen, die Mitarbeitende zur neuen Fassung wahrscheinlich stellen – mit Antworten, die sich nur auf v2 stützen.
```

**Was herauskommen soll (Prüfmaßstab):** Genau 5 realistische Fragen. Jede Aussage ist in v2 belegbar. Zahlen laut v2: 0,25 €/km (4.3), 130 €/Nacht ohne Frühstück (5), 1. Klasse bei einfacher Fahrtdauer > 3 h (4.1), Inlandsflug nur bei Bahnfahrt > 5 h (4.2), Abrechnung innerhalb von 6 Wochen (8), Freigabe durch die Geschäftsführung bei > 2.000 € (3). Trinkgeld wird in v2 nicht mehr erwähnt (7), v2 „ersetzt alle bisherigen Regelungen“ (9). Für Verpflegung nennt v2 **keine Beträge**, nur „die jeweils aktuellen steuerlichen Pauschalen“ (6).

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Genau 5 Fragen | ja | ja | formal ja, aber Frage 4 bündelt zwei Themen (Bahn + Hotel), dazu ein Zusatzhinweis zu Trinkgeld |
| Fragen realistisch / auf die Änderungen bezogen | ja (GF-Freigabe, Flug, Km, Hotel, Frist) | ja (Frist, Km, Bahn + Flug, Hotel, Genehmigung) | ja (Frist, Km, Flug, Bahn + Hotel, Genehmigung) |
| Alle Zahlen korrekt nach v2 | ja | ja | ja |
| Nichts erfunden / nichts aus v1 | ja | ja | ja (Deutung „Inland = vermutlich Deutschland“ als Vermutung gekennzeichnet) |
| 1. Klasse > 3 h erwähnt | **nein** (fehlt ganz) | ja | ja |
| Trinkgeld-Frage behandelt | nein | nein | ja (als Zusatzhinweis, Verweis auf Personalabteilung lt. Abschnitt 9) |
| Keine Verpflegungsbeträge | ja (Verpflegung nicht erwähnt) | ja (nicht erwähnt) | ja (nicht erwähnt) |
| Fundstellen angegeben | nein | nein | ja (Abschnitt je Antwort) |
| Vergleichstabelle (Turn 1): 7/7 Änderungen | ja | ja | ja |
| Ergebnis | **bestanden** (eine Kernänderung fehlt) | **bestanden** | **bestanden** (am besten prüfbar, Format leicht überzogen) |

Nachgerechnet mit `python3`: 200 km × 0,05 € = 10,00 € (Sonnet, Turn 1, stimmt). 300 km × 0,30 € = 90,00 €, 300 km × 0,25 € = 75,00 € (Opus, Turn 1, stimmt). 130 − 110 = 20 € (alle, stimmt). Drei Monate ≈ 13,0 Wochen, sechs Wochen sind also ≈ 46 % davon (Opus: „nur noch halb so lang“, ungefähr richtig).

## Gefundene Fehler mit Beleg

**In den FAQs: keine sachlichen Fehler, keine Halluzinationen.** Jeder Satz aller drei FAQs lässt sich fast wörtlich in v2 wiederfinden. Die Antworten sind im Kern Umformulierungen der Abschnitte 3, 4.1, 4.2, 4.3, 5 und 8. Kein Modell nennt Verpflegungsbeträge, kein Modell übernimmt eine v1-Zahl.

**Lücken und Ungenauigkeiten:**

- **Haiku lässt die 1. Klasse weg.** Die Änderung „1. Klasse ab > 3 h“ (v2, 4.1) ist eine der beiden Verbesserungen für Mitarbeitende und fehlt in der FAQ ganz. Haiku hat sie in Turn 1 selbst als Änderung Nr. 2 aufgeführt.
- **Haiku und Sonnet übergehen Trinkgeld.** Gerade die Frage „Bekomme ich Trinkgeld noch erstattet?“ ist nach einer gestrichenen Regel sehr wahrscheinlich. Beide wählen nur Fragen, die sich mit einem v2-Satz beantworten lassen. Wer nur die FAQ liest, erfährt nichts vom Wegfall (v1, 7: „Trinkgelder können bis zur Höhe von 10 % des Rechnungsbetrags erstattet werden …“, in v2 gestrichen).
- **Opus dehnt die Vorgabe „fünf Fragen“.** Frage 4 lautet „Wann darf ich 1. Klasse Bahn fahren, und wie teuer darf mein Hotel sein?“, also zwei Fragen in einer, plus ein sechster Block zu Trinkgeld. Inhaltlich sinnvoll, formal nicht ganz auftragsgemäß. Sonnet bündelt ebenfalls (Frage 3: Bahn 1. Klasse + Inlandsflug), aber thematisch passend (Verkehrsmittel).
- **Opus, Turn 1:** „Formulierungs- oder Formatierungsänderungen gibt es darüber hinaus keine.“ Stimmt nicht ganz: Die Versionsnummer im Kopf ändert sich („Version 1“ → „Version 2“). Das ist laut Lösungshinweisen die einzige redaktionelle Änderung. Kleinigkeit, aber eine überzeugt klingende Gesamtaussage, die nicht stimmt.
- **Sonnet, Turn 1, Trinkgeld:** „im Zweifel vorher die Führungskraft fragen“. v2, Abschnitt 9 nennt als Ansprechstelle die **Personalabteilung**. Kein Fehler, aber nicht aus v2 belegt.
- **Haiku, Turn 1:** „Die 1. Klasse ist bei kürzeren Strecken erlaubt“ – v2 spricht von **Fahrtdauer**, nicht Strecke. Unscharf, nicht falsch im Ergebnis.

## Lehren für die Auswertung

1. **„Nur auf v2 stützen“ funktioniert gut.** Alle drei Modelle halten sich an die Quelle, keine einzige Zahl ist falsch. Das ist eine gute Botschaft: Mit einem vorliegenden Dokument und einer klaren Einschränkung liefern die Assistenten verlässliche Texte. Die Prüfung geht schnell: jede Zahl in v2 suchen und abhaken.
2. **Die eigentliche Lehre ist die Auswahl, nicht die Richtigkeit.** Haiku und Sonnet lassen die heikelste Frage (Trinkgeld) weg, weil v2 dazu nichts sagt. Haiku vergisst außerdem die 1. Klasse. Frage an die Runde: „Welche Frage würden eure Kolleginnen und Kollegen als Erstes stellen und steht sie in der FAQ?“ Richtig, aber unvollständig ist bei einer FAQ auch ein Problem.
3. **Gestrichene Regeln brauchen einen Hinweis.** Eine FAQ „nur aus v2“ kann Wegfälle grundsätzlich nicht zeigen, weil sie nur das Neue kennt. Opus löst das gut: v2 erwähnt Trinkgeld nicht, eine verbindliche Antwort gibt es nicht, also bei der Personalabteilung nachfragen (Abschnitt 9). Gutes Beispiel für eine ehrliche „Steht nicht drin“-Antwort.
4. **Fundstellen machen Prüfen leicht.** Nur Opus gibt bei jeder Antwort den Abschnitt an. Tipp für die Runde: „Gib zu jeder Antwort den Abschnitt aus v2 an“ in den Prompt schreiben. Dann dauert das Nachprüfen eine Minute.
5. **Verpflegung als Kontrollpunkt:** Kein Modell nennt Beträge, weil keins nach Verpflegung fragt. Wer eine FAQ mit Verpflegungsfrage bekommt, sollte prüfen, ob dort Euro-Beträge stehen. Die stammen dann nicht aus v2 (siehe Rechenfall in den Lösungshinweisen).
6. **Zeit:** Die FAQ entsteht in Sekunden, das Prüfen (5 Antworten gegen v2) braucht 3–5 Minuten. Passt als Zusatzaufgabe.

---

## Gesprächsprotokoll: Haiku

### Nutzer 1

Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?

### Assistent 1

Ich habe beide Fassungen verglichen. Inhaltlich unverändert sind die Abschnitte 1 (Geltungsbereich), 2 (Grundsätze), 4.4 (Mietwagen und Taxi), 6 (Verpflegung) und 9 (Inkrafttreten). Die folgenden sieben inhaltlichen Änderungen gibt es:

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung ab 2.000 Euro (Abschnitt 3) | Bei voraussichtlichen Reisekosten über 2.000 Euro ist die Freigabe durch die Abteilungsleitung nötig. | Die zusätzliche Freigabe erfolgt durch die Geschäftsführung. | Teure Reisen brauchen eine höhere Freigabeebene. Anträge können dadurch länger dauern. |
| 2 | 1. Klasse bei der Bahn (Abschnitt 4.1) | Die 1. Klasse darf ab einer einfachen Fahrtdauer von mehr als vier Stunden gebucht werden. | Die 1. Klasse darf schon ab mehr als drei Stunden einfacher Fahrtdauer gebucht werden. | Die 1. Klasse ist bei kürzeren Strecken erlaubt, was zu höheren Reisekosten führen kann. |
| 3 | Inlandsflüge (Abschnitt 4.2) | Keine Einschränkung nach Strecke. Flüge sind in der Economy Class zu buchen und über die Reisestelle zu buchen. | Inlandsflüge sind nur zulässig, wenn die einfache Bahnfahrt mehr als fünf Stunden dauern würde. | Für kurze und mittlere Strecken ist ein Inlandsflug nicht mehr erlaubt. Die Reise sollte per Bahn erfolgen. |
| 4 | Kilometerpauschale privater Pkw (Abschnitt 4.3) | 0,30 Euro je gefahrenem Kilometer. | 0,25 Euro je gefahrenem Kilometer. | Wer das eigene Auto nutzt, erhält pro Kilometer weniger Erstattung. |
| 5 | Hotelobergrenze (Abschnitt 5) | Übernachtung bis 110 Euro pro Nacht (ohne Frühstück) gegen Hotelrechnung. | Übernachtung bis 130 Euro pro Nacht (ohne Frühstück) gegen Hotelrechnung. | Die erstattungsfähige Hotelobergrenze steigt um 20 Euro pro Nacht. |
| 6 | Trinkgelder (Abschnitt 7) | Trinkgelder können bis 10 % des Rechnungsbetrags erstattet werden, wenn sie auf dem Beleg vermerkt sind. | Diese Regel entfällt ersatzlos. In v2 steht nichts mehr zu Trinkgeldern. | Trinkgelder sind nach v2 nicht mehr ausdrücklich erstattungsfähig. Im Zweifel bei der Buchhaltung oder Personalabteilung nachfragen. |
| 7 | Abrechnungsfrist (Abschnitt 8) | Die Abrechnung muss innerhalb von drei Monaten nach Reiseende mit Originalbelegen eingereicht werden. | Die Abrechnung muss innerhalb von sechs Wochen nach Reiseende mit Originalbelegen eingereicht werden. | Die Abrechnung muss deutlich schneller erfolgen. Die Frist ist deutlich kürzer. |

### Nutzer 2

Erstelle eine FAQ mit den fünf Fragen, die Mitarbeitende zur neuen Fassung wahrscheinlich stellen – mit Antworten, die sich nur auf v2 stützen.

### Assistent 2

**FAQ zur Reisekostenrichtlinie (Version 2)**

**1. Ich soll eine Dienstreise mit voraussichtlich mehr als 2.000 Euro Kosten machen. Wer muss zustimmen?**
Zusätzlich zur direkten Führungskraft ist die Freigabe durch die Geschäftsführung erforderlich. Ohne vorherige Genehmigung besteht kein Anspruch auf Erstattung. Der Antrag muss vor Reiseantritt gestellt werden, schriftlich oder über das Reiseantragsformular im Intranet.

**2. Darf ich für eine Dienstreise fliegen?**
Flüge sind in der Economy Class zu buchen, und die Buchung erfolgt ausschließlich über die Reisestelle. Inlandsflüge sind nur zulässig, wenn die einfache Bahnfahrt länger als fünf Stunden dauern würde. Bei kürzeren Strecken bitte die Bahn nutzen. Zusatzleistungen wie Sitzplatzwahl oder zusätzliches Gepäck werden nur erstattet, wenn sie dienstlich notwendig sind.

**3. Wie viel bekomme ich, wenn ich mein privates Auto nutze?**
Mit vorheriger Genehmigung erstattet das Unternehmen eine Kilometerpauschale von 0,25 Euro je gefahrenem Kilometer. Parkgebühren werden gegen Beleg erstattet. Für Schäden am privaten Fahrzeug haftet das Unternehmen nicht, sofern keine gesonderte Vereinbarung besteht.

**4. Wie hoch ist die Erstattung für eine Hotelübernachtung?**
Die Übernachtung wird gegen Hotelrechnung bis zu 130 Euro pro Nacht erstattet, ohne Frühstück. In Städten mit erfahrungsgemäß hohen Hotelpreisen sowie während großer Messen kann die Führungskraft im Einzelfall eine höhere Obergrenze genehmigen. Die Buchung sollte möglichst frühzeitig erfolgen.

**5. Bis wann muss ich meine Reisekostenabrechnung einreichen?**
Die Abrechnung muss innerhalb von sechs Wochen nach Ende der Dienstreise mit allen Originalbelegen bei der Buchhaltung eingereicht werden. Digitale Belege sind zulässig, wenn sie gut lesbar sind. Verspätet eingereichte Abrechnungen können abgelehnt werden. Vorschüsse sind spätestens mit der Abrechnung zu verrechnen.

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1

Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?

### Assistent 1

Ich habe beide Fassungen verglichen. Es gibt sieben inhaltliche Änderungen. Die übrigen Abschnitte sind unverändert: Geltungsbereich, Grundsätze, Mietwagen und Taxi, Verpflegung, Inkrafttreten. Bei Abschnitt 3 ist die Änderung klein, aber relevant, weil sich die Instanz der Freigabe ändert.

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Zusätzliche Freigabe bei teuren Reisen (§ 3) | Bei voraussichtlichen Kosten über 2.000 Euro muss zusätzlich die Abteilungsleitung freigeben. | Bei voraussichtlichen Kosten über 2.000 Euro muss zusätzlich die Geschäftsführung freigeben. Die Schwelle bleibt gleich. | Teure Reisen müssen jetzt der Geschäftsführung zur Freigabe vorgelegt werden, nicht mehr der Abteilungsleitung. Das kann den Genehmigungsweg verlängern, also früher beantragen. |
| 2 | Bahn: 1. Klasse (§ 4.1) | 1. Klasse ab einer einfachen Fahrtdauer von mehr als 4 Stunden. | 1. Klasse ab einer einfachen Fahrtdauer von mehr als 3 Stunden. | Die 1. Klasse darf früher gebucht werden. Eine Fahrt von 3,5 Stunden berechtigt jetzt dazu. |
| 3 | Inlandsflüge (§ 4.2) | Keine Einschränkung für Inlandsflüge. Flüge sind in Economy über die Reisestelle zu buchen. | Inlandsflüge sind nur zulässig, wenn die einfache Bahnfahrt länger als 5 Stunden dauern würde. Economy und Buchung über die Reisestelle bleiben bestehen. | Für Strecken im Inland mit höchstens 5 Stunden Bahnfahrt ist ein Flug nicht mehr erlaubt. Dann muss die Bahn genommen werden. |
| 4 | Kilometerpauschale (§ 4.3) | 0,30 Euro je gefahrenem Kilometer. | 0,25 Euro je gefahrenem Kilometer. | Wer mit dem privaten Auto fährt, bekommt pro Kilometer 5 Cent weniger. Bei 200 km sind das 10 Euro weniger. |
| 5 | Hotelobergrenze (§ 5) | Bis 110 Euro pro Nacht (ohne Frühstück). | Bis 130 Euro pro Nacht (ohne Frühstück). Die Ausnahme für teure Städte und Messen bleibt. | Es gibt 20 Euro mehr Spielraum pro Nacht. Bei hohen Preisen gilt weiterhin die Einzelfallgenehmigung durch die Führungskraft. |
| 6 | Trinkgelder (§ 7) | Trinkgelder können bis 10 % des Rechnungsbetrags erstattet werden, wenn sie auf dem Beleg vermerkt sind. | Die Regelung zu Trinkgeldern ist in v2 gestrichen. Visa, dienstliche Telefonate und Gepäckaufbewahrung gegen Beleg sowie der Ausschluss privater Kosten bleiben. | Trinkgelder sind in der Richtlinie nicht mehr als erstattungsfähig genannt. Man sollte nicht mehr mit einer Erstattung rechnen und im Zweifel vorher die Führungskraft fragen. |
| 7 | Abrechnungsfrist (§ 8) | Einreichung innerhalb von drei Monaten nach Ende der Dienstreise. | Einreichung innerhalb von sechs Wochen nach Ende der Dienstreise. | Die Frist wird deutlich kürzer. Abrechnungen sollten zeitnah erstellt werden, sonst können sie abgelehnt werden. |

### Nutzer 2

Erstelle eine FAQ mit den fünf Fragen, die Mitarbeitende zur neuen Fassung wahrscheinlich stellen – mit Antworten, die sich nur auf v2 stützen.

### Assistent 2

**FAQ zur Reisekostenrichtlinie, Version 2**

**1. Wie lange habe ich Zeit, meine Reisekosten abzurechnen?**
Die Abrechnung muss innerhalb von sechs Wochen nach Ende der Dienstreise mit allen Originalbelegen bei der Buchhaltung eingereicht werden. Digitale Belege sind zulässig, wenn sie gut lesbar sind. Verspätet eingereichte Abrechnungen können abgelehnt werden. Vorschüsse werden spätestens mit der Abrechnung verrechnet.

**2. Wie viel erstattet das Unternehmen, wenn ich mit meinem privaten Auto fahre?**
Mit Genehmigung erstattet das Unternehmen 0,25 Euro je gefahrenem Kilometer. Parkgebühren werden gegen Beleg erstattet. Für Schäden am privaten Fahrzeug haftet das Unternehmen nicht, sofern keine gesonderte Vereinbarung besteht.

**3. Wann darf ich Bahn 1. Klasse fahren, und wann ist ein Inlandsflug erlaubt?**
Die Bahn fährt man grundsätzlich in der 2. Klasse. Die 1. Klasse darf gebucht werden, wenn die einfache Fahrt länger als drei Stunden dauert. Ein Inlandsflug ist nur zulässig, wenn die einfache Bahnfahrt länger als fünf Stunden dauern würde. Flüge werden in Economy ausschließlich über die Reisestelle gebucht. Sitzplatzwahl oder zusätzliches Gepäck werden nur erstattet, wenn sie dienstlich notwendig sind.

**4. Wie viel darf das Hotel kosten?**
Erstattet werden bis zu 130 Euro pro Nacht (ohne Frühstück) gegen Vorlage der Hotelrechnung. In Städten mit erfahrungsgemäß hohen Hotelpreisen und bei großen Messen kann die Führungskraft im Einzelfall eine höhere Obergrenze genehmigen. Die Buchung soll möglichst frühzeitig erfolgen.

**5. Wer muss meine Dienstreise genehmigen?**
Jede Dienstreise muss vor Reiseantritt schriftlich oder über das Reiseantragsformular im Intranet beantragt werden. Die direkte Führungskraft genehmigt. Bei voraussichtlichen Kosten über 2.000 Euro ist zusätzlich die Freigabe durch die Geschäftsführung erforderlich. Ohne vorherige Genehmigung besteht kein Anspruch auf Erstattung der Reisekosten.

---

## Gesprächsprotokoll: Opus

### Nutzer 1

Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?

### Assistent 1

Ich habe beide Fassungen Abschnitt für Abschnitt verglichen. Es gibt **sieben inhaltliche Änderungen**. Die übrigen Abschnitte sind wortgleich geblieben: 1 Geltungsbereich, 2 Grundsätze, 4.4 Mietwagen/Taxi, 6 Verpflegung und 9 Inkrafttreten. Formulierungs- oder Formatierungsänderungen gibt es darüber hinaus keine.

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung teurer Reisen (Abschn. 3) | Bei voraussichtlichen Kosten über 2.000 Euro muss zusätzlich die **Abteilungsleitung** freigeben. | Bei voraussichtlichen Kosten über 2.000 Euro muss zusätzlich die **Geschäftsführung** freigeben. | Für teure Reisen gibt es eine höhere Freigabestufe. Das kann länger dauern, also früher beantragen. Die Grenze von 2.000 Euro bleibt gleich. |
| 2 | Bahn, 1. Klasse (Abschn. 4.1) | Die 1. Klasse ist erlaubt, wenn die einfache Fahrt **mehr als vier Stunden** dauert. | Die 1. Klasse ist erlaubt, wenn die einfache Fahrt **mehr als drei Stunden** dauert. | Vorteil: Die 1. Klasse ist jetzt schon bei kürzeren Fahrten erlaubt, nämlich ab mehr als 3 Stunden. |
| 3 | Inlandsflüge (Abschn. 4.2) | Keine besondere Einschränkung, es gilt nur: Economy Class und Buchung über die Reisestelle. | **Neu:** Inlandsflüge sind nur zulässig, wenn die einfache Bahnfahrt **länger als fünf Stunden** dauern würde. | Bei Inlandsreisen ist meist die Bahn Pflicht. Ein Flug ist nur noch erlaubt, wenn die Bahnfahrt länger als 5 Stunden dauern würde. |
| 4 | Kilometerpauschale Privat-Pkw (Abschn. 4.3) | **0,30 Euro** je gefahrenem Kilometer | **0,25 Euro** je gefahrenem Kilometer | Nachteil: Fahrten mit dem eigenen Auto werden geringer erstattet. Beispiel für 300 km: früher 90 Euro, jetzt 75 Euro. |
| 5 | Übernachtung (Abschn. 5) | Erstattet werden bis **110 Euro** pro Nacht (ohne Frühstück). | Erstattet werden bis **130 Euro** pro Nacht (ohne Frühstück). | Vorteil: Es dürfen teurere Hotels gebucht werden. Die Ausnahme für teure Städte und Messen gilt weiterhin, mit Genehmigung der Führungskraft. |
| 6 | Trinkgelder (Abschn. 7) | Trinkgelder werden bis 10 % des Rechnungsbetrags erstattet, wenn sie auf dem Beleg vermerkt sind. | **Die Regelung ist gestrichen.** Trinkgelder werden nicht mehr erwähnt. | Laut v2 gibt es keine Grundlage mehr für die Erstattung von Trinkgeldern. Mitarbeitende sollten davon ausgehen, dass Trinkgelder nicht mehr erstattet werden. Im Zweifel bei der Personalabteilung nachfragen. |
| 7 | Frist für die Abrechnung (Abschn. 8) | Einreichen innerhalb von **drei Monaten** nach Ende der Reise | Einreichen innerhalb von **sechs Wochen** nach Ende der Reise | Die Frist ist nur noch halb so lang. Wer zu spät abrechnet, riskiert die Ablehnung. Belege also sofort sammeln und zügig einreichen. |

**Kurz zusammengefasst:**
- **Günstiger für Mitarbeitende:** Nr. 2 (1. Klasse ab 3 Stunden) und Nr. 5 (Hotel bis 130 Euro)
- **Ungünstiger oder strenger:** Nr. 1 (Freigabe durch die Geschäftsführung), Nr. 3 (Einschränkung bei Inlandsflügen), Nr. 4 (weniger Geld pro Kilometer), Nr. 6 (keine Trinkgelder mehr) und Nr. 7 (kürzere Frist)

### Nutzer 2

Erstelle eine FAQ mit den fünf Fragen, die Mitarbeitende zur neuen Fassung wahrscheinlich stellen – mit Antworten, die sich nur auf v2 stützen.

### Assistent 2

**FAQ zur Reisekostenrichtlinie (Version 2)**

**1. Wie lange habe ich Zeit, meine Reisekostenabrechnung einzureichen?**
Sie haben **sechs Wochen nach Ende der Dienstreise** Zeit. Reichen Sie die Abrechnung mit allen Originalbelegen bei der Buchhaltung ein. Digitale Belege sind erlaubt, wenn sie gut lesbar sind. Abrechnungen, die zu spät kommen, können abgelehnt werden. Erhaltene Vorschüsse werden spätestens mit der Abrechnung verrechnet. *(Abschnitt 8)*

**2. Wie viel bekomme ich, wenn ich mit meinem eigenen Auto fahre?**
Sie bekommen **0,25 Euro je gefahrenem Kilometer**, wenn die Nutzung des Privatwagens genehmigt wurde. Parkgebühren werden gegen Beleg zusätzlich erstattet. Schäden am eigenen Fahrzeug übernimmt das Unternehmen nicht, außer es gibt dazu eine gesonderte Vereinbarung. *(Abschnitt 4.3)*

**3. Darf ich innerhalb Deutschlands fliegen?**
Nur wenn die **einfache Bahnfahrt länger als fünf Stunden** dauern würde. Flüge werden in der Economy Class und ausschließlich über die Reisestelle gebucht. Zusatzleistungen wie Sitzplatzwahl oder zusätzliches Gepäck werden nur erstattet, wenn sie dienstlich notwendig sind. *(Abschnitt 4.2)*
*Hinweis:* In v2 steht „Inlandsflüge“. Gemeint ist das Inland aus Sicht des Unternehmens, vermutlich also Deutschland.

**4. Wann darf ich 1. Klasse Bahn fahren, und wie teuer darf mein Hotel sein?**
- **Bahn:** Grundsätzlich fahren Sie 2. Klasse. Die 1. Klasse ist erlaubt, wenn die **einfache Fahrt mehr als drei Stunden** dauert. Sitzplatzreservierungen werden erstattet. *(Abschnitt 4.1)*
- **Hotel:** Erstattet werden bis **130 Euro pro Nacht ohne Frühstück**, gegen Hotelrechnung. In Städten mit hohen Hotelpreisen oder während großer Messen kann Ihre Führungskraft im Einzelfall eine höhere Grenze genehmigen. Buchen Sie möglichst früh. *(Abschnitt 5)*

**5. Wer muss meine Dienstreise genehmigen?**
Jede Dienstreise muss **vor Reiseantritt** beantragt werden, schriftlich oder über das Reiseantragsformular im Intranet. Genehmigen muss sie Ihre **direkte Führungskraft**. Wenn die Reise voraussichtlich **mehr als 2.000 Euro** kostet, muss zusätzlich die **Geschäftsführung** freigeben. Ohne vorherige Genehmigung haben Sie keinen Anspruch auf Erstattung. *(Abschnitt 3)*

---
**Zusatzhinweis zu Trinkgeldern:** Viele werden fragen, ob Trinkgelder noch erstattet werden. Version 2 erwähnt Trinkgelder **gar nicht**. Abschnitt 7 nennt nur Nebenkosten wie Visagebühren, dienstliche Telefonate und Gepäckaufbewahrung als erstattungsfähig. Eine verbindliche Antwort lässt sich aus v2 deshalb nicht ableiten. Bitte klären Sie das mit der Personalabteilung. Laut Abschnitt 9 ist sie die Ansprechstelle für Fragen zur Richtlinie.

---

[Zurück zum Übungsblatt](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md)
