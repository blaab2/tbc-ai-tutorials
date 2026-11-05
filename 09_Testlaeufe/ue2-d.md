# Testlauf: Übung 2 / Weiter D – Schritt für Schritt nachschärfen

**Herkunft:** [Uebung_2_Gute_Prompts.md, Aufgabe D](../06_Uebungen/Uebung_2_Gute_Prompts.md) · Abgleich mit [Trainer-Lösungshinweise, Übung 2](../06_Uebungen/Trainer-Loesungshinweise.md) · Prompt-Baukasten: [Spickzettel](../05_Spickzettel.md)

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf des Tests:** Turn 1 = Baukasten-Prompt aus Aufgabe B. Turns 2–5 = **alle vier** Nachschärfungen aus Aufgabe D in der Reihenfolge des Übungsblatts, alles im selben Chat. (Das Blatt verlangt „mindestens zwei“ – im Test wurden alle vier gemacht, um jede einzeln bewerten zu können.)

**Ziel laut Material:** Das Ergebnis wird mit jeder Rückmeldung gezielt besser, ohne dass der Rest „zerfällt“: kürzer, Feedbackgespräch am Freitag + Spalte „Erledigt“, lockerere Willkommensnachricht, 3 sinnvolle Ergänzungsvorschläge.

**Soll (objektiv prüfbar):** Alle Turns im selben Chat · Turn 2: Plan spürbar kürzer (≈ halbe Seite), Spalten erhalten · Turn 3: Freitag enthält Feedbackgespräch, neue Spalte „Erledigt“ (z. B. ☐), übrige Spalten/Platzhalter bleiben · Turn 4: Nachricht lockerer, weiterhin ≤ 80 Wörter, Du-Form · Turn 5: genau 3 Punkte (z. B. Pate/Buddy, IT-Zugänge vorab, PSA/Arbeitskleidung, Notfall-/Brandschutz, Pausenregelung) · keine erfundenen Namen.

## Bewertung

Gezählt per python3 (Platzhalter in eckigen Klammern = 1 Wort, Anrede und Gruß mitgezählt; Tabellen: nur Zelleninhalt ohne Kopfzeile).

| Messwert | Haiku | Sonnet | Opus |
|---|---|---|---|
| Willkommensnachricht Turn 1 | 55 Wörter | 70 Wörter | 70 Wörter |
| Willkommensnachricht Turn 4 | 46 Wörter | 63 Wörter | 67 Wörter |
| Plan Turn 1 → Turn 2 | 51 → 37 Wörter (−27 %) | 65 → 33 Wörter (−49 %) | 98 → 37 Wörter (−62 %) |

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Turn 1: Tabelle mit 4 Spalten, Platzhalter statt Namen | ja | ja | ja (plus unverlangter „Tipp“ zum Paten) |
| Turn 2: Plan spürbar kürzer, Spalten erhalten | ja, aber nur mäßig – der Plan war schon kurz, gekürzt wurde v. a. „Montag“ → „Mo“ | ja, deutlich | ja, sehr deutlich |
| Turn 2: nichts Wichtiges verloren | ja | ja (Stapler-Beauftragte/r fällt als Ansprechperson weg) | teilweise – [NAME TEAMLEITUNG] verschwindet am Freitag, Produktion-Ansprechperson am Donnerstag |
| Turn 3: Spalte „Erledigt“ mit ☐ | ja | ja | ja |
| Turn 3: Feedbackgespräch am Freitag | ja (ca. 20 Min.) | ja (ca. 30 Min.) | ja (14:30 Uhr, ca. 30 Min., plus 3 Leitfragen) |
| Turn 3: Rest bleibt erhalten | teilweise – „Wochenrückblick“ wurde durch das Feedbackgespräch **ersetzt** statt ergänzt | ja („Wochenrückblick, Feedbackgespräch“) | ja, [NAME TEAMLEITUNG] kommt am Freitag wieder dazu |
| Turn 4: spürbar lockerer, Du-Form | ja („Hey“, „Mach dir keinen Stress“) | ja („ich hol dich“, „wie bei uns der Hase läuft“) | ja („mit anpackst“, „ruf einfach durch“) |
| Turn 4: ≤ 80 Wörter | ja | ja | ja |
| Turn 4: keine neuen Fakten | ja | nein – Treffpunkt „vorne am Empfang“ und „ich hol dich ab“ (schon in Turn 1 erfunden) | nein – „Arbeitsschuhe hast du“, Treffpunkt Empfang |
| Turn 5: genau 3 Punkte | formal ja, Punkt 3 bündelt aber zwei Themen (Ziele Woche 2 + Zeiterfassung/Pausen/Krankmeldung) | ja | nein – 3 Punkte **plus „Bonus“** (zweites Feedbackgespräch nach 4–6 Wochen) |
| Turn 5: Punkte sinnvoll, passen zum Lager | ja (PSA/Unterweisung dokumentieren, Pate, Ziele Woche 2) | ja (Pate, Vorbereitung vor Tag 1, soziale Einbindung) | ja (Vorbereitung vor Tag 1, Pate mit freigeplanter Zeit, ungeschriebene Regeln) – am praxisnächsten |
| Keine erfundenen Personennamen | ja | ja | ja |

