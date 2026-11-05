# Testlauf: Übung 2 / Trainer-Musterprompt E – Wöchentlicher Statusbericht Projektleitung

**Herkunft:** [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md), Abschnitt „Übung 2: Gute Prompts“ → „Musterprompts“ (fertiges Beispiel für Aufgabe E). Übungsblatt: [Übung 2: Gute Prompts](../06_Uebungen/Uebung_2_Gute_Prompts.md), Aufgabe E „Dein eigener wiederverwendbarer Prompt“.
Die Stichpunkte für den Test sind erfunden, aber an das Beispielmaterial angelehnt: [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md) (LS-3015) und [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt) (Messe/Standpersonal, Lieferantenliste vor dem Audit). Die Lücke `[ART DES UNTERNEHMENS]` wurde mit „mittelständischen Unternehmens“ gefüllt.

> **Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prüfkriterien:** genau 4 Tabellenzeilen; Spalten wie vorgegeben (Projekt | Status | Was ist passiert | Nächster Schritt | Entscheidung nötig?); plausible Ampel (LS-3015 gelb mit „Entscheidung nötig: ja“, Messe gelb, Azubi grün, Lieferantenliste gelb oder rot); Gesamteinschätzung höchstens 3 Sätze, per du; keine erfundenen Daten/Termine (Audit-Termin bleibt unklar), stattdessen Rückfragen.

---

## Bewertung

Sätze und Wörter der Gesamteinschätzung per Python gezählt (Satzende = `.`/`!`/`?` mit folgendem Leerzeichen oder Textende): Haiku 3 Sätze/39 Wörter, Sonnet 3/39, Opus 3/40.

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| 4 Zeilen, Spalten wie vorgegeben | ja | ja | ja |
| Ampel LS-3015 / Messe / Azubi / Lieferantenliste | gelb / gelb / grün / rot – plausibel | gelb / gelb / grün / rot – plausibel | gelb / gelb / grün / rot – plausibel, rot vs. gelb begründet |
| LS-3015 „Entscheidung nötig: ja“ | ja | ja (fett) | ja (fett), mit Platzhalter „Bis [Datum]“ |
| Gesamteinschätzung ≤ 3 Sätze | ja (3) | ja (3) | ja (3) |
| Per du an die GF | nein – spricht von „die Geschäftsführung“ in der 3. Person | ja, aber holprig: „brauchen wir von dir als Geschäftsführung“ | ja: „brauche ich deine Entscheidung“ |
| Nichts erfunden (Audit-Termin offen) | ja; kleine Verschärfung „muss“ statt „soll“ | ja; leichte Umdeutung „Termin zum Audit unklar“ | ja, Lücken als `[Platzhalter]`; kleine Ergänzung „Nachbesserung beim Lieferanten“, „muss“ statt „soll“ |
| Rückfragen statt Erfindung | 3 Fragen (Audit-Datum, Zuständigkeit, Frist Standpersonal) | 4 Fragen, inkl. Inhalt des Vorbehalts und Ampel-Bestätigung | 5 Fragen, inkl. Vorbehalte, KW, Startdatum, Ampel-Begründung |
| Direkt versandfähig | fast (Du-Form fehlt) | fast | nein – Entwurf mit Platzhaltern, bewusst |

**Gesamturteil:** Der Musterprompt funktioniert wie gedacht. Alle drei Modelle liefern die vorgegebene Tabelle mit identischer, plausibler Ampel, halten die 3-Satz-Grenze ein und erfinden keine Termine. Kein Modell „fragt nur nach und wartet“ – alle liefern einen Bericht **und** hängen Rückfragen an. Das ist für einen Wochenbericht sinnvoll, sollte der Trainer aber so ankündigen. Unterschiede gibt es bei der Du-Form und bei der Spalte „Entscheidung nötig?“, die jedes Modell anders füllt.

---

## Gefundene Fehler mit Beleg

