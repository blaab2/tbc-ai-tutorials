# Erwartete Ergebnisse: Was die KI bei den Übungen tatsächlich liefert

**Nur für dich als Trainer – nicht an die Teilnehmenden austeilen.**

Dieses Dokument ergänzt die [Trainer-Lösungshinweise](Trainer-Loesungshinweise.md). Dort steht, was eine *gute* Lösung enthält. Hier steht, was im Testlauf *tatsächlich* herauskam: Was bekommen die Teilnehmenden typischerweise? Welche Fehler macht die KI, und wie nutzt du sie in der Auswertung? Wo unterscheiden sich einfachere und stärkere Modelle? Und worauf achtest du beim Herumgehen?

Zurück zur [Übersicht](../README.md) · [Trainer-Leitfaden](../01_Trainer-Leitfaden.md) · [Alle Testlauf-Protokolle](../09_Testlaeufe/README.md) · [Demo-Prompts](../07_Beispielmaterial/demo_fehler_zeigen.md)

---

## So wurde getestet – und was das bedeutet

- **Alle Übungen, Zusatzaufgaben und Demos** wurden am 2. November 2026 durchgespielt, mit drei Modellen: einem **einfacheren, schnelleren Modell** (Claude Haiku), einem **mittleren Modell** (Claude Sonnet) und einem **stärkeren Modell** (Claude Opus).
- Die Modelle liefen **ohne Internetzugang** und ohne Anbindung an Firmendaten. Sie stehen stellvertretend für [KI-TOOL] – euer Werkzeug kann anders antworten.
- Jede Aufgabe lief in einem neuen Chat, die Prompts wörtlich aus dem Material. **Jedes Modell lief pro Aufgabe nur einmal.** Dieselbe Frage kann beim nächsten Mal anders ausgehen.
- Alle Zahlen, Wortzahlen, Zeilen und Summen wurden nachgerechnet, Quellen per Websuche geprüft, Zitate gegen das Beispielmaterial abgeglichen. Die Belege stehen in den einzelnen Protokollen.

> **Wichtig:** Die Ergebnisse unten sind eine Orientierung, kein Versprechen. **Teste die Übungen und vor allem die Demos vor dem Termin selbst mit [KI-TOOL]** und mach Screenshots als Backup. Tools mit Websuche, Gedächtnisfunktion oder Firmendaten-Anbindung verhalten sich teils deutlich anders.

---

## Die wichtigsten Erkenntnisse auf einen Blick

1. **Viele Fehler-Demos scheitern nicht mehr.** Erfundene Quellen, erfundene Nachrichten, erfundenes Firmenwissen, falsche Rechnungen, falsches Zählen, falsche Voraussetzung: Bei keinem der drei Modelle trat der geplante Fehler zuverlässig auf. Plane Block 1 so, dass auch „die KI macht es richtig“ eine gute Lehre ist – und halte Screenshots bereit.
2. **Die Fehler sind leiser geworden.** Statt erfundener Termine kommen *weiche Zusagen* („bis Mittwoch erhalten Sie den Termin“), *erfundene erledigte Schritte* („ich habe das mit der Fertigung geklärt“), *Aufweichungen* („1 Woche“ → „etwa eine Woche“) und *Verschärfungen* („soll“ → „muss“, „gebeten“ → „verlangt“). Diese Fehler findet nur, wer Satz für Satz gegen die Quelle liest.
3. **Folgeschritte sind gefährlicher als der erste Entwurf.** Beim Kürzen, Umformulieren, Übersetzen oder Weiterverarbeiten zur Mail gehen Fakten verloren oder kommen neue Zusagen dazu. Merksatz für die Gruppe: „Nach jeder Änderung die Checkliste noch einmal.“
4. **Fehler in der Quelle werden übernommen.** Alle Modelle glauben dem Fazit des Prüfberichts („alle Maße in Toleranz“), obwohl die Tabelle widerspricht. Erst die gezielte Nachfrage („Rechne jede Zeile nach“) findet den Fehler – das ist eine der stärksten Lehren des Tages.
5. **Selbstauskünfte der KI stimmen oft nicht.** Wortzahlen („ca. 145 Wörter“ bei tatsächlich 119), Satzzahlen, „alle Anliegen abgehakt“, „keine Zusage gemacht“: Was die KI über ihre eigene Antwort sagt, muss man nachzählen.
6. **Schwache Prompts sind mit gutem Material oft schon gut.** Bei den Notizen liefert auch „Fass das zusammen“ fast alles. Der Gewinn des Baukastens zeigt sich dann vor allem in Länge, Format und Vorhersagbarkeit – und dort, wo Kontext fehlt (Einarbeitungsplan: Büro statt Lager, drei Monate statt erste Woche).
7. **Stärkere Modelle liefern mehr – und mehr zum Prüfen.** Sie finden mehr Lücken und geben bessere Prüfhinweise, schreiben aber auch länger und schmücken mehr aus. Einfachere Modelle sind knapper, lassen aber eher Inhalte weg oder haken pauschal ab.

---

## Ampel-Übersicht aller Aufgaben

**Legende:** 🟢 ja = liefert, was das Material erwartet · 🟡 teilweise = brauchbar, aber anders als erwartet (oft: geplanter Fehler bleibt aus oder es kommen andere Fehler) · 🔴 nein = zeigt nicht, was es zeigen soll.

**Block 1/2 – Demos aus demo_fehler_zeigen.md**

| Aufgabe | Funktioniert | Kurz gesagt | Protokoll |
|---|---|---|---|
| Demo 1 – Erfundene Quellen | 🟡 teilweise | Keine erfundene Quelle; echte, aber unpassende Studien | [demo-1-quellen](../09_Testlaeufe/demo-1-quellen.md) |
| Demo 2 – Aktuelle Nachrichten | 🟡 teilweise | Alle lehnen ehrlich ab, kein Fehler sichtbar | [demo-2-aktuelles](../09_Testlaeufe/demo-2-aktuelles.md) |
| Demo 3 – Firmenwissen (Urlaub) | 🟡 teilweise | Ehrliche Absage plus gekennzeichneter allgemeiner Ablauf | [demo-3a-firmenwissen-urlaub](../09_Testlaeufe/demo-3a-firmenwissen-urlaub.md) |
| Demo 3 Variante – Geschäftsführer Nordlicht | 🟡 teilweise | Ehrliche Absage, nichts erfunden | [demo-3b-firmenwissen-gf](../09_Testlaeufe/demo-3b-firmenwissen-gf.md) |
| Demo 4A – Rechnen | 🟡 teilweise | Meist richtig; einmal Komma statt Tausenderpunkt | [demo-4a-rechnen](../09_Testlaeufe/demo-4a-rechnen.md) |
| Demo 4B – Buchstaben zählen | 🟡 teilweise | Alle zählen richtig (9/10) | [demo-4b-zaehlen](../09_Testlaeufe/demo-4b-zaehlen.md) |
| Demo 5 – Falsche Voraussetzung | 🟡 teilweise | Alle widersprechen sofort | [demo-5-falsche-voraussetzung](../09_Testlaeufe/demo-5-falsche-voraussetzung.md) |
| Demo 6 – Varianz kreativ | 🟡 teilweise | Namen ähneln sich stark (Terra…) | [demo-6a-varianz-kreativ](../09_Testlaeufe/demo-6a-varianz-kreativ.md) |
| Demo 6 Zusatz – DIN 476 | 🟡 teilweise | Immer 1922, keine Widersprüche | [demo-6b-varianz-fakt](../09_Testlaeufe/demo-6b-varianz-fakt.md) |
| Demo 7 – Kundenmail (Wow) | 🟢 ja | Sicherer Wow-Moment; weiche Zusagen zum Gegenlesen | [demo-7a-kundenmail-wow](../09_Testlaeufe/demo-7a-kundenmail-wow.md) |
| Demo 7 Variante B – Vorgaben + Englisch | 🟢 ja | Vorgaben übernommen, aber verstärkt | [demo-7b-vorgaben-englisch](../09_Testlaeufe/demo-7b-vorgaben-englisch.md) |
| Folie 6 / Demo 7 C – Mail aus Stichworten | 🟡 teilweise | Wow klappt; „1 Woche“ wird oft „etwa eine Woche“ | [demo-f6-wow-stichworte](../09_Testlaeufe/demo-f6-wow-stichworte.md) |

**Input-Demos (Block 4–6)**