**Gesamturteil:** Die Übung funktioniert bei allen drei Modellen wie gedacht: Jede Rückmeldung wird gezielt umgesetzt, die Tabelle bleibt stabil, Platzhalter bleiben Platzhalter. Kein Modell nennt erfundene Namen. Die Unterschiede sind klein, aber gut für die Auswertung zu gebrauchen: Haiku liefert schon in Turn 1 einen knappen Plan, darum bringt „Kürzer bitte“ dort wenig. Dafür ersetzt Haiku in Turn 3 den Wochenrückblick, statt das Feedbackgespräch dazuzuschreiben. Sonnet arbeitet am saubersten. Opus liefert die reichhaltigsten Inhalte, verliert beim Kürzen aber Ansprechpersonen, erfindet in der lockeren Nachricht ein Detail und hält sich bei „3 Punkte“ nicht an die Zahl.

## Gefundene Fehler mit Beleg

1. **Opus, Turn 4 – erfundene Tatsache.** „Arbeitsschuhe hast du, den Rest kriegst du von uns.“ Im Kontext steht nichts über Arbeitsschuhe. Das widerspricht außerdem Opus' eigener Empfehlung in Turn 5 („Arbeitskleidung und PSA in der richtigen Größe sollten schon am Montag um 7 Uhr bereitliegen“). Wer die Nachricht ungeprüft verschickt, sagt dem neuen Kollegen womöglich etwas Falsches.
2. **Sonnet und Opus, Turn 1 und 4 – erfundener Treffpunkt.** Sonnet: „ich nehme dich am Empfang in Empfang“ bzw. „ich hol dich vorne am Empfang ab“. Opus: „Am Montag um 7 Uhr holen wir dich am Empfang ab“. Der Prompt nennt nur die Arbeitszeit (7 bis 15:30 Uhr), keinen Treffpunkt. Das ist plausibel, aber geraten. Hier passt der Satz aus dem Material „Was du nicht sagst, wird geraten.“
3. **Sonnet, Turn 1 – sprachlicher Fehler.** „ich nehme dich am Empfang in Empfang“ (doppeltes „Empfang“). In Turn 4 ist der Satz verschwunden.
4. **Haiku, Turn 3 – Inhalt ersetzt statt ergänzt.** In Turn 2 steht am Freitagnachmittag „Wochenrückblick“, in Turn 3 nur noch „Kurzes Feedbackgespräch (ca. 20 Min.)“. Inhaltlich vertretbar, weil sich beides überschneidet, aber genau das „Zerfallen“, auf das die Übung achten soll: Die KI ändert nebenbei etwas, das nicht verlangt war.
5. **Opus, Turn 2 – Ansprechpersonen verloren.** Turn 1, Freitag: „[NAME PATE/PATIN], [NAME TEAMLEITUNG]“, Donnerstag: „[NAME SICHERHEITSFACHKRAFT], [NAME ANSPRECHPERSON PRODUKTION]“. In Turn 2 steht jeweils nur noch eine Person, obwohl am Donnerstag weiterhin „Schnittstellen Produktion/Einkauf“ eingeplant ist. In Turn 3 wird die Teamleitung am Freitag wieder ergänzt, die Produktion bleibt weg. Außerdem werden Platzhalter umbenannt ([NAME KOLLEGE WARENEINGANG] → [NAME WARENEINGANG]).
6. **Opus, Turn 5 – mehr als 3 Punkte.** Nach den drei Punkten folgt „**Bonus:** Plane gleich ein zweites Feedbackgespräch nach ca. 4–6 Wochen ein.“ Ähnlich Haiku, Punkt 3: Er enthält zwei getrennte Themen („Klare Ziele für Woche 2“ und „Zeiterfassung, Pausenregelung und Krankmeldeweg“). Mengenvorgaben werden also eher locker ausgelegt.
7. **Kein Fehler, aber auffällig:** In Turn 2 liefern alle drei Modelle **nur** den Plan, ohne die Willkommensnachricht. Das ist richtig verstanden („der Plan soll …“). Teilnehmende könnten aber denken, die Nachricht sei „weg“. Sie steht weiter oben im Chat, und Turn 4 greift sie auch korrekt wieder auf.