1. **Haiku – Du-Form nicht umgesetzt:** Der Prompt verlangt „Sachlich, per du.“ Die Gesamteinschätzung lautet: „Bei der Laserschneidanlage braucht die **Geschäftsführung** eine Entscheidung …“ – die Empfängerin wird in der dritten Person angesprochen, nirgends geduzt. Kein Sachfehler, aber eine nicht erfüllte Formatvorgabe.
2. **Sonnet – unklare Perspektive:** „Bei der Laserschneidanlage brauchen **wir von dir als Geschäftsführung** eine Entscheidung“. Der Bericht kommt von einer Person aus der Projektleitung („ich“ laut Kontext); „wir … von dir als Geschäftsführung“ wirkt künstlich. Außerdem fehlt die Messe in Sonnets Gesamteinschätzung ganz, obwohl sie gelb ist.
3. **Sonnet – leichte Umdeutung der Quelle:** Stichpunkt: „noch nicht begonnen, **Termin unklar** (soll vor dem Lieferantenaudit fertig sein)“. Sonnet schreibt: „… und **der Termin zum Audit** unklar ist.“ In der Quelle ist der Projekttermin unklar; ob das Audit-Datum bekannt ist, steht nicht da (unbekannt ist es trotzdem, daher Fragen aller Modelle danach – korrekt).
4. **Haiku und Opus – „muss“ statt „soll“:** Quelle: „**soll** vor dem Lieferantenaudit fertig sein“. Haiku: „Die Liste **muss** vor dem Lieferantenaudit fertig sein.“ Opus: „**Muss** vor dem Lieferantenaudit [Datum] fertig sein.“ Kleine, aber typische Verschärfung beim Umformulieren – im Statusbericht an die GF ändert das die Dringlichkeit.
5. **Opus – kleine Ergänzung:** Nächster Schritt LS-3015: „… bzw. **Nachbesserung beim Lieferanten anfordern**.“ Dass der Vorbehalt eine Nachbesserung durch den Lieferanten bedeutet, steht nicht in den Stichpunkten (im Prüfbericht-Material ist das zwar plausibel, aber der KI lag er nicht vor). Opus fragt allerdings selbst nach den Vorbehalten.
6. **Opus – leichter Widerspruch:** „Zwei Projekte laufen weitgehend planmäßig, bei der Messe ist das Standpersonal noch offen.“ Gemeint sind offenbar Azubi und Messe – die Messe ist in der Tabelle aber gelb. Für die GF ist unklar, welche zwei Projekte gemeint sind.
7. **Spalte „Entscheidung nötig?“ uneinheitlich (alle):** Für die Lieferantenliste schreibt Haiku „**Ja, falls** die Bereinigung bis zum Audit nicht machbar ist“, Sonnet „**Nein, aber** ohne Terminfestlegung droht ein Konflikt“, Opus „**[offen: Ja, falls** Ressourcen oder Priorität geklärt werden müssen]“. Bei der Messe ähnlich (Haiku „Nur, falls das Personal intern nicht besetzt werden kann“ – eine Annahme, die nicht in den Stichpunkten steht). Kein Fehler im engeren Sinn, aber die Spalte soll laut Kontext auf einen Blick zeigen „Wo brauche ich eine Entscheidung?“ – bedingte Antworten verwässern das.
8. **Nicht erfunden (positiv):** Kein Modell nennt ein Audit-Datum, ein Messedatum, eine KW oder einen Vorbehaltsinhalt. Die Zahl „2 Azubis“ und „nächsten Monat“ werden korrekt übernommen. Opus setzt fehlende Angaben konsequent als `[Platzhalter]`.

---

## Lehren für die Auswertung

- **„Frag nach“ heißt in der Praxis „liefern und nachfragen“.** Keines der Modelle hat gewartet. Für einen Wochenbericht ist das richtig – wer wirklich erst Fragen will, braucht die Technik aus Aufgabe C („Stell mir zuerst 3 Fragen und warte“). Guter Brückenschlag zwischen C und E.
- **Rückfragen zeigen, was im Prompt fehlt.** Die Fragen der Modelle (Inhalt des Vorbehalts, Audit-Datum, wer entscheidet übers Standpersonal, KW) sind genau die Angaben, die man beim nächsten Mal in die Stichpunkte schreibt. Aufgabe an die Gruppe: „Nimm die Rückfragen und ergänze deine Vorlage um eine Zeile dafür.“
- **Feste Spalten brauchen feste Bedeutung.** „Entscheidung nötig?“ wird mal mit „Ja, falls …“, mal mit „Nein, aber …“ gefüllt. Verbesserung für den Prompt: „In der Spalte ‚Entscheidung nötig?‘ nur ‚Ja: [Frage an die GF]‘ oder ‚Nein‘.“ Das ist eine schöne Iterations-Übung (Aufgabe D/F).
- **Kleine Wortverschiebungen prüfen.** „soll“ wird zu „muss“, „Termin unklar“ zu „Termin zum Audit unklar“. Beim Statusbericht an die Chefin zählt genau das – Prüfauftrag: jede Zeile gegen den eigenen Stichpunkt lesen.
- **Formatvorgaben werden unterschiedlich ernst genommen.** „Per du“ setzt nur Opus sauber um. Zeigen: Vorgaben, die man nicht prüft, gehen leise verloren.
- **Ampel ist Ermessen.** Alle Modelle wählen rot für die Lieferantenliste; Opus und Sonnet bitten um Bestätigung. Die Ampel bleibt die Entscheidung der Projektleitung, nicht der KI.
- **Modellunterschied:** Haiku liefert den kompaktesten, fast fertigen Bericht; Sonnet liegt dazwischen; Opus liefert einen Entwurf mit Platzhaltern und die gründlichsten Rückfragen – mehr Nacharbeit, aber weniger Risiko, Unbelegtes weiterzugeben.