| Aufgabe | Funktioniert | Kurz gesagt | Protokoll |
|---|---|---|---|
| Folie 14 – Schwacher Prompt Lieferantenmail | 🟡 teilweise | Vorlage mit Platzhaltern + Rückfragen statt Erfindungen | [demo-f14-schwach](../09_Testlaeufe/demo-f14-schwach.md) |
| Folie 14/15 – Starker Prompt + Nachsteuern | 🟢 ja | Zuverlässig; beim Kürzen fallen Details weg | [demo-f14-stark](../09_Testlaeufe/demo-f14-stark.md) |
| Block 4 Alternative – „Schreib ein Protokoll.“ | 🔴 nein | Mit Notizen ist auch der schwache Prompt gut | [demo-protokoll-schwach](../09_Testlaeufe/demo-protokoll-schwach.md) |
| Block 4 Alternative – Starker Protokoll-Prompt | 🟡 teilweise | Gut, aber jedes Modell eine Falle | [demo-protokoll-stark](../09_Testlaeufe/demo-protokoll-stark.md) |
| Folie 18 – Prüfbericht live | 🟡 teilweise | Seitenfrage führt ins Leere; Schlitzbreite übersehen | [demo-f18-pruefbericht](../09_Testlaeufe/demo-f18-pruefbericht.md) |
| Folie 21 – Ideen-Prompt | 🟡 teilweise | 10 gute Ideen; Datenschutz-Hinweis fehlt teils | [demo-f21-ideen](../09_Testlaeufe/demo-f21-ideen.md) |

**Übung 1 – Texte schreiben**

| Aufgabe | Funktioniert | Kurz gesagt | Protokoll |
|---|---|---|---|
| A – Antwort auf die Beschwerde | 🟡 teilweise | Nichts erfunden; feine Fehler (bedingte Zusagen) | [ue1-a](../09_Testlaeufe/ue1-a.md) |
| A – Trainerhilfe „alle Anliegen prüfen“ | 🟡 teilweise | Pauschales Abhaken; neuer Entwurf fehlt oft | [ue1-a-hilfe-anliegen](../09_Testlaeufe/ue1-a-hilfe-anliegen.md) |
| B – Ton ändern | 🟡 teilweise | Tonwechsel verschiebt Zusagen | [ue1-b](../09_Testlaeufe/ue1-b.md) |
| C – Übersetzen | 🟢 ja | Treu, aber nur so vollständig wie die Vorlage | [ue1-c](../09_Testlaeufe/ue1-c.md) |
| C – Rückübersetzung | 🟡 teilweise | Im Test ohne eingefügten Text: alle fragen nach | [ue1-c-rueck](../09_Testlaeufe/ue1-c-rueck.md) |
| D – Eigene Mail verbessern | 🟡 teilweise | Platzhalter bleiben; Inhalt verschiebt sich | [ue1-d](../09_Testlaeufe/ue1-d.md) |
| E – Betreffzeilen | 🟢 ja | Zusagen im Betreff | [ue1-e](../09_Testlaeufe/ue1-e.md) |
| F – Perspektivwechsel | 🟡 teilweise | Kundensicht drängt zu neuen Zusagen | [ue1-f](../09_Testlaeufe/ue1-f.md) |
| G – Interne Kurznachricht | 🟢 ja | 3 Sätze, aber sehr lang | [ue1-g](../09_Testlaeufe/ue1-g.md) |
| Zusatz – GF-Mail Nachlass | 🟢 ja | Brauchbare Entscheidungsvorlage | [ue1-zusatz-gf-nachlass](../09_Testlaeufe/ue1-zusatz-gf-nachlass.md) |
| Zusatz – Keine Teillieferung | 🟢 ja | Gut; schwächere Modelle streichen Anliegen | [ue1-zusatz-keine-teillieferung](../09_Testlaeufe/ue1-zusatz-keine-teillieferung.md) |

**Übung 2 – Gute Prompts**

| Aufgabe | Funktioniert | Kurz gesagt | Protokoll |
|---|---|---|---|
| A – Minimal-Prompt | 🟢 ja | Büroplan über 3 Monate statt Lager/erste Woche | [ue2-a](../09_Testlaeufe/ue2-a.md) |
| B – Baukasten-Prompt | 🟢 ja | Passt; vermutete Details | [ue2-b](../09_Testlaeufe/ue2-b.md) |
| C – „Stell mir zuerst 3 Fragen“ | 🟢 ja | Fragen kommen zuverlässig, als Sammelfragen | [ue2-c](../09_Testlaeufe/ue2-c.md) |
| D – Nachschärfen | 🟢 ja | Klappt; Nebenänderungen beachten | [ue2-d](../09_Testlaeufe/ue2-d.md) |
| E – Eigener Prompt | 🟢 ja | Format hält, Rückfragen nach Ampel prüfen | [ue2-e](../09_Testlaeufe/ue2-e.md) |
| E – Trainer-Musterprompt Statusbericht | 🟢 ja | Liefert und fragt nach, statt zu warten | [ue2-e-muster-statusbericht](../09_Testlaeufe/ue2-e-muster-statusbericht.md) |
| F – KI verbessert den Prompt | 🟢 ja | Gute Vorschläge, erfundene Ampel-Regeln | [ue2-f](../09_Testlaeufe/ue2-f.md) |
| G – „Fass das zusammen“ | 🔴 nein | Minimal-Prompt findet schon alles | [ue2-g1-schwach](../09_Testlaeufe/ue2-g1-schwach.md) |
| G – Baukasten-Prompt Notizen | 🟡 teilweise | 5-Satz-Grenze oft überschritten | [ue2-g2-baukasten](../09_Testlaeufe/ue2-g2-baukasten.md) |

**Übung 3 – Dokumente und Tabellen**

| Aufgabe | Funktioniert | Kurz gesagt | Protokoll |
|---|---|---|---|
| Upload-Ersatz: Einfügen + Kontrollfrage | 🟢 ja | Vollständig angekommen; Kontrollfrage mehrdeutig | [ue3-fallback-einfuegen](../09_Testlaeufe/ue3-fallback-einfuegen.md) |
| A Basis – Prüfbericht in 5 Sätzen | 🟡 teilweise | Gut, aber „alle Maße in Toleranz“ übernommen | [ue3-a-basis](../09_Testlaeufe/ue3-a-basis.md) |
| A Weiter – Risiken, Zitat, Widersprüche | 🟢 ja | Schlitzbreite wird auf Nachfrage gefunden | [ue3-a-weiter](../09_Testlaeufe/ue3-a-weiter.md) |
| A Trainer-Prüfprompts | 🟢 ja | Nachrechnen findet den Fehler zuverlässig | [ue3-a-pruef-trainer](../09_Testlaeufe/ue3-a-pruef-trainer.md) |
| A Schnelle – andere Zielgruppen | 🟡 teilweise | Erfundene Zusagen im Kundentext | [ue3-a-schnell-zielgruppen](../09_Testlaeufe/ue3-a-schnell-zielgruppen.md) |
| A Schnelle – Drei Fragen der GF | 🟢 ja | Gute Fragen, eine falsche Annahme | [ue3-a-schnell-fragen-gf](../09_Testlaeufe/ue3-a-schnell-fragen-gf.md) |
| A Schnelle – Einbehalt in Euro | 🟡 teilweise | Keine Halluzination – alle ehrlich | [ue3-a-schnell-einbehalt](../09_Testlaeufe/ue3-a-schnell-einbehalt.md) |
| Zusatz – Station A + C kombiniert | 🟢 ja | Nichts erfunden, Schlitzbreite übersehen | [ue3-ac-kombi](../09_Testlaeufe/ue3-ac-kombi.md) |
| B Basis – v1 vs. v2 | 🟡 teilweise | 7 von 7 gefunden; Trinkgeld-Deutung | [ue3-b-basis](../09_Testlaeufe/ue3-b-basis.md) |
| B Weiter – Nachprüfen + Info-Mail | 🟡 teilweise | Nachprüfung bestätigt nur; Mail verkürzt | [ue3-b-weiter](../09_Testlaeufe/ue3-b-weiter.md) |
| B Trainer-Prüfprompt | 🟡 teilweise | Bestätigt nur; Zählfehler im Begleittext | [ue3-b-pruef-trainer](../09_Testlaeufe/ue3-b-pruef-trainer.md) |
| B Schnelle – FAQ | 🟢 ja | Korrekt; Trinkgeld-Frage fehlt | [ue3-b-schnell-faq](../09_Testlaeufe/ue3-b-schnell-faq.md) |
| B Schnelle – Unklare Formulierungen | 🟡 teilweise | Lange Listen, teils konstruiert | [ue3-b-schnell-unklar](../09_Testlaeufe/ue3-b-schnell-unklar.md) |
| B Schnelle – Rechenfall | 🟡 teilweise | Rechnung richtig; Verpflegung aus Fremdwissen | [ue3-b-schnell-rechenfall](../09_Testlaeufe/ue3-b-schnell-rechenfall.md) |
| C Basis – Protokoll | 🟢 ja | Nachtrag teils als Widerspruch gewertet | [ue3-c-basis](../09_Testlaeufe/ue3-c-basis.md) |
| C Weiter – Aufgabentabelle + Mail | 🟡 teilweise | Fehler beim Weiterverarbeiten zur Mail | [ue3-c-weiter](../09_Testlaeufe/ue3-c-weiter.md) |
| C Trainer-Prüfprompts | 🟢 ja | Holen Widersprüche zuverlässig hervor | [ue3-c-pruef-trainer](../09_Testlaeufe/ue3-c-pruef-trainer.md) |
| C Schnelle – Checkliste | 🟢 ja | 8/8; zugeschobene Zusatzpunkte | [ue3-c-schnell-checkliste](../09_Testlaeufe/ue3-c-schnell-checkliste.md) |
| C Schnelle – Punkte ohne Verantwortliche | 🟢 ja | Gut; Person vs. Termin gemischt | [ue3-c-schnell-rueckfragen](../09_Testlaeufe/ue3-c-schnell-rueckfragen.md) |
| C Schnelle – Tagesordnung | 🟢 ja | Alle Punkte; Zeitsummen falsch | [ue3-c-schnell-tagesordnung](../09_Testlaeufe/ue3-c-schnell-tagesordnung.md) |
| D Basis – Liste analysieren | 🟡 teilweise | Richtig gezählt; falsche Spalte, stille Annahmen | [ue3-d-basis](../09_Testlaeufe/ue3-d-basis.md) |
| D Weiter – Bereinigen + CSV | 🟡 teilweise | Daten fehlerfrei; Zeilennummern gemischt | [ue3-d-weiter](../09_Testlaeufe/ue3-d-weiter.md) |
| D Trainer-Prüfprompts | 🟡 teilweise | Annahmenlisten unvollständig | [ue3-d-pruef-trainer](../09_Testlaeufe/ue3-d-pruef-trainer.md) |
| D Kontrollwert – Summe | 🟡 teilweise | Alle richtig (461.001,25 €) | [ue3-d-schnell-summe](../09_Testlaeufe/ue3-d-schnell-summe.md) |
| D Schnelle – Fehlende Spalten | 🟢 ja | Gute Checkliste, Datenschutz nur teils | [ue3-d-schnell-spalten](../09_Testlaeufe/ue3-d-schnell-spalten.md) |
| D Schnelle – Pflegeanleitung | 🟢 ja | Gute Regeln, innere Widersprüche | [ue3-d-schnell-pflegeanleitung](../09_Testlaeufe/ue3-d-schnell-pflegeanleitung.md) |
| D Schnelle – Excel-Anleitung | 🟡 teilweise | Versprochene 4 Duplikate stimmen in Excel nicht | [ue3-d-schnell-excel](../09_Testlaeufe/ue3-d-schnell-excel.md) |

