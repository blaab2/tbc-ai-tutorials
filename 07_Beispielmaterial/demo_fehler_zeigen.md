# Demo: Typische KI-Schwächen live zeigen

**Für den Trainer** – Einsatz in Block 1 „Was ist KI eigentlich?“ (0:00–0:15), bei Bedarf auch in Block 2 „Spielregeln“ (0:15–0:30).
Zurück zum [Trainer-Leitfaden](../01_Trainer-Leitfaden.md) · Passende Folien: [Folien](../04_Folien.md) · Regeln zur Dateneingabe: [Daten-Ampel](../03_Daten-Ampel.md)

---

## Bevor du loslegst: Bitte unbedingt lesen

- **Die Ergebnisse variieren.** Ein Sprachmodell (also das Programm hinter dem KI-Assistenten, das den wahrscheinlich passenden nächsten Text vorhersagt) antwortet nicht jedes Mal gleich. Dieselbe Frage kann heute einen Fehler liefern und morgen eine richtige Antwort.
- **Moderne Modelle machen manche dieser Fehler deutlich seltener als noch vor ein, zwei Jahren.** Viele Assistenten können inzwischen im Internet suchen, rechnen mit Hilfswerkzeugen oder sagen offen „Das weiß ich nicht“. Das ist gut – macht die Demo aber weniger vorhersehbar.
- **Teste jeden Prompt (also jede Eingabe an die KI) vorher** mit genau dem [KI-TOOL] und der Lizenz, die ihr im Tutorial nutzt – am besten am Vortag und noch einmal kurz vor Beginn.
- **Mach Screenshots als Backup.** Wenn ein Fehler beim Testen auftritt, sichere ihn als Bild. Läuft die Demo live „zu gut“, zeigst du den Screenshot: „So sah das gestern aus.“
- **Auch „Die KI hat es richtig gemacht“ ist eine gute Lehre.** Die Botschaft lautet dann: „Diesmal stimmt es – aber woher wisst ihr das? Ihr müsst trotzdem prüfen.“ Genau darum geht es in Block 2.
- **Zwei bis drei Demos reichen.** Wähle vorher aus, du hast in Block 1 nur wenige Minuten. Die übrigen kannst du in Block 2 oder in der Abschlussrunde nutzen.
- Gib in den Demos **keine echten Firmendaten** ein – auch nicht „nur zum Zeigen“. Du bist Vorbild.

---

## Demo 1: Erfundene Quellen und Zitate

**Prompt:**
```
Nenne mir drei wissenschaftliche Studien aus Deutschland zur Produktivität von Homeoffice in mittelständischen Industriebetrieben. Bitte jeweils mit Autor, Jahr, Titel, Zeitschrift und Seitenzahl.
```

**Was du zeigen willst:** Die KI liefert möglicherweise sehr überzeugend klingende Quellen – mit Namen, Titeln und Seitenzahlen –, die es so nicht gibt oder bei denen Details nicht stimmen. Das nennt man **Halluzination**: Die KI erfindet Inhalte, die plausibel klingen, aber falsch sind.

**Warum das passieren kann:** Das Sprachmodell hat gelernt, wie Literaturangaben typischerweise aussehen. Es erzeugt eine wahrscheinlich klingende Angabe, ohne in einer Datenbank nachzuschlagen. Assistenten mit Websuche liefern oft Links – auch die sollte man anklicken.

**So prüfst du live:** Eine der Angaben in eine Suchmaschine kopieren. Findet sich nichts oder etwas anderes: Punkt gemacht. Findet sich die Studie: „Super – und genau so prüft ihr das in Zukunft auch.“

**Merksatz für die Gruppe:** „Quellen von der KI immer selbst öffnen und gegenlesen.“

---

## Demo 2: Sehr aktuelle Ereignisse

**Prompt:**
```
Was waren gestern die wichtigsten Nachrichten aus der deutschen Wirtschaft? Fasse sie in fünf Punkten zusammen.
```

**Was du zeigen willst:** Ohne Internetzugriff kennt die KI nur Wissen bis zu einem bestimmten Stichtag (dem Ende ihrer Trainingsdaten). Sie sagt das im besten Fall offen – im schlechteren Fall erzählt sie ältere Nachrichten, als wären sie von gestern.

**Warum das passieren kann:** Das Modell wurde mit Texten bis zu einem bestimmten Zeitpunkt trainiert. Was danach passiert ist, weiß es nicht, es sei denn, das Tool sucht aktiv im Internet.

**Variante:** Wenn dein [KI-TOOL] eine Websuche hat, zeige beide Fälle (mit und ohne Suche), falls sich das einstellen lässt. Sonst: Hinweis, dass auch Suchergebnisse falsch zusammengefasst werden können.

**Merksatz:** „Bei Aktuellem: Hat die KI wirklich nachgesehen? Quelle zeigen lassen.“

---