Keine Zahlenfehler: Alle Nachrichten bleiben unter 80 Wörtern, die Uhrzeit 14:30 Uhr + 30 Min. (Opus) liegt innerhalb der Arbeitszeit bis 15:30 Uhr.

## Lehren für die Auswertung

- **Nachschärfen funktioniert zuverlässig.** Bei allen drei Modellen wird jede Rückmeldung umgesetzt, ohne dass man neu anfangen muss. Das ist die Kernbotschaft der Aufgabe („Ein Gespräch mit zwei, drei Rückmeldungen ist ganz normal“).
- **Nach jeder Änderung prüfen, was sich *nebenbei* geändert hat.** Gute Beispiele aus dem Test: Haiku streicht den Wochenrückblick, Opus verliert beim Kürzen Ansprechpersonen. Die Leitfrage für die Teilnehmenden: „Was hat die KI verändert, worum ich nicht gebeten habe?“
- **„Lockerer“ verleitet zum Ausschmücken.** Wer die KI bittet, „wie unter Kollegen“ zu schreiben, bekommt oft kleine konkrete Details dazu (Treffpunkt Empfang, „Arbeitsschuhe hast du“). Die klingen echt, sind aber geraten. Vor dem Versenden muss man sie prüfen oder streichen.
- **„Kürzer“ wirkt unterschiedlich stark.** Wie viel gekürzt wird, hängt davon ab, wie lang die erste Fassung war (Haiku −27 %, Opus −62 %). Wer schon einen knappen Plan hatte, sieht kaum einen Unterschied. Das ist kein Fehler.
- **„Was fehlt noch?“ ist die wertvollste Nachschärfung.** Alle drei Modelle nennen sinnvolle Punkte, die im Plan fehlen (Pate/Buddy, Vorbereitung vor Tag 1 mit PSA und Zugängen, Pausen/Zeiterfassung/Krankmeldung). Die KI dient hier als Checkliste. Gut zeigen kann man auch: Die Punkte passen gut zueinander, Opus' Punkt 1 widerspricht aber der eigenen Nachricht aus Turn 4.
- **Mengenangaben werden locker ausgelegt.** „Nenne 3 Punkte“ ergibt bei Opus 3 + Bonus. Wenn die Zahl wichtig ist, muss man sie klar verlangen („genau 3, nicht mehr“).

## Probleme im Material

- **Lösungshinweise zu Aufgabe D sind sehr knapp.** Dort steht nur ein Satz („Das Ergebnis wird mit jeder Rückmeldung gezielt besser, ohne dass der Rest ‚zerfällt‘“). Woran der Trainer das „Zerfallen“ erkennt, steht nicht da. Die Testläufe zeigen typische Muster, die man konkret nennen kann.
- **Dem Übungsblatt fehlt ein Beobachtungsauftrag.** Aufgabe C hat ein „**Beobachte:**“, Aufgabe D nicht. Ohne diesen Hinweis prüfen Teilnehmende vermutlich nur, ob die gewünschte Änderung da ist, und nicht, was nebenbei verloren ging oder dazukam.
- **Zeit:** 5 Minuten für „C **oder** D“ reichen für zwei Nachschärfungen gut aus. Alle vier schaffen nur Schnelle; das Blatt sagt aber richtig „mindestens zwei“.
- Kleinigkeit: Die Prompt-Kästen enthalten harte Zeilenumbrüche mitten im Satz („Spalte⏎"Erledigt"“). Das ist beim Kopieren harmlos, die Modelle stört es nicht.

## Korrekturvorschlag

1. **`06_Uebungen/Uebung_2_Gute_Prompts.md`, Aufgabe D**, direkt vor dem „> **Merke:**“-Kasten einfügen:
   > **Beobachte:** Prüfe nach jeder Rückmeldung zwei Dinge: Wurde deine Änderung umgesetzt? Und hat die KI nebenbei etwas gestrichen oder dazugedichtet, um das du nicht gebeten hast (z. B. eine Ansprechperson, einen Treffpunkt, eine Uhrzeit)?
