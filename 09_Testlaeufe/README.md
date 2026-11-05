# Testläufe – Index der Protokolle

**Für den Trainer.** Hier liegen die Protokolle, in denen jede Übung, jede Zusatzaufgabe und jede Demo des Tutorials mit drei KI-Modellen durchgespielt und bewertet wurde. Die Zusammenfassung für die Praxis – was Teilnehmende typischerweise bekommen, typische Fehler, worauf du beim Herumgehen achtest – steht in **[Erwartete Ergebnisse](../06_Uebungen/Erwartete_Ergebnisse.md)**.

Zurück zur [Übersicht](../README.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md) · [Trainer-Leitfaden](../01_Trainer-Leitfaden.md)

---

## So wurde getestet

- **Testdatum:** Montag, 2. November 2026.
- **Modelle:** Claude Haiku (einfacheres, schnelleres Modell), Claude Sonnet (mittleres Modell) und Claude Opus (stärkstes Modell) – als Stellvertreter für [KI-TOOL], **ohne Internetzugang** und ohne Firmendaten.
- **Ablauf:** Jede Aufgabe in einem neuen, leeren Chat, Prompts wörtlich aus dem Material, Folgeprompts im selben Chat. Jedes Modell lief pro Aufgabe **einmal** – Schwankungen innerhalb eines Modells sind also nicht erfasst.
- **Prüfung:** Zahlen, Wortzahlen, Zeilen und Summen wurden mit Python nachgerechnet, Quellen per Websuche geprüft, Zitate gegen das Beispielmaterial abgeglichen.
- **Einschränkung:** Andere Tools, andere Versionen oder Tools mit Websuche bzw. Firmendaten-Anbindung können deutlich anders antworten. Ein eigener Test mit eurem [KI-TOOL] bleibt nötig.

**Spalte „Funktioniert“:** 🟢 ja = die Aufgabe liefert, was das Material erwartet · 🟡 teilweise = brauchbar, aber mit Abweichungen von der Erwartung (oft: der geplante Fehler tritt nicht auf, oder es kommen andere Fehler) · 🔴 nein = die Aufgabe zeigt nicht, was sie zeigen soll (bei beiden „nein“-Fällen ist der schwache Prompt zu gut).

Insgesamt **68 Protokolle**: 31 × ja, 35 × teilweise, 2 × nein.

---

## Block 1/2 – Demos aus demo_fehler_zeigen.md

| Protokoll | Aufgabe | Funktioniert | Kurz gesagt |
|---|---|---|---|
| [demo-1-quellen](demo-1-quellen.md) | Demo 1 – Erfundene Quellen | 🟡 teilweise | Keine erfundene Quelle; echte, aber unpassende Studien |
| [demo-2-aktuelles](demo-2-aktuelles.md) | Demo 2 – Aktuelle Nachrichten | 🟡 teilweise | Alle lehnen ehrlich ab, kein Fehler sichtbar |
| [demo-3a-firmenwissen-urlaub](demo-3a-firmenwissen-urlaub.md) | Demo 3 – Firmenwissen (Urlaub) | 🟡 teilweise | Ehrliche Absage plus gekennzeichneter allgemeiner Ablauf |
| [demo-3b-firmenwissen-gf](demo-3b-firmenwissen-gf.md) | Demo 3 Variante – Geschäftsführer Nordlicht | 🟡 teilweise | Ehrliche Absage, nichts erfunden |
| [demo-4a-rechnen](demo-4a-rechnen.md) | Demo 4A – Rechnen | 🟡 teilweise | Meist richtig; einmal Komma statt Tausenderpunkt |
| [demo-4b-zaehlen](demo-4b-zaehlen.md) | Demo 4B – Buchstaben zählen | 🟡 teilweise | Alle zählen richtig (9/10) |
| [demo-5-falsche-voraussetzung](demo-5-falsche-voraussetzung.md) | Demo 5 – Falsche Voraussetzung | 🟡 teilweise | Alle widersprechen sofort |
| [demo-6a-varianz-kreativ](demo-6a-varianz-kreativ.md) | Demo 6 – Varianz kreativ | 🟡 teilweise | Namen ähneln sich stark (Terra…) |
| [demo-6b-varianz-fakt](demo-6b-varianz-fakt.md) | Demo 6 Zusatz – DIN 476 | 🟡 teilweise | Immer 1922, keine Widersprüche |
| [demo-7a-kundenmail-wow](demo-7a-kundenmail-wow.md) | Demo 7 – Kundenmail (Wow) | 🟢 ja | Sicherer Wow-Moment; weiche Zusagen zum Gegenlesen |
| [demo-7b-vorgaben-englisch](demo-7b-vorgaben-englisch.md) | Demo 7 Variante B – Vorgaben + Englisch | 🟢 ja | Vorgaben übernommen, aber verstärkt |
| [demo-f6-wow-stichworte](demo-f6-wow-stichworte.md) | Folie 6 / Demo 7 C – Mail aus Stichworten | 🟡 teilweise | Wow klappt; „1 Woche“ wird oft „etwa eine Woche“ |

