# Testlauf: Folie 14/15 – Starker Prompt mit Baukasten + Nachsteuern

**Herkunft:** [Folie 14 – Schlechter vs. guter Prompt und Folie 15 – Nachfragen und verbessern](../04_Folien.md) sowie [Trainer-Lösungshinweise, Abschnitt „Demo-Prompts aus dem Input (Block 4, Folie 14)“](../06_Uebungen/Trainer-Loesungshinweise.md) · Übungsblatt danach: [Übung 2 – Gute Prompts](../06_Uebungen/Uebung_2_Gute_Prompts.md)

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompts (alle im selben Chat):**

1. Starker Prompt von Folie 14 (Rolle – Kontext – Aufgabe – Format – Beispiel). Haiku bekam ihn als Fließtext, Sonnet mit Zeilenumbrüchen, Opus mit Zeilenumbrüchen **und** den Baustein-Etiketten „(Rolle)“, „(Kontext)“ usw. – genau wie in den Lösungshinweisen.
2. `Kürzer und etwas wärmer`
3. `Gib mir noch eine Variante, die mit einer Frage beginnt.`

**Ziel laut Material:** Fast versandfertige Mail mit Menge, Frist und klarer Bitte; danach zeigt Folie 15, dass Nachsteuern im Chat (kürzer/wärmer, Variante mit Frage) einfach geht.

**Nicht Teil dieses Testlaufs:** der schwache Prompt („Schreib eine Mail an den Lieferanten wegen der Lieferung.“). Der Vergleich schwach/stark muss separat getestet werden.

## Bewertung

