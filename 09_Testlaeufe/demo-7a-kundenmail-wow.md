# Testlauf: Demo 7 – Kundenmail: drei Anliegen + Antwort ohne Versprechen

**Herkunft:** [demo_fehler_zeigen.md, Demo 7 (positiv)](../07_Beispielmaterial/demo_fehler_zeigen.md) · Material: [kundenmail_beschwerde.txt](../07_Beispielmaterial/kundenmail_beschwerde.txt) · Abgleich mit [Trainer-Lösungshinweise, Übung 1](../06_Uebungen/Trainer-Loesungshinweise.md)

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt:**

```
Hier ist die Mail eines verärgerten Kunden. Fasse in drei Stichpunkten zusammen, was er konkret von uns will, und schlage eine freundliche, kurze Antwort vor, die nichts verspricht, was wir nicht halten können.

[Inhalt von kundenmail_beschwerde.txt einfügen]
```

**Ziel laut Material:** Positiver Wow-Moment – aus der emotionalen Mail werden drei klare Anliegen (Liefertermin, Rabattforderung, Rückfrage zur Rechnung) und ein brauchbarer Antwortentwurf. Anschlussfrage: „Würdet ihr das so abschicken? Was müsstet ihr noch prüfen?“

**Soll laut Quelle:** Auftrag 4711-NT, 120 Steuergehäuse SG-40, zugesagt KW 18, jetzt KW 21. Forderungen: (1) verbindlicher, schriftlicher Liefertermin, notfalls Teillieferung 60 Stück; (2) mindestens 10 % Nachlass auf diesen Auftrag; (3) Prüfung/Korrektur der Frachtkosten 85 € auf Rechnung RE-2024-0815 (frei Haus vereinbart). Dazu: Frist bis Mittwoch, Drohung mit Lieferantenwechsel, acht Jahre Zusammenarbeit.

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Genau 3 Stichpunkte | ja | ja | ja |
| Liefertermin schriftlich + Teillieferung 60 Stk. | ja | ja | ja |
| Mind. 10 % Nachlass | ja („10 %“, „mindestens“ fehlt) | ja | ja |
| Fracht 85 € / RE-2024-0815 / frei Haus | ja | ja | ja |
| Frist Mittwoch + Drohung erkannt (Zusatz) | ja | ja, sauber als „keine eigene Forderung“ eingeordnet | ja |
| Zahlen/Nummern korrekt (4711-NT, 120, SG-40, KW 18/21, 60, 10 %, 85 €) | ja | ja | ja |
| Antwort: kein konkreter Liefertermin | ja | ja, **aber** verspricht „Den schriftlichen Termin erhalten Sie bis Mittwoch“ | ja, Rückmeldung bis [Mittwoch, Uhrzeit] als Platzhalter |
| Antwort: keine Rabattzusage | ja, aber „gute Lösung finden“ weckt Erwartung | ja („weitergegeben“) | ja („weitergegeben“) |
| Antwort: keine Gutschriftzusage | ja („prüfen“) | bedingte Zusage („Sollte frei Haus vereinbart gewesen sein, korrigieren wir …“) | ja („prüfen“) |
| Platzhalter statt erfundener Fakten | [Name], [Funktion] | [Name] | viele: [Mittwoch, Uhrzeit], [zuständige Stelle], [Telefonnummer] … |
| Erfundene interne Schritte | nein | „an die zuständige Stelle weitergegeben“ (noch nicht passiert) | „heute persönlich übernommen“, „kläre gerade mit unserer Fertigung“, „weitergegeben“ |
| Auftrag 4711-NT in der Antwort | ja (Betreff + Text) | Betreff | Betreff |
| Länge Antworttext (Wörter, ca.) | 138 | 117 | 159 |
| Hinweise für den Absender | keine | ja, 4 Hinweise | ja, 4 Hinweise + Platzhalter-Erinnerung |
| **Gesamt** | gut, knapp und demotauglich | gut, Selbstkritik gelungen, Antwort verspricht aber einen Termin | **am besten** – aber längste Antwort, erfundene Handlungen |

Wortzahlen per Python (`len(text.split())`, Anrede bis Signatur) nachgezählt.

## Gefundene Fehler mit Beleg