---

## Gesprächsprotokolle

### Haiku

#### Nutzer 1

```text
Rolle: Du bist eine erfahrene Assistenz der Projektleitung.

Kontext: Ich arbeite in der Projektleitung eines mittelständischen Unternehmens. Jeden Freitag schicke ich der Geschäftsführung einen kurzen Statusbericht zu meinen Projekten. Die Geschäftsführung will schnell sehen: Läuft alles? Wo brauche ich eine Entscheidung?

Aufgabe: Erstelle aus den Stichpunkten unten den Statusbericht dieser Woche.

Format: Pro Projekt eine Zeile in einer Tabelle mit den Spalten Projekt | Status (grün/gelb/rot) | Was ist passiert | Nächster Schritt | Entscheidung nötig? Darunter höchstens 3 Sätze Gesamteinschätzung. Sachlich, per du.

Wenn dir Informationen fehlen, frag nach, statt etwas zu erfinden.

Stichpunkte:
- Laserschneidanlage LS-3015: Abnahmeprüfung abgeschlossen, Bericht liegt vor, Empfehlung Abnahme unter Vorbehalt, GF muss entscheiden
- Messe Industrietage: Stand gebucht, Prospekte werden überarbeitet, Standpersonal noch offen
- Azubi-Einarbeitung: Plan in Arbeit, Start der 2 Azubis nächsten Monat, läuft nach Plan
- Lieferantenliste bereinigen: noch nicht begonnen, Termin unklar (soll vor dem Lieferantenaudit fertig sein)
```

#### Assistent 1

| Projekt | Status | Was ist passiert | Nächster Schritt | Entscheidung nötig? |
|---|---|---|---|---|
| Laserschneidanlage LS-3015 | gelb | Abnahmeprüfung ist abgeschlossen, der Bericht liegt vor. Empfehlung: Abnahme unter Vorbehalt. | Die GF entscheidet über die Abnahme unter Vorbehalt. | Ja: Abnahme unter Vorbehalt ja oder nein |
| Messe Industrietage | gelb | Der Stand ist gebucht, die Prospekte werden überarbeitet. Das Standpersonal ist noch offen. | Prospekte fertigstellen und Standpersonal planen. | Nur, falls das Personal intern nicht besetzt werden kann |
| Azubi-Einarbeitung | grün | Der Plan ist in Arbeit. Die 2 Azubis starten nächsten Monat, der Zeitplan passt. | Einarbeitungsplan fertigstellen. | Nein |
| Lieferantenliste bereinigen | rot | Noch nicht begonnen, der Termin ist unklar. Die Liste muss vor dem Lieferantenaudit fertig sein. | Termin und Verantwortliche festlegen, bevor das Audit näher rückt. | Ja, falls die Bereinigung bis zum Audit nicht machbar ist |

**Gesamteinschätzung:** Die Azubi-Einarbeitung läuft nach Plan, und die Messevorbereitung kommt voran. Bei der Laserschneidanlage braucht die Geschäftsführung eine Entscheidung zur Abnahme unter Vorbehalt. Kritisch ist die Lieferantenliste, weil sie noch nicht begonnen wurde und vor dem Lieferantenaudit fertig sein muss.

**Offene Fragen, damit der Bericht vollständig wird:**
1. Wann findet das Lieferantenaudit statt?
2. Wer übernimmt die Bereinigung der Lieferantenliste, und wie viel Zeit steht dafür zur Verfügung?
3. Bis wann muss das Standpersonal für die Messe feststehen?

---

### Sonnet

#### Nutzer 1