## Input-Demos (Block 4–6)

| Protokoll | Aufgabe | Funktioniert | Kurz gesagt |
|---|---|---|---|
| [demo-f14-schwach](demo-f14-schwach.md) | Folie 14 – Schwacher Prompt Lieferantenmail | 🟡 teilweise | Vorlage mit Platzhaltern + Rückfragen statt Erfindungen |
| [demo-f14-stark](demo-f14-stark.md) | Folie 14/15 – Starker Prompt + Nachsteuern | 🟢 ja | Zuverlässig; beim Kürzen fallen Details weg |
| [demo-protokoll-schwach](demo-protokoll-schwach.md) | Block 4 Alternative – „Schreib ein Protokoll.“ | 🔴 nein | Mit Notizen ist auch der schwache Prompt gut |
| [demo-protokoll-stark](demo-protokoll-stark.md) | Block 4 Alternative – Starker Protokoll-Prompt | 🟡 teilweise | Gut, aber jedes Modell eine Falle |
| [demo-f18-pruefbericht](demo-f18-pruefbericht.md) | Folie 18 – Prüfbericht live | 🟡 teilweise | Seitenfrage führt ins Leere; Schlitzbreite übersehen |
| [demo-f21-ideen](demo-f21-ideen.md) | Folie 21 – Ideen-Prompt | 🟡 teilweise | 10 gute Ideen; Datenschutz-Hinweis fehlt teils |

## Übung 1 – Texte schreiben

| Protokoll | Aufgabe | Funktioniert | Kurz gesagt |
|---|---|---|---|
| [ue1-a](ue1-a.md) | A – Antwort auf die Beschwerde | 🟡 teilweise | Nichts erfunden; feine Fehler (bedingte Zusagen) |
| [ue1-a-hilfe-anliegen](ue1-a-hilfe-anliegen.md) | A – Trainerhilfe „alle Anliegen prüfen“ | 🟡 teilweise | Pauschales Abhaken; neuer Entwurf fehlt oft |
| [ue1-b](ue1-b.md) | B – Ton ändern | 🟡 teilweise | Tonwechsel verschiebt Zusagen |
| [ue1-c](ue1-c.md) | C – Übersetzen | 🟢 ja | Treu, aber nur so vollständig wie die Vorlage |
| [ue1-c-rueck](ue1-c-rueck.md) | C – Rückübersetzung | 🟡 teilweise | Im Test ohne eingefügten Text: alle fragen nach |
| [ue1-d](ue1-d.md) | D – Eigene Mail verbessern | 🟡 teilweise | Platzhalter bleiben; Inhalt verschiebt sich |
| [ue1-e](ue1-e.md) | E – Betreffzeilen | 🟢 ja | Zusagen im Betreff |
| [ue1-f](ue1-f.md) | F – Perspektivwechsel | 🟡 teilweise | Kundensicht drängt zu neuen Zusagen |
| [ue1-g](ue1-g.md) | G – Interne Kurznachricht | 🟢 ja | 3 Sätze, aber sehr lang |
| [ue1-zusatz-gf-nachlass](ue1-zusatz-gf-nachlass.md) | Zusatz – GF-Mail Nachlass | 🟢 ja | Brauchbare Entscheidungsvorlage |
| [ue1-zusatz-keine-teillieferung](ue1-zusatz-keine-teillieferung.md) | Zusatz – Keine Teillieferung | 🟢 ja | Gut; schwächere Modelle streichen Anliegen |