Kein Modell hat eine Zahl, Nummer oder Forderung falsch wiedergegeben; alle drei Anliegen sind bei allen vollständig. Die Abweichungen liegen in den **Zusagen der Antwortentwürfe** – also genau dort, wo der Prompt „nichts versprechen“ verlangt:

1. **Sonnet verspricht einen verbindlichen Termin bis Mittwoch.** Antwort: „Den schriftlichen Termin erhalten Sie von uns bis **Mittwoch**.“ Ob die Fertigung bis Mittwoch einen verbindlichen Termin nennen kann, weiß niemand – das ist ein Versprechen, das evtl. nicht zu halten ist. Sonnet erkennt das selbst in den Hinweisen („Falls nicht, ersetzen Sie den Satz …“), widerspricht damit aber der eigenen Aussage „verspricht bewusst nur das, was wir sicher halten können“.
2. **Sonnet: bedingte Gutschriftzusage.** „Sollte die Lieferung ‚frei Haus‘ vereinbart gewesen sein, korrigieren wir die Rechnung selbstverständlich.“ Sachlich fair, aber eine Zusage – das Soll laut Lösungshinweisen ist „keine Gutschrift“.
3. **Haiku: weiche Zusagen.** „Bis Mittwoch melden wir uns … mit dem aktuellen Stand und einem *konkreten Terminvorschlag*“ (ob ein Vorschlag bis Mittwoch möglich ist, ist offen); „melden uns dazu *gleich* mit dem Ergebnis“ (Frachtkosten – „gleich“ ist eine Zeitzusage ohne Grundlage); „würden wir gern … eine gute Lösung finden“ beim Nachlass – kein Rabatt, aber der Kunde wird das als „es gibt etwas“ lesen.
4. **Opus erfindet interne Handlungen.** „Ich habe Ihr Anliegen heute persönlich übernommen und kläre gerade mit unserer Fertigung …“ und „Ihren Wunsch … habe ich an [zuständige Stelle] weitergegeben.“ Nichts davon steht in der Quelle; der Absender muss diese Schritte erst tun. (Sonnet ähnlich: „haben wir an die zuständige Stelle weitergegeben“.)
5. **Opus: Widerspruch „Schuldanerkenntnis“.** Opus begründet: „Entschuldigung ohne Schuldanerkenntnis“, schreibt aber „Sie haben völlig recht: Die Lieferung ist deutlich überfällig, und wir hätten Sie von uns aus informieren müssen.“ Das ist ein klares Eingeständnis – im Ton gut, aber die eigene Begründung stimmt nicht ganz.
6. **Opus länger als „kurz“.** Ca. 159 Wörter; die Lösungshinweise zu Übung 1 nennen „höchstens ca. 150 Wörter“.
7. **Sonnet: unbelegter Hinweis zur Rechnungsnummer.** „Auffällig ist die Rechnungsnummer RE-2024-0815 ‚vom letzten Monat‘. Prüfen Sie, ob die Nummer stimmt …“ Die Mail nennt kein Jahr; ein Widerspruch lässt sich aus der Quelle nicht belegen. Harmlos (Gegenprüfen schadet nie), aber eine Vermutung der KI.
8. Kleinigkeit Haiku: „10 % Nachlass“ statt „mindestens 10 %“ – die Untergrenze geht verloren.
9. Kleinigkeit Firmenname: Haiku/Sonnet „Nordlicht Technik“, Opus „Nordlicht-Technik“. Die Quelle kennt nur die Domain „nordlicht-technik.example.com“ – die Schreibweise ist geraten.

## Lehren für die Auswertung

- **Der Wow-Moment funktioniert zuverlässig.** Alle drei Modelle liefern exakt die drei erwarteten Anliegen mit korrekten Zahlen und Nummern und erkennen zusätzlich die Frist bis Mittwoch. Kein Modell nennt einen konkreten Liefertermin oder sagt Prozente zu.
- **Die Anschlussfrage „Würdet ihr das so abschicken?“ hat echte Antworten.** Gute Prüfpunkte für das Plenum:
  - „Bis Mittwoch erhalten Sie den Termin“ (Sonnet) – könnt ihr das halten?
  - „Ich habe heute persönlich übernommen / mit der Fertigung geklärt / weitergegeben“ (Opus) – stimmt das schon?
  - „Melden uns gleich“, „gute Lösung finden“ (Haiku) – welche Erwartung weckt das beim Kunden?
  - War „frei Haus“ wirklich vereinbart? Wer entscheidet über den Nachlass?
