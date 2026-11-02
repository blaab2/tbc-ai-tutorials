# Übung 2: Gute Prompts

**Block 4 (1:00–1:30) · Dauer der Übung: ca. 18 Minuten (1:12–1:30) · Arbeitsform: Zweierteam**

Die Übung startet direkt nach dem kurzen Input zu guten Prompts.

---

## Ziel

Danach kannst du …

- erkennen, warum ein knapper Prompt oft nur ein mittelmäßiges Ergebnis bringt,
- einen Prompt mit dem **Prompt-Baukasten** (Rolle, Kontext, Aufgabe, Format, Beispiel) aufbauen,
- den KI-Assistenten mit der Technik „Stell mir zuerst 3 Fragen“ dazu bringen, fehlende Informationen bei dir abzufragen,
- ein Ergebnis Schritt für Schritt verbessern, statt neu anzufangen (das nennt man auch „iterieren“),
- dir einen **eigenen wiederverwendbaren Prompt** für eine Aufgabe bauen, die bei dir immer wieder anfällt.

---

## Was du brauchst

- Deinen Laptop mit Zugang zu [KI-TOOL] ([LINK ZUM TOOL])
- Den [Spickzettel](../05_Spickzettel.md) mit dem Prompt-Baukasten
- Die [Daten-Ampel](../03_Daten-Ampel.md) – besonders für Aufgabe E
- Optional: die Beispieldatei [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt) für die Aufgabe „Für Schnelle“

---

## Der Prompt-Baukasten

Nicht jeder Prompt braucht alle fünf Bausteine. Aber je mehr davon drin sind, desto weniger muss der KI-Assistent raten.

| Baustein | Frage dahinter | Beispiel |
|---|---|---|
| **Rolle** | Als wer soll die KI antworten? | „Du bist eine erfahrene Ausbilderin in einem Technikbetrieb.“ |
| **Kontext** | Was muss die KI über die Situation wissen? | „Wir sind ein kleiner Hersteller. Am Montag fängt ein neuer Kollege im Lager an.“ |
| **Aufgabe** | Was genau soll herauskommen? | „Erstelle einen Einarbeitungsplan für die erste Woche.“ |
| **Format** | Wie soll das Ergebnis aussehen? | „Als Tabelle mit den Spalten Tag, Thema, Ansprechperson. Höchstens eine Seite.“ |
| **Beispiel** | Wie sieht „gut“ aus? | „So ungefähr: Montag – Rundgang und Sicherheitsunterweisung – [NAME].“ |

> **Wichtig:** Der KI-Assistent kennt die Nordlicht Technik GmbH – und deine echte Firma – nicht. Alles, was er wissen soll, musst du ihm sagen (und dabei die Daten-Ampel beachten).

---

## Ablauf

| Stufe | Aufgaben | Richtzeit |
|---|---|---|
| Basis | A und B: schlechter vs. guter Prompt, Vergleich | ca. 8 Min. |
| Weiter | C **oder** D: „Stell mir zuerst 3 Fragen“ bzw. Schritt für Schritt nachschärfen | ca. 5 Min. |
| Weiter | E: dein eigener wiederverwendbarer Prompt (**bitte nicht auslassen**) | ca. 5 Min. |
| Für Schnelle | F und G (und die zweite Aufgabe aus C/D) | wenn Zeit bleibt |
| Alle | Reflexion im Team | ca. 2 Min. |

**Arbeitsteilung im Zweierteam:** Für Aufgabe A und B nehmt ihr am besten **zwei getrennte Chats** (oder Person 1 macht A, Person 2 macht B) und legt die Ergebnisse dann nebeneinander.

---

## Stufe 1: Basis

Der Auftrag ist für alle gleich: **Ein neuer Kollege fängt nächste Woche im Lager an. Du sollst ihm eine Willkommensnachricht schreiben und einen Plan für die erste Woche erstellen.**

### Aufgabe A – Der Minimal-Prompt

Starte einen **neuen Chat** und gib nur das ein:

```text
Schreib einen Einarbeitungsplan.
```

Schau dir das Ergebnis an. (Ja, die Willkommensnachricht fehlt – die KI weiß ja nichts davon.) Speichere es kurz (z. B. in einem Textdokument) oder lass den Chat offen.

### Aufgabe B – Derselbe Auftrag mit dem Baukasten

Starte einen **zweiten neuen Chat** und gib diesen Prompt ein:

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