```text
Rolle: Du bist eine erfahrene Assistenz der Projektleitung.

Kontext: Ich arbeite in der Projektleitung eines mittelständischen Unternehmens.
Jeden Freitag schicke ich der Geschäftsführung einen kurzen Statusbericht zu meinen Projekten.
Die Geschäftsführung will schnell sehen: Läuft alles? Wo brauche ich eine Entscheidung?

Aufgabe: Erstelle aus den Stichpunkten unten den Statusbericht dieser Woche.

Format: Pro Projekt eine Zeile in einer Tabelle mit den Spalten
Projekt | Status (grün/gelb/rot) | Was ist passiert | Nächster Schritt | Entscheidung nötig?
Darunter höchstens 3 Sätze Gesamteinschätzung. Sachlich, per du.

Wenn dir Informationen fehlen, frag nach, statt etwas zu erfinden.

Stichpunkte:
- Laserschneidanlage LS-3015: Abnahmeprüfung abgeschlossen, Bericht liegt vor, Empfehlung Abnahme unter Vorbehalt, GF muss entscheiden
- Messe Industrietage: Stand gebucht, Prospekte werden überarbeitet, Standpersonal noch offen
- Azubi-Einarbeitung: Plan in Arbeit, Start der 2 Azubis nächsten Monat, läuft nach Plan
- Lieferantenliste bereinigen: noch nicht begonnen, Termin unklar (soll vor dem Lieferantenaudit fertig sein)
```

#### Assistent 1

Hier ist der Statusbericht für diese Woche. Die Status-Ampeln habe ich aus deinen Stichpunkten abgeleitet. Sag Bescheid, wenn du eine anders einschätzt.

| Projekt | Status | Was ist passiert | Nächster Schritt | Entscheidung nötig? |
|---|---|---|---|---|
| Laserschneidanlage LS-3015 | gelb | Abnahmeprüfung ist abgeschlossen, der Bericht liegt vor. Die Empfehlung lautet: Abnahme unter Vorbehalt. | Entscheidung der Geschäftsführung abwarten, danach die Abnahme entsprechend umsetzen. | **Ja:** Abnahme unter Vorbehalt, ja oder nein? |
| Messe Industrietage | gelb | Stand ist gebucht, die Prospekte werden überarbeitet. Das Standpersonal ist noch offen. | Standpersonal festlegen, Prospekte fertigstellen. | Offen: Wer besetzt den Stand? (siehe Rückfrage 2) |
| Azubi-Einarbeitung | grün | Der Einarbeitungsplan ist in Arbeit. Die 2 Azubis starten nächsten Monat. | Plan fertigstellen. | Nein |
| Lieferantenliste bereinigen | rot | Noch nicht begonnen, Termin unklar. Die Liste soll vor dem Lieferantenaudit fertig sein. | Starttermin und Fertigstellungstermin festlegen. | Nein, aber ohne Terminfestlegung droht ein Konflikt mit dem Audit. |

**Gesamteinschätzung:** Die Azubi-Einarbeitung läuft nach Plan. Bei der Laserschneidanlage brauchen wir von dir als Geschäftsführung eine Entscheidung zur Abnahme unter Vorbehalt. Die Lieferantenliste ist das größte Risiko, weil sie noch nicht begonnen ist und der Termin zum Audit unklar ist.

**Rückfragen, damit ich nichts erfinde:**
1. Welcher Vorbehalt steht in der Abnahmeempfehlung für die LS-3015 (z. B. Mängel, Nachbesserungen, Fristen)? Die Geschäftsführung braucht das für die Entscheidung.
2. Wann finden die Industrietage statt, und wer soll das Standpersonal bestimmen? Falls die Geschäftsführung dabei entscheiden soll, setze ich in der Tabelle "Ja".
3. Wann ist das Lieferantenaudit? Mit dem Datum kann ich einen Fristvorschlag für die Lieferantenliste ergänzen und die Ampel genauer begründen.
4. Stimmt die Ampel für die Lieferantenliste (rot) und die Messe (gelb) für dich?

---

### Opus

#### Nutzer 1

