# Testlauf: Übung 3 / Station B Für Schnelle – Unklare Formulierungen in v2

**Herkunft:** Station B, Abschnitt „Für Schnelle“, zweiter Punkt in [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#für-schnelle-1): „Frag: ‚Gibt es in v2 Formulierungen, die unklar sind oder unterschiedlich verstanden werden können?‘“ Material: [richtlinie_reisekosten_v1.md](../07_Beispielmaterial/richtlinie_reisekosten_v1.md) und [richtlinie_reisekosten_v2.md](../07_Beispielmaterial/richtlinie_reisekosten_v2.md). Die [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md) (Station B) enthalten zu dieser Zusatzfrage **keinen** Erwartungswert, nur zur Änderungsliste und zum Rechenfall.

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf:** Im selben Gespräch kam zuerst der Basis-Prompt von Station B (Änderungstabelle), danach die Testfrage:

```text
Gibt es in v2 Formulierungen, die unklar sind oder unterschiedlich verstanden werden können?
```

**Was herauskommen soll (Prüfmaßstab dieses Testlaufs):** Benennung tatsächlich mehrdeutiger Stellen in v2 mit Zitat bzw. Abschnitt, ohne erfundene Probleme. Jede genannte Stelle muss in v2 auffindbar sein (Strg+F). Plausible Kandidaten:

- 4.1/4.2: „einfachen Fahrtdauer“ bzw. „einfache Bahnfahrt“ – laut Fahrplan oder tatsächlich, mit Umstiegen?
- 6: „jeweils aktuellen steuerlichen Pauschalen“ – kein Betrag genannt
- 8: „sechs Wochen nach Ende der Dienstreise“ – Stichtag, Folgen („können abgelehnt werden“)
- weitere echte Kandidaten aus v2: „voraussichtliche Kosten“ (3), „schriftlich“ (3), „zumutbar“, „in der Regel“, „kurze Strecken“ (4.4), „erfahrungsgemäß hohen Hotelpreisen“, „großer Messen“ (5), „Originalbelegen“ vs. „Digitale Belege“ (8), Inkrafttreten ohne Datum (9)

Keine Kritik an Regeln, die nicht in v2 stehen.

---

## Bewertung

Turn 1 (Änderungstabelle) zur Einordnung: Alle drei Modelle finden **alle 7 Änderungen** korrekt, keine Zahl falsch, keine redaktionelle Änderung als inhaltlich gezählt. Nachgerechnet mit `python3`: 400 × 0,30 = 120 €, 400 × 0,25 = 100 €, Differenz 20 € (Sonnet und Opus stimmen).

| Kriterium (Turn 2) | Haiku | Sonnet | Opus |
|---|---|---|---|
| Anzahl genannter Punkte | 7 | 8 (+ Hinweis „Kilometerpauschale eindeutig“) | 11 (in zwei Gruppen + Empfehlung) |
| Abschnitt zu jedem Punkt angegeben | ja | ja | ja |
| Fahrtdauer laut Fahrplan oder tatsächlich (4.1/4.2) | nur für 4.2 | ja, für 4.1 und 4.2 | ja, für 4.1 und 4.2 (mit Beispiel 2:55 h + Verspätung) |
| Verpflegung ohne Betrag (6) | ja („jeweils aktuelle steuerliche Pauschalen“) | nein | teilweise („entsprechend gekürzt“, nicht der fehlende Betrag) |
| Frist / Stichtag (8) | ja (ab Rückkehr, letztem Reisetag, Belegeingang?) | ja (Etappen, nachträgliche Belege) | nennt Formulierung „ziemlich klar“, kritisiert nur „können abgelehnt werden“ und Übergang |
| Inkrafttreten ohne Datum (9) | ja | ja | ja |
| Originalbelege vs. digitale Belege (8) | nein | ja | ja |
| Alle Fundstellen existieren in v2 | ja (Wortformen leicht abgewandelt) | ja (Wortformen leicht abgewandelt) | ja (zwei „Zitate“ nicht wörtlich) |
| Kritik an Text, der nicht in v2 steht | ja: Trinkgeld, Abteilungsleitung | ja: Trinkgeld (aber mit Bezug auf „Notwendige Nebenkosten“) | ja: Trinkgeld (mit Bezug auf „notwendigen Nebenkosten“), Abteilungsleitung |
| Konstruierte / schwache Probleme | „Unterschiedliche Schwellen“ (Nr. 2), „ab Eingang der Belege“ | Bewirtungs-„Schwelle“ (Nr. 8), Streik-Ausnahme | „Unstimmigkeit“ 3 h/5 h, die „zusammenpasst“ (Nr. 3) |
| Ergebnis | **brauchbar** | **gut** | **gut, aber sehr lang** |

**Wortlaut-Check per `grep` gegen v2** (Treffer 0 = Strg+F findet die Zeichenkette so nicht):

| Von Modell zitiert | Treffer | Tatsächlicher Text in v2 |
|---|---|---|
| „wenn die einfache Bahnfahrt länger als fünf Stunden dauern würde“ (Haiku, Opus) | 1 | wörtlich |
| „sechs Wochen nach Ende der Dienstreise“, „können abgelehnt werden“, „mit allen Originalbelegen“, „Digitale Belege sind zulässig“, „entsprechend gekürzt“, „dienstlich notwendig“, „kurze Strecken“, „schweres Gepäck“, „in der Regel“, „zumutbar“ | je 1 | wörtlich |
| „erfahrungsgemäß hohe Hotelpreise“ (Haiku) | 0 | „erfahrungsgemäß hohen Hotelpreisen“ |
| „jeweils aktuelle steuerliche Pauschalen“ (Haiku) | 0 | „jeweils aktuellen steuerlichen Pauschalen“ |
| „wirtschaftlichstes Verkehrsmittel“, „angemessen berücksichtigen“ (Sonnet) | 0 | „wirtschaftlichste Verkehrsmittel“, „angemessen zu berücksichtigen“ |
| „darf gebucht werden“ (Sonnet) | 0 | „darf die 1. Klasse gebucht werden“ |
| „große Messen“ (Sonnet, Opus) | 0 | „während großer Messen“ |
| „voraussichtlichen Kosten über 2.000 Euro“ (Opus, in Anführungszeichen) | 0 | „voraussichtliche Kosten 2.000 Euro übersteigen“ |
| „wenn sich dies voraussichtlich rechnet“ (Opus, in Anführungszeichen) | 0 | „wenn sich dies durch die Anzahl der geplanten Dienstreisen voraussichtlich rechnet“ |
| „Trinkgeld“, „Abteilungsleitung“ | 0 | kommen in v2 gar nicht vor (nur in v1) |
| „einfache Fahrtdauer“ (**Beispiel aus dem Prüfmaßstab selbst**) | 0 | „einer einfachen Fahrtdauer“ |

Fazit: **Kein Modell erfindet eine Fundstelle.** Alle Stellen sind inhaltlich in v2 vorhanden. Mehrere „Zitate“ sind aber gebeugt oder verkürzt und lassen sich mit Strg+F nicht 1:1 finden. Das betrifft auch das Beispiel im Prüfmaßstab.

## Gefundene Fehler mit Beleg

**Keine erfundenen Stellen, keine falschen Zahlen.** Die Fehler sind kleiner und liegen in der Einordnung:

1. **Kritik an Text, der nicht in v2 steht (alle drei).** Trinkgeld kommt in v2 nicht vor (grep: 0 Treffer). Alle drei nennen die Streichung als „unklare Formulierung“. Strenggenommen ist das eine **Lücke**, keine mehrdeutige Formulierung, und das Wissen stammt aus v1. Sonnet und Opus verankern den Punkt immerhin an echtem v2-Text („Notwendige Nebenkosten … werden gegen Beleg erstattet“ vs. „Kosten für private Zwecke“). Das ist ein berechtigter Auslegungskonflikt. Haiku begründet nur mit der Streichung.
2. **Abteilungsleitung (Haiku Nr. 3, Opus Nr. 4).** Haiku: „Es ist nicht klar, ob die Geschäftsführung die Abteilungsleitung ersetzt oder zusätzlich zur Führungskraft und Abteilungsleitung zustimmt.“ Opus: „ob die Abteilungsleitung jetzt gar nicht mehr beteiligt ist“. In v2 steht die Abteilungsleitung nicht (grep: 0 Treffer). Liest man nur v2, ist der Satz eindeutig: Führungskraft genehmigt, Geschäftsführung gibt „zusätzlich“ frei. Die Unklarheit entsteht nur aus dem Vergleich mit v1.
3. **Konstruierte Probleme.**
   - Haiku Nr. 2: „Die 1. Klasse ist ab drei Stunden Bahnfahrt erlaubt, Inlandsflüge sind erst ab fünf Stunden Bahnfahrt zulässig. Das kann zu Verwechslungen führen.“ Zwei verschiedene Regeln mit verschiedenen Schwellen sind nicht mehrdeutig.
   - Opus Nr. 3 nennt dasselbe eine „Unstimmigkeit“ und schreibt im nächsten Satz „Das passt zusammen“. Widerspricht sich selbst.
   - Sonnet Nr. 8: „bei Bewirtungen unklar, ab welcher Höhe oder in welchem Rahmen die Führungskraft zustimmen muss“. v2 Abschnitt 6: „Bewirtungen von Geschäftspartnern sind vorher mit der Führungskraft abzustimmen“ – also immer, ohne Schwelle. Das ist klar.
   - Haiku Nr. 5: Frist „ab Eingang der Belege“. v2 sagt eindeutig „nach Ende der Dienstreise“. Die Deutung ist weit hergeholt.
4. **Nicht wörtliche „Zitate“ (vor allem Opus).** Opus setzt „voraussichtlichen Kosten über 2.000 Euro“ und „wenn sich dies voraussichtlich rechnet“ in Anführungszeichen. Beides steht so nicht in v2 (siehe Tabelle oben). Inhaltlich richtig, aber wer mit Strg+F prüft, findet es nicht.
5. **Punkte über „unklar“ hinaus.** Mehrere Punkte sind Wünsche nach Zusatzregeln, keine Mehrdeutigkeiten: Streik-Ausnahme (Sonnet, Opus), Frist für die Freigabe durch die Geschäftsführung (Sonnet), „brutto oder netto“ (Sonnet), Auslandsflüge (Haiku, Sonnet). Das ist kein Fehler, verwässert aber die Antwort.
6. **Nebenbefund Turn 1, Haiku Zeile 6:** „Ob es trotzdem erstattet wird, bleibt offen (siehe Nachricht 2).“ Verweis auf eine Nachricht, die es zu dem Zeitpunkt noch nicht gab. Kleiner Artefakt, kein inhaltlicher Fehler.
7. **Nebenbefund Turn 1, Opus:** In der Tabelle vorsichtig („Wahrscheinlich bekommt man Trinkgeld nicht mehr erstattet … nachfragen“), in der Zusammenfassung dann als Tatsache: „kein Trinkgeld mehr (Nr. 6)“.

**Abgleich mit den drei erwarteten Kandidaten:**

- *Fahrtdauer laut Fahrplan oder tatsächlich:* Sonnet und Opus für 4.1 und 4.2, Haiku nur für 4.2.
- *Verpflegung ohne Betrag:* nur Haiku nennt den fehlenden Betrag. Sonnet gar nicht, Opus nur „entsprechend gekürzt“.
- *Stichtag der 6-Wochen-Frist:* Haiku und Sonnet ja. Opus hält die Formulierung für „ziemlich klar“. Das ist vertretbar, denn „nach Ende der Dienstreise“ ist ein benannter Stichtag.

## Lehren für die Auswertung

1. **Die Übung funktioniert, aber anders als „findet die KI alle Fehler?“.** Alle drei Modelle liefern eine lange, plausible Liste. Keins erfindet eine Stelle. Die Lehre: **Bei „Was ist unklar?“ findet der Assistent fast immer etwas.** Die Arbeit der Teilnehmenden ist das Sortieren: Was ist echt mehrdeutig, was ist nur eine Lücke, was ist konstruiert?
2. **Drei Schubladen für die Auswertung.** Lass die Teilnehmenden jeden Punkt einordnen:
   - **mehrdeutig** (Text kann man so oder so lesen: Fahrtdauer, „zumutbar“, „Originalbelegen“ vs. „Digitale Belege“),
   - **Lücke** (etwas fehlt: Trinkgeld, Datum des Inkrafttretens, Betrag der Verpflegungspauschale),
   - **konstruiert** (bei genauem Lesen klar: 3 h vs. 5 h, Bewirtung, „ab Eingang der Belege“).
3. **Wissen aus v1 sickert ein.** Trinkgeld und Abteilungsleitung stehen nicht in v2. Die Modelle kritisieren sie trotzdem, weil v1 im selben Gespräch liegt. Gute Frage an die Runde: „Würde jemand, der nur v2 liest, hier stolpern?“ Bei Trinkgeld ja (Nebenkosten vs. private Zwecke), bei Abteilungsleitung nein.
4. **Strg+F-Probe zeigt Grenzen von „Zitaten“.** Deutsche Wortformen werden angepasst („hohe Hotelpreise“ statt „hohen Hotelpreisen“), Opus kürzt Sätze in Anführungszeichen. Tipp für Teilnehmende: nach einem **Kernwort** suchen („Hotelpreis“, „Fahrtdauer“), nicht nach dem ganzen Zitat. Wer wörtliche Zitate braucht, muss sie ausdrücklich verlangen.
5. **Mehr ist nicht besser.** Opus liefert 11 Punkte, sortiert und mit Empfehlung. Das wirkt gründlich, kostet aber am meisten Prüfzeit und enthält trotzdem eine Selbstwiderspruch-Stelle. Haiku ist kürzer und findet als einziges Modell die fehlende Verpflegungspauschale.
6. **Brücke zum Rechenfall.** Haikus Punkt zu den „jeweils aktuellen steuerlichen Pauschalen“ passt direkt zur letzten Für-Schnelle-Frage (Verpflegung): Genau diese Lücke führt dazu, dass ein Assistent Beträge „von woanders“ mitbringt.
7. **Zeit:** Die Frage dauert unter einer Minute. Das Prüfen von 7 bis 11 Punkten mit Strg+F dauert 5 bis 10 Minuten. Für Schnelle passt das, aber nur, wenn die Prüfung eingeschränkt wird (siehe Vorschlag).

**Vorschlag für einen schärferen Prompt** (in diesem Testlauf **nicht** geprüft):

```text
Nenne höchstens 5 Stellen in v2, die man wirklich unterschiedlich verstehen kann.
Zitiere jede Stelle wörtlich aus v2 (so, dass ich sie mit Strg+F finde) und nenne den Abschnitt.
Beschreibe für jede Stelle die zwei möglichen Lesarten.
Lass Punkte weg, die nur fehlen, und alles, was nur in v1 steht.
```

---

## Gesprächsprotokoll: Claude Haiku

### Nutzer 1

```text
Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?
```

(Anhänge: [richtlinie_reisekosten_v1.md](../07_Beispielmaterial/richtlinie_reisekosten_v1.md), [richtlinie_reisekosten_v2.md](../07_Beispielmaterial/richtlinie_reisekosten_v2.md))

### Assistent 1

Ich habe beide Fassungen verglichen. Die Abschnitte 1, 2, 4.4, 6 und 9 sind inhaltlich gleich geblieben. Folgende inhaltlichen Änderungen gibt es:

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung bei hohen Kosten (Abschnitt 3) | Bei voraussichtlichen Reisekosten über 2.000 Euro ist zusätzlich die Freigabe durch die **Abteilungsleitung** nötig. | Bei voraussichtlichen Reisekosten über 2.000 Euro ist zusätzlich die Freigabe durch die **Geschäftsführung** nötig. | Die zweite Freigabe kommt jetzt von ganz oben. Das kann die Genehmigung größerer Reisen länger dauern lassen. |
| 2 | 1. Klasse bei der Bahn (Abschnitt 4.1) | Die 1. Klasse darf gebucht werden, wenn die einfache Fahrt länger als **vier** Stunden dauert. | Die 1. Klasse darf gebucht werden, wenn die einfache Fahrt länger als **drei** Stunden dauert. | Bei Fahrten zwischen drei und vier Stunden darf man jetzt die 1. Klasse buchen. |
| 3 | Inlandsflüge (Abschnitt 4.2) | Keine Regel zu Inlandsflügen. Flüge sind in der Economy Class zu buchen. | Neu: Inlandsflüge sind nur zulässig, wenn die einfache Bahnfahrt **länger als fünf Stunden** dauern würde. | Für Inlandsreisen muss man zuerst prüfen, ob die Bahn länger als fünf Stunden braucht. Nur dann ist ein Flug erlaubt. |
| 4 | Kilometerpauschale privates Auto (Abschnitt 4.3) | 0,30 Euro je gefahrenem Kilometer. | 0,25 Euro je gefahrenem Kilometer. | Wer mit dem privaten Auto fährt, bekommt pro Kilometer 5 Cent weniger. |
| 5 | Übernachtungsobergrenze (Abschnitt 5) | Bis 110 Euro pro Nacht (ohne Frühstück) gegen Hotelrechnung. | Bis 130 Euro pro Nacht (ohne Frühstück) gegen Hotelrechnung. | Hotelübernachtungen dürfen bis 130 Euro pro Nacht kosten, ohne dass eine Ausnahme nötig ist. |
| 6 | Trinkgeld (Abschnitt 7) | Trinkgeld kann bis 10 % des Rechnungsbetrags erstattet werden, wenn es auf dem Beleg vermerkt ist. | Die Regel zum Trinkgeld ist ersatzlos gestrichen. | Trinkgeld ist nicht mehr ausdrücklich erstattungsfähig. Ob es trotzdem erstattet wird, bleibt offen (siehe Nachricht 2). |
| 7 | Abrechnungsfrist (Abschnitt 8) | Abrechnung innerhalb von **drei Monaten** nach Ende der Dienstreise. | Abrechnung innerhalb von **sechs Wochen** nach Ende der Dienstreise. | Die Frist wird deutlich kürzer. Belege sollten zeitnah eingereicht werden. |

### Nutzer 2

```text
Gibt es in v2 Formulierungen, die unklar sind oder unterschiedlich verstanden werden können?
```

### Assistent 2

Ja, einige Formulierungen in v2 sind unklar oder lassen mehrere Deutungen zu:

1. **Inlandsflüge (Abschnitt 4.2):** "Wenn die einfache Bahnfahrt länger als fünf Stunden dauern würde" lässt offen, wie diese Dauer ermittelt wird: anhand der Fahrplanauskunft, des tatsächlichen Buchungsangebots oder inklusive Umstiegszeiten? Die Regel sagt außerdem nichts über Auslandsflüge.
2. **Unterschiedliche Schwellen:** Die 1. Klasse ist ab drei Stunden Bahnfahrt erlaubt, Inlandsflüge sind erst ab fünf Stunden Bahnfahrt zulässig. Das kann zu Verwechslungen führen.
3. **Freigabe bei hohen Kosten (Abschnitt 3):** Es ist nicht klar, ob die Geschäftsführung die Abteilungsleitung ersetzt oder zusätzlich zur Führungskraft und Abteilungsleitung zustimmt. Ungeklärt ist auch, ob die 2.000 Euro pro Reise, pro Person oder als Gesamtsumme gelten.
4. **Trinkgeld (Abschnitt 7):** Die Streichung lässt offen, ob Trinkgeld gar nicht mehr erstattet wird oder ob es nur nicht mehr geregelt ist. Mitarbeitende könnten weiterhin von den bisherigen 10 % ausgehen.
5. **Abrechnungsfrist (Abschnitt 8):** Unklar ist, ob die sechs Wochen ab Rückkehr, ab dem letzten Reisetag oder ab Eingang der Belege laufen. Auch ist nicht geregelt, was bei verspäteter Einreichung passiert (die Formulierung "können abgelehnt werden" ist eine Kann-Regel).
6. **Inkrafttreten (Abschnitt 9):** Es fehlt ein Datum. Offen ist, ob v2 auch für Reisen gilt, die schon begonnen wurden oder deren Abrechnung noch aussteht.
7. **Unbestimmte Begriffe, die in beiden Versionen vorkommen:** "in der Regel" (Abschnitt 4.4), "zumutbar" (Abschnitt 4.4), "erfahrungsgemäß hohe Hotelpreise" (Abschnitt 5), "jeweils aktuelle steuerliche Pauschalen" (Abschnitt 6) und "angemessen" (Abschnitt 2). Mitarbeitende können diese Begriffe unterschiedlich auslegen.

---

## Gesprächsprotokoll: Claude Sonnet

### Nutzer 1

```text
Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?
```

(Anhänge: [richtlinie_reisekosten_v1.md](../07_Beispielmaterial/richtlinie_reisekosten_v1.md), [richtlinie_reisekosten_v2.md](../07_Beispielmaterial/richtlinie_reisekosten_v2.md))

### Assistent 1

Ich habe beide Fassungen verglichen und 7 inhaltliche Änderungen gefunden. Alle anderen Abschnitte (1, 2, 4.4, 6 und 9) sind unverändert.

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung bei hohen Reisekosten (Abschn. 3) | Bei voraussichtlichen Kosten über 2.000 Euro ist zusätzlich die Freigabe der **Abteilungsleitung** nötig. | Bei voraussichtlichen Kosten über 2.000 Euro ist zusätzlich die Freigabe der **Geschäftsführung** nötig. | Teure Reisen müssen jetzt eine Ebene höher freigegeben werden. Das kann länger dauern, also früher beantragen. |
| 2 | Bahn: 1. Klasse (Abschn. 4.1) | 1. Klasse erlaubt ab einer einfachen Fahrtdauer von mehr als **4 Stunden**. | 1. Klasse erlaubt ab einer einfachen Fahrtdauer von mehr als **3 Stunden**. | Die 1. Klasse darf früher gebucht werden, nämlich schon bei Fahrten über 3 Stunden. |
| 3 | Inlandsflüge (Abschn. 4.2) | Keine besondere Einschränkung für Inlandsflüge, es galt nur die Economy-Vorgabe. | Inlandsflüge sind nur zulässig, wenn die einfache Bahnfahrt **länger als 5 Stunden** dauern würde. | Für Inlandsziele wird in der Regel die Bahn gebucht. Ein Flug ist nur bei langen Bahnstrecken erlaubt. |
| 4 | Kilometerpauschale (Abschn. 4.3) | **0,30 Euro** pro km mit dem privaten Kfz. | **0,25 Euro** pro km mit dem privaten Kfz. | Die Erstattung sinkt um 5 Cent pro km. Bei 400 km Fahrt sind das 20 Euro weniger. |
| 5 | Hotelkosten (Abschn. 5) | Bis **110 Euro** pro Nacht (ohne Frühstück). | Bis **130 Euro** pro Nacht (ohne Frühstück). | Der Spielraum für Übernachtungen wächst um 20 Euro pro Nacht. Die Ausnahmeregelung durch die Führungskraft bleibt bestehen. |
| 6 | Trinkgeld (Abschn. 7) | Trinkgelder können bis 10 % des Rechnungsbetrags erstattet werden, wenn sie auf dem Beleg vermerkt sind. | Der Passus zu Trinkgeldern ist **entfallen**. | Trinkgeld wird voraussichtlich nicht mehr erstattet bzw. ist nicht mehr ausdrücklich geregelt. Im Zweifel vorher klären. |
| 7 | Abrechnungsfrist (Abschn. 8) | Einreichung innerhalb von **drei Monaten** nach Reiseende. | Einreichung innerhalb von **sechs Wochen** nach Reiseende. | Die Frist ist deutlich kürzer. Abrechnungen sollten zeitnah gemacht werden, sonst droht die Ablehnung. |

### Nutzer 2

```text
Gibt es in v2 Formulierungen, die unklar sind oder unterschiedlich verstanden werden können?
```

### Assistent 2

Ja, einige Stellen in v2 lassen Spielraum für Auslegung.

1. **Streichung des Trinkgelds (Abschn. 7).** Die Regel ist einfach weggefallen, ohne zu sagen, ob das ein Verbot ist oder nur keine Regelung mehr. Fallen Trinkgelder jetzt unter "notwendige Nebenkosten" (gegen Beleg erstattbar) oder unter "private Zwecke" (nicht erstattbar)? Das sollte ausdrücklich geklärt werden.

2. **Inlandsflüge (Abschn. 4.2).** "Einfache Bahnfahrt länger als fünf Stunden" lässt offen, nach welcher Grundlage die Dauer bemessen wird. Zählt die fahrplanmäßige Dauer, die tatsächliche Dauer mit Verspätungen oder die Dauer inklusive Umstiege und Anfahrt zum Bahnhof? Auch ist nicht geregelt, wer das prüft und wie das nachgewiesen wird. Zudem steht dort "Inlandsflüge", aber Strecken mit Ausland (zum Beispiel Zürich oder Wien) werden nicht angesprochen. Außerdem fehlt eine Ausnahme, falls die Bahn nicht verfügbar ist, etwa bei Streik.

3. **Bahn, 1. Klasse (Abschn. 4.1).** "Darf gebucht werden" ist eine Kann-Regelung. Es ist unklar, ob ein Anspruch besteht oder ob die Führungskraft entscheiden kann. Auch hier ist offen, ob die fahrplanmäßige oder tatsächliche Fahrtdauer gilt und ob "einfach" je Teilstrecke oder für die Gesamtreise mit Umstiegen gemeint ist.

4. **Hotelobergrenze (Abschn. 5).** Der Betrag von 130 Euro gilt "ohne Frühstück". Unklar ist, wie vorzugehen ist, wenn Frühstück im Preis enthalten ist und nicht getrennt ausgewiesen wird. Außerdem ist offen, was "Städte mit erfahrungsgemäß hohen Hotelpreisen" und "große Messen" konkret sind und wie hoch die höhere Obergrenze sein darf. Es ist auch nicht festgelegt, ob 130 Euro brutto oder netto gemeint sind.

5. **Genehmigung über 2.000 Euro (Abschn. 3).** "Voraussichtliche Kosten" ist nicht definiert. Zählen Reise, Hotel, Verpflegung und Nebenkosten zusammen? Gilt die Grenze pro Person oder pro Reise mit mehreren Teilnehmenden? Zudem ist nicht geregelt, wie die Geschäftsführung die Freigabe erteilt und in welcher Frist.

6. **Abrechnungsfrist (Abschn. 8).** "Sechs Wochen nach Ende der Dienstreise" ist nicht ganz eindeutig bei Reisen mit mehreren Etappen oder bei Belegen, die erst später eintreffen, etwa Hotelrechnungen im Nachgang. Es fehlt auch eine Übergangsregel, ob die neue Frist für bereits laufende oder abgeschlossene Reisen gilt. Zudem ist "Original­belege" neben "digitale Belege sind zulässig" widersprüchlich oder zumindest erklärungsbedürftig.

7. **Inkrafttreten (Abschn. 9).** "Mit ihrer Veröffentlichung im Intranet" nennt kein konkretes Datum. Für Reisen, die vor der Veröffentlichung gebucht wurden, aber danach stattfinden, ist nicht klar, welche Version gilt.

8. **Unveränderte, aber auslegbare Begriffe.** "Wirtschaftlichstes Verkehrsmittel", "angemessen berücksichtigen", "zumutbar", "kurze Strecken" und "schweres Gepäck" (Abschn. 2 und 4.4) sind nicht beziffert. Das führt in der Praxis häufig zu Diskussionen. Zusätzlich ist bei Bewirtungen unklar, ab welcher Höhe oder in welchem Rahmen die Führungskraft zustimmen muss.

Die Kilometerpauschale (0,25 Euro) ist dagegen eindeutig formuliert.

---

## Gesprächsprotokoll: Claude Opus

### Nutzer 1

```text
Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?
```

(Anhänge: [richtlinie_reisekosten_v1.md](../07_Beispielmaterial/richtlinie_reisekosten_v1.md), [richtlinie_reisekosten_v2.md](../07_Beispielmaterial/richtlinie_reisekosten_v2.md))

### Assistent 1

Ich habe beide Fassungen Abschnitt für Abschnitt verglichen. Es gibt **7 inhaltliche Änderungen**. Die Abschnitte 1 (Geltungsbereich), 2 (Grundsätze), 4.4 (Mietwagen und Taxi), 6 (Verpflegung) und 9 (Inkrafttreten) sind wortgleich geblieben. Auch reine Formulierungsänderungen habe ich nicht gefunden: Außer den unten genannten Stellen ist der Text identisch.

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung von Reisen über 2.000 € (Abschnitt 3) | Zusätzliche Freigabe durch die **Abteilungsleitung** | Zusätzliche Freigabe durch die **Geschäftsführung** | Teure Reisen müssen jetzt eine Ebene höher freigegeben werden. Das kann länger dauern, also früher beantragen. Die direkte Führungskraft muss weiterhin zustimmen. |
| 2 | 1. Klasse bei der Bahn (Abschnitt 4.1) | Erlaubt ab einer einfachen Fahrtdauer von **mehr als vier Stunden** | Erlaubt ab einer einfachen Fahrtdauer von **mehr als drei Stunden** | Verbesserung: Die 1. Klasse ist schon bei kürzeren Strecken erlaubt. |
| 3 | Inlandsflüge (Abschnitt 4.2) | Keine besondere Regel (nur Economy Class und Buchung über die Reisestelle) | **Neu:** Inlandsflüge nur, wenn die einfache Bahnfahrt **länger als fünf Stunden** dauern würde | Einschränkung: Bei Strecken, die mit der Bahn bis zu fünf Stunden dauern, muss man den Zug nehmen. Vor der Buchung also die Bahnfahrzeit prüfen. |
| 4 | Kilometerpauschale für das private Auto (Abschnitt 4.3) | **0,30 €** je gefahrenem Kilometer | **0,25 €** je gefahrenem Kilometer | Verschlechterung: Für die gleiche Strecke gibt es weniger Geld. Beispiel: Bei 400 km sind das 100 € statt 120 €, also 20 € weniger. |
| 5 | Obergrenze für Hotelkosten (Abschnitt 5) | Bis **110 €** pro Nacht (ohne Frühstück) | Bis **130 €** pro Nacht (ohne Frühstück) | Verbesserung: 20 € mehr Spielraum pro Nacht. Die höhere Obergrenze im Einzelfall (teure Städte, Messen) gibt es weiterhin. |
| 6 | Trinkgeld (Abschnitt 7) | Trinkgeld wird bis **10 % des Rechnungsbetrags** erstattet, wenn es auf dem Beleg vermerkt ist | **Regel gestrichen.** Trinkgeld wird nicht mehr erwähnt. | Wahrscheinlich bekommt man Trinkgeld nicht mehr erstattet. Weil die Richtlinie dazu aber gar nichts mehr sagt, sollte man das bei Personal oder Finanzen nachfragen. |
| 7 | Frist für die Abrechnung (Abschnitt 8) | Innerhalb von **drei Monaten** nach Reiseende | Innerhalb von **sechs Wochen** nach Reiseende | Verschärfung: Die Frist ist ungefähr halb so lang. Wer zu spät abrechnet, riskiert, dass die Abrechnung abgelehnt wird. Am besten gleich nach der Reise abrechnen. |

**Kurz zusammengefasst:**
- **Verbesserungen:** 1. Klasse bei der Bahn früher erlaubt (Nr. 2), höhere Hotel-Obergrenze (Nr. 5)
- **Verschlechterungen oder Verschärfungen:** weniger Kilometergeld (Nr. 4), kein Trinkgeld mehr (Nr. 6), kürzere Abrechnungsfrist (Nr. 7), Inlandsflüge eingeschränkt (Nr. 3)
- **Anderer Ablauf:** Reisen über 2.000 € gibt jetzt die Geschäftsführung frei (Nr. 1)

Hinweis: In v2 steht kein Datum, ab wann die neue Fassung gilt. Für Reisen, die gerade in der Zeit der Umstellung stattfinden, sollte man klären, welche Fassung gilt.

### Nutzer 2

```text
Gibt es in v2 Formulierungen, die unklar sind oder unterschiedlich verstanden werden können?
```

### Assistent 2

Ja, einige. Ich habe sie danach sortiert, wie wahrscheinlich sie im Alltag zu Rückfragen oder Streit führen.

**Unklarheiten bei den neuen oder geänderten Regeln**

1. **Trinkgeld (Abschnitt 7):** Die Regel ist einfach gestrichen. Es steht nicht ausdrücklich da, dass Trinkgeld nicht mehr erstattet wird. Man kann den Text so lesen, dass Trinkgeld gar nicht mehr erstattet wird. Man kann aber auch argumentieren, dass es zu den „notwendigen Nebenkosten“ gehört, die gegen Beleg erstattet werden. *Vorschlag:* Eindeutig festlegen, zum Beispiel „Trinkgelder werden nicht erstattet“ oder eine neue Obergrenze nennen.

2. **Inlandsflüge (Abschnitt 4.2), „wenn die einfache Bahnfahrt länger als fünf Stunden dauern würde“:**
   - Welche Fahrtdauer zählt? Die schnellste Verbindung laut Fahrplan, eine Verbindung zur passenden Uhrzeit oder die Strecke von Tür zu Tür?
   - Zählen Umstiege und Wartezeiten mit?
   - Was bedeutet „Inland“? Ist damit Deutschland gemeint oder das Land, von dem aus die Reise beginnt? Gilt die Regel auch für Inlandsflüge innerhalb eines anderen Landes während einer Auslandsreise?
   - Gibt es Ausnahmen, etwa bei Terminen am frühen Morgen, bei Bahnstreik oder wenn Material transportiert werden muss?

3. **1. Klasse ab „mehr als drei Stunden“ (Abschnitt 4.1):** Auch hier ist offen, ob die Fahrtdauer laut Fahrplan oder die tatsächliche Fahrtdauer zählt. Ein Beispiel: Die Fahrt ist mit 2:55 Stunden geplant und hat dann Verspätung. Offen ist außerdem, ob Umstiege mitzählen. Eine Unstimmigkeit gibt es zusätzlich: Für die 1. Klasse gilt die Grenze von drei Stunden, für die Pflicht zur Bahn statt Flugzeug die Grenze von fünf Stunden. Das passt zusammen, sollte aber ausdrücklich so beschrieben werden.

4. **Geschäftsführung bei „voraussichtlichen Kosten über 2.000 Euro“ (Abschnitt 3):** Wer schätzt die Kosten und wie? Zählen Verpflegungspauschalen und Nebenkosten mit? Was passiert, wenn eine Reise auf 1.900 € geschätzt war und am Ende 2.300 € kostet? Muss die Freigabe dann nachträglich eingeholt werden? Offen ist auch, ob die Abteilungsleitung jetzt gar nicht mehr beteiligt ist oder nur nicht mehr freigeben muss.

5. **Frist von „sechs Wochen nach Ende der Dienstreise“ (Abschnitt 8):** Diese Formulierung ist ziemlich klar. Unklar ist aber, dass „verspätet eingereichte Abrechnungen *können* abgelehnt werden“. Das hängt vom Ermessen ab, und es steht nicht da, wer entscheidet und nach welchen Kriterien. Auch der Übergang ist nicht geregelt: Gilt für Reisen vor Inkrafttreten von v2 noch die alte Frist von drei Monaten?

**Unklarheiten, die schon in v1 standen und in v2 geblieben sind**

6. **„Mit allen Originalbelegen“ und „Digitale Belege sind zulässig“ (Abschnitt 8):** Die beiden Aussagen widersprechen sich zum Teil. Muss man das Papieroriginal trotzdem aufheben oder abgeben? Was heißt „gut lesbar“?

7. **„Schriftlich“ beantragen (Abschnitt 3):** Reicht eine E-Mail? Rechtlich und umgangssprachlich wird „schriftlich“ oft unterschiedlich verstanden.

8. **Hotel: „Städte mit erfahrungsgemäß hohen Hotelpreisen“ und „große Messen“ (Abschnitt 5):** Es gibt keine Liste und keine Kriterien. Welche Städte und Messen gemeint sind, hängt davon ab, wie die jeweilige Führungskraft das sieht. Mitarbeitende werden je nach Abteilung unterschiedlich behandelt. Unklar ist auch, ob die Ausnahme vor der Buchung genehmigt werden muss.

9. **Unbestimmte Begriffe:** Gemeint sind „zumutbar“ (öffentliche Verkehrsmittel, Alternative zum Taxi), „kurze Strecken“ (Taxi), „dienstlich notwendig“ (Zusatzleistungen beim Flug), „in der Regel“ (Kompaktklasse) und „wenn sich dies voraussichtlich rechnet“ (Bahncard). Keiner dieser Begriffe ist mit einem Maßstab oder Beispiel erklärt. Offen ist auch, wer jeweils entscheidet.

10. **Verpflegung, „entsprechend gekürzt“ (Abschnitt 6):** Es steht nicht da, um wie viel gekürzt wird. Wahrscheinlich sind die steuerlichen Kürzungssätze gemeint, das wird aber nicht gesagt.

11. **Inkrafttreten (Abschnitt 9):** „Mit ihrer Veröffentlichung im Intranet“ nennt kein konkretes Datum. In v2 gibt es auch weder ein Versionsdatum noch eine Übergangsregel. Bei einer Reise, die vor der Veröffentlichung gebucht und danach angetreten wurde, ist unklar, welche Kilometerpauschale, welche Hotel-Obergrenze und welche Frist gelten.

**Meine Empfehlung:** Am dringendsten sollten Nr. 1 (Trinkgeld), Nr. 2 (Inlandsflüge) und Nr. 11 (Inkrafttreten mit Übergangsregel) nachgebessert werden. Sie betreffen die neuen Regeln direkt und führen im Alltag am ehesten zu Rückfragen. Zur Übergangsregel ein Beispiel: „Für Reisen, die vor dem [Datum] beantragt wurden, gilt Version 1.“
