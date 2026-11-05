# Testlauf: Übung 3 / Station B Für Schnelle – Rechenfall Fahrt + Hotel, dann Verpflegung

**Herkunft:** Station B, Abschnitt „Für Schnelle“, dritter Punkt in [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#für-schnelle-1): „Spiel einen Fall durch – und rechne danach selbst nach“ (Rechenfall 180 km hin, 180 km zurück, Hotel 125 € ohne Frühstück). Danach: „Frag danach auch nach der Verpflegung. Steht dazu ein Betrag in den Richtlinien – oder bringt der KI-Assistent Zahlen von woanders mit?“ Der Erwartungswert stammt aus [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md), Station B, „Rechenfall ‚Für Schnelle‘“. Material: [richtlinie_reisekosten_v1.md](../07_Beispielmaterial/richtlinie_reisekosten_v1.md) und [richtlinie_reisekosten_v2.md](../07_Beispielmaterial/richtlinie_reisekosten_v2.md).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf:** Im selben Gespräch kam zuerst der Basis-Prompt von Station B (Vergleichstabelle), dann der Rechenfall-Prompt vom Übungsblatt, dann die freie Nachfrage:

```text
Und was bekomme ich für die Verpflegung erstattet?
```

**Was laut Material herauskommen soll:**

| | v1 | v2 |
|---|---|---|
| Fahrt (Abschnitt 4.3) | 360 km × 0,30 € = **108,00 €** | 360 km × 0,25 € = **90,00 €** |
| Übernachtung (Abschnitt 5) | Obergrenze 110 € → **110,00 €** | Obergrenze 130 € → **125,00 €** (voll) |
| **Summe** | **218,00 €** | **215,00 €** |

Typischer Fehler laut Lösungshinweisen: Rechnen mit 180 statt 360 km. Verpflegung: aus den Richtlinien **nicht** berechenbar. Abschnitt 6 ist in v1 und v2 wortgleich: „Für Verpflegungsmehraufwendungen gelten die jeweils aktuellen steuerlichen Pauschalen. […]“ Konkrete Euro-Beträge kommen nicht aus dem Dokument.

**Fundstellen (beide Fassungen geprüft, per `diff`):**

- 4.3 v1: „Kilometerpauschale von 0,30 Euro je gefahrenem Kilometer“, v2: „0,25 Euro“. Gleich in beiden: „mit Genehmigung“, „Parkgebühren werden gegen Beleg erstattet“.
- 5 v1: „bis zu einem Betrag von 110 Euro pro Nacht (ohne Frühstück)“, v2: „130 Euro“. Gleich in beiden: Ausnahme durch die Führungskraft für teure Städte und Messen.
- 6 (wortgleich): keine Euro-Beträge, nur Verweis auf die steuerlichen Pauschalen, Kürzung bei gestellten Mahlzeiten, Bewirtung mit Beleg.
- 9 (wortgleich): „Fragen zur Richtlinie beantwortet die Personalabteilung.“

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Hin- und Rückweg addiert (360 km, nicht 180 km) | ja | ja | ja (begründet mit „je gefahrenem Kilometer“) |
| Fahrt v1 108,00 € / v2 90,00 € | ja | ja | ja |
| Hotel v1 auf 110 € gekappt / v2 125 € voll | ja | ja | ja |
| Summen 218,00 € / 215,00 € | ja | ja | ja |
| Abschnitt zu jeder Zahl genannt | ja (als „§ 4.3“, „§ 5“) | ja (je Fassung getrennt) | ja |
| Nur Angaben aus den Fassungen (Turn 2) | ja | ja | ja |
| Hinweise Genehmigung / Parkgebühren / Ausnahme Führungskraft | ja | ja | ja (am vollständigsten) |
| Verpflegung: sagt klar, dass kein Betrag in den Richtlinien steht | ja | ja | ja |
| Verpflegung: nennt keine Euro-Beträge aus eigenem Wissen | ja (lehnt ausdrücklich ab) | ja (lehnt ausdrücklich ab) | **nein** – nennt 14 €/28 €, Kürzung 5,60 €/11,20 €, rechnet „ca. 246 €/243 €“ (als allgemeines Wissen gekennzeichnet) |
| Verweist auf Personalabteilung/Buchhaltung | ja | ja | ja (mit Abschnitt 9) |
| Ergebnis Rechenfall | **bestanden** | **bestanden** | **bestanden** |
| Ergebnis Verpflegung | **bestanden** | **bestanden** | **teilweise** – sauber gekennzeichnet, aber Fremdwissen in die Gesamtsumme gemischt |

Nachgerechnet mit `python3`: 360 × 0,30 = 108,00; 360 × 0,25 = 90,00; 108 + 110 = 218; 90 + 125 = 215; Differenzen 18 € (Fahrt), 15 € (Hotel), 3 € (gesamt). Opus: 0,2 × 28 = 5,60; 0,4 × 28 = 11,20; 218 + 28 = 246; 215 + 28 = 243; Beispiel Turn 1: 500 km × 0,05 € = 25 €. Alle Rechnungen stimmen.

**Ergebnis kurz:** Den Rechenfall lösen alle drei Modelle fehlerfrei. Der Stolperstein „180 statt 360 km“ ist in diesem Testlauf bei keinem Modell aufgetreten. Bei der Verpflegung zeigt nur Opus, worauf die Übung zielt: Es bringt Zahlen von außerhalb des Dokuments mit.

## Gefundene Fehler mit Beleg

### Rechenfall (Turn 2)

Keine sachlichen Fehler bei allen drei Modellen.

Kleinigkeit bei Haiku: Es schreibt „§ 4.3“, „§ 5“. Die Richtlinie hat nummerierte Abschnitte, keine Paragrafen. Die Angabe ist trotzdem eindeutig.

### Verpflegung (Turn 3)

- **Opus – Beträge aus allgemeinem Wissen:** „14 € für den Anreisetag und 14 € für den Abreisetag […] 28 € für einen vollen Kalendertag“, „20 % […] für ein Frühstück und 40 % für ein Mittag- oder Abendessen, also 5,60 € bzw. 11,20 €“ und „v1: 218 € + ca. 28 € = ca. 246 €“. Beleg: Abschnitt 6 beider Fassungen nennt keinen Betrag. Die Zahlen sind nicht frei erfunden. Sie entsprechen dem deutschen Steuerrecht nach Stand des Modellwissens, sind aber **unbelegt** im Sinne der Übung und können veraltet sein. Opus kennzeichnet sie korrekt („Einordnung aus allgemeinem Wissen (nicht aus der Richtlinie)“, „Ich kann nicht prüfen, ob sie für dieses Jahr noch stimmen“). Problematisch ist die Schlusszeile: Dort stehen die gesicherten 218/215 € und die unbelegten 28 € in einer gemeinsamen Summe. Wer nur die letzte Zeile liest, übernimmt „246 €“.
- **Sonnet – kleine unmarkierte Zusatzinfo:** „die Pauschalen sind abhängig von der Abwesenheitsdauer“. Das steht nicht in Abschnitt 6. Es stimmt sachlich, ist aber Fremdwissen ohne Kennzeichnung. Harmlos, eignet sich aber als Beispiel dafür, wie unauffällig Fremdwissen einfließt.
- **Haiku:** keine Fehler.

### Nebenbefunde zum Vergleich (Turn 1, gehört zu Station B Basis)

Alle drei finden die 7 Änderungen aus den Lösungshinweisen und zählen die Versionsnummer nicht mit. Dabei gibt es zwei Ausrutscher:

- **Haiku, Nr. 2 (1. Klasse) – Folge falsch herum:** „Auf mittleren Strecken (3 bis 4 Stunden) ist die 1. Klasse nicht mehr automatisch zulässig.“ Richtig ist das Gegenteil. v1 erlaubt die 1. Klasse ab „mehr als vier Stunden“, v2 schon ab „mehr als drei Stunden“. Zwischen 3 und 4 Stunden ist sie also **neu erlaubt**. Die Spalten v1/v2 sind richtig, nur die Erklärung für Mitarbeitende ist verdreht. Genau so ein Fehler würde in der Info-Mail weitergetragen.
- **Haiku, Nr. 5 (Hotel):** „Teurere Hotelzimmer werden vollständig erstattet.“ Das ist zu pauschal, es gilt nur bis 130 €.
- Sonnet und Opus: Turn 1 ist sachlich korrekt. Sonnet merkt richtig an, dass v2 Trinkgeld nicht ausdrücklich verbietet.

## Lehren für die Auswertung

1. **Rechenfall ist zu leicht als Fehler-Demo.** Alle drei Modelle rechnen 2 × 180 km korrekt und nennen die Abschnitte. Daraus lernt man: Bei klaren Zahlen im Dokument und dem Auftrag „Schritt für Schritt mit Abschnitt“ sind die Ergebnisse gut und lassen sich leicht nachprüfen. Selbst nachrechnen bleibt trotzdem Pflicht, weil andere Tools hier durchaus 180 km nehmen können.
2. **Die Verpflegungsfrage ist der eigentliche Lerneffekt.** Hier sieht man drei Spielarten nebeneinander: verweigern (Haiku), verweigern mit Hinweis auf fehlende Angaben (Sonnet) und hilfsbereit Fremdwissen liefern, sauber gekennzeichnet (Opus). Frage an die Gruppe: „Welche Antwort ist die beste für eine Abrechnung? Woher kommen die 14 €? Steht das irgendwo in unseren Dateien?“
3. **Kennzeichnung schützt nur, wenn man sie liest.** Opus trennt Fremdwissen ehrlich ab, rechnet es am Ende aber in „ca. 246 €“ ein. Genau diese Zahl landet sonst in der Mail an die Kollegin. Lehre: Bei Mischantworten immer fragen, welche Zahl aus welcher Quelle kommt.
4. **Vorgaben gelten nicht automatisch weiter.** „Nutze nur Angaben aus den beiden Fassungen“ stand nur im Rechenfall-Prompt. Bei der kurzen Nachfrage hat Opus diese Vorgabe nicht mehr als bindend behandelt. Haiku und Sonnet schon. Lehre: Wichtige Einschränkungen in der Nachfrage wiederholen.
5. **„Nicht erfunden“ ist nicht gleich „belegt“.** Die Opus-Zahlen sind vermutlich korrekt (Stand Modellwissen). Für die Übung zählt aber, dass sie nicht aus dem Dokument stammen und nicht geprüft werden können. Den Begriff „Halluzination“ hier vorsichtig verwenden. Besser ist „unbelegtes Wissen von außerhalb“.
6. **Bonus aus Turn 1:** Haikus verdrehte Erklärung zur 1. Klasse zeigt, dass auch richtige Spalten v1/v2 eine falsche Schlussfolgerung tragen können. Die Spalte „Was bedeutet das?“ also genauso prüfen wie die Zahlen.

---

## Gesprächsprotokoll: Haiku

### Nutzer 1

Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?

### Assistent 1

Ich habe beide Fassungen verglichen. Inhaltlich geändert haben sich folgende Punkte:

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung bei hohen Kosten (§ 3) | Bei voraussichtlichen Reisekosten über 2.000 Euro ist die Freigabe durch die Abteilungsleitung nötig. | Die Freigabe erfolgt durch die Geschäftsführung. | Bei teuren Reisen ist die nächste Freigabestufe die Geschäftsführung statt der Abteilungsleitung. |
| 2 | 1. Klasse bei der Bahn (§ 4.1) | Die 1. Klasse darf bei einer einfachen Fahrtdauer von mehr als 4 Stunden gebucht werden. | Schwelle sinkt auf mehr als 3 Stunden. | Auf mittleren Strecken (3 bis 4 Stunden) ist die 1. Klasse nicht mehr automatisch zulässig. |
| 3 | Inlandsflüge (§ 4.2) | Keine Einschränkung für Inlandsflüge. | Inlandsflüge sind nur zulässig, wenn die einfache Bahnfahrt mehr als 5 Stunden dauern würde. | Für Inlandsziele muss man vorher die Bahnzeit prüfen. Flüge sind nicht mehr frei wählbar. |
| 4 | Kilometerpauschale Privatauto (§ 4.3) | 0,30 Euro je gefahrenem Kilometer. | 0,25 Euro je gefahrenem Kilometer. | Für dieselbe Strecke gibt es weniger Geld, etwa 5 Cent pro Kilometer weniger. |
| 5 | Hotel-Obergrenze (§ 5) | Erstattung bis 110 Euro pro Nacht ohne Frühstück. | Erstattung bis 130 Euro pro Nacht ohne Frühstück. | Teurere Hotelzimmer werden vollständig erstattet. Der Spielraum steigt um 20 Euro. |
| 6 | Trinkgeld (§ 7) | Trinkgeld kann bis 10 % des Rechnungsbetrags erstattet werden, wenn es auf dem Beleg steht. | Die Regelung zu Trinkgeld ist entfallen. Trinkgeld wird nicht mehr erwähnt. | Trinkgeld sollte man nicht mehr als erstattungsfähig einplanen. Eine Rücksprache mit der Buchhaltung ist sinnvoll. |
| 7 | Abrechnungsfrist (§ 8) | Einreichung innerhalb von 3 Monaten nach Ende der Dienstreise. | Einreichung innerhalb von 6 Wochen nach Ende der Dienstreise. | Die Abrechnung muss deutlich schneller erfolgen. |

Unverändert sind die Verpflegung (§ 6), die Mietwagen- und Taxiregeln (§ 4.4), die Bahncard-Regel, die Sitzplatzreservierung (§ 4.1), der Geltungsbereich (§ 1) und das Inkrafttreten (§ 9). Die Änderungen an Versionsnummer und Hinweistext sind rein formal.

### Nutzer 2

Ich fahre mit dem eigenen Auto zu einem Kunden: 180 km hin und 180 km zurück.
Ich übernachte einmal im Hotel, die Rechnung beträgt 125 Euro ohne Frühstück.
Was bekomme ich für Fahrt und Übernachtung nach v1 erstattet, was nach v2?
Rechne Schritt für Schritt und nenne zu jeder Zahl den Abschnitt der Richtlinie.
Nutze nur Angaben aus den beiden Fassungen.

### Assistent 2

Voraussetzung für beides ist in beiden Fassungen eine vorherige Genehmigung (§ 3). Ohne sie besteht kein Erstattungsanspruch.

**Fahrt mit dem Privatauto (§ 4.3)**
- Strecke: 180 km + 180 km = 360 km
- Nach v1: 360 km × 0,30 Euro = **108,00 Euro**
- Nach v2: 360 km × 0,25 Euro = **90,00 Euro**
- Parkgebühren werden zusätzlich gegen Beleg erstattet, in beiden Fassungen.

**Übernachtung (§ 5)**
- Rechnung: 125 Euro ohne Frühstück
- Nach v1: Die Obergrenze liegt bei 110 Euro. Erstattet werden **110,00 Euro**. Die restlichen 15 Euro trägst du selbst, außer die Führungskraft genehmigt im Einzelfall eine höhere Obergrenze.
- Nach v2: Die Obergrenze liegt bei 130 Euro. Die Rechnung liegt darunter, daher werden **125,00 Euro** vollständig erstattet.

**Summe**
- Nach v1: 108,00 + 110,00 = **218,00 Euro**
- Nach v2: 90,00 + 125,00 = **215,00 Euro**

Nach v2 erhältst du für die Fahrt 18 Euro weniger, für das Hotel 15 Euro mehr. Insgesamt sind es 3 Euro weniger als nach v1.

### Nutzer 3

Und was bekomme ich für die Verpflegung erstattet?

### Assistent 3

Die Verpflegung ist in beiden Fassungen gleich geregelt (§ 6). Es werden die jeweils aktuellen steuerlichen Verpflegungspauschalen erstattet. Die Fassungen nennen keinen Eurobetrag. Deshalb kann ich dir keine konkrete Summe nennen, und ich würde dir keine Zahl aus meinem Wissen nennen, da die Pauschalen sich ändern.

Wichtig zu wissen:
- Werden Mahlzeiten vom Unternehmen, vom Kunden oder vom Hotel gestellt, wird die Pauschale gekürzt. In deinem Beispiel ist nur angegeben, dass das Frühstück nicht enthalten ist. Eine Kürzung ergibt sich daraus also nicht.
- Bewirtungen von Geschäftspartnern musst du vorher mit deiner Führungskraft abstimmen und mit Bewirtungsbeleg abrechnen. Sie fallen nicht unter die Verpflegungspauschale.

Bitte frag bei der Buchhaltung oder Personalabteilung nach der aktuellen Pauschale, wenn du die genaue Summe brauchst.

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1

Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?

### Assistent 1

Ich habe beide Fassungen abschnittsweise verglichen und sieben inhaltliche Änderungen gefunden:

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung bei hohen Reisekosten (Abschnitt 3) | Bei voraussichtlichen Kosten über 2.000 Euro ist zusätzlich die Freigabe der **Abteilungsleitung** nötig. | Bei voraussichtlichen Kosten über 2.000 Euro ist zusätzlich die Freigabe der **Geschäftsführung** nötig. | Teure Reisen brauchen jetzt eine höhere Freigabestufe. Plant dafür mehr Vorlauf ein. |
| 2 | Bahn: 1. Klasse (Abschnitt 4.1) | 1. Klasse erlaubt bei einfacher Fahrtdauer von mehr als **vier** Stunden. | 1. Klasse erlaubt bei einfacher Fahrtdauer von mehr als **drei** Stunden. | Die 1. Klasse ist schon bei kürzeren Fahrten erlaubt. Das ist eine Erleichterung. |
| 3 | Inlandsflüge (Abschnitt 4.2) | Keine besondere Einschränkung für Inlandsflüge, nur Economy Class und Buchung über die Reisestelle. | Inlandsflüge sind nur zulässig, wenn die einfache Bahnfahrt **länger als fünf Stunden** dauern würde. | Innerhalb Deutschlands wird meist die Bahn gebucht. Ein Flug ist nur bei sehr langen Bahnstrecken möglich. |
| 4 | Kilometerpauschale, privater Pkw (Abschnitt 4.3) | **0,30 Euro** je Kilometer. | **0,25 Euro** je Kilometer. | Fahrten mit dem eigenen Auto werden geringer erstattet. Pro 100 km sind das 5 Euro weniger. |
| 5 | Hotel-Obergrenze (Abschnitt 5) | Bis **110 Euro** pro Nacht (ohne Frühstück). | Bis **130 Euro** pro Nacht (ohne Frühstück). | Mehr Spielraum bei der Hotelwahl. Die Ausnahme durch die Führungskraft für teure Städte und Messen bleibt. |
| 6 | Trinkgelder (Abschnitt 7) | Trinkgelder können bis 10 % des Rechnungsbetrags erstattet werden, wenn sie auf dem Beleg vermerkt sind. | Die Regelung ist **ersatzlos gestrichen**. Trinkgelder werden in v2 nicht mehr erwähnt. | Rechnet nicht mehr mit einer Erstattung von Trinkgeld. Im Zweifel bei der Buchhaltung nachfragen. |
| 7 | Abrechnungsfrist (Abschnitt 8) | Einreichung innerhalb von **drei Monaten** nach Reiseende. | Einreichung innerhalb von **sechs Wochen** nach Reiseende. | Die Frist ist deutlich kürzer. Reicht die Abrechnung zeitnah ein, sonst droht die Ablehnung. |

Unverändert sind u. a. Geltungsbereich, Grundsätze, Mietwagen und Taxi, Verpflegung und Inkrafttreten. Bei Punkt 6 ist es eine Auslegungsfrage, ob v2 Trinkgeld ausschließt. Der Text verbietet es nicht ausdrücklich, regelt es aber auch nicht mehr.

### Nutzer 2

Ich fahre mit dem eigenen Auto zu einem Kunden: 180 km hin und 180 km zurück.
Ich übernachte einmal im Hotel, die Rechnung beträgt 125 Euro ohne Frühstück.
Was bekomme ich für Fahrt und Übernachtung nach v1 erstattet, was nach v2?
Rechne Schritt für Schritt und nenne zu jeder Zahl den Abschnitt der Richtlinie.
Nutze nur Angaben aus den beiden Fassungen.

### Assistent 2

Voraussetzung ist, dass die Dienstreise und die Nutzung des privaten Pkw vorab genehmigt wurden (Abschnitt 3 und 4.3 in beiden Fassungen).

**Schritt 1: Gefahrene Strecke**
180 km + 180 km = **360 km** (Angabe von dir)

**Nach v1**
- Fahrt: 360 km × 0,30 Euro/km (v1, Abschnitt 4.3) = **108,00 Euro**
- Übernachtung: Die Obergrenze beträgt 110 Euro pro Nacht ohne Frühstück (v1, Abschnitt 5). Deine Rechnung über 125 Euro liegt darüber, erstattet werden also **110,00 Euro**. Die 15 Euro Differenz zahlst du selbst. Eine höhere Obergrenze wäre nur im Einzelfall durch die Führungskraft möglich (v1, Abschnitt 5).
- **Summe v1: 108,00 + 110,00 = 218,00 Euro**

**Nach v2**
- Fahrt: 360 km × 0,25 Euro/km (v2, Abschnitt 4.3) = **90,00 Euro**
- Übernachtung: Die Obergrenze beträgt 130 Euro pro Nacht ohne Frühstück (v2, Abschnitt 5). Die 125 Euro liegen darunter, erstattet werden also die vollen **125,00 Euro** gegen Hotelrechnung.
- **Summe v2: 90,00 + 125,00 = 215,00 Euro**

| | v1 | v2 |
|---|---|---|
| Fahrt (4.3) | 108,00 € | 90,00 € |
| Übernachtung (5) | 110,00 € | 125,00 € |
| **Gesamt** | **218,00 €** | **215,00 €** |

Nach v2 bekommst du für diese Reise 3 Euro weniger. Die Fahrt wird 18 Euro schlechter erstattet, die Übernachtung dafür 15 Euro besser. Eventuelle Parkgebühren kämen dazu und würden in beiden Fassungen gegen Beleg erstattet (Abschnitt 4.3).

### Nutzer 3

Und was bekomme ich für die Verpflegung erstattet?

### Assistent 3

Dazu kann ich dir keinen Euro-Betrag nennen. Abschnitt 6 ist in v1 und v2 wortgleich und enthält selbst keine Zahlen:

- Für Verpflegungsmehraufwendungen gelten "die jeweils aktuellen steuerlichen Pauschalen". Die Höhe steht nicht in der Richtlinie, und die Pauschalen sind abhängig von der Abwesenheitsdauer. Du müsstest sie also extern nachschlagen, etwa bei der Personal- oder Buchhaltungsabteilung. Aus den beiden Fassungen allein kann ich sie nicht ableiten, und ich will keine Beträge raten.
- Werden Mahlzeiten vom Unternehmen, vom Kunden oder vom Hotel gestellt, wird die Pauschale entsprechend gekürzt.
- Dein Hotel war ohne Frühstück gebucht. Von dort käme also keine Kürzung. Wenn dich der Kunde verpflegt, schon.
- Bewirtungen von Geschäftspartnern müssen vorher mit der Führungskraft abgestimmt und mit Bewirtungsbeleg abgerechnet werden (Abschnitt 6).

Zwischen v1 und v2 gibt es bei der Verpflegung keinen Unterschied. Die Frage hat also für beide Fassungen dieselbe Antwort.

Für eine konkrete Zahl bräuchte ich die Abwesenheitsdauer (An- und Abreisezeiten, Anzahl der Tage) und die Information, ob Mahlzeiten gestellt wurden. Außerdem brauchst du den aktuellen Pauschalbetrag, den du bei der Personalabteilung erfragen kannst.

---

## Gesprächsprotokoll: Opus

### Nutzer 1

Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?

### Assistent 1

Ich habe die beiden Fassungen Abschnitt für Abschnitt verglichen. Es gibt **7 inhaltliche Änderungen**:

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung bei Reisen über 2.000 € (Abschnitt 3) | Neben der Führungskraft muss auch die **Abteilungsleitung** zustimmen. | Neben der Führungskraft muss auch die **Geschäftsführung** zustimmen. | Teure Reisen müssen von einer höheren Ebene freigegeben werden. Das kann länger dauern, also früher beantragen. |
| 2 | 1. Klasse bei der Bahn (Abschnitt 4.1) | Erlaubt ab einer einfachen Fahrtdauer von **mehr als vier Stunden**. | Erlaubt ab einer einfachen Fahrtdauer von **mehr als drei Stunden**. | Verbesserung: Die 1. Klasse ist jetzt schon bei kürzeren Fahrten erlaubt. |
| 3 | Inlandsflüge (Abschnitt 4.2) | Keine Einschränkung. Es gilt nur: Economy Class, Buchung über die Reisestelle. | **Neu:** Inlandsflüge sind nur erlaubt, wenn die einfache Bahnfahrt **länger als fünf Stunden** dauern würde. | Einschränkung: Bei vielen Strecken innerhalb Deutschlands muss man jetzt die Bahn nehmen. Vor einer Flugbuchung die Bahnfahrzeit prüfen. |
| 4 | Kilometerpauschale für das eigene Auto (Abschnitt 4.3) | **0,30 €** je gefahrenem Kilometer | **0,25 €** je gefahrenem Kilometer | Verschlechterung: 5 Cent weniger pro Kilometer, also z. B. 25 € weniger auf 500 km. |
| 5 | Höchstbetrag für die Übernachtung (Abschnitt 5) | bis **110 €** pro Nacht (ohne Frühstück) | bis **130 €** pro Nacht (ohne Frühstück) | Verbesserung: Teurere Hotels werden ohne Sondergenehmigung erstattet. Die Ausnahme für teure Städte und Messen bleibt bestehen. |
| 6 | Trinkgelder (Abschnitt 7) | Werden bis **10 % des Rechnungsbetrags** erstattet, wenn sie auf dem Beleg stehen. | Die Regel ist **gestrichen**. Trinkgelder werden nicht mehr erwähnt. | Verschlechterung: Trinkgelder sind nicht mehr ausdrücklich erstattungsfähig. Man sollte damit rechnen, sie selbst zu zahlen, oder bei der Personalabteilung nachfragen. |
| 7 | Frist für die Abrechnung (Abschnitt 8) | innerhalb von **drei Monaten** nach Reiseende | innerhalb von **sechs Wochen** nach Reiseende | Die Frist ist ungefähr halb so lang. Verspätete Abrechnungen können weiterhin abgelehnt werden, also zügig einreichen. |

**Ohne inhaltliche Änderung** sind diese Abschnitte: 1 (Geltungsbereich), 2 (Grundsätze), 4.4 (Mietwagen und Taxi), 6 (Verpflegung) und 9 (Inkrafttreten). Auch die übrigen Sätze in den geänderten Abschnitten sind gleich geblieben.

### Nutzer 2

Ich fahre mit dem eigenen Auto zu einem Kunden: 180 km hin und 180 km zurück.
Ich übernachte einmal im Hotel, die Rechnung beträgt 125 Euro ohne Frühstück.
Was bekomme ich für Fahrt und Übernachtung nach v1 erstattet, was nach v2?
Rechne Schritt für Schritt und nenne zu jeder Zahl den Abschnitt der Richtlinie.
Nutze nur Angaben aus den beiden Fassungen.

### Assistent 2

**Schritt 1: Gefahrene Kilometer**
180 km hin + 180 km zurück = **360 km**. Abschnitt 4.3 zahlt „je gefahrenem Kilometer“, deshalb zählen beide Strecken.

**Schritt 2: Fahrtkosten (Abschnitt 4.3)**
- v1: 360 km × 0,30 € = **108,00 €**
- v2: 360 km × 0,25 € = **90,00 €**

**Schritt 3: Übernachtung (Abschnitt 5)**
- v1: Die Obergrenze liegt bei 110 € pro Nacht. Die Rechnung über 125 € liegt darüber. Erstattet werden deshalb **110,00 €**, und 15 € zahlst du selbst.
- v2: Die Obergrenze liegt bei 130 € pro Nacht. Die 125 € liegen darunter, also werden **125,00 €** voll erstattet.

**Schritt 4: Summe**

| | v1 | v2 |
|---|---|---|
| Fahrt (Abschnitt 4.3) | 108,00 € | 90,00 € |
| Übernachtung (Abschnitt 5) | 110,00 € | 125,00 € |
| **Gesamt** | **218,00 €** | **215,00 €** |

Nach v2 bekommst du also **3 € weniger** als nach v1. Du verlierst 18 € bei der Fahrt und bekommst 15 € mehr für das Hotel.

**Voraussetzungen und Hinweise:**
- Die Reise muss vorher genehmigt sein (Abschnitt 3). Die Fahrt mit dem eigenen Auto muss ebenfalls genehmigt sein (Abschnitt 4.3). Ohne Genehmigung gibt es keine Erstattung.
- Für das Hotel brauchst du die Rechnung (Abschnitt 5).
- Nach v1 kann deine Führungskraft im Einzelfall eine höhere Obergrenze genehmigen, etwa in einer teuren Stadt oder während einer Messe (Abschnitt 5). Dann würden auch dort die vollen 125 € erstattet.
- Parkgebühren kommen gegen Beleg in beiden Fassungen hinzu (Abschnitt 4.3). Ich habe sie nicht eingerechnet, weil du keine genannt hast.
- Die Verpflegung ist hier nicht enthalten.

### Nutzer 3

Und was bekomme ich für die Verpflegung erstattet?

### Assistent 3

**Was die Richtlinie sagt:** Abschnitt 6 ist in v1 und v2 gleich. Es gelten „die jeweils aktuellen steuerlichen Pauschalen“. Werden Mahlzeiten gestellt, wird die Pauschale gekürzt. **Konkrete Beträge stehen in keiner der beiden Fassungen.** Aus den Dokumenten allein kann ich dir also keine Zahl nennen. Für die Verpflegung ändert sich zwischen v1 und v2 nichts.

**Einordnung aus allgemeinem Wissen (nicht aus der Richtlinie):** Nach meinem Kenntnisstand gelten in Deutschland diese Pauschalen für Inlandsreisen:
- **14 €** für den Anreisetag und **14 €** für den Abreisetag, wenn du dazwischen auswärts übernachtest
- 28 € für einen vollen Kalendertag mit 24 Stunden Abwesenheit. Das betrifft dich bei einer Nacht nicht.

Bei deiner Reise mit einer Übernachtung wären das wahrscheinlich **14 € + 14 € = 28 €**.

**Kürzungen:** Laut Abschnitt 6 wird die Pauschale gekürzt, wenn Mahlzeiten gestellt werden. Deine Hotelrechnung ist ohne Frühstück, also entfällt dort eine Kürzung. Lädt dich der Kunde aber zum Beispiel zum Mittagessen ein, wird gekürzt. Üblich sind 20 % der vollen Tagespauschale für ein Frühstück und 40 % für ein Mittag- oder Abendessen, also 5,60 € bzw. 11,20 €.

**Wichtig:**
- Die Beträge können sich ändern. Ich kann nicht prüfen, ob sie für dieses Jahr noch stimmen. Bitte lass dir die aktuellen Werte von der Buchhaltung oder Personalabteilung bestätigen. Laut Abschnitt 9 ist die Personalabteilung für Fragen zur Richtlinie zuständig.
- Das ist keine steuerliche Beratung.

**Gesamtbild (vorbehaltlich der Verpflegung):**
- v1: 218 € + ca. 28 € = ca. **246 €**
- v2: 215 € + ca. 28 € = ca. **243 €**