## Demo 3: Wissen über die eigene Firma

**Prompt:**
```
Wie funktioniert bei [FIRMENNAME] die Urlaubsbeantragung, und wer ist bei uns für die Freigabe zuständig?
```

**Variante mit der fiktiven Beispielfirma** (so steht sie auch im Trainer-Leitfaden, Block 1):
```
Wer ist der Geschäftsführer der Nordlicht Technik GmbH und welche Produkte hat sie?
```
Die Nordlicht Technik GmbH ist frei erfunden. Jede konkrete Antwort mit Namen oder Produkten ist also ausgedacht. Sagt die KI ehrlich „dazu habe ich keine Informationen“, ist das auch eine gute Lehre: Dann zeigst du, wie die Antwort bei der Frage nach [FIRMENNAME] aussieht. Achtung: Falls es zufällig eine echte Firma mit ähnlichem Namen gibt, kann die KI über diese berichten – deshalb vorher testen.

**Was du zeigen willst:** Die KI kennt eure Firma nicht. Sie kennt weder interne Abläufe noch Ansprechpersonen noch eure Richtlinien. Trotzdem kann sie eine allgemeine, „typische“ Antwort geben, die klingt, als wäre sie für euch zugeschnitten.

**Warum das passieren kann:** Das Modell füllt die Lücke mit dem, was in vielen Firmen üblich ist. Interne Informationen waren nie Teil seiner Trainingsdaten.

**Gute Überleitung:** „Wenn ihr wollt, dass die KI mit euren Abläufen arbeitet, müsst ihr ihr diese Informationen geben – und genau da kommt die Daten-Ampel ins Spiel.“ → Block 2.

**Merksatz:** „Die KI kennt [FIRMENNAME] nicht. Kontext musst du mitliefern.“

---

## Demo 4: Rechnen und Zählen

**Prompt A (Rechnen):**
```
Was ist 48.763 × 9.217? Antworte nur mit der Zahl, ohne Rechenweg.
```
(Richtige Lösung: **449.448.571** – vorher selbst mit dem Taschenrechner nachprüfen.)

**Prompt B (Zählen):**
```
Wie oft kommt der Buchstabe „e“ in diesem Satz vor: „Die Nordlicht Technik GmbH liefert Steuergehäuse an Kunden in ganz Europa.“
```
(Richtige Lösung: **9** kleine „e“ – bzw. **10**, wenn das große „E“ in „Europa“ mitzählt. Vorher selbst nachzählen.)

**Was du zeigen willst:** Lange Zahlen exakt multiplizieren oder Buchstaben zählen gehört nicht unbedingt zu den Stärken eines Sprachmodells – vor allem, wenn es „ohne Rechenweg“ antworten soll. Viele moderne Assistenten rechnen inzwischen mit einem eingebauten Werkzeug richtig. Dann zeigst du: „Mit Rechenweg ist es richtig – aber prüfen müsst ihr es bei wichtigen Zahlen trotzdem.“

**Warum das passieren kann:** Das Modell verarbeitet Text in Stücken (sogenannten Tokens), nicht Ziffer für Ziffer oder Buchstabe für Buchstabe. Es „schätzt“ das Ergebnis eher, als es auszurechnen.

**Merksatz:** „Für Zahlen, die zählen: Taschenrechner oder Tabellenkalkulation.“

---

## Demo 5: Frage mit falscher Voraussetzung

**Prompt:**
```
Warum hat Deutschland im Jahr 2019 die Sommerzeit abgeschafft, und welche Folgen hatte das für die Industrie?
```

**Was du zeigen willst:** Die Frage enthält eine falsche Annahme – die Sommerzeit wurde nicht abgeschafft. Ein gutes Modell widerspricht. Ein weniger gutes Modell (oder dasselbe an einem schlechten Tag) baut eine selbstbewusste Begründung um die falsche Voraussetzung herum.

**Warum das passieren kann:** Sprachmodelle sind darauf trainiert, hilfreich auf die gestellte Frage zu antworten. Die Voraussetzung der Frage wird manchmal einfach übernommen.

**Hinweis:** Prüfe vorher, wie dein Tool reagiert. Gut zu wissen: Das EU-Parlament hat 2019 zwar für ein Ende der Zeitumstellung gestimmt, umgesetzt wurde das aber nicht – die Sommerzeit gilt weiterhin (prüfe den aktuellen Stand kurz vor dem Termin). Erwähnt die KI diese Abstimmung, ist das korrekt und kein Fehler. Widerspricht es, ist das eine schöne positive Demo: „Seht ihr, sie hat es gemerkt – aber würdet ihr es merken, wenn sie es nicht gemerkt hätte?“

**Merksatz:** „Wie ich frage, beeinflusst, was ich bekomme. Suggestivfragen vermeiden.“

---

## Demo 6: Unterschiedliche Antworten auf dieselbe Frage

