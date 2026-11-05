# Testlauf: Übung 1 / Für Schnelle G – Interne Kurznachricht an die Logistik

**Herkunft:** [Uebung_1_Texte_schreiben.md, Stufe 3 „Für Schnelle“, Aufgabe G](../06_Uebungen/Uebung_1_Texte_schreiben.md) · Material: [kundenmail_beschwerde.txt](../07_Beispielmaterial/kundenmail_beschwerde.txt) · Abgleich mit [Trainer-Lösungshinweise, Übung 1](../06_Uebungen/Trainer-Loesungshinweise.md)

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf:** Im selben Chat zuerst der Startprompt aus Aufgabe A (Antwortentwurf an den Kunden), danach der Prompt aus Aufgabe G:

```text
Fasse den Fall für meine Kollegin aus der Logistik in 3 Sätzen zusammen:
Was ist passiert, was haben wir dem Kunden geantwortet, was muss sie
jetzt klären? Lockerer Ton, wir duzen uns.
```

**Ziel laut Material:** Interne Kurznachricht in genau 3 Sätzen, per du, mit Sachstand, Antwortinhalt und konkretem Klärungsauftrag an die Logistik.

**Soll laut Quelle:** Auftrag 4711-NT, 120 Steuergehäuse SG-40, zugesagt KW 18, jetzt KW 21, nichts angekommen, keine Info, zweimal vertröstet, Montage *teilweise* still. Was geantwortet wurde, muss dem Entwurf aus Aufgabe A entsprechen (keine nachträglich erfundenen Zusagen). Klärungsauftrag an die Logistik: verbindlicher Liefertermin, ob Teillieferung 60 Stück möglich, Frist Mittwoch (Kundenfrist). Kein erfundener Liefertermin.

**Hinweis zum Testaufbau:** Die Kundenmail wurde den Modellen unterschiedlich übergeben (Haiku und Sonnet: zusammengefasster Inhalt, Opus: Platzhalter auf die Datei). Haikus Eingabe enthielt „Montage steht still“ ohne „teilweise“ – die Formulierung in Haikus Antwort stammt also aus der Eingabe, nicht aus einer Halluzination. In der Übung kopieren Teilnehmende die vollständige Mail.

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Genau 3 Sätze | ja (36/37/26 Wörter) | ja (39/39/24) | ja (40/32/38) |
| Du-Form, lockerer Ton | ja („Hey“, „Du musst“) | ja („Hey“, „Kannst du bitte“) | ja („Hi“, „Kannst du bitte“) |
| 4711-NT / 120 SG-40 | ja | ja | ja |
| KW 18 zugesagt, jetzt KW 21 | ja | ja | ja |
| Montage *teilweise* still | „steht still“ (aus verkürzter Eingabe) | ja | ja |
| Antwortinhalt deckt sich mit Entwurf A | ja, Platzhalter [DATUM] übernommen | ja (Entwurf A hatte schon „bis Mittwoch“ zugesagt) | weitgehend; aber „falsch berechnete Fracht“ statt „prüfen“, Teillieferung im Antwortteil nicht erwähnt |
| Klärungsauftrag: verbindlicher Liefertermin | ja („realistisch“) | ja („realistisch“) | ja („ganz sicher halten“) |
| Klärungsauftrag: Teillieferung 60 Stk. | ja | ja („ob 60 Stück vorab gehen“) | ja |
| Frist Mittwoch | ja („bis Mittwoch klären“) | indirekt („schnellstmöglich … damit wir bis Mittwoch zusagen können“) | ja, plus interne Frist „bis morgen“ |
| Kein erfundener Liefertermin | ja | ja | ja |
| Klärungsauftrag passt zur Logistik | teils – Frachtprüfung RE-2024-0815 eher Buchhaltung/Vertrieb | ja, nur Logistik-Themen | ja, nur Logistik-Themen |
| Länge gesamt (Wörter) | 99 | 102 | 110 |
| **Gesamt** | gut, aber Frist zu knapp gesetzt und Fracht an die falsche Stelle | **sehr gut**, sauberste Trennung | sehr gut, praxisnah; kleine Vorverurteilung bei der Fracht |

Satz- und Wortzahlen per Python (`re.split` an `.?!`, `len(text.split())`) nachgezählt.

## Gefundene Fehler mit Beleg

Keine harten Fehler (keine falschen Zahlen, kein erfundener Liefertermin, keine erfundene Rabattzusage). Kleinere Ungenauigkeiten:

1. **Opus – Fracht als „falsch berechnet“ vorverurteilt:** „die Prüfung einer falsch berechneten Fracht (85 Euro auf RE-2024-0815)“. Die Quelle sagt nur: „stehen Frachtkosten von 85 Euro, obwohl wir damals frei Haus vereinbart hatten. Können Sie das bitte prüfen“. Opus' eigener Entwurf schrieb korrekt „prüfen … und korrigieren sie gegebenenfalls“. Die interne Notiz übernimmt also die Sicht des Kunden als Tatsache.
2. **Opus – zusätzliche interne Frist „bis morgen“:** Steht in keiner Quelle. Sachlich sinnvoll (Puffer vor der Kundenfrist), aber eine eigenmächtige Ergänzung – Teilnehmende sollten prüfen, ob sie das so wollen.
3. **Haiku – Frist „bis Mittwoch klären“:** Mittwoch ist die Frist für die Antwort an den Kunden („Ich erwarte bis spätestens Mittwoch eine Rückmeldung“). Wenn die Logistik erst Mittwoch liefert, ist es für die Kundenantwort zu spät. Sonnet und Opus lösen das besser.
4. **Haiku – Frachtprüfung an die Logistik:** Die 85 € auf RE-2024-0815 betreffen eine frühere Ersatzteilrechnung („das war die Ersatzteillieferung“) und gehören eher zu Buchhaltung/Vertrieb. Nicht falsch, aber der Klärungsauftrag wird unschärfer.
5. **Alle – Entwurf als „geantwortet“ dargestellt:** Haiku „Wir haben ihm … geantwortet“, Opus „Ich habe mich bei ihm entschuldigt“, Sonnet etwas vorsichtiger „im Antwortentwurf“. Der Entwurf aus Aufgabe A ist aber noch nicht verschickt. Das folgt aus dem Prompt („was haben wir dem Kunden geantwortet“), ist also kein Modellfehler – aber ein Punkt zum Prüfen vor dem Versand.
6. **Sonnet – übernommene Zusage aus Entwurf A:** „zugesagt, bis Mittwoch einen verbindlichen Liefertermin schriftlich zu nennen“ ist konsistent mit dem eigenen Entwurf, aber genau diese Termin-Zusage gegenüber dem Kunden ist heikel, solange die Logistik nichts bestätigt hat. Die interne Notiz macht das sichtbar – gut für die Diskussion.

## Lehren für die Auswertung

- **Die Übung funktioniert wie gedacht:** Alle drei Modelle halten genau 3 Sätze, duzen, nennen alle Kerndaten und erfinden keinen Termin. Gutes Erfolgserlebnis für Schnelle – und ein Beleg, dass der Chat-Verlauf (Entwurf aus Aufgabe A) wirklich mitgenommen wird.
- **Sätze sind lang:** 3 Sätze werden mit je 25–40 Wörtern erkauft (Komma-Ketten). „Genau 3 Sätze“ ist erfüllt, eine Kurznachricht für den Messenger ist es kaum. Lehre: Formatvorgaben werden wörtlich erfüllt – wer es wirklich kurz will, sollte „höchstens 50 Wörter“ oder „3 kurze Sätze“ ergänzen.
- **Prüfen, ob die Notiz zum Entwurf passt:** Steht in der internen Nachricht etwas, das im Kundenentwurf nicht stand (Opus: „falsch berechnete Fracht“, „bis morgen“)? Das ist die Übertragung der Checkliste aus Aufgabe A auf die interne Kommunikation.
- **Fristen mitdenken:** Kundenfrist Mittwoch ≠ interne Frist. Haiku setzt beides gleich, Opus baut Puffer ein. Schöne Frage ans Plenum: „Bis wann braucht ihr die Info von der Logistik wirklich?“
- **Zuständigkeiten:** Nur Sonnet und Opus beschränken den Auftrag auf Logistik-Themen (Termin, Teillieferung); Nachlass und Fracht gehören woandershin. Anschlussidee: „Schreib je eine Zeile an Logistik, Buchhaltung und Vertriebsleitung.“
- **„Geantwortet“ vs. „Entwurf“:** Die Notiz behauptet, der Kunde sei schon informiert. Vor dem Weiterleiten erst die Kundenmail wirklich abschicken – oder im Prompt „was wir ihm antworten werden“ schreiben.

## Gesprächsprotokolle

### Haiku

#### Nutzer 1

Ich arbeite im Vertrieb der Nordlicht Technik GmbH. Unten steht eine verärgerte Kundenmail wegen eines Lieferverzugs. Schreibe mir einen Antwortentwurf, der sich für die Verzögerung entschuldigt, ohne Schuld abzuwälzen, auf die konkreten Punkte des Kunden eingeht, einen nächsten Schritt anbietet, höflich und sachlich ist und höchstens 150 Wörter hat. Erfinde keine Fakten wie Liefertermine oder Rabatte, sondern setze Platzhalter in eckigen Klammern.

