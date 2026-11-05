# Testlauf: Übung 3 / Station A Basis – Prüfbericht in 5 Sätzen für die GF

**Herkunft:** Station A, Stufe „Basis“ aus [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#station-a-langen-bericht-zusammenfassen) (Block 5). Material: [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md) (Abnahmeprüfbericht LS-3015, PB-2024-017). Zugehörige Lösungshinweise: [Trainer-Loesungshinweise.md – Station A](../06_Uebungen/Trainer-Loesungshinweise.md#station-a-prüfbericht-zusammenfassen) („Kernfakten“, „Versteckte Prüfpunkte“, „Woran du ein gutes Ergebnis erkennst“, „Typische Stolpersteine“).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt (jeweils in einem neuen Chat, Bericht angehängt bzw. eingefügt):**

```text
Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.
```

**Was laut Material herauskommen soll:** Genau 5 Sätze mit Ergebnis, Aufwand/Kosten, Terminen und einer klaren Entscheidungsfrage. Enthalten sein sollen: Die GF muss über die formale Abnahme entscheiden (Schlusszahlung 30 %), Empfehlung **Abnahme unter Vorbehalt** mit drei Bedingungen (Update 4.3 bis zu einem verbindlichen Termin, Wartungsplan Schutzglas, getrennte Leistungsmessung) und **Einbehalt 5 % des Kaufpreises**. Möglich sind: Verfügbarkeit 96,2 %, ca. 85.000 €/Jahr Ersparnis, Taktzeit C mit 41 s knapp verfehlt. Es darf **kein Eurobetrag** für Einbehalt oder Schlusszahlung vorkommen (der Kaufpreis steht nicht im Bericht) und **kein fester Termin** für Update 4.3 (im Bericht steht nur „im Laufe des Quartals“). Die Zusammenfassung soll nicht übermäßig positiv sein. Danach Prüfschritt: drei Aussagen im Original suchen.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Genau 5 Sätze? | **ja** | **ja** (aber Schachtelsätze, s. u.) | **nein**: Überschrift + 5 nummerierte Absätze mit zusammen 8 Sätzen, Absatz 3 als Aufzählung mit 5 Punkten |
| Länge gesamt / längster Satz (Wörter, per `python3`) | ca. 175 / 41 | ca. 245 / 57 | ca. 310 (ohne Überschrift) / 57 (Absatz 4; Absatz 3 mit Aufzählung: 78) |
| Für die GF in kurzer Zeit lesbar? | mäßig, alle Sätze 25–41 Wörter | schlecht, drei von fünf Sätzen mit über 50 Wörtern, Detailballast (Altanlage, Händler) | gut gegliedert, aber das Format ist eine Liste statt 5 Sätze |
| Entscheidung nötig (formale Abnahme) | ja, Satz 5 | ja, Satz 5 („Ja, eine Entscheidung ist nötig“) | ja, fett hervorgehoben, inkl. Gefahrübergang |
| Schlusszahlung 30 % | ja | ja | ja |
| Empfehlung „Abnahme unter Vorbehalt“ | ja | ja („schriftlicher Vorbehalt“) | ja („schriftlicher Vorbehalt“) |
| Drei Bedingungen vollständig | 3 von 3 genannt, aber „verbindlicher Termin“ für Update 4.3 fehlt | 3 von 3, korrekt | 3 von 3, korrekt |
| Einbehalt 5 % **des Kaufpreises** | **ungenau**: „Einbehalt von 5 % von der Schlusszahlung (30 % des Kaufpreises)“, lässt sich als 5 % von 30 % lesen | korrekt („5 % des Kaufpreises von der Schlusszahlung“) | korrekt („5 % des Kaufpreises von der Schlusszahlung“) |
| Verfügbarkeit 96,2 % | ja | ja | ja |
| Ersparnis ca. 85.000 €/Jahr + was nicht enthalten ist | ja, beides | ja, beides | ja, beides |
| Taktzeit C (41 s statt 40 s) | ja | ja | ja |
| Offene Punkte laut Abschnitt 7 (Taktzeit C, Leistung, Staub, Wartungsplan, Update, Schulung) | 5 von 6: Schulung weiterer Bediener fehlt als offener Punkt (nur als Kostenposten) | 6 von 6 | 6 von 6 |
| Bonus: Schutzglas-Lieferzeit 3–6 Wochen | nein (nur in Haikus eigener Prüfliste) | ja (aber ohne „2 Stück auf Lager“) | ja, inkl. „zwei auf Lager“ |
| Bonus: Widerspruch Schlitzbreite (0,13 mm bei ±0,10 mm) | **nein**, übernimmt „innerhalb der Toleranz“ | **nein**, übernimmt „bei allen drei Prüfteilen in der Toleranz“ | **nein**, übernimmt „bei allen drei Prüfteilen innerhalb der Toleranz“ |
| Erfundener Eurobetrag für Einbehalt/Schlusszahlung? | nein | nein | nein |
| Erfundener Termin für Update 4.3? | nein („ein konkreter Termin fehlt“) | nein („noch nicht terminiert“) | nein („nur ‚im Laufe des Quartals‘“) |
| Übermäßig positiv? | nein | nein | nein |
| Sonstiges Erfundenes? | nein (kleine Umdeutungen, s. u.) | nein | nein |

**Kurz:** Inhaltlich sind alle drei Antworten solide. Kein Modell erfindet einen Eurobetrag oder einen Termin, alle nennen Empfehlung, Bedingungen und die Entscheidung der GF. Die vom Material angekündigten Halluzinationen treten in der **Basis-Stufe nicht auf**. Die Schwächen liegen woanders: **Format** (Opus hält „genau 5 Sätze“ nicht ein, Haiku und Sonnet halten es nur mit Monstersätzen ein), eine **leicht verdrehte Bezugsgröße** beim Einbehalt (Haiku) und der **übernommene Fehler** des Berichts zur Maßhaltigkeit (alle drei).

---

## Gefundene Fehler mit Beleg

1. **Alle drei – Fehler aus dem Bericht ungeprüft übernommen (Schlitzbreite).** Alle schreiben sinngemäß, die Maßhaltigkeit liege bei allen Prüfteilen in der Toleranz. Das steht so in Abschnitt 7 des Berichts. Die Messwerttabelle in Abschnitt 4 widerspricht aber: „B – Seitenwand 3 mm | Schlitzbreite | 4,00 | ±0,10 | 4,07 | **0,13** | i. O.“ Nachgerechnet per `python3`: Von den 12 Zeilen überschreitet genau diese eine die Toleranz (0,13 > 0,10). Das ist kein Fehler der Modelle im engeren Sinn, aber genau der versteckte Prüfpunkt aus den Lösungshinweisen: **Die Zusammenfassung glaubt dem Fazit und rechnet nicht nach.** Bestätigt die Lösungshinweise („Kaum ein KI-Assistent findet das von selbst“).
2. **Opus – Formatvorgabe nicht eingehalten.** Gefordert: „genau 5 Sätze“. Geliefert: eine Überschrift, fünf nummerierte Absätze mit insgesamt 8 Sätzen (Absatz 1: 2, Absatz 2: 2, Absatz 3: 1 Einleitung + Aufzählung mit 5 Punkten, Absatz 4: 1 langer Satz mit Semikolons, Absatz 5: 2). Opus legt „5 Sätze“ offenbar als „5 Punkte“ aus. Das ist der Stolperstein „Mehr als 5 Sätze“ aus den Lösungshinweisen, hier ausgerechnet beim stärksten Modell.
3. **Haiku – Bezugsgröße beim Einbehalt unscharf.** Haiku: „… ob sie einen Einbehalt von 5 % von der Schlusszahlung (30 % des Kaufpreises) vereinbart.“ Bericht, Abschnitt 7: „Einbehalt von **5 % des Kaufpreises** von der Schlusszahlung“. Wer Haikus Satz wörtlich nimmt, rechnet 5 % von 30 % = **1,5 % des Kaufpreises** (per `python3` nachgerechnet) statt 5 %. Kein erfundener Betrag, aber eine Verdrehung, die man nur beim Prüfschritt („Steht es dort genau so?“) bemerkt.
4. **Haiku – Bedingung verkürzt.** Bei den drei Vorbehaltspunkten steht nur „Software-Update“. Im Bericht heißt die Bedingung: Update 4.3 „bis zu einem **verbindlichen Termin**“. Gerade der fehlende Termin ist der Kern der Bedingung. Sonnet und Opus nennen ihn.
5. **Haiku – kleine Umdeutungen.** (a) „für das **laufende** Quartal angekündigt“: Im Bericht steht „im Laufe des Quartals“, welches Quartal gemeint ist, bleibt offen. (b) „den der Hersteller schriftlich zusichern soll“: Laut Bericht soll der **Vorbehalt** schriftlich festhalten, was der Hersteller liefert. Das ist sinngemäß ähnlich, aber nicht wörtlich. (c) Die Schulung weiterer Bediener taucht nur als nicht eingerechneter Kostenposten auf, nicht als offener Punkt (Bericht Abschnitt 3.6 und 7).
6. **Sonnet – formal 5 Sätze, aber Ziel verfehlt.** Satz 1 (Ergebnis, 57 Wörter), Satz 3 (offene Punkte, 56) und Satz 5 (Entscheidung, 56) sind jeweils länger als 50 Wörter (per `python3` gezählt). Satz 4 (Ersatzteil-Lieferzeit, Verkauf der Altanlage, Händlerinteresse) ist für die Entscheidung nebensächlich. Fakten stimmen alle (Abschnitte 3.3 und 5). Das ist der Stolperstein „sehr lange Schachtelsätze“.
7. **Keine Halluzinationen bei Beträgen und Terminen.** Alle drei vermeiden einen Eurobetrag für Einbehalt oder Schlusszahlung und einen festen Termin für Update 4.3. Alle Zahlen (96,2 %, 95 %, 41/40 s, 31 kW, 92 %, 85.000 €, ca. 60 € Schutzglas, 3–6 Wochen, 45 %, 60 %, 30 %, 5 %) stehen so im Bericht.
8. **Randnotiz zur Quelle (nicht Modellfehler):** Verfügbarkeit nachgerechnet: Stillstände 35 + 130 + 20 = 185 min bei 80 h = 4.800 min → (4.800 − 185) / 4.800 = **96,15 %**. Der Bericht schreibt „rund 96,2 %“, kaufmännisch gerundet wären es 96,1 %. Für die Aussage („Anforderung ≥ 95 % erfüllt“) ist das unerheblich. Es zeigt aber, dass auch das Original nicht fehlerfrei ist und Modelle Zahlen ungeprüft übernehmen.
9. **Haiku – Testartefakt, kein Modellverhalten.** Am Ende der Haiku-Antwort stehen eine Liste „Erwartete Ergebnisse (Prüfpunkte für die Gegenprüfung)“ und ein Hinweis zu ultracode/Subagenten. Das kommt aus der Testumgebung und würde in [KI-TOOL] nicht erscheinen. Es ist unten vollständig enthalten, zählt aber nicht zur Bewertung.

---

## Lehren für die Auswertung

- **Die Übung funktioniert, aber der „Aha“-Moment kommt nicht von selbst.** Mit diesem Prompt liefern gute Modelle eine sachlich weitgehend korrekte Zusammenfassung. Wer erwartet, in der Basis-Stufe einen erfundenen Eurobetrag oder Termin zu sehen, wird meist enttäuscht. Die Halluzination zeigt sich zuverlässiger erst bei der gezielten Frage aus „Für Schnelle“: „Wie viel Euro behalten wir als Einbehalt zurück?“
- **Der stärkste Beleg für „immer prüfen“ ist die Schlitzbreite.** Alle drei Modelle übernehmen „alle Maße in Toleranz“. Zeigen Sie in der Auswertung Abschnitt 4, Zeile „Schlitzbreite“: 0,13 mm bei ±0,10 mm, trotzdem „i. O.“. Lehre: **Die KI fasst zusammen, was im Text steht – auch wenn der Text sich selbst widerspricht.** Mit dem Musterprompt „Rechne jede Zeile einzeln nach“ lässt sich das live nachholen.
- **„Steht es dort genau so?“ lohnt sich.** Haikus „5 % von der Schlusszahlung“ klingt richtig, ist aber eine andere Größe (1,5 % statt 5 % des Kaufpreises). Gute Übung für den Prüfschritt: Zahl im Original suchen (Strg + F „5 %“) und den **Bezug** prüfen, nicht nur die Zahl.
- **Formatvorgaben werden unterschiedlich ernst genommen.** Opus macht eine gegliederte Liste mit 8 Sätzen, Sonnet hält 5 Sätze mit Bandwurmsätzen ein. Beides ist für eine GF-Mail nicht direkt nutzbar. Nachsteuern wie in den Lösungshinweisen: „Genau 5 Sätze, je höchstens 20 Wörter, keine Aufzählung, keine Überschrift.“ Gute Diskussion: Was ist für die GF wirklich hilfreicher – 5 Sätze oder 5 Stichpunkte?
- **Vollständigkeit unterscheidet sich.** Nur Opus nennt „zwei Schutzgläser auf Lager“ zusammen mit der Lieferzeit, also das versteckte Stillstandsrisiko. Haiku lässt die Schulung als offenen Punkt weg. Vergleich in der Gruppe: „Welche offenen Punkte hat Ihre Zusammenfassung – und welche fehlen?“
- **Kein Modell ist übermäßig positiv.** Der Stolperstein „Zu positiv“ trat hier nicht auf. Er kann bei anderen Tools oder bei Upload-Problemen (nur Anfang gelesen) trotzdem vorkommen. Kontrollfrage: „Was steht im letzten Abschnitt?“

---

## Gesprächsprotokolle

### Haiku

**Nutzer 1**

```text
Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.
```

**Assistent 1**

Die Fertigungstechnik empfiehlt, die neue Laserschneidanlage LS-3015 unter Vorbehalt abzunehmen, da sie die wesentlichen Anforderungen aus Lastenheft und Kaufvertrag erfüllt, Schnittqualität und Maßhaltigkeit innerhalb der Toleranz liegen und die technische Verfügbarkeit im Dauerlauf mit 96,2 % die geforderten 95 % übertrifft. Offen sind die Taktzeit für Prüfteil C (41 statt 40 Sekunden), die nicht getrennt gemessene Leistungsaufnahme (31 kW statt unter 30 kW, inklusive Absaugung) und eine Wiederholungsmessung der Staubkonzentration beim Schneiden von verzinktem Blech, die nach drei Monaten fällig ist. Laut Bericht ergibt sich eine jährliche Kostenersparnis von etwa 85.000 Euro, wobei zusätzliche Schulungen, eine mögliche Verstärkung der Absaugung und höhere Verbrauchskosten für Schutzgläser (rund 60 Euro je Stück) nicht enthalten sind. Das Software-Update 4.3 wurde für das laufende Quartal angekündigt, ein konkreter Termin fehlt, und der Wartungsplan muss um das häufigere Wechselintervall des Schutzglases ergänzt werden. Die Geschäftsführung muss entscheiden, ob sie unter diesem Vorbehalt abnimmt, den der Hersteller schriftlich zusichern soll (Software-Update, Wartungsplan, getrennte Leistungsmessung), und ob sie einen Einbehalt von 5 % von der Schlusszahlung (30 % des Kaufpreises) vereinbart.

---

**Erwartete Ergebnisse (Prüfpunkte für die Gegenprüfung):**
- Genau 5 Sätze, auf Deutsch, ohne Aufzählung.
- Ergebnis: Anlage erfüllt die wesentlichen Anforderungen, Abnahme unter Vorbehalt empfohlen.
- Aufwand/Kosten: 85.000 Euro jährliche Ersparnis; nicht enthalten sind Schulung, Absaugung, Schutzgläser; Schlusszahlung 30 %; Einbehalt 5 % vorgeschlagen.
- Termine: Software-Update 4.3 "im Laufe des Quartals" ohne konkreten Termin; Wiederholungsmessung nach drei Monaten; Ersatzteil-Lieferzeit 3 bis 6 Wochen (im Satz nicht ausdrücklich genannt).
- Entscheidung: ja, Geschäftsführung muss über Abnahme unter Vorbehalt und Einbehalt entscheiden.
- Keine Erfindungen: keine Namen, Zahlen oder Termine, die nicht im Bericht stehen.

Hinweis: Die angeforderte Gegenprüfung mit anderen Modellen (ultracode, Sonnet, Haiku oder Opus) konnte ich aus diesem Subagenten nicht ausführen. Dafür fehlt mir ein passendes Werkzeug, und die Aufgabe erlaubt nur das Lesen der Datei.

### Sonnet

**Nutzer 1**

```text
Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.
```

**Assistent 1**

Die neue Laserschneidanlage LS-3015 erfüllt die wesentlichen Vorgaben aus Lastenheft und Kaufvertrag: Schnittqualität und Maßhaltigkeit liegen bei allen drei Prüfteilen in der Toleranz, die Verfügbarkeit im Dauerlauf beträgt 96,2 % (gefordert: 95 %), und die Taktzeiten liegen bei den Prüfteilen A und B unter den zugesicherten Werten, bei Prüfteil C mit 41 statt 40 Sekunden knapp darüber. Die Fertigungstechnik erwartet gegenüber der Altanlage eine jährliche Ersparnis von etwa 85.000 Euro (rund 45 % kürzere Bearbeitungszeit, rund 60 % weniger Energieverbrauch, weniger Materialverbrauch), wobei zusätzliche Schulungen, eine mögliche Verstärkung der Absaugung und der höhere Schutzglasverbrauch (ca. 60 Euro pro Stück) darin nicht enthalten sind. Offen sind die nicht getrennt gemessene Leistungsaufnahme (31 statt unter 30 kW, inklusive Absaugung), die Wiederholungsmessung der Staubkonzentration bei verzinktem Blech (derzeit 92 % des Richtwerts, Wiederholung nach drei Monaten gewünscht), das noch nicht terminierte Software-Update auf Version 4.3, der ergänzungsbedürftige Wartungsplan und die Schulung von mindestens zwei weiteren Bedienern, die nicht im Kaufvertrag enthalten ist. Ersatzteile aus dem Herstellerlager haben derzeit eine Lieferzeit von drei bis sechs Wochen, und die Altanlage soll nach der Abnahme verkauft werden, wofür bereits ein Händler Interesse gezeigt hat. Ja, eine Entscheidung ist nötig: Die Geschäftsführung soll über die Abnahme befinden, und die Fertigungstechnik empfiehlt eine Abnahme unter schriftlichem Vorbehalt (Software-Update 4.3 zu einem verbindlichen Termin, Ergänzung des Wartungsplans, getrennte Leistungsmessung) mit einem Einbehalt von 5 % des Kaufpreises von der Schlusszahlung, die mit der Abnahme in Höhe von 30 % des Kaufpreises fällig würde.

### Opus

**Nutzer 1**

```text
Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.
```

**Assistent 1**

**Zusammenfassung Abnahmeprüfbericht Laserschneidanlage LS-3015 (PB-2024-017)**

1. Laut Bericht erfüllt die neue Faserlaser-Schneidanlage LS-3015 die wesentlichen Anforderungen aus Lastenheft und Kaufvertrag. Schnittqualität und Maßhaltigkeit sind bei allen drei Prüfteilen innerhalb der Toleranz, die technische Verfügbarkeit im Dauerlauf liegt bei 96,2 % (gefordert: mindestens 95 %), und die Taktzeiten der beiden wichtigsten Serienteile liegen deutlich unter den zugesicherten Werten.

2. Gegenüber der alten CO₂-Anlage verkürzt sich die Bearbeitungszeit um rund 45 %, sodass voraussichtlich ein Einschichtbetrieb reicht, und der Energieverbrauch sinkt um rund 60 %. Die Fertigungstechnik schätzt überschlägig eine jährliche Ersparnis von etwa 85.000 Euro, darin fehlen aber die Kosten für weitere Schulungen, eine eventuell nötige Verstärkung der Absaugung und den höheren Verbrauch an Schutzgläsern.

3. Noch offen oder nur knapp erreicht sind diese Punkte:
   - die Taktzeit bei Prüfteil C (41 s statt höchstens 40 s),
   - die Leistungsaufnahme (31 kW einschließlich Absaugung statt „unter 30 kW“; eine getrennte Messung fehlt),
   - die Staubkonzentration bei verzinktem Blech (92 % des internen Richtwerts),
   - der Wartungsplan, in dem das häufigere Wechseln des Schutzglases noch fehlt,
   - die Schulung von mindestens zwei weiteren Bedienern, die nicht im Kaufvertrag enthalten ist und gesondert beauftragt werden muss.

4. Zu den Terminen: Das Software-Update 4.3, das einen Fehler bei der Übergabe von Auftragsdaten aus dem ERP-System behebt, ist nur „im Laufe des Quartals“ angekündigt, ohne konkreten Termin; die Fachkraft für Arbeitssicherheit möchte die Staubmessung nach drei Monaten wiederholen, und für Schutzgläser (je ca. 60 Euro, zwei auf Lager) beträgt die Lieferzeit derzeit drei bis sechs Wochen.

5. **Eine Entscheidung ist nötig:** Die Geschäftsführung muss über die formale Abnahme entscheiden, mit der die Gefahr auf das Unternehmen übergeht und die Schlusszahlung von 30 % des Kaufpreises fällig wird. Die Fertigungstechnik empfiehlt eine Abnahme unter schriftlichem Vorbehalt (verbindlicher Termin für Update 4.3, ergänzter Wartungsplan, getrennte Messung der Leistungsaufnahme) und bis zur Erledigung einen Einbehalt von 5 % des Kaufpreises von der Schlusszahlung.