2. **`06_Uebungen/Trainer-Loesungshinweise.md`, Abschnitt „Woran du ein gutes Ergebnis erkennst“**, den Punkt zu Aufgabe D ergänzen:
   > - **Aufgabe D:** Das Ergebnis wird mit jeder Rückmeldung gezielt besser, ohne dass der Rest „zerfällt“. Typisch im Test: „Kürzer“ wirkt je nach Ausgangslänge stark oder kaum; beim Ergänzen wird gelegentlich etwas ersetzt statt ergänzt (z. B. „Wochenrückblick“ verschwindet) oder es gehen Ansprechpersonen verloren; die „lockere“ Nachricht enthält oft geratene Details (Treffpunkt Empfang, „Arbeitsschuhe hast du“); bei „3 Punkte“ kommt manchmal ein vierter als „Bonus“. Gute Ergänzungsvorschläge: Pate/Buddy, Zugänge und PSA vor Tag 1 bereitlegen, Pausen/Zeiterfassung/Krankmeldung klären, soziale Einbindung, Ziele für Woche 2.
3. Optional in **Typische Stolpersteine**: „Bei D wundern sich manche, dass nach ‚Kürzer bitte‘ die Willkommensnachricht fehlt – sie steht weiter oben im Chat, die KI hat nur den Plan neu ausgegeben.“

---

## Gesprächsprotokoll: Haiku

### Nutzer 1
Du bist eine erfahrene Teamleiterin in einem kleinen technischen Herstellerbetrieb.

Kontext: Wir sind die Nordlicht Technik GmbH, ca. 80 Mitarbeitende. Am Montag fängt ein neuer Kollege im Lager an. Er hat schon Erfahrung in der Lagerlogistik, kennt aber unsere Abläufe und Systeme noch nicht. Arbeitszeit: Montag bis Freitag, 7 bis 15:30 Uhr.

Aufgabe: Erstelle
1. eine kurze, herzliche Willkommensnachricht an ihn (höchstens 80 Wörter, wir duzen uns),
2. einen Einarbeitungsplan für seine erste Woche.

Format: Den Plan als Tabelle mit den Spalten Tag | Vormittag | Nachmittag | Ansprechperson. Für Namen setze Platzhalter wie [NAME TEAMLEITUNG].

Beispiel für eine Tabellenzeile:
Montag | Begrüßung, Rundgang, Arbeitssicherheit | Arbeitsplatz einrichten, Zugänge testen | [NAME TEAMLEITUNG]

### Assistent 1
**Willkommensnachricht**

Hallo [NAME NEUER KOLLEGE], herzlich willkommen bei der Nordlicht Technik GmbH! Schön, dass du am Montag im Lager anfängst. Du bringst schon viel Erfahrung mit, unsere Abläufe und Systeme lernst du in den ersten Tagen Schritt für Schritt kennen. Frag einfach, wenn etwas unklar ist, dafür sind wir da. Wir freuen uns auf dich!

Bis Montag, [NAME TEAMLEITUNG]

**Einarbeitungsplan – erste Woche**

| Tag | Vormittag | Nachmittag | Ansprechperson |
|---|---|---|---|
| Montag | Begrüßung, Rundgang, Arbeitssicherheit | Arbeitsplatz einrichten, Zugänge testen (Lagersystem, Scanner) | [NAME TEAMLEITUNG] |
| Dienstag | Wareneingang begleiten, Prozesse verstehen | Wareneingang unter Anleitung selbst bearbeiten | [NAME WARENEINGANG] |
| Mittwoch | Kommissionierung und Versand kennenlernen | Kommissionierung unter Anleitung | [NAME KOMMISSIONIERUNG] |
| Donnerstag | Bestandsführung und Inventur im System | Kleinere Aufgaben selbstständig, mit Rückfragen | [NAME TEAMLEITUNG] |
| Freitag | Offene Fragen klären, eigenständige Aufgaben | Wochenrückblick | [NAME TEAMLEITUNG] |

### Nutzer 2
Kürzer bitte – der Plan soll auf eine halbe Seite passen.

### Assistent 2
| Tag | Vormittag | Nachmittag | Ansprechperson |
|---|---|---|---|
| Mo | Begrüßung, Rundgang, Arbeitssicherheit | Arbeitsplatz, Zugänge | [NAME TEAMLEITUNG] |
| Di | Wareneingang begleiten | Wareneingang unter Anleitung | [NAME WARENEINGANG] |
| Mi | Kommissionierung und Versand | Kommissionierung unter Anleitung | [NAME KOMMISSIONIERUNG] |
| Do | Bestandsführung im System | Kleinere Aufgaben, mit Rückfragen | [NAME TEAMLEITUNG] |
| Fr | Offene Fragen klären | Wochenrückblick | [NAME TEAMLEITUNG] |

### Nutzer 3
Ergänze am Freitag ein kurzes Feedbackgespräch und eine Spalte "Erledigt" zum Abhaken.

