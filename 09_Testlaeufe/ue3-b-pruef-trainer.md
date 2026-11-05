# Testlauf: Übung 3 / Station B Trainer-Prüfprompt – Abschnitt für Abschnitt klassifizieren

**Herkunft:** Zusätzlicher Musterprompt aus [Trainer-Loesungshinweise.md – Station B](../06_Uebungen/Trainer-Loesungshinweise.md#station-b-reisekostenrichtlinie-v1-vs-v2) (Abschnitt „Musterprompts“). Er steht **nicht** im [Übungsblatt](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#station-b-zwei-versionen-einer-richtlinie-vergleichen). Dort gibt es unter „Weiter“ nur den Prompt „Prüfe deine Tabelle noch einmal Abschnitt für Abschnitt …“. Getestet als zweite Nachricht im selben Chat, nach dem Basis-Prompt. Material: [richtlinie_reisekosten_v1.md](../07_Beispielmaterial/richtlinie_reisekosten_v1.md) und [richtlinie_reisekosten_v2.md](../07_Beispielmaterial/richtlinie_reisekosten_v2.md).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt (2. Nachricht, nach dem Basis-Prompt von Station B):**

```text
Gehe beide Fassungen Abschnitt für Abschnitt durch. Gib für jeden Abschnitt an:
"unverändert", "nur Formulierung geändert" oder "inhaltlich geändert" – mit kurzer Begründung.
```

**Was laut Material herauskommen soll:** Eine vollständige Einstufung aller Abschnitte. Inhaltlich geändert: **3, 4.1, 4.2, 4.3, 5, 7, 8**. Unverändert: **1, 2, 4.4, 6, 9** (auch Bahncard, Parkgebühren, digitale Belege). Der Kopf mit der Versionsnummer darf höchstens als „nur Formulierung/redaktionell“ eingestuft werden.

**Gegenprobe (Textvergleich mit `diff`):** Die Dateien unterscheiden sich in genau 8 Zeilen: Kopfzeile 4 (Version) und je ein Absatz in 3, 4.1, 4.2, 4.3, 5, 7 und 8. Alle anderen Zeilen sind gleich. Ein Abschnitt, in dem sich **nur** die Formulierung ändert, kommt in diesem Material nicht vor.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Basis-Tabelle: alle 7 Änderungen gefunden? | **ja, 7/7** | **ja, 7/7** | **ja, 7/7** |
| Alt und neu richtig zugeordnet, Zahlen richtig? | ja | ja | ja |
| Versionsnummer **nicht** als Änderung gezählt? | ja | ja (ausdrücklich erwähnt) | ja (ausdrücklich erwähnt) |
| Abschnittsliste: 3, 4.1, 4.2, 4.3, 5, 7, 8 „inhaltlich geändert“ | ja | ja | ja |
| Abschnittsliste: 1, 2, 4.4, 6, 9 „unverändert“ | ja | ja | ja |
| Einstufung Kopf/Version | „unverändert“, Begründung nennt aber die geänderte Versionsnummer (widersprüchlich, harmlos) | „nur Formulierung geändert“ (sauber) | „unverändert (bis auf die Versionsnummer)“ (sauber erklärt) |
| Zusätzliche/fragwürdige Zeilen | Überschrift „4. Verkehrsmittel“ als eigene Zeile „inhaltlich geändert“ (die Überschrift selbst hat keinen Text, s. u.) | keine | keine |
| Unveränderte Details in geänderten Abschnitten genannt (Parkgebühren, digitale Belege usw.) | nein | **ja** (Parkgebühren, Haftung, digitale Belege, Vorschüsse, Ausnahmeregel Hotel) | **ja** (Parkgebühren, Haftung, Ausnahmen Hotel) |
| Zählfehler / Eigenkorrektur | – | **ja**: „7 von 13 … unverändert“, danach selbst auf 6 von 13 korrigiert | – |
| Nicht belegte Aussagen | keine | keine | kleine Verallgemeinerungen in der Basis-Tabelle (s. u.) |
| Gesamturteil | gut, eine überflüssige Zeile | sehr gut, aber sichtbarer Zählfehler | sehr gut, mit hilfreichem Hinweis, dass „nur Formulierung“ hier nirgends vorkommt |

---

## Gefundene Fehler mit Beleg

**Kein Modell hat eine Änderung übersehen, erfunden oder alt und neu vertauscht.** Alle Zahlen stimmen mit den Quellen überein (geprüft per `diff`). Die Beispielrechnungen stimmen ebenfalls (per `python3`): Sonnet „200 km → 10 Euro weniger“ (200 × 0,05 € = 10,00 €), Opus „400 km: 100 € statt 120 €“ (400 × 0,25 € = 100 €, 400 × 0,30 € = 120 €), Opus „Frist ungefähr halb so lang“ (6 Wochen gegenüber ca. 13 Wochen = 46 %).

Kleinere Punkte:

1. **Haiku – Kopfzeile widersprüchlich:** Einstufung „unverändert“, die Begründung sagt aber „Nur die Versionsnummer wurde von 1 auf 2 geändert“. Laut Quelle (Zeile 4: „Version 1“ → „Version 2“) wäre „nur Formulierung/redaktionell geändert“ genauer. Nach den Lösungshinweisen ist das zulässig, weil die Version nicht als inhaltliche Änderung gezählt wird.
2. **Haiku – Zeile „4. Verkehrsmittel (Überschrift)“ als „inhaltlich geändert“:** Unter der Überschrift `## 4. Verkehrsmittel` steht in beiden Fassungen kein eigener Text. Haiku stuft hier eigentlich die Unterabschnitte zusammen ein. Das ist kein Sachfehler, aber eine doppelte Zählung. Wer die Zeilen mit „inhaltlich geändert“ zählt, kommt bei Haiku auf **8**.
3. **Sonnet – Zählfehler in der Zusammenfassung:** „Ergebnis: 7 von 13 Einträgen sind unverändert oder nur formal geändert (Kopf, Abschnitte 1, 2, 4.4, 6, 9)“. In der Klammer stehen 6 Einträge. Sonnet korrigiert das im nächsten Absatz selbst („richtig ist 6 von 13“). Die Tabelle selbst ist richtig.
4. **Opus – Verallgemeinerungen in der Basis-Tabelle (Nachricht 1):**
   - „Bei Inlandsreisen ist meistens die Bahn Pflicht.“ Das Wort „meistens“ steht nicht in der Quelle. Die Richtlinie sagt nur, dass Inlandsflüge erst bei mehr als fünf Stunden Bahnfahrt zulässig sind. Wie oft das zutrifft, ist eine Annahme.
   - „Teurere Hotels werden jetzt ohne Sondergenehmigung erstattet.“ Das gilt nur bis 130 €, nicht für beliebig teure Hotels.
5. **Haiku/Sonnet/Opus – Trinkgeld:** Alle sagen richtig, dass die Regel gestrichen ist, und raten zur Nachfrage. Sonnet weist zusätzlich korrekt darauf hin, dass v2 Trinkgeld **nicht ausdrücklich ausschließt**. Das ist die genaueste Lesart.

---

## Lehren für die Auswertung

- **Der Prüfprompt bestätigt hier nur, er deckt nichts auf.** Alle drei Modelle hatten schon mit dem Basis-Prompt 7/7 Änderungen. Der in den Lösungshinweisen beschriebene Stolperstein („findet nur 4–5 von 7“) trat in diesem Test nicht auf. Der Prompt ist trotzdem nützlich als Gegenkontrolle mit anderem Blickwinkel: Er zwingt dazu, auch die **unveränderten** Abschnitte ausdrücklich zu nennen. Fehlt in dieser Liste ein Abschnitt, ist das ein Warnzeichen.
- **Selbst zählen bleibt Pflicht.** Sonnet macht einen Zählfehler in der eigenen Zusammenfassung und korrigiert ihn. Haiku fügt eine Überschrift als zusätzliche Zeile ein, damit stimmt die Anzahl „inhaltlich geändert“ nicht mehr (8 statt 7). Gute Frage an die Gruppe: „Zählt nach, wie viele Zeilen ‚inhaltlich geändert‘ eure Tabelle hat – und stimmt das mit der ersten Tabelle überein?“
- **Die Kategorie „nur Formulierung geändert“ kommt im Material nicht vor.** Opus sagt das ausdrücklich. Das ist eine gute Lehre: Ein KI-Assistent muss nicht jede angebotene Kategorie benutzen. Gleichzeitig kann man die Kategorie mit dem Material nicht üben (siehe Hinweise zum Material).
- **Versionsnummer:** Alle drei haben sie richtig **nicht** als inhaltliche Änderung gezählt. Der Stolperstein „meldet 8 Änderungen wegen der Version“ trat nicht auf. Die Einstufung des Kopfes schwankt aber („unverändert“ / „nur Formulierung“ / „unverändert bis auf Versionsnummer“). Alle drei Varianten sind vertretbar.
- **Hinsehen bei den Erklärungen, nicht nur bei der Tabelle:** Die Fehler stecken in der Spalte „Was bedeutet das für Mitarbeitende?“ (Opus: „meistens“, „teurere Hotels“). Das sind Deutungen, keine Regeln aus dem Dokument.
- **Modellunterschiede klein:** Bei sauber getrenntem, kurzem Material liefern alle drei Modelle fast dieselbe Liste. Unterschiede zeigen sich bei der Gründlichkeit der Begründungen (Sonnet/Opus nennen auch unveränderte Teilregeln) und bei Formfehlern (Haiku: Überschrift-Zeile, Sonnet: Zählfehler).

---

## Hinweise zum Material

- Der Prüfprompt steht nur in den Lösungshinweisen, nicht im Übungsblatt. Wenn Teilnehmende ihn nutzen sollen, müsste er ins Übungsblatt (z. B. unter „Weiter“).
- Die Lösungshinweise warnen vor „verschobenen Abschnitten“ und Formulierungsänderungen. Beides kommt in v1/v2 nicht vor. Die Kategorie „nur Formulierung geändert“ kann deshalb nicht geübt werden. Vorschlag: In v2 eine reine Umformulierung ohne neue Regel einbauen (z. B. in Abschnitt 6: „Verpflegungsmehraufwendungen werden … erstattet“ umformulieren), damit der Prompt etwas zu unterscheiden hat. Dann müssten die Lösungshinweise und die Zählung (7 inhaltlich + Version + 1 Umformulierung) angepasst werden.
- Der Stolperstein „findet nur 4–5 von 7 Änderungen“ ließ sich mit Haiku, Sonnet und Opus nicht nachstellen. Formulierung abschwächen, z. B. „kann einzelne Änderungen übersehen – vor allem neue oder gestrichene Sätze (Nr. 3 und Nr. 6)“.

---

## Gesprächsprotokoll: Haiku

### Nutzer 1
Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?

### Assistent 1
Hier sind alle inhaltlichen Änderungen zwischen v1 und v2:

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung bei hohen Kosten (Abschnitt 3) | Bei Reisen über 2.000 Euro ist zusätzlich die Freigabe durch die **Abteilungsleitung** nötig. | Bei Reisen über 2.000 Euro ist zusätzlich die Freigabe durch die **Geschäftsführung** nötig. | Teure Reisen brauchen eine höhere Freigabeebene. Die Genehmigung dauert unter Umständen länger. |
| 2 | Bahn: 1. Klasse (Abschnitt 4.1) | Die 1. Klasse darf gebucht werden, wenn die einfache Fahrtdauer **mehr als vier Stunden** beträgt. | Die 1. Klasse darf gebucht werden, wenn die einfache Fahrtdauer **mehr als drei Stunden** beträgt. | Die 1. Klasse ist schon bei kürzeren Bahnfahrten erlaubt. |
| 3 | Inlandsflüge (Abschnitt 4.2) | Keine besondere Regel zu Inlandsflügen. Flüge sind in der Economy Class zu buchen. | Inlandsflüge sind **nur zulässig, wenn die einfache Bahnfahrt länger als fünf Stunden dauern würde**. | Für Inlandsstrecken muss man vorher prüfen, ob die Bahn mehr als fünf Stunden braucht. Sonst ist kein Flug erlaubt. |
| 4 | Kilometerpauschale Privatauto (Abschnitt 4.3) | 0,30 Euro je gefahrenem Kilometer. | 0,25 Euro je gefahrenem Kilometer. | Wer mit dem eigenen Auto dienstlich fährt, bekommt pro Kilometer 5 Cent weniger. |
| 5 | Hotel-Obergrenze (Abschnitt 5) | Erstattung bis 110 Euro pro Nacht (ohne Frühstück). | Erstattung bis 130 Euro pro Nacht (ohne Frühstück). | Hotelkosten werden bis 20 Euro mehr pro Nacht erstattet. |
| 6 | Trinkgeld (Abschnitt 7) | Trinkgelder können bis 10 % des Rechnungsbetrags erstattet werden, wenn sie auf dem Beleg vermerkt sind. | Die Regelung zu Trinkgeld ist gestrichen. | Trinkgeld ist nicht mehr ausdrücklich erstattungsfähig. Im Zweifel bei der Personalabteilung nachfragen, bevor Trinkgeld abgerechnet wird. |
| 7 | Abrechnungsfrist (Abschnitt 8) | Abrechnung innerhalb von **drei Monaten** nach Ende der Dienstreise. | Abrechnung innerhalb von **sechs Wochen** nach Ende der Dienstreise. | Die Frist ist deutlich kürzer. Belege sollten zeitnah eingereicht werden. |

### Nutzer 2
Gehe beide Fassungen Abschnitt für Abschnitt durch. Gib für jeden Abschnitt an:
"unverändert", "nur Formulierung geändert" oder "inhaltlich geändert" – mit kurzer Begründung.

### Assistent 2
Abschnitt für Abschnitt im Vergleich v1 zu v2:

| Abschnitt | Einstufung | Begründung |
|---|---|---|
| Kopfzeile (Version) | unverändert | Nur die Versionsnummer wurde von 1 auf 2 geändert. Das ist keine inhaltliche Regel. |
| 1. Geltungsbereich | unverändert | Der Text ist identisch. |
| 2. Grundsätze | unverändert | Der Text ist identisch. |
| 3. Genehmigung | inhaltlich geändert | Die zusätzliche Freigabe bei Kosten über 2.000 Euro liegt jetzt bei der Geschäftsführung statt bei der Abteilungsleitung. |
| 4. Verkehrsmittel (Überschrift) | inhaltlich geändert | Die Unterabschnitte 4.1, 4.2 und 4.3 enthalten inhaltliche Änderungen. 4.4 ist unverändert. |
| 4.1 Bahn | inhaltlich geändert | Die 1. Klasse ist ab einer Fahrtdauer von mehr als drei statt vier Stunden erlaubt. |
| 4.2 Flugzeug | inhaltlich geändert | Neu ist die Regel, dass Inlandsflüge nur zulässig sind, wenn die Bahnfahrt länger als fünf Stunden dauert. |
| 4.3 Privates Fahrzeug | inhaltlich geändert | Die Kilometerpauschale sinkt von 0,30 auf 0,25 Euro. |
| 4.4 Mietwagen und Taxi | unverändert | Der Text ist identisch. |
| 5. Übernachtung | inhaltlich geändert | Die Obergrenze steigt von 110 auf 130 Euro pro Nacht. |
| 6. Verpflegung | unverändert | Der Text ist identisch. |
| 7. Sonstige Kosten | inhaltlich geändert | Der Absatz zur Erstattung von Trinkgeld bis 10 % ist entfallen. Die übrigen Sätze sind gleich. |
| 8. Abrechnung | inhaltlich geändert | Die Abrechnungsfrist wird von drei Monaten auf sechs Wochen verkürzt. |
| 9. Inkrafttreten | unverändert | Der Text ist identisch. |

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1
Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?

### Assistent 1
Ich habe beide Fassungen verglichen und sieben inhaltliche Änderungen gefunden. Die Versionsnummer im Kopf (Version 1 zu Version 2) habe ich nicht aufgeführt, weil sie nur die Fassung kennzeichnet.

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung (Abschn. 3): Zusatzfreigabe bei hohen Kosten | Bei voraussichtlichen Kosten über 2.000 Euro muss zusätzlich die **Abteilungsleitung** freigeben. | Bei voraussichtlichen Kosten über 2.000 Euro muss zusätzlich die **Geschäftsführung** freigeben. | Teure Reisen brauchen jetzt die Freigabe der Geschäftsführung statt der Abteilungsleitung. Der Genehmigungsweg ist länger und kann mehr Vorlauf erfordern. Die Schwelle von 2.000 Euro bleibt gleich. |
| 2 | Bahn (Abschn. 4.1): 1. Klasse | 1. Klasse ist erlaubt bei einfacher Fahrtdauer von mehr als **vier Stunden**. | 1. Klasse ist erlaubt bei einfacher Fahrtdauer von mehr als **drei Stunden**. | Die 1. Klasse ist jetzt schon bei kürzeren Fahrten erlaubt. Das ist eine Verbesserung für Fahrten zwischen 3 und 4 Stunden. |
| 3 | Flugzeug (Abschn. 4.2): Inlandsflüge | Keine Einschränkung für Inlandsflüge. Vorgabe war nur Economy Class und Buchung über die Reisestelle. | Inlandsflüge sind nur zulässig, wenn die einfache Bahnfahrt **länger als fünf Stunden** dauern würde. | Für Inlandsziele mit einer Bahnfahrt bis fünf Stunden ist ein Flug nicht mehr erlaubt, dort muss die Bahn genommen werden. Vor der Buchung die Bahnfahrzeit prüfen. |
| 4 | Privates Fahrzeug (Abschn. 4.3): Kilometerpauschale | **0,30 Euro** je gefahrenem Kilometer. | **0,25 Euro** je gefahrenem Kilometer. | Es gibt weniger Geld pro Kilometer. Bei 200 km sind das 10 Euro weniger. Das gilt für alle Fahrten mit dem Privatwagen. |
| 5 | Übernachtung (Abschn. 5): Obergrenze pro Nacht | Bis **110 Euro** pro Nacht (ohne Frühstück). | Bis **130 Euro** pro Nacht (ohne Frühstück). | Das Hotelbudget ist 20 Euro pro Nacht höher. Die Ausnahmeregelung durch die Führungskraft für teure Städte und Messen bleibt unverändert. |
| 6 | Sonstige Kosten (Abschn. 7): Trinkgeld | Trinkgelder können bis **10 % des Rechnungsbetrags** erstattet werden, wenn sie auf dem Beleg vermerkt sind. | Die Trinkgeldregelung ist **ersatzlos entfallen**. Genannt werden nur noch Nebenkosten gegen Beleg und der Ausschluss privater Kosten. | Trinkgelder werden voraussichtlich nicht mehr erstattet. Das sollte man bei Unklarheit mit Personal oder Finanzen bestätigen, da die Richtlinie sie nicht ausdrücklich ausschließt. Sie nennt Trinkgeld aber auch nicht mehr als erstattungsfähig. |
| 7 | Abrechnung (Abschn. 8): Frist | Einreichung innerhalb von **drei Monaten** nach Ende der Dienstreise. | Einreichung innerhalb von **sechs Wochen** nach Ende der Dienstreise. | Die Frist ist deutlich kürzer. Abrechnungen sollten zeitnah erstellt werden, weil verspätete Abrechnungen abgelehnt werden können. |

Alle anderen Abschnitte (Geltungsbereich, Grundsätze, Privatfahrzeug außer Pauschale, Mietwagen und Taxi, Verpflegung, Inkrafttreten) sind inhaltlich gleich geblieben.

### Nutzer 2
Gehe beide Fassungen Abschnitt für Abschnitt durch. Gib für jeden Abschnitt an:
"unverändert", "nur Formulierung geändert" oder "inhaltlich geändert" – mit kurzer Begründung.

### Assistent 2
| Abschnitt | Einstufung | Begründung |
|---|---|---|
| Kopf / Titel | nur Formulierung geändert | Nur die Versionsangabe wechselt von "Version 1" zu "Version 2". Titel, Verantwortliche und Hinweis sind identisch. |
| 1. Geltungsbereich | unverändert | Der Text ist wörtlich identisch. |
| 2. Grundsätze | unverändert | Der Text ist wörtlich identisch. |
| 3. Genehmigung | inhaltlich geändert | Die zusätzliche Freigabe bei Kosten über 2.000 Euro liegt jetzt bei der Geschäftsführung statt bei der Abteilungsleitung. |
| 4.1 Bahn | inhaltlich geändert | Die 1. Klasse ist ab mehr als drei Stunden (vorher vier) einfacher Fahrtdauer erlaubt. |
| 4.2 Flugzeug | inhaltlich geändert | Neu ist die Einschränkung für Inlandsflüge: nur zulässig, wenn die einfache Bahnfahrt länger als fünf Stunden dauern würde. |
| 4.3 Privates Fahrzeug | inhaltlich geändert | Die Kilometerpauschale sinkt von 0,30 auf 0,25 Euro. Parkgebühren und Haftungsausschluss sind unverändert. |
| 4.4 Mietwagen und Taxi | unverändert | Der Text ist wörtlich identisch. |
| 5. Übernachtung | inhaltlich geändert | Die Obergrenze steigt von 110 auf 130 Euro pro Nacht. Ausnahmeregel und Hinweis zur frühen Buchung sind unverändert. |
| 6. Verpflegung | unverändert | Der Text ist wörtlich identisch. |
| 7. Sonstige Kosten | inhaltlich geändert | Der Satz zur Trinkgeld-Erstattung (bis 10 % des Rechnungsbetrags) ist in v2 gestrichen. Die übrigen Regeln sind gleich. |
| 8. Abrechnung | inhaltlich geändert | Die Einreichungsfrist verkürzt sich von drei Monaten auf sechs Wochen. Belegpflicht, digitale Belege, Ablehnung und Vorschussverrechnung sind unverändert. |
| 9. Inkrafttreten | unverändert | Der Text ist wörtlich identisch. |

Ergebnis: 7 von 13 Einträgen sind unverändert oder nur formal geändert (Kopf, Abschnitte 1, 2, 4.4, 6, 9). Inhaltlich geändert sind 7 Abschnitte (3, 4.1, 4.2, 4.3, 5, 7, 8).

Hinweis zu meiner Zählung: Das sind 6 unveränderte bzw. formal geänderte Einträge und 7 inhaltlich geänderte, zusammen 13. Die Zahl "7 von 13" im ersten Satz war ungenau, richtig ist 6 von 13.

---

## Gesprächsprotokoll: Opus

### Nutzer 1
Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?

### Assistent 1
Ich habe beide Fassungen vollständig verglichen. Es gibt **7 inhaltliche Änderungen**. Bei den Formulierungen hat sich sonst nichts geändert. Alle übrigen Passagen sind Wort für Wort gleich.

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung bei Reisen über 2.000 € (Abschnitt 3) | Zusätzliche Freigabe durch die **Abteilungsleitung** | Zusätzliche Freigabe durch die **Geschäftsführung** | Teure Reisen müssen auf einer höheren Ebene freigegeben werden. Das dauert wahrscheinlich länger, deshalb sollten Sie früher planen und den Antrag früher stellen. |
| 2 | 1. Klasse Bahn (Abschnitt 4.1) | 1. Klasse erlaubt ab einer einfachen Fahrtdauer von **mehr als vier Stunden** | 1. Klasse erlaubt ab einer einfachen Fahrtdauer von **mehr als drei Stunden** | Das ist eine Verbesserung. Sie dürfen jetzt schon bei kürzeren Strecken 1. Klasse fahren. |
| 3 | Inlandsflüge (Abschnitt 4.2) | Keine Einschränkung für Inlandsflüge geregelt | Inlandsflüge **nur zulässig, wenn die einfache Bahnfahrt länger als fünf Stunden** dauern würde | Das ist eine neue Einschränkung. Bei Inlandsreisen ist meistens die Bahn Pflicht. Ein Flug ist nur noch erlaubt, wenn die Bahnfahrt mehr als 5 Stunden dauern würde. |
| 4 | Kilometerpauschale privater Pkw (Abschnitt 4.3) | **0,30 €** je km | **0,25 €** je km | Sie bekommen weniger erstattet. Beispiel: Für 400 km gibt es 100 € statt 120 €. |
| 5 | Hotel-Obergrenze (Abschnitt 5) | bis **110 €** pro Nacht (ohne Frühstück) | bis **130 €** pro Nacht (ohne Frühstück) | Das ist eine Verbesserung. Teurere Hotels werden jetzt ohne Sondergenehmigung erstattet. |
| 6 | Trinkgelder (Abschnitt 7) | Trinkgelder bis **10 % des Rechnungsbetrags** erstattungsfähig, wenn sie auf dem Beleg vermerkt sind | Diese Regel ist **gestrichen**. Trinkgelder werden nicht mehr erwähnt. | Es gibt keine ausdrückliche Grundlage mehr, um Trinkgelder erstatten zu lassen. Sie sollten damit rechnen, dass Trinkgelder nicht mehr erstattet werden. Im Zweifel fragen Sie bei Personal/Finanzen nach. |
| 7 | Frist für die Abrechnung (Abschnitt 8) | innerhalb von **drei Monaten** nach Reiseende | innerhalb von **sechs Wochen** nach Reiseende | Die Frist ist ungefähr halb so lang. Reichen Sie Ihre Abrechnung zügig ein, denn verspätete Abrechnungen können abgelehnt werden. |

Außerdem hat sich die Versionsangabe im Kopf von „Version 1“ zu „Version 2“ geändert. Das ist eine Verwaltungsangabe und keine inhaltliche Regeländerung.

**Kurzfazit:** Für Mitarbeitende gibt es zwei Verbesserungen (Bahn 1. Klasse, Hotel-Obergrenze). Vier Punkte sind schlechter oder strenger geworden: die Kilometerpauschale, die Trinkgelder, die kürzere Abrechnungsfrist und die Einschränkung bei Inlandsflügen. Bei teuren Reisen läuft die Genehmigung jetzt über die Geschäftsführung.

### Nutzer 2
Gehe beide Fassungen Abschnitt für Abschnitt durch. Gib für jeden Abschnitt an:
"unverändert", "nur Formulierung geändert" oder "inhaltlich geändert" – mit kurzer Begründung.

### Assistent 2
| Abschnitt | Status | Begründung |
|---|---|---|
| Kopf / Titel und Hinweis | unverändert (bis auf die Versionsnummer) | Titel, Firmenname, Zuständigkeit und Hinweistext sind gleich. Nur „Version 1“ wurde zu „Version 2“. Das ist eine Verwaltungsangabe und keine Regeländerung. |
| 1. Geltungsbereich | unverändert | Der Text ist Wort für Wort gleich. |
| 2. Grundsätze | unverändert | Der Text ist Wort für Wort gleich. |
| 3. Genehmigung | inhaltlich geändert | Reisen über 2.000 € muss jetzt die Geschäftsführung zusätzlich freigeben, vorher war es die Abteilungsleitung. |
| 4.1 Bahn | inhaltlich geändert | Die Grenze für die 1. Klasse sinkt von mehr als vier auf mehr als drei Stunden einfache Fahrtdauer. |
| 4.2 Flugzeug | inhaltlich geändert | Ein Satz ist neu: Inlandsflüge sind nur zulässig, wenn die einfache Bahnfahrt länger als fünf Stunden dauern würde. Der restliche Text ist gleich. |
| 4.3 Privates Fahrzeug | inhaltlich geändert | Die Kilometerpauschale sinkt von 0,30 € auf 0,25 € je km. Die Regeln zu Parkgebühren und Haftung sind gleich. |
| 4.4 Mietwagen und Taxi | unverändert | Der Text ist Wort für Wort gleich. |
| 5. Übernachtung | inhaltlich geändert | Die Obergrenze steigt von 110 € auf 130 € pro Nacht. Die Ausnahmen für teure Städte und Messen sowie der Hinweis auf frühe Buchung sind gleich. |
| 6. Verpflegung | unverändert | Der Text ist Wort für Wort gleich. |
| 7. Sonstige Kosten | inhaltlich geändert | Die Regel, dass Trinkgelder bis 10 % erstattet werden, ist ersatzlos gestrichen. Nebenkosten und der Ausschluss privater Kosten sind gleich. |
| 8. Abrechnung | inhaltlich geändert | Die Frist zum Einreichen verkürzt sich von drei Monaten auf sechs Wochen. Die übrigen Regeln sind gleich. |
| 9. Inkrafttreten | unverändert | Der Text ist Wort für Wort gleich. |

**Zusammenfassung:** 7 Abschnitte sind inhaltlich geändert (3, 4.1, 4.2, 4.3, 5, 7, 8). 5 Abschnitte sind unverändert (1, 2, 4.4, 6, 9). Im Kopf hat sich nur die Versionsnummer geändert. Es gibt keinen Abschnitt, in dem nur die Formulierung geändert wurde: Jede Textänderung zwischen v1 und v2 ändert auch eine Regel.
