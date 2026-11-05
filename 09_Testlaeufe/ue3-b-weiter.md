# Testlauf: Übung 3 / Station B Weiter – Nachprüfen lassen und Info-Mail

**Herkunft:** Station B, Stufe „Weiter“ aus [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#station-b-zwei-versionen-einer-richtlinie-vergleichen) (Block 5). Material: [richtlinie_reisekosten_v1.md](../07_Beispielmaterial/richtlinie_reisekosten_v1.md) und [richtlinie_reisekosten_v2.md](../07_Beispielmaterial/richtlinie_reisekosten_v2.md). Zugehörige Lösungshinweise: [Trainer-Loesungshinweise.md – Station B](../06_Uebungen/Trainer-Loesungshinweise.md#station-b-reisekostenrichtlinie-v1-vs-v2) („Die vollständige Liste der Unterschiede“, „Woran du ein gutes Ergebnis erkennst“, „Typische Stolpersteine“). Vorstufe: [ue3-b-basis.md](ue3-b-basis.md).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf (jeweils ein Chat, drei Nachrichten, beide Fassungen angehängt):**

1. Basis-Prompt (Tabelle aller inhaltlichen Änderungen)
2. Weiter, Teil 1: „Prüfe deine Tabelle noch einmal Abschnitt für Abschnitt gegen beide Fassungen. Hast du etwas übersehen? Gibt es Regeln, die in v2 neu dazugekommen oder ganz weggefallen sind?“
3. Weiter, Teil 2: „Schreib aus der Tabelle eine kurze Info-Mail an alle Mitarbeitenden (max. 150 Wörter, Ton: freundlich, sachlich, per du). Die wichtigste Änderung zuerst.“

**Was laut Material herauskommen soll:** Die Selbstprüfung ergänzt Übersehenes (vor allem die neue Inlandsflug-Regel in 4.2 und das gestrichene Trinkgeld in 7), sodass am Ende **7 inhaltliche Änderungen** in der Liste stehen (Versionsnummer zählt nicht). Die Info-Mail hat höchstens 150 Wörter, ist per du, freundlich-sachlich, nennt die wichtigste Änderung zuerst, enthält keine Regeln, die in keiner Fassung stehen, und alle Zahlen stimmen.

**Kontrolle per `diff`:** Die beiden Dateien unterscheiden sich in genau 8 Zeilen: Versionsnummer (redaktionell) plus die 7 Punkte aus den Lösungshinweisen (3, 4.1, 4.2, 4.3, 5, 7, 8). Die Liste in den Lösungshinweisen stimmt.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Turn 1: Änderungen gefunden | **7 von 7**, nichts erfunden, Versionsnummer nicht mitgezählt | **7 von 7**, nichts erfunden, Versionsnummer nur als Randnotiz | **7 von 7**, nichts erfunden |
| Turn 2: Hat die Selbstprüfung etwas ergänzt? | nein (es fehlte nichts) | nein (es fehlte nichts) | nein (es fehlte nichts) |
| Turn 2: neu dazugekommen / weggefallen korrekt benannt | ja: Inlandsflüge / Trinkgeld | ja: Inlandsflüge / Trinkgeld | ja: Inlandsflüge / Trinkgeld |
| Turn 2: Liste nach Prüfung = 7, nichts erfunden | 7, aber **Scheinbefund**: „fehlendes Inkrafttreten-Datum in v2“ soll ergänzt werden (steht in v1 genauso, keine Änderung) | 7, sauber, Abschnitt für Abschnitt | 7, sauber, als Abschnittstabelle |
| Turn 2: Hinweis, dass v2 zum Trinkgeld nur schweigt | nein („nicht mehr ausdrücklich erstattungsfähig“) | **ja**, Klärung durch Personal empfohlen | **ja**, Klärung vor Versand empfohlen |
| Turn 3: Wortzahl (per `python3`, mit Betreff / ohne) | 131 / 126 | 128 / 123 | 130 / 122 |
| Turn 3: ≤ 150 Wörter | ja | ja | ja |
| Turn 3: Du-Form | ja, aber meist passiv („müssen eingereicht werden“) | **ja, durchgängig** („musst du“, „darfst du“, „hilft dir“) | **gemischt**: „Reicht eure …“ (ihr) neben „für dich“, „findest du“ |
| Turn 3: Ton freundlich-sachlich | ja | ja | ja |
| Turn 3: wichtigste Änderung zuerst | ja, Abrechnungsfrist 6 Wochen | ja, Abrechnungsfrist 6 Wochen (als „Wichtigste Änderung“ markiert) | ja, Abrechnungsfrist 6 Wochen |
| Turn 3: alle 7 Änderungen enthalten | ja | ja | ja |
| Turn 3: alle Zahlen korrekt | ja | ja | ja |
| Turn 3: Regeln erfunden? | nein, aber **Trinkgeld überzogen**: „wird nicht mehr erstattet“ | nein | nein |
| Turn 3: Genehmigung korrekt („zusätzlich“ zur Führungskraft) | **ungenau**: „entscheidet … die Geschäftsführung“ | korrekt („zusätzlich“) | **ungenau**: „gibt jetzt die Geschäftsführung frei“ |
| Turn 3: sonstige Ungenauigkeiten | – | „Hotels **kosten** bis zu 130 Euro“ (gemeint ist die Erstattungsgrenze) | „ab 3 Stunden“ statt „mehr als drei Stunden“; „ab sofort gilt“ (v2 gilt ab Veröffentlichung im Intranet) |
| **Gesamt** | brauchbar, kleine Überinterpretationen | **beste Mail**, kleiner Formulierungsfehler | sehr gute Prüfung, Mail mit du/ihr-Mix |

---

## Gefundene Fehler mit Beleg

Keine falschen Zahlen, keine erfundenen Regeln im Sinne der Lösungshinweise. Alle Zahlen sind gegen die Quellen geprüft: 0,30 → 0,25 € (5 Cent weniger), 110 → 130 € (20 € mehr), 4 → 3 Stunden, 3 Monate → 6 Wochen, neue 5-Stunden-Grenze für Inlandsflüge, 2.000-€-Grenze unverändert. Opus' Beispiel „100 km: 25 € statt 30 €“ stimmt. Die folgenden Punkte sind kleinere Fehler und Ungenauigkeiten:

1. **Haiku, Turn 2 – Scheinbefund beim Inkrafttreten.** „Abschnitt 9 ist in beiden Fassungen gleich. In v2 steht aber kein eigenes Datum für das Inkrafttreten. … Ich würde sie nur um einen Hinweis zum fehlenden Inkrafttreten-Datum in v2 ergänzen.“ Beleg: Abschnitt 9 ist in v1 und v2 wortgleich („tritt mit ihrer Veröffentlichung im Intranet in Kraft“). Auch v1 nennt kein Datum. Das ist keine Änderung und gehört nicht in die Tabelle. Die Nachfrage „Hast du etwas übersehen?“ verleitet hier dazu, *irgendetwas* zu finden. Außerdem steht die echte Änderung Nr. 1 (Geschäftsführung) unter der Überschrift „Nicht geändert, aber auffällig“. Das ist verwirrend gegliedert.
2. **Haiku, Turn 3 – Trinkgeld überzogen.** „Trinkgeld: wird nicht mehr erstattet.“ Beleg: In v2 Abschnitt 7 fehlt der Trinkgeld-Satz einfach. Ein Verbot steht nirgends. Haiku selbst hatte in Turn 1 und 2 noch „nicht mehr ausdrücklich erstattungsfähig“ geschrieben. In der Mail wird daraus eine feste Regel. Sonnet („in der Richtlinie nicht mehr geregelt“) und Opus („Die Regel zur Erstattung gibt es nicht mehr“) bleiben näher am Text.
3. **Haiku und Opus, Turn 3 – „zusätzlich“ fehlt bei der Genehmigung.** Haiku: „entscheidet künftig die Geschäftsführung statt der Abteilungsleitung“. Opus: „Reisen über 2.000 € gibt jetzt die Geschäftsführung frei“. Beleg v2 Abschnitt 3: „Die Genehmigung erteilt die direkte Führungskraft. Bei Reisen, deren voraussichtliche Kosten 2.000 Euro übersteigen, ist **zusätzlich** die Freigabe durch die Geschäftsführung erforderlich.“ Wer nur die Mail liest, könnte denken, die Führungskraft müsse bei teuren Reisen nicht mehr gefragt werden.
4. **Opus, Turn 3 – du/ihr-Mix.** „Reicht eure Reisekosten bitte …“ steht neben „das ändert sich für dich“, „findest du“, „hilft dir“. Gefordert war „per du“. Opus merkt das am Ende selbst an. Die Mail ist trotzdem nicht einheitlich.
5. **Opus, Turn 3 – kleine Ungenauigkeiten.** „Bahn 1. Klasse ist schon ab 3 Stunden Fahrtdauer erlaubt“. Laut v2 gilt „mehr als drei Stunden“ und die „einfache Fahrtdauer“. „Ab sofort gilt Version 2“: Laut Abschnitt 9 gilt sie ab der Veröffentlichung im Intranet, ein Datum steht nicht im Text. Aus Turn 1: „nur noch halb so viel Zeit“. 6 Wochen sind rund 46 % von 3 Monaten (ca. 13 Wochen), also ungefähr die Hälfte. Das ist vertretbar, aber gerundet.
6. **Sonnet, Turn 3 – falscher Bezug.** „Hotels kosten bis zu 130 Euro pro Nacht“. Beleg v2 Abschnitt 5: Übernachtungskosten werden „bis zu einem Betrag von 130 Euro pro Nacht (ohne Frühstück) **erstattet**“. Das ist eine Erstattungsgrenze und kein Hotelpreis. „Ohne Frühstück“ fehlt in allen drei Mails.
7. **Alle, Turn 3 – „einfache“ Bahnfahrt fehlt** bei der Inlandsflug-Regel („wenn die Bahnfahrt länger als fünf Stunden dauern würde“). Das ist eine kleine Verkürzung. Hin und zurück sind zusammen schnell über 5 Stunden, dann würde die Regel falsch angewendet.
8. **Sonnet, Turn 2 – Selbstsicherheit.** „Ich habe nichts übersehen und nichts falsch wiedergegeben.“ Hier stimmt das. Eine solche Aussage ist aber keine Prüfung (siehe Lehren).

---

## Lehren für die Auswertung

- **Der gedachte Effekt tritt nicht auf.** Laut Material soll die Selbstprüfung Übersehenes ergänzen. In diesem Testlauf haben alle drei Modelle schon in Turn 1 alle 7 Änderungen gefunden, auch die schwer zu findende neue Inlandsflug-Regel und das gestrichene Trinkgeld. Turn 2 hat also nur bestätigt. Der Stolperstein „findet nur 4–5 von 7“ hat sich mit diesen Modellen und angehängten Dateien nicht gezeigt. Mit anderen Tools, mit langen eingefügten Texten oder ohne klare Trennung ALT/NEU kann es anders sein.
- **Bessere Lehre aus Turn 2: Nachfragen bringt nicht automatisch Wahrheit.** Bei Haiku sieht man das Gegenteil: Auf „Hast du etwas übersehen?“ liefert das Modell einen Scheinbefund (fehlendes Datum in v2, das auch in v1 fehlt). Die Botschaft: Die Selbstprüfung ist ein nützlicher zweiter Blick. Den eigenen Abgleich mit dem Original ersetzt sie aber nicht. Neue Befunde aus der Nachprüfung genauso prüfen wie die erste Tabelle.
- **„Ich habe nichts übersehen“ ist keine Prüfung.** Sonnet klingt völlig sicher. Hier stimmt es zufällig, aber genau so klingt es auch, wenn 2 Punkte fehlen. Deshalb bleibt der Pflicht-Prüfschritt (zählen, abhaken) wichtig.
- **Der eigentliche Fehler steckt in der Mail, nicht in der Tabelle.** Beim Verdichten auf 150 Wörter gehen Feinheiten verloren: „zusätzlich“ (Genehmigung), „einfache“ Fahrt, „ohne Frühstück“, „Erstattung“ statt „Preis“. Und aus „Regel fehlt“ wird bei Haiku „wird nicht erstattet“. Gute Frage für die Auswertung: „Stimmt jeder Satz in eurer Mail noch genau mit der Richtlinie überein?“
- **Gutes Beispiel für verantwortungsvolles Verhalten:** Sonnet und Opus weisen von sich aus darauf hin, dass v2 zum Trinkgeld nur schweigt, und empfehlen eine Klärung mit der Personalabteilung, bevor die Mail rausgeht. Das kann man zeigen: Ein guter Assistent markiert Unklarheiten, statt sie glattzubügeln.
- **„Per du“ bei einer Mail an alle** führt zu Mischformen (du/ihr, siehe Opus). Wer einheitlich will, sagt es genau, zum Beispiel: „Sprich die Leser einzeln mit du an.“
- **Die Absenderzeile** („Personal und Finanzen“) haben alle aus dem Kopf der Richtlinie übernommen („Verantwortlich: Personal und Finanzen“). Das ist nicht erfunden, aber der Absender muss trotzdem vor dem Versand angepasst werden.
- **Zeit:** Drei Nachrichten plus Prüfung passen gut in die Arbeitszeit von ca. 27 Minuten, wenn eine Station gründlich bearbeitet wird. Die Antworten auf Turn 2 sind teils lang (Abschnittstabellen). Lesezeit einplanen.

---

## Gesprächsprotokolle

### Haiku

#### Nutzer 1

Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?

#### Assistent 1

Ich habe beide Fassungen Abschnitt für Abschnitt verglichen. Es gibt sieben inhaltliche Änderungen.

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung (Abschn. 3) | Bei voraussichtlichen Kosten über 2.000 Euro ist zusätzlich die Freigabe durch die **Abteilungsleitung** nötig. | Die zusätzliche Freigabe erteilt die **Geschäftsführung**. | Bei größeren Reisen ändert sich der Genehmigungsweg. Plane mehr Vorlauf ein. |
| 2 | Bahn: 1. Klasse (Abschn. 4.1) | Die 1. Klasse darf ab einer einfachen Fahrtdauer von **mehr als vier Stunden** gebucht werden. | Die 1. Klasse darf ab mehr als **drei Stunden** einfacher Fahrtdauer gebucht werden. | Die 1. Klasse ist früher erlaubt. |
| 3 | Flug: Inlandsflüge (Abschn. 4.2) | Keine Regelung zu Inlandsflügen. | Inlandsflüge sind nur zulässig, wenn die einfache Bahnfahrt **länger als fünf Stunden** dauern würde. | Für Inlandsreisen zuerst die Bahn prüfen. Ein Flug ist nur bei sehr langer Bahnfahrt erlaubt. |
| 4 | Privates Fahrzeug (Abschn. 4.3) | Kilometerpauschale von **0,30 Euro** je gefahrenem Kilometer. | Kilometerpauschale von **0,25 Euro** je gefahrenem Kilometer. | Pro Kilometer gibt es 5 Cent weniger. |
| 5 | Übernachtung (Abschn. 5) | Erstattung bis **110 Euro** pro Nacht (ohne Frühstück). | Erstattung bis **130 Euro** pro Nacht (ohne Frühstück). | Höhere Obergrenze für Hotelkosten. |
| 6 | Trinkgeld (Abschn. 7) | Trinkgeld kann bis 10 % des Rechnungsbetrags erstattet werden, wenn es auf dem Beleg vermerkt ist. | Die Trinkgeld-Regelung ist ersatzlos gestrichen. | Trinkgeld ist nicht mehr ausdrücklich erstattungsfähig. Bei Unsicherheit bei der Personalabteilung nachfragen. |
| 7 | Abrechnungsfrist (Abschn. 8) | Abrechnung mit Originalbelegen innerhalb von **drei Monaten** nach Ende der Dienstreise. | Abrechnung innerhalb von **sechs Wochen** nach Ende der Dienstreise. | Die Frist ist deutlich kürzer. Belege möglichst zeitnah einreichen, da verspätete Abrechnungen abgelehnt werden können. |

#### Nutzer 2

Prüfe deine Tabelle noch einmal Abschnitt für Abschnitt gegen beide Fassungen.
Hast du etwas übersehen? Gibt es Regeln, die in v2 neu dazugekommen oder ganz weggefallen sind?

#### Assistent 2

Ich habe die Tabelle noch einmal gegen beide Fassungen geprüft.

**Vollständigkeit:** Die sieben Änderungen sind vollständig erfasst. Die Abschnitte 1 (Geltungsbereich), 2 (Grundsätze), 4.4 (Mietwagen und Taxi), 6 (Verpflegung) und 9 (Inkrafttreten) sind inhaltlich unverändert. Zu den übrigen Punkten:

- **Neu hinzugekommen:** Die Regel zu Inlandsflügen in Abschnitt 4.2 (Nr. 3). In v1 gab es dazu keine Regelung.
- **Ersatzlos weggefallen:** Die Trinkgeld-Regelung in Abschnitt 7 (Nr. 6). In v2 wird Trinkgeld nicht mehr erwähnt. Es ist daher nicht mehr ausdrücklich erstattungsfähig.
- **Nicht geändert, aber auffällig:** Abschnitt 9 ist in beiden Fassungen gleich. In v2 steht aber kein eigenes Datum für das Inkrafttreten. Die Richtlinie gilt also mit der Veröffentlichung im Intranet. Außerdem wurde die Abteilungsleitung bei Kosten über 2.000 Euro durch die Geschäftsführung ersetzt (Nr. 1). Die Abteilungsleitung ist für diesen Fall also nicht mehr in der Genehmigungskette vorgesehen.

Die Tabelle ist damit vollständig. Ich würde sie nur um einen Hinweis zum fehlenden Inkrafttreten-Datum in v2 ergänzen.

#### Nutzer 3

Schreib aus der Tabelle eine kurze Info-Mail an alle Mitarbeitenden (max. 150 Wörter, Ton: freundlich, sachlich, per du).
Die wichtigste Änderung zuerst.

#### Assistent 3

**Betreff:** Neue Reisekostenrichtlinie (Version 2)

Hallo zusammen,

die neue Reisekostenrichtlinie (Version 2) ist da. Das Wichtigste zuerst:

- **Abrechnungsfrist:** Reisekosten müssen jetzt innerhalb von **sechs Wochen** nach Ende der Dienstreise eingereicht werden (bisher drei Monate). Verspätete Abrechnungen können abgelehnt werden.
- **Übernachtung:** Erstattet werden bis zu **130 Euro** pro Nacht (bisher 110 Euro).
- **Privates Auto:** Die Kilometerpauschale sinkt auf **0,25 Euro** je Kilometer (bisher 0,30 Euro).
- **Genehmigung:** Bei Reisen über 2.000 Euro entscheidet künftig die **Geschäftsführung** statt der Abteilungsleitung.
- **Bahn:** Die 1. Klasse ist ab einer Fahrtdauer von **mehr als drei Stunden** erlaubt (bisher vier).
- **Flug:** Inlandsflüge sind nur erlaubt, wenn die Bahnfahrt länger als fünf Stunden dauern würde.
- **Trinkgeld:** wird nicht mehr erstattet.

Die vollständige Richtlinie findest du im Intranet. Bei Fragen wende dich an die Personalabteilung.

Viele Grüße
Personal und Finanzen

---

### Sonnet

#### Nutzer 1

Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?

#### Assistent 1

Ich habe beide Fassungen verglichen. Es gibt sieben inhaltliche Änderungen:

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung (Abschn. 3): zweite Freigabe | Bei voraussichtlichen Kosten über 2.000 € ist zusätzlich die Freigabe der Abteilungsleitung nötig. | Bei voraussichtlichen Kosten über 2.000 € ist zusätzlich die Freigabe der Geschäftsführung nötig. | Teure Reisen müssen jetzt bei der Geschäftsführung freigegeben werden. Plant dafür etwas mehr Vorlauf ein. |
| 2 | Bahn (4.1): 1. Klasse | 1. Klasse erlaubt ab einer einfachen Fahrtdauer von mehr als 4 Stunden. | 1. Klasse erlaubt ab einer einfachen Fahrtdauer von mehr als 3 Stunden. | Die 1. Klasse darf früher gebucht werden, nämlich schon bei Fahrten über 3 Stunden. |
| 3 | Flugzeug (4.2): Inlandsflüge | Keine Einschränkung für Inlandsflüge. Es gilt nur Economy und Buchung über die Reisestelle. | Inlandsflüge sind nur zulässig, wenn die einfache Bahnfahrt länger als 5 Stunden dauern würde. | Für Inlandsziele wird jetzt grundsätzlich die Bahn genutzt. Ein Flug ist nur bei sehr langen Bahnstrecken möglich. |
| 4 | Privates Fahrzeug (4.3): Kilometerpauschale | 0,30 € je Kilometer. | 0,25 € je Kilometer. | Für Fahrten mit dem Privatwagen gibt es weniger Geld, nämlich 5 Cent pro Kilometer weniger. |
| 5 | Übernachtung (5): Obergrenze | Bis zu 110 € pro Nacht (ohne Frühstück). | Bis zu 130 € pro Nacht (ohne Frühstück). | Beim Hotel gibt es mehr Spielraum, nämlich 20 € mehr pro Nacht. |
| 6 | Sonstige Kosten (7): Trinkgeld | Trinkgeld konnte bis 10 % des Rechnungsbetrags erstattet werden, wenn es auf dem Beleg vermerkt war. | Die Regelung zum Trinkgeld fehlt. | Trinkgeld wird nach der Richtlinie nicht mehr ausdrücklich erstattet. Rechnet nicht damit. |
| 7 | Abrechnung (8): Frist | Einreichung innerhalb von 3 Monaten nach Reiseende. | Einreichung innerhalb von 6 Wochen nach Reiseende. | Die Abrechnung muss deutlich schneller erfolgen. Verspätete Abrechnungen können abgelehnt werden. |

Alle übrigen Abschnitte (Geltungsbereich, Grundsätze, Mietwagen und Taxi, Verpflegung, Inkrafttreten) sind inhaltlich unverändert. Die Versionsnummer im Kopf wurde von 1 auf 2 geändert.

#### Nutzer 2

Prüfe deine Tabelle noch einmal Abschnitt für Abschnitt gegen beide Fassungen.
Hast du etwas übersehen? Gibt es Regeln, die in v2 neu dazugekommen oder ganz weggefallen sind?

#### Assistent 2

Ich habe alle neun Abschnitte noch einmal gegen beide Fassungen geprüft. Die Tabelle ist vollständig und die Angaben stimmen. Ich habe nichts übersehen und nichts falsch wiedergegeben.

Abschnitt für Abschnitt:
- 1 Geltungsbereich: unverändert.
- 2 Grundsätze: unverändert.
- 3 Genehmigung: Abteilungsleitung wird zur Geschäftsführung (Zeile 1). Die Grenze von 2.000 € und der Satz zur fehlenden Erstattung ohne Genehmigung sind gleich geblieben.
- 4.1 Bahn: Schwelle für die 1. Klasse sinkt von 4 auf 3 Stunden (Zeile 2). Reservierungen und Bahncard sind unverändert.
- 4.2 Flugzeug: Ein neuer Satz zu Inlandsflügen ist dazugekommen (Zeile 3).
- 4.3 Privates Fahrzeug: Pauschale sinkt von 0,30 € auf 0,25 € (Zeile 4). Parkgebühren und Haftungsausschluss sind unverändert.
- 4.4 Mietwagen und Taxi: unverändert.
- 5 Übernachtung: Obergrenze steigt von 110 € auf 130 € (Zeile 5). Die Ausnahmeregel für teure Städte und Messen ist unverändert.
- 6 Verpflegung: unverändert.
- 7 Sonstige Kosten: Die Trinkgeldregel ist ganz weggefallen (Zeile 6). Der Rest ist unverändert.
- 8 Abrechnung: Frist sinkt von 3 Monaten auf 6 Wochen (Zeile 7). Digitale Belege, Ablehnung bei Verspätung und Vorschussverrechnung sind unverändert.
- 9 Inkrafttreten: unverändert.

Zu deinen Fragen:
- **Neu dazugekommen** ist eine Regel, nämlich die Einschränkung für Inlandsflüge in 4.2 (Zeile 3).
- **Ganz weggefallen** ist eine Regel, nämlich die Trinkgeldregel in Abschnitt 7 (Zeile 6).

Eine Einschränkung zu Zeile 6: In v2 steht nichts zum Trinkgeld, es wird also weder erlaubt noch ausdrücklich verboten. Ob es trotzdem erstattet wird, geht aus dem Text nicht hervor. Das sollte die Personalabteilung klären.

#### Nutzer 3

Schreib aus der Tabelle eine kurze Info-Mail an alle Mitarbeitenden (max. 150 Wörter, Ton: freundlich, sachlich, per du).
Die wichtigste Änderung zuerst.

#### Assistent 3

**Betreff: Neue Reisekostenrichtlinie (Version 2)**

Hallo zusammen,

die Reisekostenrichtlinie wurde überarbeitet. Das ist neu:

**Wichtigste Änderung:** Reiseabrechnungen musst du jetzt innerhalb von sechs Wochen nach Reiseende einreichen, bisher waren es drei Monate. Verspätete Abrechnungen können abgelehnt werden.

**Weitere Änderungen:**
- Reisen über 2.000 Euro muss zusätzlich die Geschäftsführung freigeben, nicht mehr die Abteilungsleitung.
- Die 1. Klasse im Zug darfst du schon bei Fahrten über drei Stunden buchen (bisher vier).
- Inlandsflüge sind nur noch erlaubt, wenn die Bahnfahrt länger als fünf Stunden dauern würde.
- Für den Privatwagen gibt es 0,25 Euro pro Kilometer (bisher 0,30 Euro).
- Hotels kosten bis zu 130 Euro pro Nacht (bisher 110 Euro).
- Trinkgeld ist in der Richtlinie nicht mehr geregelt.

Bei Fragen hilft dir die Personalabteilung gern weiter.

Viele Grüße
Dein Team Personal und Finanzen

---

### Opus

#### Nutzer 1

Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?

#### Assistent 1

Ich habe beide Fassungen Abschnitt für Abschnitt verglichen. Es gibt **7 inhaltliche Änderungen**:

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung teurer Reisen (Abschnitt 3) | Bei voraussichtlichen Kosten über 2.000 € gibt zusätzlich die **Abteilungsleitung** frei | Bei voraussichtlichen Kosten über 2.000 € gibt zusätzlich die **Geschäftsführung** frei | Teure Reisen brauchen jetzt die Freigabe einer höheren Stelle. Besser früher beantragen, weil das länger dauern kann. |
| 2 | Bahn 1. Klasse (4.1) | 1. Klasse ab einer einfachen Fahrtdauer von **mehr als 4 Stunden** | 1. Klasse ab einer einfachen Fahrtdauer von **mehr als 3 Stunden** | Die 1. Klasse ist jetzt schon bei kürzeren Strecken erlaubt. Das ist eine Verbesserung. |
| 3 | Inlandsflüge (4.2) | Keine besondere Regel für Inlandsflüge | **Neu:** Inlandsflüge sind nur erlaubt, wenn die einfache Bahnfahrt **länger als 5 Stunden** dauern würde | Bei Reisen im Inland ist die Bahn jetzt der Normalfall. Fliegen geht nur noch bei langen Bahnstrecken. |
| 4 | Kilometerpauschale Privat-Pkw (4.3) | **0,30 €** je km | **0,25 €** je km | Wer mit dem eigenen Auto fährt, bekommt weniger erstattet (z. B. 100 km: 25 € statt 30 €). |
| 5 | Obergrenze Übernachtung (5) | Bis **110 €** pro Nacht (ohne Frühstück) | Bis **130 €** pro Nacht (ohne Frühstück) | Ihr könnt teurere Hotels buchen, ohne eine Ausnahme beantragen zu müssen. Das ist eine Verbesserung. |
| 6 | Trinkgeld (7) | Trinkgeld bis 10 % des Rechnungsbetrags wird erstattet, wenn es auf dem Beleg steht | **Gestrichen:** Die Regel zum Trinkgeld gibt es nicht mehr | Trinkgeld wird voraussichtlich nicht mehr erstattet. Am besten bei der Buchhaltung oder Personalabteilung nachfragen, ob das so gemeint ist. |
| 7 | Frist für die Abrechnung (8) | Innerhalb von **3 Monaten** nach Reiseende | Innerhalb von **6 Wochen** nach Reiseende | Ihr habt nur noch halb so viel Zeit für die Abrechnung. Wer zu spät einreicht, riskiert, dass die Abrechnung abgelehnt wird. |

**Unverändert** sind die Abschnitte 1 (Geltungsbereich), 2 (Grundsätze), 4.4 (Mietwagen und Taxi), 6 (Verpflegung) und 9 (Inkrafttreten). Ebenfalls gleich geblieben sind die übrigen Regeln in 3, 4.1 bis 4.3, 5, 7 und 8, zum Beispiel die 2.000-€-Grenze, die Economy Class, die Buchung über die Reisestelle, die Parkgebühren und die digitalen Belege.

#### Nutzer 2

Prüfe deine Tabelle noch einmal Abschnitt für Abschnitt gegen beide Fassungen.
Hast du etwas übersehen? Gibt es Regeln, die in v2 neu dazugekommen oder ganz weggefallen sind?

#### Assistent 2

Ich bin beide Fassungen noch einmal Satz für Satz durchgegangen:

| Abschnitt | Ergebnis |
|---|---|
| Kopf | Nur die Versionsnummer ist anders (1 → 2), das ist keine inhaltliche Regel |
| 1. Geltungsbereich | Gleich |
| 2. Grundsätze | Gleich |
| 3. Genehmigung | Eine Änderung: Abteilungsleitung → Geschäftsführung (Nr. 1). Die Grenze von 2.000 € bleibt. |
| 4.1 Bahn | Eine Änderung: 4 → 3 Stunden für die 1. Klasse (Nr. 2). Reservierungen und Bahncard bleiben gleich. |
| 4.2 Flugzeug | Ein neuer Satz: Inlandsflüge nur bei mehr als 5 Stunden Bahnfahrt (Nr. 3). Alles andere bleibt. |
| 4.3 Privates Fahrzeug | Eine Änderung: 0,30 € → 0,25 € pro km (Nr. 4). Parkgebühren und Haftung bleiben gleich. |
| 4.4 Mietwagen und Taxi | Gleich |
| 5. Übernachtung | Eine Änderung: 110 € → 130 € (Nr. 5). Die Ausnahme für teure Städte und Messen bleibt. |
| 6. Verpflegung | Gleich |
| 7. Sonstige Kosten | Ein Satz fällt weg: die Trinkgeld-Regel (Nr. 6). Nebenkosten und Privatkosten bleiben gleich. |
| 8. Abrechnung | Eine Änderung: 3 Monate → 6 Wochen (Nr. 7). Digitale Belege, Ablehnung bei Verspätung und Vorschüsse bleiben gleich. |
| 9. Inkrafttreten | Gleich |

**Ergebnis:** Die Tabelle ist vollständig. Ich habe keine weitere Änderung gefunden.

- **Neu dazugekommen** ist genau eine Regel: die Einschränkung für Inlandsflüge (Nr. 3).
- **Ganz weggefallen** ist genau eine Regel: die Erstattung von Trinkgeld bis 10 % (Nr. 6).
- Die anderen fünf Punkte ändern eine bestehende Regel (Zahl, Frist oder Zuständigkeit).

Ein Hinweis zu Nr. 6: In v2 steht nicht ausdrücklich, dass Trinkgeld nicht mehr erstattet wird. Die Regel fehlt einfach. Bevor ihr das so an alle weitergebt, solltet ihr bei der zuständigen Stelle nachfragen, wie es gemeint ist.

#### Nutzer 3

Schreib aus der Tabelle eine kurze Info-Mail an alle Mitarbeitenden (max. 150 Wörter, Ton: freundlich, sachlich, per du).
Die wichtigste Änderung zuerst.

#### Assistent 3

**Betreff:** Neue Reisekostenrichtlinie – das ändert sich für dich

Hallo zusammen,

ab sofort gilt Version 2 unserer Reisekostenrichtlinie. Das Wichtigste in Kürze:

- **Kürzere Abrechnungsfrist:** Reicht eure Reisekosten bitte innerhalb von **6 Wochen** nach Reiseende ein (bisher 3 Monate). Wer später einreicht, riskiert, dass die Abrechnung abgelehnt wird.
- **Privat-Pkw:** Die Kilometerpauschale sinkt auf **0,25 €** (bisher 0,30 €).
- **Inlandsflüge** sind nur noch erlaubt, wenn die Bahnfahrt länger als 5 Stunden dauern würde.
- **Bahn 1. Klasse** ist schon ab 3 Stunden Fahrtdauer erlaubt (bisher 4).
- **Hotel:** Die Obergrenze steigt auf **130 €** pro Nacht (bisher 110 €).
- **Reisen über 2.000 €** gibt jetzt die Geschäftsführung frei, nicht mehr die Abteilungsleitung.
- **Trinkgeld:** Die Regel zur Erstattung gibt es nicht mehr.

Die vollständige Richtlinie findest du im Intranet. Bei Fragen hilft dir die Personalabteilung gern.

Viele Grüße
Personal und Finanzen

*(rund 130 Wörter. Hinweis: Die Anrede „Hallo zusammen“ und „euch/eure“ passen zu einer Mail an alle. Wenn du jede Person einzeln ansprechen willst, ändere sie in „Hallo“ und „deine“.)*