### Vergleicht die Ergebnisse von A und B

| Frage | Minimal-Prompt (A) | Baukasten-Prompt (B) |
|---|---|---|
| Passt das Ergebnis zur Situation (Lager, kleiner Betrieb)? | | |
| Ist das Format direkt brauchbar? | | |
| Wie viel müsstest du noch nacharbeiten? | | |
| Hat die KI etwas erfunden oder vermutet? | | |

> **Typische Beobachtung:** Beim Minimal-Prompt rät der KI-Assistent – oft kommt etwas Allgemeines für ein Büro oder ein großes Unternehmen heraus. Das ist kein „Fehler“ der KI: Ihr fehlten einfach die Informationen.

---

## Stufe 2: Weiter

### Aufgabe C – „Stell mir zuerst 3 Fragen“

Manchmal weißt du gar nicht, welche Informationen die KI braucht. Dann dreh den Spieß um. Starte einen **neuen Chat**:

```text
Ich möchte einen Einarbeitungsplan für einen neuen Kollegen im Lager
unseres kleinen Technikbetriebs erstellen.

Bevor du anfängst: Stell mir zuerst 3 Fragen, die du brauchst, um einen
wirklich passenden Plan zu schreiben. Warte auf meine Antworten.
```

Beantworte die Fragen kurz (mit erfundenen oder unbedenklichen Angaben) und lass dann den Plan erstellen. Falls der KI-Assistent nicht wartet, sondern gleich loslegt: Schreib ihm „Stopp, bitte erst die Fragen.“

**Beobachte:** Welche Fragen stellt der KI-Assistent? Hättest du an diese Punkte selbst gedacht?

### Aufgabe D – Schritt für Schritt nachschärfen

Bleib im Chat aus Aufgabe B oder C und verbessere das Ergebnis in kleinen Schritten. Probiere mindestens zwei dieser Nachschärfungen:

```text
Kürzer bitte – der Plan soll auf eine halbe Seite passen.
```

```text
Ergänze am Freitag ein kurzes Feedbackgespräch und eine Spalte
"Erledigt" zum Abhaken.
```

```text
Die Willkommensnachricht klingt zu förmlich. Schreib sie so,
wie man einem Kollegen im Lager schreibt.
```

```text
Was fehlt in diesem Plan noch? Nenne mir 3 Punkte, die erfahrene
Teamleitungen oft vergessen.
```

> **Merke:** Du musst nicht beim ersten Versuch den perfekten Prompt schreiben. Ein Gespräch mit zwei, drei Rückmeldungen ist ganz normal – und oft schneller als ein riesiger Prompt.

### Aufgabe E – Dein eigener wiederverwendbarer Prompt

Diese Aufgabe ist das Wichtigste aus Stufe 2 – hier entsteht etwas, das du ab morgen nutzen kannst. Denk an eine Aufgabe, die bei dir **regelmäßig** anfällt, zum Beispiel:

- Wochenbericht oder Statusmeldung an die Chefin
- Antwort auf eine typische Kundenanfrage
- Protokoll aus Stichpunkten
- Stellenanzeige, Aushang oder Rundmail
- Angebotsanschreiben, Erinnerung an offene Unterlagen

Fülle diese Vorlage für deine Aufgabe aus. Die Teile in eckigen Klammern sind **feste Lücken**, die du jedes Mal neu befüllst.

```text
Rolle: Du bist [ROLLE, z. B. eine erfahrene Assistenz der Geschäftsführung].

Kontext: Ich arbeite in [ABTEILUNG] eines [ART DES UNTERNEHMENS, z. B.
mittelständischen Unternehmens]. Ich brauche regelmäßig [ART DES TEXTES] für [EMPFÄNGER].
Wichtig ist uns: [z. B. kurz, sachlich, wir duzen uns intern].

Aufgabe: Erstelle aus den Stichpunkten unten einen [ART DES TEXTES].

Format: [z. B. höchstens 150 Wörter / 3 Abschnitte mit Zwischenüberschrift /
Tabelle mit Spalten ...].

Beispiel für den Stil: [OPTIONAL: EIN KURZER, UNBEDENKLICHER BEISPIELSATZ].

Wenn dir Informationen fehlen, frag nach, statt etwas zu erfinden.

Stichpunkte:
[HIER JEDES MAL DIE AKTUELLEN STICHPUNKTE EINFÜGEN – DATEN-AMPEL BEACHTEN]
```