Hier die Kundenmail:
Von: Markus Brenner, Betreff: WIE LANGE NOCH??? Auftrag 4711-NT / Steuergehäuse (120 Steuergehäuse SG-40, zugesagt KW 18, jetzt KW 21 ohne Lieferung, zweimal vertröstet, Montage steht still, Forderung nach verbindlichem Liefertermin in Schriftform, Teillieferung von 60 Stück möglich, mindestens 10 % Nachlass, Prüfung der 85 Euro Frachtkosten auf RE-2024-0815 trotz vereinbarter Lieferung frei Haus, Rückmeldung bis Mittwoch).

#### Assistent 1

Betreff: Re: Auftrag 4711-NT / Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

vielen Dank für Ihre deutlichen Worte. Es tut uns leid, dass die Gehäuse nicht wie zugesagt in KW 18 eingetroffen sind, dass Sie zweimal ohne belastbare Auskunft vertröstet wurden und dass Ihre Montage dadurch stillsteht. Das hätte so nicht passieren dürfen, und wir verstehen den Ärger.

Zu Ihren Punkten:
- Liefertermin: Sie erhalten von uns bis [DATUM] einen verbindlichen Termin schriftlich bestätigt, aktuell geplant für [NEUER LIEFERTERMIN].
- Teillieferung: Eine Teillieferung von 60 Stück ist [möglich am TERMIN / derzeit nicht möglich].
- Nachlass: Ihren Wunsch nach einem Entgegenkommen prüfen wir und melden uns dazu bis [DATUM].
- Frachtkosten zu RE-2024-0815: Wir prüfen die 85 Euro gegen die getroffene Vereinbarung und korrigieren sie gegebenenfalls.

Ich rufe Sie gern an, um die nächsten Schritte abzustimmen. Passt Ihnen [TAG, UHRZEIT]? Alternativ erreichen Sie mich unter [TELEFON].

Mit freundlichen Grüßen
[NAME]
[FUNKTION]
Nordlicht Technik GmbH

#### Nutzer 2

Fasse den Fall für meine Kollegin aus der Logistik in 3 Sätzen zusammen: Was ist passiert, was haben wir dem Kunden geantwortet, was muss sie jetzt klären? Lockerer Ton, wir duzen uns.

#### Assistent 2

Hey, Markus Brenner von Brenner Gerätebau wartet seit KW 18 auf die 120 Steuergehäuse SG-40 aus Auftrag 4711-NT, jetzt ist es KW 21, seine Montage steht still und er hat zweimal nur ein "nächste Woche" gehört. Wir haben ihm mit einem Entschuldigungsentwurf geantwortet, in dem wir einen verbindlichen, schriftlichen Liefertermin bis [DATUM] zusagen, eine Teillieferung von 60 Stück prüfen, seinen Nachlasswunsch prüfen und die 85 Euro Frachtkosten auf RE-2024-0815 gegen die frei-Haus-Vereinbarung checken. Du musst also bis Mittwoch klären, welcher Liefertermin realistisch ist, ob eine Teillieferung machbar ist und ob die Fracht falsch berechnet wurde, bevor wir ihm zurückschreiben.

