# Testlauf: Übung 2 / Weiter E – Eigener wiederverwendbarer Prompt (Wochenbericht Vertriebsinnendienst)

**Herkunft:** [Übung 2, Aufgabe E im Übungsblatt](../06_Uebungen/Uebung_2_Gute_Prompts.md#aufgabe-e--dein-eigener-wiederverwendbarer-prompt) (Vorlage mit festen Teilen und Lücken). Passender Abschnitt in den [Trainer-Lösungshinweisen](../06_Uebungen/Trainer-Loesungshinweise.md#übung-2-gute-prompts) (Musterprompt „Statusbericht Projektleitung“, „Woran du ein gutes Ergebnis erkennst“, „Aufgabe E zu allgemein“).

**Testdatum:** Montag, 2. November 2026

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

Getestet wurde, wie eine Teilnehmerin aus dem Vertriebsinnendienst die Vorlage ausfüllen könnte. Für den Testlauf wurden die Lücken befüllt (Rolle, Abteilung, Empfängerin, Format, Stilbeispiel) und sechs erfundene Stichpunkte mit anonymisierten Kunden (A–E) eingesetzt. Jedes Modell bekam den Prompt in einem neuen, leeren Chat. Die Wortzahlen wurden per Skript (python3) gezählt, und zwar nur der Bericht selbst mit Überschriften, ohne Einleitungssatz und ohne Rückfragen.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Höchstens 150 Wörter (Bericht nachgezählt) | ja, 88 | ja, 78 | ja, 84 (selbst angegeben: „ca. 85“, stimmt) |
| Genau 3 Abschnitte Erledigt / Offen / Entscheidung nötig | **teilweise**: zusätzlicher Einleitungsabsatz vor „Erledigt“, der Inhalte doppelt | ja | ja |
| Alle 6 Stichpunkte enthalten und richtig zugeordnet | ja | ja | ja |
| Kunde E sinnvoll aufgeteilt (Rückruf → Erledigt, Termin → Offen) | ja | ja | ja |
| Nachlass-Frage unter „Entscheidung nötig“ | ja | ja | ja |
| Keine erfundenen Werte (Liefertermin E, Nachlasshöhe, Kundennamen) | ja | ja | ja |
| Ton: sachlich, intern, kein „Sie“ | ja | ja | ja |
| Stilbeispiel („Diese Woche 5 Angebote raus …“) aufgegriffen | ja (im Einleitungsabsatz) | nein, eher förmliche ganze Sätze | ja |
| Platzhalter [VERTRIEBSLEITUNG] im Bericht erhalten | nein (Frage ohne Adressat) | nein, aber als Rückfrage angesprochen | nein (Frage ohne Adressat) |
| Rückfragen statt Erfinden | ja, 3 Fragen (Nachlassgrenze, Frist B, Frist Druckerei) | ja, 2 Fragen (Fristen, Name im Bericht) | ja, 4 Fragen, die besten (Rückmeldung C/D, Bezug Auftrag A, Daten zu E, Frist Druckerei) |
| Bericht sofort nutzbar | ja, Einleitung streichen | ja | ja |

**Gesamturteil:** Die Übung funktioniert wie gedacht. Mit der ausgefüllten Vorlage liefern alle drei Modelle beim ersten Versuch einen kurzen, korrekt gegliederten Wochenbericht, erfinden nichts und stellen von sich aus Rückfragen. Der Satz „frag nach, statt etwas zu erfinden“ zeigt sichtbare Wirkung. Kleine Abweichungen: Haiku setzt einen zusätzlichen Einleitungsabsatz vor die drei Abschnitte, und kein Modell lässt den Platzhalter [VERTRIEBSLEITUNG] im Bericht stehen.

---

## Gefundene Fehler mit Beleg

Es gibt keine sachlichen Fehler und keine Halluzinationen. Alle Zahlen stimmen mit den Stichpunkten überein: 5 Angebote, Verteilung 2x A und je 1x B, C, D, ca. 20.000 € bei Kunde A. Liefertermin und Nachlasshöhe bleiben bei allen Modellen offen. Kleinere Abweichungen:

1. **Haiku – Format nicht ganz eingehalten.** Vor „Erledigt“ steht ein eigener Absatz („Diese Woche 5 Angebote Steuergehäuse raus, davon 2x Kunde A … Kunde A hat einen Auftrag über ca. 20.000 € bestätigt.“), dessen Inhalt unter „Erledigt“ noch einmal kommt. Gefordert waren „3 Abschnitte mit Zwischenüberschrift“. Das ist eine Doppelung, aber kein inhaltlicher Fehler.
2. **Alle – Platzhalter [VERTRIEBSLEITUNG] fällt weg.** Im Stichpunkt steht „Frage an [VERTRIEBSLEITUNG]: Dürfen wir …“. Im Bericht steht bei allen dreien nur noch „Dürfen wir Kunde E …?“. Weil der ganze Bericht an die Vertriebsleiterin geht, ergibt das Weglassen Sinn. Ein Prüfkriterium „Platzhalter bleibt“ erfüllt aber keines der Modelle. Sonnet erwähnt den Platzhalter als Einziges und fragt, ob der Name an den Anfang soll. Damit lädt es dazu ein, einen echten Namen einzutragen (Daten-Ampel beachten).
3. **Opus – kleine, plausible Ergänzungen.** „Kunde B wartet auf **unsere** technische Rückmeldung“ und „Nachlass **wegen des Lieferverzugs**“ stehen so nicht in den Stichpunkten. Beides folgt aber direkt aus dem Kontext. Es sind keine erfundenen Werte.
4. **Opus – Rückfrage nach dem Auftragswert von Kunde E.** Inhaltlich ist die Frage sinnvoll. Sie fordert aber genau die Art Daten an (Preise, Auftragswerte), die laut Daten-Ampel-Check nicht in den Prompt gehören. Das eignet sich gut für die Auswertung: Die KI kennt eure Datenregeln nicht.
5. **Sonnet – Stilbeispiel kaum übernommen.** Statt des lockeren Kurzstils („5 Angebote raus“) schreibt Sonnet ganze, eher förmliche Sätze („Die Daten sind noch nicht an die Druckerei gegangen.“). Das ist kein Fehler, zeigt aber, dass ein einzelnes Stilbeispiel nur schwach wirkt.

---

## Lehren für die Auswertung

- **Die Vorlage wirkt.** Mit Rolle, Kontext, Format und Stichpunkten gelingt der Bericht beim ersten Mal. Gut zum Zeigen: drei Modelle, dreimal fast dieselbe Struktur, weil das Format genau vorgegeben war.
- **„Frag nach, statt zu erfinden“ ist der wertvollste Satz.** Kein Modell erfindet einen Liefertermin oder eine Nachlasshöhe. Alle stellen Rückfragen. Opus fällt sogar eine echte Lücke in den Stichpunkten auf: Was ist mit den Angeboten an C und D, und gehört der Auftrag von A zu einem oder zu beiden Angeboten? Fragen: „Hättet ihr das selbst bemerkt?“
- **Rückfragen kritisch lesen.** Nicht jede Rückfrage sollte man beantworten. Die Frage nach dem Auftragswert von Kunde E (Opus) oder nach dem Namen der Vertriebsleiterin (Sonnet) betrifft Daten, die die Daten-Ampel ausschließt. Die KI kennt eure Regeln nicht, also entscheidet ihr.
- **Format nachzählen lohnt sich.** Alle Berichte liegen deutlich unter 150 Wörtern, Haiku hält aber die „3 Abschnitte“ nicht genau ein. Typisch: Die Vorgabe wird fast, aber nicht ganz erfüllt. Hier eignet sich Nachschärfen (wie bei Aufgabe D): „Bitte ohne Einleitung, nur die drei Abschnitte.“
- **Stilbeispiel ist ein schwacher Baustein.** Zwei Modelle greifen den Kurzstil auf, eines nicht. Wer einen bestimmten Ton will, sollte ihn zusätzlich beschreiben, z. B. „Stichpunkte im Telegrammstil, keine ganzen Sätze“.
- **Platzhalter in den Stichpunkten** verschwinden leicht, wenn sie für den Text nicht nötig sind. Wer sie am Ende wieder ersetzen will, sollte das sagen: „Platzhalter in eckigen Klammern unverändert lassen.“
- **Speichern nicht vergessen:** Der eigentliche Gewinn der Aufgabe ist die gespeicherte Vorlage. Im Testlauf passte das Ergebnis sofort, also ist das der Moment zum Speichern.

---

## Hinweise zum Material

- **Widerspruch zur Daten-Ampel:** Der Check auf dem Übungsblatt sagt „Keine Preise, Vertragsinhalte …“, und der Musterprompt in den Lösungshinweisen sagt „OHNE KUNDENNAMEN UND PREISE“. Ein naheliegendes Testbeispiel wie dieses enthält aber einen Auftragswert („ca. 20.000 €“). Teilnehmende sind sich deshalb unsicher, ob ein gerundeter Betrag erlaubt ist. Das Material sollte klar sagen, ob gerundete oder erfundene Beträge zum Testen erlaubt sind.
- **Lösungshinweise passen.** Das Kriterium „feste Teile und Lücken in eckigen Klammern, enthält ‚frag nach, statt zu erfinden‘, ist gespeichert“ entspricht dem, was im Test herauskommt. Was fehlt, ist ein Hinweis zum **Testlauf** selbst: Das Ergebnis gegen das eigene Format prüfen (Wörter, Abschnitte) und Rückfragen der KI kritisch lesen.
- **Zeit:** ca. 5 Min. reichen für Ausfüllen und einen Testlauf nur knapp, wenn die Teilnehmenden erst eigene, anonymisierte Stichpunkte formulieren müssen. Mit vorbereiteten Beispiel-Stichpunkten oder dem Statusbericht-Muster („Hilfen für Langsame“) ist die Zeit realistisch.

---

## Gesprächsprotokolle

### Haiku

**Nutzer 1**

```text
Rolle: Du bist eine erfahrene Assistenz der Vertriebsleitung.

Kontext: Ich arbeite im Vertriebsinnendienst eines mittelständischen technischen Herstellers. Ich brauche regelmäßig einen Wochenbericht zu Angeboten, Aufträgen und Reklamationen für unsere Vertriebsleiterin.
Wichtig ist uns: kurz, sachlich, wir duzen uns intern.

Aufgabe: Erstelle aus den Stichpunkten unten einen Wochenbericht.

Format: höchstens 150 Wörter / 3 Abschnitte mit Zwischenüberschrift (Erledigt, Offen, Entscheidung nötig).

Beispiel für den Stil: "Diese Woche 5 Angebote raus, 2 davon schon mit Rückmeldung."

Wenn dir Informationen fehlen, frag nach, statt etwas zu erfinden.

Stichpunkte:
- 5 Angebote für Steuergehäuse verschickt (2x Kunde A, je 1x Kunde B, C, D)
- Kunde A: Auftrag über ca. 20.000 € bestätigt
- Kunde B wartet auf technische Rückmeldung zur Schutzart, Technik ist informiert
- Reklamation Kunde E (Lieferverzug): Rückruf erfolgt, neuer Liefertermin noch offen
- Messeprospekte: Daten an Druckerei noch nicht raus
- Frage an [VERTRIEBSLEITUNG]: Dürfen wir Kunde E einen Nachlass anbieten, und wenn ja, wie viel?
```

**Assistent 1**

> **Wochenbericht Vertrieb**
>
> Diese Woche 5 Angebote Steuergehäuse raus, davon 2x Kunde A, je 1x Kunde B, C und D. Kunde A hat einen Auftrag über ca. 20.000 € bestätigt.
>
> **Erledigt**
> - 5 Angebote Steuergehäuse verschickt
> - Auftrag Kunde A über ca. 20.000 € bestätigt
> - Rückruf an Kunde E wegen Lieferverzug erfolgt
>
> **Offen**
> - Kunde B wartet auf technische Rückmeldung zur Schutzart (Technik ist informiert)
> - Kunde E: neuer Liefertermin noch offen
> - Messeprospekte: Daten noch nicht an die Druckerei gegeben
>
> **Entscheidung nötig**
> - Dürfen wir Kunde E einen Nachlass anbieten, und wenn ja, in welcher Höhe?
>
> Zum Nachlass für Kunde E kann ich ohne Vorgaben keine Empfehlung geben, deshalb habe ich ihn bewusst nicht beziffert. Damit der Bericht vollständig wird, brauche ich noch: Gibt es eine Nachlassgrenze oder Freigaberegel? Bis wann soll Kunde B die Rückmeldung haben? Und bis wann müssen die Messeprospekte in der Druckerei sein?

### Sonnet

**Nutzer 1**

(identischer Prompt wie bei Haiku)

**Assistent 1**

> **Wochenbericht Vertriebsinnendienst**
>
> **Erledigt**
> - 5 Angebote für Steuergehäuse verschickt (2x Kunde A, je 1x Kunde B, C, D).
> - Kunde A hat einen Auftrag über ca. 20.000 € bestätigt.
> - Reklamation Kunde E (Lieferverzug): Rückruf ist erfolgt.
>
> **Offen**
> - Kunde B wartet auf die technische Rückmeldung zur Schutzart. Die Technik ist informiert.
> - Kunde E: Neuer Liefertermin steht noch aus.
> - Messeprospekte: Die Daten sind noch nicht an die Druckerei gegangen.
>
> **Entscheidung nötig**
> - Dürfen wir Kunde E einen Nachlass anbieten? Wenn ja, in welcher Höhe?
>
> ---
> Zwei Rückfragen, bevor du den Bericht abschickst. Ich habe bewusst nichts ergänzt:
> 1. Gibt es eine Frist für die Druckerei-Daten oder für die Entscheidung zu Kunde E? Wenn ja, trage ich sie ein.
> 2. Soll der Bericht mit dem Namen deiner Vertriebsleiterin beginnen? Der Platzhalter [VERTRIEBSLEITUNG] ist noch offen.

### Opus

**Nutzer 1**

(identischer Prompt wie bei Haiku)

**Assistent 1**

> Hier ist dein Wochenbericht:
>
> ---
>
> **Wochenbericht Vertriebsinnendienst**
>
> **Erledigt**
> - Diese Woche 5 Angebote für Steuergehäuse raus: 2x Kunde A, je 1x Kunde B, C und D.
> - Kunde A hat einen Auftrag über ca. 20.000 € bestätigt.
> - Reklamation Kunde E (Lieferverzug): Rückruf ist erfolgt.
>
> **Offen**
> - Kunde B wartet auf unsere technische Rückmeldung zur Schutzart. Die Technik ist informiert.
> - Kunde E: Der neue Liefertermin steht noch aus.
> - Messeprospekte: Die Daten sind noch nicht an die Druckerei raus.
>
> **Entscheidung nötig**
> - Dürfen wir Kunde E wegen des Lieferverzugs einen Nachlass anbieten? Wenn ja, wie viel?
>
> ---
>
> (ca. 85 Wörter)
>
> Zu ein paar Punkten fehlen mir Infos. Ich habe dazu nichts ergänzt:
>
> 1. **Kunde C und D:** Gibt es schon eine Rückmeldung, oder ist das noch offen? Dann würde ich beide unter „Offen“ aufnehmen.
> 2. **Kunde A:** Gilt der Auftrag für eines der beiden Angebote oder für beide? Wenn eines noch offen ist, sollte das in den Bericht.
> 3. **Kunde E:** Wie hoch ist der Auftragswert, und wie lange ist der Verzug? Damit kann deine Vertriebsleiterin den Nachlass leichter einschätzen.
> 4. **Messeprospekte:** Gibt es eine Frist bei der Druckerei? Wenn die bald abläuft, gehört das eher unter „Entscheidung nötig“ oder sollte als dringend markiert werden.
>
> Schick mir die Infos, dann passe ich den Bericht an.

---

Zurück zum [Übungsblatt Übung 2](../06_Uebungen/Uebung_2_Gute_Prompts.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md#übung-2-gute-prompts)