### Assistent 3
| Tag | Vormittag | Nachmittag | Ansprechperson | Erledigt |
|---|---|---|---|---|
| Mo | Begrüßung, Rundgang, Arbeitssicherheit | Arbeitsplatz, Zugänge | [NAME TEAMLEITUNG] | ☐ |
| Di | Wareneingang begleiten | Wareneingang unter Anleitung | [NAME WARENEINGANG] | ☐ |
| Mi | Kommissionierung und Versand | Kommissionierung unter Anleitung | [NAME KOMMISSIONIERUNG] | ☐ |
| Do | Bestandsführung im System | Kleinere Aufgaben, mit Rückfragen | [NAME TEAMLEITUNG] | ☐ |
| Fr | Offene Fragen klären | Kurzes Feedbackgespräch (ca. 20 Min.) | [NAME TEAMLEITUNG] | ☐ |

### Nutzer 4
Die Willkommensnachricht klingt zu förmlich. Schreib sie so, wie man einem Kollegen im Lager schreibt.

### Assistent 4
Hey [NAME NEUER KOLLEGE], willkommen im Team! Schön, dass du ab Montag bei uns im Lager anfängst. Du bringst ja schon einiges mit, den Rest zeigen wir dir Schritt für Schritt. Mach dir keinen Stress, wenn am Anfang nicht alles sofort sitzt, frag einfach nach.

Bis Montag!
[NAME TEAMLEITUNG]

### Nutzer 5
Was fehlt in diesem Plan noch? Nenne mir 3 Punkte, die erfahrene Teamleitungen oft vergessen.

### Assistent 5
1. **Sicherheit und Ausstattung vor der ersten Schicht:** Schutzausrüstung (Sicherheitsschuhe, Handschuhe), Stapler- oder Geräteberechtigungen und die Unterweisungen sollten schriftlich dokumentiert und unterschrieben werden, bevor er allein arbeitet.
2. **Eine feste Ansprechperson im Alltag:** Ein Pate oder Buddy aus dem Lager, der ihn durch Pausen, Schichtübergaben und "Wo finde ich was?" begleitet. Die Teamleitung ist für Fachliches da, der Pate für den Alltag.
3. **Klare Ziele für Woche 2:** Am Freitag sollte man nicht nur Feedback geben, sondern auch festhalten, was in Woche 2 konkret erwartet wird. Außerdem gehören Zeiterfassung, Pausenregelung und Krankmeldeweg in den ersten Tagen geklärt.

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1
```text
Rolle: Du bist eine erfahrene Teamleiterin in einem kleinen technischen
Herstellerbetrieb.

Kontext: Wir sind die Nordlicht Technik GmbH, ca. 80 Mitarbeitende.
Am Montag fängt ein neuer Kollege im Lager an. Er hat schon Erfahrung
in der Lagerlogistik, kennt aber unsere Abläufe und Systeme noch nicht.
Arbeitszeit: Montag bis Freitag, 7 bis 15:30 Uhr.

Aufgabe: Erstelle
1. eine kurze, herzliche Willkommensnachricht an ihn (höchstens 80 Wörter,
   wir duzen uns),
2. einen Einarbeitungsplan für seine erste Woche.

Format: Den Plan als Tabelle mit den Spalten Tag | Vormittag | Nachmittag |
Ansprechperson. Für Namen setze Platzhalter wie [NAME TEAMLEITUNG].

Beispiel für eine Tabellenzeile:
Montag | Begrüßung, Rundgang, Arbeitssicherheit | Arbeitsplatz einrichten,
Zugänge testen | [NAME TEAMLEITUNG]
```

### Assistent 1
**1. Willkommensnachricht**

Hallo [VORNAME],

herzlich willkommen bei der Nordlicht Technik GmbH! Wir freuen uns sehr, dass du ab Montag unser Lagerteam verstärkst. Du startest um 7:00 Uhr, ich nehme dich am Empfang in Empfang und zeige dir alles in Ruhe. Mach dir keine Sorgen: Deine Erfahrung bringt dich schnell weiter, und wir erklären dir gern unsere Abläufe und Systeme. Bei Fragen bin ich jederzeit für dich da. Bis Montag!

Viele Grüße
[NAME TEAMLEITUNG]

**2. Einarbeitungsplan – erste Woche (7:00–15:30 Uhr)**

