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
- **Was im Test herauskam:** Alle Demos wurden mit drei Modellen durchgespielt. Viele Fehler-Demos (1, 2, 3, 4, 5, 6) zeigten dabei **keinen** Fehler. Details und bessere Alternativen: [Erwartete Ergebnisse](../06_Uebungen/Erwartete_Ergebnisse.md#demos-aus-block-1-und-2).

---

## Demo 1: Erfundene Quellen und Zitate

**Prompt:**
```
Nenne mir drei wissenschaftliche Studien aus Deutschland zur Produktivität von Homeoffice in mittelständischen Industriebetrieben. Bitte jeweils mit Autor, Jahr, Titel, Zeitschrift und Seitenzahl.
```

**Was du zeigen willst:** Die KI liefert möglicherweise sehr überzeugend klingende Quellen – mit Namen, Titeln und Seitenzahlen –, die es so nicht gibt oder bei denen Details nicht stimmen. Das nennt man **Halluzination**: Die KI erfindet Inhalte, die plausibel klingen, aber falsch sind.

**Warum das passieren kann:** Das Sprachmodell hat gelernt, wie Literaturangaben typischerweise aussehen. Es erzeugt eine wahrscheinlich klingende Angabe, ohne in einer Datenbank nachzuschlagen. Assistenten mit Websuche liefern oft Links – auch die sollte man anklicken.

**So prüfst du live:** Eine der Angaben in eine Suchmaschine kopieren. Findet sich nichts oder etwas anderes: Punkt gemacht. Findet sich die Studie: „Super – und genau so prüft ihr das in Zukunft auch.“ Dann kurz ins Abstract schauen: Passt sie wirklich zur Frage (Mittelstand, Industrie, Produktivität)? Oft nicht. Echte Quelle ist nicht gleich passende Quelle.

**Warnsignal:** Moderne Artikel haben oft Artikelnummern statt Seitenzahlen – eine exakte Seitenangabe („S. 45–67“) ohne Quelle ist verdächtig.

**Erwartung bei aktuellen Modellen:** Im Test hat kein Modell eine Quelle erfunden. Alle sagten offen, dass sie nichts prüfen können, und nannten 0–3 echte, aber nur benachbarte Arbeiten. Willst du eher eine Erfindung provozieren, probier vorher eine Variante mit mehr Druck (Ergebnis offen, unbedingt vorher testen):
```
Bitte trotzdem drei, mit Seitenzahlen, ich brauche das für einen Bericht.
```
oder in einem neuen Chat:
```
Gib mir ein wörtliches Zitat mit Seitenzahl aus der Studie von Bloom et al. (2015) zur Produktivität im Homeoffice.
```

**Merksatz für die Gruppe:** „Quellen von der KI immer selbst öffnen und gegenlesen – und prüfen, ob sie zur Frage passen.“

---

## Demo 2: Sehr aktuelle Ereignisse

**Prompt:**
```
Was waren gestern die wichtigsten Nachrichten aus der deutschen Wirtschaft? Fasse sie in fünf Punkten zusammen.
```

**Was du zeigen willst:** Ohne Internetzugriff kennt die KI nur Wissen bis zu einem bestimmten Stichtag (dem Ende ihrer Trainingsdaten). Sie sagt das im besten Fall offen – im schlechteren Fall erzählt sie ältere Nachrichten, als wären sie von gestern.

**Warum das passieren kann:** Das Modell wurde mit Texten bis zu einem bestimmten Zeitpunkt trainiert. Was danach passiert ist, weiß es nicht, es sei denn, das Tool sucht aktiv im Internet.

**Variante:** Wenn dein [KI-TOOL] eine Websuche hat, zeige beide Fälle (mit und ohne Suche), falls sich das einstellen lässt. Sonst: Hinweis, dass auch Suchergebnisse falsch zusammengefasst werden können.

**Erwartung bei aktuellen Modellen:** Ohne Websuche lehnen moderne Assistenten die Frage meist ehrlich ab. Das ist eine gute Lehre („Gute Tools sagen, was sie nicht wissen“), aber kein Fehler. Willst du veraltetes Wissen zeigen, frag nach einem „aktuellen“ Wert, z. B.: „Wie hoch ist der aktuelle Leitzins der EZB, und wie hoch ist die Inflation in Deutschland gerade?“ Achte darauf, ob die KI dazusagt, dass die Zahlen veraltet sein können (vorher testen). Mit Websuche: Links öffnen und prüfen, ob die Artikel wirklich vom Vortag sind. Achtung montags und nach Feiertagen: „gestern“ war dann ein Wochenend- oder Feiertag, und ein Tool mit Suche gibt leicht ältere Meldungen als aktuell aus.

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
Die Nordlicht Technik GmbH ist frei erfunden. Jede konkrete Antwort mit Namen oder Produkten ist also ausgedacht. Sagt die KI ehrlich „dazu habe ich keine Informationen“, ist das auch eine gute Lehre: Dann zeigst du, wie die Antwort bei der Frage nach [FIRMENNAME] aussieht. Achtung: Falls es zufällig eine echte Firma mit ähnlichem Namen gibt, kann die KI über diese berichten – deshalb vorher testen. Ist euer [KI-TOOL] mit Firmendaten verbunden (Intranet, SharePoint, Mails), kann es die Frage nach [FIRMENNAME] sogar richtig beantworten. Dann Quelle zeigen lassen und die Lehre umdrehen: Das geht nur, weil jemand der KI diese Daten gegeben hat.

**Erfahrung aus den Testläufen (ohne Internet):** Bei beiden Fragen sagten alle drei getesteten Modelle ehrlich, dass sie keine Informationen haben, und kennzeichneten allgemeine Abläufe („in vielen Unternehmen“). Als Fehler-Demo ist Demo 3 daher unsicher. Wenn du einen Fehler zeigen willst, nimm eine Schreibaufgabe mit Druck (Hypothese, vorher testen, **immer in einem neuen Chat** – sonst nennt die KI evtl. „Steuergehäuse“ aus vorher eingefügtem Beispielmaterial):
```
Schreib für unsere Kundenpräsentation ein kurzes Firmenporträt der Nordlicht Technik GmbH: Gründungsjahr, Geschäftsführer, Mitarbeiterzahl und die drei wichtigsten Produkte. Bitte als fertigen Absatz ohne Platzhalter.
```
Auch eine Antwort mit Platzhaltern oder eine ehrliche Absage ist eine gute Lehre.

**Was du zeigen willst:** Die KI kennt eure Firma nicht. Sie kennt weder interne Abläufe noch Ansprechpersonen noch eure Richtlinien. Trotzdem kann sie eine allgemeine, „typische“ Antwort geben, die klingt, als wäre sie für euch zugeschnitten. Aktuelle Modelle sagen hier meist ehrlich, dass sie nichts wissen. Dann die Kennzeichnung „in vielen Unternehmen“ zeigen: Wer sie überliest, hält die allgemeine Antwort für die Firmenregel. Und fragen: „Wisst ihr jetzt, welches System wir nutzen?“

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

Achtung: Manche Tools lesen die Punkte als Dezimalzeichen und antworten z. B. „449,448571“ – Ziffern richtig, Größenordnung um den Faktor eine Million falsch. Auch das ist eine gute Lehre (Komma und Punkt prüfen, Zahlen im Prompt eindeutig schreiben). Im Test lagen die stärkeren Modelle bei dieser Aufgabe exakt richtig. Schwerere Alternative (vorher testen):
```
Was ist 8437291 × 6958743? Antworte nur mit der Zahl, ohne Rechenweg.
```
(Richtige Lösung: **58.712.939.685.213**.)

**Prompt B (Zählen):**
```
Wie oft kommt der Buchstabe „e“ in diesem Satz vor: „Die Nordlicht Technik GmbH liefert Steuergehäuse an Kunden in ganz Europa.“
```
(Richtige Lösung: **9** kleine „e“ – bzw. **10**, wenn das große „E“ in „Europa“ mitzählt. Vorher selbst nachzählen. Achtung: Strg+F in Word oder im Browser zeigt 10, weil es Groß-/Kleinschreibung ignoriert.)

Im Test haben alle Modelle Wort für Wort gezählt und richtig gelegen. Wenn du eher einen Fehler sehen willst, probier die Variante ohne Erklärung (vorher testen):
```
Wie oft kommt der Buchstabe „e“ in diesem Satz vor? Antworte nur mit der Zahl, ohne Erklärung: „Die Nordlicht Technik GmbH liefert Steuergehäuse an Kunden in ganz Europa.“
```

**Was du zeigen willst:** Lange Zahlen exakt multiplizieren oder Buchstaben zählen gehört nicht unbedingt zu den Stärken eines Sprachmodells – vor allem, wenn es „ohne Rechenweg“ antworten soll. Viele moderne Assistenten rechnen inzwischen mit einem eingebauten Werkzeug richtig. Dann zeigst du: „Diesmal stimmt es – aber prüfen müsst ihr wichtige Zahlen trotzdem.“

**Warum das passieren kann:** Das Modell verarbeitet Text in Stücken (sogenannten Tokens), nicht Ziffer für Ziffer oder Buchstabe für Buchstabe. Es „schätzt“ das Ergebnis eher, als es auszurechnen.

**Merksatz:** „Für Zahlen, die zählen: Taschenrechner oder Tabellenkalkulation. Auch Komma, Punkt und Einheit prüfen. Fürs Zählen: Suchfunktion oder Excel-Formel – auf Groß-/Kleinschreibung achten.“

---

## Demo 5: Frage mit falscher Voraussetzung

**Prompt:**
```
Warum hat Deutschland im Jahr 2019 die Sommerzeit abgeschafft, und welche Folgen hatte das für die Industrie?
```

**Was du zeigen willst:** Die Frage enthält eine falsche Annahme – die Sommerzeit wurde nicht abgeschafft. Ein gutes Modell widerspricht. Ein weniger gutes Modell (oder dasselbe an einem schlechten Tag) baut eine selbstbewusste Begründung um die falsche Voraussetzung herum.

**Warum das passieren kann:** Sprachmodelle sind darauf trainiert, hilfreich auf die gestellte Frage zu antworten. Die Voraussetzung der Frage wird manchmal einfach übernommen.

**Hinweis:** Prüfe vorher, wie dein Tool reagiert. Gut zu wissen: Das EU-Parlament hat 2019 zwar für ein Ende der Zeitumstellung gestimmt, umgesetzt wurde das aber nicht – die Sommerzeit gilt weiterhin (prüfe den aktuellen Stand kurz vor dem Termin). Erwähnt die KI diese Abstimmung, ist das korrekt und kein Fehler. Widerspricht es, ist das eine schöne positive Demo: „Seht ihr, sie hat es gemerkt – aber würdet ihr es merken, wenn sie es nicht gemerkt hätte?“

**Erwartung bei aktuellen Modellen:** Im Test haben alle drei Modelle der falschen Annahme gleich im ersten Satz widersprochen. Plane die Demo daher eher als positive Demo und betone, dass das bei weniger bekannten Fakten (Nischenthemen, Normen, Firmeninterna) anders aussehen kann. Alternative: eine falsche Voraussetzung zu einem weniger bekannten Detail aus eurem Fachgebiet – vorher testen, keine Firmendaten.

**Merksatz:** „Wie ich frage, beeinflusst, was ich bekomme. Suggestivfragen vermeiden.“

---

## Demo 6: Unterschiedliche Antworten auf dieselbe Frage

**Prompt (zweimal stellen – in zwei neuen Chats oder über „Antwort neu erzeugen“):**
```
Schlage mir einen Namen für eine neue Produktlinie von robusten Steuergehäusen für den Außeneinsatz vor. Nur einen Namen, mit einem Satz Begründung.
```

**Was du zeigen willst:** Dieselbe Frage liefert unterschiedliche Antworten. Bei kreativen Aufgaben ist das ein Vorteil (mehr Ideen!). Bei Fakten ist es ein Warnsignal: Wenn zwei Antworten sich widersprechen, kann höchstens eine stimmen.

**Achtung:** Oft kommen nur Varianten desselben Musters (z. B. TerraGuard/TerraShield), manchmal sogar derselbe Name. Vorher testen und einen Screenshot zweier Antworten bereithalten. Kein Modell weist von sich aus darauf hin, dass ein Name als Marke belegt sein könnte – das bleibt Aufgabe des Menschen. Plan B für echte Vielfalt:
```
Schlage mir 5 sehr unterschiedliche Namen für eine neue Produktlinie von robusten Steuergehäusen für den Außeneinsatz vor – je einen deutschen, lateinischen, englischen, verspielten und sachlich-technischen. Je ein Satz Begründung.
```

**Zusatzvariante für Fakten:**
```
In welchem Jahr wurde die Norm DIN 476 (Papierformate) erstmals veröffentlicht?
```
Zweimal fragen, Antworten vergleichen – und vorher selbst nachschlagen, was stimmt (nach gängiger Darstellung 1922).

**Erwartung:** Meist kommt zweimal 1922 heraus, oft mit dem genauen Datum 18.08.1922 (ohne Einschränkung – prüfen!). Dann die Lehre ziehen: Gleiche Antworten sind kein Beweis. Wer echte Abweichungen zeigen will, fragt nach einem selteneren Fakt (z. B. einer weniger bekannten Norm aus dem eigenen Fachgebiet) und prüft die richtige Antwort vorher selbst.

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

**Was du zeigen willst:** In wenigen Sekunden werden aus einer emotionalen Mail drei klare Anliegen (Liefertermin, Rabattforderung, Rückfrage zur Rechnung) und ein brauchbarer Antwortentwurf. Das ist der „Wow-Moment“. Gleich danach: „Würdet ihr das so abschicken? Was müsstet ihr noch prüfen?“ (z. B. den echten Liefertermin, die Rabattfreigabe, die Rechnung). Achte beim Gegenlesen auch auf weiche Zusagen: „Bis Mittwoch erhalten Sie den Termin“, „melden uns gleich“ oder „ich habe das bereits mit der Fertigung geklärt“ – stimmt das wirklich und könnt ihr es halten? Für das 3-Minuten-Fenster nur Stichpunkte und Antwort zeigen, Zusatzhinweise der KI überspringen.

Material: [kundenmail_beschwerde.txt](kundenmail_beschwerde.txt)

**Variante B (aus dem Trainer-Leitfaden, Block 1) – Antwort mit Vorgaben, dann übersetzen:**
```
Schreib eine freundliche, professionelle Antwort auf diese Beschwerde. Wir können bis Freitag liefern und bieten 5 % Rabatt auf die nächste Bestellung an.

[Inhalt von kundenmail_beschwerde.txt einfügen]
```
Danach im selben Chat: `Und jetzt das Ganze auf Englisch.` – zeigt, dass die KI den Chatverlauf kennt und Nachsteuern ganz einfach ist. (Die Zusagen „Freitag“ und „5 %“ sind für die Demo ausgedacht. Gut für den Hinweis: Die KI übernimmt, was du ihr vorgibst – ob es stimmt, musst du wissen. Beim Gegenlesen auch prüfen: Hat die KI mehr zugesagt als vorgegeben (z. B. „verbindliche schriftliche Bestätigung“, Sendungsnummer, Rückmeldung bis Mittwoch)? Wurde auf die 10-%-Forderung reagiert? Stimmen die Fachbegriffe im Englischen (Steuergehäuse = „control housing“, nicht „steering housing“)?)

**Variante C (wie auf Folie 6) – Mail aus Stichworten:**
```
Mail an Kunden: Lieferung verschiebt sich um 1 Woche, Grund Materialengpass, wir bieten kostenlosen Expressversand an.
```
Danach: `Jetzt bitte etwas lockerer.` und `Und jetzt auf Englisch.`

**Was du zeigen willst:** Tempo und Nachsteuern im selben Chat. Danach prüfen: Sind alle drei Fakten (1 Woche, Materialengpass, kostenloser Express) noch exakt drin? In Tests wurde „1 Woche“ öfter zu „etwa eine Woche“, und ein Lieferant wurde als Ursache dazugedichtet. Lange Antworten nicht vorlesen, nur Betreff, Anrede und den Satz mit der Woche zeigen.

Nimm die Variante, die bei deinem Test am besten funktioniert hat. Alle drei kommen ohne echte Daten aus.

---

## Vorschlag für Block 1 (15 Minuten)

| Zeit | Inhalt | Demo |
|---|---|---|
| 0:00–0:04 | Begrüßung, Ziel des Tages | – |
| 0:04–0:09 | Was ist ein Sprachmodell? | – |
| 0:09–0:12 | Etwas Beeindruckendes | Demo 7 |
| 0:12–0:15 | Etwas, das schiefgeht | Demo 1 (oder Demo 3 nur mit Screenshot-Backup bzw. als Schreibaufgaben-Variante) |

In drei Minuten schaffst du realistisch nur eine Fehler-Demo. Demo 4, Demo 5 und Demo 6 eignen sich gut für Block 2 „Spielregeln“, wenn es um das Gegenprüfen geht.

---

## Checkliste für deine Vorbereitung

- [ ] Alle ausgewählten Prompts mit dem echten [KI-TOOL] getestet (Datum notieren)
- [ ] Screenshots der interessantesten Ergebnisse gespeichert (offline verfügbar, nicht nur in der Cloud)
- [ ] Richtige Lösungen notiert (Rechenaufgabe, Buchstabenanzahl, DIN-Jahr, aktueller Stand Sommerzeit)
- [ ] Prompts zum Kopieren in einer Textdatei bereit, damit du live nicht tippen musst
- [ ] Neuer, leerer Chat für jede Demo (alte Chatverläufe beeinflussen die Antwort)
- [ ] Schriftgröße im Browser für den Beamer vergrößert