### Sonnet

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
(Anhang: kundenmail_beschwerde.txt – Mail von Markus Brenner, Brenner Gerätebau GmbH, Auftrag 4711-NT, 120 Steuergehäuse SG-40, zugesagt KW 18, Forderungen: verbindlicher schriftlicher Liefertermin, ggf. Teillieferung 60 Stück, mind. 10 % Nachlass, Korrektur Frachtkosten 85 € auf Rechnung RE-2024-0815, Rückmeldung bis Mittwoch)
```

#### Assistent 1

Betreff: Ihr Auftrag 4711-NT – Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

bitte entschuldigen Sie die Verzögerung bei Ihrem Auftrag 4711-NT. Zugesagt war KW 18, geliefert haben wir nicht, und dass Sie dazu nicht von uns informiert wurden, hätte nicht passieren dürfen. Wir verstehen, dass Ihre Montage dadurch beeinträchtigt ist.

- Liefertermin: Wir bestätigen Ihnen schriftlich bis Mittwoch den verbindlichen Termin: [NEUER LIEFERTERMIN].
- Teillieferung: Eine Lieferung von 60 Stück prüfen wir; Ergebnis: [TEILLIEFERUNG MÖGLICH? TERMIN].
- Nachlass: Ihr Anliegen leiten wir intern weiter; Entscheidung: [ENTSCHEIDUNG ZUM NACHLASS].
- Fracht: Die 85 Euro auf RE-2024-0815 prüfen wir und korrigieren sie bei Vereinbarung „frei Haus“ [ERGEBNIS FRACHTPRÜFUNG].

Gern rufe ich Sie vorab an: [RUFNUMMER / ZEITFENSTER].

Mit freundlichen Grüßen
[NAME]
Nordlicht Technik GmbH

#### Nutzer 2

```text
Fasse den Fall für meine Kollegin aus der Logistik in 3 Sätzen zusammen:
Was ist passiert, was haben wir dem Kunden geantwortet, was muss sie
jetzt klären? Lockerer Ton, wir duzen uns.
```

#### Assistent 2

Hey, kurz zum Fall: Brenner Gerätebau wartet auf 120 Steuergehäuse SG-40 (Auftrag 4711-NT), zugesagt war KW 18, jetzt ist KW 21 und nichts ist da, ohne dass wir uns gemeldet haben, und beim Kunden steht teilweise die Montage still. Wir haben uns im Antwortentwurf entschuldigt und zugesagt, bis Mittwoch einen verbindlichen Liefertermin schriftlich zu nennen, eine Teillieferung von 60 Stück sowie die 85 Euro Fracht auf RE-2024-0815 zu prüfen und den geforderten 10 % Nachlass intern zu klären. Kannst du bitte schnellstmöglich klären, wann wir realistisch liefern können (und ob 60 Stück vorab gehen), damit wir den Termin bis Mittwoch zusagen können?

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

Hier ist ein Antwortentwurf mit etwa 125 Wörtern:

---

**Betreff:** AW: Auftrag 4711-NT / Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

vielen Dank für Ihre offenen Worte. Sie haben recht: Die für KW 18 zugesagte Lieferung haben wir nicht eingehalten, und Sie wurden nicht aktiv informiert. Dass dadurch Ihre Montage teilweise stillsteht und Sie gegenüber Ihrem Kunden in Schwierigkeiten geraten, bedauere ich sehr. Dafür entschuldige ich mich ausdrücklich.

Zu Ihren Punkten:
- **Liefertermin:** Verbindlich zusagen können wir Ihnen [VERBINDLICHER LIEFERTERMIN]. Eine Teillieferung von 60 Stück ist [MÖGLICH ZUM DATUM … / NICHT MÖGLICH].
- **Entgegenkommen:** Ihren Wunsch nach einem Nachlass kläre ich intern und melde mich dazu bis [DATUM].
- **Rechnung RE-2024-0815:** Wir prüfen die Frachtkosten von 85 Euro anhand der Vereinbarung „frei Haus“ und korrigieren sie gegebenenfalls.

Gern rufe ich Sie am [DATUM/UHRZEIT] an, um alles persönlich zu besprechen.

Mit freundlichen Grüßen
[NAME]
[FUNKTION]
Nordlicht Technik GmbH
[TELEFON]

---

**Hinweise vor dem Versand:**
- Herr Brenner erwartet bis **Mittwoch** eine Antwort. Schicken Sie die Mail am besten vorher ab, auch wenn noch nicht alle Punkte geklärt sind.
- Den Nachlass von 10 % habe ich bewusst weder zugesagt noch abgelehnt. Das sollte intern entschieden werden, zum Beispiel von der Vertriebsleitung.
- Setzen Sie nur einen Liefertermin ein, den Logistik oder Produktion wirklich bestätigt haben. Der Kunde will ausdrücklich kein „voraussichtlich“ mehr.

#### Nutzer 2

```text
Fasse den Fall für meine Kollegin aus der Logistik in 3 Sätzen zusammen:
Was ist passiert, was haben wir dem Kunden geantwortet, was muss sie
jetzt klären? Lockerer Ton, wir duzen uns.
```

#### Assistent 2

Hi, kurz zum Fall Brenner Gerätebau: Die 120 Steuergehäuse SG-40 aus Auftrag 4711-NT sollten in KW 18 kommen, jetzt ist KW 21 und noch nichts da, bei denen steht deshalb teilweise die Montage still und Herr Brenner ist entsprechend sauer. Ich habe mich bei ihm entschuldigt und ihm einen verbindlichen schriftlichen Liefertermin, eine Antwort zu seiner Nachlassforderung und die Prüfung einer falsch berechneten Fracht (85 Euro auf RE-2024-0815) zugesagt, außerdem einen Rückruf. Kannst du bitte klären, welchen Liefertermin wir ganz sicher halten können und ob eine Teillieferung von 60 Stück früher drin ist, und mir das am besten bis morgen sagen, weil er bis Mittwoch eine Antwort von uns erwartet?