| Tag | Vormittag | Nachmittag | Ansprechperson |
|---|---|---|---|
| Montag | Begrüßung, Rundgang, Arbeitssicherheit (Unterweisung, Fluchtwege, PSA) | Arbeitsplatz einrichten, Zugänge testen (Lagerverwaltungssystem, E-Mail) | [NAME TEAMLEITUNG] |
| Dienstag | Wareneingang: Annahme, Lieferscheinprüfung, Qualitätskontrolle, Einlagern | Lagerverwaltungssystem: Buchungen, Lagerplätze, Chargen/Seriennummern | [NAME WARENEINGANG] |
| Mittwoch | Kommissionierung: Aufträge, Pickstrategien, Verpacken | Staplerschein-Check bzw. Flurförderzeug-Unterweisung, Mitfahren | [NAME KOMMISSIONIERUNG] / [NAME STAPLERBEAUFTRAGTE/R] |
| Donnerstag | Warenausgang und Versand: Versandpapiere, Spediteure, Verladung | Inventur und Bestandskontrolle, Umgang mit Fehlbeständen | [NAME VERSAND] |
| Freitag | Selbstständig arbeiten mit Begleitung, offene Fragen klären | Wochenrückblick, Ausblick auf Woche 2 | [NAME TEAMLEITUNG] |

### Nutzer 2
Kürzer bitte – der Plan soll auf eine halbe Seite passen.

### Assistent 2
Hier die gekürzte Version:

| Tag | Vormittag | Nachmittag | Ansprechperson |
|---|---|---|---|
| Mo | Begrüßung, Rundgang, Arbeitssicherheit | Arbeitsplatz, Zugänge testen | [NAME TEAMLEITUNG] |
| Di | Wareneingang und Einlagerung | Lagerverwaltungssystem | [NAME WARENEINGANG] |
| Mi | Kommissionierung und Verpackung | Stapler-Unterweisung | [NAME KOMMISSIONIERUNG] |
| Do | Warenausgang und Versand | Inventur, Bestandskontrolle | [NAME VERSAND] |
| Fr | Selbstständig mit Begleitung | Wochenrückblick | [NAME TEAMLEITUNG] |

### Nutzer 3
Ergänze am Freitag ein kurzes Feedbackgespräch und eine Spalte "Erledigt" zum Abhaken.

### Assistent 3
| Tag | Vormittag | Nachmittag | Ansprechperson | Erledigt |
|---|---|---|---|---|
| Mo | Begrüßung, Rundgang, Arbeitssicherheit | Arbeitsplatz, Zugänge testen | [NAME TEAMLEITUNG] | ☐ |
| Di | Wareneingang und Einlagerung | Lagerverwaltungssystem | [NAME WARENEINGANG] | ☐ |
| Mi | Kommissionierung und Verpackung | Stapler-Unterweisung | [NAME KOMMISSIONIERUNG] | ☐ |
| Do | Warenausgang und Versand | Inventur, Bestandskontrolle | [NAME VERSAND] | ☐ |
| Fr | Selbstständig mit Begleitung | Wochenrückblick, Feedbackgespräch (ca. 30 Min.) | [NAME TEAMLEITUNG] | ☐ |

### Nutzer 4
Die Willkommensnachricht klingt zu förmlich. Schreib sie so, wie man einem Kollegen im Lager schreibt.

### Assistent 4
Hey [VORNAME],

schön, dass du ab Montag bei uns im Lager dabei bist! Wir starten um 7 Uhr, ich hol dich vorne am Empfang ab und zeig dir erst mal alles. Mach dir keinen Stress, du kennst den Job ja schon, wir zeigen dir nur, wie bei uns der Hase läuft. Wenn was unklar ist, frag einfach. Freu mich auf dich!

Gruß
[NAME TEAMLEITUNG]

### Nutzer 5
Was fehlt in diesem Plan noch? Nenne mir 3 Punkte, die erfahrene Teamleitungen oft vergessen.

### Assistent 5
Drei Punkte, die gern untergehen:

1. **Pate bzw. Buddy für die ganze Woche.** Ein fester Kollege an seiner Seite, den er alles fragen kann, auch Kleinigkeiten wie "Wo ist die Kaffeemaschine?" oder "Wen rufe ich an, wenn ich krank bin?". Ohne Buddy fühlen sich Neue schnell allein, weil die Teamleitung nicht ständig Zeit hat.

2. **Organisatorisches vor dem ersten Tag.** Spind, Schlüssel bzw. Zugangskarte, Arbeitskleidung und Sicherheitsschuhe, Login-Daten und Handscanner sollten schon bereitliegen. Dazu gehören auch Pausenzeiten, Kantine bzw. Mittagessen am ersten Tag und Infos zu Parken, Krankmeldung und Zeiterfassung. Sonst verliert er am Montag Zeit mit Warten.