- **Feine Lehre:** Die KI hält sich an „keine harten Zusagen“ (Datum, Prozent), schmuggelt aber **weiche Zusagen** (Fristen, erledigte Handlungen) hinein. Genau das muss ein Mensch lesen.
- **Selbstkommentar ≠ Wahrheit:** Sonnet und Opus erklären, warum ihre Antwort „nichts verspricht“ – und beide Erklärungen stimmen nicht ganz (Sonnet: Termin bis Mittwoch; Opus: „ohne Schuldanerkenntnis“ trotz „Sie haben völlig recht“). Gut zum Zeigen: Auch die Begründung der KI gegenlesen.
- **Platzhalter sind ein Qualitätsmerkmal:** Opus setzt [Mittwoch, Uhrzeit], [zuständige Stelle], [Telefonnummer]. Das ist der Stil, den Übung 1 anstrebt.
- **Zeit:** Im Zeitplan sind 3 Minuten (0:09–0:12) vorgesehen. Die Antworten von Sonnet und Opus mit Zusatzhinweisen sind zu lang zum Vorlesen. Empfehlung: nur die drei Stichpunkte und den Antwortentwurf zeigen, Zusatzhinweise überspringen – oder sie bewusst als Brücke zu „Würdet ihr das abschicken?“ nutzen.

## Probleme im Material / Verbesserungsvorschlag

- Die Übung funktioniert wie beschrieben; die drei Anliegen in [demo_fehler_zeigen.md](../07_Beispielmaterial/demo_fehler_zeigen.md) passen exakt zu dem, was die Modelle liefern.
- Die Beispiele für die Anschlussfrage („den echten Liefertermin, die Rabattfreigabe, die Rechnung“) treffen die harten Punkte, nicht aber die in den Tests tatsächlich auftretenden weichen Zusagen. Vorschlag für Demo 7, Absatz „Was du zeigen willst“, am Ende ergänzen: *„Achte beim Gegenlesen auch auf weiche Zusagen: ‚Bis Mittwoch erhalten Sie den Termin‘, ‚melden uns gleich‘ oder ‚ich habe das bereits mit der Fertigung geklärt‘ – stimmt das wirklich und könnt ihr es halten?“*
- „Kurz“ ist im Prompt nicht definiert; Opus landet knapp über der 150-Wörter-Grenze aus den Lösungshinweisen zu Übung 1. Optional im Prompt „(max. 120 Wörter)“ ergänzen, wenn die Demo-Zeit knapp ist – das ist dann zugleich ein Beispiel für präzises Prompten.

---

## Gesprächsprotokoll: Haiku

### Nutzer 1
Hier ist die Mail eines verärgerten Kunden. Fasse in drei Stichpunkten zusammen, was er konkret von uns will, und schlage eine freundliche, kurze Antwort vor, die nichts verspricht, was wir nicht halten können.

[INHALT VON kundenmail_beschwerde.txt]

### Assistent 1
**Was Herr Brenner konkret will:**

- **Verbindlicher Liefertermin, schriftlich:** Für Auftrag 4711-NT (120 Steuergehäuse SG-40) verlangt er einen festen Termin statt "voraussichtlich". Eine Teillieferung von 60 Stück nimmt er notfalls an.
- **10 % Nachlass** auf diesen Auftrag als Ausgleich für den Schaden in seiner Montage.
- **Prüfung und Korrektur der Frachtkosten** von 85 € auf Rechnung RE-2024-0815, weil "frei Haus" vereinbart war. Seine Buchhaltung wartet darauf.

Er erwartet bis spätestens **Mittwoch** eine Rückmeldung, sonst droht er mit einem Lieferantenwechsel.

**Vorschlag für eine Antwort:**

