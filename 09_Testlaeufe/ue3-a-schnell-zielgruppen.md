# Testlauf: Übung 3 / Station A Für Schnelle – Zusammenfassung für andere Zielgruppen

**Herkunft:** Abschnitt „Für Schnelle“, erster Spiegelstrich, in [Uebung_3_Dokumente_und_Tabellen.md – Station A](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#station-a-langen-bericht-zusammenfassen): „Lass dir den Bericht für eine **andere Zielgruppe** zusammenfassen, z. B. für das Montageteam in einfacher Sprache oder für einen Kunden (ohne interne Details).“ Material: [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md). Zum Abgleich: [Trainer-Loesungshinweise.md – Station A](../06_Uebungen/Trainer-Loesungshinweise.md#station-a-prüfbericht-zusammenfassen). Dort steht zu dieser Zusatzaufgabe **nichts Eigenes**.

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf:** Ein Gespräch mit drei Turns. Turn 1 ist der Basis-Prompt von Station A (mit dem Bericht im Anhang). Turn 2 und 3 haben wir aus dem Text „Für Schnelle“ abgeleitet:

```text
Fasse den Bericht jetzt für das Montageteam in einfacher Sprache zusammen.
```

```text
Fasse den Bericht jetzt für einen Kunden zusammen – ohne interne Details.
```

**Was laut Material herauskommen soll:**
- *Montageteam:* kurze Sätze, Fachbegriffe erklärt. Praxisrelevant sind z. B. der häufigere Schutzglaswechsel (nur 2 auf Lager, 3–6 Wochen Lieferzeit), die Schulung weiterer Personen, die manuelle Übertragung aus dem ERP bis zum Update 4.3 und die Staubmessung.
- *Kunde:* keine Angaben zu Kaufpreis, Einbehalt oder Schlusszahlung, keine internen Ersparnisse, keine Personalthemen, keine Fernwartungs-Zugangsdaten, keine internen Bewertungen.
- In beiden Fassungen: keine erfundenen Fakten.

---

## Bewertung

Legende: ✔ erfüllt · ◐ teilweise · ✘ nicht erfüllt

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Turn 1: genau 5 Sätze, Vorbehalt + 5 % Einbehalt, kein erfundener Betrag/Termin | ✔ | ✔ | ✔ |
| Montage: einfache Sprache, kurze Sätze | ✔ | ✔ | ✔ |
| Montage: Fachbegriffe erklärt | ✘ (Endschalter, Palettenwechsler, Erstmusterprüfung, Restgitter unerklärt) | ◐ (Bart, Erstmuster, ERP, Toleranz unerklärt) | ◐ (Toleranz, Grat, Bart, ERP unerklärt) |
| Montage: Schutzglas / Schulung / ERP manuell / Staub | 3 von 4 (Staub fehlt) | 4 von 4 | 1 von 4 (nur ERP) |
| Montage: keine erfundenen Fakten | ✘ („Update kommt in den nächsten Wochen“) | ◐ („erlaubter Wert“ statt interner Richtwert) | ◐ („45 % schneller“ statt 45 % kürzere Zeit) |
| Kunde: keine Preis-/Einbehalt-/Zahlungsinfos | ✔ | ✔ | ✔ |
| Kunde: keine Ersparnis, keine Personalthemen, keine Zugangsdaten | ✔ | ✔ | ✔ |
| Kunde: keine internen Bewertungen/offenen Punkte | ✘ (Taktzeit, Leistung, Staub, „Klärung mit Hersteller“) | ◐ („Feinheiten … Software-Updates“) | ✔ (listet Weggelassenes ausdrücklich auf) |
| Kunde: keine erfundenen Aussagen/Zusagen | ◐ („wird derzeit mit dem Hersteller abgestimmt“) | ✘ („keinen Einfluss auf Ihre Aufträge“) | ◐ („Vor der Inbetriebnahme geprüft“, „seit Kurzem“ – selbst als Prüfpunkt markiert) |
| Kunde: übernimmt falsches „alle Maße in Toleranz“ | ja | ja | ja |
| Hinweise auf Unsicherheit / Prüfbedarf | keine | keine | ja (Montage-Bezug fehlt, Abnahme offen, fiktive Daten) |

**Gesamturteil:** Die Übung funktioniert **teilweise**. Alle drei Modelle lassen bei der Kundenfassung Kaufpreis, Einbehalt, Ersparnis, Namen und Zugangsdaten zuverlässig weg. Dafür entstehen genau die typischen Fehler beim Umschreiben für eine Zielgruppe: Aussagen werden „geglättet“, und es kommen neue Zusagen hinzu. Das ist didaktisch wertvoll. Unklar ist dagegen die Zielgruppe „Montageteam“: Laut Bericht arbeiten an der Anlage Bediener aus der Fertigung, kein Montageteam. Die Modelle deuten den Begriff deshalb unterschiedlich (siehe unten).

---

## Gefundene Fehler mit Beleg

### Haiku

1. **Erfundener Zeitrahmen für das Update (Montage):** „Das Software-Update 4.3 kommt in den nächsten Wochen.“ – Bericht 3.6: „im Laufe des Quartals … Ein konkreter Termin für das Update wurde nicht genannt.“ Genau dieser Stolperstein steht schon für Turn 1 in den Lösungshinweisen („Erfundener Termin für das Software-Update“). Hier tritt er erst beim Umschreiben in einfache Sprache auf.
2. **Wunsch wird zur Notwendigkeit (Montage):** „Die Anlage braucht bald eine Ablage für Restgitter.“ – Bericht 6: „Die Bediener **wünschen sich** eine zusätzliche Ablagefläche“.
3. **Offener Punkt wird zum Beschluss (Montage):** „Es sollen mindestens zwei weitere Personen geschult werden“. Laut Bericht 3.6 sind zwei weitere Personen „nötig“, die Schulung „müsste gesondert beauftragt werden“. Beschlossen ist das also noch nicht.
4. **Staubmessung fehlt** in der Montagefassung, obwohl sie den Arbeitsplatz betrifft (Bericht 3.4).
5. **Interne Bewertungen in der Kundenfassung:** Haiku nennt dem Kunden „Taktzeit eines Teils, der Leistungsaufnahme und der Staubmessung bei verzinktem Material“ als Klärungsbedarf. Das sind interne Prüfergebnisse und Vertragspunkte gegenüber dem Lieferanten.
6. **Erfundener Stand (Kunde):** „der derzeit mit dem Hersteller abgestimmt wird“. Der Bericht ist ein Entwurf mit Empfehlung (Abschnitt 7). Von einer laufenden Abstimmung steht dort nichts.
7. Kleinigkeit: „Endschalter … repariert“. Laut Bericht 3.3 war er „falsch justiert“ und wurde dann „behoben“. Die Gesamtstillstandszeit „etwa 3 Stunden“ stimmt: 35 + 130 + 20 = 185 min ≈ 3 h 05 min (nachgerechnet).

### Sonnet

1. **Erfundene Zusage an den Kunden:** „Auf Ihre Aufträge und die Qualität Ihrer Teile haben diese Punkte nach aktuellem Stand keinen Einfluss.“ Das steht nirgends im Bericht. Er nennt sogar Punkte, die die Lieferfähigkeit betreffen können: nur 2 Schutzgläser auf Lager bei 3–6 Wochen Lieferzeit (3.3), ERP-Übergabefehler (3.6). Außerdem fertigt die Anlage Gehäuseteile für die **eigenen** Produktlinien SG-40/SG-60 (Abschnitt 1). „Ihre Teile“ ist also schon vom Ansatz her falsch.
2. **Erfundener Nutzen:** „Das hilft uns, Aufträge zuverlässiger und zügiger abzuarbeiten.“ Der Bericht nennt kürzere Bearbeitungszeiten (3.2), aber keine Auswirkung auf Kundenaufträge.
3. **„Erlaubter Wert“ statt interner Richtwert (Montage):** „Staubbelastung knapp unter dem erlaubten Wert“. Laut Bericht 3.4 liegt sie bei 92 % des **internen Richtwerts**. „Erlaubt“ klingt nach gesetzlichem Grenzwert.
4. **Heikles Personalthema an die Belegschaft:** „Ein Schichtbetrieb könnte bald reichen, wo bisher zwei Schichten nötig waren.“ Inhaltlich stimmt das (3.2: „voraussichtlich ein Einschichtbetrieb ausreichend“). Dem Team das ungefiltert zu sagen, ist aber eine Kommunikationsfrage, die die KI nicht abwägt.

### Opus

1. **Prozentfehler (Montage):** „ungefähr 45 % schneller“. Laut Bericht 3.2 ist die Bearbeitungszeit um rund 45 % **verkürzt**. Nachgerechnet: Bei 55 % der alten Zeit ist die Anlage 1/0,55 ≈ 1,82-mal so schnell, also rund **82 % schneller**. Die Aussage ist dadurch nicht übertrieben, sondern untertrieben, aber trotzdem sachlich falsch umgeformt.
2. **Reihenfolge falsch (Kunde):** „Vor der Inbetriebnahme haben wir die Anlage zwei Wochen lang geprüft“. Laut Bericht 2 fand die Inbetriebnahme **in** der ersten Prüfwoche statt.
3. **Status vorweggenommen (Kunde):** „ersetzt seit Kurzem unsere bisherige Anlage“. Die Abnahme ist noch nicht erfolgt (Status „Entwurf zur Freigabe“). Opus weist im Anschluss selbst darauf hin („Bitte vor dem Versand prüfen“).
4. **Montagefassung lässt Kernpunkte weg:** Schutzglaswechsel, Schulung und Staubmessung fehlen. Opus begründet das offen: „Im Bericht steht nichts direkt über die Arbeit in der Montage.“ Es hat „Montageteam“ als nachgelagerte Montage verstanden, die die geschnittenen Teile weiterverarbeitet. Diese Deutung ist vertretbar.
5. „Ganz weg ist es laut Bericht nicht“ (Bart bei Teil C): Im Bericht steht „deutlich reduziert“. Die Folgerung ist vertretbar, steht dort aber nicht wörtlich.

### Bei allen drei Modellen

- **„Alle Maße in Toleranz“ wird ungeprüft an den Kunden weitergegeben** (Haiku: „bei allen geprüften Teilen innerhalb der Toleranz“, Sonnet: „Alle gemessenen Maße lagen innerhalb der vorgegebenen Toleranzen“, Opus: „Alle geprüften Maße lagen innerhalb der festgelegten Toleranzen“; Sonnet und Opus auch in der Montagefassung). Nachgerechnet: Prüfteil B, Schlitzbreite, Toleranz ±0,10 mm, größte Abweichung **0,13 mm**. Das ist die einzige Zeile außerhalb der Toleranz, trotzdem steht dort „i. O.“ (Abschnitt 4). Was intern als Widerspruch im Bericht durchgeht, wird in einer Kundeninformation zu einer **falschen Qualitätsaussage nach außen**.
- Keine Fernwartungs-Zugangsdaten, kein Kaufpreis, kein Einbehalt, keine Ersparnis in der Kundenfassung. Dieser Teil funktioniert zuverlässig.
- Turn 1 ist bei allen korrekt: genau 5 Sätze, Vorbehalt + 5 % Einbehalt, Schlusszahlung 30 %, kein Eurobetrag erfunden, Update ohne festen Termin.

---

## Unterschiede zwischen den Modellen

- **Haiku** schreibt kurz und fürs Team praktisch, erfindet aber Details: „nächste Wochen“, „braucht bald“. In der Kundenfassung gibt es interne Schwachstellen preis.
- **Sonnet** liefert die vollständigste Montagefassung (alle vier Praxispunkte). Die Kundenfassung ist ausgefeilt im Marketington und enthält gerade deshalb die schwerste Erfindung, nämlich eine Zusage an den Kunden.
- **Opus** fragt sich, wer die Zielgruppe eigentlich ist, sagt offen, was der Bericht für die Montage **nicht** hergibt, und listet auf, was in der Kundenfassung bewusst fehlt und vor dem Versand geprüft werden muss. Dafür fehlen in der Montagefassung die erwarteten Praxispunkte, und es gibt einen Rechenfehler beim Prozentwert.

---

## Lehren für die Auswertung

1. **Umschreiben ist nicht neutral.** Beim Wechsel der Zielgruppe „glättet“ die KI: Aus „wünschen sich“ wird „braucht“, aus „interner Richtwert“ wird „erlaubter Wert“, aus „im Quartal, ohne Termin“ wird „in den nächsten Wochen“. Für die Auswertung eignet sich die Frage: „Welche Aussage klingt in der neuen Fassung sicherer als im Original?“
2. **Weglassen klappt, Hinzufügen ist die Gefahr.** Alle drei lassen Geld, Namen und Zugangsdaten zuverlässig weg. Beim Kunden kommen aber neue Aussagen dazu, die nach Zusagen klingen (Sonnet: „keinen Einfluss auf Ihre Aufträge“). Ein Text nach außen braucht den Prüfschritt noch dringender als einer nach innen.
3. **Ein interner Fehler wird nach außen weitergetragen.** Der Widerspruch bei der Schlitzbreite (0,13 mm bei ±0,10 mm) landet bei allen drei als „alle Maße in Toleranz“ im Kundentext. So wird ein Fehler im Bericht zu einer falschen Zusage an den Kunden. Das schließt gut an den versteckten Prüfpunkt aus den Lösungshinweisen an.
4. **Die Zielgruppe muss man beschreiben, nicht nur benennen.** „Montageteam“ verstehen die Modelle verschieden: Bediener in der Fertigung (Haiku, Sonnet) oder nachgelagerte Montage (Opus). Besser ist zum Beispiel: „für die Bediener und die Instandhaltung in Halle 3: Was ändert sich im Arbeitsalltag?“
5. **Zahlen beim Vereinfachen prüfen:** „45 % kürzere Zeit“ heißt nicht „45 % schneller“. Lässt sich gut live nachrechnen.
6. **Was „intern“ bedeutet, sollte man vorgeben.** Die KI weiß nicht, ob offene Vertragspunkte mit dem Lieferanten oder die Staubmessung für einen Kunden tabu sind (Haiku nennt sie). Liste vorgeben: „Weglassen: Preise, Zahlungen, Lieferantenthemen, Arbeitsschutz-Messwerte, Personal.“ Oder fragen: „Was hast du weggelassen?“ So macht es Opus von sich aus.
7. **Auch heikle Inhalte für das eigene Team wollen überlegt sein.** Sonnet schreibt dem Team ungefiltert „ein Schichtbetrieb könnte reichen“. Inhaltlich stimmt das, aber die Abwägung, ob man das so kommuniziert, nimmt die KI einem nicht ab.

**Bessere Folgeprompts für die Auswertung:**

```text
Fasse den Bericht für die Bediener und die Instandhaltung in Halle 3 in einfacher Sprache zusammen.
Kurze Sätze, erkläre jeden Fachbegriff in Klammern. Nur Punkte, die ihren Arbeitsalltag betreffen.
Schreib nichts, was nicht im Bericht steht.
```

```text
Schreib eine kurze Kundeninformation. Lass weg: Preise, Zahlungen, Einbehalt, Ersparnis,
Namen, Lieferantenthemen, offene Punkte, Messwerte zu Staub und Energie.
Mach keine Zusagen zu Lieferzeiten oder Qualität, die nicht wörtlich im Bericht stehen.
Liste danach auf, was du weggelassen hast und was ich vor dem Versand prüfen muss.
```

```text
Vergleiche deine Kundenfassung Satz für Satz mit dem Bericht:
Welche Aussage steht so nicht im Bericht oder klingt sicherer als dort?
```

---

## Gesprächsprotokolle

### Modell: Haiku

#### Nutzer 1

```text
Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.
```

#### Assistent 1

Die Faserlaser-Schneidanlage LS-3015 erfüllt laut dem Abnahmeprüfbericht PB-2024-017 (Entwurf) die wesentlichen Anforderungen aus Lastenheft und Kaufvertrag, denn die Maße liegen innerhalb der Toleranz, die technische Verfügbarkeit im Dauerlauf beträgt 96,2 % (gefordert: 95 %) und die Taktzeiten von Prüfteil A und B unterschreiten die zugesicherten Werte. Offen bzw. nicht erfüllt sind die Taktzeit für Prüfteil C (41 s statt 40 s), die Leistungsaufnahme im Schneidbetrieb (31 kW inklusive Absaugung statt unter 30 kW, eine getrennte Messung fehlt) und die Staubkonzentration beim Schneiden von verzinktem Blech (92 % des Richtwerts, knapp unter der Grenze). Bei verzinktem Material müssen die Schutzgläser häufiger gewechselt werden (rund 60 Euro je Stück, zwei auf Lager, Lieferzeit drei bis sechs Wochen), und die Kosten für weitere Schulungen sowie eine mögliche Verstärkung der Absaugung sind nicht beziffert, während die überschlägige Kostenersparnis gegenüber der Altanlage bei rund 85.000 Euro pro Jahr liegt. Termine: Das Software-Update 4.3 soll im Laufe des Quartals kommen, ein konkreter Termin ist nicht genannt, und die Wiederholungsmessung der Staubkonzentration ist nach drei Monaten fällig. Die Geschäftsführung muss entscheiden, ob die Anlage unter Vorbehalt abgenommen wird; die Fertigungstechnik empfiehlt dies mit einem Einbehalt von 5 % des Kaufpreises von der Schlusszahlung (30 %), bis Software-Update, Wartungsplan-Ergänzung und getrennte Leistungsmessung erledigt sind.

#### Nutzer 2

```text
Fasse den Bericht jetzt für das Montageteam in einfacher Sprache zusammen.
```

#### Assistent 2

Die neue Schneidanlage für Halle 3 ist im Test gut gelaufen. Die Teile sind sauber geschnitten und passen in den Maßen. Die Anlage lief fünf Tage im Dauerbetrieb und stand dabei insgesamt etwa 3 Stunden still.

Die Gründe für die Stillstände waren:
- Das Schutzglas war zweimal verschmutzt. Es musste gereinigt bzw. getauscht werden.
- Am automatischen Palettenwechsler war ein Endschalter falsch eingestellt. Der Servicetechniker hat ihn repariert.

Wichtig für euch:
- Bei verzinktem Blech muss das Schutzglas öfter gewechselt werden, als im Wartungsplan steht. Der Wartungsplan wird noch ergänzt.
- Ersatz-Schutzgläser sind nur zwei Stück auf Lager. Die Lieferzeit kann drei bis sechs Wochen dauern.
- Für Prüfteil C wird nach jedem Wechsel der Einstellungen eine Erstmusterprüfung empfohlen.
- Die Anlage braucht bald eine Ablage für Restgitter. Der neue Materialfluss ist noch nicht im Hallenplan eingezeichnet.
- Das Software-Update 4.3 kommt in den nächsten Wochen. Bis dahin müssen Schneidprogramme teilweise von Hand übertragen werden.
- Es sollen mindestens zwei weitere Personen geschult werden, damit es eine Vertretung gibt.

#### Nutzer 3

```text
Fasse den Bericht jetzt für einen Kunden zusammen – ohne interne Details.
```

#### Assistent 3

Die neue Laserschneidanlage LS-3015 in unserer Fertigung in Halle 3 wurde im Rahmen einer Abnahmeprüfung getestet. Die Prüfung hat ergeben, dass die Anlage die wesentlichen Anforderungen erfüllt: Die Schnittqualität und die Maßhaltigkeit liegen bei allen geprüften Teilen innerhalb der Toleranz, und die Anlage war im Dauerlauf zuverlässig verfügbar. Bei einzelnen Punkten, etwa der Taktzeit eines Teils, der Leistungsaufnahme und der Staubmessung bei verzinktem Material, gibt es noch Klärungsbedarf, der derzeit mit dem Hersteller abgestimmt wird. Ein Software-Update für die Steuerung ist angekündigt. Wir gehen davon aus, dass sich die Anlage nach Abschluss dieser Punkte wie vorgesehen in unsere Produktion einfügt.

---

### Modell: Sonnet

#### Nutzer 1

```text
Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.
```

#### Assistent 1

Die Laserschneidanlage LS-3015 erfüllt die wesentlichen Anforderungen aus Lastenheft und Kaufvertrag: Maßhaltigkeit und Schnittqualität liegen bei allen drei Prüfteilen innerhalb der Toleranz, die Verfügbarkeit im Dauerlauf beträgt 96,2 % (gefordert: 95 %), und die Taktzeiten sind bei den zwei wichtigsten Serienteilen deutlich besser als zugesichert (Prüfteil C verfehlt sie mit 41 statt 40 Sekunden knapp). Die Fertigungstechnik erwartet gegenüber der Altanlage rund 45 % kürzere Bearbeitungszeiten, etwa 60 % weniger Energieverbrauch und eine jährliche Ersparnis von etwa 85.000 Euro, wobei Kosten für zusätzliche Schulungen, eine mögliche Verstärkung der Absaugung und höheren Schutzglasverbrauch (rund 60 Euro pro Stück) nicht enthalten sind. Offen sind die getrennt zu messende Leistungsaufnahme (31 kW gemessen, "unter 30 kW" angeboten), die Wiederholungsmessung der Staubkonzentration beim Schneiden von verzinktem Blech (derzeit 92 % des Richtwerts, Wiederholung nach drei Monaten gewünscht), der unvollständige Wartungsplan, das Software-Update 4.3 ohne konkreten Termin sowie die Schulung weiterer Bediener, die nicht im Kaufvertrag enthalten ist. Ersatzteile haben laut Hersteller derzeit eine Lieferzeit von drei bis sechs Wochen, und bei Abnahme wird die Schlusszahlung von 30 % des Kaufpreises fällig. Es ist eine Entscheidung nötig: Die Fertigungstechnik empfiehlt, die Anlage unter schriftlichem Vorbehalt abzunehmen (Update 4.3 mit verbindlichem Termin, ergänzter Wartungsplan, getrennte Leistungsmessung) und bis zur Erledigung 5 % des Kaufpreises von der Schlusszahlung einzubehalten.

#### Nutzer 2

```text
Fasse den Bericht jetzt für das Montageteam in einfacher Sprache zusammen.
```

#### Assistent 2

**Zusammenfassung für das Montageteam**

Wir haben eine neue Laserschneidanlage (Typ LS-3015) für Halle 3 bekommen. Sie ersetzt die alte Anlage von 2009. Die Anlage wurde zwei Wochen lang getestet.

**Was gut läuft:**
- Die Teile werden sauber und genau geschnitten. Alle gemessenen Maße liegen in der erlaubten Toleranz.
- Die Anlage schneidet schneller als die alte. Ein Schichtbetrieb könnte bald reichen, wo bisher zwei Schichten nötig waren.
- Sie braucht deutlich weniger Strom.
- Die Bedienung ist übersichtlich und auf Deutsch. Die Bediener kamen schnell damit zurecht.
- Die Sicherheitseinrichtungen (Türen, Not-Halt, Laserschutzfenster) funktionieren.

**Was noch nicht perfekt ist:**
- Bei dem dicken Winkel (8 mm Baustahl) bildet sich unten ein leichter Bart. Der Servicetechniker hat die Einstellungen verbessert. Das ist jetzt deutlich besser.
- Beim Schneiden von verzinktem Blech muss das Schutzglas öfter gewechselt werden als im Wartungsplan steht. Zwei Ersatzgläser sind auf Lager. Neue kommen vom Hersteller erst nach drei bis sechs Wochen.
- Beim Schneiden von verzinktem Blech ist die Staubbelastung knapp unter dem erlaubten Wert. Die Messung wird nach drei Monaten wiederholt.
- Die Programme aus dem ERP-System müssen zurzeit teilweise von Hand übertragen werden. Ein Software-Update soll das beheben, einen Termin gibt es aber noch nicht.
- Bisher sind nur zwei Kollegen geschult (Lukas Brandl und Mehmet Arslan). Für Vertretung und eine zweite Schicht brauchen wir mindestens zwei weitere.

**Wünsche aus dem Team und der Prüfung:**
- Eine Ablagefläche neben der Anlage für Restgitter.
- Nach jedem Wechsel der Einstellungen beim Winkel soll ein Erstmuster geprüft werden.
- Der neue Materialfluss in Halle 3 ist noch nicht im Hallenplan eingezeichnet.

**Wie geht es weiter?**
Die Geschäftsführung entscheidet, ob die Anlage abgenommen wird. Empfohlen wird eine Abnahme mit Vorbehalt: Der Hersteller muss noch einige Punkte erledigen.

#### Nutzer 3

```text
Fasse den Bericht jetzt für einen Kunden zusammen – ohne interne Details.
```

#### Assistent 3

**Zusammenfassung für Kunden**

Wir haben unsere Blechbearbeitung modernisiert und eine neue Faserlaser-Schneidanlage in Betrieb genommen. Sie ersetzt eine ältere Anlage, die nicht mehr wirtschaftlich zu betreiben war. In einer zweiwöchigen Abnahmeprüfung unter Serienbedingungen hat die Anlage die wesentlichen Anforderungen erfüllt.

- **Qualität:** Die geprüften Bauteile aus Edelstahl, verzinktem Stahlblech und Baustahl wurden sauber und maßhaltig gefertigt. Alle gemessenen Maße lagen innerhalb der vorgegebenen Toleranzen.
- **Leistung:** Die Bearbeitungszeiten sind deutlich kürzer als bisher. Das hilft uns, Aufträge zuverlässiger und zügiger abzuarbeiten.
- **Zuverlässigkeit:** Die Anlage lief im Dauertest stabil und lag über der geforderten Verfügbarkeit.
- **Sicherheit und Umwelt:** Die Sicherheitseinrichtungen funktionieren einwandfrei. Der Energieverbrauch ist deutlich niedriger als bei der bisherigen Anlage.

Einige Feinheiten werden in der Abschlussphase noch geklärt, unter anderem Software-Updates und ergänzende Dokumentation. Auf Ihre Aufträge und die Qualität Ihrer Teile haben diese Punkte nach aktuellem Stand keinen Einfluss.

---

### Modell: Opus

#### Nutzer 1

```text
Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.
```

#### Assistent 1

Die neue Faserlaser-Schneidanlage LS-3015 erfüllt laut Abnahmeprüfung die wesentlichen Anforderungen aus Lastenheft und Kaufvertrag: Alle Prüfteile liegen in der Toleranz, die Taktzeiten der beiden wichtigsten Serienteile liegen deutlich unter den zugesicherten Werten und die Verfügbarkeit im Dauerlauf erreicht 96,2 % (gefordert: 95 %). Noch offen sind die um eine Sekunde verfehlte Taktzeit bei Prüfteil C (41 statt 40 s), die Leistungsaufnahme (31 kW statt „unter 30 kW“, gemessen einschließlich Absaugung), eine Staubkonzentration von 92 % des internen Richtwerts bei verzinktem Blech, der unvollständige Wartungsplan zum Schutzglas, das noch fehlende Software-Update 4.3 und die Schulung weiterer Bediener. Die Fertigungstechnik schätzt die jährliche Ersparnis gegenüber der Altanlage auf etwa 85.000 Euro, dabei sind die Kosten für zusätzliche Schulungen (nicht im Kaufvertrag enthalten), mehr Schutzgläser (je ca. 60 Euro) und eine eventuell nötige Verstärkung der Absaugung nicht berücksichtigt. Zu den Terminen: Das Software-Update ist für dieses Quartal angekündigt, aber ohne festen Termin, die Staubmessung soll nach drei Monaten wiederholt werden, und Ersatzteile haben derzeit drei bis sechs Wochen Lieferzeit. Sie müssen über die formale Abnahme entscheiden, mit der die Gefahr übergeht und die Schlusszahlung von 30 % fällig wird; empfohlen wird eine Abnahme unter schriftlichem Vorbehalt (Update 4.3 zu einem verbindlichen Termin, Ergänzung des Wartungsplans, getrennte Leistungsmessung) mit einem Einbehalt von 5 % des Kaufpreises bis zur Erledigung.

#### Nutzer 2

```text
Fasse den Bericht jetzt für das Montageteam in einfacher Sprache zusammen.
```

#### Assistent 2

**Die neue Laseranlage in Halle 3 – das Wichtigste für euch**

**Was ist passiert?**
In Halle 3 steht eine neue Laser-Schneidanlage (LS-3015). Sie ersetzt die alte Anlage. Sie schneidet die Blechteile für die Gehäuse von SG-40 und SG-60. Die Anlage wurde zwei Wochen lang getestet.

**Was heißt das für die Teile?**
- Die Teile sind genau. Alle gemessenen Maße liegen in der erlaubten Toleranz.
- Die Kanten bei der Frontblende SG-40 (Edelstahl) und der Seitenwand SG-60 (verzinktes Blech) sind sehr gut und ohne Grat.
- Beim dicken Montagewinkel (8 mm Stahl) gab es an der Unterseite zuerst etwas Bart. Mit neuen Einstellungen ist das deutlich weniger geworden. Ganz weg ist es laut Bericht nicht.
- Die Teile werden schneller fertig als mit der alten Anlage, ungefähr 45 % schneller.

**Was ist noch nicht fertig?**
- Bei der Übergabe der Aufträge aus dem ERP-System gibt es noch einen Fehler. Ein Software-Update soll kommen, einen festen Termin gibt es aber noch nicht. Bis dahin werden manche Schneidprogramme von Hand übertragen.
- Die Qualitätssicherung schlägt vor, den Montagewinkel nach jeder Änderung der Einstellungen zuerst als Muster zu prüfen.
- Der neue Materialfluss in Halle 3 ist noch nicht im Hallenplan eingezeichnet.

**Gut zu wissen**
- Die Anlage ist sicher: Die Kabine ist geschlossen, Türsicherungen und Not-Halt funktionieren.
- Die alte Anlage bleibt erst einmal als Reserve da, bis sie verkauft wird.

Hinweis: Im Bericht steht nichts direkt über die Arbeit in der Montage. Ob es dort Änderungen gibt, kann ich daraus nicht sagen. Wenn ihr Fragen zu den Teilen habt, fragt am besten bei der Fertigungstechnik oder der Qualitätssicherung nach.

#### Nutzer 3

```text
Fasse den Bericht jetzt für einen Kunden zusammen – ohne interne Details.
```

#### Assistent 3

**Vorschlag für eine Kundeninformation**

Betreff: Neue Laserschneidanlage für die Gehäusefertigung SG-40 und SG-60

Sehr geehrte Damen und Herren,

wir haben unsere Blechbearbeitung modernisiert: Eine neue Faserlaser-Schneidanlage ersetzt seit Kurzem unsere bisherige Anlage. Auf ihr fertigen wir die Gehäuseteile aus Edelstahl und verzinktem Stahlblech für die Produktlinien SG-40 und SG-60.

Vor der Inbetriebnahme haben wir die Anlage zwei Wochen lang geprüft, unter anderem in einem fünftägigen Dauerlauf unter Serienbedingungen. Dabei haben wir die Maße der Teile mit einem Koordinatenmessgerät kontrolliert. Alle geprüften Maße lagen innerhalb der festgelegten Toleranzen, und die Schnittkanten sind sehr sauber.

Durch die neue Anlage werden die Teile deutlich schneller bearbeitet, und die neue Software nutzt das Material besser aus.

Mit freundlichen Grüßen
[Name, Firma]

---

**Bewusst weggelassen habe ich:** Kaufpreis, Zahlungen und Einbehalt, die Abnahme unter Vorbehalt, die offenen Punkte mit dem Hersteller (Software-Update, Wartungsplan, Leistungsmessung), Messwerte zu Staub und Energie, Stillstände, Namen von Mitarbeitenden, Schulungsbedarf und die Ersparnis.

**Bitte vor dem Versand prüfen:**
- Die Anlage ist bisher nur als Entwurf zur Abnahme unter Vorbehalt empfohlen. Wenn die Abnahme noch nicht erfolgt ist, sollte „seit Kurzem im Einsatz“ vorsichtiger formuliert werden.
- Über Liefertermine, Preise oder Qualitätszusagen an Kunden steht nichts im Bericht. Deshalb habe ich dazu nichts geschrieben.
- Dem Bericht zufolge sind alle Namen, Firmen und Zahlen fiktiv (Übungsmaterial). Für eine echte Kundeninformation müssten die Angaben angepasst werden.
