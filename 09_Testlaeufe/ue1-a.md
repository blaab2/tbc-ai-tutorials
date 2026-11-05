# Testlauf: Übung 1 / Basis A – Antwort auf die Beschwerde entwerfen

**Herkunft:** Aufgabe A aus [Uebung_1_Texte_schreiben.md](../06_Uebungen/Uebung_1_Texte_schreiben.md#aufgabe-a--antwort-auf-die-beschwerde-entwerfen-lassen) (Block 3). Material: [kundenmail_beschwerde.txt](../07_Beispielmaterial/kundenmail_beschwerde.txt). Zugehörige Lösungshinweise: [Trainer-Loesungshinweise.md – Übung 1](../06_Uebungen/Trainer-Loesungshinweise.md#übung-1-texte-schreiben).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt:** Startprompt aus dem Übungsblatt, darunter der vollständige Text der Kundenmail (siehe Gesprächsprotokolle unten).

**Was eine gute Antwort enthalten muss (laut Lösungshinweisen):** alle fünf Anliegen (1. Verzug KW 18 → KW 21 ohne Information, 2. verbindlicher schriftlicher Termin, 3. Teillieferung 60 Stück, 4. mindestens 10 % Nachlass, 5. Frachtkosten 85 € auf RE-2024-0815), Entschuldigung ohne Ausreden, keine erfundenen Zusagen (Platzhalter statt Termin/Rabatt/Gutschrift), konkreter nächster Schritt, höchstens ca. 150 Wörter, Sie-Form, Auftragsnummer 4711-NT.

---

## Bewertung

Wortzahlen per `python3` gezählt (Anrede bis Signatur, ohne Betreffzeile und ohne die Hinweise außerhalb der Mail).

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Wortzahl (mit / ohne Gruß+Signatur) | 150 / 142 – genau an der Grenze | 119 / 111 (Modell behauptet „ca. 145“) | 136 / 126 (Modell behauptet „etwa 130“) |
| Sie-Form | ja | ja | ja |
| Auftragsnummer 4711-NT genannt | nur im Betreff | nur im Betreff | nur im Betreff |
| 1. Verzug KW 18 / keine Info | ja, aber ohne KW 18; holprig formuliert | ja, mit KW 18 und „keine verlässliche Auskunft“ | ja, mit KW 18 und „keine verlässliche Auskunft“ |
| 2. verbindlicher schriftlicher Termin | ja (Platzhalter) | ja (Platzhalter, bis Mittwoch) | ja (Platzhalter) |
| 3. Teillieferung 60 Stk. | ja (Platzhalter) | ja (Platzhalter) | ja (Platzhalter, inkl. „nicht möglich“) |
| 4. Nachlass | ja, ohne %, Rückmeldung bis [DATUM] | ja, ohne %, aber **ohne Frist** | ja, ohne %, Antwort bis [DATUM] |
| 5. RE-2024-0815 / Fracht 85 € | ja, Betrag fehlt; **bedingte Korrekturzusage** | ja, Betrag fehlt | ja, mit 85 Euro |
| Keine erfundenen Zusagen | weitgehend (bedingte Korrektur, „Geschäftsleitung“ angenommen) | ja | ja (aber „liefern wir verbindlich am [..]“ wirkt wie fertige Zusage) |
| Nächster Schritt | Rückruf, Satz grammatisch kaputt | Rückruf vorab + Termin bis Mittwoch | Rückruf am [DATUM/UHRZEIT] |
| Frist „bis Mittwoch“ aufgegriffen | nein | ja | nur im Hinweis an den Nutzer |
| Nicht zu unterwürfig | ja | ja | ja |
| 8 Jahre Zusammenarbeit gewürdigt | nein | nein | nein (nur als Hinweis vorgeschlagen) |
| Hinweise für den Nutzer vor dem Versand | keine | kurz, gut | ausführlich, sehr gut |
| Gesamturteil | brauchbar, Nacharbeit nötig | gut | sehr gut |

---

## Gefundene Fehler mit Beleg

1. **Kein Modell hat Fakten erfunden.** Kein konkreter Liefertermin, kein Rabatt in Prozent, keine Gutschrift. Der in den Lösungshinweisen als „wichtigste Lernchance“ beschriebene Stolperstein („Die Lieferung erfolgt am 24.05.“ / „5 %“) trat **in keinem Lauf auf**. Der Prompt mit dem ausdrücklichen Platzhalter-Gebot wirkt.
2. **Rechnung RE-2024-0815 vergessen? Nein.** Alle drei sprechen die Rechnung an. Der Stolperstein „Rechnung vergessen“ trat ebenfalls nicht auf. Nur Opus nennt auch den Betrag 85 Euro.
3. **Haiku – bedingte Zusage zur Rechnungskorrektur:** „… prüfen wir parallel und korrigieren sie, falls die frei-Haus-Vereinbarung zutrifft.“ Das ist keine harte Zusage, legt die Firma aber schon fest. Die Checkliste im Übungsblatt fragt genau danach („… oder die Korrektur der Rechnung?“). Guter Diskussionsfall.
4. **Haiku – kleine Annahme:** „prüfen wir Ihr Anliegen mit unserer Geschäftsleitung“ – wer über den Nachlass entscheidet, steht nirgends. Harmlos, aber eine Annahme. (Opus löst das mit dem Platzhalter [ZUSTÄNDIGE PERSON].)
5. **Haiku – Logik und Sprache:** „melden uns bis [DATUM] mit einem verbindlichen Termin: [NEUER LIEFERTERMIN]“ – zwei Platzhalter in einem Satz: entweder man nennt den Termin jetzt oder später. Außerdem ist der Satz „Wann passt es Ihnen, [ZEITFENSTER], oder erreichen Sie mich unter [TELEFONNUMMER].“ grammatisch kaputt (Frage ohne Fragezeichen, zwei Satzteile vermischt). „frei-Haus-Vereinbarung“ müsste „Frei-Haus-Vereinbarung“ heißen. Die KW-Angaben fehlen ganz.
6. **Haiku – Wortlimit ausgereizt:** Genau 150 Wörter mit Signatur. Formal erfüllt, aber ohne Puffer.
7. **Sonnet – Wortzahl falsch angegeben:** Das Modell schreibt „ca. 145 Wörter“, tatsächlich sind es 119 (mit Gruß und Signatur, per `python3` gezählt). Das schadet hier nicht, zeigt aber: **Selbstauskünfte zur Länge stimmen oft nicht.** Opus liegt mit „etwa 130“ (tatsächlich 126 ohne / 136 mit Signatur) nah dran.
8. **Sonnet – Nachlass ohne Frist:** „… gebe Ihnen eine Rückmeldung: [ERGEBNIS / VORGEHEN]“ – hier fehlt ein „bis [DATUM]“. Der Satz „Ich sage Ihnen bis Mittwoch, [TT.MM., UHRZEIT], schriftlich zu: [VERBINDLICHER LIEFERTERMIN]“ ist holprig. Er verspricht außerdem, dass es bis Mittwoch einen verbindlichen Termin gibt. Das kann der Vertrieb vielleicht gar nicht zusagen.
9. **Opus – leichte Übertreibung:** „… und Ihre Montage steht.“ Laut Mail steht die Montage „**teilweise** still“. Kleine Verschärfung, die man vor dem Versand korrigieren sollte.
10. **Opus – Formulierung „liefern wir verbindlich am [NEUER LIEFERTERMIN]“:** Mit Platzhalter ist das korrekt. Wer den Platzhalter aber vorschnell mit einem „Wunschtermin“ füllt, hat damit eine verbindliche Zusage gemacht. Opus warnt davor selbst in den Hinweisen („Tragen Sie nur einen Liefertermin ein, den Produktion oder Logistik wirklich zusagen kann“).
11. **Alle drei:** Die Auftragsnummer 4711-NT steht nur im Betreff, nicht im Text. Laut Lösungshinweisen reicht „Auftragsnummer genannt“. Das ist erfüllt, solange der Betreff mitgeschickt wird. Die acht Jahre Zusammenarbeit würdigt kein Entwurf im Text. Nur Opus schlägt das als Ergänzung vor.

---

## Lehren für die Auswertung

- **Der Prompt ist gut – und das ist die eigentliche Lehre.** Mit „Erfinde keine Fakten … setze einen Platzhalter“ haben alle drei Modelle sauber gearbeitet. Im Plenum zeigen: *Weil* wir das ausdrücklich verlangt haben, kommen keine erfundenen Termine. Zum Vergleich kann der Trainer live denselben Prompt **ohne** den Platzhalter-Absatz laufen lassen. Dann tauchen erfundene Termine oder Entschädigungen eher auf (vorher selbst testen).
- **Erwartung an die Teilnehmenden anpassen:** Viele werden „nichts gefunden“ melden. Dann gezielt auf die feineren Punkte lenken:
  - Was ist mit **bedingten Zusagen** („korrigieren, falls …“)?
  - Ist der Entwurf **zu stark** formuliert („Ihre Montage steht“, „verbindlich am …“)?
  - Fehlen **Fristen** („Rückmeldung: [ERGEBNIS]“ ohne Datum)?
  - Wurde die **Mittwoch-Frist** aufgegriffen?
- **Platzhalter sind Arbeitsaufträge.** Die Entwürfe enthalten 5–7 Platzhalter. Der Text ist erst versandfertig, wenn intern geklärt ist: Termin Gesamt- und Teillieferung, Nachlass, Rechnung, Rückrufzeit. Gute Brücke zu Aufgabe G (interne Kurznachricht an die Logistik).
- **Wortzahl nachzählen lassen:** Sonnet behauptet 145 Wörter, es sind 119. Kleine, harmlose Demo dafür, dass Selbstauskünfte des Modells (Länge, „ich habe alles berücksichtigt“) nicht verlässlich sind.
- **Modellunterschiede zeigen sich bei den Zusatzhinweisen:** Opus liefert ungefragt eine Checkliste für den Versand (Frist Mittwoch, Termin nur nach Rücksprache, Nachlass intern klären, acht Jahre erwähnen). Haiku liefert gar keine. Teilnehmende mit einfacherem Tool sollten diese Prüfung selbst machen. Dafür ist die Checkliste im Übungsblatt da.
- **Plus-Punkt zum Nacharbeiten:** Kein Entwurf würdigt die acht Jahre Zusammenarbeit. Das ist ein guter Anlass für Aufgabe B („wärmer und persönlicher“) oder einen eigenen Nachsatz-Prompt.
- **Zeit:** Prompt kopieren, Mail einfügen, Antwort lesen und Checkliste abhaken dauert realistisch 5–7 Minuten. Das passt in die Richtzeit „Basis A+B ca. 10 Min.“, wird aber knapp, wenn jemand die Mail abtippt statt kopiert.

---

## Probleme im Material und Vorschläge

- **Stolpersteine in den Lösungshinweisen sind zu pessimistisch.** In [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md#typische-stolpersteine) heißt es: „Erfundene Fakten … Das ist die wichtigste Lernchance der Übung“ und „Rechnung vergessen: Das Nebenthema RE-2024-0815 fällt in vielen Entwürfen unter den Tisch.“ Beides trat in keinem der drei Läufe auf. Vorschlag für eine Ergänzung unter „Typische Stolpersteine“:
  > „Hinweis: Mit dem Platzhalter-Satz im Startprompt erfinden aktuelle Modelle meist nichts und vergessen auch die Rechnung selten. Dann lohnt der Blick auf feinere Fehler: bedingte Zusagen („korrigieren wir, falls …“), Übertreibungen („Ihre Montage steht“ statt „teilweise“), fehlende Fristen bei einzelnen Punkten, nicht aufgegriffene Mittwoch-Frist. Wer den Klassiker ‚erfundener Termin‘ zeigen will, lässt den Prompt einmal ohne den Absatz ‚Erfinde keine Fakten …‘ laufen.“
- **Checkliste im Übungsblatt ergänzen:** In [Uebung_1_Texte_schreiben.md](../06_Uebungen/Uebung_1_Texte_schreiben.md#aufgabe-a--antwort-auf-die-beschwerde-entwerfen-lassen) unter „Prüfe den Entwurf kritisch“ einen Punkt ergänzen:
  `- [ ] Stimmt jede Aussage mit der Kundenmail überein – nicht übertrieben, nicht verharmlost? Hat jeder offene Punkt eine Frist?`
- **Kriterium „Auftragsnummer genannt“ präzisieren:** Alle Modelle setzen sie nur in den Betreff. Vorschlag in den Lösungshinweisen: „Auftragsnummer genannt (Betreff genügt)“. Sonst diskutieren Teilnehmende, ob das Kriterium erfüllt ist.
- Sonst ist die Aufgabe verständlich, der Prompt funktioniert mit allen drei Modellen, und die Zeit passt.

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

Hier die Kundenmail:

```text
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

**Betreff: Auftrag 4711-NT / Steuergehäuse SG-40**

Sehr geehrter Herr Brenner,

vielen Dank für Ihre Nachricht. Bitte entschuldigen Sie die Verzögerung bei der Lieferung der 120 Steuergehäuse SG-40 und dass Sie nicht rechtzeitig und nicht von uns aktiv informiert wurden. Dass Ihre Montage dadurch teilweise stillsteht, nehmen wir sehr ernst.

Ihren Wunsch nach einem verbindlichen, schriftlichen Liefertermin verstehen wir gut. Wir klären den aktuellen Stand umgehend intern und melden uns bis [DATUM] mit einem verbindlichen Termin: [NEUER LIEFERTERMIN]. Gern prüfen wir auch eine Teillieferung von 60 Stück mit dem Termin [TERMIN TEILLIEFERUNG].

Zu Ihrer Forderung nach einem Nachlass prüfen wir Ihr Anliegen mit unserer Geschäftsleitung und melden uns dazu bis [DATUM]. Die Frachtkosten auf Rechnung RE-2024-0815 prüfen wir parallel und korrigieren sie, falls die frei-Haus-Vereinbarung zutrifft.

Ich rufe Sie gern an, um die nächsten Schritte direkt zu besprechen. Wann passt es Ihnen, [ZEITFENSTER], oder erreichen Sie mich unter [TELEFONNUMMER].

Mit freundlichen Grüßen

[NAME]
[FUNKTION]
Nordlicht Technik GmbH

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

```text
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

Hier ist ein Entwurf (ca. 145 Wörter):

**Betreff:** Auftrag 4711-NT / Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

es tut mir leid, dass Ihre 120 Steuergehäuse SG-40 nicht wie zugesagt in KW 18 geliefert wurden und Sie dazu weder von uns informiert wurden noch eine verlässliche Auskunft erhielten. Die Folgen für Ihre Montage und Ihren Termin beim eigenen Kunden nehme ich sehr ernst.

Ich sage Ihnen bis Mittwoch, [TT.MM., UHRZEIT], schriftlich zu: [VERBINDLICHER LIEFERTERMIN]. Ihre Teillieferung von 60 Stück prüfen wir gern: [TERMIN TEILLIEFERUNG, falls möglich].

Ihre Frachtkosten-Anmerkung zur Rechnung RE-2024-0815 prüfen wir und melden uns dazu bis [DATUM].

Über Ihren Wunsch nach einem Nachlass spreche ich intern und gebe Ihnen eine Rückmeldung: [ERGEBNIS / VORGEHEN].

Gern rufe ich Sie vorab an: [RÜCKRUFZEIT / TELEFONNUMMER].

Mit freundlichen Grüßen
[NAME]
Vertrieb, Nordlicht Technik GmbH

Hinweise für Sie: Vor dem Versand bitte intern klären, ob und wann Gesamt- oder Teillieferung möglich ist und ob ein Entgegenkommen in Frage kommt. Nichts davon ist im Entwurf zugesagt.

---

### Opus

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
[INHALT VON /home/daniel/tbc-ai-tutorials/07_Beispielmaterial/kundenmail_beschwerde.txt]

*(Anmerkung zum Protokoll: An dieser Stelle stand im Testlauf der vollständige Inhalt der Datei [kundenmail_beschwerde.txt](../07_Beispielmaterial/kundenmail_beschwerde.txt) – derselbe Text wie bei Haiku und Sonnet oben.)*

#### Assistent 1

Gern, hier ist ein Antwortentwurf:

---

**Betreff:** AW: Auftrag 4711-NT / Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

vielen Dank für Ihre offenen Worte. Sie haben recht: Den zugesagten Liefertermin in KW 18 haben wir nicht eingehalten. Dass Sie von uns weder informiert wurden noch eine verlässliche Auskunft bekommen haben, tut mir aufrichtig leid. Mir ist bewusst, dass Sie dadurch gegenüber Ihrem Kunden in eine schwierige Lage geraten sind und Ihre Montage steht.

Zu Ihren Punkten:
- **Liefertermin:** Die 120 Gehäuse liefern wir verbindlich am [NEUER LIEFERTERMIN]. Eine Teillieferung von 60 Stück ist [MÖGLICH AM DATUM / NICHT MÖGLICH].
- **Nachlass:** Ihren Wunsch habe ich an [ZUSTÄNDIGE PERSON] weitergegeben. Sie erhalten bis [DATUM] eine Antwort.
- **Rechnung RE-2024-0815:** Wir prüfen die berechneten Frachtkosten von 85 Euro und melden uns bis [DATUM].

Gern rufe ich Sie am [DATUM/UHRZEIT] an, um alles persönlich zu besprechen.

Mit freundlichen Grüßen
[IHR NAME]
[FUNKTION], Nordlicht Technik GmbH
[TELEFON]

---

Der Entwurf hat etwa 130 Wörter. Ein paar Hinweise, bevor Sie ihn senden:
- **Frist:** Herr Brenner will bis Mittwoch eine Antwort. Senden Sie die Mail möglichst vorher, auch wenn noch nicht alle Punkte geklärt sind.
- **Termin:** Tragen Sie nur einen Liefertermin ein, den Produktion oder Logistik wirklich zusagen kann. Er verlangt ausdrücklich etwas Verbindliches und kein „voraussichtlich“.
- **Nachlass:** Ich habe bewusst nichts zugesagt. Ob es einen Nachlass gibt und wie hoch, sollte vorher intern entschieden werden.
- **Langjähriger Kunde:** Sie können noch einen Satz zu den acht Jahren Zusammenarbeit ergänzen, solange die Mail unter 150 Wörtern bleibt.
