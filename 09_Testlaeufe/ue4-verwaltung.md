# Testlauf: Übung 4 / Rolle Verwaltung – Antwortvorlage auf wiederkehrende Zahlungsanfragen

**Herkunft:** Übung 4 „Eigene Aufgabe“ aus [Uebung_4_Eigene_Aufgabe.md](../06_Uebungen/Uebung_4_Eigene_Aufgabe.md) (Block 6, 30 Minuten), Rolle Verwaltung / Buchhaltung (Ideenliste: „Standardantworten auf wiederkehrende Anfragen formulieren“). Prompt-Basis ist der Trainer-Musterprompt „Wiederkehrende Standardantwort (Verwaltung, Vertrieb)“ aus [Trainer-Loesungshinweise.md – Übung 4](../06_Uebungen/Trainer-Loesungshinweise.md#übung-4-eigene-aufgabe), ausgefüllt mit einem typischen Fall. Turn 4 ist der Iterationssatz aus Schritt 4 des Übungsblatts („Kürzer, bitte – maximal die Hälfte.“). Kein Anhang.

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf (jeweils neuer Chat, 4 Turns):**

1. Ausgefüllter Musterprompt: Sachbearbeiterin bei einem kleinen technischen Hersteller (ca. 80 MA). Lieferanten fragen, wann ihre Rechnung bezahlt wird. Regeln: Zahlung 30 Tage nach Rechnungseingang, Bearbeitung nur mit unserer Bestellnummer. Höchstens 100 Wörter, Sie-Form, Platzhalter in eckigen Klammern, vorher bis zu 3 Rückfragen.
2. Feste Antwort auf die Rückfragen: Die Mail geht an die Buchhaltung des Lieferanten, das Zahlungsziel ist immer 30 Tage ab Eingang, Unterschrift mit [MEIN NAME], Rechnungsprüfung.
3. „Gib mir noch eine zweite Variante für den Fall, dass die Rechnung ohne Bestellnummer kam …“
4. „Kürzer, bitte – maximal die Hälfte.“

**Was laut Material herauskommen soll:** Eine wiederverwendbare Standardantwort mit höchstens 100 Wörtern, in Sie-Form und mit Platzhaltern für alle variablen Teile, z. B. [LIEFERANT], [RECHNUNGSNUMMER], [RECHNUNGSDATUM], [EINGANGSDATUM], [ZAHLUNGSDATUM] und [MEIN NAME]. Die Regeln sollen korrekt drinstehen (30 Tage ab Eingang, Bestellnummer nötig), und es dürfen keine Beträge oder Daten erfunden werden. Dazu kommt eine Variante, die um eine Rechnung mit Bestellnummer bittet, und eine gekürzte Fassung mit etwa halber Länge, deren Kern erhalten bleibt. Mindestens zwei Iterationen. Daten-Ampel: grün, weil nur die Struktur beschrieben wird und keine echten Rechnungsdaten eingegeben werden.

---

## Bewertung

Wortzahlen per `python3` gezählt (Wörter mit Buchstaben/Ziffern, Platzhalter zählen als ein Wort, inkl. Betreff und Signatur, ohne Begleitkommentare der Modelle).

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Turn 1: höchstens 3 Rückfragen, kein vorschneller Text | ja, 3 Fragen. Aber geschlossene Ja/Nein-Fragen zum Format („Sollen Rechnungsnummer und Rechnungsdatum als Platzhalter …?“). Empfänger und Absender fragt Haiku nicht ab | ja, 3 Fragen: Empfänger, Ausnahmen beim Zahlungsziel (Skonto), Unterschrift | ja, 3 Fragen wie Sonnet, begründet und gut gegliedert |
| Turn 2: Länge Vorlage (höchstens 100) | 60 Wörter | 70 Wörter (selbst angegeben: „ca. 75“) | 74 Wörter (selbst angegeben: „rund 70“) |
| Sie-Form, Betreffzeile | ja, ja | ja, ja | ja, ja |
| Platzhalter | [RECHNUNGSNUMMER], [RECHNUNGSDATUM], [EINGANGSDATUM], [FÄLLIGKEITSDATUM], [BESTELLNUMMER], [MEIN NAME] | wie Haiku, aber [ZAHLUNGSDATUM] | wie Haiku, zusätzlich [FIRMENNAME]; erklärt, dass Fälligkeit = Eingang + 30 Tage |
| [LIEFERANT] / Ansprechpartner als Platzhalter | nein („Sehr geehrte Damen und Herren“, passt zu „an die Buchhaltung“) | nein (ebenso) | nein (ebenso) |
| Regel „30 Tage ab Eingang“ korrekt | ja | ja | ja |
| Regel „nur mit Bestellnummer“ sinnvoll eingebaut | **holprig**: „Bitte beachten Sie, dass wir Rechnungen nur mit unserer Bestellnummer bearbeiten. Die Bestellnummer lautet [BESTELLNUMMER].“ Im Fall „Rechnung liegt vor und läuft“ wirkt das wie eine Belehrung | ja, als Bitte für künftige Rückfragen | ja, als Bitte für künftige Rechnungen |
| Erfundene Beträge/Daten | nein | nein | nein |
| Turn 3: Variante ohne Bestellnummer, Länge | ja, 64 Wörter | ja, 77 Wörter | ja, 86 Wörter („rund 85“) |
| Turn 3: bittet um Rechnung mit [BESTELLNUMMER] | ja | ja | **anders gelöst**: „mit Bestellnummer“ ohne Platzhalter, dazu „Falls Ihnen die Nummer nicht vorliegt, erhalten Sie sie von [ANSPRECHPARTNER/ABTEILUNG]“ |
| Turn 3: Fristbeginn bei nachgereichter Rechnung | **legt sich still fest**: „Die Zahlungsfrist von 30 Tagen beginnt mit dem Rechnungseingang am [EINGANGSDATUM]“, also mit der ersten, unvollständigen Rechnung | lässt es offen („30 Tage ab Rechnungseingang“) und **weist darauf hin**, dass das geklärt werden muss | legt sich fest („ab Eingang der vollständigen Rechnung“) und **weist ausdrücklich auf die Annahme hin** |
| Turn 4: Länge (Anteil an Turn 3) | 38 Wörter = 59 % (Kerntext 27 von 53 = 51 %) | 45 Wörter = 58 % (Kerntext 34 von 65 = 52 %; selbst angegeben: „ca. 40“) | 43 Wörter = 50 % (Kerntext 32 von 73 = 44 %; selbst angegeben: „rund 40“) |
| Turn 4: Kern erhalten | ja (Bestellnummer fehlt, bitte neu senden). 30-Tage-Hinweis gestrichen, ist als Kürzung vertretbar | ja, inkl. 30 Tage („beginnt mit Eingang“, lässt den Fristbeginn wieder offen) | ja, inkl. 30 Tage. Aber „Die Zahlung erfolgt 30 Tage nach Eingang“ klingt wie eine feste Zusage, und der Hinweis auf die *vollständige* Rechnung ist weggefallen |
| Gesamturteil | brauchbar, sprachlich am einfachsten. Ein inhaltlicher Fallstrick beim Fristbeginn und ein holpriger Satz in Turn 2 | gut, sauber und kennzeichnet die offene Regel | sehr gut, am durchdachtesten (Firmenname, Ansprechpartner, Annahme offengelegt). Turn 3 ohne [BESTELLNUMMER]-Platzhalter, Turn 4 verliert eine Nuance |

**Daten-Ampel:** In allen drei Läufen grün. Eingegeben werden nur Zahlungsbedingungen, die Lieferanten ohnehin aus Bestellungen bzw. Einkaufsbedingungen kennen. Es gibt keine echten Lieferanten, Beträge oder Rechnungsnummern.

---

## Gefundene Fehler mit Beleg

1. **Haiku, Turn 3: Fristbeginn still festgelegt.** „Die Zahlungsfrist von 30 Tagen beginnt mit dem Rechnungseingang am [EINGANGSDATUM].“ Gemeint ist der Eingang der Rechnung *ohne* Bestellnummer, also der Rechnung, die laut Prompt gar nicht bearbeitet wird. Das wäre eine Zusage an den Lieferanten, die der Firmenregel wahrscheinlich widerspricht. Der Prompt sagt dazu nichts. Die Regel stammt also nicht aus der Quelle, Haiku hat sie sich ausgedacht. Sonnet („Bitte prüfen Sie, ob der Fristbeginn bei einer korrigierten Rechnung ab Eingang der neuen Rechnung gelten soll“) und Opus („Ich habe angenommen, dass die 30 Tage erst ab Eingang der korrigierten Rechnung laufen“) machen die Lücke dagegen sichtbar.
2. **Haiku, Turn 2: unlogischer Bestellnummer-Satz.** In der Vorlage für eine Rechnung, die schon in Bearbeitung ist, steht „Bitte beachten Sie, dass wir Rechnungen nur mit unserer Bestellnummer bearbeiten. Die Bestellnummer lautet [BESTELLNUMMER].“ Das klingt, als fehle die Nummer. Die Regel aus dem Prompt wird mechanisch eingebaut, statt sie an die Situation anzupassen. Kein Faktenfehler, aber für den Empfänger verwirrend.
3. **Haiku, Turn 1: Rückfragen am Bedarf vorbei.** Die Fragen betreffen das Format („Sollen … als Platzhalter …?“), nicht den fehlenden Kontext (Empfänger, Absender, Ausnahmen). Die festen Antworten in Turn 2 gehen deshalb an Haikus Fragen 1 und 3 vorbei. Haiku liefert trotzdem eine passende Vorlage. *Hinweis zum Testaufbau:* Turn 2 war fest vorgegeben und passt zu den Fragen von Sonnet und Opus. Im Kurs beantworten die Teilnehmenden die tatsächlichen Fragen.
4. **Opus, Turn 3: Platzhalter [BESTELLNUMMER] fehlt.** Das Kriterium im Material lautet: „bittet um Rechnung mit Bestellnummer [BESTELLNUMMER]“. Opus schreibt nur „mit Bestellnummer“ und verweist auf [ANSPRECHPARTNER/ABTEILUNG]. Das ist kein Fehler im eigentlichen Sinn, eher realistischer. Bei einer Rechnung ohne Bestellnummer weiß die Rechnungsprüfung oft selbst nicht, zu welcher Bestellung sie gehört. Es weicht aber vom Prüfkriterium ab.
5. **Opus, Turn 4: Nuance beim Kürzen verloren.** Aus „Das Zahlungsziel von 30 Tagen beginnt mit Eingang der vollständigen Rechnung“ wird „Die Zahlung erfolgt 30 Tage nach Eingang.“ Damit ist wieder unklar, welcher Eingang gemeint ist, und der Satz klingt wie eine Zusage. Typischer Kürzungsverlust.
6. **„Maximal die Hälfte“ knapp verfehlt (Haiku, Sonnet).** Haiku kommt auf 38 von 64 Wörtern (59 %), Sonnet auf 45 von 77 Wörtern (58 %). Nur Opus liegt mit 43 von 86 Wörtern bei 50 %. Zählt man nur den Kerntext ohne Betreff und Grußformel, liegen alle bei etwa der Hälfte (44–52 %). Das Kriterium „≈ halbe Länge“ ist damit erfüllt. Die eigenen Wortangaben der Modelle („ca. 40“, „rund 40“, „ca. 75“) sind nur grob richtig, Sonnets „ca. 40“ für 45 Wörter ist leicht geschönt.
7. **Kein Modell deckt den Fall „bereits überfällig“ ab.** Alle Vorlagen aus Turn 2 gehen davon aus, dass die Rechnung noch nicht fällig ist („erfolgt bis spätestens [ZAHLUNGSDATUM]“). Fragt ein Lieferant *nach* Ablauf der 30 Tage, passt die Vorlage nicht. Kein Modell hat das angesprochen. Danach wurde aber auch nicht gefragt.

Keine erfundenen Beträge, Daten oder Namen in allen drei Läufen.

---

## Lehren für die Auswertung

- **Die Übung funktioniert wie gedacht.** Alle drei Modelle stellen echte Rückfragen, halten Länge, Sie-Form und Platzhalter ein und liefern in vier Turns eine Vorlage, eine Variante und eine Kurzfassung. Das passt gut in die 20 Minuten für die Schritte 3 und 4. Zwei Iterationen kommen von selbst zustande.
- **Die stärkste Lehre ist der Fristbeginn.** Der Prompt enthält eine Regellücke: Ab wann laufen die 30 Tage, wenn die Rechnung nachgereicht wird? Ein Modell füllt die Lücke stillschweigend (Haiku: ab dem ersten Eingang), zwei machen sie sichtbar. Für den Trainer: „Woher weiß der KI-Assistent eure Regel? Gar nicht, er rät.“ Den Satz in der Vorlage also gegen die echte Firmenregel prüfen, bevor die Vorlage an Lieferanten geht. Das passt direkt zum Kriterium „Risiken: falsche Zusagen“ im Bewertungsraster.
- **Rückfragen sind unterschiedlich gut.** Sonnet und Opus fragen nach Empfänger, Ausnahmen und Absender, also nach Kontext, den nur der Mensch kennt. Haiku fragt nach Format-Details. Gute Diskussionsfrage: „Welche Rückfrage hat euch wirklich weitergebracht?“
- **Kürzen kostet Nuancen.** Beim Halbieren verschwinden Höflichkeiten (harmlos), aber auch Präzisierungen wie „vollständige Rechnung“ (nicht harmlos). Nach jeder Kürzung den Kernsatz noch einmal gegen die Regel lesen.
- **Selbstangaben zur Wortzahl nicht blind glauben.** Sie stimmen ungefähr, aber nicht genau. Bei harten Grenzen selbst zählen (Word-Statistik).
- **Vorlage ≠ alle Fälle.** Eine Standardantwort deckt nur den Fall ab, den man beschrieben hat. Gute Zusatzaufgabe für Schnelle: „Gib mir eine dritte Variante für eine Rechnung, die bereits überfällig ist.“
- **Gutes Beispiel für die 2-Minuten-Vorstellung:** Die Vorlagen der Modelle nebeneinander zeigen, vor allem die drei Lösungen zum Fristbeginn.

---

## Gesprächsprotokoll: Haiku

### Nutzer 1

```text
Du bist Sachbearbeiterin in der Verwaltung eines kleinen technischen Herstellers mit ca. 80 Mitarbeitenden.
Wir bekommen immer wieder Anfragen dieser Art: Lieferanten fragen per Mail nach, wann ihre Rechnung bezahlt wird, weil die Zahlung noch nicht eingegangen ist. Bei uns gilt: Zahlung 30 Tage nach Rechnungseingang, und Rechnungen werden nur mit unserer Bestellnummer bearbeitet.
Schreib mir eine Antwortvorlage, die ich jedes Mal anpassen kann.
Format: max. 100 Wörter, Sie-Form, Platzhalter in eckigen Klammern für alles, was sich ändert.
Stell mir zuerst bis zu 3 Rückfragen, wenn dir etwas fehlt.
```

### Assistent 1

Ich helfe Ihnen gern. Damit die Vorlage passt, habe ich drei Rückfragen:

1. Sollen Rechnungsnummer und Rechnungsdatum als Platzhalter in die Vorlage, damit Sie sie bei jeder Anfrage eintragen können?
2. Soll die Vorlage das konkrete Fälligkeitsdatum nennen (Rechnungseingang plus 30 Tage), oder reicht der allgemeine Hinweis auf das Zahlungsziel?
3. Soll die Vorlage auch den Fall abdecken, dass eine Rechnung ohne Bestellnummer eingegangen ist, oder brauchen Sie dafür eine separate Variante?

### Nutzer 2

```text
Zu deinen Rückfragen: Die Vorlage geht an die Buchhaltung des Lieferanten, das Zahlungsziel ist immer 30 Tage ab Rechnungseingang, ich unterschreibe mit [MEIN NAME], Rechnungsprüfung. Bitte schreib jetzt die Vorlage.
```

### Assistent 2

Betreff: Zahlungsstatus Rechnung [RECHNUNGSNUMMER]

Sehr geehrte Damen und Herren,

vielen Dank für Ihre Nachricht. Die Rechnung [RECHNUNGSNUMMER] vom [RECHNUNGSDATUM] ist bei uns am [EINGANGSDATUM] eingegangen. Unser Zahlungsziel beträgt 30 Tage ab Rechnungseingang, die Zahlung erfolgt somit spätestens am [FÄLLIGKEITSDATUM].

Bitte beachten Sie, dass wir Rechnungen nur mit unserer Bestellnummer bearbeiten. Die Bestellnummer lautet [BESTELLNUMMER].

Mit freundlichen Grüßen
[MEIN NAME]
Rechnungsprüfung

### Nutzer 3

```text
Gib mir noch eine zweite Variante für den Fall, dass die Rechnung ohne Bestellnummer kam und deshalb noch nicht bearbeitet wurde.
```

### Assistent 3

Betreff: Rechnung [RECHNUNGSNUMMER], Bestellnummer erforderlich

Sehr geehrte Damen und Herren,

vielen Dank für Ihre Nachricht. Die Rechnung [RECHNUNGSNUMMER] vom [RECHNUNGSDATUM] ist bei uns eingegangen, konnte jedoch noch nicht bearbeitet werden, da sie keine Bestellnummer enthält.

Bitte senden Sie uns die Rechnung mit der Bestellnummer [BESTELLNUMMER] erneut zu. Die Zahlungsfrist von 30 Tagen beginnt mit dem Rechnungseingang am [EINGANGSDATUM].

Mit freundlichen Grüßen
[MEIN NAME]
Rechnungsprüfung

### Nutzer 4

```text
Kürzer, bitte – maximal die Hälfte.
```

### Assistent 4

Betreff: Rechnung [RECHNUNGSNUMMER], Bestellnummer fehlt

Sehr geehrte Damen und Herren,

Ihre Rechnung [RECHNUNGSNUMMER] enthält keine Bestellnummer und wurde daher noch nicht bearbeitet. Bitte senden Sie sie mit der Bestellnummer [BESTELLNUMMER] erneut zu.

Mit freundlichen Grüßen
[MEIN NAME], Rechnungsprüfung

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1

```text
Du bist Sachbearbeiterin in der Verwaltung eines kleinen technischen Herstellers mit ca. 80 Mitarbeitenden.
Wir bekommen immer wieder Anfragen dieser Art: Lieferanten fragen per Mail nach, wann ihre Rechnung bezahlt wird, weil die Zahlung noch nicht eingegangen ist. Bei uns gilt: Zahlung 30 Tage nach Rechnungseingang, und Rechnungen werden nur mit unserer Bestellnummer bearbeitet.
Schreib mir eine Antwortvorlage, die ich jedes Mal anpassen kann.
Format: max. 100 Wörter, Sie-Form, Platzhalter in eckigen Klammern für alles, was sich ändert.
Stell mir zuerst bis zu 3 Rückfragen, wenn dir etwas fehlt.
```

### Assistent 1

Gern. Bevor ich die Vorlage schreibe, drei kurze Rückfragen:

1. An wen geht die Mail? Geht sie an die Buchhaltung des Lieferanten oder an einen Ansprechpartner im Einkauf oder Vertrieb? Davon hängen Anrede und Ton ab.
2. Gilt das Zahlungsziel von 30 Tagen immer ab Rechnungseingang, oder gibt es Ausnahmen, etwa Skonto oder abweichende Vereinbarungen?
3. Wie soll die Mail unterschrieben werden? Mit Name, Abteilung, Telefonnummer?

### Nutzer 2

```text
Zu deinen Rückfragen: Die Vorlage geht an die Buchhaltung des Lieferanten, das Zahlungsziel ist immer 30 Tage ab Rechnungseingang, ich unterschreibe mit [MEIN NAME], Rechnungsprüfung. Bitte schreib jetzt die Vorlage.
```

### Assistent 2

**Betreff:** Ihre Rechnung [RECHNUNGSNUMMER] – Zahlungsstatus

Sehr geehrte Damen und Herren,

vielen Dank für Ihre Nachricht zur Rechnung [RECHNUNGSNUMMER] vom [RECHNUNGSDATUM]. Sie ist am [EINGANGSDATUM] bei uns eingegangen und wird unter unserer Bestellnummer [BESTELLNUMMER] geführt.

Unser Zahlungsziel beträgt 30 Tage ab Rechnungseingang. Die Zahlung erfolgt daher bis spätestens [ZAHLUNGSDATUM]. Wir bitten Sie um etwas Geduld.

Bei weiteren Fragen nennen Sie uns bitte immer unsere Bestellnummer.

Mit freundlichen Grüßen
[MEIN NAME]
Rechnungsprüfung

(ca. 75 Wörter)

### Nutzer 3

```text
Gib mir noch eine zweite Variante für den Fall, dass die Rechnung ohne Bestellnummer kam und deshalb noch nicht bearbeitet wurde.
```

### Assistent 3

**Betreff:** Ihre Rechnung [RECHNUNGSNUMMER] – Bestellnummer fehlt

Sehr geehrte Damen und Herren,

vielen Dank für Ihre Nachricht. Ihre Rechnung [RECHNUNGSNUMMER] vom [RECHNUNGSDATUM] ist am [EINGANGSDATUM] bei uns eingegangen, enthält aber keine Bestellnummer. Rechnungen können wir nur mit unserer Bestellnummer bearbeiten, daher wurde sie noch nicht verarbeitet.

Bitte senden Sie uns die Rechnung mit der Bestellnummer [BESTELLNUMMER] erneut zu. Sobald sie vorliegt, bearbeiten wir sie umgehend. Das Zahlungsziel beträgt 30 Tage ab Rechnungseingang.

Mit freundlichen Grüßen
[MEIN NAME]
Rechnungsprüfung

Hinweis: Bitte prüfen Sie, ob der Fristbeginn bei einer korrigierten Rechnung ab Eingang der neuen Rechnung gelten soll. Das habe ich bewusst offen formuliert.

### Nutzer 4

```text
Kürzer, bitte – maximal die Hälfte.
```

### Assistent 4

**Betreff:** Rechnung [RECHNUNGSNUMMER] – Bestellnummer fehlt

Sehr geehrte Damen und Herren,

Ihre Rechnung [RECHNUNGSNUMMER] enthält keine Bestellnummer und wurde daher nicht bearbeitet. Bitte senden Sie sie mit der Bestellnummer [BESTELLNUMMER] erneut zu. Das Zahlungsziel von 30 Tagen beginnt mit Eingang.

Mit freundlichen Grüßen
[MEIN NAME]
Rechnungsprüfung

(ca. 40 Wörter)

---

## Gesprächsprotokoll: Opus

### Nutzer 1

```text
Du bist Sachbearbeiterin in der Verwaltung eines kleinen technischen Herstellers mit ca. 80 Mitarbeitenden.
Wir bekommen immer wieder Anfragen dieser Art: Lieferanten fragen per Mail nach, wann ihre Rechnung bezahlt wird, weil die Zahlung noch nicht eingegangen ist. Bei uns gilt: Zahlung 30 Tage nach Rechnungseingang, und Rechnungen werden nur mit unserer Bestellnummer bearbeitet.
Schreib mir eine Antwortvorlage, die ich jedes Mal anpassen kann.
Format: max. 100 Wörter, Sie-Form, Platzhalter in eckigen Klammern für alles, was sich ändert.
Stell mir zuerst bis zu 3 Rückfragen, wenn dir etwas fehlt.
```

### Assistent 1

Gern. Bevor ich die Vorlage schreibe, habe ich drei Fragen:

1. **Empfänger:** Geht die Antwort meist an die Buchhaltung des Lieferanten oder an Ihre direkten Ansprechpartner (z. B. Vertrieb)? Davon hängt ab, wie förmlich und wie ausführlich ich schreibe.
2. **Zahlungsziel:** Gilt immer „30 Tage ab Rechnungseingang“, oder gibt es Ausnahmen wie Skonto oder abweichende Vereinbarungen mit einzelnen Lieferanten? Die könnte ich dann als Platzhalter einbauen.
3. **Absender:** Mit welchem Namen und welcher Funktion bzw. Abteilung soll die Mail unterschrieben werden?

### Nutzer 2

```text
Zu deinen Rückfragen: Die Vorlage geht an die Buchhaltung des Lieferanten, das Zahlungsziel ist immer 30 Tage ab Rechnungseingang, ich unterschreibe mit [MEIN NAME], Rechnungsprüfung. Bitte schreib jetzt die Vorlage.
```

### Assistent 2

Hier ist Ihre Vorlage:

> **Betreff:** Ihre Rechnung [RECHNUNGSNUMMER] vom [RECHNUNGSDATUM]
>
> Sehr geehrte Damen und Herren,
>
> vielen Dank für Ihre Nachfrage. Ihre Rechnung [RECHNUNGSNUMMER] zu unserer Bestellung [BESTELLNUMMER] ist am [EINGANGSDATUM] bei uns eingegangen. Gemäß unserem Zahlungsziel von 30 Tagen ab Rechnungseingang erfolgt die Zahlung bis zum [FÄLLIGKEITSDATUM].
>
> Bitte geben Sie auch künftig stets unsere Bestellnummer an, da wir Rechnungen nur damit bearbeiten können.
>
> Für Rückfragen stehe ich Ihnen gern zur Verfügung.
>
> Mit freundlichen Grüßen
>
> [MEIN NAME]
> Rechnungsprüfung
> [FIRMENNAME]

Die Vorlage hat rund 70 Wörter. Das [FÄLLIGKEITSDATUM] ist einfach das [EINGANGSDATUM] plus 30 Tage.

### Nutzer 3

```text
Gib mir noch eine zweite Variante für den Fall, dass die Rechnung ohne Bestellnummer kam und deshalb noch nicht bearbeitet wurde.
```

### Assistent 3

Gern, hier die Variante für Rechnungen ohne Bestellnummer:

> **Betreff:** Ihre Rechnung [RECHNUNGSNUMMER] – Bestellnummer fehlt
>
> Sehr geehrte Damen und Herren,
>
> vielen Dank für Ihre Nachfrage. Ihre Rechnung [RECHNUNGSNUMMER] vom [RECHNUNGSDATUM] ist am [EINGANGSDATUM] bei uns eingegangen, enthält jedoch keine Bestellnummer. Da wir Rechnungen nur mit unserer Bestellnummer bearbeiten können, konnten wir die Zahlung noch nicht veranlassen.
>
> Bitte senden Sie uns die Rechnung mit Bestellnummer erneut zu. Falls Ihnen die Nummer nicht vorliegt, erhalten Sie sie von [ANSPRECHPARTNER/ABTEILUNG]. Das Zahlungsziel von 30 Tagen beginnt mit Eingang der vollständigen Rechnung.
>
> Mit freundlichen Grüßen
>
> [MEIN NAME]
> Rechnungsprüfung
> [FIRMENNAME]

Rund 85 Wörter. Bitte prüfen Sie noch einen Punkt: Ich habe angenommen, dass die 30 Tage erst ab Eingang der korrigierten Rechnung laufen. Wenn das bei Ihnen anders geregelt ist, passen Sie den letzten Satz an oder streichen ihn.

### Nutzer 4

```text
Kürzer, bitte – maximal die Hälfte.
```

### Assistent 4

Hier die gekürzte Fassung (rund 40 Wörter):

> **Betreff:** Rechnung [RECHNUNGSNUMMER] – Bestellnummer fehlt
>
> Sehr geehrte Damen und Herren,
>
> Ihrer Rechnung [RECHNUNGSNUMMER] fehlt unsere Bestellnummer, daher konnten wir sie noch nicht bearbeiten. Bitte senden Sie sie mit Bestellnummer erneut. Die Zahlung erfolgt 30 Tage nach Eingang.
>
> Mit freundlichen Grüßen
>
> [MEIN NAME]
> Rechnungsprüfung

---

Zurück zum Übungsblatt: [Uebung_4_Eigene_Aufgabe.md](../06_Uebungen/Uebung_4_Eigene_Aufgabe.md) · Lösungshinweise: [Trainer-Loesungshinweise.md – Übung 4](../06_Uebungen/Trainer-Loesungshinweise.md#übung-4-eigene-aufgabe)
