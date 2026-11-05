# Testlauf: Übung 1 / Für Schnelle F – Perspektivwechsel: Antwort aus Kundensicht

**Herkunft:** [Übung 1: Texte schreiben, Aufgabe F](../06_Uebungen/Uebung_1_Texte_schreiben.md#aufgabe-f--perspektivwechsel) (Aufbau auf Aufgabe A) · Material: [kundenmail_beschwerde.txt](../07_Beispielmaterial/kundenmail_beschwerde.txt) · Abgleich mit [Trainer-Lösungshinweise, Übung 1](../06_Uebungen/Trainer-Loesungshinweise.md#übung-1-texte-schreiben)

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf (3 Turns im selben Chat):**

1. Startprompt aus Aufgabe A plus Kundenmail
2. Prompt aus Aufgabe F (Kundensicht, höchstens 5 Stichpunkte)
3. Überarbeitung. Das Übungsblatt gibt dafür **keinen** Prompt vor („Überarbeite die Antwort anschließend mit den Hinweisen, die du sinnvoll findest“). Im Test wurde verwendet: „Überarbeite die Antwort mit diesen Hinweisen. Bleib bei höchstens 150 Wörtern und mach weiterhin keine Zusagen, die ich nicht freigegeben habe.“

**Ziel laut Material:** Die KI bewertet den eigenen Entwurf kritisch aus Kundensicht (max. 5 Stichpunkte). Danach wird überarbeitet: sinnvolle Hinweise übernehmen, ohne neue Zusagen zu erfinden.

**Soll laut Quelle (Kundenmail):** Auftrag 4711-NT, 120 Steuergehäuse SG-40, zugesagt KW 18, jetzt KW 21, keine Information, zweimal vertröstet, Montage steht teilweise still, Ärger mit dem eigenen Kunden. Forderungen: verbindlicher schriftlicher Liefertermin (nicht „voraussichtlich“), notfalls Teillieferung 60 Stück, mindestens 10 % Nachlass, Prüfung/Korrektur Frachtkosten 85 € auf RE-2024-0815 (frei Haus vereinbart). Frist bis Mittwoch, sonst Lieferantenwechsel; acht Jahre Zusammenarbeit.

**Hinweis zur Testdurchführung:** Haiku bekam in Turn 1 nur eine **verdichtete Zusammenfassung** der Kundenmail, nicht den Originaltext (siehe Protokoll). Acht Jahre Zusammenarbeit und der Ärger mit dem eigenen Kunden fehlten deshalb in seiner Eingabe. Sonnet bekam den vollständigen Text. Bei Opus steht im Protokoll nur der Verweis auf die Datei. Bei Haiku hängt am Ende eine Meta-Notiz des Testlaufs („Verifikation mit anderen Modellen nicht durchgeführt …“). Sie stammt aus der Testumgebung, nicht aus dem Chat, und ist für Teilnehmende ohne Bedeutung.

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Turn 1: Entwurf ≤ 150 Wörter | ja (ca. 102) | ja (ca. 113) | ja (ca. 117) |
| Turn 1: alle 5 Anliegen angesprochen | teilweise: Teillieferung nur im Platzhalter, ohne „60 Stück“; KW 18/21 fehlt; Nachlass + Fracht in einem Satz zusammengefasst | ja | ja |
| Turn 1: keine erfundenen Zusagen | ja | Zusage „verbindlicher Termin bis spätestens Mittwoch“ | bedingte Rechnungskorrektur; erfundene Handlung „habe … weitergegeben“ |
| Turn 2: ≤ 5 Stichpunkte | ja (5) | ja (5, davon 1 positiv) | ja (5, Punkt 5 mit zwei Anliegen) |
| Turn 2: Kritik „weiterhin kein fester Termin“ | ja | ja | ja |
| Turn 2: Kritik am Nachlass („nur geprüft/weitergegeben“) | ja | ja | ja |
| Turn 2: Frist Mittwoch angesprochen | ja | nein | ja |
| Turn 2: weitere plausible Kritik | Teillieferung nicht konkret; Entschuldigung zu allgemein | keine Erklärung für den Verzug; keine feste Ansprechperson; acht Jahre nicht gewürdigt | keine Erklärung; Schaden (Montage, eigener Kunde) fehlt; feste Ansprechperson |
| Turn 3: ≤ 150 Wörter | ja (ca. 102) | ja (ca. 113) | ja (ca. 130; selbst angegeben „rund 145“) |
| Turn 3: Kritikpunkte umgesetzt | teilweise (persönliche Entschuldigung, Fristen als Platzhalter; „60 Stück“ fehlt weiter, stattdessen [MENGE]) | ja (Ursache als Platzhalter, Fristen je Punkt, acht Jahre, Ansprechpartner) | ja (Schaden, Ursache als Platzhalter, Entscheider + Frist, Ansprechpartner) |
| Turn 3: Platzhalter statt Termin/Rabatt/Gutschrift | ja | Termin/Rabatt ja; **„vereinbart war frei Haus“ als Tatsache** | Termin/Rabatt ja; bedingte Rechnungskorrektur bleibt |
| Turn 3: keine neuen Zusagen | ja (Fristen nur als Platzhalter) | **nein:** „Ich übernehme Ihren Fall persönlich“, „Ihr Ansprechpartner bleibe ich“, „verbindlich bis spätestens Mittwoch“ | teilweise: „Ihr direkter Ansprechpartner bin ich“, mit Hinweis „nur wenn intern abgestimmt“ |
| Hinweise an den Absender | nein | nein | ja, 3 Prüfhinweise (Mittwoch, Ansprechpartner, Rechnung mit Buchhaltung klären) |
| Inhalt verloren (Turn 1 → 3) | Betreffzeile; „85 Euro“/„frei Haus“ fehlen weiter | Montage-Stillstand fällt weg | „acht Jahre“ fällt weg |
| **Gesamt** | brav und vorsichtig, aber dünn; Kundenkritik plausibel | inhaltlich am stärksten überarbeitet, **übernimmt aber neue Zusagen** und eine ungeprüfte Tatsache | **am besten:** Kritik am treffendsten, Überarbeitung gut, Risiken selbst benannt |

Wortzahlen mit Python nachgezählt (`text.split()`, Anrede bis vor die Grußformel, Aufzählungszeichen nicht mitgezählt). Mit Grußformel und Signatur sind es jeweils 6–10 Wörter mehr; alle Entwürfe bleiben unter 150.

## Gefundene Fehler mit Beleg

1. **Sonnet macht in der Überarbeitung neue Zusagen, obwohl der Prompt das ausdrücklich verbietet.** Turn 3: „Ich übernehme Ihren Fall persönlich.“ und „Ihr Ansprechpartner bleibe ich: [NAME, DURCHWAHL].“ Das ist eine organisatorische Zusage, die der Nutzer nicht freigegeben hat. Sie kommt direkt aus der eigenen Kundenkritik („Es fehlt … eine feste Ansprechperson“). Opus übernimmt denselben Punkt („Ihr direkter Ansprechpartner bin ich“), weist aber selbst darauf hin: „Übernehmen Sie die Rolle als fester Ansprechpartner nur, wenn das intern abgestimmt ist.“
2. **Sonnet stellt eine Behauptung des Kunden als Tatsache dar.** Turn 3: „Ich prüfe die Frachtkosten von 85 Euro (**vereinbart war frei Haus**)“. Die Mail sagt nur: „obwohl wir damals frei Haus vereinbart hatten“. Ob das stimmt, ist offen. Der Satz wirkt wie ein Anerkenntnis, und das spricht gegen das Soll „keine Gutschrift“ aus den Lösungshinweisen.
3. **Sonnet sagt einen verbindlichen Termin bis Mittwoch zu.** Turn 1: „Ich bestätige Ihnen schriftlich bis [DATUM/UHRZEIT, spätestens Mittwoch] einen verbindlichen Termin“. Turn 3: „Schriftlich und verbindlich bis [DATUM/UHRZEIT, spätestens Mittwoch]“. Ob die Fertigung bis Mittwoch einen verbindlichen Termin nennen kann, ist unbekannt. Der Platzhalter verschleiert, dass „spätestens Mittwoch“ schon im Text steht. Derselbe Befund steht in [demo-7a-kundenmail-wow.md](demo-7a-kundenmail-wow.md).
4. **Opus: bedingte Rechnungskorrektur und erfundene Handlung.** Turn 1: „… und korrigieren die Rechnung, falls ‚frei Haus‘ vereinbart war.“ und „Ihre Anfrage habe ich an [ZUSTÄNDIGE PERSON] weitergegeben.“ Weitergegeben wurde noch nichts. In Turn 3 ist die erfundene Handlung weg („Über Ihre Anfrage entscheidet [NAME/FUNKTION]“). Die bedingte Korrektur bleibt, wird aber im Prüfhinweis offen benannt („Bitte klären Sie das vorher mit der Buchhaltung“).
5. **Haiku lässt Fakten aus der Mail weg.** Turn 1 erwähnt weder KW 18/21 noch die Teillieferung von 60 Stück. Beides steckt nur im Platzhalter „[NEUER LIEFERTERMIN ODER TEILLIEFERUNG, MENGE UND TERMIN]“. In Turn 3 fragt Haiku die Menge wieder per Platzhalter ab („[TEILLIEFERUNG JA/NEIN, MENGE, TERMIN]“), obwohl der Kunde „60 Stück“ selbst genannt hat. Zum Teil liegt das an der verkürzten Eingabe im Test, die 60 Stück standen aber auch dort.
6. **Opus zählt sich zu hoch.** Opus gibt „rund 145 Wörter“ an. Nachgezählt sind es ca. 130 (mit Signatur ca. 139). Das ist harmlos, zeigt aber: Wortzahlen der KI selbst nachprüfen.
7. **Kleinigkeiten:** Haiku verliert in Turn 3 die Betreffzeile. Sonnet verliert den Montage-Stillstand, Opus die „acht Jahre“. Sonnet nennt in Turn 2 die Frist Mittwoch nicht als Kritikpunkt, obwohl sie ein Kern der Kundenmail ist.

Kein Modell hat eine Zahl oder Nummer falsch wiedergegeben (4711-NT, 120, SG-40, KW 18, 60, 85 €, RE-2024-0815 stimmen überall, wo sie vorkommen). Kein Modell hat einen konkreten Termin, einen Rabatt in Prozent oder eine Gutschrift ausdrücklich zugesagt.

## Lehren für die Auswertung

- **Der Perspektivwechsel funktioniert zuverlässig.** Alle drei Modelle halten die 5 Stichpunkte ein und finden plausible Kritik. Die beiden wichtigsten Punkte kommen bei allen: „Wieder kein fester Termin“ und „Nachlass wird nur geprüft/weitergereicht“. Opus und Sonnet bemerken zusätzlich die fehlende Erklärung für den Verzug.
- **Die Kundensicht kritisiert die Platzhalter.** Alle Modelle bemängeln, dass „[DATUM]“ bzw. „wir prüfen“ wie eine Nullaussage wirkt. Der echte Kunde sieht die Platzhalter aber nie, denn dort stehen später echte Angaben. Das ist ein guter Diskussionspunkt: Welche Kritik betrifft den Entwurf und welche nur die noch fehlenden Informationen? Genau deshalb heißt es im Übungsblatt „die Hinweise, die du sinnvoll findest“.
- **Kernlehre: Kundenkritik drängt zu Zusagen.** Der „Kunde“ will Termin, Ansprechpartner und Entgegenkommen. Wer alle Hinweise blind übernimmt, bekommt neue Versprechen in den Text. Bei Sonnet passiert das trotz ausdrücklichem Verbot („Ich übernehme Ihren Fall persönlich“, „vereinbart war frei Haus“). Für das Plenum: Den überarbeiteten Entwurf noch einmal mit der Checkliste aus Aufgabe A prüfen, besonders mit der Frage „Hat er etwas zugesagt, das du gar nicht zusagen darfst?“
- **„Bis Mittwoch“ ist auch eine Zusage.** Sonnet schreibt „spätestens Mittwoch“ in den Text, Opus setzt nur [DATUM] und weist auf die Frist hin. Frage an die Gruppe: Könnt ihr bis Mittwoch wirklich einen verbindlichen Termin nennen? Wenn nicht: „Bis Mittwoch erhalten Sie den aktuellen Stand“.
- **Gutes Vorbild: Prüfhinweise.** Opus liefert ungefragt drei Hinweise, was vor dem Versand zu klären ist. Teilnehmende können das selbst einfordern: „Liste danach auf, welche Aussagen ich vor dem Versand intern klären muss.“
- **Wortzahlen nachprüfen.** Alle Entwürfe bleiben unter 150 Wörtern, die Selbstauskunft von Opus („rund 145“) stimmt aber nicht genau.
- **Zeit:** Drei kurze Turns, gut in 5 Minuten zu schaffen. Als „Für Schnelle“-Aufgabe passt das.

## Gesprächsprotokolle

### Haiku

#### Nutzer 1

```text
Ich arbeite im Vertrieb der Nordlicht Technik GmbH. Unten steht eine verärgerte Kundenmail wegen eines Lieferverzugs.

Schreibe mir einen Antwortentwurf, der:
- sich für die Verzögerung entschuldigt, ohne Schuld abzuwälzen,
- auf die konkreten Punkte des Kunden eingeht,
- einen nächsten Schritt anbietet (z. B. Rückruf oder neuer Liefertermin),
- höflich und sachlich ist und höchstens 150 Wörter hat.

Erfinde keine Fakten wie Liefertermine oder Rabatte. Wo mir Informationen fehlen, setze einen Platzhalter in eckigen Klammern, z. B. [NEUER LIEFERTERMIN].

Hier die Kundenmail:
Von: Markus Brenner, Brenner Gerätebau GmbH. Betreff: WIE LANGE NOCH??? Auftrag 4711-NT / Steuergehäuse. Im März wurden 120 Steuergehäuse SG-40 bestellt, zugesagt für KW 18, jetzt ist KW 21 und nichts ist angekommen. Zweimal wurde der Einkauf auf "nächste Woche" vertröstet, niemand hat sich gemeldet. Die Montage steht teilweise still. Gefordert werden ein verbindlicher, schriftlicher Liefertermin, notfalls eine Teillieferung von 60 Stück, mindestens 10 % Nachlass und die Prüfung der Frachtkosten von 85 Euro auf Rechnung RE-2024-0815 (frei Haus vereinbart). Antwort bis Mittwoch, sonst Wechsel des Lieferanten.
```

#### Assistent 1

Betreff: Ihr Auftrag 4711-NT / Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

vielen Dank für Ihre Nachricht. Es tut uns sehr leid, dass Sie bei Auftrag 4711-NT so lange ohne Information geblieben sind und Ihre Montage darunter leidet. Das hätte nicht passieren dürfen.

Ihren Wunsch nach einem verbindlichen Liefertermin nehmen wir ernst. Aktuell können wir Ihnen folgenden Stand nennen: [NEUER LIEFERTERMIN ODER TEILLIEFERUNG, MENGE UND TERMIN].

Zu Ihrer Bitte um einen Nachlass und zur Frachtkostenfrage auf Rechnung RE-2024-0815 prüfen wir die Sachlage und melden uns dazu.

Gerne rufe ich Sie am [RÜCKRUFTERMIN] an, um die nächsten Schritte direkt mit Ihnen abzustimmen. Eine Rückmeldung zu allen Punkten erhalten Sie bis [DATUM].

Mit freundlichen Grüßen
[NAME, FUNKTION, TELEFON]

#### Nutzer 2

```text
Stell dir vor, du bist der verärgerte Kunde aus der ursprünglichen Mail. Wie wirkt die Antwort auf dich? Was würde dich noch stören? Antworte in höchstens 5 Stichpunkten.
```

#### Assistent 2

- Die Entschuldigung ist allgemein gehalten. Ich will wissen, wer sich entschuldigt und was genau schiefgelaufen ist.
- Ein Platzhalter für den Liefertermin wirkt wie eine Nullaussage. Solange dort kein Datum steht, habe ich nichts Schriftliches.
- Die Teillieferung wird nur erwähnt, nicht angeboten. Ich will eine konkrete Menge und ein Datum.
- Nachlass und Frachtkosten werden nur "geprüft". Ohne Ergebnis oder Frist wirkt das ausweichend.
- Der Rückruf ist gut, aber ich brauche bis Mittwoch eine schriftliche Antwort, nicht nur ein Telefonat.

#### Nutzer 3

```text
Überarbeite die Antwort mit diesen Hinweisen. Bleib bei höchstens 150 Wörtern und mach weiterhin keine Zusagen, die ich nicht freigegeben habe.
```

#### Assistent 3

Sehr geehrter Herr Brenner,

vielen Dank für Ihre deutliche Rückmeldung. Dass Sie über Auftrag 4711-NT nicht informiert wurden und Ihre Montage darunter leidet, hätte nicht passieren dürfen. Dafür entschuldige ich mich ausdrücklich.

Eine schriftliche Auskunft mit dem Stand zu Ihrem Liefertermin erhalten Sie bis spätestens [DATUM, MITTWOCH]. Ob eine Teillieferung möglich ist, prüfen wir derzeit: [TEILLIEFERUNG JA/NEIN, MENGE, TERMIN].

Ihre Fragen zu einem Nachlass und zu den Frachtkosten auf Rechnung RE-2024-0815 prüfen wir gesondert und geben Ihnen dazu bis [DATUM] Bescheid.

Damit wir alles direkt klären, rufe ich Sie am [RÜCKRUFTERMIN] unter Ihrer Nummer an. Bis dahin ist [NAME] unter [TELEFON] erreichbar.

Mit freundlichen Grüßen
[NAME, FUNKTION]

---

Hinweis: Ich habe die Verifikation mit anderen Modellen (ultracdoe, Sonnet, Haiku oder Opus) nicht durchgeführt, da mir dafür kein Agent-Werkzeug zur Verfügung steht. Die Fristen in Assistent 3 (Mittwoch, Rückrufzeitpunkt, Teillieferung) sind Platzhalter, die vor dem Versand freigegeben werden müssen. Die Gesprächsvorlage stammt aus /home/daniel/tbc-ai-tutorials/07_Beispielmaterial/kundenmail_beschwerde.txt.

*(Anmerkung Testlauf: Dieser letzte Hinweis ist ein Artefakt der Testumgebung, nicht Teil der Chat-Antwort an Teilnehmende.)*

### Sonnet

#### Nutzer 1

```text
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
```

#### Assistent 1

**Betreff:** Auftrag 4711-NT / Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

vielen Dank für Ihre offene Nachricht. Es tut mir leid, dass Ihre 120 Steuergehäuse nicht wie zugesagt in KW 18 geliefert wurden und Sie darüber nicht aktiv von uns informiert wurden. Dass Ihre Montage deshalb teilweise stillsteht, nehme ich sehr ernst.

Zu Ihren Punkten:
- **Liefertermin:** Ich bestätige Ihnen schriftlich bis [DATUM/UHRZEIT, spätestens Mittwoch] einen verbindlichen Termin: [NEUER LIEFERTERMIN].
- **Teillieferung:** Eine Lieferung von 60 Stück prüfen wir; Ergebnis: [MÖGLICHKEIT/TERMIN TEILLIEFERUNG].
- **Nachlass:** Ihre Forderung gebe ich intern weiter und melde mich dazu mit [ERGEBNIS/NÄCHSTER SCHRITT].
- **Rechnung RE-2024-0815:** Wir prüfen die Frachtkosten von 85 Euro und melden uns mit [ERGEBNIS DER PRÜFUNG].

Gern rufe ich Sie vorab an: [RÜCKRUFZEIT], unter [IHRE DURCHWAHL].

Mit freundlichen Grüßen
[NAME], Vertrieb, Nordlicht Technik GmbH

#### Nutzer 2

```text
Stell dir vor, du bist der verärgerte Kunde aus der ursprünglichen Mail. Wie wirkt die Antwort auf dich? Was würde dich noch stören?
Antworte in höchstens 5 Stichpunkten.
```

#### Assistent 2

- Positiv: Die Entschuldigung klingt ehrlich, und alle meine Punkte werden einzeln aufgegriffen.
- Es fehlt die Erklärung: Warum kam es zur Verzögerung, und warum hat mich niemand informiert? Das lässt mich ratlos zurück.
- Zu viele Platzhalter und "wir prüfen": Ich will einen verbindlichen Termin, aber hier steht nur, dass er noch kommt.
- Beim Nachlass wirkt "gebe ich intern weiter" wie Abwimmeln, ohne Zeitrahmen oder Ansprechpartner.
- Es fehlt ein Zeichen, dass mein Anliegen Priorität hat, etwa eine feste Ansprechperson und die Wertschätzung nach acht Jahren Zusammenarbeit.

#### Nutzer 3

```text
Überarbeite die Antwort mit diesen Hinweisen. Bleib bei höchstens 150 Wörtern und mach weiterhin keine Zusagen, die ich nicht freigegeben habe.
```

#### Assistent 3

**Betreff:** Auftrag 4711-NT / Steuergehäuse SG-40 – verbindliche Rückmeldung

Sehr geehrter Herr Brenner,

nach acht Jahren guter Zusammenarbeit haben Sie zu Recht mehr erwartet. Es tut mir leid, dass Ihre 120 Steuergehäuse nicht in KW 18 geliefert wurden und Sie nicht von uns informiert wurden. Ich übernehme Ihren Fall persönlich.

Ursache der Verzögerung: [URSACHE, nur wenn freigegeben].

- **Liefertermin:** Schriftlich und verbindlich bis [DATUM/UHRZEIT, spätestens Mittwoch]: [NEUER LIEFERTERMIN].
- **Teillieferung (60 Stück):** [MÖGLICH JA/NEIN, TERMIN].
- **Nachlass:** Dazu erhalten Sie von mir bis [DATUM] eine Antwort; [ERGEBNIS, nur wenn freigegeben].
- **Rechnung RE-2024-0815:** Ich prüfe die Frachtkosten von 85 Euro (vereinbart war frei Haus) und melde mich bis [DATUM] mit [ERGEBNIS].

Ich rufe Sie gern am [TAG/UHRZEIT] unter [NUMMER] an. Ihr Ansprechpartner bleibe ich: [NAME, DURCHWAHL].

Mit freundlichen Grüßen
[NAME], Vertrieb, Nordlicht Technik GmbH

### Opus

#### Nutzer 1

```text
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
```

#### Assistent 1

Hier ist ein Entwurf für Ihre Antwort:

---

**Betreff:** AW: Auftrag 4711-NT / Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

vielen Dank für Ihre offenen Worte. Sie haben recht: Den zugesagten Liefertermin in KW 18 haben wir nicht eingehalten, und wir haben Sie nicht von uns aus informiert. Dafür entschuldige ich mich ausdrücklich, gerade nach acht Jahren guter Zusammenarbeit.

Zu Ihren Punkten:
- **Liefertermin:** Den verbindlichen Termin bestätige ich Ihnen schriftlich bis [DATUM]: [NEUER LIEFERTERMIN].
- **Teillieferung:** Wir prüfen eine Teillieferung von 60 Stück. [STATUS / MÖGLICHER TERMIN TEILLIEFERUNG]
- **Nachlass:** Ihre Anfrage habe ich an [ZUSTÄNDIGE PERSON] weitergegeben. Ich melde mich dazu bis [DATUM].
- **Rechnung RE-2024-0815:** Wir prüfen die Frachtkosten von 85 Euro und korrigieren die Rechnung, falls „frei Haus“ vereinbart war.

Gern rufe ich Sie am [TAG/UHRZEIT] an, damit wir alles direkt besprechen können.

Mit freundlichen Grüßen
[IHR NAME]
Vertrieb, Nordlicht Technik GmbH
[TELEFON]

---

Der Entwurf hat rund 120 Wörter. Liefertermin, Teillieferung und Nachlass habe ich bewusst offen gelassen, weil die Mail dazu keine Angaben enthält.

#### Nutzer 2

```text
Stell dir vor, du bist der verärgerte Kunde aus der ursprünglichen Mail.
Wie wirkt die Antwort auf dich? Was würde dich noch stören?
Antworte in höchstens 5 Stichpunkten.
```

#### Assistent 2

- **Die Entschuldigung kommt an.** Dass Sie den Fehler offen zugeben und auch die fehlende Information ansprechen, nimmt mir etwas Ärger. Trotzdem steht wieder kein Termin drin. „Bestätige ich bis [Datum]“ klingt für mich nach dem nächsten „nächste Woche“.
- **Es fehlt eine Erklärung.** Ich erfahre nicht, warum die Lieferung so spät ist. Deshalb kann ich nicht einschätzen, ob der neue Termin realistisch ist.
- **Mein Schaden kommt nicht vor.** Den Stillstand in der Montage und meinen Ärger mit dem eigenen Kunden erwähnen Sie mit keinem Wort. Ich fühle mich damit nicht ernst genommen.
- **Der Nachlass wird weitergereicht.** „Weitergegeben“ wirkt ausweichend. Ich möchte wissen, wer entscheidet und bis wann.
- **Ich will einen festen Ansprechpartner.** Ich brauche einen Namen und eine direkte Telefonnummer und will nicht wieder in der Warteschleife landen. Außerdem fehlt eine klare Aussage, dass meine Frist bis Mittwoch eingehalten wird.

#### Nutzer 3

```text
Überarbeite die Antwort mit diesen Hinweisen. Bleib bei höchstens 150 Wörtern und mach weiterhin keine Zusagen, die ich nicht freigegeben habe.
```

#### Assistent 3

Hier ist die überarbeitete Fassung:

---

**Betreff:** AW: Auftrag 4711-NT / Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

Sie haben recht: Den zugesagten Liefertermin in KW 18 haben wir nicht eingehalten, und wir haben Sie nicht von uns aus informiert. Ich bedauere sehr, dass Ihre Montage deshalb teilweise stillsteht und Sie gegenüber Ihrem eigenen Kunden in eine schwierige Lage geraten sind. Dafür entschuldige ich mich ausdrücklich.

Grund der Verzögerung: [KURZE, EHRLICHE ERKLÄRUNG].

Zu Ihren Punkten:
- **Liefertermin:** Den verbindlichen Termin erhalten Sie schriftlich bis [DATUM]: [NEUER LIEFERTERMIN].
- **Teillieferung von 60 Stück:** [MÖGLICH AB DATUM / STATUS].
- **Nachlass:** Über Ihre Anfrage entscheidet [NAME/FUNKTION]. Die Antwort erhalten Sie bis [DATUM].
- **Rechnung RE-2024-0815:** Wir prüfen die Frachtkosten von 85 Euro. War „frei Haus“ vereinbart, erhalten Sie eine korrigierte Rechnung.

Ihr direkter Ansprechpartner bin ich. Ich rufe Sie am [TAG, UHRZEIT] an. Sie erreichen mich auch direkt unter [DURCHWAHL].

Mit freundlichen Grüßen
[IHR NAME]
Vertrieb, Nordlicht Technik GmbH

---

Der Entwurf hat rund 145 Wörter. Bitte prüfen Sie vor dem Versand:
- Bei den Daten in [DATUM] sollten Sie die Frist des Kunden (Mittwoch) einhalten. Tragen Sie dort aber nur Daten ein, die Sie wirklich halten können.
- Übernehmen Sie die Rolle als fester Ansprechpartner nur, wenn das intern abgestimmt ist.
- Die Rechnungskorrektur sagen Sie nur unter der Bedingung zu, dass „frei Haus“ tatsächlich vereinbart war. Bitte klären Sie das vorher mit der Buchhaltung.

---

Zurück zum [Übungsblatt Übung 1](../06_Uebungen/Uebung_1_Texte_schreiben.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md) · [Kundenmail](../07_Beispielmaterial/kundenmail_beschwerde.txt)
