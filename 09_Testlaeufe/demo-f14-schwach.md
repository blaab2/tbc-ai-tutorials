# Testlauf: Folie 14 – Schwacher Prompt: Mail an den Lieferanten

**Herkunft:** Live-Demo auf [Folie 14 – Schlechter vs. guter Prompt](../04_Folien.md#folie-14--schlechter-vs-guter-prompt) (Block 4). Der Prompt steht auch in den [Trainer-Lösungshinweisen, Übung 2 – Demo-Prompts aus dem Input](../06_Uebungen/Trainer-Loesungshinweise.md#demo-prompts-aus-dem-input-block-4-folie-14). Gegenstück: der starke Prompt (Testlauf `demo-f14-stark.md`, zum Zeitpunkt dieses Protokolls noch nicht vorhanden).

**Prompt (neuer Chat, getrennt vom starken Prompt):**
```
Schreib eine Mail an den Lieferanten wegen der Lieferung.
```

**Erwartung laut Material:**
- Folie 14, Tabelle: „Allgemeine, lange Mail, Details erfunden oder Platzhalter“
- Folie 14, Sprechernotiz: „Typische Beobachtungen beim schwachen Prompt: Die KI erfindet Details (Bestellnummer, Datum), schreibt sehr allgemein oder setzt Platzhalter wie [Name] ein.“
- Lösungshinweise: „allgemeine, oft lange Mail mit erfundenen Details (Bestellnummer, Menge, Datum) oder vielen Platzhaltern“

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Einschränkung:** Jedes Modell wurde einmal gefragt. Der direkte Vergleich mit dem starken Prompt (demo-f14-stark) war beim Schreiben dieses Protokolls nicht möglich, weil das Protokoll noch fehlt. Die Vergleichsaussagen unten stützen sich auf die Vorgaben des starken Prompts (höchstens 120 Wörter, 500 Dichtungsringe, Termin 15., Frist Freitag).

---

## Bewertung

Wortzahlen mit `wc -w` über die gesamte Antwort gezählt (inklusive Rückfragen). Platzhalter sind Angaben in eckigen Klammern. Gliederungshinweise wie „[Variante A – Verspätung:]“ sind getrennt gezählt.

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Länge der Antwort (Wörter) | 202 | 213 | 311 |
| Zum Vergleich: Vorgabe starker Prompt | max. 120 | max. 120 | max. 120 |
| Platzhalter in eckigen Klammern | 9 | 10 (+1 Gliederungshinweis) | 15 (+3 Gliederungshinweise/Alternativen) |
| Erfundene Details (Bestellnummer, Menge, Datum) | keine | keine | keine (die Mengen „50/40 Stück“ stehen nur als Beispiel im Platzhalter) |
| Ungeprüfte Annahmen im Mailtext (ohne Klammer) | ja: geht fest von einer ausgebliebenen Lieferung aus („Bislang haben wir die Ware nicht erhalten.“) | nein, bietet drei Varianten an | ja, klein: „Fotos und eine Kopie des Lieferscheins haben wir beigefügt.“, „dringend“ |
| Rückfragen gestellt | ja, 5 Punkte (nach der Vorlage) | ja, 4 nummerierte Fragen (nach der Vorlage) | ja, 5 Fragen + weitere benötigte Angaben (vor der Vorlage) |
| Mail versandfertig? | nein | nein | nein |
| Allgemein/unkonkret? | ja | ja, sogar mit Auswahl-Varianten | ja, mit Varianten A/B |
| Anrede der Nutzerin/des Nutzers | du | du | Sie |
| Zeigt die Demo den Unterschied zum starken Prompt? | ja | ja | ja |
| Tritt der Effekt „Details erfunden“ auf? | nein | nein | nein |

**Gesamturteil:** Die Demo funktioniert **teilweise** wie gedacht. Der Kontrast zum starken Prompt ist deutlich: Keine der drei Antworten ist versandfertig. Alle sind fast doppelt bis zweieinhalbmal so lang wie die 120 Wörter des starken Prompts, allgemein gehalten und voller Platzhalter. Was das Material als *typisch* ankündigt, tritt aber nicht ein: **Kein Modell erfindet eine Bestellnummer, eine Menge oder ein Datum.** Alle drei nutzen dasselbe Muster: Vorlage mit Platzhaltern plus Rückfragen. Den ersten Teil der Sprechernotiz („Die KI erfindet Details (Bestellnummer, Datum)“) sollte der Trainer also nicht als sichere Vorhersage formulieren.

---

## Gefundene Fehler mit Beleg

Es gibt keine sachlich falschen Angaben, weil der Prompt keine Fakten vorgibt, gegen die man prüfen könnte. Gefunden wurden kleinere **Annahmen**, die im Text wie Tatsachen stehen:

1. **Haiku legt sich auf einen Fall fest.** Der Mailtext lautet „wir warten auf die Lieferung …“ und „Bislang haben wir die Ware nicht erhalten.“ Der Prompt sagt nur „wegen der Lieferung“. Ob die Ware fehlt, beschädigt oder falsch ist, steht dort nicht. Haiku fragt das zwar hinterher ab („Liegt eine Verzögerung vor, oder ist etwas anderes passiert?“), die Vorlage selbst geht aber schon von einer Verzögerung aus. Wer die Vorlage ungelesen ausfüllt, schickt im Zweifel die falsche Beschwerde.
2. **Opus behauptet Anhänge.** In Variante B steht ohne Klammer: „Fotos und eine Kopie des Lieferscheins haben wir beigefügt.“ Das ist eine erfundene Tatsache. Wer die Vorlage übernimmt, kündigt Anhänge an, die es vielleicht gar nicht gibt. Ähnlich „Da wir die Ware dringend … benötigen“: Die Dringlichkeit kommt nicht vom Nutzer.
3. **Opus-Platzhalter mit Beispielzahlen:** „[z. B. Artikel XY fehlt / statt 50 nur 40 Stück geliefert / Ware beschädigt]“. Das ist korrekt als Beispiel markiert und kein Fehler. Es zeigt aber, wie schnell beim Ausfüllen eine Beispielzahl stehen bleiben kann.
4. **Sonnet:** keine Annahmen gefunden. Die drei Varianten (verspätet, fehlerhaft, Statusanfrage) werden ausdrücklich zur Auswahl gestellt.

Platzhalter-Zählung zur Kontrolle (per Python über die Antworttexte):
- Haiku 9: [Bestellnummer] ×2, [Bestelldatum], [vereinbarten Liefertermin], [Datum], [Telefonnummer] ×2, [Dein Name], [Firma]
- Sonnet 10 + 1: [Bestell-/Auftragsnummer], [Bestellnummer], [Datum] ×4, [Beschreibung des Mangels …], [Name], [Position, Firma], [Telefon / E-Mail]. Dazu kommt der Gliederungshinweis „[Passende Variante auswählen:]“.
- Opus 15 + 3: [Bestellnummer] ×2, [Datum] ×5, [Bestelldatum], [Frau/Herr Nachname], [z. B. Artikel XY …], [Zweck/Projekt], [Ihr Name], [Position], [Firma], [Telefon / E-Mail]. Dazu kommen „[Variante A – Verspätung:]“, „[Variante B – Mangel/Unvollständigkeit:]“ und „[oder: uns eine entsprechende Gutschrift zu erteilen]“.

---

## Lehren für die Auswertung

1. **Ankündigung anpassen.** Die Teilnehmenden sehen mit großer Wahrscheinlichkeit eine *Vorlage mit Platzhaltern und Rückfragen*, keine erfundene Bestellnummer. Wer „gleich erfindet die KI eine Bestellnummer“ ankündigt, wird widerlegt. Besser: „Mal sehen, was die KI aus so wenig Information macht.“ Dann die Gruppe zählen lassen: Wie viele eckige Klammern? Wie viele Wörter? Wie viel davon müsste ich selbst noch ausfüllen?
2. **Die Lehre bleibt trotzdem gültig, nur anders begründet.** Der schwache Prompt spart keine Arbeit. Die Antwort sieht hilfreich aus, aber man muss danach noch die Fragen beantworten, die richtige Variante wählen und 9 bis 15 Lücken füllen. Der starke Prompt liefert diese Informationen gleich mit. Damit wird die Sprechernotiz „40 Sekunden länger – dafür kaum Nacharbeit“ sogar besonders gut sichtbar.
3. **Gute Brücke zu Folie 15 (Joker).** Alle drei Modelle stellen von sich aus Rückfragen. Daran lässt sich zeigen: Die KI braucht genau die Bausteine Kontext und Aufgabe. Wer die Fragen vorher beantwortet, also den starken Prompt schreibt, bekommt sofort eine passende Mail. Wer sie nicht beantworten kann, nimmt den Joker „Stell mir erst bis zu 3 Fragen“.
4. **Versteckte Annahmen zeigen.** Die eigentliche Falle steckt nicht in den Platzhaltern, sondern in den Sätzen *ohne* Klammern: Haiku geht von einer ausgebliebenen Lieferung aus, Opus behauptet „Fotos … haben wir beigefügt“. Wer so eine Vorlage nur ausfüllt und nicht ganz liest, verschickt falsche Aussagen. Das passt zur Kernbotschaft „Die erste Antwort ist ein Entwurf“.
5. **Mit anderen Tools kann es anders laufen.** Kleinere oder ältere Modelle oder Tools mit sehr kurzer Systemanweisung schreiben eher eine fertige Mail mit erfundenen Daten. Darum im Material besser „oder“ statt „typisch“ schreiben und offen lassen, welcher Fall eintritt. Beide Fälle eignen sich für die Auswertung.
6. **Falls der Trainer den Erfinde-Effekt zuverlässig zeigen will,** hilft ein schwacher Prompt, der Rückfragen indirekt ausschließt, zum Beispiel: „Schreib eine fertige Mail an den Lieferanten wegen der Lieferung, ohne Platzhalter.“ Dann muss das Modell Details erfinden oder sehr vage bleiben. Das sollte vor dem Kurs im eigenen [KI-TOOL] getestet werden. Als Hauptdemo ist der Originalprompt aber realistischer, weil Teilnehmende genau so schreiben.

---

## Gesprächsprotokolle

### Haiku

**Nutzer 1**

Schreib eine Mail an den Lieferanten wegen der Lieferung.

**Assistent 1**

Gern. Damit die Mail konkret wird, brauche ich noch ein paar Angaben. Falls du sie nicht gleich hast, nimm die Vorlage unten und fülle die eckigen Klammern aus.

**Betreff:** Nachfrage zu Ihrer Lieferung [Bestellnummer]

Sehr geehrte Damen und Herren,

wir warten auf die Lieferung zu unserer Bestellung [Bestellnummer] vom [Bestelldatum]. Laut unseren Unterlagen war die Lieferung für den [vereinbarten Liefertermin] vorgesehen. Bislang haben wir die Ware nicht erhalten.

Bitte teilen Sie uns bis spätestens [Datum] mit, wann die Lieferung erfolgt und ob es Verzögerungen gibt.

Vielen Dank für Ihre Rückmeldung. Bei Fragen erreichen Sie mich unter [Telefonnummer] oder per E-Mail.

Mit freundlichen Grüßen

[Dein Name]
[Firma]
[Telefonnummer]

---

Damit ich die Mail genauer formulieren kann, wären diese Angaben hilfreich:

- **Lieferant und Ansprechpartner:** Wer soll die Mail bekommen, und wie wird die Person angesprochen?
- **Bestellung:** Bestellnummer, Bestelldatum und was genau bestellt wurde
- **Liegt eine Verzögerung vor, oder ist etwas anderes passiert?** Zum Beispiel falsche oder beschädigte Ware, fehlende Teile oder eine Teillieferung
- **Gewünschter Ton:** eher freundlich, neutral oder bestimmt (z. B. wenn schon mehrfach nachgefragt wurde)
- **Gewünschte Reaktion:** nur Nachfrage nach dem Liefertermin, Fristsetzung oder Forderung nach Entschädigung

Schick mir diese Infos, dann passe ich die Mail an.

---

### Sonnet

**Nutzer 1**

Schreib eine Mail an den Lieferanten wegen der Lieferung.

**Assistent 1**

Gerne! Damit die Mail wirklich passt, brauche ich noch ein paar Angaben. Bis dahin hier ein Entwurf, den du anpassen kannst:

**Betreff:** Rückfrage zu unserer Lieferung [Bestell-/Auftragsnummer]

Sehr geehrte Damen und Herren,

bezüglich unserer Bestellung [Bestellnummer] vom [Datum] möchte ich mich bei Ihnen melden.

[Passende Variante auswählen:]
- **Lieferung verspätet:** Die Lieferung war für den [Datum] zugesagt, ist bei uns bisher jedoch nicht eingegangen. Bitte teilen Sie uns kurzfristig den aktuellen Status und den voraussichtlichen Liefertermin mit.
- **Lieferung fehlerhaft/beschädigt/unvollständig:** Bei der Warenannahme am [Datum] haben wir festgestellt, dass [Beschreibung des Mangels, z. B. Artikel fehlen / Ware beschädigt]. Bitte teilen Sie uns mit, wie Sie das Problem lösen möchten (Ersatzlieferung, Nachlieferung oder Gutschrift).
- **Statusanfrage:** Könnten Sie uns bitte den aktuellen Stand der Lieferung und den voraussichtlichen Liefertermin bestätigen?

Wir bitten um eine Rückmeldung bis zum [Datum].

Vielen Dank für Ihre Unterstützung.

Mit freundlichen Grüßen
[Name]
[Position, Firma]
[Telefon / E-Mail]

**Damit ich die Mail passgenau formulieren kann, beantworte mir bitte kurz:**
1. Worum geht es genau: Verspätung, Mangel, falsche oder fehlende Ware, oder nur eine Statusanfrage?
2. Wie heißt der Lieferant, und gibt es eine Bestell- oder Lieferscheinnummer?
3. Bis wann brauchst du die Ware bzw. eine Rückmeldung?
4. Soll der Ton eher freundlich-neutral oder bestimmt (z. B. mit Fristsetzung) sein?

---

### Opus

**Nutzer 1**

Schreib eine Mail an den Lieferanten wegen der Lieferung.

**Assistent 1**

Gerne! Mir fehlen noch ein paar Angaben, damit die Mail genau passt. Worum geht es bei der Lieferung?

- Ist die Lieferung **verspätet** oder noch gar nicht angekommen?
- Ist sie **unvollständig**, sind also Positionen oder Mengen falsch?
- Ist Ware **beschädigt** oder fehlerhaft?
- Wurde **falsche Ware** geliefert?
- Oder möchten Sie einen **Liefertermin anfragen** bzw. bestätigen lassen?

Hilfreich wären außerdem: Name des Lieferanten und der Ansprechperson, Bestell- oder Lieferscheinnummer, Bestelldatum, der vereinbarte Liefertermin und was Sie sich wünschen (z. B. Nachlieferung, Ersatz, Gutschrift oder einen neuen Termin).

Bis dahin hier eine **allgemeine Vorlage** für den häufigsten Fall, eine verspätete oder fehlerhafte Lieferung. Die Platzhalter in eckigen Klammern ersetzen Sie einfach:

---

**Betreff:** Unsere Bestellung Nr. [Bestellnummer] vom [Datum] – Rückfrage zur Lieferung

Sehr geehrte/r [Frau/Herr Nachname],

wir beziehen uns auf unsere Bestellung Nr. [Bestellnummer] vom [Bestelldatum]. Der Liefertermin war für den [Datum] vereinbart.

[Variante A – Verspätung:]
Leider ist die Ware bis heute nicht bei uns eingetroffen. Bitte teilen Sie uns bis zum [Datum] mit, wann wir mit der Lieferung rechnen können.

[Variante B – Mangel/Unvollständigkeit:]
Die Lieferung ist am [Datum] bei uns eingegangen. Bei der Wareneingangskontrolle haben wir jedoch Folgendes festgestellt:
- [z. B. Artikel XY fehlt / statt 50 nur 40 Stück geliefert / Ware beschädigt]

Fotos und eine Kopie des Lieferscheins haben wir beigefügt. Wir bitten Sie, die fehlende bzw. mangelfreie Ware bis zum [Datum] nachzuliefern [oder: uns eine entsprechende Gutschrift zu erteilen].

Da wir die Ware dringend für [Zweck/Projekt] benötigen, sind wir für eine schnelle Rückmeldung dankbar.

Vielen Dank für Ihre Unterstützung.

Mit freundlichen Grüßen

[Ihr Name]
[Position]
[Firma]
[Telefon / E-Mail]

---

Wenn Sie mir kurz sagen, was genau passiert ist, und die wichtigsten Daten nennen, schreibe ich Ihnen eine fertige Mail ohne Platzhalter. Ich kann den Ton auch anpassen, etwa freundlich-neutral bei einer ersten Nachfrage oder bestimmter, wenn Sie schon mehrfach nachgefragt haben.
