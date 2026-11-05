# Testlauf: Übung 1 / Trainer-Zusatz – Interne Mail an GF zur Nachlass-Entscheidung

**Herkunft:** Zusatzaufgabe für Schnelle aus [Trainer-Loesungshinweise.md – Übung 1, „Zusatzaufgaben für Schnelle“](../06_Uebungen/Trainer-Loesungshinweise.md#zusatzaufgaben-für-schnelle). Übungsblatt: [Uebung_1_Texte_schreiben.md](../06_Uebungen/Uebung_1_Texte_schreiben.md). Material: [kundenmail_beschwerde.txt](../07_Beispielmaterial/kundenmail_beschwerde.txt). Die Aufgabe setzt auf Aufgabe A auf (gleicher Chat, Kundenmail ist schon bekannt).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt (2. Nachricht im selben Chat nach dem Startprompt aus Aufgabe A):**

```
Schreib eine interne Mail an die Geschäftsführung mit der Bitte um Entscheidung zum Nachlass. Stelle Pro und Contra in je 3 Punkten dar.
```

**Was ein gutes Ergebnis enthalten muss:** sachliche interne Entscheidungsvorlage, klare Bitte um Entscheidung, **genau 3 Pro und 3 Contra**, Kundenforderung korrekt wiedergegeben (**mindestens 10 %** auf Auftrag 4711-NT), Frist des Kunden (Mittwoch). Typische Pro-Punkte: 8 Jahre Kundenbeziehung, Drohung mit Lieferantenwechsel, Stillstand der Montage beim Kunden, eigenes Versäumnis. Typische Contra-Punkte: Margenverlust, Präzedenzfall, Alternativen (Teillieferung). **Keine erfundenen Auftragswerte oder Euro-Beträge** – der Auftragswert steht nicht in der Kundenmail, die einzige Euro-Angabe sind die 85 € Fracht auf RE-2024-0815.

---

## Bewertung

Wortzahlen per `python3` gezählt (Anrede bis Signatur, ohne Betreff): Haiku 233, Sonnet 191, Opus deutlich länger (mehr als doppelt so lang wie Sonnet, mit Sachverhalt, Optionen und Zusatzinfo).

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Genau 3 Pro / 3 Contra | ja | ja (Contra 3 bündelt zwei Argumente) | ja |
| „mindestens 10 %“ korrekt | ja | ja | ja (fett) |
| Auftrag 4711-NT, 120 Stk. SG-40 | ja | ja | ja |
| Klare Bitte um Entscheidung | ja | ja (knapp) | ja, mit Optionen A/B/C |
| Frist Mittwoch + GF-Frist | ja, [DATUM] + Mittwoch | ja, „[DATUM, spätestens Mittwoch]“ | ja, im Betreff und am Ende |
| Pro: 8 Jahre / Abwanderung / Stillstand | alle drei | 8 Jahre, eigenes Versäumnis, Stillstand (Abwanderung nur im Sachverhalt) | Kundenbindung inkl. Wechseldrohung, eigenes Versäumnis, Stillstand |
| Contra: Marge / Präzedenz / Alternative | Marge, Präzedenz, unbelegter Schaden (keine Alternative) | Marge, Präzedenz, unbelegter Schaden + Alternativen | Marge, Präzedenz, Alternativen (Teillieferung, Express, kleinerer %-Satz) |
| Keine erfundenen Euro-Beträge | ja ([AUFTRAGSWERT], [BETRAG]) | ja ([AUFTRAGSWERT], [BETRAG]) | ja ([BETRAG], [AUFTRAGSWERT], [X] %) |
| Sachverhalt korrekt | **nein** – „Kunde nennt jetzt KW 21 als Stand“ | ja | ja (sehr vollständig: März, KW 21 = heute, zweimal vertröstet) |
| Eigenes Versäumnis (keine Info) erwähnt | nein | ja | ja |
| Frachtkosten-Thema sauber abgegrenzt | erwähnt | „separat prüfen“ | „zur Info, getrennt prüfen“ |
| Eigene Empfehlung | ja (Nachlass an Liefertermin koppeln – nicht verlangt, aber nützlich) | nein | Optionen statt Empfehlung |
| Länge / Lesbarkeit für GF | angemessen | kompakt, sehr gut | lang, aber gut gegliedert |
| Gesamturteil | brauchbar, ein Sachfehler | gut | sehr gut |

---

## Gefundene Fehler mit Beleg

1. **Haiku: KW 21 falsch gedeutet.** Haiku schreibt: „Zugesagt war KW 18, eingetroffen ist bislang nichts; der Kunde nennt jetzt **KW 21 als Stand**.“ In der Kundenmail ist KW 21 die aktuelle Woche, kein Liefertermin oder Stand: „Jetzt haben wir KW 21 und bei uns ist NICHTS angekommen.“ Die GF könnte das als neuen Termin oder Lieferstatus missverstehen. Typischer Lesefehler, gut für die Auswertung.
2. **Kein Modell hat Auftragswert oder Nachlassbetrag erfunden.** Alle drei verwenden Platzhalter ([AUFTRAGSWERT], [BETRAG]). Die einzige Euro-Angabe (85 € Fracht, RE-2024-0815) stimmt mit der Quelle überein. Die „mindestens 10 %“ sind überall korrekt wiedergegeben.
3. **Sonnet: Contra 3 bündelt zwei Argumente** („Unbelegter Schaden … denkbar wären auch Alternativen wie Teillieferung, Expressversand oder Fracht-Gutschrift“). Formal sind es 3 Punkte, inhaltlich 4. Kein Fehler, aber ein Beispiel dafür, wie Modelle Mengenvorgaben „dehnen“.
4. **Kleinere Zusätze ohne Quelle (zulässig als Vorschläge):** „Expressversand auf unsere Kosten“ (Sonnet, Opus), „Fracht-Gutschrift“ (Sonnet), Kopplung an Liefertermin (Haiku). Alles klar als Optionen formuliert, nicht als Tatsache. Opus weist zusätzlich darauf hin, dass Vertrag/AGB zum Lieferverzug zu prüfen sind – gute Vorsicht statt erfundener Rechtslage.
5. **Nebenbefund aus Antwort 1 (Aufgabe A), Sonnet:** „Verbindlich bestätigen wir Ihnen schriftlich bis Mittwoch: [NEUER LIEFERTERMIN]“ – die Zusage „bis Mittwoch“ macht das Modell selbst; und „(vereinbart war frei Haus)“ übernimmt die Behauptung des Kunden als Tatsache. Für die Zusatzaufgabe nicht relevant, aber für Aufgabe A ein Prüfpunkt.

---

## Lehren für die Auswertung

- **Die Aufgabe funktioniert.** Alle drei Modelle liefern eine brauchbare Entscheidungsvorlage mit genau 3/3 Punkten, korrekter Forderung und ohne erfundene Beträge. Der Folge-Prompt ist kurz, wirkt aber, weil der Kontext aus Aufgabe A im Chat steht.
- **Lehre 1 – Kontext im Chat nutzen:** Der kurze Prompt klappt nur im selben Chat. Wer einen neuen Chat öffnet, muss die Kundenmail wieder einfügen (Gegenstück zum Stolperstein „Chat-Verlauf“ bei der Rückübersetzung).
- **Lehre 2 – genau lesen:** Haikus „KW 21 als Stand“ zeigt, dass auch eine flüssige, plausible Zusammenfassung falsch sein kann. Frage ans Plenum: „Was ist KW 21 laut Kundenmail?“
- **Lehre 3 – was die KI nicht wissen kann:** Auftragswert, Marge, Ursache des Verzugs und Vertragslage fehlen. Gute Modelle setzen Platzhalter (Opus nennt das ausdrücklich im Tipp). Die eigentliche Abwägung bleibt Aufgabe des Menschen – die KI liefert nur die Struktur.
- **Lehre 4 – Format-Vorgaben prüfen:** „Je 3 Punkte“ wird eingehalten, aber Punkte werden manchmal gebündelt (Sonnet). Nachzählen und auf Inhalt prüfen.
- **Lehre 5 – Länge steuern:** Opus liefert eine sehr gute, aber lange Vorlage. Für eine GF-Mail lohnt der Nachsatz „höchstens 150 Wörter“ oder „auf eine Bildschirmseite“.
- **Datenschutz:** In der Praxis enthält so eine interne Mail echte Kundennamen und Preise – Hinweis auf die [Daten-Ampel](../03_Daten-Ampel.md).
- **Zeit:** ca. 5 Minuten inkl. Lesen – passt als Aufgabe für Schnelle.

---

## Gesprächsprotokolle

### Modell: Haiku

#### Nutzer 1

Ich arbeite im Vertrieb der Nordlicht Technik GmbH. Unten steht eine verärgerte Kundenmail wegen eines Lieferverzugs.

Schreibe mir einen Antwortentwurf, der:
- sich für die Verzögerung entschuldigt, ohne Schuld abzuwälzen,
- auf die konkreten Punkte des Kunden eingeht,
- einen nächsten Schritt anbietet (z. B. Rückruf oder neuer Liefertermin),
- höflich und sachlich ist und höchstens 150 Wörter hat.

Erfinde keine Fakten wie Liefertermine oder Rabatte. Wo mir Informationen fehlen, setze einen Platzhalter in eckigen Klammern, z. B. [NEUER LIEFERTERMIN].

Hier die Kundenmail: [Anhang: kundenmail_beschwerde.txt]

#### Assistent 1

**Betreff:** Auftrag 4711-NT / Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

vielen Dank für Ihre offenen Worte. Es tut uns aufrichtig leid, dass die 120 Steuergehäuse SG-40 nicht wie zugesagt in KW 18 eingetroffen sind und Sie bisher keine klare Auskunft erhalten haben. Wir verstehen, wie sehr Sie das in Ihrer Montage und gegenüber Ihrem Kunden belastet.

Zu Ihren Punkten:
- **Liefertermin:** Wir klären den aktuellen Stand und bestätigen Ihnen einen verbindlichen Termin schriftlich bis [DATUM]. Auch eine Teillieferung prüfen wir.
- **Frachtkosten (RE-2024-0815):** Wir prüfen die Vereinbarung und korrigieren die Berechnung, falls eine Frei-Haus-Lieferung vereinbart war.
- **Nachlass:** Ihren Wunsch nehmen wir ernst und klären ihn intern. Eine Rückmeldung dazu folgt bis [DATUM].

Damit Sie zeitnah eine Antwort erhalten, rufe ich Sie am [RÜCKRUFTERMIN] an.

Mit freundlichen Grüßen

[NAME]
Vertrieb, Nordlicht Technik GmbH

#### Nutzer 2

Schreib eine interne Mail an die Geschäftsführung mit der Bitte um Entscheidung zum Nachlass. Stelle Pro und Contra in je 3 Punkten dar.

#### Assistent 2

**Betreff:** Entscheidungsbedarf Nachlass – Auftrag 4711-NT (Brenner Gerätebau GmbH)

Sehr geehrte Geschäftsführung,

Brenner Gerätebau GmbH (Auftrag 4711-NT, 120 Steuergehäuse SG-40, Auftragswert [AUFTRAGSWERT]) hat eine verspätete Lieferung reklamiert. Zugesagt war KW 18, eingetroffen ist bislang nichts; der Kunde nennt jetzt KW 21 als Stand. Der Kunde fordert mindestens 10 % Nachlass auf den Auftrag, eine schriftliche verbindliche Terminzusage und ggf. eine Teillieferung von 60 Stück. Er setzt eine Rückmeldung bis Mittwoch. Zusätzlich bittet er um Prüfung der Frachtkosten von 85 € auf Rechnung RE-2024-0815.

Wir bitten um Ihre Entscheidung, ob und in welcher Höhe ein Nachlass angeboten werden soll.

**Pro Nachlass:**
1. Kundenbindung: Der Kunde arbeitet seit acht Jahren mit uns zusammen; ein Nachlass kann das Vertrauen wiederherstellen.
2. Abwendung eines Lieferantenwechsels: Der Kunde hat angekündigt, sich andernfalls nach einem anderen Lieferanten umzusehen.
3. Schadensbegrenzung: Der Kunde steht durch die Verzögerung selbst unter Druck und hat Stillstandskosten in seiner Montage; ein Entgegenkommen kann die Eskalation entschärfen.

**Contra Nachlass:**
1. Präzedenzwirkung: Ein Nachlass nach Verzug könnte künftige Forderungen anderer Kunden begründen.
2. Ergebnisbelastung: Bei 10 % entspricht das [BETRAG] € bei dem genannten Auftragswert.
3. Ungeklärter Schaden: Der Schaden des Kunden ist bisher weder beziffert noch belegt; ein pauschaler Nachlass ist daher nicht begründet.

**Vorschlag zur Entscheidung:** Ein Nachlass sollte an die Einhaltung eines verbindlichen neuen Liefertermins gekoppelt werden. Bitte teilen Sie uns Ihre Entscheidung bis [DATUM] mit, damit wir dem Kunden bis Mittwoch antworten können.

Mit freundlichen Grüßen

[NAME]
Vertrieb, Nordlicht Technik GmbH

---

### Modell: Sonnet

#### Nutzer 1

Ich arbeite im Vertrieb der Nordlicht Technik GmbH. Unten steht eine verärgerte Kundenmail wegen eines Lieferverzugs.

Schreibe mir einen Antwortentwurf, der:
- sich für die Verzögerung entschuldigt, ohne Schuld abzuwälzen,
- auf die konkreten Punkte des Kunden eingeht,
- einen nächsten Schritt anbietet (z. B. Rückruf oder neuer Liefertermin),
- höflich und sachlich ist und höchstens 150 Wörter hat.

Erfinde keine Fakten wie Liefertermine oder Rabatte. Wo mir Informationen fehlen, setze einen Platzhalter in eckigen Klammern, z. B. [NEUER LIEFERTERMIN].

Hier die Kundenmail:
[Inhalt von kundenmail_beschwerde.txt: Markus Brenner, Brenner Gerätebau GmbH, Auftrag 4711-NT, 120 Steuergehäuse SG-40, zugesagt KW 18, jetzt KW 21 nichts geliefert, keine Info, zweimal auf "nächste Woche" vertröstet; Montage steht teilweise still; fordert schriftlichen verbindlichen Liefertermin, alternativ Teillieferung 60 Stück; erwartet mindestens 10 % Nachlass; Rechnung RE-2024-0815 mit 85 Euro Fracht trotz vereinbarter Frei-Haus-Lieferung, bitte prüfen; Rückmeldung bis Mittwoch, sonst Lieferantenwechsel.]

#### Assistent 1

Betreff: Ihr Auftrag 4711-NT – Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

bitte entschuldigen Sie die Verzögerung bei Ihrem Auftrag 4711-NT. Die zugesagte Lieferung in KW 18 haben wir nicht eingehalten, und dass Sie keine aktive Information von uns erhalten und zweimal nur eine vage Auskunft bekommen haben, hätte nicht passieren dürfen. Das tut mir leid, gerade nach acht Jahren guter Zusammenarbeit.

Konkret:
- Liefertermin: Verbindlich bestätigen wir Ihnen schriftlich bis Mittwoch: [NEUER LIEFERTERMIN].
- Teillieferung: Die Möglichkeit, vorab 60 Stück zu liefern, prüfen wir: [TERMIN TEILLIEFERUNG / MACHBARKEIT].
- Frachtkosten: Wir prüfen die 85 € auf RE-2024-0815 (vereinbart war frei Haus) und korrigieren sie bei Bestätigung: [ERGEBNIS PRÜFUNG].
- Nachlass: Ihre Anfrage geben wir intern weiter; [ANTWORT ZUM NACHLASS].

Gern rufe ich Sie heute an: [RUFNUMMER / UHRZEIT].

Mit freundlichen Grüßen
[NAME]
Nordlicht Technik GmbH

#### Nutzer 2

Schreib eine interne Mail an die Geschäftsführung mit der Bitte um Entscheidung zum Nachlass. Stelle Pro und Contra in je 3 Punkten dar.

#### Assistent 2

Betreff: Entscheidungsbitte – Nachlass Auftrag 4711-NT (Brenner Gerätebau GmbH)

Liebe Geschäftsführung,

der Kunde Brenner Gerätebau GmbH fordert wegen des Lieferverzugs bei Auftrag 4711-NT (120 Steuergehäuse SG-40, zugesagt KW 18, bislang nicht geliefert) mindestens 10 % Nachlass auf den Auftrag. Er verlangt zudem einen schriftlichen, verbindlichen Liefertermin (alternativ Teillieferung von 60 Stück) und droht bis Mittwoch mit einem Lieferantenwechsel. Zudem beanstandet er 85 € Fracht auf RE-2024-0815 trotz vereinbarter Frei-Haus-Lieferung, die wir separat prüfen.

Bitte um Entscheidung, ob und in welcher Höhe wir einen Nachlass gewähren.

Pro Nachlass:
1. Kundenbindung: Seit acht Jahren Geschäftsbeziehung, bisher zufriedener Kunde; ein Signal der Wertschätzung kann ihn halten.
2. Eigenes Versäumnis: Wir haben den Termin nicht gehalten und nicht aktiv informiert; ein Entgegenkommen wirkt fair und deeskalierend.
3. Risikobegrenzung: Er nennt eigene Schäden (Stillstand in der Montage); ein Nachlass kann weitergehende Forderungen oder Eskalation vermeiden.

Contra Nachlass:
1. Margenbelastung: Ein Nachlass von 10 % auf den Auftragswert [AUFTRAGSWERT] mindert den Ertrag direkt ([BETRAG]).
2. Präzedenzfall: Weitere Kunden könnten bei künftigen Verzögerungen ähnliche Nachlässe erwarten.
3. Unbelegter Schaden: Die Höhe seines Schadens ist nicht nachgewiesen; denkbar wären auch Alternativen wie Teillieferung, Expressversand oder Fracht-Gutschrift statt Prozentnachlass.

Benötigt bis: [DATUM, spätestens Mittwoch]

Mit freundlichen Grüßen
[NAME], Vertrieb

---

### Modell: Opus

#### Nutzer 1

Ich arbeite im Vertrieb der Nordlicht Technik GmbH. Unten steht eine
verärgerte Kundenmail wegen eines Lieferverzugs.

Schreibe mir einen Antwortentwurf, der:
- sich für die Verzögerung entschuldigt, ohne Schuld abzuwälzen,
- auf die konkreten Punkte des Kunden eingeht,
- einen nächsten Schritt anbietet (z. B. Rückruf oder neuer Liefertermin),
- höflich und sachlich ist und höchstens 150 Wörter hat.

Erfinde keine Fakten wie Liefertermine oder Rabatte. Wo mir Informationen
fehlen, setze einen Platzhalter in eckigen Klammern, z. B. [NEUER LIEFERTERMIN].

Hier die Kundenmail:
[Anhang: kundenmail_beschwerde.txt – Mail von Markus Brenner, Leitung Einkauf, Brenner Gerätebau GmbH, Betreff „WIE LANGE NOCH??? Auftrag 4711-NT / Steuergehäuse“]

#### Assistent 1

Hier ist ein Entwurf mit etwa 130 Wörtern:

---

**Betreff:** AW: Auftrag 4711-NT / Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

wir entschuldigen uns für die Verzögerung Ihres Auftrags 4711-NT über 120 Steuergehäuse SG-40. Ebenso tut es uns leid, dass wir Sie nicht selbst informiert haben. Ihre Montage steht teilweise still und Sie geraten bei Ihrem Kunden in Verzug. Das bedauern wir sehr, gerade nach acht Jahren guter Zusammenarbeit.

**Liefertermin:** Die vollständige Lieferung sagen wir Ihnen verbindlich für den [VERBINDLICHER LIEFERTERMIN] zu. Eine Teillieferung von 60 Stück ist [MÖGLICH AM DATUM / NICHT MÖGLICH].

**Nachlass:** Ihren Wunsch nach 10 % Nachlass habe ich intern zur Entscheidung weitergegeben. Die Antwort erhalten Sie bis [DATUM].

**Rechnung RE-2024-0815:** Wir prüfen die berechneten Frachtkosten von 85 Euro, weil „frei Haus“ vereinbart war. Ergebnis oder Korrektur kommen bis [DATUM].

Gern rufe ich Sie am [DATUM, UHRZEIT] an und bespreche alles persönlich mit Ihnen.

Mit freundlichen Grüßen
[NAME]
Vertrieb, Nordlicht Technik GmbH
[TELEFON]

---

**Hinweis:** Herr Brenner erwartet bis **Mittwoch** eine Antwort. Schicken Sie die Mail möglichst vorher, auch wenn noch nicht alle Platzhalter geklärt sind.

#### Nutzer 2

Schreib eine interne Mail an die Geschäftsführung mit der Bitte um Entscheidung zum Nachlass. Stelle Pro und Contra in je 3 Punkten dar.

#### Assistent 2

Hier ist ein Entwurf für die interne Mail:

---

**An:** Geschäftsführung
**Betreff:** Bitte um Entscheidung bis [DATUM, vor Mittwoch]: Nachlassforderung Brenner Gerätebau, Auftrag 4711-NT

Guten Tag [NAME GESCHÄFTSFÜHRUNG],

ich bitte Sie um eine Entscheidung zur Nachlassforderung unseres Kunden Brenner Gerätebau GmbH (Herr Markus Brenner, Leitung Einkauf).

**Sachverhalt:**
- Auftrag 4711-NT: 120 Steuergehäuse SG-40, bestellt im März, zugesagt für KW 18. Heute ist KW 21 und es wurde noch nichts geliefert.
- Der Kunde wurde von uns nicht selbst informiert. Zwei Nachfragen seines Einkaufs haben wir mit „nächste Woche“ beantwortet.
- Beim Kunden steht die Montage teilweise still und er ist bei seinem eigenen Kunden in Verzug.
- Er fordert einen verbindlichen schriftlichen Liefertermin. Eine Teillieferung von 60 Stück würde er akzeptieren.
- Er fordert **mindestens 10 % Nachlass** auf diesen Auftrag. Das wären [BETRAG] € bei einem Auftragswert von [AUFTRAGSWERT] €.
- Er erwartet bis Mittwoch eine Rückmeldung und droht sonst mit einem Lieferantenwechsel.
- Die Zusammenarbeit besteht seit acht Jahren. Bisher war der Kunde nach eigener Aussage zufrieden.

**Pro Nachlass:**
1. **Kundenbindung:** Ein langjähriger, bisher zufriedener Kunde droht ausdrücklich mit dem Wechsel. Der Nachlass ist ein deutliches Zeichen, dass wir ihn ernst nehmen.
2. **Verantwortung liegt bei uns:** Wir haben den Termin verpasst und den Kunden nicht informiert. Ein Entgegenkommen ist deshalb nachvollziehbar und glaubwürdig.
3. **Schadensbegrenzung:** Der Kunde hat nach eigener Aussage täglich Kosten durch den Stillstand. Eine schnelle, freiwillige Geste kann weitergehende Forderungen oder eine Eskalation vermeiden. Ob es solche Ansprüche gibt, wäre rechtlich bzw. vertraglich zu prüfen.

**Contra Nachlass:**
1. **Margenverlust:** 10 % auf den Auftrag kosten uns [BETRAG] € und schmälern die Marge deutlich. Die genaue Höhe ist mit Controlling bzw. Kalkulation zu klären.
2. **Präzedenzfall:** Ein pauschaler Nachlass kann bei diesem und bei anderen Kunden die Erwartung wecken, dass jeder Verzug automatisch zu Preisnachlässen führt.
3. **Andere Wege sind möglich:** Wir könnten auch ohne pauschalen Nachlass entgegenkommen, zum Beispiel mit einer vorgezogenen Teillieferung von 60 Stück, Expressversand auf unsere Kosten oder einem kleineren Nachlass von [X] %. Ob der Vertrag oder unsere AGB für Lieferverzug etwas regeln, ist noch zu prüfen: [VERTRAGLICHE REGELUNG].

**Entscheidungsoptionen:**
- A) 10 % Nachlass wie gefordert
- B) geringerer Nachlass von [X] %
- C) kein Nachlass, stattdessen [ALTERNATIVES ENTGEGENKOMMEN]

**Zusätzlich zur Info:** Der Kunde hat Frachtkosten von 85 € auf Rechnung RE-2024-0815 beanstandet, weil „frei Haus“ vereinbart war. Das prüfen wir getrennt. Falls die Beanstandung berechtigt ist, sollten wir zügig korrigieren. Das wäre auch ein positives Signal.

Damit wir die Frist des Kunden einhalten, brauche ich Ihre Entscheidung bitte bis [DATUM/UHRZEIT]. Für Rückfragen stehe ich gern zur Verfügung.

Viele Grüße
[NAME]
Vertrieb
[TELEFON]

---

**Tipp:** Ergänzen Sie vor dem Versand den Auftragswert und, wenn bekannt, die Ursache des Verzugs. Beides hilft der Geschäftsführung bei der Entscheidung.
