# Testlauf: Übung 4 / Rolle Einkauf – Mahnung wegen Lieferverzug an Lieferanten

**Herkunft:** [Übung 4: Deine eigene Aufgabe](../06_Uebungen/Uebung_4_Eigene_Aufgabe.md), Ideenliste „Einkauf: freundliche, aber bestimmte Mahnung wegen Lieferverzug“, Prompt nach dem Baukasten-Beispiel aus Schritt 3, Iterationen mit den Musterformulierungen aus Schritt 4 · Abgleich mit [Trainer-Lösungshinweise, Übung 4](../06_Uebungen/Trainer-Loesungshinweise.md#übung-4-eigene-aufgabe)

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Gesprächsverlauf (für alle Modelle gleich):**

1. Baukasten-Prompt (Rolle – Kontext – Aufgabe – Format – Beispiel + „stell mir zuerst Rückfragen“)
2. Antwort auf Rückfragen: Platzhalter [BESTELLNUMMER], [ANSPRECHPARTNER], [MEIN NAME]
3. „Kürzer, bitte – maximal die Hälfte.“
4. „Punkt 3 stimmt so nicht. Richtig ist: … spätestens Mittwoch in KW 22 …“
5. „Gib mir drei unterschiedliche Varianten, damit ich auswählen kann.“

**Ziel laut Material:** Eigene wiederkehrende Aufgabe mit dem Baukasten bearbeitet, Daten-Ampel grün (anonymisiert), versandfähiger Entwurf, mindestens zwei Iterationen, gespeicherter Prompt, ehrlich ausgefülltes Bewertungsraster.

**Soll (Fakten aus dem Prompt):** 2.000 Gehäusedeckel; zweimal verschoben; zugesagt KW 19, jetzt KW 21; Bedarf spätestens Ende KW 22 (ab Turn 4: **Mittwoch KW 22**); verbindlicher Termin bis Freitag; Frage nach Teillieferung; max. 120 Wörter, Betreff, Sie-Form; keine erfundene Bestellnummer, kein erfundener Name.

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Daten-Ampel grün (Lieferant X, keine Preise, keine Namen) | ja | ja | ja |
| Turn 1: Rückfragen | 3 sinnvolle (Bestellnr., Ansprechpartner, Unterschrift) | 6 (zusätzlich AB-Nummer, Konsequenzen, Datum Freitag, Mindestmenge Teillieferung) | 5 (zusätzlich Datum Freitag, Konsequenzen), Angebot „sonst Platzhalter“ |
| Turn 2: Betreff, Sie-Form | ja | ja | ja (Betreff recht lang) |
| Turn 2: Länge ≤ 120 Wörter (nachgezählt) | 83 | 76 (behauptet „ca. 85“) | 90 (behauptet „ca. 95“) |
| Turn 2: alle Fakten korrekt (2.000, 2× verschoben, KW 19 → 21, Ende KW 22, Freitag, Teillieferung) | ja | ja | ja |
| Turn 2: Platzhalter statt Erfundenem | ja | ja | ja |
| Turn 2: Beispielsatz übernommen | wörtlich | wörtlich | wörtlich |
| Turn 3: „max. die Hälfte“ (Verhältnis nachgezählt) | 49/83 = 59 % – nicht erfüllt | 39/76 = 51 % – knapp, ≈ erfüllt | 54/90 = 60 % – nicht erfüllt |
| Turn 3: Kern erhalten | ja, aber KW 19 → 21 entfällt | ja, aber Bestellnr. im Text und Kundenauftrag entfallen | ja, vollständig |
| Turn 4: Termin auf Mittwoch KW 22 korrigiert | ja | ja | ja |
| Turn 4: Umgang mit „Punkt 3“ (es gibt keine Punkte) | stillschweigend richtig gedeutet | Hinweis „keine nummerierten Punkte“, Annahme offengelegt | Hinweis + Bitte um Rückmeldung, falls anders gemeint |
| Turn 4: Zusatznutzen | – | Tipp „Wareneingang bei uns“ ausdrücklich nennen | Tipp konkretes Datum statt KW |
| Turn 5: drei klar unterschiedliche Varianten | ja (sachlich / partnerschaftlich / knapp) | ja, am deutlichsten (freundlich / bestimmt / lösungsorientiert) + Auswahlempfehlung | teilweise – Variante 1 und 3 inhaltlich sehr ähnlich; + Empfehlung |
| Turn 5: alle mit Mittwoch KW 22 | ja | ja | ja |
| Turn 5: Fakten vollständig in allen Varianten | B ohne „zweimal verschoben“ | ja | ja (V2 ohne KW-Angaben, aber „nach zwei Verschiebungen“) |
| Versandfähig nach Platzhalter-Ersetzung | ja (Anrede-Konstrukt „z. H.“ glätten) | ja (V-C-Satz „Hilft eine Teillieferung …“ glätten) | ja („Sehr geehrte/r [ANSPRECHPARTNER]“ anpassen) |
| **Gesamt** | gut, knapp, kein Kommentar zu Unklarheiten | **am besten für die Übung** – Hinweise, klare Varianten; Wortzahl-Angaben aber falsch | sehr sauber, transparent; Kürzung zu schwach, Varianten ähnlich |

Wortzahlen per Python (`len(text.split())`, Anrede bis Signatur, ohne Betreff) nachgezählt.

**Bewertungsraster (Schritt 5) – so würde eine Teilnehmerin es typischerweise ausfüllen:**

| Kriterium | Einschätzung |
|---|---|
| Zeit gespart | 4 – Mail selbst schreiben ca. 10 Min., mit KI inkl. Prompt und Prüfen ca. 5–7 Min.; beim zweiten Mal mit gespeichertem Prompt deutlich schneller |
| Qualität | 4–5 – alle Entwürfe nach Platzhalter-Ersetzung versandfähig |
| Korrektheit | 5 bei Fakten (nichts erfunden), aber Längenvorgaben und Selbstauskünfte zur Wortzahl stimmen nicht – nachzählen |
| Risiken | gering – keine Zusagen, keine Drohungen; Platzhalter vor dem Versand ersetzen |
| Wiederverwendbar | ja – Prompt mit Platzhaltern für Lieferant, Menge, Teil, KW |

## Gefundene Fehler mit Beleg

Kein Modell hat eine Zahl, eine Bestellnummer oder einen Namen erfunden; alle Fakten (2.000 Gehäusedeckel, KW 19/21/22, Freitag, Teillieferung) sind korrekt wiedergegeben. Die Abweichungen liegen bei Längenvorgaben, Selbstauskünften und Kleinigkeiten:

1. **„Maximal die Hälfte“ wird von Haiku und Opus nicht eingehalten.** Nachgezählt: Haiku 83 → 49 Wörter (59 %), Opus 90 → 54 Wörter (60 %). Nur Sonnet kommt mit 76 → 39 (51 %) etwa auf die Hälfte.
2. **Falsche Wortzahl-Angaben.** Sonnet Turn 2: „(ca. 85 Wörter im Mailtext)“ – tatsächlich 76. Sonnet Turn 3: „ca. 40 Wörter im Mailtext, unter der Hälfte der 120 Wörter“ – bezieht „Hälfte“ auf das Limit (120), nicht auf den eigenen Entwurf (76); das war nicht gefragt. Opus Turn 2: „ca. 95 Wörter“ – tatsächlich 90; Turn 3 „ca. 50“ – tatsächlich 54; Turn 5 „je ca. 50–60 Wörter“ – tatsächlich 44 / 58 / 56. Die Abweichungen sind klein, zeigen aber: KI-Angaben zur eigenen Länge sind Schätzungen.
3. **Information geht beim Kürzen verloren.** Haiku Turn 3 streicht „KW 19 → KW 21“ (nur noch „zweimal verschoben“); Sonnet Turn 3 streicht die Bestellnummer aus dem Mailtext („unsere 2.000 Gehäusedeckel wurden … verschoben“ – Bestellnummer nur noch im Betreff) und den Kundenauftrag. Haiku Variante B nennt die zwei Verschiebungen gar nicht mehr.
4. **„Punkt 3“ passt nicht zum Text.** Keiner der gekürzten Entwürfe hat nummerierte Punkte. Sonnet und Opus sagen das offen („Mein Entwurf hatte keine nummerierten Punkte“ / „Der Text hat keine nummerierten Punkte“) und legen ihre Annahme offen; Haiku korrigiert kommentarlos. Alle treffen die richtige Stelle – weil der Korrektursatz selbst eindeutig ist („nicht erst Ende KW 22, sondern Mittwoch“).
5. **Sprachliche Unebenheiten (vor dem Versand glätten):**
   - Haiku Turn 2: „Sehr geehrte Damen und Herren, / z. H. [ANSPRECHPARTNER],“ – „z. H.“ gehört ins Adressfeld, nicht unter die Anrede.
   - Opus: „Sehr geehrte/r [ANSPRECHPARTNER]“ – ergibt nach Ersetzung „Sehr geehrte/r Frau Müller“; korrekt wäre „Sehr geehrte Frau …/Sehr geehrter Herr …“.
   - Sonnet Turn 3–5: „unsere 2.000 Gehäusedeckel wurden … verschoben“ – verschoben wurde die Lieferung, nicht die Teile.
   - Sonnet Variante C: „Hilft eine Teillieferung, die Sie früher liefern können?“ – gemeint ist „Können Sie vorab eine Teilmenge liefern?“.
   - Opus Turn 2: „Falls eine vollständige Lieferung bis dahin nicht möglich ist“ – „bis dahin“ ist mehrdeutig (Freitag oder KW 22?).
6. **Opus: Varianten 1 und 3 kaum unterschiedlich.** Beide: Bestellung, zweimal verschoben, Mittwoch KW 22, Termin bis Freitag, Teillieferung – Variante 3 ergänzt nur den Kundenauftrag und „Dringend“ im Betreff. Die Aufgabe „drei unterschiedliche Varianten“ ist damit nur teilweise erfüllt.
7. **Kleinigkeit Sonnet Variante B:** „können wir keine weitere Verzögerung akzeptieren“ – ist bestimmt, aber härter als „freundlich, aber bestimmt“ aus dem Ausgangsprompt; als bewusst gekennzeichnete „bestimmte“ Variante vertretbar.

## Lehren für die Auswertung

- **Die Übung funktioniert wie gedacht.** Mit dem Baukasten-Prompt liefern alle drei Modelle im ersten Entwurf eine versandfähige, sachlich korrekte Mahnung mit Platzhaltern. Die Iterationen aus Schritt 4 zeigen sichtbare Wirkung – gut für die 2-Minuten-Vorstellung.
- **„Stell mir zuerst Rückfragen“ wirkt – unterschiedlich stark.** Haiku fragt 3, Opus 5, Sonnet 6 Dinge. Die Zusatzfragen (Datum für „Freitag“, Konsequenzen androhen? Mindestmenge bei Teillieferung?) sind echtes Einkaufs-Know-how und ein guter Gesprächsanlass: „Was musstet ihr erklären, das für euch selbstverständlich war?“ (Reflexionsfrage 2).
- **Das Beispiel wird wörtlich übernommen.** Alle drei Modelle bauen den Beispielsatz „Wir schätzen die langjährige Zusammenarbeit …“ wortgleich ein. Lehre: Der Baustein „Beispiel“ wirkt stark – ein schwaches Beispiel führt zu einem schwachen Text.
- **Längenvorgaben nachzählen.** „Maximal die Hälfte“ halten zwei von drei Modellen nicht ein, und die Wortzahl-Angaben der Modelle stimmen nicht (Sonnet „ca. 85“ bei 76). Das passt zum Bewertungskriterium „Korrektheit – habe ich es geprüft?“ und zur Zähl-Demo aus Block 5.
- **Beim Kürzen geht Information verloren.** Nach „Kürzer“ fehlen je nach Modell KW 19/21, Bestellnummer oder Kundenauftrag. Teilnehmende sollten nach jeder Iteration prüfen, ob alles Wichtige noch drin ist.
- **Korrekturen präzise formulieren.** „Punkt 3“ passt nicht zu einem Fließtext; die Modelle treffen die Stelle nur, weil der Rest des Satzes eindeutig ist. Sonnet und Opus sagen offen, dass es keine Punkte gibt – Haiku nicht. Lehre: Besser die betroffene Stelle zitieren („Der Satz mit ‚Ende KW 22‘ stimmt nicht …“).
- **Gute Zusatztipps sind fachlich wertvoll:** „Wareneingang bei uns“ statt nur „Liefertermin“ (Sonnet) und konkretes Datum statt Kalenderwoche (Opus) – beides typische Einkaufspraxis, die sich in den wiederverwendbaren Prompt übernehmen lässt.
- **Zeit:** Fünf Turns brauchen inklusive Lesen und Prüfen ca. 12–15 Minuten – passt in den Zeitplan (2:23–2:43), auch im Modus „nacheinander“ (je ca. 12 Min.), wenn Turn 5 knapp gelesen wird.
- **Vorschlag für den wiederverwendbaren Prompt** (Ergebnis der Übung):

```
Du bist erfahrene Sachbearbeiterin im Einkauf.
Kontext: Lieferant [X] hat unsere Bestellung [BESTELLNUMMER] über [MENGE] [TEIL] [ANZAHL]-mal verschoben – zugesagt war [KW], jetzt [KW]. Wareneingang bei uns spätestens [DATUM] für einen Kundenauftrag.
Aufgabe: Freundliche, aber bestimmte Mahnung. Bitte um verbindlichen Liefertermin bis [DATUM] und frag, ob eine Teillieferung möglich ist.
Format: max. 80 Wörter, Betreffzeile, per Sie, Platzhalter in eckigen Klammern für Ansprechpartner und Unterschrift.
```

## Probleme im Material / Verbesserungsvorschlag

- Die Übung läuft wie beschrieben; alle „Woran du ein gutes Ergebnis erkennst“-Punkte der Lösungshinweise lassen sich mit diesem Fall erfüllen.
- **„Punkt 3 stimmt so nicht“ (Schritt 4)** passt nur auf nummerierte Texte. Bei Mails führt es zu Rückfragen oder stillen Annahmen. Vorschlag für [Uebung_4_Eigene_Aufgabe.md](../06_Uebungen/Uebung_4_Eigene_Aufgabe.md), Schritt 4, Codeblock ersetzen durch: `Punkt 3 (bzw. der Satz mit „…“) stimmt so nicht. Richtig ist: [...]. Bitte überarbeite den Text entsprechend.`
- **„Kürzer, bitte – maximal die Hälfte“** wird nicht zuverlässig eingehalten. Vorschlag: Unter dem Codeblock in Schritt 4 einen Satz ergänzen: *„Prüf nach: Hat der KI-Assistent wirklich gekürzt – und ist alles Wichtige noch drin?“*
- **Lösungshinweise:** Das Einkaufs-Mahnungsbeispiel aus Schritt 3 ist das sichtbarste Beispiel des Übungsblatts, in den [Trainer-Lösungshinweisen, Übung 4](../06_Uebungen/Trainer-Loesungshinweise.md#übung-4-eigene-aufgabe) fehlt aber ein Musterprompt dafür. Vorschlag: unter „Musterprompts für häufige Aufgaben“ einen Block **„Mahnung Lieferverzug (Einkauf)“** mit dem Prompt oben ergänzen und den Hinweis: *„Erwartung: versandfähiger Entwurf mit Platzhaltern; typische Schwächen: Kürzung zu schwach, Fakten gehen beim Kürzen verloren, Wortzahl-Angaben der KI stimmen nicht.“*

---

## Gesprächsprotokoll: Haiku

### Nutzer 1
Du bist erfahrene Sachbearbeiterin im Einkauf.

Kontext: Wir sind ein kleiner technischer Hersteller mit ca. 80 Mitarbeitenden. Ein langjähriger Lieferant für Kunststoffteile (im Folgenden Lieferant X) hat unsere Bestellung über 2.000 Gehäusedeckel bereits zweimal verschoben – zugesagt war KW 19, jetzt haben wir KW 21. Wir brauchen die Teile spätestens Ende KW 22 für einen Kundenauftrag. Die Mail geht an die Auftragsbearbeitung des Lieferanten.

Aufgabe: Formuliere eine freundliche, aber bestimmte Mahnung wegen der verspäteten Lieferung. Bitte um einen verbindlichen Liefertermin bis Freitag und frag, ob eine Teillieferung möglich ist.

Format: Max. 120 Wörter, mit Betreffzeile, per Sie.

Beispiel (so soll es ungefähr aussehen):
"Wir schätzen die langjährige Zusammenarbeit, sind jetzt aber auf einen verlässlichen Termin angewiesen."

Wenn dir Informationen fehlen, stell mir zuerst Rückfragen, bevor du loslegst.

### Assistent 1
Ich brauche noch ein paar Angaben, damit die Mahnung passt:

1. Wie lautet die Bestellnummer des Lieferanten X?
2. Gibt es einen Ansprechpartner beim Lieferanten, den ich direkt anschreiben soll, oder geht die Mail nur an die Auftragsbearbeitung?
3. Mit welchem Namen soll die Mail unterschrieben werden?

Sobald ich das habe, schreibe ich den Entwurf.

### Nutzer 2
Zu möglichen Rückfragen: Bestellnummer bitte als Platzhalter [BESTELLNUMMER], Ansprechpartner beim Lieferanten als [ANSPRECHPARTNER], unterschreiben werde ich mit [MEIN NAME]. Bitte schreib jetzt den Entwurf.

### Assistent 2
**Betreff:** Verspätete Lieferung – Bestellung [BESTELLNUMMER]

Sehr geehrte Damen und Herren,
z. H. [ANSPRECHPARTNER],

wir schätzen die langjährige Zusammenarbeit, sind jetzt aber auf einen verlässlichen Termin angewiesen. Unsere Bestellung [BESTELLNUMMER] über 2.000 Gehäusedeckel war für KW 19 zugesagt und wurde bereits zweimal verschoben. Aktuell ist KW 21 avisiert.

Für einen Kundenauftrag benötigen wir die Teile spätestens Ende KW 22. Bitte bestätigen Sie uns bis Freitag einen verbindlichen Liefertermin.

Ist vorab auch eine Teillieferung möglich? Dann könnten wir zumindest einen Teil der Menge früher einsetzen.

Mit freundlichen Grüßen
[MEIN NAME]

### Nutzer 3
Kürzer, bitte – maximal die Hälfte.

### Assistent 3
**Betreff:** Verspätete Lieferung, Bestellung [BESTELLNUMMER]

Sehr geehrte Damen und Herren,

wir schätzen die Zusammenarbeit, benötigen aber einen verlässlichen Termin. Die Bestellung [BESTELLNUMMER] über 2.000 Gehäusedeckel wurde bereits zweimal verschoben. Wir brauchen die Teile spätestens Ende KW 22 und bitten um einen verbindlichen Liefertermin bis Freitag. Ist eine Teillieferung möglich?

Mit freundlichen Grüßen
[MEIN NAME]

### Nutzer 4
Punkt 3 stimmt so nicht. Richtig ist: Wir brauchen die Teile nicht erst Ende KW 22, sondern spätestens Mittwoch in KW 22. Bitte überarbeite den Text entsprechend.

### Assistent 4
**Betreff:** Verspätete Lieferung, Bestellung [BESTELLNUMMER]

Sehr geehrte Damen und Herren,

wir schätzen die Zusammenarbeit, benötigen aber einen verlässlichen Termin. Die Bestellung [BESTELLNUMMER] über 2.000 Gehäusedeckel wurde bereits zweimal verschoben. Wir brauchen die Teile spätestens am Mittwoch in KW 22 und bitten um einen verbindlichen Liefertermin bis Freitag. Ist eine Teillieferung möglich?

Mit freundlichen Grüßen
[MEIN NAME]

### Nutzer 5
Gib mir drei unterschiedliche Varianten, damit ich auswählen kann.

### Assistent 5
**Variante A (sachlich)**

**Betreff:** Verspätete Lieferung – Bestellung [BESTELLNUMMER]

Sehr geehrte Damen und Herren,

die Bestellung [BESTELLNUMMER] über 2.000 Gehäusedeckel wurde bereits zweimal verschoben, zuletzt auf KW 21. Wir benötigen die Teile spätestens Mittwoch in KW 22. Bitte bestätigen Sie uns bis Freitag einen verbindlichen Liefertermin. Ist vorab eine Teillieferung möglich?

Mit freundlichen Grüßen
[MEIN NAME]

**Variante B (freundlich, partnerschaftlich)**

**Betreff:** Bitte um verbindlichen Liefertermin – Bestellung [BESTELLNUMMER]

Sehr geehrte Damen und Herren,

wir schätzen die langjährige Zusammenarbeit sehr. Umso mehr bitten wir Sie, die Bestellung [BESTELLNUMMER] (2.000 Gehäusedeckel) vorrangig zu bearbeiten. Wir benötigen die Teile spätestens Mittwoch in KW 22 für einen Kundenauftrag. Könnten Sie uns bis Freitag einen verbindlichen Termin nennen? Eine Teillieferung wäre für uns ebenfalls hilfreich. Ist sie möglich?

Mit freundlichen Grüßen
[MEIN NAME]

**Variante C (knapp)**

**Betreff:** Mahnung Bestellung [BESTELLNUMMER]

Sehr geehrte Damen und Herren,

die Lieferung von 2.000 Gehäusedeckeln (Bestellung [BESTELLNUMMER]) ist nach zwei Verschiebungen weiterhin offen. Wir benötigen die Ware spätestens Mittwoch in KW 22. Bitte teilen Sie uns bis Freitag einen verbindlichen Liefertermin mit und prüfen Sie eine Teillieferung.

Mit freundlichen Grüßen
[MEIN NAME]

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1
Du bist erfahrene Sachbearbeiterin im Einkauf.

Kontext: Wir sind ein kleiner technischer Hersteller mit ca. 80 Mitarbeitenden. Ein langjähriger Lieferant für Kunststoffteile (im Folgenden Lieferant X) hat unsere Bestellung über 2.000 Gehäusedeckel bereits zweimal verschoben – zugesagt war KW 19, jetzt haben wir KW 21. Wir brauchen die Teile spätestens Ende KW 22 für einen Kundenauftrag. Die Mail geht an die Auftragsbearbeitung des Lieferanten.

Aufgabe: Formuliere eine freundliche, aber bestimmte Mahnung wegen der verspäteten Lieferung. Bitte um einen verbindlichen Liefertermin bis Freitag und frag, ob eine Teillieferung möglich ist.

Format: Max. 120 Wörter, mit Betreffzeile, per Sie.

Beispiel (so soll es ungefähr aussehen):
"Wir schätzen die langjährige Zusammenarbeit, sind jetzt aber auf einen verlässlichen Termin angewiesen."

Wenn dir Informationen fehlen, stell mir zuerst Rückfragen, bevor du loslegst.

### Assistent 1
Gern. Bevor ich den Entwurf schreibe, brauche ich ein paar Angaben:

1. Wie lautet die Bestellnummer, und gibt es eine Auftragsbestätigungsnummer, auf die ich mich beziehen soll?
2. Gibt es einen festen Ansprechpartner in der Auftragsbearbeitung, oder soll ich allgemein anschreiben ("Sehr geehrte Damen und Herren")?
3. Wie soll die Mail unterschrieben werden (Name, Position)?
4. Gibt es Konsequenzen, die ich andeuten darf, zum Beispiel Vertragsstrafe, Stornierung oder Wechsel des Lieferanten? Oder soll die Mail rein freundlich-bestimmt bleiben, ohne Drohung?
5. Welche Frist gilt für die Rückmeldung: "bis Freitag" dieser Woche? Soll ich das Datum nennen?
6. Wäre für Sie eine Teillieferung in beliebiger Menge nützlich, oder gibt es eine Mindestmenge, die Sie für den Kundenauftrag brauchen?

Wenn Sie möchten, setze ich sonst Platzhalter ein und lasse Konsequenzen weg.

### Nutzer 2
Zu möglichen Rückfragen: Bestellnummer bitte als Platzhalter [BESTELLNUMMER], Ansprechpartner beim Lieferanten als [ANSPRECHPARTNER], unterschreiben werde ich mit [MEIN NAME]. Bitte schreib jetzt den Entwurf.

### Assistent 2
**Betreff:** Dringend: verbindlicher Liefertermin für Bestellung [BESTELLNUMMER]

Guten Tag [ANSPRECHPARTNER],

wir schätzen die langjährige Zusammenarbeit, sind jetzt aber auf einen verlässlichen Termin angewiesen. Unsere Bestellung [BESTELLNUMMER] über 2.000 Gehäusedeckel wurde bereits zweimal verschoben, von KW 19 auf KW 21. Wir benötigen die Teile spätestens Ende KW 22 für einen Kundenauftrag.

Bitte bestätigen Sie uns bis Freitag einen verbindlichen Liefertermin. Ist alternativ eine Teillieferung möglich? Falls ja, in welchem Umfang und zu welchem Zeitpunkt?

Vielen Dank für Ihre schnelle Rückmeldung.

Freundliche Grüße
[MEIN NAME]

(ca. 85 Wörter im Mailtext)

### Nutzer 3
Kürzer, bitte – maximal die Hälfte.

### Assistent 3
**Betreff:** Verbindlicher Liefertermin für Bestellung [BESTELLNUMMER]

Guten Tag [ANSPRECHPARTNER],

unsere 2.000 Gehäusedeckel wurden bereits zweimal verschoben (KW 19 auf KW 21). Wir benötigen sie spätestens Ende KW 22. Bitte bestätigen Sie uns bis Freitag einen verbindlichen Termin. Wäre eine Teillieferung möglich?

Freundliche Grüße
[MEIN NAME]

(ca. 40 Wörter im Mailtext, unter der Hälfte der 120 Wörter)

### Nutzer 4
Punkt 3 stimmt so nicht. Richtig ist: Wir brauchen die Teile nicht erst Ende KW 22, sondern spätestens Mittwoch in KW 22. Bitte überarbeite den Text entsprechend.

### Assistent 4
Kleiner Hinweis: Mein Entwurf hatte keine nummerierten Punkte. Ich gehe davon aus, dass Sie die Frist "Ende KW 22" meinen, und habe sie angepasst.

**Betreff:** Verbindlicher Liefertermin für Bestellung [BESTELLNUMMER]

Guten Tag [ANSPRECHPARTNER],

unsere 2.000 Gehäusedeckel wurden bereits zweimal verschoben (KW 19 auf KW 21). Wir benötigen sie spätestens am Mittwoch in KW 22. Bitte bestätigen Sie uns bis Freitag einen verbindlichen Termin. Wäre eine Teillieferung möglich?

Freundliche Grüße
[MEIN NAME]

Hinweis: Wenn die Teile am Mittwoch in KW 22 bei Ihnen sein müssen, sollte die Lieferung beim Lieferanten spätestens einige Tage vorher versandt werden. Es kann sinnvoll sein, "Wareneingang bei uns" ausdrücklich zu schreiben.

### Nutzer 5
Gib mir drei unterschiedliche Varianten, damit ich auswählen kann.

### Assistent 5
Hier sind drei Varianten, jeweils mit der Frist Mittwoch in KW 22.

**Variante A: freundlich-sachlich**

Betreff: Verbindlicher Liefertermin für Bestellung [BESTELLNUMMER]

Guten Tag [ANSPRECHPARTNER],

wir schätzen die langjährige Zusammenarbeit, sind jetzt aber auf einen verlässlichen Termin angewiesen. Die 2.000 Gehäusedeckel wurden schon zweimal verschoben. Wir benötigen sie spätestens am Mittwoch in KW 22. Bitte nennen Sie uns bis Freitag einen verbindlichen Termin. Ist eine Teillieferung möglich?

Freundliche Grüße
[MEIN NAME]

**Variante B: bestimmt und knapp**

Betreff: Dringend: Bestellung [BESTELLNUMMER] verbindlich bestätigen

Guten Tag [ANSPRECHPARTNER],

nach zwei Terminverschiebungen (KW 19, KW 21) können wir keine weitere Verzögerung akzeptieren. Wareneingang bei uns muss spätestens Mittwoch in KW 22 sein. Bitte bestätigen Sie uns bis Freitag verbindlich den Liefertermin und teilen Sie mit, ob eine Teillieferung möglich ist.

Mit freundlichen Grüßen
[MEIN NAME]

**Variante C: lösungsorientiert, kooperativ**

Betreff: Gemeinsam eine Lösung finden: Bestellung [BESTELLNUMMER]

Guten Tag [ANSPRECHPARTNER],

die Verschiebung unserer 2.000 Gehäusedeckel von KW 19 auf KW 21 bringt uns bei einem Kundenauftrag in Bedrängnis. Wir brauchen die Teile spätestens Mittwoch in KW 22. Könnten Sie uns bis Freitag einen festen Termin nennen? Hilft eine Teillieferung, die Sie früher liefern können? Wir finden gern gemeinsam eine Lösung.

Beste Grüße
[MEIN NAME]

Empfehlung: Variante A passt zur langjährigen Beziehung, B, wenn Sie Druck aufbauen wollen, C, wenn der Lieferant selbst ein Kapazitätsproblem haben könnte.

---

## Gesprächsprotokoll: Opus

### Nutzer 1
Du bist erfahrene Sachbearbeiterin im Einkauf.

Kontext: Wir sind ein kleiner technischer Hersteller mit ca. 80 Mitarbeitenden. Ein langjähriger Lieferant für Kunststoffteile (im Folgenden Lieferant X) hat unsere Bestellung über 2.000 Gehäusedeckel bereits zweimal verschoben – zugesagt war KW 19, jetzt haben wir KW 21. Wir brauchen die Teile spätestens Ende KW 22 für einen Kundenauftrag. Die Mail geht an die Auftragsbearbeitung des Lieferanten.

Aufgabe: Formuliere eine freundliche, aber bestimmte Mahnung wegen der verspäteten Lieferung. Bitte um einen verbindlichen Liefertermin bis Freitag und frag, ob eine Teillieferung möglich ist.

Format: Max. 120 Wörter, mit Betreffzeile, per Sie.

Beispiel (so soll es ungefähr aussehen):
"Wir schätzen die langjährige Zusammenarbeit, sind jetzt aber auf einen verlässlichen Termin angewiesen."

Wenn dir Informationen fehlen, stell mir zuerst Rückfragen, bevor du loslegst.

### Assistent 1
Gern! Vor dem Entwurf habe ich ein paar kurze Rückfragen:

1. **Bestellnummer:** Wie lautet die Bestell- bzw. Auftragsnummer? Damit findet die Auftragsbearbeitung den Vorgang sofort.
2. **Ansprechpartner:** Kennen Sie beim Lieferanten eine Ansprechperson mit Namen? Sonst schreibe ich „Sehr geehrte Damen und Herren“.
3. **Absender:** Mit welchem Namen (und ggf. welcher Funktion) soll die Mail unterschrieben werden?
4. **Freitag:** Ist der kommende Freitag gemeint? Wenn Sie mir das Datum nennen, schreibe ich es direkt in den Text, das wirkt verbindlicher.
5. **Konsequenzen:** Soll die Mail andeuten, was passiert, wenn der Termin nicht klappt (z. B. ein anderer Lieferant)? Oder soll sie rein partnerschaftlich bleiben?

Wenn Sie die Angaben nicht zur Hand haben, setze ich einfach Platzhalter ein.

### Nutzer 2
Zu möglichen Rückfragen: Bestellnummer bitte als Platzhalter [BESTELLNUMMER], Ansprechpartner beim Lieferanten als [ANSPRECHPARTNER], unterschreiben werde ich mit [MEIN NAME]. Bitte schreib jetzt den Entwurf.

### Assistent 2
Hier ist der Entwurf (ca. 95 Wörter):

**Betreff:** Bestellung [BESTELLNUMMER] – 2.000 Gehäusedeckel: Bitte um verbindlichen Liefertermin

Sehr geehrte/r [ANSPRECHPARTNER],

unsere Bestellung [BESTELLNUMMER] über 2.000 Gehäusedeckel war ursprünglich für KW 19 zugesagt. Sie wurde inzwischen zweimal verschoben, zuletzt auf KW 21. Wir schätzen die langjährige Zusammenarbeit, sind jetzt aber auf einen verlässlichen Termin angewiesen: Wir benötigen die Teile spätestens Ende KW 22 für einen Kundenauftrag.

Bitte bestätigen Sie uns bis Freitag einen verbindlichen Liefertermin. Falls eine vollständige Lieferung bis dahin nicht möglich ist, teilen Sie uns bitte mit, ob und in welcher Menge eine Teillieferung möglich wäre.

Vielen Dank für Ihre Unterstützung.

Mit freundlichen Grüßen
[MEIN NAME]

Tipp: Wenn Sie beim Freitag das genaue Datum einsetzen (z. B. „bis Freitag, TT.MM.“), wirkt die Frist noch verbindlicher.

### Nutzer 3
Kürzer, bitte – maximal die Hälfte.

### Assistent 3
Hier ist die kürzere Fassung (ca. 50 Wörter):

**Betreff:** Bestellung [BESTELLNUMMER] – verbindlicher Liefertermin benötigt

Sehr geehrte/r [ANSPRECHPARTNER],

unsere Bestellung [BESTELLNUMMER] (2.000 Gehäusedeckel) wurde zweimal verschoben, von KW 19 auf KW 21. Für einen Kundenauftrag benötigen wir die Teile spätestens Ende KW 22.

Bitte bestätigen Sie uns bis Freitag einen verbindlichen Termin und teilen Sie uns mit, ob eine Teillieferung möglich ist.

Vielen Dank und freundliche Grüße
[MEIN NAME]

### Nutzer 4
Punkt 3 stimmt so nicht. Richtig ist: Wir brauchen die Teile nicht erst Ende KW 22, sondern spätestens Mittwoch in KW 22. Bitte überarbeite den Text entsprechend.

### Assistent 4
Danke für die Korrektur. Kurzer Hinweis: Der Text hat keine nummerierten Punkte. Ich gehe davon aus, dass Sie den Bedarfstermin meinen, und habe ihn auf Mittwoch in KW 22 geändert:

**Betreff:** Bestellung [BESTELLNUMMER] – verbindlicher Liefertermin benötigt

Sehr geehrte/r [ANSPRECHPARTNER],

unsere Bestellung [BESTELLNUMMER] (2.000 Gehäusedeckel) wurde zweimal verschoben, von KW 19 auf KW 21. Für einen Kundenauftrag benötigen wir die Teile spätestens am Mittwoch der KW 22.

Bitte bestätigen Sie uns bis Freitag einen verbindlichen Termin und teilen Sie uns mit, ob eine Teillieferung möglich ist.

Vielen Dank und freundliche Grüße
[MEIN NAME]

Tipp: Ein konkretes Datum („spätestens Mittwoch, TT.MM.“) lässt weniger Spielraum für Missverständnisse als die Kalenderwoche. Falls Sie etwas anderes mit „Punkt 3“ gemeint haben, sagen Sie mir bitte Bescheid.

### Nutzer 5
Gib mir drei unterschiedliche Varianten, damit ich auswählen kann.

### Assistent 5
Gern, hier sind drei Varianten im gleichen Umfang (je ca. 50–60 Wörter):

---

**Variante 1 – sachlich und knapp**

**Betreff:** Bestellung [BESTELLNUMMER] – verbindlicher Liefertermin bis Freitag

Sehr geehrte/r [ANSPRECHPARTNER],

unsere Bestellung [BESTELLNUMMER] über 2.000 Gehäusedeckel wurde zweimal verschoben, zuletzt auf KW 21. Wir benötigen die Teile spätestens am Mittwoch der KW 22.

Bitte bestätigen Sie uns bis Freitag einen verbindlichen Liefertermin. Ist eine Teillieferung möglich?

Mit freundlichen Grüßen
[MEIN NAME]

---

**Variante 2 – partnerschaftlich**

**Betreff:** Bestellung [BESTELLNUMMER] – gemeinsame Lösung für den Liefertermin

Sehr geehrte/r [ANSPRECHPARTNER],

wir schätzen die langjährige Zusammenarbeit, sind bei unserer Bestellung [BESTELLNUMMER] (2.000 Gehäusedeckel) jetzt aber auf einen verlässlichen Termin angewiesen. Nach zwei Verschiebungen benötigen wir die Teile spätestens am Mittwoch der KW 22.

Könnten Sie uns bis Freitag einen verbindlichen Termin nennen und prüfen, ob eine Teillieferung möglich ist?

Vielen Dank und freundliche Grüße
[MEIN NAME]

---

**Variante 3 – bestimmt und dringlich**

**Betreff:** Dringend: Bestellung [BESTELLNUMMER] – Liefertermin gefährdet Kundenauftrag

Sehr geehrte/r [ANSPRECHPARTNER],

die Lieferung unserer Bestellung [BESTELLNUMMER] (2.000 Gehäusedeckel) wurde bereits zweimal verschoben, von KW 19 auf KW 21. Davon hängt ein Kundenauftrag ab: Spätester Termin ist Mittwoch der KW 22.

Bitte bestätigen Sie uns bis Freitag verbindlich den Liefertermin und teilen Sie uns mit, ob eine Teillieferung möglich ist.

Mit freundlichen Grüßen
[MEIN NAME]

---

Meine Empfehlung: Variante 2 passt gut zu einem langjährigen Lieferanten. Variante 3 eignet sich, wenn schon die erste Mahnung nichts gebracht hat.

---

Zurück zu [Übung 4: Deine eigene Aufgabe](../06_Uebungen/Uebung_4_Eigene_Aufgabe.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md)