**Übung 4 – Eigene Aufgabe (Beispielrollen)**

| Aufgabe | Funktioniert | Kurz gesagt | Protokoll |
|---|---|---|---|
| Einkauf – Mahnung Lieferverzug | 🟢 ja | Rückfragen wirken; Kürzung zu schwach | [ue4-einkauf](../09_Testlaeufe/ue4-einkauf.md) |
| Vertrieb – Nachfass-Mail | 🟢 ja | Unterstellte Produkteigenschaften | [ue4-vertrieb](../09_Testlaeufe/ue4-vertrieb.md) |
| Verwaltung – Antwortvorlage | 🟢 ja | Regellücke Fristbeginn wird teils geraten | [ue4-verwaltung](../09_Testlaeufe/ue4-verwaltung.md) |

---

## Einfachere und stärkere Modelle – was du erwarten kannst

Deine Teilnehmenden arbeiten je nach Lizenz mit unterschiedlich starken Modellen. Im Test zeigten sich über alle Aufgaben hinweg diese Muster:

| | Einfachere, schnellere Modelle | Stärkere Modelle |
|---|---|---|
| **Länge** | knapp, gut am Beamer lesbar | lang, oft mit Zusatzhinweisen; für 2–3-Minuten-Demos zu lang |
| **Vollständigkeit** | lassen eher etwas weg (z. B. 30 % Schlusszahlung, Teillieferung 60 Stück, Rechnung) | meist vollständig, finden auch versteckte Punkte (Schlitzbreite, Altanlage ohne Wartungsvertrag) |
| **Selbstprüfung** | haken gern pauschal alles ab | markieren eher ehrlich Lücken, geben Prüfhinweise vor dem Versand |
| **Typische Fehler** | Lesefehler (Komma/Punkt, falsche Spalte), Fachbegriffe („steering housing“), holprige Sätze | Ausschmückung, erfundene erledigte Schritte, Zuspitzungen, angedeutete Zusagen |
| **Formatvorgaben** | „genau 5 Sätze“ wird eher eingehalten | „5 Sätze“ wird zu 5 nummerierten Punkten mit 7–8 Sätzen |
| **Rückfragen** | wenige, eher zu Formatdetails | mehr und fachlich bessere (z. B. „Gilt IP66 serienmäßig?“) |

**Daraus folgt für die Auswertung:** „Mehr Text heißt nicht weniger Fehler.“ Ein guter Vergleich im Plenum: dieselbe Aufgabe von zwei Teams mit unterschiedlichen Ergebnissen nebeneinanderlegen.

---

## Worauf du beim Herumgehen immer achtest

- **Sätze ohne Klammer:** Wo behauptet der Entwurf etwas, das nicht in der Quelle steht (Ursache, erledigte Handlung, Anhang, Frist)?
- **Weiche Zusagen:** „bis Mittwoch“, „melden uns gleich“, „verbindlich“, „schriftliche Bestätigung“, „korrigieren wir, falls …“.
- **Nach jeder Änderung:** Ist etwas weggefallen oder dazugekommen? Besonders nach „kürzer“, „wärmer“, „lockerer“, Übersetzung.
- **Selbstangaben nachzählen:** Wortzahl, Satzzahl, Anzahl der gefundenen Änderungen.
- **Quelle schlägt Fazit:** Bei Zahlen und Tabellen nachrechnen lassen, nicht dem Text glauben.
- **Rückfragen nach Ampel beantworten:** Die KI fragt teils nach Auftragswerten, Namen oder Preisen – nicht einfach eintippen.
- **Zeit:** Lange Antworten nur überfliegen, gezielt drei Prüfpunkte suchen.

---

## Demos aus Block 1 und 2

Material: [demo_fehler_zeigen.md](../07_Beispielmaterial/demo_fehler_zeigen.md). Dort sind die Hinweise unten bereits eingearbeitet.

### Demo 1 – Erfundene Quellen 🟡

**Was kommt:** Keine erfundenen Quellen. Alle Modelle lehnen es ab, drei vollständige Angaben zu liefern, sagen offen, dass sie nichts prüfen können, und verweisen auf Datenbanken. Je nach Modell kommen 0 bis 3 echte, thematisch benachbarte Arbeiten, meist mit Artikelnummer statt Seitenzahl. 5 von 5 genannten Arbeiten existieren.

**So nutzt du es:** Eine Angabe live googeln, dann fragen: „Steht da drin, was wir wissen wollten?“ – meist nicht. Lehre: *Echte Quelle ist nicht gleich passende Quelle.* Beispiel: „My home is my castle“ (Alipour u. a. 2021) handelt von Kurzarbeit und Infektionsrisiko, nicht von Produktivität.

**Modellunterschiede:** Das einfachere Modell nennt gar keine passende Studie. Das stärkere Modell liefert drei korrekte Angaben, aber auch die meisten ungeprüften Zusatzbehauptungen zur Methode.

**Wenn du einen Fehler zeigen willst:** Variante mit Druck aus dem Demo-Blatt (vorher testen) oder Screenshot.

### Demo 2 – Aktuelle Nachrichten 🟡

**Was kommt:** Alle drei lehnen ab („kein Internetzugriff, Wissen hat einen Stichtag“), verweisen auf seriöse Quellen und bieten an, eingefügte Artikel zusammenzufassen. Keine erfundenen Nachrichten.

**So nutzt du es:** Positive Lehre „Gute Tools sagen, was sie nicht wissen“. Der eigentliche Lerneffekt liegt in der Variante mit Websuche: Links öffnen, Datum prüfen. **Achtung montags und nach Feiertagen:** „gestern“ war dann kein Werktag (der Testtag war ein Montag, der Vortag Sonntag/Allerheiligen). Kleiner Fund: Das einfachere Modell kündigt „fünf Punkte“ an und liefert vier – Brücke zu Demo 4.

### Demo 3 – Firmenwissen 🟡

**Was kommt:** Bei der Urlaubsfrage und bei der Frage nach dem Geschäftsführer der Nordlicht Technik GmbH: ehrliche Absage, dann ein allgemeiner Ablauf mit Kennzeichnung („in vielen Unternehmen“, „nur zur Orientierung“). Das stärkere Modell nennt echte Produktnamen (Personio, SAP SuccessFactors …) als Beispiele.