3. **Soziale Einbindung und Vorstellung im Team.** Gemeinsames Mittagessen am ersten Tag, Vorstellung bei den Nachbarabteilungen (Produktion, Einkauf, Büro) und ein kurzer Blick aufs Gesamtbild: Wer macht was im Betrieb? Gerade bei 80 Mitarbeitenden hilft das, schnell dazuzugehören.

---

## Gesprächsprotokoll: Opus

### Nutzer 1
```text
Rolle: Du bist eine erfahrene Teamleiterin in einem kleinen technischen
Herstellerbetrieb.

Kontext: Wir sind die Nordlicht Technik GmbH, ca. 80 Mitarbeitende.
Am Montag fängt ein neuer Kollege im Lager an. Er hat schon Erfahrung
in der Lagerlogistik, kennt aber unsere Abläufe und Systeme noch nicht.
Arbeitszeit: Montag bis Freitag, 7 bis 15:30 Uhr.

Aufgabe: Erstelle
1. eine kurze, herzliche Willkommensnachricht an ihn (höchstens 80 Wörter,
   wir duzen uns),
2. einen Einarbeitungsplan für seine erste Woche.

Format: Den Plan als Tabelle mit den Spalten Tag | Vormittag | Nachmittag |
Ansprechperson. Für Namen setze Platzhalter wie [NAME TEAMLEITUNG].

Beispiel für eine Tabellenzeile:
Montag | Begrüßung, Rundgang, Arbeitssicherheit | Arbeitsplatz einrichten,
Zugänge testen | [NAME TEAMLEITUNG]
```

### Assistent 1
**1. Willkommensnachricht**

Hallo [NAME NEUER KOLLEGE],

herzlich willkommen bei der Nordlicht Technik GmbH! Wir freuen uns sehr, dass du ab Montag unser Lagerteam verstärkst. Deine Erfahrung in der Lagerlogistik bringst du schon mit, unsere Abläufe und Systeme zeigen wir dir in der ersten Woche in Ruhe. Am Montag um 7 Uhr holen wir dich am Empfang ab. Wenn du vorher Fragen hast, melde dich gern jederzeit bei mir.

Bis Montag und viele Grüße
[NAME TEAMLEITUNG]

*(ca. 70 Wörter)*

**2. Einarbeitungsplan erste Woche (jeweils 7:00–15:30 Uhr)**

| Tag | Vormittag | Nachmittag | Ansprechperson |
|---|---|---|---|
| Montag | Begrüßung, Vorstellung im Team, Rundgang durch Betrieb und Lager, Arbeitssicherheitsunterweisung (Fluchtwege, PSA, Erste Hilfe) | Arbeitsplatz einrichten, Arbeitskleidung/PSA ausgeben, Zugänge zu Lagerverwaltungssystem und E-Mail testen | [NAME TEAMLEITUNG] |
| Dienstag | Wareneingang: Annahme, Prüfung, Buchung im System, Umgang mit Lieferpapieren | Einlagerung: Lagerplatzlogik, Beschriftung, Scanner bedienen | [NAME KOLLEGE WARENEINGANG] |
| Mittwoch | Kommissionierung: Auftragsabwicklung, Pickliste, Pickreihenfolge | Verpackung und Versand: Packvorschriften, Versanddienstleister, Versandpapiere | [NAME KOLLEGE VERSAND] |
| Donnerstag | Flurförderzeuge: Unterweisung und Einweisung für Stapler/Hubwagen (Befähigungsnachweis prüfen), Gefahrstoffe/Sonderlagerung | Schnittstellen kennenlernen: kurzer Besuch in Produktion und Einkauf, Materialbereitstellung für die Fertigung | [NAME SICHERHEITSFACHKRAFT], [NAME ANSPRECHPERSON PRODUKTION] |
| Freitag | Inventur, Bestandskorrekturen, Reklamationen und Retouren | Erste Aufgaben selbstständig unter Begleitung, offene Fragen klären, Ausblick auf Woche 2 | [NAME PATE/PATIN], [NAME TEAMLEITUNG] |

**Tipp:** Gib ihm für die ganze Woche einen festen Paten oder eine feste Patin aus dem Lagerteam, dann weiß er immer, an wen er sich wenden kann.

### Nutzer 2
Kürzer bitte – der Plan soll auf eine halbe Seite passen.

### Assistent 2
Gern, hier ist die kompakte Version:

**Einarbeitungsplan erste Woche (7:00–15:30 Uhr)**