Wortzahlen per Python nachgezählt (Betreff + Anrede + Text + Grußformel/Platzhalter-Signatur; ohne Opus' Anmerkung „ca. … Wörter“).

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Betreffzeile (T1) | ja | ja | ja |
| ≤ 120 Wörter (T1) | ja – 90 | ja – 95 | ja – 102 (selbst angegeben „ca. 100“, stimmt) |
| Sie-Form | ja | ja | ja |
| 500 Dichtungsringe | ja | ja | ja |
| Zweite Verschiebung um eine Woche | ja | ja | ja |
| Bedarf spätestens am 15. | ja (mit Platzhalter [Monat]) | ja | ja |
| Bitte um verbindlichen Termin bis Freitag | ja (mit Platzhalter [Datum]) | ja (+ „schriftlich“ ergänzt) | ja |
| Ton freundlich-bestimmt | ja – Beispielsatz fast wörtlich übernommen | ja – leicht spitz („Umso mehr überrascht uns …“) | ja – am bestimmtesten („… nicht auffangen“) |
| Keine erfundene Bestellnummer / nur Platzhalter | ja | ja | ja (+ [Telefon]) |
| Nichts Inhaltliches dazuerfunden | ja (nur Bitte um Alternativen) | weitgehend – T3: „damit wir unseren Kunden verbindlich informieren können“ | nein – T1: „Eine weitere Verschiebung können wir leider nicht auffangen.“ |
| T2 kürzer | ja – 71 (−21 %) | knapp – 80 (−16 %) | ja – 75 (−26 %) |
| T2 wärmer, gleicher Inhalt | ja; „um eine Woche“ entfällt | ja; „um eine Woche“ entfällt; Betreff ohne „bis Freitag“ | ja, am wärmsten; „um eine Woche“ entfällt |
| T3 beginnt mit Frage | ja (Betreff **und** erster Satz) | ja (erster Satz; Betreff unverändert aus T2) | ja (Betreff **und** erster Satz) |
| T3 enthält weiterhin alle Kernpunkte | ja | ja | ja |
| Fast versandfertig | ja | ja | ja (Wortzahl-Anmerkung vor Versand löschen) |
| **Gesamt** | **sehr gut**, sauberste Platzhalter | sehr gut | sehr gut, kleine Zuspitzung |

## Gefundene Fehler mit Beleg

Keine Faktenfehler: Menge (500), Frist (15.), Termin (Freitag) und „zum zweiten Mal um eine Woche“ stimmen in allen T1-Mails. Kein Modell erfindet eine Bestellnummer, ein Monatsdatum oder einen Firmennamen. Folgende Kleinigkeiten:

1. **Erfundene Aussage mit Gewicht** (Opus T1): „Eine weitere Verschiebung können wir leider nicht auffangen.“ Im Prompt steht nur, dass die Ware spätestens am 15. gebraucht wird – ob eine weitere Verschiebung noch vor dem 15. läge, weiß die KI nicht. Das macht die Mail härter, als der Absender es vielleicht will.
2. **Erfundener Zweck** (Sonnet T3): „…, damit wir unseren Kunden verbindlich informieren können.“ Plausibel, aber nicht vorgegeben.
3. **Zusatzforderung „schriftlich“** (Sonnet T1–T3): „bestätigen Sie uns daher bis Freitag *schriftlich*“. Stand nicht im Prompt – harmlos, aber eine Entscheidung der KI.
4. **Detail geht beim Kürzen verloren** (alle drei, T2): aus „zum zweiten Mal um eine Woche verschoben“ wird „schon zweimal verzögert“ (Haiku) bzw. „schon zum zweiten Mal verschoben/verzögert“ (Sonnet, Opus). Die Woche fehlt. Inhaltlich vertretbar, aber Beispiel dafür, dass beim Nachsteuern Details wegfallen können.
5. **Beispielsatz wörtlich kopiert** (Haiku T1, Sonnet T3): „wir schätzen die Zusammenarbeit mit Ihnen, brauchen jetzt aber Verlässlichkeit“. Der Prompt sagt „ungefähr so“. Kein Fehler, aber Anlass für den Hinweis: Ein Beispiel wird oft eins zu eins übernommen.
6. **„Kürzer“ wirkt nur mäßig** (Sonnet T2): von 95 auf 80 Wörter (−16 %). Ohne Zahl entscheidet die KI selbst, was „kürzer“ heißt.
7. **Meta-Kommentar in der Antwort** (Opus T1–T3): „*(ca. 100 Wörter)*“. Hilfreich zum Prüfen, muss aber beim Kopieren in die Mail entfernt werden.
8. **Betreff in T3 nicht angepasst** (Sonnet): identisch mit T2. Die Aufgabe ist trotzdem erfüllt, weil die Mail mit einer Frage beginnt.

## Lehren für die Auswertung

- **Die Demo funktioniert zuverlässig.** Alle drei Modelle liefern mit dem Baukasten-Prompt in einem Schritt eine Mail mit Menge, Frist und klarer Bitte, im richtigen Ton und unter 120 Wörtern. Die Aussage „Passende Mail, fast versandfertig“ auf Folie 14 trifft zu.
- **Etiketten stören nicht.** Opus bekam die Baustein-Etiketten „(Rolle)“, „(Kontext)“ … mit in den Prompt und hat sie weder übernommen noch kommentiert. Man kann den Prompt also so zeigen, wie er auf der Folie steht.
- **Platzhalter sind hier gut.** Beim starken Prompt sind [Ihr Name], [Firmenname] oder [Datum] richtig, denn diese Angaben kennt die KI nicht. Haiku ergänzt sogar [Monat] beim „15.“ und [Datum] beim „Freitag“. Damit kann man zeigen: Der Prompt selbst hat Lücken (welcher Monat? welcher Freitag?) – wer sie füllt, bekommt eine Mail, die wirklich fertig ist.
- **Nachsteuern ist einfach – aber gegenlesen.** „Kürzer und etwas wärmer“ und „mit einer Frage beginnen“ setzen alle sofort um, ohne dass der Inhalt neu erklärt werden muss. Dabei fällt aber bei allen „um eine Woche“ weg, und manches wird dazugedichtet (Opus: „können wir nicht auffangen“, Sonnet: „unseren Kunden informieren“). Gute Frage an die Runde: „Würdet ihr das so abschicken? Stimmt das bei uns überhaupt?“
- **Konkrete Maße steuern besser als Gefühlswörter.** „Kürzer“ bringt je nach Modell −16 % bis −26 %. Wer eine bestimmte Länge will, schreibt „höchstens 60 Wörter“ oder „maximal 3 Sätze“ – genau wie auf Folie 15 vorgeschlagen.
- **Beispiele werden gern wörtlich übernommen.** Der Ton-Beispielsatz taucht bei Haiku fast wörtlich auf. Wer das nicht will, schreibt dazu: „Nicht wörtlich übernehmen.“
- **Gleicher Prompt, ähnliche Ergebnisse.** Anders als bei offenen Prompts sind sich die drei Mails sehr ähnlich – ein schöner Beleg, dass ein klarer Prompt die Streuung verringert.
- Für die Live-Demo: Die Antworten sind kurz genug, um sie in den geplanten 1–2 Minuten zu zeigen. Nur Betreff, ersten Satz und Bitte vorlesen.

## Probleme im Material / Verbesserungsvorschlag

- **Folie 14, Sprechernotiz ([04_Folien.md](../04_Folien.md)):** Platzhalter wie „[Name]“ werden nur als Nachteil des schwachen Prompts genannt. Im Test setzen aber auch alle starken Mails Platzhalter (Name, Firma, teils Datum). Vorschlag: nach „Beim starken Prompt: konkret, richtige Länge, richtiger Ton.“ ergänzen: *„Platzhalter für Name, Firma oder das genaue Datum sind auch hier normal – sie markieren, was nur ihr wissen könnt. Schlecht sind Platzhalter oder Erfindungen bei den eigentlichen Inhalten (Menge, Frist, Anliegen).“*
- **Folie 15, Sprechernotiz:** Nach „Dann: ‚Gib mir noch eine Variante, die mit einer Frage beginnt.‘“ einen Satz zum Gegenlesen ergänzen: *„Kurz prüfen: Ist beim Kürzen etwas weggefallen (z. B. ‚um eine Woche‘) oder dazugekommen? In Tests hat die KI einmal ‚Eine weitere Verschiebung können wir nicht auffangen‘ ergänzt.“*
- Kleinigkeit: Die Live-Demo auf Folie 15 nutzt „Kürzer und etwas wärmer“, die Folie selbst „Kürzer, bitte – maximal 3 Sätze.“. Das passt gut zusammen, wenn man es ausspricht: *„Mit einer Zahl dazu wird ‚kürzer‘ noch genauer.“*

---

## Gesprächsprotokoll: Haiku

### Nutzer 1
Du bist Einkäuferin bei einem kleinen technischen Hersteller. Unser Lieferant hat die Lieferung von 500 Dichtungsringen zum zweiten Mal um eine Woche verschoben. Wir brauchen sie spätestens am 15. für einen Kundenauftrag. Schreib eine E-Mail, in der du um einen verbindlichen Liefertermin bis Freitag bittest. Höchstens 120 Wörter, freundlich, aber bestimmt, mit Betreffzeile, Sie-Form. Der Ton soll ungefähr so sein: „Wir schätzen die Zusammenarbeit, brauchen jetzt aber Verlässlichkeit.“

### Assistent 1
**Betreff:** Verbindlicher Liefertermin für 500 Dichtungsringe bis Freitag

Sehr geehrte Damen und Herren,

wir schätzen die Zusammenarbeit mit Ihnen, brauchen jetzt aber Verlässlichkeit. Die Lieferung von 500 Dichtungsringen wurde bereits zum zweiten Mal um eine Woche verschoben. Für einen Kundenauftrag benötigen wir die Ware spätestens am 15. [Monat].

Wir bitten Sie, uns bis Freitag, den [Datum], einen verbindlichen Liefertermin zu bestätigen. Sollte der 15. nicht einzuhalten sein, teilen Sie uns bitte mit, welche Alternativen Sie uns anbieten können.

Vielen Dank für Ihre rasche Rückmeldung.

Mit freundlichen Grüßen
[Ihr Name]
Einkauf [Firmenname]

### Nutzer 2
Kürzer und etwas wärmer

### Assistent 2
**Betreff:** Bitte um verbindlichen Liefertermin bis Freitag – 500 Dichtungsringe

Sehr geehrte Damen und Herren,

vielen Dank für die gute Zusammenarbeit. Leider hat sich die Lieferung der 500 Dichtungsringe nun schon zweimal verzögert. Wir benötigen die Ware spätestens am 15. für einen Kundenauftrag.

Könnten Sie uns bis Freitag, den [Datum], einen verbindlichen Liefertermin bestätigen? Das würde uns sehr helfen, verlässlich zu planen.

Herzlichen Dank im Voraus und viele Grüße

[Ihr Name]
Einkauf [Firmenname]

### Nutzer 3
Gib mir noch eine Variante, die mit einer Frage beginnt.

### Assistent 3
**Betreff:** Können Sie den Liefertermin bis Freitag verbindlich bestätigen?

Sehr geehrte Damen und Herren,

können Sie uns bis Freitag einen verbindlichen Liefertermin für die 500 Dichtungsringe nennen? Die Lieferung hat sich bereits zweimal verschoben, wir benötigen die Ware aber spätestens am 15. für einen Kundenauftrag.

Wir schätzen die Zusammenarbeit mit Ihnen und möchten gemeinsam eine verlässliche Lösung finden. Bitte teilen Sie uns mit, ob der 15. machbar ist. Andernfalls benötigen wir kurzfristig Alternativen.

Vielen Dank für Ihre Rückmeldung.

Mit freundlichen Grüßen
[Ihr Name]
Einkauf [Firmenname]

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1
Du bist Einkäuferin bei einem kleinen technischen Hersteller.
Unser Lieferant hat die Lieferung von 500 Dichtungsringen zum zweiten Mal um eine Woche verschoben.
Wir brauchen sie spätestens am 15. für einen Kundenauftrag.
Schreib eine E-Mail, in der du um einen verbindlichen Liefertermin bis Freitag bittest.
Höchstens 120 Wörter, freundlich, aber bestimmt, mit Betreffzeile, Sie-Form.
Der Ton soll ungefähr so sein: „Wir schätzen die Zusammenarbeit, brauchen jetzt aber Verlässlichkeit."

### Assistent 1
**Betreff:** Verbindlicher Liefertermin für 500 Dichtungsringe bis Freitag

Sehr geehrte Damen und Herren,

wir schätzen die Zusammenarbeit mit Ihnen sehr. Umso mehr überrascht uns, dass sich die Lieferung der 500 Dichtungsringe nun bereits zum zweiten Mal um eine Woche verschoben hat.

Wir benötigen die Ware spätestens am 15. für einen Kundenauftrag und brauchen jetzt Verlässlichkeit. Bitte bestätigen Sie uns daher bis Freitag schriftlich einen verbindlichen Liefertermin, der diesen Zeitpunkt einhält.

Sollte das nicht möglich sein, informieren Sie uns bitte umgehend, damit wir rechtzeitig Alternativen prüfen können.

Vielen Dank für Ihre Unterstützung.

Freundliche Grüße
[Name]
Einkauf
[Firma]

### Nutzer 2
Kürzer und etwas wärmer

### Assistent 2
**Betreff:** Verbindlicher Liefertermin für unsere 500 Dichtungsringe

Sehr geehrte Damen und Herren,

vielen Dank für die gute Zusammenarbeit, die wir sehr schätzen. Leider hat sich die Lieferung der 500 Dichtungsringe nun schon zum zweiten Mal verschoben.

Da wir die Ringe spätestens am 15. für einen Kundenauftrag benötigen, bitten wir Sie herzlich um die schriftliche Bestätigung eines verbindlichen Liefertermins bis Freitag. Gerne unterstützen wir Sie dabei, falls es etwas zu klären gibt.

Vielen Dank für Ihre Hilfe!

Freundliche Grüße
[Name]
Einkauf
[Firma]

### Nutzer 3
Gib mir noch eine Variante, die mit einer Frage beginnt.

### Assistent 3
**Betreff:** Verbindlicher Liefertermin für unsere 500 Dichtungsringe

Sehr geehrte Damen und Herren,

können wir bis Freitag mit einem verbindlichen Liefertermin für die 500 Dichtungsringe rechnen? Die Lieferung wurde bereits zweimal um eine Woche verschoben, und wir benötigen die Ringe spätestens am 15. für einen Kundenauftrag.

Wir schätzen die Zusammenarbeit mit Ihnen sehr, brauchen jetzt aber Verlässlichkeit. Bitte bestätigen Sie uns den Termin schriftlich, damit wir unseren Kunden verbindlich informieren können.

Herzlichen Dank für Ihre Unterstützung!

Freundliche Grüße
[Name]
Einkauf
[Firma]

---

## Gesprächsprotokoll: Opus

### Nutzer 1
Du bist Einkäuferin bei einem kleinen technischen Hersteller. (Rolle)
Unser Lieferant hat die Lieferung von 500 Dichtungsringen zum zweiten Mal um eine Woche verschoben.
Wir brauchen sie spätestens am 15. für einen Kundenauftrag. (Kontext)
Schreib eine E-Mail, in der du um einen verbindlichen Liefertermin bis Freitag bittest. (Aufgabe)
Höchstens 120 Wörter, freundlich, aber bestimmt, mit Betreffzeile, Sie-Form. (Format)
Der Ton soll ungefähr so sein: „Wir schätzen die Zusammenarbeit, brauchen jetzt aber Verlässlichkeit.“ (Beispiel)

### Assistent 1
**Betreff:** Bitte um verbindlichen Liefertermin – 500 Dichtungsringe

Sehr geehrte Damen und Herren,

wir schätzen die Zusammenarbeit mit Ihnen sehr. Die Lieferung der 500 Dichtungsringe ist nun aber bereits zum zweiten Mal um eine Woche verschoben worden, und jetzt brauchen wir Verlässlichkeit.

Wir benötigen die Ware spätestens am 15. für einen Kundenauftrag. Eine weitere Verschiebung können wir leider nicht auffangen.

Bitte bestätigen Sie uns deshalb bis Freitag einen verbindlichen Liefertermin. Falls der 15. aus Ihrer Sicht gefährdet ist, geben Sie uns bitte ebenfalls bis Freitag Bescheid, damit wir rechtzeitig planen können.

Vielen Dank für Ihre Unterstützung.

Mit freundlichen Grüßen

[Ihr Name]
Einkauf
[Firmenname]
[Telefon]

*(ca. 100 Wörter)*

### Nutzer 2
Kürzer und etwas wärmer

### Assistent 2
**Betreff:** Liefertermin Dichtungsringe – kurze Bitte

Sehr geehrte Damen und Herren,

wir arbeiten gern mit Ihnen zusammen und wissen, dass Verschiebungen nicht immer zu vermeiden sind. Da sich die Lieferung der 500 Dichtungsringe nun aber schon zum zweiten Mal verzögert, brauchen wir jetzt Planungssicherheit: Wir benötigen die Ware spätestens am 15. für einen Kundenauftrag.

Könnten Sie uns bis Freitag einen verbindlichen Liefertermin bestätigen? Das würde uns sehr helfen.

Herzlichen Dank und viele Grüße

[Ihr Name]
Einkauf, [Firmenname]

*(ca. 70 Wörter)*

### Nutzer 3
Gib mir noch eine Variante, die mit einer Frage beginnt.

### Assistent 3
**Betreff:** Können wir mit dem 15. rechnen? – 500 Dichtungsringe

Sehr geehrte Damen und Herren,

können wir uns auf eine Lieferung der 500 Dichtungsringe bis spätestens zum 15. verlassen? Wir brauchen die Ware für einen Kundenauftrag. Da sich der Termin bereits zweimal verschoben hat, ist uns Planungssicherheit jetzt besonders wichtig.

Wir schätzen die Zusammenarbeit mit Ihnen sehr. Bitte bestätigen Sie uns deshalb bis Freitag einen verbindlichen Liefertermin.

Vielen Dank für Ihre Mühe und herzliche Grüße

[Ihr Name]
Einkauf, [Firmenname]

*(ca. 75 Wörter)*