**So nutzt du es:** Die Kennzeichnung zeigen – wer sie überliest, hält die allgemeine Antwort für die Firmenregel. Frage: „Wisst ihr jetzt, welches System wir nutzen?“ Alle Modelle bieten von sich aus an, eine eingefügte Richtlinie zu verarbeiten – perfekte Überleitung zur Daten-Ampel („Darf ich unsere Urlaubsrichtlinie einfügen?“).

**Achtung:** Ist euer [KI-TOOL] mit Intranet oder SharePoint verbunden, kann die Antwort zu [FIRMENNAME] richtig sein. Für einen sichtbaren Fehler: Schreibaufgaben-Variante aus dem Demo-Blatt (Firmenporträt „ohne Platzhalter“, neuer Chat).

### Demo 4 – Rechnen und Zählen 🟡

**Was kommt:** Rechnen: mittleres und stärkeres Modell exakt 449.448.571. Das einfachere Modell antwortete **„449,448571“** – Ziffern richtig, aber um den Faktor eine Million daneben, weil es die Tausenderpunkte im Prompt als Dezimalpunkte las. Zählen: alle richtig (9 bzw. 10), alle zählen Wort für Wort.

**So nutzt du es:** „Diesmal stimmt es – aber woher wisst ihr das?“ Live mit dem Taschenrechner prüfen. Der Komma-Fall ist alltagsnah (CSV-Import, englische Tools). Beim Zählen: Strg+F in Word/Browser meldet 10, weil Groß-/Kleinschreibung ignoriert wird – auch Prüfwerkzeuge muss man verstehen.

### Demo 5 – Falsche Voraussetzung (Sommerzeit) 🟡

**Was kommt:** Alle drei widersprechen im ersten Satz, erklären die EU-Abstimmung von 2019 und dass der Rat nie zugestimmt hat. Keine erfundenen Industrie-Folgen.

**So nutzt du es:** Als positive Demo: „Sie hat es gemerkt – hättet ihr es gemerkt, wenn nicht?“ Betonen: Bei bekannten Fakten klappt das, bei Nischenthemen, Normen und Firmeninterna übernimmt die KI eine falsche Voraussetzung eher. Das stärkere Modell erklärt zusätzlich, woher der Irrtum kommt – gutes Vorbild einer Antwort.

### Demo 6 – Unterschiedliche Antworten 🟡

**Was kommt:** Kreativ: ein Name mit Begründung, oft nach demselben Muster („TerraGuard“, „TerraShield“), beim einfacheren Modell „Armora“ mit einer ungenauen Latein-Herleitung. Fakt (DIN 476): immer 1922, das stärkere Modell nennt ohne Einschränkung den 18. August 1922.

**So nutzt du es:** „Gleiche Antworten beweisen nichts.“ Auch kreative Antworten enthalten Sachbehauptungen (Latein-Herleitung). Kein Modell erwähnt Markenrecht – das bleibt beim Menschen. Für echte Vielfalt: Plan-B-Prompt mit 5 unterschiedlichen Namen.

### Demo 7 – Kundenmail (Wow) 🟢

**Was kommt:** Sicherer Wow-Moment: genau drei Stichpunkte (verbindlicher Termin für 4711-NT, mind. 10 % Nachlass, Prüfung der 85 € Fracht) und eine freundliche Antwort ohne Datum und ohne Rabatthöhe. Aber: **weiche Zusagen** sind fast immer drin.

> Beispiel-Auszug (mittleres Modell): „Den schriftlichen Termin erhalten Sie von uns bis Mittwoch.“ – Stärkeres Modell: „Ich habe Ihr Anliegen heute persönlich übernommen und kläre gerade mit unserer Fertigung …“

**So nutzt du es:** „Würdet ihr das abschicken?“ hat jetzt echte Antworten. Bonus: Die KI behauptet selbst, ihre Antwort verspreche nichts bzw. enthalte kein Schuldanerkenntnis („Sie haben völlig recht …“) – auch die Selbstbegründung gegenlesen.

**Variante B (Vorgaben + Englisch) 🟢:** „Freitag“ und „5 %“ werden übernommen – aber verstärkt („Bitte betrachten Sie diese Mail als schriftliche Bestätigung“, Sendungsnummer zugesagt). Das einfachere Modell übersetzt Steuergehäuse als **„steering housing“** (richtig: control housing). Keine Mail reagiert auf die 10-%-Forderung. Die Rechnung wurde entgegen der Erwartung nie vergessen.

**Variante C / Folie 6 (Stichworte) 🟡:** Tempo und Nachsteuern klappen sicher. Aber zwei von drei Modellen machen aus „1 Woche“ „etwa eine Woche“, eines erfindet einen Lieferanten als Ursache, und ob der Expressversand automatisch kommt oder auf Nachfrage, entscheidet jedes Modell anders. Frage an die Runde: „Wer entscheidet das – ihr oder die KI?“

### Vorschlag für Block 1 auf Basis der Tests

- **Wow:** Demo 7 (Grundvariante) – am zuverlässigsten, und das Gegenlesen liefert gleich eine Lehre.
- **Schiefgehen:** Demo 1 mit Live-Suche und der Frage „Passt die Quelle?“ – oder Screenshot aus deinem Vortest. Demo 3 nur mit Screenshot oder als Schreibaufgabe.
- **Block 2 (Gegenprüfen):** Demo 4 (Komma-Falle, Strg+F-Falle) oder Demo 5 als Positivbeispiel.

---

## Input-Demos in Block 4–6

### Folie 14 – Schwacher vs. starker Prompt (Lieferantenmail)

**Schwach 🟡:** Keine erfundene Mail, sondern eine Vorlage mit 9–15 Platzhaltern und 4–5 Rückfragen, 200–310 Wörter – fast doppelt so lang wie der starke Prompt erlaubt. Die Falle steckt in den Sätzen *ohne* Klammer: Das einfachere Modell unterstellt eine Verspätung („Bislang haben wir die Ware nicht erhalten“), das stärkere behauptet „Fotos und eine Kopie des Lieferscheins haben wir beigefügt“.

**Stark 🟢:** 90–102 Wörter, alle Fakten richtig (500 Dichtungsringe, zweite Verschiebung, Bedarf bis zum 15., Termin bis Freitag), Platzhalter für Name, Firma, teils Datum. Die drei Modelle liefern sehr ähnliche Mails – ein klarer Prompt verringert die Streuung.

**Nachsteuern (Folie 15):** „Kürzer und etwas wärmer“ kürzt um 16–26 %, dabei fällt meist „um eine Woche“ weg; einmal kam „Eine weitere Verschiebung können wir nicht auffangen“ dazu.

**So nutzt du es:** Beim schwachen Prompt zählen lassen: „Wie viele Lücken müsste ich noch füllen?“ Die Rückfragen der KI sind genau die fehlenden Bausteine – Brücke zum Joker. Beim starken Prompt: Platzhalter für Name/Datum sind normal und gut.

### Block 4 Alternative – Protokoll aus Notizen

**Schwach („Schreib ein Protokoll.“ mit Notizen) 🔴:** Alle drei liefern ein korrektes, vollständiges Protokoll – NACHTRAG KW 22 übernommen, Rabatt offen, Kaffeemaschine erledigt. Der erwartete Kontrast an den Fallen bleibt aus; der Unterschied liegt in Format und Länge. **Deshalb den schwachen Prompt ohne Notizen eingeben** (so steht er auf Folie 14) – dann kommt eine Vorlage, ein erfundenes Protokoll oder eine Rückfrage.

**Stark 🟡:** Deutlich besser im Format, aber jedes Modell hatte eine Schwäche: Kaffeemaschine als Tabellenzeile (mittleres Modell), erfundene Aufgabe „Rabatt-Anfrage: GF-Freigabe einholen | offen | offen“ (einfacheres Modell), Rabatt zusätzlich unter Beschlüssen. „Erfinde nichts“ schützt die Felder, nicht die Zeilen. Nachschärf-Satz steht in den Lösungshinweisen.

### Folie 18 – Prüfbericht live 🟡

**Was kommt:** Gute, zahlengenaue Zusammenfassungen (5 Stichpunkte, 3 Risiken, Vorbehalt mit 5 % Einbehalt). Auf „Auf welcher Seite?“ sagen alle ehrlich, dass es keine Seiten gibt – positiv, aber nicht die angekündigte Lehre. Zwei von drei Modellen schreiben „alle Maße in Toleranz“. Das stärkere Modell findet die Schlitzbreite ungefragt, schreibt aber „45 % schneller“ (richtig: 45 % kürzere Zeit ≈ 82 % schneller).

**So nutzt du es:** Eine Aussage tatsächlich im Original aufschlagen – am besten „alle Maße in Toleranz“ gegen Abschnitt 4, Zeile Schlitzbreite (0,13 mm bei ±0,10 mm).

### Folie 21 – Ideen-Prompt 🟡

