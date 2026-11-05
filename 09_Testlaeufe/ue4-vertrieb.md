# Testlauf: Übung 4 / Rolle Vertrieb – Nachfass-Mail nach der Messe

**Herkunft:** [Uebung_4_Eigene_Aufgabe.md](../06_Uebungen/Uebung_4_Eigene_Aufgabe.md), [Ideenliste nach Rollen → Vertrieb](../06_Uebungen/Uebung_4_Eigene_Aufgabe.md#vertrieb) („Nachfass-Mail nach einer Messe oder einem Termin schreiben“). Der Prompt folgt der Vorlage aus Schritt 3, die Nachbesserungen stammen wörtlich aus Schritt 4. Zugehörige Lösungshinweise: [Trainer-Loesungshinweise.md – Übung 4](../06_Uebungen/Trainer-Loesungshinweise.md#übung-4-eigene-aufgabe). Dort gibt es keinen eigenen Musterprompt für Vertriebs-Mails.

**Testdatum:** Montag, 2. November 2026

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf (5 Turns, jeweils in einem neuen Chat):**

1. Baukasten-Prompt (Rolle, Kontext, Aufgabe, Format, Beispiel, „stell mir zuerst Rückfragen“), siehe Protokolle unten
2. Antwort auf die Rückfragen: Platzhalter [ANSPRECHPARTNER], [MEIN NAME], [TERMIN 1], [TERMIN 2], keine Preise
3. „Der Ton ist zu förmlich. Schreib lockerer, aber trotzdem professionell.“
4. „Gib mir drei unterschiedliche Varianten, damit ich auswählen kann.“
5. „Was müsste ich dir noch sagen, damit das Ergebnis besser wird?“

**Daten-Ampel des Szenarios:** grün. Der Kunde ist als „Kunde A“ anonymisiert, es gibt keine Preise, Namen oder Konstruktionsdaten. Die Messe („Industrietage“) und die Serienbezeichnung SG-40 sind unkritisch.

**Was laut Material herauskommen soll:** Eine sachliche, technikgerechte Nachfass-Mail mit Platzhaltern, ohne Preise und ohne erfundene Produkteigenschaften. Dazu mindestens zwei Iterationen und am Ende eine Reflexion, welches Firmenwissen der KI fehlt (Reflexionsfrage 2 auf dem Übungsblatt).

---

## Bewertung

Wortzahlen per `python3` nachgezählt (Leerzeichen-getrennt, inklusive Betreff, Anrede und Gruß, ohne Kommentare der Modelle).

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Turn 1: stellt zuerst Rückfragen | ja, 7 Fragen, schlägt Platzhalter selbst vor | ja, 7 Fragen, sehr ausführlich | ja, 6 Fragen. Fragt als einziges, ob die SG-40 IP66 **serienmäßig** erfüllt |
| Turn 2: Betreffzeile | ja | ja | ja |
| Turn 2: Wortzahl ≤ 150 | 90 | 117 (selbst angegeben: „ca. 100“) | 105 (selbst angegeben: „ca. 110“) |
| Turn 2: per Sie, keine Werbefloskeln | ja | ja | ja |
| Turn 2: Bezug Messegespräch | ja | ja | ja (Stand, Industrietage) |
| Turn 2: SG-40 | ja | ja | ja |
| Turn 2: IP66 / Außeneinsatz | **nein, fehlt beides** | ja | ja |
| Turn 2: ca. 300 Stück/Jahr | ja | ja | ja |
| Turn 2: Datenblätter im Anhang | ja | ja | ja |
| Turn 2: Angebot bis Ende nächster Woche | ja | ja | ja |
| Turn 2: Telefontermin [TERMIN 1]/[TERMIN 2] | ja, mit „nächsten zwei Wochen“ | ja, mit „nächsten zwei Wochen“ | ja, aber **ohne** „nächsten zwei Wochen“ |
| Turn 2: Preise/Rabatte | keine | keine | keine |
| Turn 2: Erfundene Produktdaten | keine | leichte Annahme: „Sie enthalten die technischen Daten zur Schutzart IP66“ | keine; weist ausdrücklich darauf hin, IP66 im Datenblatt zu prüfen |
| Turn 3: lockerer, aber professionell | ja („Hallo“, „danke nochmal“) | nur leicht („Guten Tag“, sonst ähnlich) | ja („Hallo“, „SG-40 für draußen“), bleibt per Sie |
| Turn 3: Wortzahl | 80 | 114 (selbst: „ca. 105“) | 103 (selbst: „ca. 100“) |
| Turn 4: drei unterschiedliche Varianten | ja (kurz / locker / technisch). Zwei davon wieder förmlich, d. h. Turn-3-Wunsch teils vergessen | ja (kurz / technisch / persönlich), alle „Guten Tag“ | ja (kurz / technisch / persönlich), alle locker, plus Empfehlung für den Techniker-Leser |
| Turn 4: Wortzahlen | 75 / 80 / 97 | 60 / 99 / 82 | 58 / 94 / 90 (selbst: „ca. 70 / 115 / 105“) |
| Turn 4: Erfundenes / Annahmen | V2-Betreff „Ihre Anfrage … – Unterlagen folgen“ (falsch: Unterlagen hängen an); V3 behauptet IP66 als Produkteigenschaft | VB: „dafür passt die SG-40 gut“ (Eignungszusage); VC: „Danke für Ihre offenen Fragen“ (selbst als Annahme markiert) | V2: Datenblätter „mit allen Angaben zu … Material und Abmessungen“, „15 Minuten“; V3: „Ihr Projekt“, „Angebot ist in Arbeit“ |
| Turn 5: sinnvolle Liste fehlender Infos | ja, aber kurz und teils redundant (Namen, Termine, Platzhalter); Punkt 6 widersprüchlich | ja, 9 Punkte, u. a. Gesprächsdetails, technische Eckdaten, Kundensituation, Formalia, „Vermeidenswertes“ (Lieferzeiten, Rabatte) | ja, 8 Punkte, priorisiert („vor allem 1 bis 3“); u. a. IP66 serienmäßig?, Alleinstellungsmerkmale, Lieferzeiten, konkretes Datum, Signatur |
| Gesamt | brauchbar, aber dünn und mit Lücken | solide, kleine Grammatikfehler | am stärksten, kleine Ausschmückungen in den Varianten |

**Gesamturteil:** Die Übung funktioniert wie gedacht. Alle drei Modelle stellen auf den Rückfragen-Satz hin zuerst Fragen, liefern danach eine verwendbare Mail unter 150 Wörtern ohne Preise und reagieren sichtbar auf jede Nachbesserung. Die Unterschiede liegen im Detail: Haiku lässt im ersten Entwurf die zentrale Anforderung IP66/Außeneinsatz weg, Sonnet und Opus nehmen sie auf. In den Varianten (Turn 4) schmücken alle drei Modelle leicht aus. Genau das sollen die Teilnehmenden beim Prüfen finden.

---

## Gefundene Fehler mit Beleg

| # | Modell / Turn | Fehler | Beleg |
|---|---|---|---|
| 1 | Haiku, Turn 2 und 3 | **Pflichtinhalt fehlt:** IP66 und Außeneinsatz werden nicht erwähnt. Für den Techniker ist das aber der Kern der Anfrage. | Prompt: „für den Außeneinsatz, braucht Schutzart IP66“. Haiku T2: „Wie besprochen sende ich Ihnen die Datenblätter zur Gehäuseserie SG-40 im Anhang.“ Kein IP66. Erst in Variante 3 (Turn 4) taucht IP66 auf. |
| 2 | Haiku V3, Sonnet T2/T3/VB, Opus V2 | **Produkteigenschaft als Tatsache dargestellt.** Der Prompt sagt nur, dass der Kunde IP66 *braucht*. Dass die SG-40 IP66 erfüllt oder dass die Datenblätter das ausweisen, steht nirgends. | Haiku V3: „SG-40 …, die für den Außeneinsatz mit Schutzart IP66 vorgesehen ist“. Sonnet T2: „Sie enthalten die technischen Daten zur Schutzart IP66“. Sonnet VB: „dafür passt die SG-40 gut“. Opus hat das Problem selbst erkannt (Rückfrage 6, Hinweis nach T2: „Bitte prüfen Sie vor dem Versand, ob die Datenblätter IP66 … tatsächlich ausweisen“), schreibt es in T3 und V2 aber trotzdem als Tatsache. |
| 3 | Opus V2 | **Inhalt der Datenblätter erfunden**, dazu eine Gesprächsdauer, die nicht vorgegeben war. | „Datenblätter zur SG-40 mit allen Angaben zu Schutzart IP66, Material und Abmessungen“. Material und Abmessungen kommen im Prompt nicht vor. Dazu „Telefonat von etwa 15 Minuten“. |
| 4 | Opus V3, Sonnet VC | **Gesprächsinhalte unterstellt.** | Opus V3: „Ihr Projekt für den Außeneinsatz ist mir im Kopf geblieben“, „Angebot … ist in Arbeit“. Sonnet VC: „Danke für Ihre offenen Fragen“. Sonnet markiert das selbst: „Variante C setzt voraus, dass der Kunde … tatsächlich Fragen gestellt hat.“ |
| 5 | Haiku V2 | **Betreff widerspricht dem Inhalt.** | Betreff „Ihre Anfrage zur SG-40 – Unterlagen folgen“. Im Text hängen die Datenblätter aber schon an („hängen die Datenblätter zur SG-40 an dieser Mail“). Außerdem war es ein Messegespräch und keine schriftliche „Anfrage“. |
| 6 | Sonnet T3, VA, VC | **Grammatik:** „Industrietage“ ist Plural. | „an unserem Stand auf der Industrietage“, „Gespräch auf der Industrietage“, „Nachgefasst nach der Industrietage“. Richtig wäre „auf den Industrietagen“ / „nach den Industrietagen“. In T2 schreibt Sonnet noch korrekt „auf der Messe Industrietage“. |
| 7 | Sonnet T2/T3, Opus T2/T3/V1–V3 | **Selbst angegebene Wortzahlen ungenau.** Unkritisch, weil alle Mails unter 150 Wörtern bleiben, aber ein gutes Beispiel dafür, dass Zählen keine Stärke der KI ist. | Nachgezählt per `python3`: Sonnet T2 117 statt „ca. 100“. Opus V1 58 statt „ca. 70“, V2 94 statt „ca. 115“, V3 90 statt „ca. 105“. |
| 8 | Haiku, Turn 4 | **Nachbesserung aus Turn 3 teils vergessen.** | Variante 1 und 3 beginnen wieder mit „Sehr geehrte/r“ und enden mit „Mit freundlichen Grüßen“, obwohl in Turn 3 „zu förmlich“ beanstandet wurde. Man kann das als bewusste Bandbreite lesen, Haiku sagt dazu aber nichts. |
| 9 | Haiku, Turn 5 | **Widersprüchlicher Punkt.** | „6. Tonfall: Ob Sie eher die Variante mit Du-Ansprache oder die förmlichere Form bevorzugen. Das haben wir mit Sie bereits geklärt.“ Keine Variante war per Du. Der Punkt stellt eine Frage und beantwortet sie im selben Atemzug. |
| 10 | alle, Turn 2 ff. | **Unschöne Anrede mit Platzhalter.** | Haiku/Sonnet: „Sehr geehrte/r [ANSPRECHPARTNER],“. Ersetzt man den Platzhalter durch „Herr Müller“, entsteht „Sehr geehrte/r Herr Müller“. Das Modell setzt den Platzhalter nur mechanisch ein. Die Ursache liegt in der Platzhalter-Vorgabe aus Turn 2 (siehe „Probleme im Material“). |
| 11 | Opus T2, T3, V1–V3 | **Kleine Lücke:** „in den nächsten zwei Wochen“ fehlt. | Opus nennt nur [TERMIN 1]/[TERMIN 2] bzw. „einen anderen Zeitpunkt“. Der Zeitrahmen aus der Aufgabe steht nicht in der Mail. Das ist vertretbar, weil die Platzhalter ihn abdecken. |

Keine Preise, Rabatte, Lieferzeiten oder erfundenen Zertifikate in irgendeiner Mail. Die Vorgabe „Preise nennen wir in der Mail nicht“ wurde von allen eingehalten.

---

## Lehren für die Auswertung

1. **Der Rückfragen-Satz wirkt.** Alle drei Modelle schreiben in Turn 1 noch keine Mail, sondern fragen nach. Das ist ein gutes Live-Beispiel für den Tipp in Schritt 3. Man sieht aber auch: Ohne Turn 2 („Platzhalter genügen, bitte schreib jetzt“) bekommt man nichts. Teilnehmende sollten wissen, dass sie die Fragen auch pauschal beantworten dürfen.
2. **Die beste Rückfrage ist die fachliche.** Nur Opus fragt: „Erfüllt die SG-40 IP66 serienmäßig, oder hängt das von der Ausführung ab?“ Genau an dieser Stelle schreiben die anderen Modelle später eine Produkteigenschaft als Tatsache hin. Daran lässt sich der Satz „Woher weißt du, dass das stimmt?“ aus den Lösungshinweisen gut zeigen.
3. **Varianten laden zum Ausschmücken ein.** Je „persönlicher“ oder „technischer“ eine Variante sein soll, desto mehr erfinden die Modelle: Projekt, offene Fragen, Material, Abmessungen, 15 Minuten. Die Lehre: Bei „gib mir Varianten“ jede Variante Satz für Satz gegen das prüfen, was man wirklich gesagt und versprochen hat (Bewertungsraster: „falsche Zusagen an Kunden?“).
4. **Fehlende Pflichtinhalte fallen nur beim Abhaken auf.** Haikus erster Entwurf liest sich gut, lässt aber IP66 weg. Tipp für die Teilnehmenden: Die Punkte aus dem eigenen Prompt als Checkliste neben die Mail legen.
5. **Turn 5 liefert genau die Antwort auf Reflexionsfrage 2.** Die Listen nennen das Firmenwissen, das der KI fehlt: Gesprächsdetails, technische Eckdaten und Ausführungen der SG-40, Alleinstellungsmerkmale, Lieferzeiten, Signatur. Opus priorisiert („vor allem 1 bis 3“), Sonnet nennt zusätzlich „Vermeidenswertes“ (keine Zusagen zu Lieferzeiten oder Rabatten). Diese Listen eignen sich gut für die 2-Minuten-Vorstellung.
6. **„Lockerer“ bedeutet bei jedem Modell etwas anderes.** Sonnet wechselt nur von „Sehr geehrte/r“ zu „Guten Tag“, Haiku und Opus gehen auf „Hallo“. Haiku fällt in den Varianten teilweise wieder ins Förmliche zurück. Wer einen bestimmten Ton will, sollte ein Beispiel mitgeben (Baustein „Beispiel“).
7. **Wortzahlen der KI nicht glauben.** Die Selbstauskünfte („ca. 115 Wörter“ bei tatsächlich 94) passen zu Demo 4b (Zählen). Bei harten Grenzen selbst zählen, z. B. mit der Wortzählung im Mailprogramm.
8. **Ergebnis für das Bewertungsraster:** realistisch „Zeit gespart 4“, „Qualität 4“, „Korrektheit 3–4“ (nach Prüfung), „Risiken gering“ (IP66-Aussage und erfundene Details vor Versand streichen), „Prompt wiederverwendbar: ja“.

---

## Probleme im Material und Vorschläge

- **Kein Musterprompt für Vertriebsmails in den Lösungshinweisen.** Unter „Musterprompts für häufige Aufgaben“ gibt es Standardantwort, Excel, Anleitung und Statusbericht. Eine Nachfass-Mail fehlt, obwohl sie in der Ideenliste steht und vermutlich häufig gewählt wird. Der hier getestete Prompt hat gut funktioniert und kann direkt übernommen werden.
- **Platzhalter für die Anrede.** Mit [ANSPRECHPARTNER] entstehen Anreden wie „Sehr geehrte/r [ANSPRECHPARTNER]“. Besser wären [ANREDE] [NACHNAME] oder ein Hinweis, die Anrede selbst anzupassen.
- **Prüfhinweis zu Produkteigenschaften fehlt.** Beim Marketing steht „Behauptungen über Produkte, Zahlen und Zitate immer selbst prüfen“, beim Vertrieb nicht. Der Test zeigt, dass gerade beim Vertrieb Produkteigenschaften und Gesprächsinhalte unterstellt werden.
- Zeitplan und Anleitung passen: Die 5 Turns sind in etwa 10–12 Minuten Tippzeit machbar, das Lesen und Prüfen der drei Varianten kostet am meisten Zeit.

---

## Gesprächsprotokolle

### Haiku

#### Nutzer 1

Du bist erfahrener Vertriebsmitarbeiter im Außendienst.

Kontext: Wir sind ein kleiner technischer Hersteller von robusten Steuergehäusen. Auf der Messe Industrietage hatte ich ein gutes Gespräch mit dem technischen Einkäufer eines Maschinenbauers (im Folgenden Kunde A). Er interessiert sich für unsere Gehäuseserie SG-40 für den Außeneinsatz, braucht Schutzart IP66 und etwa 300 Stück pro Jahr. Ich habe ihm Datenblätter und ein unverbindliches Angebot versprochen. Er ist Techniker, kein Marketingmensch, und liest die Mail selbst.

Aufgabe: Schreib eine Nachfass-Mail, die an das Gespräch anknüpft, die Datenblätter im Anhang ankündigt, das Angebot bis Ende nächster Woche in Aussicht stellt und einen kurzen Telefontermin in den nächsten zwei Wochen vorschlägt.

Format: Max. 150 Wörter, mit Betreffzeile, per Sie, sachlich und freundlich, keine Werbefloskeln.

Beispiel (so soll es ungefähr aussehen):
"Vielen Dank für das gute Gespräch an unserem Stand. Wie besprochen sende ich Ihnen …"

Wenn dir Informationen fehlen, stell mir zuerst Rückfragen, bevor du loslegst.

#### Assistent 1

Ich habe noch ein paar Fragen, damit die Mail passt:

1. Wie heißt der technische Einkäufer (Anrede und Name)? Soll ich bis dahin [ANSPRECHPARTNER] stehen lassen?
2. Wie heißen Sie und wie lautet Ihre Funktion? Soll ich [MEIN NAME] stehen lassen?
3. Wie heißt das Unternehmen des Kunden? Soll ich es in der Betreffzeile nennen?
4. Wie heißen die Datenblätter-Dateien bzw. welche Unterlagen hängen Sie an?
5. Gibt es Termine, die Sie vorschlagen möchten? Sonst nutze ich [TERMIN 1] und [TERMIN 2].
6. Gibt es ein konkretes Thema aus dem Gespräch, auf das ich Bezug nehmen soll (z. B. Befestigung, Dichtung, Montage, Temperaturbereich)?
7. Sollen Preise erwähnt werden oder nicht?

Mit diesen Angaben schreibe ich den Entwurf.

#### Nutzer 2

Zu möglichen Rückfragen: Namen bitte als [ANSPRECHPARTNER] und [MEIN NAME], Terminvorschläge als [TERMIN 1] und [TERMIN 2]. Preise nennen wir in der Mail nicht. Bitte schreib jetzt den Entwurf.

#### Assistent 2

**Betreff:** Steuergehäuse SG-40 – Datenblätter und Angebot

Sehr geehrte/r [ANSPRECHPARTNER],

vielen Dank für das gute Gespräch auf den Industrietagen. Wie besprochen sende ich Ihnen die Datenblätter zur Gehäuseserie SG-40 im Anhang.

Für Ihren Bedarf von etwa 300 Stück pro Jahr erstellen wir Ihnen ein unverbindliches Angebot. Sie erhalten es bis Ende nächster Woche.

Gerne besprechen wir die Details kurz telefonisch. Hätten Sie Zeit am [TERMIN 1] oder am [TERMIN 2]? Gern nehme ich auch einen anderen Termin in den nächsten zwei Wochen, der Ihnen besser passt.

Mit freundlichen Grüßen
[MEIN NAME]

#### Nutzer 3

Der Ton ist zu förmlich. Schreib lockerer, aber trotzdem professionell.

#### Assistent 3

**Betreff:** SG-40 – Datenblätter und Angebot

Hallo [ANSPRECHPARTNER],

danke nochmal für das gute Gespräch auf den Industrietagen. Wie besprochen hängen die Datenblätter zur SG-40 an dieser Mail.

Für die rund 300 Stück im Jahr bekommen Sie von uns ein unverbindliches Angebot, und zwar bis Ende nächster Woche.

Lassen Sie uns die Details kurz am Telefon durchgehen. Passt Ihnen [TERMIN 1] oder [TERMIN 2]? Falls nicht, nennen Sie mir gern einen anderen Zeitpunkt in den nächsten zwei Wochen.

Viele Grüße
[MEIN NAME]

#### Nutzer 4

Gib mir drei unterschiedliche Varianten, damit ich auswählen kann.

#### Assistent 4

**Variante 1: Kurz und direkt**

**Betreff:** SG-40 – Datenblätter und Angebot

Sehr geehrte/r [ANSPRECHPARTNER],

vielen Dank für das Gespräch auf den Industrietagen. Wie besprochen finden Sie die Datenblätter zur SG-40 im Anhang.

Das unverbindliche Angebot für Ihren Bedarf von rund 300 Stück pro Jahr erhalten Sie bis Ende nächster Woche.

Für eine kurze Abstimmung am Telefon schlage ich [TERMIN 1] oder [TERMIN 2] vor. Alternativ nennen Sie mir gern einen Zeitpunkt in den nächsten zwei Wochen.

Mit freundlichen Grüßen
[MEIN NAME]

**Variante 2: Locker und persönlich**

**Betreff:** Ihre Anfrage zur SG-40 – Unterlagen folgen

Hallo [ANSPRECHPARTNER],

danke nochmal für das nette Gespräch auf den Industrietagen. Wie versprochen hängen die Datenblätter zur SG-40 an dieser Mail.

Das unverbindliche Angebot für Ihre rund 300 Stück pro Jahr folgt bis Ende nächster Woche.

Am einfachsten klären wir offene Punkte kurz am Telefon. Wie wäre es mit [TERMIN 1] oder [TERMIN 2]? Falls es nicht passt, finden wir gern einen anderen Termin in den nächsten zwei Wochen.

Viele Grüße
[MEIN NAME]

**Variante 3: Technisch orientiert**

**Betreff:** SG-40 für den Außeneinsatz (IP66) – Datenblätter und Angebot

Sehr geehrte/r [ANSPRECHPARTNER],

vielen Dank für das Gespräch auf den Industrietagen. Wie besprochen sende ich Ihnen die Datenblätter zur Gehäuseserie SG-40 im Anhang, die für den Außeneinsatz mit Schutzart IP66 vorgesehen ist.

Für Ihren Bedarf von etwa 300 Stück pro Jahr erstelle ich ein unverbindliches Angebot, das Sie bis Ende nächster Woche erhalten.

Für Rückfragen zu Ihren Anforderungen wäre ein kurzer Telefontermin hilfreich. Ich schlage [TERMIN 1] oder [TERMIN 2] vor. Alternativ passt mir auch ein anderer Zeitpunkt in den nächsten zwei Wochen.

Mit freundlichen Grüßen
[MEIN NAME]

#### Nutzer 5

Was müsste ich dir noch sagen, damit das Ergebnis besser wird?

#### Assistent 5

Damit die Mail stärker wird, helfen mir diese Angaben:

1. **Namen:** Anrede und Name des Einkäufers sowie Ihr Name und Ihre Funktion, damit ich die Platzhalter ersetzen kann.
2. **Gesprächsinhalt:** Ein bis zwei konkrete Punkte aus dem Gespräch, etwa eine Anforderung an Dichtung, Befestigung, Temperaturbereich oder Montage. Dann wirkt die Mail weniger allgemein.
3. **Anhang:** Die genauen Namen der Datenblätter, damit ich sie benennen kann.
4. **Angebot:** Ob es als PDF per Mail oder nach einem Telefonat kommt und ob es bereits vorbereitet ist. So kann ich das Versprechen präziser formulieren.
5. **Termine:** Konkrete Zeitfenster, die Sie anbieten können.
6. **Tonfall:** Ob Sie eher die Variante mit Du-Ansprache oder die förmlichere Form bevorzugen. Das haben wir mit Sie bereits geklärt.
7. **Kunde:** Firmenname und, falls bekannt, Projekt oder Einsatzort. Der Einkäufer liest die Mail selbst, daher sind Fakten wichtiger als Floskeln.

Mit diesen Angaben kann ich die Mail genauer auf Ihr Gespräch und Ihren Stil zuschneiden.

---

### Sonnet

#### Nutzer 1

Du bist erfahrener Vertriebsmitarbeiter im Außendienst.

Kontext: Wir sind ein kleiner technischer Hersteller von robusten Steuergehäusen. Auf der Messe Industrietage hatte ich ein gutes Gespräch mit dem technischen Einkäufer eines Maschinenbauers (im Folgenden Kunde A). Er interessiert sich für unsere Gehäuseserie SG-40 für den Außeneinsatz, braucht Schutzart IP66 und etwa 300 Stück pro Jahr. Ich habe ihm Datenblätter und ein unverbindliches Angebot versprochen. Er ist Techniker, kein Marketingmensch, und liest die Mail selbst.

Aufgabe: Schreib eine Nachfass-Mail, die an das Gespräch anknüpft, die Datenblätter im Anhang ankündigt, das Angebot bis Ende nächster Woche in Aussicht stellt und einen kurzen Telefontermin in den nächsten zwei Wochen vorschlägt.

Format: Max. 150 Wörter, mit Betreffzeile, per Sie, sachlich und freundlich, keine Werbefloskeln.

Beispiel (so soll es ungefähr aussehen):
"Vielen Dank für das gute Gespräch an unserem Stand. Wie besprochen sende ich Ihnen …"

Wenn dir Informationen fehlen, stell mir zuerst Rückfragen, bevor du loslegst.

#### Assistent 1

Gern. Bevor ich den Entwurf schreibe, brauche ich noch ein paar Angaben:

1. **Ansprechpartner:** Wie heißt der Einkäufer, und wie soll er angesprochen werden (Herr/Frau plus Nachname)? Wie lautet Ihr Name samt Funktion und Signatur?
2. **Gesprächsinhalt:** Was wurde am Stand konkret besprochen? Gab es technische Details wie Maße, Material, Temperaturbereich oder Zubehör? Ein oder zwei konkrete Anknüpfungspunkte machen die Mail persönlicher.
3. **Datenblätter:** Welche genau hängen an (SG-40 Datenblatt, IP66-Nachweis, Zeichnungen, Zertifikate)? In welchem Format?
4. **Angebot:** Soll die Mail Preise, Staffeln oder Lieferzeiten erwähnen oder nur das Angebot ankündigen? Soll die Jahresmenge von ca. 300 Stück genannt werden?
5. **Telefontermin:** Haben Sie konkrete Terminvorschläge (Tage und Uhrzeiten)? Wie lange soll das Telefonat dauern, und wer ruft wen an?
6. **Offene Punkte:** Gibt es Fragen des Kunden, die Sie noch klären müssen, zum Beispiel Sonderausführungen, Lieferzeit oder Muster?
7. **Weitere Wünsche:** Soll die Mail eine Gesprächsnotiz-Referenz, ein Muster-Angebot oder einen Hinweis auf Prüfzeugnisse enthalten? Soll Ihre Firma im Betreff genannt werden?

Wenn Sie möchten, kann ich auch mit Platzhaltern arbeiten, die Sie später ersetzen.

#### Nutzer 2

Zu möglichen Rückfragen: Namen bitte als [ANSPRECHPARTNER] und [MEIN NAME], Terminvorschläge als [TERMIN 1] und [TERMIN 2]. Preise nennen wir in der Mail nicht. Bitte schreib jetzt den Entwurf.

#### Assistent 2

**Betreff:** SG-40 für den Außeneinsatz – Datenblätter und Angebot

Sehr geehrte/r [ANSPRECHPARTNER],

vielen Dank für das gute Gespräch auf der Messe Industrietage. Gern knüpfe ich an Ihre Anfrage zur Gehäuseserie SG-40 an.

Wie besprochen erhalten Sie die Datenblätter im Anhang. Sie enthalten die technischen Daten zur Schutzart IP66 für den Außeneinsatz. Auf Basis Ihres Jahresbedarfs von etwa 300 Stück erstelle ich Ihnen ein unverbindliches Angebot und sende es Ihnen bis Ende nächster Woche zu.

Für Rückfragen und die Abstimmung technischer Details schlage ich ein kurzes Telefonat in den nächsten zwei Wochen vor, zum Beispiel am [TERMIN 1] oder am [TERMIN 2]. Falls Ihnen ein anderer Termin besser passt, richte ich mich gern danach.

Mit freundlichen Grüßen
[MEIN NAME]

*(ca. 100 Wörter. Anlage: Datenblätter SG-40)*

#### Nutzer 3

Der Ton ist zu förmlich. Schreib lockerer, aber trotzdem professionell.

#### Assistent 3

**Betreff:** SG-40 für den Außeneinsatz – Datenblätter und Angebot

Guten Tag [ANSPRECHPARTNER],

vielen Dank für das gute Gespräch an unserem Stand auf der Industrietage. Es hat mich gefreut, mit Ihnen über die SG-40 und Ihren Bedarf für den Außeneinsatz zu sprechen.

Die Datenblätter hängen wie versprochen an dieser Mail, inklusive der Angaben zu IP66. Das unverbindliche Angebot für Ihre ca. 300 Stück pro Jahr schicke ich Ihnen bis Ende nächster Woche.

Wenn Sie mögen, sprechen wir in den nächsten zwei Wochen kurz am Telefon, etwa am [TERMIN 1] oder am [TERMIN 2]. Dann können wir offene technische Fragen direkt klären. Sagen Sie mir gern Bescheid, falls ein anderer Termin besser passt.

Viele Grüße
[MEIN NAME]

*(ca. 105 Wörter. Anlage: Datenblätter SG-40)*

#### Nutzer 4

Gib mir drei unterschiedliche Varianten, damit ich auswählen kann.

#### Assistent 4

Hier sind drei Varianten mit unterschiedlichem Schwerpunkt. Alle haben unter 150 Wörter und verwenden Ihre Platzhalter.

**Variante A: kurz und direkt**

**Betreff:** SG-40: Datenblätter im Anhang, Angebot folgt

Guten Tag [ANSPRECHPARTNER],

danke für das Gespräch auf der Industrietage. Anbei die Datenblätter zur SG-40 (IP66, Außeneinsatz). Das unverbindliche Angebot für Ihre ca. 300 Stück pro Jahr bekommen Sie bis Ende nächster Woche.

Passt Ihnen ein kurzes Telefonat in den nächsten zwei Wochen, etwa am [TERMIN 1] oder [TERMIN 2]?

Viele Grüße
[MEIN NAME]

**Variante B: technisch orientiert**

**Betreff:** SG-40 für Ihren Außeneinsatz: Unterlagen und nächste Schritte

Guten Tag [ANSPRECHPARTNER],

vielen Dank für das Gespräch an unserem Stand. Sie suchen ein Gehäuse mit Schutzart IP66 für den Außeneinsatz, und dafür passt die SG-40 gut. Die Datenblätter mit den technischen Daten finden Sie im Anhang. Bitte prüfen Sie, ob alle für Sie wichtigen Angaben enthalten sind. Falls etwas fehlt, ergänze ich es gern.

Das unverbindliche Angebot für ca. 300 Stück pro Jahr erhalten Sie bis Ende nächster Woche. Technische Details besprechen wir am besten kurz am Telefon, zum Beispiel am [TERMIN 1] oder [TERMIN 2].

Viele Grüße
[MEIN NAME]

**Variante C: persönlich, mit Gesprächsbezug**

**Betreff:** Nachgefasst nach der Industrietage: SG-40 und Angebot

Guten Tag [ANSPRECHPARTNER],

unser Gespräch auf der Industrietage ist mir gut in Erinnerung geblieben. Danke für Ihre offenen Fragen zur SG-40 und zu Ihren Anforderungen im Außeneinsatz.

Wie versprochen schicke ich Ihnen die Datenblätter im Anhang. Das unverbindliche Angebot folgt bis Ende nächster Woche. Wenn Sie vorher Fragen haben, melden Sie sich jederzeit.

Wollen wir uns in den nächsten zwei Wochen kurz telefonisch abstimmen, etwa am [TERMIN 1] oder [TERMIN 2]?

Viele Grüße
[MEIN NAME]

Hinweis: Variante C setzt voraus, dass der Kunde im Gespräch tatsächlich Fragen gestellt hat. Sonst bitte den Satz anpassen.

#### Nutzer 5

Was müsste ich dir noch sagen, damit das Ergebnis besser wird?

#### Assistent 5

Mit diesen Informationen könnte ich die Mail deutlich konkreter und überzeugender machen:

1. **Gesprächsdetails:** Was hat den Kunden am meisten beschäftigt, zum Beispiel Wetterfestigkeit, Montage, Maße, Temperaturbereich oder Lieferzeit? Ein konkreter Bezug wirkt auf einen Techniker besser als eine allgemeine Dankesformel.
2. **Technische Eckdaten der SG-40:** Material, Maße, Schutzart und weitere Normen wie IK-Schutz, UV-Beständigkeit oder Temperaturbereich. Dann kann ich einzelne Argumente nennen, ohne etwas zu erfinden.
3. **Inhalt des Anhangs:** Welche Dokumente sind es genau, und wie heißen sie? Dann kann ich sie korrekt benennen.
4. **Kundensituation:** Ist es ein Erstkontakt oder besteht schon eine Geschäftsbeziehung? Gibt es einen Wettbewerber oder eine bestehende Lösung, die er ersetzen will?
5. **Ziel der Mail:** Soll vor allem der Telefontermin zustande kommen, oder soll das Angebot im Vordergrund stehen? Davon hängt ab, was ich an den Anfang stelle.
6. **Zeitrahmen des Kunden:** Gibt es einen Projektstart oder Liefertermin? Das könnte ich in der Mail aufgreifen.
7. **Ton und Stil:** Wie schreiben Sie üblicherweise, und wie sprach der Kunde mit Ihnen? Ein Beispiel einer früheren Mail von Ihnen hilft mir, Ihren Stil zu treffen.
8. **Formalia:** Signatur, Firmenname, Telefonnummer und gegebenenfalls ein Link zu einem Online-Terminkalender.
9. **Vermeidenswertes:** Gibt es Formulierungen oder Zusagen, die Sie nicht machen möchten, etwa zu Lieferzeiten oder Rabatten?

Mit diesen Angaben passe ich den Entwurf an und streiche die Platzhalter, wo es geht.

---

### Opus

#### Nutzer 1

Du bist erfahrener Vertriebsmitarbeiter im Außendienst.

Kontext: Wir sind ein kleiner technischer Hersteller von robusten Steuergehäusen. Auf der Messe Industrietage hatte ich ein gutes Gespräch mit dem technischen Einkäufer eines Maschinenbauers (im Folgenden Kunde A). Er interessiert sich für unsere Gehäuseserie SG-40 für den Außeneinsatz, braucht Schutzart IP66 und etwa 300 Stück pro Jahr. Ich habe ihm Datenblätter und ein unverbindliches Angebot versprochen. Er ist Techniker, kein Marketingmensch, und liest die Mail selbst.

Aufgabe: Schreib eine Nachfass-Mail, die an das Gespräch anknüpft, die Datenblätter im Anhang ankündigt, das Angebot bis Ende nächster Woche in Aussicht stellt und einen kurzen Telefontermin in den nächsten zwei Wochen vorschlägt.

Format: Max. 150 Wörter, mit Betreffzeile, per Sie, sachlich und freundlich, keine Werbefloskeln.

Beispiel (so soll es ungefähr aussehen):
"Vielen Dank für das gute Gespräch an unserem Stand. Wie besprochen sende ich Ihnen …"

Wenn dir Informationen fehlen, stell mir zuerst Rückfragen, bevor du loslegst.

#### Assistent 1

Gerne. Bevor ich den Entwurf schreibe, habe ich ein paar kurze Rückfragen:

1. **Namen:** Wie heißt Ihr Ansprechpartner (und wie soll er angesprochen werden, z. B. „Herr …“)? Mit welchem Namen und welcher Funktion unterschreiben Sie?
2. **Termine:** Welche zwei oder drei konkreten Zeitfenster für das Telefonat kann ich vorschlagen?
3. **Preise:** Sollen in der Mail schon Preise oder Preisspannen stehen, oder bleibt das ganz dem Angebot vorbehalten?
4. **Anhänge:** Welche Datenblätter hängen Sie genau an, etwa die Serie SG-40 allgemein, bestimmte Baugrößen oder Zubehör?
5. **Gesprächsinhalt:** Gab es auf der Messe technische Punkte, die ich aufgreifen sollte? Zum Beispiel Temperaturbereich, UV-Beständigkeit, Material, Montage, Kabeleinführungen oder Sonderbearbeitung.
6. **Technik:** Erfüllt die SG-40 IP66 serienmäßig, oder hängt das von der Ausführung ab? Das möchte ich in der Mail richtig darstellen.

Wenn Sie nicht alles beantworten möchten, kann ich auch mit Platzhaltern arbeiten.

#### Nutzer 2

Zu möglichen Rückfragen: Namen bitte als [ANSPRECHPARTNER] und [MEIN NAME], Terminvorschläge als [TERMIN 1] und [TERMIN 2]. Preise nennen wir in der Mail nicht. Bitte schreib jetzt den Entwurf.

#### Assistent 2

Hier ist der Entwurf (ca. 110 Wörter):

**Betreff:** Gehäuseserie SG-40 für den Außeneinsatz – Datenblätter und nächste Schritte

Guten Tag [ANSPRECHPARTNER],

vielen Dank für das gute Gespräch an unserem Stand auf den Industrietagen. Wie besprochen sende ich Ihnen im Anhang die Datenblätter zu unserer Gehäuseserie SG-40 für den Außeneinsatz, inklusive der Angaben zur Schutzart IP66.

Ein unverbindliches Angebot für Ihren Bedarf von etwa 300 Stück pro Jahr erhalten Sie bis Ende nächster Woche.

Um offene technische Fragen zu klären und Ihre Anforderungen genau abzustimmen, schlage ich ein kurzes Telefonat vor. Passt Ihnen [TERMIN 1] oder [TERMIN 2]? Falls beides nicht geht, nennen Sie mir gern einen anderen Zeitpunkt.

Mit freundlichen Grüßen

[MEIN NAME]

---
Hinweis: Bitte prüfen Sie vor dem Versand, ob die Datenblätter IP66 für die gewünschte Ausführung tatsächlich ausweisen. Ein Techniker achtet genau darauf.

#### Nutzer 3

Der Ton ist zu förmlich. Schreib lockerer, aber trotzdem professionell.

#### Assistent 3

Hier ist eine lockerere Fassung, weiterhin per Sie (ca. 100 Wörter):

**Betreff:** SG-40 für draußen – Datenblätter wie versprochen

Hallo [ANSPRECHPARTNER],

danke noch mal für das gute Gespräch bei uns am Stand auf den Industrietagen. Wie versprochen finden Sie im Anhang die Datenblätter zur SG-40. Die Angaben zu IP66 und zum Außeneinsatz stehen dort im Detail.

Das unverbindliche Angebot für rund 300 Stück im Jahr schicke ich Ihnen bis Ende nächster Woche.

Ich würde vorher gern kurz mit Ihnen telefonieren, damit das Angebot genau zu Ihrer Anwendung passt. Wie sieht es bei Ihnen am [TERMIN 1] oder [TERMIN 2] aus? Wenn beides nicht klappt, schlagen Sie gern einen anderen Termin vor.

Viele Grüße

[MEIN NAME]

#### Nutzer 4

Gib mir drei unterschiedliche Varianten, damit ich auswählen kann.

#### Assistent 4

Gerne. Hier sind drei Varianten mit unterschiedlichem Schwerpunkt, alle per Sie, locker und unter 150 Wörtern.

---

**Variante 1 – Kurz und direkt** (ca. 70 Wörter)

**Betreff:** Ihre Unterlagen zur SG-40

Hallo [ANSPRECHPARTNER],

danke für das gute Gespräch auf den Industrietagen. Im Anhang finden Sie wie besprochen die Datenblätter zur SG-40 (IP66, Außeneinsatz).

Das unverbindliche Angebot für ca. 300 Stück pro Jahr bekommen Sie bis Ende nächster Woche.

Haben Sie am [TERMIN 1] oder [TERMIN 2] Zeit für ein kurzes Telefonat?

Viele Grüße
[MEIN NAME]

---

**Variante 2 – Technischer Fokus** (ca. 115 Wörter)

**Betreff:** SG-40 / IP66 – Datenblätter und kurze Abstimmung

Hallo [ANSPRECHPARTNER],

vielen Dank für den Austausch an unserem Stand auf den Industrietagen. Im Anhang sind die Datenblätter zur SG-40 mit allen Angaben zu Schutzart IP66, Material und Abmessungen.

Bis Ende nächster Woche schicke ich Ihnen ein unverbindliches Angebot für rund 300 Stück pro Jahr. Damit es zu Ihrer Anwendung passt, würde ich vorher gern ein paar Details mit Ihnen klären, etwa Einbausituation, Kabeleinführungen und eventuelle Bearbeitungen.

Passt Ihnen ein kurzes Telefonat von etwa 15 Minuten am [TERMIN 1] oder [TERMIN 2]?

Viele Grüße
[MEIN NAME]

---

**Variante 3 – Persönlich, mit Bezug aufs Gespräch** (ca. 105 Wörter)

**Betreff:** Nach unserem Gespräch auf den Industrietagen

Hallo [ANSPRECHPARTNER],

ich hoffe, Sie sind gut von der Messe zurückgekommen. Ihr Projekt für den Außeneinsatz ist mir im Kopf geblieben, deshalb hier wie versprochen die Datenblätter zur SG-40 im Anhang.

Ihr unverbindliches Angebot für etwa 300 Stück im Jahr ist in Arbeit und kommt bis Ende nächster Woche.

Ich würde mich freuen, wenn wir vorher kurz telefonieren. So kann ich offene Fragen gleich mitnehmen. Wie wäre es am [TERMIN 1] oder [TERMIN 2]? Andere Zeiten sind natürlich auch möglich.

Viele Grüße
[MEIN NAME]

---

Meine Empfehlung für einen Techniker als Leser: **Variante 2**. Sie ist konkret und macht klar, wozu das Telefonat gut ist.

#### Nutzer 5

Was müsste ich dir noch sagen, damit das Ergebnis besser wird?

#### Assistent 5

Mit diesen Angaben würde die Mail konkreter und überzeugender:

1. **Inhalt des Messegesprächs:** Welche Anwendung hat der Kunde, und welche Punkte waren ihm wichtig, etwa Temperaturbereich, UV- und Witterungsbeständigkeit, Material, Montage oder Vibration? Ein konkreter Bezug zeigt ihm, dass Sie zugehört haben.
2. **Technische Details zur SG-40:** Welche Baugrößen oder Varianten kommen in Frage? Gilt IP66 serienmäßig oder nur in bestimmten Ausführungen? Gibt es Prüfzeugnisse oder Zertifikate, die Sie mitschicken können?
3. **Offene Fragen fürs Angebot:** Was müssen Sie noch wissen, um das Angebot zu kalkulieren, zum Beispiel Bearbeitung, Farbe, Zubehör, Abrufmengen oder Liefertermine? Daraus ergibt sich ein konkreter Grund für das Telefonat.
4. **Konkretes Datum:** Ein festes Datum statt „Ende nächster Woche“, etwa „bis Freitag, den …“, wirkt verbindlicher.
5. **Beziehung und Ton:** Wie war die Stimmung im Gespräch? Wie spricht man sich an, mit Namen und Titel? Haben Sie schon einmal zusammengearbeitet?
6. **Was Sie besonders auszeichnet:** Gibt es einen sachlichen Vorteil, den Sie erwähnen möchten, ohne werblich zu klingen? Zum Beispiel kurze Lieferzeiten, Sonderbearbeitung im eigenen Haus oder Muster zum Testen.
7. **Nächster Schritt:** Möchten Sie zusätzlich ein Muster anbieten oder einen Besuch vor Ort vorschlagen?
8. **Formales:** Signatur mit Funktion und Telefonnummer, Firmenname und eventuelle Vorgaben aus Ihrem Haus, etwa zur Grußformel.

Schon zwei oder drei dieser Punkte, vor allem 1 bis 3, machen die Mail spürbar individueller.

---

Zurück zu [Übung 4: Eigene Aufgabe](../06_Uebungen/Uebung_4_Eigene_Aufgabe.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md#übung-4-eigene-aufgabe)