**Prompt (zweimal stellen – in zwei neuen Chats oder über „Antwort neu erzeugen“):**
```
Schlage mir einen Namen für eine neue Produktlinie von robusten Steuergehäusen für den Außeneinsatz vor. Nur einen Namen, mit einem Satz Begründung.
```

**Was du zeigen willst:** Dieselbe Frage liefert unterschiedliche Antworten. Bei kreativen Aufgaben ist das ein Vorteil (mehr Ideen!). Bei Fakten ist es ein Warnsignal: Wenn zwei Antworten sich widersprechen, kann höchstens eine stimmen.

**Zusatzvariante für Fakten:**
```
In welchem Jahr wurde die Norm DIN 476 (Papierformate) erstmals veröffentlicht?
```
Zweimal fragen, Antworten vergleichen – und vorher selbst nachschlagen, was stimmt (nach gängiger Darstellung 1922).

**Warum das passieren kann:** Das Modell wählt den nächsten Text mit einer gewissen Zufälligkeit aus. Deshalb sieht jede Antwort ein bisschen anders aus.

**Merksatz:** „Bei Ideen: mehrfach fragen. Bei Fakten: nicht der KI glauben, sondern prüfen.“

---

## Demo 7 (positiv): Etwas Beeindruckendes zeigen

Damit Block 1 nicht nur aus Fehlern besteht, beginne oder ende mit etwas, das gut funktioniert. Nutze dafür das fiktive Beispielmaterial:

**Prompt:**
```
Hier ist die Mail eines verärgerten Kunden. Fasse in drei Stichpunkten zusammen, was er konkret von uns will, und schlage eine freundliche, kurze Antwort vor, die nichts verspricht, was wir nicht halten können.

[Inhalt von kundenmail_beschwerde.txt einfügen]
```

**Was du zeigen willst:** In wenigen Sekunden werden aus einer emotionalen Mail drei klare Anliegen (Liefertermin, Rabattforderung, Rückfrage zur Rechnung) und ein brauchbarer Antwortentwurf. Das ist der „Wow-Moment“. Gleich danach: „Würdet ihr das so abschicken? Was müsstet ihr noch prüfen?“ (z. B. den echten Liefertermin, die Rabattfreigabe, die Rechnung).

Material: [kundenmail_beschwerde.txt](kundenmail_beschwerde.txt)

**Variante B (aus dem Trainer-Leitfaden, Block 1) – Antwort mit Vorgaben, dann übersetzen:**
```
Schreib eine freundliche, professionelle Antwort auf diese Beschwerde. Wir können bis Freitag liefern und bieten 5 % Rabatt auf die nächste Bestellung an.

[Inhalt von kundenmail_beschwerde.txt einfügen]
```
Danach im selben Chat: `Und jetzt das Ganze auf Englisch.` – zeigt, dass die KI den Chatverlauf kennt und Nachsteuern ganz einfach ist. (Die Zusagen „Freitag“ und „5 %“ sind für die Demo ausgedacht. Gut für den Hinweis: Die KI übernimmt, was du ihr vorgibst – ob es stimmt, musst du wissen.)

**Variante C (wie auf Folie 6) – Mail aus Stichworten:**
```
Mail an Kunden: Lieferung verschiebt sich um 1 Woche, Grund Materialengpass, wir bieten kostenlosen Expressversand an.
```
Danach: `Jetzt bitte etwas lockerer.` und `Und jetzt auf Englisch.`

Nimm die Variante, die bei deinem Test am besten funktioniert hat. Alle drei kommen ohne echte Daten aus.

---

## Vorschlag für Block 1 (15 Minuten)

| Zeit | Inhalt | Demo |
|---|---|---|
| 0:00–0:04 | Begrüßung, Ziel des Tages | – |
| 0:04–0:09 | Was ist ein Sprachmodell? | – |
| 0:09–0:12 | Etwas Beeindruckendes | Demo 7 |
| 0:12–0:15 | Etwas, das schiefgeht | Demo 1 **oder** Demo 3 |

In drei Minuten schaffst du realistisch nur eine Fehler-Demo. Demo 4, Demo 5 und Demo 6 eignen sich gut für Block 2 „Spielregeln“, wenn es um das Gegenprüfen geht.

---

## Checkliste für deine Vorbereitung

- [ ] Alle ausgewählten Prompts mit dem echten [KI-TOOL] getestet (Datum notieren)
- [ ] Screenshots der interessantesten Ergebnisse gespeichert (offline verfügbar, nicht nur in der Cloud)
- [ ] Richtige Lösungen notiert (Rechenaufgabe, Buchstabenanzahl, DIN-Jahr)
- [ ] Prompts zum Kopieren in einer Textdatei bereit, damit du live nicht tippen musst
- [ ] Neuer, leerer Chat für jede Demo (alte Chatverläufe beeinflussen die Antwort)
- [ ] Schriftgröße im Browser für den Beamer vergrößert