**Was kommt:** Genau 10 passende Ideen (z. B. Anfrage DE/EN, Angebotsvergleich, Mahnung, Lieferantenbewertung). Das einfachere Modell gibt keinen Datenschutzhinweis; die anderen beiden fordern in der Liste dazu auf, Preise oder Bestellungen hineinzukopieren, und warnen erst am Schluss davor.

**So nutzt du es:** „Welche der 10 Ideen gehen mit grünen Daten?“ Nur die Überschriften lesen lassen (Zeit!). Der Prompt enthält jetzt den Zusatz „die ohne vertrauliche Daten funktionieren“.

---

## Übung 1: Texte schreiben

Übungsblatt: [Uebung_1_Texte_schreiben.md](Uebung_1_Texte_schreiben.md)

### Aufgabe A – Antwort auf die Beschwerde 🟡

**Was kommt:** Höflicher Entwurf in Sie-Form, 110–150 Wörter, 5–7 Platzhalter ([NEUER LIEFERTERMIN], [TEILLIEFERUNG], [FRIST], [NAME] …), alle fünf Anliegen angesprochen, Rückruf angeboten. **Kein Modell erfand einen Termin, Rabatt oder eine Gutschrift, keins vergaß die Rechnung** – die in den Lösungshinweisen erwartete „wichtigste Lernchance“ bleibt also meist aus. 4711-NT steht meist nur im Betreff, die acht Jahre Zusammenarbeit fehlen fast immer.

**Typische feinere Fehler:** bedingte Zusage („korrigieren sie, falls die frei-Haus-Vereinbarung zutrifft“), Übertreibung („Ihre Montage steht“ statt „teilweise still“), fehlende Fristen, Mittwoch-Frist nicht aufgegriffen, falsche Selbstangabe („ca. 145 Wörter“ bei 119).

**So nutzt du es:** Wenn Teilnehmende „nichts gefunden“ melden, gezielt auf diese feineren Fehler lenken. Wer den Klassiker sehen will: Prompt einmal ohne den Satz „Erfinde keine Fakten …“ laufen lassen.

**Trainerhilfe „alle Anliegen prüfen“ 🟡:** Einfachere Modelle haken pauschal alles ab – auch „verbindlich, nicht voraussichtlich“, obwohl im eigenen Entwurf „voraussichtlich [NEUER LIEFERTERMIN]“ steht. Kundensatz und KI-Satz nebeneinander zeigen: „Wenn alles abgehakt ist, misstrauisch werden.“ Der Ergänzungsprompt verlangt jetzt ehrliche Markierungen und den überarbeiteten Entwurf.

### Aufgabe B – Ton ändern 🟡

**Was kommt:** Drei klar unterschiedliche Varianten. Förmlich: gehobene Wortwahl, Anrede und Gruß bleiben meist gleich (der Entwurf war schon förmlich). Wärmer: Ich-Form, oft „Herzliche Grüße“, teils über 150 Wörter. Kurz: genau 5 Sätze, meist auf Basis der warmen Fassung.

**Typischer Fehler – Tonwechsel verschiebt Zusagen:**

> Beispiel-Auszug (stärkeres Modell, warme Fassung): „Ich habe mich direkt darum gekümmert: Die Lieferung kommt verbindlich am [NEUER LIEFERTERMIN].“

Dazu: bedingte Rechnungskorrektur bei allen Modellen, falsche Selbstaussagen („Beide Fassungen sind in 8 Sätze gegliedert“ – es waren 7 und 9), in der Kurzfassung fehlt teils die Anrede.

**So nutzt du es:** Nach jeder Variante die Checkliste aus A erneut anwenden. Diskussion: „Darf der Vertrieb die Rechnungskorrektur zusagen?“ und „Passt ‚Lieber Herr Brenner‘ bei einer Drohung mit Lieferantenwechsel?“

### Aufgabe C – Übersetzen und Rückübersetzen 🟢 / 🟡

**Was kommt:** Flüssiges britisches Englisch („Dear Mr Brenner“, „Yours sincerely“, „apologise“), Nummern und Platzhalter bleiben (werden aber mitübersetzt: [NEW DELIVERY DATE]). KW 18 wird bei allen zu „calendar week 18“. „Steuergehäuse“ wurde hier überall korrekt „control housings“.

**Typischer Fehler:** *Flüssig heißt nicht vollständig* – fehlen im deutschen Entwurf schon die 60 Stück oder die 85 €, fehlen sie auch im Englischen, und die Rückübersetzung zeigt das nicht.

**Rückübersetzung:** Im Test wurde der Platzhalter nicht gefüllt – alle Modelle fragten nach dem Text und erfanden nichts. Gutes Positivbeispiel, falls Teilnehmende den Prompt leer abschicken. Das stärkere Modell erklärt, dass es andere Chats nicht sieht. Bei Tools mit Gedächtnisfunktion besser einen temporären Chat nutzen. *(Der eigentliche Vergleich ist noch nicht getestet, siehe offene Empfehlungen.)*

### Aufgabe D – Eigene Mail verbessern 🟡

**Was kommt:** Deutlich kürzere Mail (49–66 statt 82 Wörter), Platzhalter bleiben zuverlässig, Grammatikfehler verschwinden. Stärkere Modelle stellen auf eine Liste um und ergänzen unverlangt einen Betreff.

**Typische Fehler:** Dringlichkeit gestrichen oder zugespitzt („Die Druckerei wartet schon“); Erklärung passt nicht zum Text (das stärkere Modell beschreibt eine Korrektur „wegen der Unterlagen“, das Wort „wegen“ kommt gar nicht mehr vor). „Lockerer“ kippt beim einfacheren Modell ins Vorwurfsvolle: „Wo bleiben die denn?“

**So nutzt du es:** „Verbessern heißt auch verändern.“ Beim Nachsteuern alte Vorgaben mitnennen: „lockerer, aber freundlich, ohne neue Inhalte“.

### Aufgabe E – Betreffzeilen 🟢

**Was kommt:** Drei sachliche Betreffs mit 5–8 Wörtern, fast immer mit 4711-NT, z. B. „Auftrag 4711-NT: Liefertermin und nächste Schritte“.

**Typischer Fehler:** Zusage im Betreff („Verbindlicher Liefertermin“, „Terminbestätigung“), obwohl im Text nur [NEUER LIEFERTERMIN] steht; „Rückmeldung bis Mittwoch“ wirkt wie die nächste Vertröstung. Das stärkere Modell zählt eine Wortzahl falsch.

**So nutzt du es:** „Würdest du ‚Verbindlicher Liefertermin‘ schreiben, solange der Termin ein Platzhalter ist?“ Funktioniert nur im selben Chat wie A.

### Aufgabe F – Perspektivwechsel 🟡

**Was kommt:** Fünf plausible Kritikpunkte aus Kundensicht, fast immer „wieder kein fester Termin“ und „Nachlass wird nur geprüft“. Die Überarbeitung bleibt unter 150 Wörtern.

**Typischer Fehler:** Kundenkritik drängt zu neuen Zusagen – trotz Verbot im Prompt. Beispiel (mittleres Modell): „Ich übernehme Ihren Fall persönlich.“, „verbindlich bis spätestens Mittwoch“, „(vereinbart war frei Haus)“ als Tatsache. Die KI kritisiert auch Platzhalter, die der Kunde nie sieht.

**So nutzt du es:** „Welche Kritik betrifft den Text, welche nur noch fehlende Infos?“ Das Übungsblatt hat jetzt einen Überarbeitungs-Prompt mit „keine neuen Zusagen“.

### Aufgabe G – Interne Kurznachricht 🟢

**Was kommt:** Genau 3 Sätze in Du-Form – aber mit 25–40 Wörtern pro Satz. Sachstand, Entwurfsinhalt und Auftrag an die Logistik sind korrekt.

**Typische Fehler:** Kundenfrist und interne Frist verwechselt („bis Mittwoch klären“ – zu spät); Frachtprüfung landet bei der Logistik; „falsch berechnete Fracht“ statt „bitte prüfen“; alle schreiben „wir haben geantwortet“, obwohl nur ein Entwurf existiert. Der Prompt verlangt jetzt „3 kurze Sätze (höchstens 60 Wörter)“.

### Zusatzaufgaben für Schnelle 🟢

- **GF-Mail zum Nachlass:** brauchbare Entscheidungsvorlage, Auftragswert als Platzhalter. Stolperstein beim einfacheren Modell: „der Kunde nennt jetzt KW 21 als Stand“ – KW 21 ist die aktuelle Woche, kein neuer Termin. Das stärkere Modell ist inhaltlich am besten, aber für eine GF-Mail zu lang.
- **Keine Teillieferung:** Absage mit Platzhalter für die Begründung, nichts erfunden. Das einfachere Modell streicht Nachlass und Rechnung ganz. Drei Absage-Formulierungen nebeneinanderzeigen: „derzeit nicht zusichern“ / „nicht darstellen“ / „nicht vorziehen, weil …“ – was wirkt ehrlich?

