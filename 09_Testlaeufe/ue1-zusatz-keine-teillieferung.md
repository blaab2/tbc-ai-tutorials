# Testlauf: Übung 1 / Trainer-Zusatz – Antwort, falls Teillieferung nicht möglich

**Herkunft:** Zusatzaufgabe für Schnelle aus [Trainer-Loesungshinweise.md – Übung 1, „Zusatzaufgaben für Schnelle“](../06_Uebungen/Trainer-Loesungshinweise.md#zusatzaufgaben-für-schnelle): „Formuliere eine Antwort, falls wir die Teillieferung **nicht** leisten können.“ – Wie geht man mit schlechten Nachrichten um? Übungsblatt: [Uebung_1_Texte_schreiben.md](../06_Uebungen/Uebung_1_Texte_schreiben.md). Material: [kundenmail_beschwerde.txt](../07_Beispielmaterial/kundenmail_beschwerde.txt).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf:** Im selben Chat wie Aufgabe A: zuerst der Startprompt aus dem Übungsblatt mit der Kundenmail, danach als zweite Nachricht wörtlich der Zusatz-Satz aus den Lösungshinweisen (siehe Gesprächsprotokolle unten).

**Was eine gute Antwort enthalten muss:** klare, nicht beschönigende Absage der Teillieferung von 60 Stück; Entschuldigung ohne Schuldzuweisung; konkreter nächster Schritt (Rückruf, Termin-Platzhalter); weiterhin keine erfundenen Termine, Rabatte oder Gutschriften; Sie-Form; höchstens ca. 150 Wörter. Zusätzlich (aus Aufgabe A übernommen): die übrigen Anliegen des Kunden (Nachlass, Rechnung RE-2024-0815) sollten nicht verloren gehen, wenn die Mail die erste Antwort ersetzt.

---

## Bewertung

Wortzahlen per `python3` gezählt (Anrede bis Signatur, ohne Betreffzeile, ohne Einleitungssatz und Hinweise außerhalb der Mail).

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Wortzahl (mit / ohne Gruß+Signatur) | 150 / 141 – genau an der Grenze | 116 / 108 | 150 / 141 (Modell sagt „ca. 145“ – stimmt) |
| Sie-Form | ja | ja | ja |
| Absage der Teillieferung klar? | **weich:** „derzeit nicht zusichern“ – lässt offen, ob doch noch möglich | klar, aber Amtsdeutsch: „nicht darstellen“ | klar: „nicht vorziehen, weil [KURZE BEGRÜNDUNG]“ |
| Begründung vorgesehen | ja, Platzhalter (optional) | nein | ja, Platzhalter |
| Entschuldigung ohne Ausrede | ja, aber allgemein („die Verzögerung“, ohne KW 18) | ja, mit KW 18 und fehlender Information | ja, mit KW 18 und fehlender Information |
| Verständnis für Folgen beim Kunden | ja (eigener Kunde, Montage) | knapp („Zwischenlösung fehlt“) | ja (Montage, eigener Kunde) |
| Alternative angeboten | ja, Platzhalter [OPTIONEN] | nein, nur Gesamttermin | ja, optionaler Platzhalter (Expressversand o. Ä.) |
| Verbindlicher Termin Gesamtmenge | ja, „bis [DATUM]“ melden + [NEUER LIEFERTERMIN] | ja, Platzhalter, schriftlich bestätigt | ja, Platzhalter |
| Nachlass / Rechnung RE-2024-0815 weiter enthalten | **nein, beide fehlen** | ja (ohne Frist, ohne 85 €) | ja (mit 10 % als Kundenwunsch, 85 €, Frist [DATUM]) |
| Keine erfundenen Zusagen | ja | ja | ja |
| Nächster Schritt | Rückruf am [DATUM] um [UHRZEIT] + Telefon | Gesprächsangebot mit [TELEFONNUMMER / ZEITFENSTER] – passiv | Rückruf am [DATUM/UHRZEIT] |
| Frist „bis Mittwoch“ | nein | nein (in der ersten Antwort noch ja) | nein (nur im Hinweis der ersten Antwort) |
| Hinweise an den Nutzer | keine | keine | ja: Begründung + Alternative, vorher anrufen |
| Gesamturteil | brauchbar, Nacharbeit nötig | gut, etwas nüchtern | sehr gut |

---

## Gefundene Fehler mit Beleg

1. **Keine erfundenen Fakten.** Kein Modell nennt einen konkreten Liefertermin, Rabatt oder eine Gutschrift. Alle arbeiten mit Platzhaltern. Auch der Grund für die Absage wurde nicht erfunden: Haiku und Opus setzen [GRUND …] bzw. [KURZE BEGRÜNDUNG], Sonnet lässt den Grund weg. Die Platzhalter-Regel aus dem ersten Prompt wirkt also auch in der Folgenachricht.
2. **Haiku vergisst zwei Anliegen.** In der Absage-Variante fehlen der Nachlass (Kundenmail: „mindestens 10 % Nachlass“) und die Rechnung RE-2024-0815 („Frachtkosten von 85 Euro, obwohl wir damals frei Haus vereinbart hatten“) komplett. Wer diese Mail anstelle der ersten verschickt, lässt zwei Punkte des Kunden unbeantwortet. Das ist genau der Stolperstein „Rechnung vergessen“ aus den Lösungshinweisen. Er tritt hier in der Folgeaufgabe auf, nicht in Aufgabe A.
3. **Haiku formuliert die Absage beschönigend.** „derzeit nicht zusichern“ ist keine klare Absage: Der Kunde kann daraus lesen, dass es vielleicht doch klappt. Der Prompt wollte eine Antwort, *falls wir die Teillieferung nicht leisten können*.
4. **Haiku (erste Antwort) widerspricht sich.** „Eine Teillieferung von 60 Stück ist möglich: [TEILLIEFERUNG JA/NEIN, ggf. Termin]“ – der Satz sagt zuerst zu und lässt dann im Platzhalter offen, ob es überhaupt geht. Genau diese Unklarheit macht die Zusatzaufgabe nötig.
5. **Sonnet: „nicht darstellen“.** Sachlich richtig, aber kaufmännisches Amtsdeutsch. Für einen verärgerten Kunden wirkt das ausweichend. Außerdem fehlt jede Begründung und Alternative. Das ist kein Fehler, aber eine schwächere schlechte Nachricht.
6. **Sonnet: Frist „bis Mittwoch“ fällt weg.** In der ersten Antwort stand noch „Bis Mittwoch erhalten Sie von uns schriftlich einen verbindlichen Liefertermin“. In der Variante fehlt der Bezug auf die Frist des Kunden.
7. **Opus: Alternative mit leichtem Widerspruch.** Der optionale Platzhalter schlägt „VERSAND IN TEILMENGEN AB DATUM“ vor. Das ist inhaltlich eine spätere Teillieferung und passt nicht ganz zur Absage. Weil es als optionaler Platzhalter markiert ist und Opus im Hinweis „löschen Sie den optionalen Satz einfach“ schreibt, ist es unkritisch, aber ein guter Prüfpunkt.
8. **Wortangaben:** Opus sagt „ca. 145 Wörter“, gezählt sind 141 (ohne Gruß) bzw. 150 (mit Gruß). Die Angabe stimmt hier – anders als in Aufgabe A, wo die Selbstauskunft daneben lag. Haiku liegt mit 150 Wörtern (mit Gruß) genau an der Grenze.

---

## Lehren für die Auswertung

- **Die Übung funktioniert.** Alle drei Modelle liefern eine brauchbare Absage mit Platzhaltern. Es wird nichts erfunden. Der Lerneffekt liegt nicht bei „KI erfindet“, sondern beim **Ton der schlechten Nachricht**: Wie klar ist die Absage? Gibt es eine Begründung? Gibt es eine Alternative?
- **Drei Formulierungen nebeneinander zeigen:** „derzeit nicht zusichern“ (Haiku) – „nicht darstellen“ (Sonnet) – „nicht vorziehen, weil …“ (Opus). Frage an die Gruppe: Welche Version würde Herr Brenner als ehrlich empfinden? Welche klingt nach Ausrede?
- **Folgeaufgaben verlieren Inhalte.** Haiku hat sich ganz auf die Teillieferung konzentriert und Nachlass und Rechnung gestrichen. Lehre: Bei jeder neuen Variante erneut mit der Checkliste prüfen, ob alle Anliegen noch drin sind. Hilfreicher Nachschub-Prompt: „Behalte alle übrigen Punkte aus dem ersten Entwurf bei und ändere nur den Absatz zur Teillieferung.“
- **Schlechte Nachrichten nicht nur per Mail.** Opus empfiehlt von sich aus, vorher anzurufen. Das ist ein guter Diskussionspunkt: Die KI schreibt den Text, aber die Entscheidung über den Kanal trifft der Mensch.
- **Platzhalter für die Begründung ist wichtig.** Wenn kein Grund genannt wird (Sonnet), fragt der Kunde nach. Wenn ein Grund erfunden würde (z. B. „Materialengpass“), wäre das gefährlich. Gute Frage an die Gruppe: Was wäre passiert, wenn die KI selbst einen Grund geschrieben hätte?
- **Zeit:** Die Aufgabe ist in 3–5 Minuten machbar, passt also als Zusatz für Schnelle.

**Hinweis zum Material:** Der Zusatz-Satz in den Lösungshinweisen sagt nicht, ob die neue Mail die erste ersetzt oder ergänzt. Das erklärt, warum Haiku Nachlass und Rechnung weglässt. Ein Halbsatz wie „… und behalte die übrigen Punkte bei“ würde das klären – oder man nutzt die Unklarheit bewusst als Lernpunkt (siehe oben).

---

## Gesprächsprotokolle

### Haiku

#### Nutzer 1

Ich arbeite im Vertrieb der Nordlicht Technik GmbH. Unten steht eine verärgerte Kundenmail wegen eines Lieferverzugs.

Schreibe mir einen Antwortentwurf, der:
- sich für die Verzögerung entschuldigt, ohne Schuld abzuwälzen,
- auf die konkreten Punkte des Kunden eingeht,
- einen nächsten Schritt anbietet (z. B. Rückruf oder neuer Liefertermin),
- höflich und sachlich ist und höchstens 150 Wörter hat.

Erfinde keine Fakten wie Liefertermine oder Rabatte. Wo mir Informationen fehlen, setze einen Platzhalter in eckigen Klammern, z. B. [NEUER LIEFERTERMIN].

Hier die Kundenmail: [Inhalt der angehängten Datei kundenmail_beschwerde.txt, Von Markus Brenner, Auftrag 4711-NT / Steuergehäuse]

#### Assistent 1

Betreff: Ihr Auftrag 4711-NT, Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

vielen Dank für Ihre offenen Worte. Wir bedauern die Verzögerung sehr und dass Sie zweimal nur auf „nächste Woche“ vertröstet wurden, ohne eine verbindliche Auskunft zu erhalten. Das hätte nicht passieren dürfen.

Zu Ihren Punkten:
- **Liefertermin:** Den verbindlichen Liefertermin bestätigen wir Ihnen schriftlich: [NEUER LIEFERTERMIN].
- **Teillieferung:** Eine Teillieferung von 60 Stück ist möglich: [TEILLIEFERUNG JA/NEIN, ggf. Termin].
- **Frachtkosten zu RE-2024-0815:** Wir prüfen die Vereinbarung „frei Haus“ und korrigieren die Rechnung, falls zutreffend, bis [DATUM].
- **Nachlass:** Zu Ihrer Forderung melden wir uns mit einer Entscheidung bis [DATUM].

Als nächsten Schritt rufe ich Sie am [DATUM] um [UHRZEIT] an, um Termin und Teillieferung abzustimmen. Sie erreichen mich auch unter [TELEFON].

Mit freundlichen Grüßen

[IHR NAME]
Vertrieb, Nordlicht Technik GmbH

#### Nutzer 2

Formuliere eine Antwort, falls wir die Teillieferung nicht leisten können.

#### Assistent 2

Betreff: Ihr Auftrag 4711-NT, Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

vielen Dank für Ihre Nachricht und entschuldigen Sie bitte die Verzögerung. Ich verstehe, dass Sie Ihrem eigenen Kunden einen festen Termin zugesagt haben und dass der Stillstand in Ihrer Montage für Sie belastend ist.

Leider können wir Ihnen eine Teillieferung von 60 Stück derzeit nicht zusichern: [GRUND, z. B. Materialverfügbarkeit, nur wenn Sie ihn nennen möchten]. Wir wissen, dass Sie dadurch weiter planen müssen, und möchten Ihnen trotzdem so schnell wie möglich eine verlässliche Perspektive geben.

Dazu schlage ich vor:
- Wir melden Ihnen bis [DATUM] einen verbindlichen Liefertermin für die Gesamtmenge von 120 Stück: [NEUER LIEFERTERMIN].
- Falls Sie bis dahin Alternativen für die Montage brauchen, besprechen wir mit Ihnen gern, welche Optionen wir haben: [OPTIONEN, falls vorhanden].

Ich rufe Sie am [DATUM] um [UHRZEIT] an, um die Lage mit Ihnen durchzugehen. Alternativ erreichen Sie mich unter [TELEFON].

Mit freundlichen Grüßen

[IHR NAME]
Vertrieb, Nordlicht Technik GmbH

---

### Sonnet

#### Nutzer 1

Ich arbeite im Vertrieb der Nordlicht Technik GmbH. Unten steht eine verärgerte Kundenmail wegen eines Lieferverzugs.

Schreibe mir einen Antwortentwurf, der:
- sich für die Verzögerung entschuldigt, ohne Schuld abzuwälzen,
- auf die konkreten Punkte des Kunden eingeht,
- einen nächsten Schritt anbietet (z. B. Rückruf oder neuer Liefertermin),
- höflich und sachlich ist und höchstens 150 Wörter hat.

Erfinde keine Fakten wie Liefertermine oder Rabatte. Wo mir Informationen fehlen, setze einen Platzhalter in eckigen Klammern, z. B. [NEUER LIEFERTERMIN].

Hier die Kundenmail:
[Inhalt der Mail von Markus Brenner, Brenner Gerätebau GmbH: Auftrag 4711-NT, 120 Steuergehäuse SG-40, zugesagt KW 18, bis KW 21 nichts geliefert, keine Info, zweimal vertröstet; Montage steht teilweise still; gewünscht: verbindlicher schriftlicher Liefertermin, notfalls Teillieferung von 60 Stück; Forderung mindestens 10 % Nachlass; Rechnung RE-2024-0815 mit 85 Euro Fracht trotz vereinbarter Frei-Haus-Lieferung; Rückmeldung bis Mittwoch erwartet.]

#### Assistent 1

Betreff: Ihr Auftrag 4711-NT – Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

es tut uns leid, dass Ihre 120 Steuergehäuse SG-40 nicht wie zugesagt in KW 18 geliefert wurden. Dass Sie dazu weder von uns informiert wurden noch eine verbindliche Auskunft erhielten, hätte nicht passieren dürfen. Wir verstehen, dass Ihre Montage dadurch beeinträchtigt ist.

Bis Mittwoch erhalten Sie von uns schriftlich einen verbindlichen Liefertermin: [NEUER LIEFERTERMIN]. Eine Teillieferung von 60 Stück prüfen wir derzeit: [TERMIN TEILLIEFERUNG / MACHBARKEIT].

Ihre Rechnung RE-2024-0815 prüfen wir hinsichtlich der Frachtkosten von 85 Euro und korrigieren sie, sofern Frei-Haus vereinbart war: [ERGEBNIS PRÜFUNG].

Zu Ihrer Nachlassforderung melden wir uns gesondert: [STELLUNGNAHME NACHLASS].

Gern rufe ich Sie vorab an: [TELEFONNUMMER / ZEITFENSTER].

Mit freundlichen Grüßen
[NAME]
Vertrieb, Nordlicht Technik GmbH

#### Nutzer 2

Formuliere eine Antwort, falls wir die Teillieferung nicht leisten können.

#### Assistent 2

Hier eine Variante für den Fall, dass die Teillieferung nicht möglich ist:

Betreff: Ihr Auftrag 4711-NT – Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

es tut uns leid, dass Ihre 120 Steuergehäuse SG-40 nicht wie zugesagt in KW 18 bei Ihnen eingetroffen sind. Dass Sie dazu keine rechtzeitige Information von uns erhielten, hätte nicht passieren dürfen.

Eine Teillieferung von 60 Stück können wir leider nicht darstellen. Wir wissen, dass Ihnen damit eine Zwischenlösung fehlt, und bedauern das. Die Gesamtlieferung der 120 Stück sagen wir Ihnen verbindlich für [NEUER LIEFERTERMIN] zu und bestätigen dies schriftlich.

Die Frachtkosten auf Rechnung RE-2024-0815 prüfen wir und melden uns dazu: [ERGEBNIS PRÜFUNG].

Zu Ihrem Wunsch nach einem Nachlass nimmt [NAME/ABTEILUNG] Stellung: [STELLUNGNAHME NACHLASS].

Gern erläutere ich Ihnen die Situation persönlich: [TELEFONNUMMER / ZEITFENSTER].

Mit freundlichen Grüßen
[NAME]
Vertrieb, Nordlicht Technik GmbH

---

### Opus

#### Nutzer 1

Ich arbeite im Vertrieb der Nordlicht Technik GmbH. Unten steht eine verärgerte Kundenmail wegen eines Lieferverzugs.

Schreibe mir einen Antwortentwurf, der:
- sich für die Verzögerung entschuldigt, ohne Schuld abzuwälzen,
- auf die konkreten Punkte des Kunden eingeht,
- einen nächsten Schritt anbietet (z. B. Rückruf oder neuer Liefertermin),
- höflich und sachlich ist und höchstens 150 Wörter hat.

Erfinde keine Fakten wie Liefertermine oder Rabatte. Wo mir Informationen fehlen, setze einen Platzhalter in eckigen Klammern, z. B. [NEUER LIEFERTERMIN].

Hier die Kundenmail:
[Anhang: kundenmail_beschwerde.txt – Mail von Markus Brenner, Brenner Gerätebau GmbH, Betreff „WIE LANGE NOCH??? Auftrag 4711-NT / Steuergehäuse“]

#### Assistent 1

Hier ist ein Entwurf (ca. 130 Wörter):

---

**Betreff:** Ihr Auftrag 4711-NT – Lieferverzug Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

es tut mir sehr leid, dass die 120 Steuergehäuse SG-40 nicht wie zugesagt in KW 18 bei Ihnen angekommen sind. Ebenso leid tut es mir, dass Sie von uns keine verlässliche Information bekommen haben. Mir ist bewusst, dass Ihre Montage dadurch teilweise stillsteht und Sie gegenüber Ihrem eigenen Kunden in eine schwierige Lage geraten sind.

Ihren verbindlichen Liefertermin bestätige ich Ihnen hiermit schriftlich: [NEUER LIEFERTERMIN]. Eine Teillieferung von 60 Stück ist [MÖGLICH BIS DATUM / NICHT MÖGLICH].

Ihren Wunsch nach einem Nachlass von 10 % habe ich an [ZUSTÄNDIGE STELLE] weitergegeben. Sie erhalten dazu bis [DATUM] eine Antwort.

Die Frachtkosten von 85 Euro auf der Rechnung RE-2024-0815 prüfen wir und melden uns wegen der Korrektur bei Ihnen.

Gern rufe ich Sie am [DATUM/UHRZEIT] an, um alles persönlich mit Ihnen zu besprechen.

Mit freundlichen Grüßen
[NAME]
[FUNKTION]
Nordlicht Technik GmbH
[TELEFON]

---

**Hinweise:**
- Herr Brenner erwartet bis **Mittwoch** eine Antwort. Am besten schicken Sie die Mail vorher ab, auch wenn noch nicht jeder Punkt geklärt ist.
- Zum Rabatt habe ich bewusst nichts zugesagt. Das sollte mit der zuständigen Stelle abgestimmt werden.
- Bitte setzen Sie den Liefertermin erst ein, wenn er intern wirklich bestätigt ist. Der Kunde hat ausdrücklich kein „voraussichtlich“ mehr akzeptiert.

#### Nutzer 2

Formuliere eine Antwort, falls wir die Teillieferung nicht leisten können.

#### Assistent 2

Hier ist die Variante für den Fall, dass keine Teillieferung möglich ist (ca. 145 Wörter):

---

**Betreff:** Ihr Auftrag 4711-NT – Lieferverzug Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

es tut mir sehr leid, dass die 120 Steuergehäuse SG-40 nicht wie zugesagt in KW 18 bei Ihnen angekommen sind und dass Sie in dieser Zeit keine verlässliche Information von uns bekommen haben. Mir ist bewusst, welche Folgen das für Ihre Montage und für Ihren eigenen Kunden hat.

Leider können wir Ihnen die gewünschte Teillieferung von 60 Stück nicht vorziehen, weil [KURZE BEGRÜNDUNG]. Die vollständige Lieferung bestätige ich Ihnen verbindlich für den [NEUER LIEFERTERMIN]. [OPTIONAL: ALTERNATIVE, Z. B. EXPRESSVERSAND ODER VERSAND IN TEILMENGEN AB DATUM].

Ihren Wunsch nach einem Nachlass von 10 % habe ich an [ZUSTÄNDIGE STELLE] weitergegeben. Sie erhalten dazu bis [DATUM] eine Antwort. Die Frachtkosten von 85 Euro auf der Rechnung RE-2024-0815 prüfen wir und melden uns wegen der Korrektur.

Gern rufe ich Sie am [DATUM/UHRZEIT] an, um gemeinsam nach einer Lösung zu suchen.

Mit freundlichen Grüßen
[NAME]
[FUNKTION]
Nordlicht Technik GmbH
[TELEFON]

---

**Hinweise:**
- Eine Absage trifft den Kunden härter. Deshalb lohnt sich hier eine kurze, ehrliche Begründung, und wenn es eine gibt, eine Alternative. Wenn Sie keine Alternative anbieten können, löschen Sie den optionalen Satz einfach.
- Bei dieser Nachricht wäre es gut, zusätzlich vorher kurz anzurufen. Dann erfährt Herr Brenner die Absage nicht nur per Mail.
