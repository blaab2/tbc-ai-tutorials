# Testlauf: Übung 3 / Station B Basis – Reisekostenrichtlinie v1 vs. v2 vergleichen

**Herkunft:** Station B, Abschnitt „Basis“ aus [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#station-b-zwei-versionen-einer-richtlinie-vergleichen). Sollergebnis aus [Trainer-Loesungshinweise.md – Station B](../06_Uebungen/Trainer-Loesungshinweise.md#station-b-reisekostenrichtlinie-v1-vs-v2). Material: [richtlinie_reisekosten_v1.md](../07_Beispielmaterial/richtlinie_reisekosten_v1.md) und [richtlinie_reisekosten_v2.md](../07_Beispielmaterial/richtlinie_reisekosten_v2.md).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt (Vorlage aus dem Übungsblatt, beide Dateien als Anhang):**

```text
Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?
```

**Was laut Material herauskommen soll:** Eine Tabelle mit genau 7 inhaltlichen Änderungen, alt und neu richtig zugeordnet. Die Versionsnummer („Version 1“ → „Version 2“) zählt nicht mit.

**Tatsächliche Unterschiede (per `diff` geprüft):** genau 8 geänderte Zeilen. Davon ist eine die Versionsnummer (Zeile 4), die übrigen 7 sind:

| Nr. | Abschnitt | v1 | v2 |
|---|---|---|---|
| 1 | 3. Genehmigung, Reisen über 2.000 € | Freigabe durch Abteilungsleitung | Freigabe durch Geschäftsführung |
| 2 | 4.1 Bahn, 1. Klasse | mehr als vier Stunden | mehr als drei Stunden |
| 3 | 4.2 Flugzeug | keine Regel | neu: Inlandsflug nur, wenn Bahn länger als fünf Stunden |
| 4 | 4.3 Kilometerpauschale | 0,30 € | 0,25 € |
| 5 | 5. Übernachtung | bis 110 € (ohne Frühstück) | bis 130 € (ohne Frühstück) |
| 6 | 7. Trinkgeld | bis 10 % erstattbar, wenn auf Beleg | Satz ersatzlos gestrichen |
| 7 | 8. Einreichungsfrist | drei Monate | sechs Wochen |

Unverändert: Abschnitte 1, 2, 4.4, 6, 9 sowie Bahncard, Parkgebühren, digitale Belege. In der Datei gibt es **keine** verschobenen Abschnitte und keine reinen Umformulierungen.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Alle 7 Änderungen gefunden? | ja (7/7) | ja (7/7) | ja (7/7) |
| Nr. 1 (Abteilungsleitung → Geschäftsführung) | ja | ja | ja |
| Nr. 3 (neue Inlandsflug-Regel) | ja | ja | ja |
| Nr. 6 (Trinkgeld gestrichen) | ja | ja | ja |
| Alt/neu richtig zugeordnet? | ja | ja | ja |
| Versionsnummer weggelassen? | ja (stillschweigend) | ja | ja, und ausdrücklich begründet |
| Erfundene Änderungen? | nein | nein | nein |
| Anzahl stimmig angegeben? | keine Zahl im Text, Tabelle 7 | **widersprüchlich**: Einleitung „8 Änderungen“, Tabelle 7, danach Selbstkorrektur „7, nicht 8“ | „7 inhaltliche Änderungen“, stimmig |
| Unveränderte Abschnitte genannt? | ja, 1, 2, 4.4, 6, 9 (korrekt) | ja, inhaltlich korrekt | ja, 1, 2, 4.4, 6, 9 (korrekt) |
| Rechenbeispiele korrekt (per `python3`)? | ja (300 km: 75 € statt 90 €; 3 Nächte: +60 €) | ja (200 km: 10 € weniger) | ja (400 km: 100 € statt 120 €) |
| Umgang mit gestrichener Trinkgeld-Regel | stellt als Tatsache dar: „nicht mehr erstattet und ist selbst zu tragen“ | vorsichtig: „vermutlich … steht dort nicht ausdrücklich“, Rückfrage empfohlen | vorsichtig: „nicht mehr ausdrücklich erstattet“, Rückfrage empfohlen |
| Zusatznutzen | knapp, sachlich | Hinweise, was gleich bleibt (Betragsgrenze 2.000 €, Parkgebühren, Messe-Ausnahme) | Einordnung „besser / schlechter / neuer Ablauf“ |
| Anrede | neutral | neutral | du |

**Kurz:** Die Übung funktioniert inhaltlich, aber anders als in den Lösungshinweisen erwartet. Alle drei Modelle finden alle 7 Änderungen, auch die als „schwer zu finden“ beschriebenen Nr. 1, 3 und 6. Niemand erfindet etwas, niemand vertauscht alt und neu. Der einzige echte Ausrutscher ist Sonnets widersprüchliche Zählung (erst 8, dann 7). Der Unterschied liegt vor allem in der Deutung der gestrichenen Trinkgeld-Regel.

---

## Gefundene Fehler mit Beleg

- **Sonnet, Zählung widersprüchlich:** Einleitung „dabei 8 inhaltliche Änderungen gefunden“, Tabelle hat 7 Zeilen, am Ende „Korrektur zur Zählung: Es sind **7** inhaltliche Änderungen, nicht 8“. Laut `diff` sind es 8 geänderte Zeilen, davon eine Versionsnummer. Vermutlich hat das Modell zuerst die Versionszeile mitgezählt. Das ist kein Fehler in der Tabelle, aber eine Antwort, die sich selbst widerspricht. Wer nur den ersten Satz liest, sucht eine achte Änderung.
- **Haiku, Trinkgeld überinterpretiert:** „Trinkgeld wird nach v2 nicht mehr erstattet und ist selbst zu tragen.“ v2, Abschnitt 7, sagt nur nichts mehr über Trinkgeld; ein ausdrückliches Verbot steht dort nicht. Die Folgerung ist naheliegend, wird aber als sichere Tatsache formuliert. Sonnet und Opus kennzeichnen das als Schluss und empfehlen eine Rückfrage.
- **Haiku, kleine Ungenauigkeit Nr. 1:** „Ab voraussichtlich 2.000 Euro“ bzw. „Ab 2.000 Euro“. Die Quelle sagt „deren voraussichtliche Kosten 2.000 Euro **übersteigen**“, also erst über 2.000 €. Für die Übung unerheblich, aber ein gutes Beispiel für Unschärfe beim Umformulieren.
- **Opus, Nr. 7 „ungefähr halb so lang“:** 6 Wochen gegenüber 3 Monaten (ca. 13 Wochen) sind etwa 46 % (per `python3`). Die Aussage ist vertretbar.
- **Alle Rechenbeispiele stimmen:** 300 × 0,25 = 75 €, 300 × 0,30 = 90 €; 3 × 20 € = 60 €; 200 × 0,05 = 10 €; 400 × 0,25 = 100 €, 400 × 0,30 = 120 € (per `python3`).
- Sonnet „Kompaktklasse bei Mietwagen“, „Pauschalen bei Verpflegung“, „digitale Belege“ als unverändert: stimmt (Abschnitte 4.4, 6, 8 wortgleich bis auf die Frist).

---

## Lehren für die Auswertung

1. **Der erwartete Fehler (übersehene Änderungen) tritt hier nicht auf.** Mit sauber hochgeladenen Markdown-Dateien finden alle drei Modelle alle 7 Punkte. Der Hinweis in den Lösungshinweisen („Erfahrungsgemäß schwer zu finden: Nr. 3 und Nr. 6 … Nr. 1 übersieht man leicht“) beschreibt eher, was **Menschen** beim Lesen übersehen, oder ältere/andere Tools. Die Frage „Wer hat alle 7 gefunden?“ funktioniert trotzdem, das Ergebnis wird aber oft „alle“ lauten. Das ist keine Entwarnung: Der Prüfschritt bleibt Pflicht, weil man ohne Abgleich nicht weiß, ob die Liste vollständig ist.
2. **Zählung und Text gegeneinander prüfen.** Sonnets Antwort sagt „8“ und liefert 7. Das zeigt: Auch eine richtige Tabelle kann von einem falschen Begleitsatz umrahmt sein. Teilnehmende sollen Zeilen selbst zählen, statt der genannten Zahl zu glauben.
3. **Gestrichene Regeln richtig deuten.** Was fehlt, ist nicht automatisch verboten. Haiku schreibt „ist selbst zu tragen“, Sonnet und Opus empfehlen eine Rückfrage bei Personal/Finanzen. Guter Diskussionspunkt: Welche Formulierung gehört in die Info-Mail an alle?
4. **Die Spalte „Was bedeutet das?“ ist der eigentliche Mehrwert und zugleich die Fehlerquelle.** Hier stehen Deutungen und Rechenbeispiele, die nicht im Dokument stehen. Rechenbeispiele nachrechnen lassen (hier alle richtig), Deutungen als solche erkennen.
5. **Ehrlicher Vergleich mit dem Werkzeug:** Ein Vergleichswerkzeug (Word „Vergleichen“) zeigt dieselben 8 Stellen in Sekunden. Die KI spart nicht das Finden, sondern das Erklären und Einordnen. Wer den Fehlerfall vorführen will, nimmt längere Dokumente, eingescannte PDFs oder fügt beide Fassungen unbeschriftet in einen einzigen Block ein.

---

## Gesprächsprotokolle

### Haiku

**Nutzer 1**

Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?

**Assistent 1**

Ich habe beide Fassungen verglichen. Die Abschnitte 1, 2, 4.4, 6 und 9 sind inhaltlich unverändert. Die folgende Tabelle enthält alle inhaltlichen Änderungen (Abschnitt 4.2 ergänzt, Abschnitt 7 gekürzt, sonst jeweils geänderte Werte bzw. Zuständigkeiten).

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Zusatzfreigabe bei hohen Reisekosten (§ 3) | Ab voraussichtlich 2.000 Euro Reisekosten ist die Freigabe durch die **Abteilungsleitung** nötig. | Ab 2.000 Euro ist die Freigabe durch die **Geschäftsführung** nötig. | Teure Dienstreisen brauchen eine höhere Freigabeebene. Der Genehmigungsweg kann dadurch länger dauern, daher Anträge früher stellen. |
| 2 | Bahn: Reise in der 1. Klasse (§ 4.1) | Die 1. Klasse darf ab einer einfachen Fahrtdauer von **mehr als 4 Stunden** gebucht werden. | Die 1. Klasse darf ab einer einfachen Fahrtdauer von **mehr als 3 Stunden** gebucht werden. | Auf längeren Strecken (3 bis 4 Stunden) ist die 1. Klasse jetzt erlaubt. Standard bleibt die 2. Klasse. |
| 3 | Inlandsflüge (§ 4.2) | Keine besondere Regel für Inlandsflüge. Flüge sind in der Economy Class und nur über die Reisestelle zu buchen. | Inlandsflüge sind **nur zulässig, wenn die einfache Bahnfahrt länger als 5 Stunden dauern würde**. | Kurze Inlandsflüge sind nicht mehr vorgesehen. Vor einem Flug die Bahnzeit prüfen. |
| 4 | Kilometerpauschale privates Auto (§ 4.3) | 0,30 Euro je gefahrenem Kilometer. | 0,25 Euro je gefahrenem Kilometer. | Pro Kilometer gibt es 5 Cent weniger. Beispiel: 300 km ergeben 75 Euro statt 90 Euro. |
| 5 | Hotelobergrenze pro Nacht (§ 5) | Übernachtung wird bis 110 Euro pro Nacht (ohne Frühstück) erstattet. | Übernachtung wird bis 130 Euro pro Nacht (ohne Frühstück) erstattet. | Mehr Spielraum bei der Hotelwahl. Beispiel: Bei 3 Nächten sind bis zu 60 Euro mehr erstattbar. |
| 6 | Trinkgeld (§ 7) | Trinkgeld wird bis 10 % des Rechnungsbetrags erstattet, wenn es auf dem Beleg vermerkt ist. | Die Erstattungsregel für Trinkgeld ist **ersatzlos entfallen**. | Trinkgeld wird nach v2 nicht mehr erstattet und ist selbst zu tragen. |
| 7 | Frist für die Reisekostenabrechnung (§ 8) | Abrechnung mit Originalbelegen innerhalb von **drei Monaten** nach Reiseende. | Abrechnung mit Originalbelegen innerhalb von **sechs Wochen** nach Reiseende. | Die Frist ist deutlich kürzer. Belege zeitnah nach der Reise einreichen, sonst droht eine Ablehnung. |

Wichtig: Die Richtlinie ist laut Kopfzeile fiktives Übungsmaterial. Die Angaben beziehen sich nur auf die beiden Fassungen und ersetzen keine echte Beratung.

### Sonnet

**Nutzer 1**

Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?

**Assistent 1**

Ich habe beide Fassungen verglichen und dabei 8 inhaltliche Änderungen gefunden. Alles andere ist unverändert geblieben (Geltungsbereich, Grundsätze, Mietwagen/Taxi, Verpflegung, Inkrafttreten).

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung (Abschn. 3): zusätzliche Freigabe bei Reisen über 2.000 € | Zusätzliche Freigabe durch die **Abteilungsleitung** | Zusätzliche Freigabe durch die **Geschäftsführung** | Teure Reisen (über 2.000 €) brauchen jetzt die Freigabe der Geschäftsführung statt der Abteilungsleitung. Der Weg dauert vermutlich länger, daher früher beantragen. Die Betragsgrenze von 2.000 € bleibt gleich. |
| 2 | Bahn (4.1): 1. Klasse | 1. Klasse erlaubt bei einfacher Fahrtdauer **mehr als 4 Stunden** | 1. Klasse erlaubt bei einfacher Fahrtdauer **mehr als 3 Stunden** | Die 1. Klasse darf jetzt schon bei kürzeren Fahrten gebucht werden (ab über 3 Stunden statt über 4). |
| 3 | Flugzeug (4.2): Inlandsflüge | Keine besondere Einschränkung für Inlandsflüge (nur Economy, Buchung über die Reisestelle) | Inlandsflüge nur zulässig, wenn die einfache Bahnfahrt **länger als 5 Stunden** dauern würde | Für Inlandsziele ist die Bahn der Normalfall. Fliegen ist nur noch bei Bahnfahrten über 5 Stunden erlaubt. Economy und Buchung über die Reisestelle gelten weiterhin. |
| 4 | Privates Fahrzeug (4.3): Kilometerpauschale | 0,30 € je Kilometer | 0,25 € je Kilometer | Bei Fahrten mit dem Privat-Pkw gibt es weniger Geld, 5 Cent weniger pro km (bei 200 km also 10 € weniger). Parkgebühren gegen Beleg und der Haftungsausschluss bleiben gleich. |
| 5 | Übernachtung (5): Hotelobergrenze | Bis zu 110 € pro Nacht (ohne Frühstück) | Bis zu 130 € pro Nacht (ohne Frühstück) | Hotels dürfen 20 € pro Nacht teurer sein. Ausnahmen für teure Städte und Messen durch die Führungskraft bleiben möglich. |
| 6 | Sonstige Kosten (7): Trinkgelder | Trinkgelder können bis 10 % des Rechnungsbetrags erstattet werden, wenn sie auf dem Beleg vermerkt sind | Regelung zu Trinkgeldern ist **entfallen** (nicht mehr erwähnt) | Trinkgelder werden nach der neuen Fassung vermutlich nicht mehr erstattet. Das steht dort nicht ausdrücklich, daher im Zweifel bei Personal/Buchhaltung nachfragen. |
| 7 | Abrechnung (8): Einreichungsfrist | Innerhalb von **drei Monaten** nach Reiseende | Innerhalb von **sechs Wochen** nach Reiseende | Die Frist ist deutlich kürzer. Abrechnung mit allen Belegen zeitnah einreichen, sonst droht Ablehnung wegen Verspätung. |

Korrektur zur Zählung: Es sind **7** inhaltliche Änderungen, nicht 8 (siehe Tabelle). Nicht geändert wurden unter anderem die Belegpflicht für Parkgebühren, die Kompaktklasse bei Mietwagen, die Pauschalen bei Verpflegung und die Zulässigkeit digitaler Belege.

Hinweis: Die Änderung bei den Trinkgeldern (Nr. 6) ist eine Streichung, also nicht ausdrücklich als Verbot formuliert. Die rechtliche oder steuerliche Bewertung ist hier nicht Teil meiner Antwort.

### Opus

**Nutzer 1**

Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?

**Assistent 1**

Ich habe beide Fassungen Abschnitt für Abschnitt verglichen. Es gibt **7 inhaltliche Änderungen**. Die Abschnitte 1, 2, 4.4, 6 und 9 sind in beiden Fassungen gleich. Die neue Versionsnummer (Version 1 → Version 2) habe ich nicht in die Tabelle aufgenommen, weil sie keine Regel ändert.

| Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende? |
|---|---|---|---|---|
| 1 | Genehmigung bei Reisen über 2.000 € (Abschnitt 3) | Zusätzliche Freigabe durch die **Abteilungsleitung** | Zusätzliche Freigabe durch die **Geschäftsführung** | Teure Reisen müssen jetzt eine höhere Stelle durchlaufen. Plane dafür mehr Zeit ein und stelle den Antrag früher. |
| 2 | 1. Klasse Bahn (Abschnitt 4.1) | Erlaubt ab einer einfachen Fahrtdauer von **mehr als vier Stunden** | Erlaubt ab einer einfachen Fahrtdauer von **mehr als drei Stunden** | Verbesserung: Du darfst schon bei kürzeren Strecken 1. Klasse buchen. |
| 3 | Inlandsflüge (Abschnitt 4.2) | Keine besondere Einschränkung für Inlandsflüge (nur Economy, Buchung über die Reisestelle) | Inlandsflüge **nur zulässig, wenn die einfache Bahnfahrt länger als fünf Stunden** dauern würde | Neue Einschränkung: Bei kürzeren Inlandsstrecken musst du die Bahn nehmen. Prüfe vor jeder Flugbuchung die Bahnfahrzeit. |
| 4 | Kilometerpauschale privater Pkw (Abschnitt 4.3) | **0,30 €** je gefahrenem Kilometer | **0,25 €** je gefahrenem Kilometer | Verschlechterung: Für Fahrten mit dem eigenen Auto bekommst du weniger Geld. Beispiel: Bei 400 km sind das 100 € statt bisher 120 €. |
| 5 | Übernachtung (Abschnitt 5) | Erstattung bis **110 €** pro Nacht (ohne Frühstück) | Erstattung bis **130 €** pro Nacht (ohne Frühstück) | Verbesserung: Du kannst teurere Hotels buchen, ohne eine Ausnahme beantragen zu müssen. Die Ausnahmeregel für teure Städte und Messen gilt weiter. |
| 6 | Trinkgelder (Abschnitt 7) | Trinkgelder bis **10 % des Rechnungsbetrags** werden erstattet, wenn sie auf dem Beleg vermerkt sind | Die Regelung ist **ersatzlos gestrichen** | Trinkgelder werden laut Richtlinie nicht mehr ausdrücklich erstattet. Rechne damit, dass du sie selbst zahlst, und frag im Zweifel bei Personal oder Finanzen nach. |
| 7 | Abgabefrist Abrechnung (Abschnitt 8) | Innerhalb von **drei Monaten** nach Reiseende | Innerhalb von **sechs Wochen** nach Reiseende | Die Frist ist ungefähr halb so lang. Reiche deine Abrechnung deutlich früher ein, sonst kann sie abgelehnt werden. |

**Kurz zusammengefasst:**
- **Besser für Mitarbeitende:** Nr. 2 (1. Klasse) und Nr. 5 (Hotel).
- **Schlechter oder strenger:** Nr. 3 (Inlandsflüge), Nr. 4 (Kilometergeld), Nr. 6 (Trinkgeld) und Nr. 7 (kürzere Frist).
- **Neuer Ablauf:** Nr. 1 (Geschäftsführung statt Abteilungsleitung).

Hinweis: Die Liste stammt aus einem Textvergleich. Prüfe bei wichtigen Entscheidungen bitte trotzdem die Originalfassungen.

---

Zurück zum [Übungsblatt Übung 3](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md)