### Beim Herumgehen in Übung 1

- Ist jede Zusage durch die Kundenmail oder eine Vorgabe gedeckt? Besonders nach B und F.
- Stehen die 60 Stück, die 10 % und die 85 € noch drin – vor der Übersetzung?
- Wurde für die Rückübersetzung wirklich ein neuer Chat geöffnet und der Text eingefügt?

---

## Übung 2: Gute Prompts

Übungsblatt: [Uebung_2_Gute_Prompts.md](Uebung_2_Gute_Prompts.md)

### Aufgabe A – Minimal-Prompt 🟢

**Was kommt:** Ein allgemeiner Einarbeitungsplan fürs Büro über etwa **3 Monate bzw. 90 Tage**, oft mit Konzernzügen (Personal, IT, Facility). Kein Lager, keine Willkommensnachricht (höchstens als To-do). Stärkere Modelle stellen zusätzlich 5–7 Rückfragen. Namen werden nicht erfunden.

**So nutzt du es:** „Die KI rät“ lässt sich am besten an der Dauer zeigen: Niemand hat „3 Monate“ gesagt. Das einfachere Modell schreibt sogar ausdrücklich „im Büro“. Länge und professionelles Aussehen (stärkeres Modell) heißen nicht, dass der Plan passt.

### Aufgabe B – Baukasten-Prompt 🟢

**Was kommt:** Herzliche Du-Nachricht mit 56–68 Wörtern und Tabelle Mo–Fr mit genau 4 Spalten, Lagerbezug, durchgehend Platzhalter. In drei Läufen kein einziger erfundener Name.

**Typische Fehler:** Vermutete Details („Komm am Montag um 7:00 Uhr zum Haupteingang … Bring bitte Sicherheitsschuhe mit“, „holen wir dich am Empfang ab“). Das einfachere Modell übernimmt die Beispielzeile wörtlich. Die Tabelle des stärkeren Modells ist sehr voll – Brücke zu D („Kürzer bitte“).

### Aufgabe C – „Stell mir zuerst 3 Fragen“ 🟢

**Was kommt:** Kein Modell legte vorschnell los. Die drei Fragen sind Sammelfragen mit insgesamt 7–9 Teilfragen: Vorerfahrung/Systeme, Nachweise/Unterweisungen, Rahmen (Ansprechperson, Pate, Arbeitszeit). Danach ein Plan, der die Antworten aufgreift – bei stärkeren Modellen 2–3 Seiten.

**Modellunterschied:** Nur die stärkeren Modelle weisen darauf hin, dass ein Staplerschein ohne betriebliche Einweisung und schriftliche Beauftragung nicht reicht. Das einfachere Modell lässt den Kollegen am Donnerstag „ganztägig“ mitarbeiten, ohne Stapler-Einweisung. Frage: „Hättet ihr daran gedacht?“

### Aufgabe D – Nachschärfen 🟢

**Was kommt:** Jede Nachschärfung wird umgesetzt. „Kürzer“ wirkt je nach Ausgangslänge stark oder kaum (−27 % bis −62 %). „Was fehlt noch?“ liefert gute Punkte (Pate, PSA und Zugänge vor Tag 1, Pausen/Krankmeldung, Ziele für Woche 2).

**Typische Fehler:** Ersetzen statt ergänzen (Wochenrückblick verschwindet), Ansprechpersonen gehen beim Kürzen verloren, die lockere Nachricht erfindet Details („Arbeitsschuhe hast du“ – und widerspricht damit der eigenen Empfehlung zwei Antworten später). „3 Punkte“ werden zu 3 + „Bonus“. Das Übungsblatt hat jetzt einen „Beobachte“-Auftrag dazu.

### Aufgabe E – Eigener Prompt 🟢

**Was kommt:** Mit ausgefüllter Vorlage ein kurzer Bericht im gewünschten Format (78–88 Wörter), keine erfundenen Werte, dazu 2–4 Rückfragen. Platzhalter wie [VERTRIEBSLEITUNG] verschwinden. Beim Trainer-Musterprompt (Statusbericht) liefert die KI Bericht *und* Rückfragen, statt zu warten; die Ampelfarben fielen bei allen gleich aus.

**Typische Fehler:** Rückfragen nach Daten, die die Ampel ausschließt (Auftragswert, Name der Vertriebsleiterin); „per du“ geht leise verloren; „soll vor dem Audit fertig sein“ wird zu „muss“. Das einfachere Modell setzt einen zusätzlichen Einleitungsabsatz vor die „3 Abschnitte“.

### Aufgabe F – KI verbessert den Prompt 🟢

**Was kommt:** Genau 5 Vorschläge und eine 1,5- bis 2-mal so lange verbesserte Version. Alle drei bemängeln die mehrdeutige Format-Zeile „150 Wörter / 3 Abschnitte / Tabelle“ (inzwischen in der Vorlage korrigiert) und den Hinweis „DATEN-AMPEL BEACHTEN“, der für die KI wirkungslos ist.

**Typischer Fehler:** Die Modelle denken sich Ampel-Regeln und Beispiele aus, die der echten Ampel widersprechen („Angebot AG-2026-114 an Kunde Müller“, „Beträge gerundet = gelb“, Lücke für den Namen der Empfängerin). Also auch die Vorschläge der KI gegen die [Daten-Ampel](../03_Daten-Ampel.md) prüfen. Leitfrage „besser oder nur länger?“: „Nenne am Ende die Wortzahl“ ist nur scheinbar besser.

### Aufgabe G – Notizen: Minimal vs. Baukasten 🔴 / 🟡

**Was kommt:** Schon „Fass das zusammen“ liefert bei allen drei ein fast vollständiges Protokoll mit allen 8 Aufgaben und dem Nachtrag – aber länger als die Notizen selbst und jedes Mal anders formatiert. Der Baukasten-Prompt ist kürzer, vorhersagbar und setzt „offen“ sinnvoll.

**Typische Fehler:** 2 von 3 Modellen schreiben 7 statt höchstens 5 Sätze; Kaffeemaschine als Zeile „reparieren lassen – erledigt“ (erledigt war die *Meldung*); „Mitte Juni?“ fehlt in der Tabelle; beim Minimal-Prompt glättet das einfachere Modell den Q3-vs.-Juni-Widerspruch. Die Auswertungsfrage im Übungsblatt fragt jetzt nach Länge, Aufbau und „offen“-Markierungen statt nach „fehlenden Aufgaben“.

### Beim Herumgehen in Übung 2

- Laufen A und B in getrennten Chats?
- Was wurde *vermutet* (Dauer, Treffpunkt, Schuhe)? Das gehört in die Vergleichstabelle.
- Werden Rückfragen der KI mit grünen Daten beantwortet?
- Sätze und Wörter selbst zählen, nicht der KI-Angabe glauben.

---

## Übung 3: Dokumente und Tabellen

Übungsblatt: [Uebung_3_Dokumente_und_Tabellen.md](Uebung_3_Dokumente_und_Tabellen.md)

### Upload-Ersatz: Text einfügen 🟢

**Was kommt:** Kurze Bestätigung (24–64 Wörter, stärkere Modelle fassen ungefragt zusammen), dann auf „letzter Satz?“ korrekt die Unterschrift „Frank Albers, Fertigungstechnik“ und/oder den letzten echten Satz. Die Kontrollfrage ist mehrdeutig, weil das Dokument mit einer Unterschrift endet; sie lautet jetzt „Wie lauten die letzten zwei Zeilen, wörtlich?“. **Achtung:** „Ich habe es vollständig gelesen“ würden die Modelle auch bei abgeschnittenem Text sagen – den Fehlerfall zeigst du, indem du absichtlich nur die Hälfte einfügst.

### Station A – Prüfbericht zusammenfassen

**Basis 🟡:** Inhaltlich solide (Vorbehalt mit drei Bedingungen, 5 % Einbehalt, 96,2 %, 85.000 €/Jahr, Taktzeit C). **Kein Modell erfand einen Eurobetrag oder Update-Termin.** Aber alle übernahmen „Maßhaltigkeit bei allen Prüfteilen in der Toleranz“. Format: Das stärkere Modell machte aus „genau 5 Sätzen“ 5 nummerierte Absätze mit 8 Sätzen plus Aufzählung; das mittlere schrieb Sätze über 50 Wörter. Das einfachere Modell verdrehte die Bezugsgröße: „5 % von der Schlusszahlung (30 % des Kaufpreises)“ – wörtlich wären das 1,5 % statt 5 % des Kaufpreises.