| Tag | Vormittag | Nachmittag | Ansprechperson |
|---|---|---|---|
| Mo | Begrüßung, Rundgang, Arbeitssicherheit | Arbeitsplatz, PSA, Zugänge testen | [NAME TEAMLEITUNG] |
| Di | Wareneingang & Buchung | Einlagerung, Scanner | [NAME WARENEINGANG] |
| Mi | Kommissionierung | Verpackung & Versand | [NAME VERSAND] |
| Do | Stapler-Einweisung, Gefahrstoffe | Schnittstellen Produktion/Einkauf | [NAME SICHERHEITSFACHKRAFT] |
| Fr | Inventur, Retouren | Erste Aufgaben selbstständig, Fragen klären | [NAME PATE/PATIN] |

### Nutzer 3
```text
Ergänze am Freitag ein kurzes Feedbackgespräch und eine Spalte
"Erledigt" zum Abhaken.
```

### Assistent 3
Hier ist der ergänzte Plan:

**Einarbeitungsplan erste Woche (7:00–15:30 Uhr)**

| Tag | Vormittag | Nachmittag | Ansprechperson | Erledigt |
|---|---|---|---|---|
| Mo | Begrüßung, Rundgang, Arbeitssicherheit | Arbeitsplatz, PSA, Zugänge testen | [NAME TEAMLEITUNG] | ☐ |
| Di | Wareneingang & Buchung | Einlagerung, Scanner | [NAME WARENEINGANG] | ☐ |
| Mi | Kommissionierung | Verpackung & Versand | [NAME VERSAND] | ☐ |
| Do | Stapler-Einweisung, Gefahrstoffe | Schnittstellen Produktion/Einkauf | [NAME SICHERHEITSFACHKRAFT] | ☐ |
| Fr | Inventur, Retouren | Erste Aufgaben selbstständig; **14:30 Uhr Feedbackgespräch (ca. 30 Min.)** | [NAME PATE/PATIN], [NAME TEAMLEITUNG] | ☐ |

Mögliche Fragen für das Feedbackgespräch: Was lief gut? Wo bist du noch unsicher? Was brauchst du in Woche 2?

### Nutzer 4
```text
Die Willkommensnachricht klingt zu förmlich. Schreib sie so,
wie man einem Kollegen im Lager schreibt.
```

### Assistent 4
Klar, hier eine lockerere Version:

Hey [NAME],

schön, dass du ab Montag bei uns im Lager mit anpackst! Wir freuen uns auf dich. Lager kannst du ja schon, wie wir hier ticken, zeigen wir dir in der ersten Woche. Komm am Montag um 7 einfach zum Empfang, da holen wir dich ab. Arbeitsschuhe hast du, den Rest kriegst du von uns.

Wenn vorher noch was ist, ruf einfach durch.

Bis Montag!
[NAME TEAMLEITUNG]

### Nutzer 5
```text
Was fehlt in diesem Plan noch? Nenne mir 3 Punkte, die erfahrene
Teamleitungen oft vergessen.
```

### Assistent 5
Drei Punkte, die in der Praxis oft untergehen:

1. **Alles vor dem ersten Tag vorbereiten.** Zugänge zum Lagerverwaltungssystem, Scanner, Spind, Arbeitskleidung und PSA in der richtigen Größe sollten schon am Montag um 7 Uhr bereitliegen. Sonst sitzt der Neue den halben ersten Tag herum und wartet auf die IT, und so einen Einstieg vergisst man nicht so schnell.

2. **Ein fester Pate mit eingeplanter Zeit.** Im Plan stehen jeden Tag andere Ansprechpersonen. Das ist fachlich sinnvoll, aber er braucht zusätzlich eine feste Bezugsperson für die ganze Woche, also für Fragen wie „Wo ist der Pausenraum?“ oder „Wie läuft das mit der Zeiterfassung?“. Wichtig ist auch, dass der Pate für diese Woche weniger eigene Arbeit hat, sonst fehlt ihm die Zeit dafür.

3. **Organisatorisches und die ungeschriebenen Regeln.** Zeiterfassung, Pausenregelung, Krankmeldung, Urlaubsantrag, Schichtübergabe und Parkplatz. Dazu die informellen Dinge: Wer entscheidet bei Engpässen? Welche Kunden oder Aufträge haben Vorrang? Gerade erfahrene Leute kennen solche Regeln aus ihrem alten Betrieb und machen es dann so wie dort, wenn man ihnen nicht sagt, wie es hier läuft.

**Bonus:** Plane gleich ein zweites Feedbackgespräch nach ca. 4–6 Wochen ein. Erst dann merkt man, wo es wirklich hakt.

---

Zurück zum [Übungsblatt Übung 2](../06_Uebungen/Uebung_2_Gute_Prompts.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md)