## Übung 2 – Gute Prompts

| Protokoll | Aufgabe | Funktioniert | Kurz gesagt |
|---|---|---|---|
| [ue2-a](ue2-a.md) | A – Minimal-Prompt | 🟢 ja | Büroplan über 3 Monate statt Lager/erste Woche |
| [ue2-b](ue2-b.md) | B – Baukasten-Prompt | 🟢 ja | Passt; vermutete Details |
| [ue2-c](ue2-c.md) | C – „Stell mir zuerst 3 Fragen“ | 🟢 ja | Fragen kommen zuverlässig, als Sammelfragen |
| [ue2-d](ue2-d.md) | D – Nachschärfen | 🟢 ja | Klappt; Nebenänderungen beachten |
| [ue2-e](ue2-e.md) | E – Eigener Prompt | 🟢 ja | Format hält, Rückfragen nach Ampel prüfen |
| [ue2-e-muster-statusbericht](ue2-e-muster-statusbericht.md) | E – Trainer-Musterprompt Statusbericht | 🟢 ja | Liefert und fragt nach, statt zu warten |
| [ue2-f](ue2-f.md) | F – KI verbessert den Prompt | 🟢 ja | Gute Vorschläge, erfundene Ampel-Regeln |
| [ue2-g1-schwach](ue2-g1-schwach.md) | G – „Fass das zusammen“ | 🔴 nein | Minimal-Prompt findet schon alles |
| [ue2-g2-baukasten](ue2-g2-baukasten.md) | G – Baukasten-Prompt Notizen | 🟡 teilweise | 5-Satz-Grenze oft überschritten |

## Übung 3 – Dokumente und Tabellen