**Weiter 🟢:** Risikotabelle mit 13–14 Zeilen, alle Pflichtpunkte, „keine Angabe“ statt erfundener Schweregrade, Zitate zeichengenau. **Auf „Gibt es Widersprüche?“ fanden alle drei die Schlitzbreite.** Aber: Das einfachere Modell erfand einen Widerspruch („Abschnitt 7 nennt die Leistungsaufnahme nicht“ – steht dort sehr wohl). Das stärkere Modell lieferte den besten Fund: Der Vorbehalt sichert nur 3 von 6 offenen Punkten ab.

**Trainer-Prüfprompts 🟢:** „Rechne jede Zeile einzeln nach“ findet den Fehler bei allen. Fundstellen stimmen meist, 2 von 3 Modellen nannten aber mindestens einmal einen falschen Abschnitt. Ein Modell „bestätigte“ beim Nachrechnen die 96,2 % aus dem Text – nachgerechnet sind es 96,15 %.

**Für Schnelle:**
- *Andere Zielgruppen 🟡:* Weglassen klappt (Preis, Namen, Zugangsdaten), aber Aussagen werden sicherer als im Original („Das Update kommt in den nächsten Wochen“, „erlaubter Wert“ statt interner Richtwert), und der Kundentext erfindet Zusagen: „Auf Ihre Aufträge und die Qualität Ihrer Teile haben diese Punkte keinen Einfluss.“ „Montageteam“ wurde unterschiedlich verstanden – auf dem Übungsblatt steht jetzt „Bediener und Instandhaltung in Halle 3“.
- *Drei Fragen der GF 🟢:* gute, kritische Fragen; stärkere Modelle liefern Fragenbündel (6–8 Fragezeichen). Eine kritisch klingende Frage beruhte auf einer falschen Annahme („Update 4.3 nicht im Vorbehalt“). Die Schlitzbreite fragte niemand an.
- *Einbehalt in Euro 🟡:* Alle drei ehrlich: 5 % des Kaufpreises, Betrag steht nicht drin. Das stärkere Modell rechnet ein gekennzeichnetes Beispiel vor („bei 400.000 € wären das 20.000 €“) – leises Risiko beim Kopieren. Die „perfekte Halluzinations-Demo“ blieb aus; Druck-Varianten stehen in den Lösungshinweisen.
- *Kombination A + C 🟢:* nichts erfunden, Kaufpreis und Fristen als fehlend benannt, Schlitzbreite übersehen, trotz „kurz“ ca. eine Seite.

### Station B – Richtlinie v1 vs. v2

**Basis 🟡:** Alle drei fanden **alle 7 Änderungen** – auch die angeblich schwer zu findenden (neue Inlandsflug-Regel, gestrichenes Trinkgeld). Die erwartete Frage „Wer hat alle gefunden?“ läuft deshalb ins Leere. Tatsächliche Stolpersteine: Das mittlere Modell schreibt „8 inhaltliche Änderungen“ und korrigiert am Ende selbst auf 7; das einfachere Modell deutet die gestrichene Regel als Verbot („Trinkgeld … ist selbst zu tragen“).

**Weiter 🟡:** Die Nachprüfung bestätigt nur – oder liefert einen Scheinbefund (einfacheres Modell: „fehlendes Inkrafttreten-Datum in v2“, obwohl Abschnitt 9 wortgleich ist). Die Info-Mail (122–131 Wörter) ist korrekt in den Zahlen, verliert aber Feinheiten: „zusätzlich“ bei der GF-Freigabe, „einfache“ Bahnfahrt, „Hotels kosten bis zu 130 Euro“ statt Erstattungsgrenze, Du/Ihr-Mischung.

**Trainer-Prüfprompt (Abschnitt für Abschnitt) 🟡:** dieselbe richtige Einstufung bei allen; Zählfehler in den Begleitsätzen. Die Kategorie „nur Formulierung geändert“ kommt im Material nicht vor – das stärkere Modell sagt das selbst.

**Für Schnelle:**
- *FAQ 🟢:* korrekte Zahlen; die naheliegende Frage „Gibt es noch Trinkgeld?“ fehlt bei 2 von 3, weil v2 dazu schweigt. Die eigentliche Lehre: Die Auswahl der Fragen ist das Problem, nicht ihre Richtigkeit.
- *Unklare Formulierungen 🟡:* immer 7–11 Punkte, teils konstruiert (3 h vs. 5 h), teils mit v1-Wissen (Trinkgeld, Abteilungsleitung), Zitate oft gebeugt und mit Strg+F nicht auffindbar. Drei Schubladen sortieren lassen: mehrdeutig / Lücke / konstruiert.
- *Rechenfall 🟡:* Rechnung bei allen richtig (218 € vs. 215 €), kein Modell rechnete mit 180 km. Bei der Verpflegung drei Stile: knapp ablehnen, ablehnen und nachfragen, oder **Steuerpauschalen aus allgemeinem Wissen** (14 €/28 €) liefern und in eine Gesamtsumme „ca. 246 €“ einrechnen. Frage: „Woher kommen die 14 €?“

### Station C – Notizen → Protokoll und Aufgabentabelle

**Basis 🟢:** Brauchbares Protokoll, alle 5 Personen, Datum [UNKLAR], Rabatt offen, Kaffeemaschine erledigt, alle 8 Aufgaben. Unterschied beim NACHTRAG: richtig übernommen (stärkeres Modell), verteilt (mittleres) oder als Widerspruch offengelassen („KW 23 oder KW 22 ([UNKLAR])“, einfacheres). „Je 1–3 Sätze“ wird überschritten, Fragen werden zu Aussagen („hat den keiner gelesen?“ → „offenbar hat ihn niemand gelesen“).

**Weiter 🟡:** Vollständige Tabelle mit 9–11 Zeilen (Zusatzzeilen für Rabatt-Entscheidung und Standpersonal sind *erwünscht*), Zitate wörtlich, keine errechneten Daten. Fehler entstehen beim Weiterverarbeiten zur Mail: Sabine fällt weg, „nächster Jour fixe (laut Notizen in 2 Wochen)“ ist geraten, Q3/Audit wird geglättet. Mail 250–410 Wörter.

**Trainer-Prüfprompts 🟢:** finden KW 22 und den Q3-Widerspruch zuverlässig. „Erledigt“ ist dehnbar – „Stand gebucht“ und „Bericht liegt vor“ sind als Antwort in Ordnung.

**Für Schnelle (alle 🟢):**
- *Checkliste:* 8/8 bei allen. Das einfachere Modell schiebt Zusatzpunkte Personen zu („Petra W. / GF: Rabattfrage klären“) und macht den Nachtrag zu „Widerspruch klären“.
- *Punkte ohne Verantwortliche:* Rabatt, Standpersonal, Protokollführung bei allen. Teils konstruiert („Teilnehmende offen“). Keiner fragt nach Petras Anwesenheit.
- *Tagesordnung:* alle offenen Punkte, kein Datum erfunden, Kaffeemaschine draußen. Zeitangaben nachrechnen („ca. 60 Minuten“ bei 65 Minuten Summe).

### Station D – Lieferantenliste bereinigen

**Basis 🟡:** Alle zählen richtig (27), alle finden die 4 Dubletten-Paare, keine falschen Treffer. Fehler sind subtil: falsche Spalte („n/a“ bei Richter als fehlendes Datum statt fehlender Umsatz), stille Gleichsetzung „März 2024 = 2024-03-01“, glattes Fazit „keine abweichenden Informationen“. Modelle nennen Dateizeilen (mit Kopfzeile), die Lösungshinweise Datenzeilen – beides ist richtig, die Tabelle in den Lösungshinweisen nennt jetzt beide.

**Weiter 🟢 in den Daten, 🟡 insgesamt:** Alle drei CSVs Zelle für Zelle geprüft: **0 Abweichungen**, Summe 461.001,25 €. Die angekündigten Stolpersteine (verschluckte Zeilen, 12.300 → 12,30) blieben aus. Tatsächlich: gemischte Zeilennummerierung innerhalb einer Antwort, still gekürzte Hinweise in der CSV, ein falscher Excel-Tipp.

**Trainer-Prüfprompts 🟡:** Nachzählen bestätigt; die Annahmenliste ist bei jedem Modell unvollständig (fehlend z. B. „n/a“, 15/01/2024, Rechtsform GmbH, 12.300), beim einfacheren Modell sogar falsch („habe ‚Kunststoffteile‘ gewählt“ – in der Tabelle stehen beide Werte).