> Betreff: Ihr Auftrag 4711-NT – Ihre Nachricht
>
> Sehr geehrter Herr Brenner,
>
> vielen Dank für Ihre Nachricht, und entschuldigen Sie bitte, dass Sie so lange ohne Information geblieben sind. Das hätte nicht passieren dürfen, und wir verstehen, wie belastend das für Ihre Montage und Ihren eigenen Kunden ist.
>
> Wir klären den aktuellen Stand Ihres Auftrags 4711-NT intern und prüfen, welche Mengen wann verfügbar sind, auch im Hinblick auf eine mögliche Teillieferung. Einen verbindlichen Termin möchten wir Ihnen erst nennen, wenn wir ihn sicher einhalten können. Bis Mittwoch melden wir uns bei Ihnen mit dem aktuellen Stand und einem konkreten Terminvorschlag.
>
> Die Frachtkosten auf Rechnung RE-2024-0815 prüfen wir ebenfalls und melden uns dazu gleich mit dem Ergebnis.
>
> Zu Ihrer Forderung nach einem Nachlass würden wir gern im Gespräch mit Ihnen eine gute Lösung finden, sobald der Sachverhalt geklärt ist.
>
> Mit freundlichen Grüßen
> [Name]
> [Funktion] · Nordlicht Technik

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1
Hier ist die Mail eines verärgerten Kunden. Fasse in drei Stichpunkten zusammen, was er konkret von uns will, und schlage eine freundliche, kurze Antwort vor, die nichts verspricht, was wir nicht halten können.

[Anhang: kundenmail_beschwerde.txt]

### Assistent 1
**Was Herr Brenner konkret von uns will**

- **Verbindlicher, schriftlicher Liefertermin** für Auftrag 4711-NT (120 Steuergehäuse SG-40, zugesagt für KW 18, jetzt KW 21). Notfalls akzeptiert er eine Teillieferung von 60 Stück. Er erwartet dazu eine Rückmeldung bis spätestens Mittwoch.
- **Preisnachlass von mindestens 10 %** auf diesen Auftrag als Entschädigung für den entstandenen Ärger und Schaden (Montagestillstand, Terminprobleme bei seinem eigenen Kunden).
- **Prüfung und Korrektur der Rechnung RE-2024-0815:** Dort stehen 85 € Frachtkosten, obwohl "frei Haus" vereinbart war.

Außerdem droht er damit, sich nach einem anderen Lieferanten umzusehen, wenn er bis Mittwoch keine Antwort hat. Das ist keine eigene Forderung, aber der Zeitdruck.

**Vorschlag für eine Antwort**

> Betreff: AW: Auftrag 4711-NT / Steuergehäuse SG-40
>
> Sehr geehrter Herr Brenner,
>
> vielen Dank für Ihre Nachricht. Es tut uns leid, dass die Lieferung nicht wie zugesagt eingetroffen ist und dass Sie dazu keine Rückmeldung von uns bekommen haben. Das hätte anders laufen müssen.
>
> Wir klären aktuell intern, wann wir Ihnen die Gehäuse verbindlich liefern können, auch in Form einer Teillieferung von 60 Stück. Den schriftlichen Termin erhalten Sie von uns bis **Mittwoch**.
>
> Die Frachtkosten auf der Rechnung RE-2024-0815 prüfen wir anhand der vereinbarten Konditionen. Sollte die Lieferung "frei Haus" vereinbart gewesen sein, korrigieren wir die Rechnung selbstverständlich.
>
> Ihren Wunsch nach einem Entgegenkommen beim Auftragspreis haben wir an die zuständige Stelle weitergegeben und melden uns dazu gesondert bei Ihnen.
>
> Mit freundlichen Grüßen
> [Name]
> Nordlicht Technik

**Hinweise zur Antwort (nicht für den Kunden gedacht)**

- Die Mail verspricht bewusst nur das, was wir sicher halten können: eine Rückmeldung bis Mittwoch, die Prüfung der Fracht und eine Entscheidung zum Nachlass. Sie nennt keinen Liefertermin und sagt keinen Rabatt zu.
- Vor dem Versand sollten Sie intern klären, ob Sie bis Mittwoch tatsächlich einen verbindlichen Termin nennen können. Falls nicht, ersetzen Sie den Satz durch eine ehrliche Zusage, zum Beispiel "bis Mittwoch melden wir uns mit dem aktuellen Stand".
- Auffällig ist die Rechnungsnummer RE-2024-0815 "vom letzten Monat". Prüfen Sie, ob die Nummer stimmt, bevor Sie sie im Antwortschreiben nennen.
- Über den Rabatt sollte jemand mit Entscheidungsbefugnis entscheiden.

