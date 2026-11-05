# Testlauf: Übung 1 / Weiter C – Antwort ins britische Englisch übersetzen

**Herkunft:** [Übung 1, Aufgabe C – Ins Englische übersetzen und zurück prüfen](../06_Uebungen/Uebung_1_Texte_schreiben.md#aufgabe-c--ins-englische-übersetzen-und-zurück-prüfen), erster Prompt (Übersetzung). Vorlauf im selben Chat: Aufgabe A (Antwortentwurf) und Aufgabe B, Variante „förmlicher“. Material: [kundenmail_beschwerde.txt](../07_Beispielmaterial/kundenmail_beschwerde.txt). Lösungshinweise: [Trainer-Loesungshinweise.md – Übung 1](../06_Uebungen/Trainer-Loesungshinweise.md#übung-1-texte-schreiben) („Woran du ein gutes Ergebnis erkennst“, Punkt Übersetzung). Fortsetzung: [ue1-c-rueck.md](ue1-c-rueck.md) (Rückübersetzung im neuen Chat; die englischen Texte unten sind dafür der Input).

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt (Turn 3, im selben Chat):**

```text
Übersetze deine letzte Version der Antwort ins Englische.
Ton: höflich, geschäftlich, britisches Englisch.
```

**Ziel laut Material:** Höfliche, geschäftliche Übersetzung in britischem Englisch, die Auftragsnummer, Stückzahl, KW-Angaben und Platzhalter erhält und weder Zusagen verliert noch hinzufügt.

## Bewertung

Geprüft wurde jeweils die englische Fassung (Turn 3) gegen die **eigene** förmliche deutsche Vorlage des Modells (Turn 2) und gegen die Kundenmail.

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Britische Konventionen („Dear Mr Brenner“ ohne Punkt, „Yours sincerely“) | ja | ja | ja (und erklärt sie im Hinweis) |
| Britische Schreibweise/Wortwahl | ja („ring you“, „reach me on“, „consignment“); kein Wort mit -ise/-ize im Text | ja („apologise“) | ja („agree the next steps“) |
| Keine US-Schreibweisen | ja | ja | ja |
| Auftragsnummer 4711-NT erhalten | ja | ja | ja |
| Stückzahl 120 erhalten | ja | ja | ja |
| Teillieferung 60 Stück erhalten | – (schon in der deutschen Vorlage nur `[MENGE]` → `[QUANTITY]`) | ja | ja |
| KW 18 erhalten | ja („calendar week 18“) | ja („calendar week 18“) | ja („calendar week 18“) + Tipp „week commencing [DATE]“ |
| Rechnung RE-2024-0815 / 85 Euro | Rechnung ja; 85 Euro fehlen schon in der Vorlage | ja („EUR 85“) | ja („EUR 85“) |
| Alle Platzhalter erhalten und übersetzt | ja (6 von 6) | ja (7 von 7) | ja (alle, inkl. Auswahl-Platzhalter „POSSIBLE BY DATE / NOT POSSIBLE BECAUSE …“) |
| Keine Zusage verloren | ja | ja | ja |
| Keine Zusage hinzugefügt | ja | ja | ja |
| Ton höflich, geschäftlich | ja | ja | ja |
| Sprachliche Schwächen | „we have not met it [trust]“ etwas holprig | „call you on [DAY/TIME] on [TELEPHONE NUMBER]“ (doppeltes „on“) | „sincerely regret“ etwas schwächer als „bedauern außerordentlich“ |
| **Gesamt** | **gut** – treue Übersetzung, aber Lücken aus A/B werden mitübersetzt | **sehr gut** | **sehr gut**, mit hilfreichem Hinweis zur KW |

## Gefundene Fehler mit Beleg

**Übersetzungsfehler im engeren Sinn: keine.** Alle drei Modelle übersetzen inhaltlich deckungsgleich. Fachbegriff „Steuergehäuse“ wird überall korrekt zu „control housings“ (im Testlauf [demo-7b](demo-7b-vorgaben-englisch.md) hatte Haiku noch „steering housing“ geschrieben – der Fehler trat hier nicht auf). Zahlen geprüft: 4711-NT, 120, 60 (Sonnet/Opus), KW 18, RE-2024-0815, 85 (Sonnet/Opus) stehen in Turn 3 genau so wie in Turn 2 und in der Kundenmail.

Beobachtungen, die man trotzdem kennen sollte:

1. **Lücken aus Aufgabe A werden treu weitergereicht (Haiku).** Haikus deutsche Vorlage nennt die vom Kunden angebotene Teillieferung „von 60 Stück“ nicht mehr, sondern „Teillieferung von [MENGE] Stück“. Auch die 10-%-Forderung und die 85 Euro werden nicht genannt („Ihre Anmerkungen zu einem Nachlass sowie zu den Frachtkosten“). Die Übersetzung übernimmt das korrekt als „partial delivery of [QUANTITY] units“. Das Kriterium „Stückzahl erhalten“ ist damit erfüllt – trotzdem fehlt dem englischen Leser die Zahl 60. Eine Übersetzungs- oder Rückübersetzungsprüfung findet so etwas **nicht**, weil sie nur mit der deutschen Vorlage vergleicht.
2. **Kleine Nuancenverschiebungen.**
   - Opus: „Wir bedauern außerordentlich“ → „We sincerely regret“ (etwas schwächer). „Hiermit bestätigen wir Ihnen verbindlich den [NEUER LIEFERTERMIN]“ → „We hereby confirm a firm delivery date of …“ – korrekt, aber die Zusage ist schon im Deutschen sehr stark: Sobald der Platzhalter gefüllt ist, ist es eine verbindliche schriftliche Zusage. Opus hatte in Turn 1 darauf hingewiesen, den Termin erst nach Bestätigung durch Fertigung/Logistik einzutragen.
   - Sonnet: Überschrift „Entgegenkommen“ → „Goodwill gesture“. Inhaltlich gleichwertig; für einen englischen Leser kann „Goodwill gesture“ als Überschrift aber schon nach einem Angebot klingen. Der Text darunter sagt nur „We are passing your request on“.
   - Haiku: „Wann dürfen wir Sie am besten anrufen“ → „May we ring you at a convenient time“ – gut britisch, aber aus der offenen Frage nach dem Zeitpunkt wird eine Ja/Nein-Frage.
3. **„Week 18“-Stolperstein trat nicht auf.** Die Lösungshinweise warnen, „KW 18“ werde manchmal zu „week 18“. Alle drei Modelle schreiben „calendar week 18“. Das ist klarer, aber für britische Leser ebenfalls ungewohnt, weil man in Großbritannien selten mit Kalenderwochen arbeitet. Nur Opus weist von sich aus darauf hin und schlägt „the week commencing [DATE]“ vor.
4. **Format-Umstellung „85 Euro“ → „EUR 85“ (Sonnet, Opus).** Korrekt und im Englischen üblich – bei der Rückübersetzung aber kein Fehler, falls „85 EUR“ zurückkommt.
5. **Kein Hinweis zum Prüfen (Haiku, Sonnet).** Nur Opus erklärt die Konventionen und gibt einen Tipp zur KW. Haiku und Sonnet liefern den Text kommentarlos. Das ist kein Fehler, zeigt aber: Ob Teilnehmende auf „calendar week“ aufmerksam werden, hängt vom Tool ab.

## Lehren für die Auswertung

- **Die Übung funktioniert wie gedacht.** Die Übersetzung im selben Chat klappt bei allen Modellen ohne erneutes Einfügen der Vorlage, und die britischen Konventionen werden zuverlässig umgesetzt. Zeitbedarf: unter einer Minute für den Prompt, der Lernanteil liegt in der Rückübersetzung ([ue1-c-rueck](ue1-c-rueck.md)).
- **Flüssig ≠ vollständig.** Gute Gelegenheit, im Plenum Haikus Fassung zu zeigen: perfektes Englisch, und trotzdem fehlen 60 Stück, 10 % und 85 Euro – nicht durch die Übersetzung, sondern schon im deutschen Entwurf. Lehre: Die Rückübersetzung prüft nur, ob die Übersetzung zur deutschen Vorlage passt. Ob die Vorlage selbst vollständig ist, muss man **vorher** mit der Checkliste aus Aufgabe A prüfen.
- **Britische Merkmale zum Zeigen:** „Dear Mr Brenner“ (ohne Punkt), „Yours sincerely“ (bei bekanntem Namen; „Yours faithfully“ nur bei „Dear Sir or Madam“), „apologise“ mit s, „ring you“, „reach me on [number]“. Opus erklärt das im Hinweis – das kann man direkt zeigen.
- **Kalenderwochen als Kulturthema:** „calendar week 18“ ist verständlich, aber in Großbritannien unüblich. Diskussionsfrage: „Würdet ihr einem britischen Kunden lieber ein Datum schreiben?“ Lösung: „the week commencing [DATE]“ oder ein konkretes Datum.
- **Platzhalter überleben die Übersetzung**, werden aber mitübersetzt (`[NEUER LIEFERTERMIN]` → `[NEW DELIVERY DATE]`). Wer später intern nach deutschen Platzhaltern sucht, findet sie nicht mehr – kleiner praktischer Hinweis.
- **Starke Zusagen in der Vorlage bleiben stark.** Opus' „We hereby confirm a firm delivery date“ ist korrekt übersetzt, aber eine rechtlich relevante Formulierung. Vor dem Versand muss der Platzhalter mit einem wirklich bestätigten Termin gefüllt sein.

## Hinweise zum Material

- Lösungshinweis „KW 18 wird manchmal zu ‚week 18‘“: Im Test schrieben alle drei Modelle „calendar week 18“. Der Diskussionspunkt bleibt richtig, sollte aber beide Varianten nennen und die Lösung „week commencing [DATUM]“ anbieten.
- Lösungshinweis „Auftragsnummer, Stückzahl, KW-Angaben und Platzhalter sind erhalten“: Ergänzen, dass die Übersetzung nur so vollständig sein kann wie der deutsche Entwurf. Fehlende Punkte aus A/B (z. B. 60 Stück, Rechnung, 10 %) fallen bei der Übersetzungsprüfung nicht auf.

---

## Gesprächsprotokoll: Haiku

### Nutzer 1
Ich arbeite im Vertrieb der Nordlicht Technik GmbH. Unten steht eine verärgerte Kundenmail wegen eines Lieferverzugs.

Schreibe mir einen Antwortentwurf, der:
- sich für die Verzögerung entschuldigt, ohne Schuld abzuwälzen,
- auf die konkreten Punkte des Kunden eingeht,
- einen nächsten Schritt anbietet (z. B. Rückruf oder neuer Liefertermin),
- höflich und sachlich ist und höchstens 150 Wörter hat.

Erfinde keine Fakten wie Liefertermine oder Rabatte. Wo mir Informationen fehlen, setze einen Platzhalter in eckigen Klammern, z. B. [NEUER LIEFERTERMIN].

Hier die Kundenmail:

Von: Markus Brenner <m.brenner@kunde-example.com>
An: vertrieb@nordlicht-technik.example.com
Datum: Montag, 08:47 Uhr
Betreff: WIE LANGE NOCH??? Auftrag 4711-NT / Steuergehäuse

Sehr geehrte Damen und Herren,

ich bin ehrlich gesagt ziemlich sauer. Wir haben bei Ihnen im März 120 Steuergehäuse SG-40 bestellt, Auftragsnummer 4711-NT, zugesagt war die Lieferung für KW 18. Jetzt haben wir KW 21 und bei uns ist NICHTS angekommen. Kein Anruf, keine Mail, nichts. Mein Einkauf hat zweimal bei Ihnen angerufen und wurde beide Male auf "nächste Woche" vertröstet.

Sie müssen verstehen, wir haben unserem eigenen Kunden einen festen Termin zugesagt und stehen jetzt selbst blöd da. Unsere Montage steht teilweise still, weil die Gehäuse fehlen. Das kostet uns jeden Tag Geld. So etwas habe ich in acht Jahren Zusammenarbeit mit Ihnen noch nicht erlebt, und eigentlich waren wir immer zufrieden.

Was ich jetzt brauche, ist ein verbindlicher Liefertermin, und zwar schriftlich und nicht wieder "voraussichtlich". Wenn es nicht anders geht, nehmen wir auch eine Teillieferung von 60 Stück, Hauptsache es kommt überhaupt etwas.

Außerdem erwarte ich, dass Sie uns für den ganzen Ärger entgegenkommen. Ich denke da an mindestens 10 % Nachlass auf diesen Auftrag. Das ist bei dem Schaden, den wir haben, wirklich nicht zu viel verlangt.

Und noch etwas, was mir bei der Gelegenheit aufgefallen ist: Auf Ihrer Rechnung RE-2024-0815 vom letzten Monat (das war die Ersatzteillieferung) stehen Frachtkosten von 85 Euro, obwohl wir damals frei Haus vereinbart hatten. Können Sie das bitte prüfen und korrigieren? Meine Buchhaltung fragt schon nach.

Ich erwarte bis spätestens Mittwoch eine Rückmeldung, sonst muss ich mich ernsthaft nach einem anderen Lieferanten umsehen.

Mit freundlichen Grüßen
Markus Brenner
Leitung Einkauf
Brenner Gerätebau GmbH (fiktiv)
Musterweg 12, 00000 Beispielstadt
Tel. 0000 123456

### Assistent 1
**Betreff:** Auftrag 4711-NT – Ihre Anfrage zur Lieferung

Sehr geehrter Herr Brenner,

vielen Dank für Ihre Nachricht. Es tut uns aufrichtig leid, dass die Lieferung der 120 Steuergehäuse SG-40 (Auftrag 4711-NT) nicht wie zugesagt in KW 18 erfolgt ist und Sie von uns keine Information erhalten haben. Wir verstehen, wie belastend das für Ihre Montage und Ihre Kundentermine ist.

Wir prüfen den Auftrag derzeit mit Nachdruck. Bis spätestens Mittwoch, [UHRZEIT], melden wir uns bei Ihnen mit einem verbindlichen, schriftlichen Liefertermin: [NEUER LIEFERTERMIN]. Sofern ein Teil der Ware früher verfügbar ist, bieten wir Ihnen gerne eine Teillieferung von [MENGE] Stück an.

Auch Ihren Wunsch nach einem Nachlass und die Frachtkosten auf Rechnung RE-2024-0815 prüfen wir und antworten Ihnen dazu gesondert bis [DATUM].

Gerne rufe ich Sie zeitnah an, um die Details zu besprechen. Wann passt es Ihnen am besten? Alternativ erreichen Sie mich unter [TELEFON].

Mit freundlichen Grüßen

[VORNAME NACHNAME]
[FUNKTION], Nordlicht Technik GmbH

*Hinweis:* Die Mail nennt die Rechnung "vom letzten Monat" mit der Nummer RE-2024-0815. Bitte Rechnungsnummer und Jahr vor dem Versand prüfen. Der Entwurf enthält keine Zusage zu Nachlass oder Frachtkosten.

### Nutzer 2
Formuliere die Antwort förmlicher – so, wie wir einem langjährigen Großkunden schreiben würden.

### Assistent 2
**Betreff:** Auftrag 4711-NT – Lieferung Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

vielen Dank für Ihr Schreiben. Wir bedauern die Verzögerung bei der Lieferung der 120 Steuergehäuse SG-40 im Rahmen des Auftrags 4711-NT außerordentlich. Die für KW 18 zugesagte Lieferung ist nicht erfolgt, und Sie haben von uns zu keinem Zeitpunkt eine Information erhalten. Auch Ihre beiden Anrufe hätten eine verlässliche Auskunft verdient. Wir sind uns bewusst, welche Folgen dies für Ihre Montage und Ihre Zusagen gegenüber Ihren Kunden hat.

Die Zusammenarbeit mit Ihrem Haus besteht seit acht Jahren, und wir wissen dieses Vertrauen sehr zu schätzen. Umso mehr bedauern wir, dass wir ihm in diesem Fall nicht gerecht geworden sind.

Wir prüfen den Auftrag derzeit mit höchster Priorität. Bis spätestens Mittwoch, [UHRZEIT] Uhr, erhalten Sie von uns eine schriftliche und verbindliche Aussage zum Liefertermin: [NEUER LIEFERTERMIN]. Sollte ein Teil der Ware früher bereitgestellt werden können, bieten wir Ihnen gerne eine Teillieferung von [MENGE] Stück an.

Ihre Anmerkungen zu einem Nachlass sowie zu den Frachtkosten auf Rechnung RE-2024-0815 nehmen wir ernst. Wir prüfen beide Punkte sorgfältig und antworten Ihnen hierzu gesondert bis [DATUM].

Für ein persönliches Gespräch stehe ich Ihnen gerne zur Verfügung. Wann dürfen wir Sie am besten anrufen, oder Sie erreichen mich direkt unter [TELEFON].

Mit freundlichen Grüßen

[VORNAME NACHNAME]
[FUNKTION]
Nordlicht Technik GmbH

### Nutzer 3
Übersetze deine letzte Version der Antwort ins Englische. Ton: höflich, geschäftlich, britisches Englisch.

### Assistent 3
**Subject:** Order 4711-NT – Delivery of SG-40 Control Housings

Dear Mr Brenner,

Thank you for your letter. We sincerely regret the delay in delivering the 120 SG-40 control housings under order 4711-NT. The delivery originally confirmed for calendar week 18 has not taken place, and you received no information from us at any point. Your two calls deserved a clear and reliable answer. We are fully aware of the impact this has on your assembly work and on your commitments to your own customers.

We have valued our cooperation with your company for eight years and greatly appreciate that trust. We regret all the more that we have not met it in this instance.

We are giving this order our highest priority. By Wednesday, [TIME], you will receive from us a written and binding statement of the delivery date: [NEW DELIVERY DATE]. Should part of the consignment be ready earlier, we would be happy to offer a partial delivery of [QUANTITY] units.

We take your remarks on a discount and on the freight charges on invoice RE-2024-0815 seriously. We are reviewing both points carefully and will reply separately by [DATE].

I would be glad to discuss this with you personally. May we ring you at a convenient time, or you may reach me directly on [TELEPHONE].

Yours sincerely,

[FIRST NAME SURNAME]
[POSITION]
Nordlicht Technik GmbH

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1
Ich arbeite im Vertrieb der Nordlicht Technik GmbH. Unten steht eine verärgerte Kundenmail wegen eines Lieferverzugs.

Schreibe mir einen Antwortentwurf, der:
- sich für die Verzögerung entschuldigt, ohne Schuld abzuwälzen,
- auf die konkreten Punkte des Kunden eingeht,
- einen nächsten Schritt anbietet (z. B. Rückruf oder neuer Liefertermin),
- höflich und sachlich ist und höchstens 150 Wörter hat.

Erfinde keine Fakten wie Liefertermine oder Rabatte. Wo mir Informationen fehlen, setze einen Platzhalter in eckigen Klammern, z. B. [NEUER LIEFERTERMIN].

Hier die Kundenmail:
[Inhalt von kundenmail_beschwerde.txt: Markus Brenner, Leitung Einkauf, Brenner Gerätebau GmbH, Betreff "WIE LANGE NOCH??? Auftrag 4711-NT / Steuergehäuse". Er bemängelt, dass 120 Steuergehäuse SG-40 nicht wie zugesagt in KW 18 geliefert wurden (jetzt KW 21). Es gab keine Information, und zwei Anrufe wurden auf "nächste Woche" vertröstet. Die Montage steht teilweise still. Er verlangt einen verbindlichen, schriftlichen Liefertermin, akzeptiert eine Teillieferung von 60 Stück und fordert mindestens 10 % Nachlass. Außerdem beanstandet er 85 Euro Frachtkosten auf Rechnung RE-2024-0815, obwohl "frei Haus" vereinbart war. Er erwartet eine Rückmeldung bis Mittwoch, sonst sucht er einen anderen Lieferanten.]

*(Anmerkung: So im Protokoll des Testlaufs festgehalten; inhaltlich entspricht das der vollständigen [Kundenmail](../07_Beispielmaterial/kundenmail_beschwerde.txt).)*

### Assistent 1
Hier ist ein Entwurf (ca. 135 Wörter):

**Betreff: Auftrag 4711-NT / Steuergehäuse SG-40**

Sehr geehrter Herr Brenner,

vielen Dank für Ihre offene Nachricht. Es tut uns leid, dass Ihre 120 Steuergehäuse nicht wie zugesagt in KW 18 geliefert wurden. Wir hätten Sie von uns aus informieren müssen, und die wiederholte Vertröstung war nicht in Ordnung.

Zu Ihren Punkten:
- **Liefertermin:** Wir bestätigen Ihnen bis Mittwoch schriftlich einen verbindlichen Termin: [NEUER LIEFERTERMIN]. Eine Teillieferung von 60 Stück prüfen wir und nennen Ihnen dazu [TERMIN TEILLIEFERUNG].
- **Entgegenkommen:** Ihren Wunsch nach einem Nachlass besprechen wir intern und melden uns mit [ERGEBNIS/ANGEBOT].
- **Rechnung RE-2024-0815:** Wir prüfen die Frachtkosten von 85 Euro und korrigieren sie, falls "frei Haus" vereinbart war. [ERGEBNIS DER PRÜFUNG]

Gern rufe ich Sie am [TAG/UHRZEIT] unter [TELEFONNUMMER] an, um alles persönlich zu besprechen.

Mit freundlichen Grüßen
[NAME]
Vertrieb, Nordlicht Technik GmbH

Hinweis: Ich habe weder einen Rabatt noch einen Termin zugesagt. Bitte klären Sie vor dem Versand intern, was Sie tatsächlich anbieten können.

### Nutzer 2
Formuliere die Antwort förmlicher – so, wie wir einem langjährigen Großkunden schreiben würden.

### Assistent 2
Hier ist die förmlichere Fassung:

**Betreff: Ihr Auftrag 4711-NT – Steuergehäuse SG-40**

Sehr geehrter Herr Brenner,

haben Sie vielen Dank für Ihr Schreiben. Wir bedauern aufrichtig, dass die 120 Steuergehäuse SG-40 nicht, wie zugesagt, in der KW 18 geliefert wurden. Dass wir Sie nicht von uns aus informiert und Ihren Einkauf mehrfach vertröstet haben, entspricht nicht dem Anspruch, den wir an unsere Zusammenarbeit stellen. Dafür bitten wir um Entschuldigung.

Zu den von Ihnen genannten Punkten:

1. **Liefertermin:** Wir werden Ihnen bis Mittwoch einen verbindlichen Liefertermin schriftlich bestätigen: [NEUER LIEFERTERMIN]. Die von Ihnen angeregte Teillieferung von 60 Stück prüfen wir umgehend; den möglichen Termin nennen wir Ihnen mit [TERMIN TEILLIEFERUNG].
2. **Entgegenkommen:** Ihr Anliegen leiten wir an die zuständige Stelle weiter und teilen Ihnen das Ergebnis mit: [ERGEBNIS/ANGEBOT].
3. **Rechnung RE-2024-0815:** Wir überprüfen die berechneten Frachtkosten von 85 Euro und veranlassen gegebenenfalls eine Korrektur. [ERGEBNIS DER PRÜFUNG]

Gerne rufe ich Sie am [TAG/UHRZEIT] unter [TELEFONNUMMER] an, um das weitere Vorgehen persönlich mit Ihnen abzustimmen.

Wir schätzen die langjährige Zusammenarbeit sehr und danken Ihnen für Ihr Vertrauen.

Mit freundlichen Grüßen

[NAME]
[FUNKTION], Vertrieb
Nordlicht Technik GmbH

### Nutzer 3
Übersetze deine letzte Version der Antwort ins Englische.
Ton: höflich, geschäftlich, britisches Englisch.

### Assistent 3
**Subject: Your Order 4711-NT – SG-40 Control Housings**

Dear Mr Brenner,

Thank you for your message. We sincerely regret that the 120 SG-40 control housings were not delivered in calendar week 18 as promised. That we did not inform you proactively, and that your purchasing department was put off more than once, falls short of the standard we set for our working relationship. We apologise for this.

With regard to the points you raised:

1. **Delivery date:** We will confirm a binding delivery date to you in writing by Wednesday: [NEW DELIVERY DATE]. We are looking into the partial delivery of 60 units that you suggested as a matter of urgency, and will let you know the possible date: [PARTIAL DELIVERY DATE].
2. **Goodwill gesture:** We are passing your request on to the relevant department and will inform you of the outcome: [OUTCOME/OFFER].
3. **Invoice RE-2024-0815:** We are reviewing the freight charges of EUR 85 and will arrange a correction if appropriate. [RESULT OF REVIEW]

I would be happy to call you on [DAY/TIME] on [TELEPHONE NUMBER] to discuss the next steps with you personally.

We greatly value our long-standing relationship and thank you for your continued trust.

Yours sincerely,

[NAME]
[JOB TITLE], Sales
Nordlicht Technik GmbH

---

## Gesprächsprotokoll: Opus

### Nutzer 1
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
[INHALT VON /home/daniel/tbc-ai-tutorials/07_Beispielmaterial/kundenmail_beschwerde.txt]

*(Anmerkung: Im Testlauf wurde an dieser Stelle der vollständige Text der [Kundenmail](../07_Beispielmaterial/kundenmail_beschwerde.txt) eingesetzt.)*

### Assistent 1
Hier ist ein Antwortentwurf (ca. 140 Wörter ohne Signatur):

---

**Betreff:** AW: Auftrag 4711-NT / Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

vielen Dank für Ihre offenen Worte. Es tut mir sehr leid, dass die 120 Steuergehäuse SG-40 nicht wie zugesagt in KW 18 bei Ihnen eingetroffen sind und Sie von uns keine verlässliche Auskunft bekommen haben. Mir ist klar, dass Sie dadurch bei Ihrem Kunden und in Ihrer Montage in eine schwierige Lage geraten sind.

Zu Ihren Punkten:
- **Liefertermin:** Wir bestätigen Ihnen verbindlich den [NEUER LIEFERTERMIN].
- **Teillieferung:** Eine Teillieferung von 60 Stück ist [MÖGLICH BIS DATUM / NICHT MÖGLICH, WEIL …].
- **Nachlass:** Ihren Wunsch nach 10 % Nachlass habe ich an [ZUSTÄNDIGE PERSON] weitergegeben. Sie erhalten bis [DATUM] eine Antwort.
- **Rechnung RE-2024-0815:** Wir prüfen die berechneten Frachtkosten von 85 Euro und melden uns bis [DATUM].

Gern rufe ich Sie [TAG/UHRZEIT] an, um alles persönlich zu besprechen.

Mit freundlichen Grüßen
[NAME]
[POSITION]
Nordlicht Technik GmbH
[TELEFON]

---

**Hinweise:**
- Schicken Sie die Antwort vor Mittwoch ab, denn bis dahin erwartet Herr Brenner eine Rückmeldung.
- Den Liefertermin sollten Sie erst eintragen, wenn Fertigung oder Logistik ihn wirklich bestätigt haben. Der Kunde verlangt ausdrücklich keinen „voraussichtlichen“ Termin.
- Über den Nachlass habe ich bewusst nichts entschieden. Klären Sie das bitte intern.

### Nutzer 2
Formuliere die Antwort förmlicher – so, wie wir einem langjährigen
Großkunden schreiben würden.

### Assistent 2
Hier ist eine förmlichere Fassung (ca. 150 Wörter ohne Signatur):

---

**Betreff:** Ihr Auftrag 4711-NT – Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

haben Sie vielen Dank für Ihr Schreiben. Wir bedauern außerordentlich, dass die Lieferung der 120 Steuergehäuse SG-40 nicht wie zugesagt in KW 18 erfolgt ist und wir Sie nicht rechtzeitig und verlässlich informiert haben. Das entspricht nicht dem Anspruch, den wir an eine Zusammenarbeit von acht Jahren haben. Die Folgen für Sie und Ihre Montage nehmen wir sehr ernst.

Zu Ihren Anliegen:
- **Liefertermin:** Hiermit bestätigen wir Ihnen verbindlich den [NEUER LIEFERTERMIN].
- **Teillieferung:** Eine Vorablieferung von 60 Stück ist [MÖGLICH ZUM DATUM / NICHT MÖGLICH, WEIL …].
- **Nachlass:** Ihr Anliegen wird derzeit von [ZUSTÄNDIGE PERSON/STELLE] geprüft. Wir geben Ihnen bis [DATUM] Bescheid.
- **Rechnung RE-2024-0815:** Wir prüfen die ausgewiesenen Frachtkosten von 85 Euro und informieren Sie bis [DATUM].

Gern würde ich die weiteren Schritte am [TAG/UHRZEIT] in einem persönlichen Telefonat mit Ihnen abstimmen.

Mit freundlichen Grüßen
[NAME]
[POSITION]
Nordlicht Technik GmbH
[TELEFON] | [E-MAIL]

---

### Nutzer 3
Übersetze deine letzte Version der Antwort ins Englische.
Ton: höflich, geschäftlich, britisches Englisch.

### Assistent 3
Hier ist die englische Fassung in britischem Englisch:

---

**Subject:** Your order 4711-NT – SG-40 control housings

Dear Mr Brenner,

Thank you for your letter. We sincerely regret that the 120 SG-40 control housings were not delivered in calendar week 18 as agreed. We also regret that we did not keep you informed in a timely and reliable manner. This falls short of the standard we set for a partnership of eight years, and we take the consequences for you and your assembly operations very seriously.

Regarding your points:
- **Delivery date:** We hereby confirm a firm delivery date of [NEW DELIVERY DATE].
- **Partial delivery:** An advance delivery of 60 units is [POSSIBLE BY DATE / NOT POSSIBLE BECAUSE …].
- **Discount:** Your request is currently being reviewed by [RESPONSIBLE PERSON/DEPARTMENT]. We will let you know by [DATE].
- **Invoice RE-2024-0815:** We are looking into the freight charges of EUR 85 shown on this invoice and will update you by [DATE].

I would welcome the opportunity to agree the next steps with you in a personal telephone call on [DAY/TIME].

Yours sincerely,
[NAME]
[POSITION]
Nordlicht Technik GmbH
[TELEPHONE] | [EMAIL]

---

**Hinweis:** Weil die Mail mit „Dear Mr Brenner“ und dem Namen beginnt, endet sie im britischen Englisch mit „Yours sincerely“. „Mr“ schreibt man im Britischen ohne Punkt. „KW 18“ habe ich mit „calendar week 18“ übersetzt. Falls Ihr Kunde keine Kalenderwochen verwendet, schreiben Sie besser das Datum der Woche hin, z. B. „the week commencing [DATE]“.