```text
Rolle: Du bist eine erfahrene Assistenz der Projektleitung.

Kontext: Ich arbeite in der Projektleitung eines mittelständischen Unternehmens.
Jeden Freitag schicke ich der Geschäftsführung einen kurzen Statusbericht zu meinen Projekten.
Die Geschäftsführung will schnell sehen: Läuft alles? Wo brauche ich eine Entscheidung?

Aufgabe: Erstelle aus den Stichpunkten unten den Statusbericht dieser Woche.

Format: Pro Projekt eine Zeile in einer Tabelle mit den Spalten
Projekt | Status (grün/gelb/rot) | Was ist passiert | Nächster Schritt | Entscheidung nötig?
Darunter höchstens 3 Sätze Gesamteinschätzung. Sachlich, per du.

Wenn dir Informationen fehlen, frag nach, statt etwas zu erfinden.

Stichpunkte:
- Laserschneidanlage LS-3015: Abnahmeprüfung abgeschlossen, Bericht liegt vor, Empfehlung Abnahme unter Vorbehalt, GF muss entscheiden
- Messe Industrietage: Stand gebucht, Prospekte werden überarbeitet, Standpersonal noch offen
- Azubi-Einarbeitung: Plan in Arbeit, Start der 2 Azubis nächsten Monat, läuft nach Plan
- Lieferantenliste bereinigen: noch nicht begonnen, Termin unklar (soll vor dem Lieferantenaudit fertig sein)
```

#### Assistent 1

Hier ist ein Entwurf für den Statusbericht dieser Woche. Wo mir Angaben fehlen, steht ein Platzhalter in eckigen Klammern. Die Fragen dazu findest du unter dem Bericht.

---

**Statusbericht Projekte – KW [xx]**

| Projekt | Status | Was ist passiert | Nächster Schritt | Entscheidung nötig? |
|---|---|---|---|---|
| Laserschneidanlage LS-3015 | gelb | Abnahmeprüfung abgeschlossen, Prüfbericht liegt vor. Empfehlung: Abnahme unter Vorbehalt [Vorbehalte/offene Punkte nennen]. | Entscheidung der GF einholen, danach Abnahme formal abschließen bzw. Nachbesserung beim Lieferanten anfordern. | **Ja:** Abnahme unter Vorbehalt freigeben? Bis [Datum]. |
| Messe Industrietage | gelb | Stand ist gebucht, Prospekte werden überarbeitet. Standpersonal ist noch nicht festgelegt. | Standpersonal klären [wer/bis wann], Prospekte fertigstellen. | [offen: Ja, falls die GF das Standpersonal benennen oder freigeben muss] |
| Azubi-Einarbeitung | grün | Einarbeitungsplan ist in Arbeit, Start der 2 Azubis im nächsten Monat. Läuft nach Plan. | Einarbeitungsplan fertigstellen [bis Datum]. | Nein |
| Lieferantenliste bereinigen | rot | Noch nicht begonnen, kein Termin festgelegt. Muss vor dem Lieferantenaudit [Datum] fertig sein. | Verantwortliche Person und Termin festlegen, Bereinigung starten. | [offen: Ja, falls Ressourcen oder Priorität geklärt werden müssen] |

**Gesamteinschätzung:** Zwei Projekte laufen weitgehend planmäßig, bei der Messe ist das Standpersonal noch offen. Für die LS-3015 brauche ich deine Entscheidung zur Abnahme unter Vorbehalt. Kritisch ist die Lieferantenliste: Sie ist noch nicht begonnen und muss vor dem Lieferantenaudit fertig sein.

---

**Damit der Bericht vollständig ist, brauche ich noch ein paar Angaben:**

1. **LS-3015:** Was sind die Vorbehalte, also welche Mängel oder offenen Punkte nennt der Prüfbericht? Und bis wann braucht ihr die Entscheidung der GF?
2. **Messe Industrietage:** Wann ist die Messe? Wer entscheidet über das Standpersonal? Muss die GF dafür Leute freigeben?
3. **Azubi-Einarbeitung:** Bis wann soll der Plan fertig sein, und gibt es ein genaues Startdatum?
4. **Lieferantenliste:** Wann ist das Lieferantenaudit, und wer ist zuständig? Den Status „rot“ habe ich gewählt, weil das Projekt noch nicht begonnen hat und kein Termin feststeht. Ist das Audit noch weit weg, passt auch „gelb“. Soll die GF hier etwas entscheiden, zum Beispiel über Priorität oder Kapazität?
5. **Kalenderwoche:** Welche KW soll im Titel stehen?

Wenn du mir das schickst, mache ich dir die fertige Version ohne Platzhalter.

---

Zurück zum Übungsblatt: [Übung 2: Gute Prompts](../06_Uebungen/Uebung_2_Gute_Prompts.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md)