---

## Gesprächsprotokoll: Opus

### Nutzer 1
Hier ist die Mail eines verärgerten Kunden. Fasse in drei Stichpunkten zusammen, was er konkret von uns will, und schlage eine freundliche, kurze Antwort vor, die nichts verspricht, was wir nicht halten können.

[INHALT VON kundenmail_beschwerde.txt]

### Assistent 1
**Was Herr Brenner konkret will:**

- **Einen verbindlichen Liefertermin, schriftlich**, für Auftrag 4711-NT (120 Steuergehäuse SG-40, zugesagt war KW 18). Ein „voraussichtlich“ reicht ihm nicht. Notfalls nimmt er auch eine **Teillieferung von 60 Stück**.
- **Ein Entgegenkommen für den Ärger**: Er verlangt **mindestens 10 % Nachlass** auf diesen Auftrag.
- **Die Prüfung und Korrektur der Rechnung RE-2024-0815**: Dort stehen 85 € Frachtkosten, obwohl „frei Haus“ vereinbart war.

Dazu kommt eine Frist: Er will **bis spätestens Mittwoch** eine Antwort, sonst sucht er sich einen anderen Lieferanten.

---

**Vorschlag für eine Antwort:**

> **Betreff:** AW: Auftrag 4711-NT / Steuergehäuse SG-40
>
> Sehr geehrter Herr Brenner,
>
> vielen Dank für Ihre offene Nachricht. Sie haben völlig recht: Die Lieferung ist deutlich überfällig, und wir hätten Sie von uns aus informieren müssen. Dass Sie dadurch selbst in eine schwierige Lage gegenüber Ihrem Kunden geraten sind, tut mir sehr leid.
>
> Ich habe Ihr Anliegen heute persönlich übernommen und kläre gerade mit unserer Fertigung, wann die 120 Gehäuse geliefert werden können und ob eine Teillieferung von 60 Stück früher möglich ist. Bis **[Mittwoch, Uhrzeit]** erhalten Sie von mir eine schriftliche Rückmeldung zum Liefertermin.
>
> Ihren Wunsch nach einem Entgegenkommen habe ich an **[zuständige Stelle / Geschäftsleitung]** weitergegeben. Die Rechnung RE-2024-0815 lasse ich ebenfalls prüfen, insbesondere die Frachtkosten von 85 € im Hinblick auf die vereinbarte Lieferung frei Haus. Zu beiden Punkten melde ich mich gesondert bei Ihnen.
>
> Wir schätzen die langjährige Zusammenarbeit mit Ihnen sehr und möchten das wieder in Ordnung bringen. Bei Fragen erreichen Sie mich direkt unter **[Telefonnummer]**.
>
> Mit freundlichen Grüßen
> **[Name]**
> **[Funktion]**
> Nordlicht-Technik

---

**Warum die Antwort so formuliert ist:**

- **Kein fester Liefertermin**: Die Mail sagt nur zu, dass bis Mittwoch eine Rückmeldung kommt. Dieses Versprechen können Sie halten, auch wenn die Fertigung noch keinen Termin nennen kann. Bitte schreiben Sie dort nur einen Zeitpunkt hinein, den Sie sicher einhalten können.
- **Kein Nachlass zugesagt**: Der Wunsch wird nur „weitergegeben“. Weder die 10 % noch ein anderer Betrag werden bestätigt.
- **Keine Gutschrift für die Fracht zugesagt**: Es heißt nur „prüfen“. Ob „frei Haus“ wirklich vereinbart war, sollten Sie im Angebot oder in der Auftragsbestätigung nachsehen.
- **Entschuldigung ohne Schuldanerkenntnis**: Der Ärger wird ernst genommen, aber es steht nichts darin, was nach einer Zusage für Schadenersatz klingt (z. B. für den Stillstand seiner Montage).

Ersetzen Sie die Platzhalter in eckigen Klammern vor dem Versand.