**Daten-Ampel-Check vor dem Test:**

- [ ] Keine echten Namen von Kunden oder Mitarbeitenden (Platzhalter verwenden)
- [ ] Keine Preise, Vertragsinhalte, Konstruktions- oder Personaldaten
- [ ] Im Zweifel mit erfundenen Beispieldaten testen

Teste deinen Prompt einmal mit Beispielinhalten. Wenn das Ergebnis passt: **Speichere den Prompt** – z. B. in einer Textdatei, in deinen Notizen oder unten auf diesem Blatt. Dann musst du ihn nächstes Mal nur noch kopieren.

---

## Stufe 3: Für Schnelle

### Aufgabe F – Die KI verbessert deinen Prompt

```text
Hier ist ein Prompt, den ich regelmäßig verwenden möchte.
Wie kann ich ihn verbessern, damit die Ergebnisse zuverlässiger werden?
Nenne höchstens 5 konkrete Vorschläge und zeige mir dann die verbesserte
Version.

[HIER DEINEN PROMPT AUS AUFGABE E EINFÜGEN]
```

Prüfe: Sind die Vorschläge wirklich besser – oder nur länger?

### Aufgabe G – Baukasten an einem anderen Beispiel

Öffne [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt) und vergleiche wieder zwei Prompts:

```text
Fass das zusammen.

[HIER DIE NOTIZEN EINFÜGEN]
```

```text
Du bist Assistenz der Teamleitung. Unten stehen ungeordnete Notizen aus
unserer Teambesprechung. Erstelle daraus:
1. eine Zusammenfassung in höchstens 5 Sätzen,
2. eine Tabelle aller Aufgaben mit den Spalten Aufgabe | Wer | Bis wann.
Wenn "Wer" oder "Bis wann" in den Notizen fehlt, schreibe "offen" –
erfinde nichts.

[HIER DIE NOTIZEN EINFÜGEN]
```

Welche Aufgaben oder Termine findet nur der zweite Prompt? Hat die KI irgendwo etwas ergänzt, das gar nicht in den Notizen steht? Und: Hat sie den **Nachtrag** am Ende der Notizen berücksichtigt?

---

## Reflexion (im Zweierteam, ca. 2 Minuten)

Sucht euch zwei Fragen aus:

1. Wie groß war der Unterschied zwischen Minimal-Prompt und Baukasten-Prompt?
2. Welcher Baustein hat am meisten gebracht – Rolle, Kontext, Aufgabe, Format oder Beispiel?
3. War die Technik „Stell mir zuerst 3 Fragen“ hilfreich? Wann würdest du sie nutzen?
4. Für welche wiederkehrende Aufgabe hast du jetzt einen Prompt – und lohnt er sich?
5. Wo bist du dir unsicher, ob du bestimmte Informationen eingeben darfst? (Notieren und beim Trainer oder bei [ANSPRECHPARTNER IT] nachfragen.)

---

## Das nimmst du mit

- **Die KI kann nicht Gedanken lesen.** Was du nicht sagst, wird geraten.
- **Baukasten:** Rolle – Kontext – Aufgabe – Format – Beispiel. Nicht immer alles, aber lieber mehr als zu wenig.
- **Fragen lassen:** „Stell mir zuerst 3 Fragen“ hilft, wenn du nicht weißt, was die KI braucht.
- **Nachschärfen ist normal:** „Kürzer“, „lockerer“, „was fehlt noch?“ – Schritt für Schritt zum Ziel.
- **„Erfinde nichts, frag nach“** gehört in jeden wichtigen Prompt.
- **Gute Prompts speichern** und wiederverwenden – und mit Kolleginnen und Kollegen teilen, z. B. im [TIPPS-KANAL].
- **Daten-Ampel gilt immer** – auch in Vorlagen.

Zurück zu [Übung 1: Texte schreiben](Uebung_1_Texte_schreiben.md) · Weiter nach der Pause mit [Übung 3: Dokumente und Tabellen](Uebung_3_Dokumente_und_Tabellen.md)

---

## Meine Notizen

**Mein wiederverwendbarer Prompt (Aufgabe E):**

```text




```

**Was am meisten gebracht hat:**

&nbsp;

&nbsp;

**Wofür ich mir noch einen Prompt bauen will:**

&nbsp;

&nbsp;

**Offene Fragen:**

&nbsp;

&nbsp;