**Für Schnelle:**
- *Summe 🟡:* alle richtig. Das einfachere Modell nennt nur die Endzahl – nicht nachprüfbar. Kontrollwerte: 461.001,25 € richtig, 575.751,75 € = Dubletten mitgezählt, 448.713,55 € = „12.300“ als 12,30 gelesen.
- *Fehlende Spalten 🟢:* gute Checkliste (Lieferantennummer, USt-IdNr., Status, Zertifikate …), 20+ Vorschläge. Nur das stärkere Modell erwähnt DSGVO bei Kontaktdaten; das mittlere empfiehlt die IBAN ohne Warnung – Anlass für die Daten-Ampel.
- *Pflegeanleitung 🟢:* sinnvolle Regeln, aber Widersprüche zwischen den Regeln (Pflichtfeld vs. „unbekannt bleibt leer“, Vorbelegung „B“ und 0), „Elektronik“ fällt beim Vereinheitlichen still weg. Frage: „Wer müsste das bei euch festlegen?“
- *Excel-Anleitung 🟡:* Menüpfade meist korrekt, aber die vorgeschlagene Spaltenwahl liefert **nicht** die versprochenen 4 Treffer: Nur über E-Mail werden auch Hoffmann und Krüger (beide leere E-Mail) als Duplikat gelöscht (22 statt 23); über E-Mail + Telefon wird Müller/Mueller wegen „0000-111201“ vs. „0000 111201“ nicht gefunden. Das einfachere Modell erfindet zudem einen Menüpfad („Format > Zelle > Zahl“). Lehre: „Auch eine kompetent klingende Anleitung muss man ausprobieren.“

### Beim Herumgehen in Übung 3

- Wird der Prüfschritt gemacht? „Welche drei Aussagen hast du im Original gefunden?“
- Station A: Hat jemand die Messwerttabelle nachgerechnet?
- Station B: Stimmt die genannte Anzahl mit den Tabellenzeilen? Ist eine Deutung als Tatsache formuliert?
- Station C: Steht KW 22 drin – als Korrektur, nicht als Widerspruch?
- Station D: Zählt der Editor die leere letzte Zeile mit (Strg + Ende → 29)? Dann 29 − 1 Leerzeile − 1 Kopfzeile = 27.

---

## Übung 4: Eigene Aufgabe

Übungsblatt: [Uebung_4_Eigene_Aufgabe.md](Uebung_4_Eigene_Aufgabe.md). Getestet wurden drei Beispielrollen mit dem Baukasten-Prompt und den Iterationsschritten des Übungsblatts.

**Was kommt (alle 🟢):** Mit „stell mir zuerst Rückfragen“ stellen alle Modelle zuerst 3–7 Fragen und warten. Danach ein versandfähiger Entwurf mit Platzhaltern, Fakten korrekt, keine erfundenen Nummern oder Namen. Varianten unterscheiden sich klar.

**Typische Fehler:**
- **Kürzen:** „maximal die Hälfte“ wird nur ungefähr eingehalten (50–60 %), dabei gehen Fakten verloren (z. B. „KW 19 → 21“, die Bestellnummer im Text).
- **Selbstangaben:** Wortzahlen der KI liegen oft daneben („ca. 85“ bei 76).
- **„Punkt 3 stimmt so nicht“** passt nicht auf eine Mail ohne Nummerierung – die Vorlage nennt jetzt zusätzlich „bzw. der Satz mit …“.
- **Vertrieb:** Produkteigenschaften werden als Tatsache dargestellt („die SG-40 ist für den Außeneinsatz mit Schutzart IP66 vorgesehen“), obwohl der Prompt nur sagt, dass der Kunde IP66 braucht. Varianten unterstellen Gesprächsinhalte („Ihr Projekt ist mir im Kopf geblieben“).
- **Verwaltung:** Eine Regellücke (ab wann läuft die Zahlungsfrist?) wird vom einfacheren Modell still geraten – eine riskante Zusage an Lieferanten. Die stärkeren Modelle machen die Lücke sichtbar.

**Modellunterschiede:** Stärkere Modelle stellen fachlich bessere Rückfragen (konkretes Datum statt „Freitag“, „Gilt IP66 serienmäßig?“, Skonto-Ausnahmen) und sagen offen, wenn eine Korrektur nicht passt („es gibt keinen Punkt 3“). Einfachere Modelle fragen eher nach Formatdetails und setzen Korrekturen stillschweigend um.

**Beim Herumgehen:**
- Daten-Ampel vor dem ersten Prompt.
- Nach jeder Iteration: Ist alles Wichtige noch drin? Wurde wirklich gekürzt?
- Jede Zusage (Frist, Produkteigenschaft, Zahlungstermin) gegen die echte Firmenregel bzw. das echte Gespräch prüfen.
- Gute Kandidaten für die Vorstellung in Block 7: Teams, bei denen die KI etwas Plausibles, aber Falsches ergänzt hat.

---

## Offene Empfehlungen

Diese Vorschläge aus den Testläufen sind **nicht** umgesetzt, weil sie größer oder strittig sind. Entscheide selbst, ob du sie übernimmst.

1. **Prüfbericht korrigieren?** In [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md), Abschnitt 3.3, steht „rund 96,2 %“, nachgerechnet sind es 96,15 % (also 96,1 %). Entweder im Bericht ändern (dann auch Lösungshinweise und Protokolle anpassen) oder als Bonus-Prüfpunkt stehen lassen (aktuell so gelöst). Ebenso offen: In Abschnitt 3.1 definieren, dass „Größte Abweichung“ die Abweichung vom Sollmaß meint.
2. **Ersatzmail für Übung 1 D:** Das Übungsblatt rät zu einer „erfundenen Beispielmail“, im Beispielmaterial gibt es aber keine. Vorschlag: neue Datei `07_Beispielmaterial/kollegenmail_unterlagen.txt` (Nachfrage nach Unterlagen für die Industrietage, mit [KOLLEGIN], [DATUM], [DURCHWAHL], [MEIN NAME]) anlegen und im Übungsblatt verlinken.
3. **Redaktionelle Änderung in Richtlinie v2:** Das Material enthält keine reine Umformulierung und keinen verschobenen Abschnitt, die Kategorie „nur Formulierung geändert“ lässt sich also nicht üben. Vorschlag: in v2, Abschnitt 6, einen Satz umstellen, ohne die Regel zu ändern – dann aber Lösungshinweise (Zählung „7 Änderungen“) und Protokolle anpassen.
4. **Demo-Prompts mit mehr Druck testen:** Die neuen Varianten im Demo-Blatt (Demo 1 „Bitte trotzdem drei, mit Seitenzahlen“, Demo 3 Firmenporträt „ohne Platzhalter“, Demo 4 schwere Multiplikation und Zählen „ohne Erklärung“, Demo 2 Leitzins-Frage) sind **ungetestet**. Vor dem Einsatz ausprobieren und Ergebnisse ergänzen.
5. **Wiederholungslauf Demo 6:** Der Kern der Demo (dieselbe Frage zweimal an *dasselbe* Modell) wurde nicht getestet – jedes Modell lief nur einmal.
6. **Rückübersetzung (Übung 1 C) wiederholen:** Im Testlauf war der Platzhalter nicht mit der englischen Fassung gefüllt; der eigentliche Vergleich ist noch ungetestet.
7. **Varianten mit Websuche bzw. Firmendaten-Anbindung** (Demo 2, Demo 3) testen, falls euer [KI-TOOL] das kann.
8. **Demo 7, Prompt präzisieren:** „kurze Antwort“ durch „kurze Antwort (max. 120 Wörter)“ ersetzen, wenn die 3 Minuten knapp werden; Variante B: Englisch-Schritt begründen („für unseren englischsprachigen Kollegen, der den Fall übernimmt“), weil der Kunde Deutsch schreibt.
9. **Übung 3, Prompts präzisieren** (optional, nicht getestet): Station A „Drei Fragen der GF“ mit „genau drei Fragen, je ein Satz, mit Abschnitt“; Station A Weiter „Nenne höchstens fünf Widersprüche, jeweils mit Abschnitt“; Station B „Unklare Formulierungen“ mit „höchstens 5 Stellen, wörtlich zitiert, ohne v1-Wissen“; Station C Mail „max. 200 Wörter mit Kurzprotokoll“; Station D Pflegeanleitung „höchstens eine Seite, Regeln auf Widersprüche prüfen“. Längere Listen kosten Prüfzeit, die in 27 Minuten fehlt.
10. **Übung 2 E, Platzhalter erhalten:** In der Vorlage optional „Lass Platzhalter in eckigen Klammern unverändert.“ ergänzen.
11. **Zeitplanung prüfen:** Übung 1 C+D (8 Min.) und Übung 3 (Basis + Weiter + Prüfschritt) sind mit ausführlichen Modellen knapp. Bei stärkeren Modellen ggf. „höchstens … Wörter“ in die Prompts aufnehmen.
12. **CSV öffnen:** Im Übungsblatt Station D einen Hinweis ergänzen, wie man die bereinigte CSV speichert und öffnet (UTF-8 mit BOM bzw. Daten → Aus Text/CSV), damit Umlaute stimmen.

---

Zurück zur [Übersicht](../README.md) · [Trainer-Lösungshinweise](Trainer-Loesungshinweise.md) · [Alle Testlauf-Protokolle](../09_Testlaeufe/README.md)