| Protokoll | Aufgabe | Funktioniert | Kurz gesagt |
|---|---|---|---|
| [ue3-fallback-einfuegen](ue3-fallback-einfuegen.md) | Upload-Ersatz: Einfügen + Kontrollfrage | 🟢 ja | Vollständig angekommen; Kontrollfrage mehrdeutig |
| [ue3-a-basis](ue3-a-basis.md) | A Basis – Prüfbericht in 5 Sätzen | 🟡 teilweise | Gut, aber „alle Maße in Toleranz“ übernommen |
| [ue3-a-weiter](ue3-a-weiter.md) | A Weiter – Risiken, Zitat, Widersprüche | 🟢 ja | Schlitzbreite wird auf Nachfrage gefunden |
| [ue3-a-pruef-trainer](ue3-a-pruef-trainer.md) | A Trainer-Prüfprompts | 🟢 ja | Nachrechnen findet den Fehler zuverlässig |
| [ue3-a-schnell-zielgruppen](ue3-a-schnell-zielgruppen.md) | A Schnelle – andere Zielgruppen | 🟡 teilweise | Erfundene Zusagen im Kundentext |
| [ue3-a-schnell-fragen-gf](ue3-a-schnell-fragen-gf.md) | A Schnelle – Drei Fragen der GF | 🟢 ja | Gute Fragen, eine falsche Annahme |
| [ue3-a-schnell-einbehalt](ue3-a-schnell-einbehalt.md) | A Schnelle – Einbehalt in Euro | 🟡 teilweise | Keine Halluzination – alle ehrlich |
| [ue3-ac-kombi](ue3-ac-kombi.md) | Zusatz – Station A + C kombiniert | 🟢 ja | Nichts erfunden, Schlitzbreite übersehen |
| [ue3-b-basis](ue3-b-basis.md) | B Basis – v1 vs. v2 | 🟡 teilweise | 7 von 7 gefunden; Trinkgeld-Deutung |
| [ue3-b-weiter](ue3-b-weiter.md) | B Weiter – Nachprüfen + Info-Mail | 🟡 teilweise | Nachprüfung bestätigt nur; Mail verkürzt |
| [ue3-b-pruef-trainer](ue3-b-pruef-trainer.md) | B Trainer-Prüfprompt | 🟡 teilweise | Bestätigt nur; Zählfehler im Begleittext |
| [ue3-b-schnell-faq](ue3-b-schnell-faq.md) | B Schnelle – FAQ | 🟢 ja | Korrekt; Trinkgeld-Frage fehlt |
| [ue3-b-schnell-unklar](ue3-b-schnell-unklar.md) | B Schnelle – Unklare Formulierungen | 🟡 teilweise | Lange Listen, teils konstruiert |
| [ue3-b-schnell-rechenfall](ue3-b-schnell-rechenfall.md) | B Schnelle – Rechenfall | 🟡 teilweise | Rechnung richtig; Verpflegung aus Fremdwissen |
| [ue3-c-basis](ue3-c-basis.md) | C Basis – Protokoll | 🟢 ja | Nachtrag teils als Widerspruch gewertet |
| [ue3-c-weiter](ue3-c-weiter.md) | C Weiter – Aufgabentabelle + Mail | 🟡 teilweise | Fehler beim Weiterverarbeiten zur Mail |
| [ue3-c-pruef-trainer](ue3-c-pruef-trainer.md) | C Trainer-Prüfprompts | 🟢 ja | Holen Widersprüche zuverlässig hervor |
| [ue3-c-schnell-checkliste](ue3-c-schnell-checkliste.md) | C Schnelle – Checkliste | 🟢 ja | 8/8; zugeschobene Zusatzpunkte |
| [ue3-c-schnell-rueckfragen](ue3-c-schnell-rueckfragen.md) | C Schnelle – Punkte ohne Verantwortliche | 🟢 ja | Gut; Person vs. Termin gemischt |
| [ue3-c-schnell-tagesordnung](ue3-c-schnell-tagesordnung.md) | C Schnelle – Tagesordnung | 🟢 ja | Alle Punkte; Zeitsummen falsch |
| [ue3-d-basis](ue3-d-basis.md) | D Basis – Liste analysieren | 🟡 teilweise | Richtig gezählt; falsche Spalte, stille Annahmen |
| [ue3-d-weiter](ue3-d-weiter.md) | D Weiter – Bereinigen + CSV | 🟡 teilweise | Daten fehlerfrei; Zeilennummern gemischt |
| [ue3-d-pruef-trainer](ue3-d-pruef-trainer.md) | D Trainer-Prüfprompts | 🟡 teilweise | Annahmenlisten unvollständig |
| [ue3-d-schnell-summe](ue3-d-schnell-summe.md) | D Kontrollwert – Summe | 🟡 teilweise | Alle richtig (461.001,25 €) |
| [ue3-d-schnell-spalten](ue3-d-schnell-spalten.md) | D Schnelle – Fehlende Spalten | 🟢 ja | Gute Checkliste, Datenschutz nur teils |
| [ue3-d-schnell-pflegeanleitung](ue3-d-schnell-pflegeanleitung.md) | D Schnelle – Pflegeanleitung | 🟢 ja | Gute Regeln, innere Widersprüche |
| [ue3-d-schnell-excel](ue3-d-schnell-excel.md) | D Schnelle – Excel-Anleitung | 🟡 teilweise | Versprochene 4 Duplikate stimmen in Excel nicht |

## Übung 4 – Eigene Aufgabe (Beispielrollen)

| Protokoll | Aufgabe | Funktioniert | Kurz gesagt |
|---|---|---|---|
| [ue4-einkauf](ue4-einkauf.md) | Einkauf – Mahnung Lieferverzug | 🟢 ja | Rückfragen wirken; Kürzung zu schwach |
| [ue4-vertrieb](ue4-vertrieb.md) | Vertrieb – Nachfass-Mail | 🟢 ja | Unterstellte Produkteigenschaften |
| [ue4-verwaltung](ue4-verwaltung.md) | Verwaltung – Antwortvorlage | 🟢 ja | Regellücke Fristbeginn wird teils geraten |

---

**Aufbau jedes Protokolls:** Herkunft (Link ins Material), Prompt, Bewertungstabelle je Modell, gefundene Fehler mit Belegen, Lehren für die Auswertung, Probleme im Material, Verbesserungsvorschlag und am Ende die vollständigen Gesprächsprotokolle.
