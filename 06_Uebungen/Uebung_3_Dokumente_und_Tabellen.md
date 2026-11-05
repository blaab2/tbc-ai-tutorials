# Übung 3: Mit Dokumenten und Tabellen arbeiten

**Block 5 · 1:40–2:20 · Dauer: 40 Minuten** (inkl. kurzer Einführung und Auswertung, ca. 27 Minuten reine Arbeitszeit)

---

## Ziel

Nach dieser Übung kannst du …

- eine Datei in [KI-TOOL] hochladen (oder ihren Inhalt einfügen) und gezielt Fragen dazu stellen,
- lange Texte für eine bestimmte Zielgruppe zusammenfassen lassen,
- zwei Versionen eines Dokuments vergleichen lassen,
- aus chaotischen Notizen ein sauberes Protokoll mit Aufgabenliste machen,
- eine unordentliche Tabelle bereinigen lassen,
- **und vor allem: das Ergebnis im Original überprüfen.** Der KI-Assistent kann beim Zusammenfassen Dinge weglassen, verdrehen oder hinzuerfinden. Das nennt man **Halluzination**: Das Sprachmodell erzeugt Text, der überzeugend klingt, aber nicht stimmt.

## Material

- Dein Laptop mit Zugang zu [KI-TOOL] ([LINK ZUM TOOL])
- Die Beispieldateien aus dem Ordner `07_Beispielmaterial` (vom Trainer bereitgestellt, z. B. als Download oder auf einem USB-Stick):
  - [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md) – Station A
  - [richtlinie_reisekosten_v1.md](../07_Beispielmaterial/richtlinie_reisekosten_v1.md) und [richtlinie_reisekosten_v2.md](../07_Beispielmaterial/richtlinie_reisekosten_v2.md) – Station B
  - [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt) – Station C
  - [lieferantenliste_unsortiert.csv](../07_Beispielmaterial/lieferantenliste_unsortiert.csv) – Station D

  Keine Sorge wegen der Dateiendungen: `.txt` und `.md` sind einfache Textdateien (`.md` enthält zusätzlich ein paar Formatierungszeichen wie `#` für Überschriften). `.csv` ist eine Tabelle im Textformat: Jede Zeile ist ein Eintrag, die Spalten sind durch ein Semikolon (`;`) getrennt.
- Die [Daten-Ampel](../03_Daten-Ampel.md) und der [Spickzettel](../05_Spickzettel.md)

> **Gut zu wissen:** Alle Beispieldateien spielen in der fiktiven Firma „Nordlicht Technik GmbH“. Personen, Firmen und Zahlen sind erfunden. Du darfst diese Dateien also bedenkenlos hochladen – sie sind **grün** auf der Daten-Ampel. Bei echten Firmendokumenten gilt das nicht automatisch!

### Falls der Upload nicht funktioniert

Nicht bei jedem Zugang ist das Hochladen von Dateien freigeschaltet, und manchmal hakt es technisch. Dann gilt:

1. Öffne die Datei in einem Texteditor (bei `.md` und `.txt` z. B. Editor/Notepad; bei `.csv` ebenfalls im Texteditor, **nicht** in Excel – Excel verändert beim Öffnen gern Datumsformate).
2. Alles markieren (Strg + A), kopieren (Strg + C).
3. In das Eingabefeld des KI-Assistenten einfügen (Strg + V). Setz den Text am besten zwischen zwei Markierungen (hier: drei Anführungszeichen), damit klar ist, wo er anfängt und aufhört:

```
Hier ist das Dokument, um das es geht:

"""
[HIER DEN INHALT EINFÜGEN]
"""

Bitte lies es vollständig und bestätige kurz, dass du es hast. Warte dann auf meine Frage.
```

4. Prüfe, ob alles angekommen ist: Frag „Wie lauten die letzten zwei Zeilen des Dokuments, wörtlich?“ und vergleiche die Antwort mit dem Ende der Datei (im Editor Strg + Ende).

---

## So läuft die Übung

Es gibt **vier Stationen (A–D)**. Du wählst frei – nimm die, die am besten zu deiner Arbeit passt. Arbeite am besten mit deinem Teampartner zusammen.

| Station | Thema | Passt gut für … |
|---|---|---|
| **A** | Langen Bericht zusammenfassen | alle, die viel lesen müssen: Projektleitung, Technik, Geschäftsführungsnähe |
| **B** | Zwei Versionen vergleichen | Verwaltung, Personal, Qualitätsmanagement, alle mit Richtlinien und Verträgen |
| **C** | Notizen → Protokoll + Aufgaben | alle, die Besprechungen haben (also fast alle) |
| **D** | Tabelle bereinigen | Einkauf, Buchhaltung, Vertrieb, alle mit Listen und Excel |

**Empfehlung:** Mach eine Station gründlich (Basis + Weiter) statt alle vier oberflächlich. Wer fertig ist, nimmt sich eine zweite Station oder die Aufgaben „Für Schnelle“ vor.

**Zeitplan:**

| Zeit | Was passiert |
|---|---|
| 1:40–1:45 | Trainer zeigt kurz: Datei hochladen bzw. Inhalt einfügen |
| 1:45–2:12 | Du arbeitest an deiner Station |
| 2:12–2:20 | Kurze Runde: Was hat geklappt? Wo lag der KI-Assistent daneben? |

**Die goldene Regel dieser Übung:** Jede Station endet mit einem **Prüfschritt**. Den lässt du nicht weg. Genau darum geht es.

---

## Station A: Langen Bericht zusammenfassen

**Datei:** [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md) (ein langer technischer Prüf-/Projektbericht)

**Szenario:** Die Geschäftsführung hat keine Zeit, den ganzen Bericht zu lesen. Sie braucht in fünf Sätzen das Wichtigste – und eine ehrliche Einschätzung, wo es noch hakt.

### Basis

Lade die Datei hoch (oder füge den Inhalt ein) und schreib:

```
Du bist Assistent der Geschäftsführung eines kleinen technischen Herstellers.
Fasse den angehängten (bzw. eingefügten) Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammen.
Die Geschäftsführung ist technisch interessiert, hat aber keine Zeit für Details.
Wichtig: Ergebnis, Kosten oder Aufwand (falls genannt), Termine, und ob eine Entscheidung nötig ist.
Schreib nichts, was nicht im Bericht steht.
```

### Weiter

Stelle Nachfragen an das Dokument:

```
Welche Risiken oder offenen Punkte nennt der Bericht, die noch nicht gelöst sind?
Liste sie als Tabelle mit den Spalten: Risiko | Wie schlimm (laut Bericht) | Abschnitt im Bericht.
Wenn der Bericht zu einem Punkt keine Einschätzung enthält, schreib "keine Angabe".
```

Und danach zum Beispiel:

```
Was empfiehlt der Bericht als nächsten Schritt? Zitiere die entsprechende Stelle wörtlich.
```

```
Gibt es Widersprüche oder Stellen, die unklar formuliert sind?
```

### Prüfschritt (Pflicht!)

Nimm dir **drei Aussagen** aus der Zusammenfassung oder der Risikotabelle und suche sie im Original:

- [ ] Aussage 1 gefunden? Steht es dort genau so?
- [ ] Aussage 2 gefunden? Stimmen Zahlen und Termine?
- [ ] Aussage 3 gefunden? Fehlt etwas Wichtiges, das im Bericht steht?

**Tipp:** Mit Strg + F kannst du im Originaldokument nach einem Stichwort oder einer Zahl suchen.

### Für Schnelle

- **Modellvergleich:** Stell dieselbe Basis-Aufgabe noch einmal in einem **neuen Chat** – diesmal mit einem anderen Modell (z. B. [STARKES MODELL] statt [SCHNELLES MODELL] oder mit [DENK-MODUS]). Vergleiche: Was ist länger, was vollständiger? Hält sich das Modell an „genau 5 Sätze“? Findet eines von beiden den Fehler in der Messwerttabelle von selbst? Hinweise: [Modellauswahl](../05b_Modellauswahl.md)

- Lass dir den Bericht für eine **andere Zielgruppe** zusammenfassen, z. B. für die Bediener und die Instandhaltung in Halle 3 in einfacher Sprache (Was ändert sich im Arbeitsalltag?) oder für einen Kunden (ohne interne Details). Prüfe danach: Welche Aussage klingt sicherer als im Original? Würdest du den Kundentext so verschicken?
- Frag: „Welche drei Fragen sollte die Geschäftsführung den Autoren des Berichts stellen?“
- Frag nach etwas, das **nicht** im Bericht steht, z. B. „Wie viel Euro behalten wir als Einbehalt zurück?“ (Tipp: Such im Bericht nach dem Kaufpreis.) Gibt der KI-Assistent zu, dass er es nicht weiß – oder erfindet er etwas? Beides ist lehrreich: Gibt er es zu, prüf trotzdem nach. Nennt er eine Zahl, such, woher sie kommt.

---

## Station B: Zwei Versionen einer Richtlinie vergleichen

**Dateien:** [richtlinie_reisekosten_v1.md](../07_Beispielmaterial/richtlinie_reisekosten_v1.md) (alte Fassung) und [richtlinie_reisekosten_v2.md](../07_Beispielmaterial/richtlinie_reisekosten_v2.md) (neue Fassung)

**Szenario:** Die Reisekostenrichtlinie wurde überarbeitet. Du sollst den Kolleginnen und Kollegen erklären, was sich geändert hat – ohne beide Fassungen Zeile für Zeile nebeneinanderzulegen.

### Basis

Lade **beide** Dateien hoch (oder füge beide nacheinander ein, klar beschriftet mit „ALTE FASSUNG“ und „NEUE FASSUNG“) und schreib:

```
Ich gebe dir zwei Fassungen unserer internen Reisekostenrichtlinie: v1 (alt) und v2 (neu).
Vergleiche sie und liste ALLE inhaltlichen Änderungen auf.
Reine Formulierungs- oder Formatierungsänderungen kannst du weglassen.

Format: Tabelle mit den Spalten
Nr. | Thema | Alte Regel (v1) | Neue Regel (v2) | Was bedeutet das für Mitarbeitende?
```

### Weiter

```
Prüfe deine Tabelle noch einmal Abschnitt für Abschnitt gegen beide Fassungen.
Hast du etwas übersehen? Gibt es Regeln, die in v2 neu dazugekommen oder ganz weggefallen sind?
```

Und dann:

```
Schreib aus der Tabelle eine kurze Info-Mail an alle Mitarbeitenden (max. 150 Wörter, Ton: freundlich, sachlich, per du).
Die wichtigste Änderung zuerst.
```

### Prüfschritt (Pflicht!)

Wurden wirklich **alle** Änderungen gefunden? So prüfst du (ca. 5–8 Minuten einplanen):

1. Lege beide Fassungen nebeneinander (zwei Fenster) und gehe Abschnitt für Abschnitt durch.
2. Achte besonders auf **Zahlen** (Beträge, Kilometer, Tage, Fristen) – hier verstecken sich Änderungen gern.
3. Hake jede Änderung in der Tabelle ab, die du im Original wiederfindest.
4. Notiere, was der KI-Assistent übersehen oder falsch dargestellt hat. Stimmt die genannte Anzahl mit den Zeilen der Tabelle überein? Ist eine Deutung als Tatsache formuliert?
5. Lies die Info-Mail Satz für Satz gegen die neue Fassung: Steht jede Aussage genau so in v2?

Am Ende verrät der Trainer, wie viele Änderungen es tatsächlich gibt. Wie nah warst du dran?

- Gefundene Änderungen laut KI: ______
- Davon im Original bestätigt: ______
- Übersehen: ______

### Für Schnelle

- Lass dir eine **FAQ** mit den fünf Fragen erstellen, die Mitarbeitende zur neuen Fassung wahrscheinlich stellen – mit Antworten, die sich nur auf v2 stützen. Tipp: Lass zu jeder Antwort den Abschnitt angeben, und prüfe, ob die Frage nach dem Trinkgeld dabei ist.
- Frag: „Gibt es in v2 Formulierungen, die unklar sind oder unterschiedlich verstanden werden können?“
- Spiel einen Fall durch – und rechne danach selbst nach:

```
Ich fahre mit dem eigenen Auto zu einem Kunden: 180 km hin und 180 km zurück.
Ich übernachte einmal im Hotel, die Rechnung beträgt 125 Euro ohne Frühstück.
Was bekomme ich für Fahrt und Übernachtung nach v1 erstattet, was nach v2?
Rechne Schritt für Schritt und nenne zu jeder Zahl den Abschnitt der Richtlinie.
Nutze nur Angaben aus den beiden Fassungen.
```

Frag danach auch nach der Verpflegung:

```
Und was bekomme ich für die Verpflegung erstattet?
```

Steht dazu ein Betrag in den Richtlinien – oder bringt der KI-Assistent Zahlen von woanders mit? Probier danach: „Nenne nur Beträge, die wörtlich in einer der beiden Fassungen stehen.“ Vergleiche beide Antworten.

---

## Station C: Chaotische Notizen → Protokoll und Aufgabenliste

**Datei:** [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt) (Stichpunkte einer Teambesprechung, ziemlich durcheinander)

**Szenario:** Du hast in der Besprechung mitgeschrieben – schnell und unordentlich. Jetzt soll daraus ein Protokoll werden, das alle verstehen. Und vor allem: Wer macht was bis wann?

### Basis

```
Hier sind meine Stichpunkt-Notizen aus einer Teambesprechung. Sie sind unordentlich.
Mach daraus ein sauberes Protokoll mit diesen Abschnitten:
1. Teilnehmende
2. Besprochene Themen (je 1–3 Sätze)
3. Entscheidungen
4. Offene Fragen

Erfinde nichts dazu. Wenn etwas in den Notizen unklar ist, markiere es mit [UNKLAR].
```

### Weiter

```
Erstelle jetzt eine Aufgabentabelle aus den Notizen mit den Spalten:
Nr. | Was | Wer | Bis wann | Quelle (Zitat aus den Notizen)

Wenn keine Person oder kein Termin genannt ist, schreib "offen" – rate nicht.
Sortiere nach Termin, früheste zuerst.
```

Danach zum Beispiel:

```
Formuliere eine kurze Mail an alle Teilnehmenden mit dem Protokoll und der Aufgabentabelle.
Bitte am Ende darum, fehlende Verantwortliche bis Freitag zu ergänzen.
```

### Prüfschritt (Pflicht!)

Gehe die Notizen Zeile für Zeile durch:

- [ ] Protokoll (Basis): Steht der Liefertermin aus dem NACHTRAG drin? Ist der Rabatt eine offene Frage und keine Entscheidung? Sind Notizzeilen mit Fragezeichen als [UNKLAR] markiert und nicht zur Tatsache geworden?
- [ ] Ist jede Aufgabe aus den Notizen in der Tabelle? (Achtung: Manche Aufgaben verstecken sich in Nebensätzen.)
- [ ] Stimmen die Namen bei „Wer“? Hat der KI-Assistent jemandem eine Aufgabe zugeschoben, die so nicht in den Notizen steht?
- [ ] Stimmen die Termine? Wurden Angaben wie „nächste Woche“ oder „bis Ende des Monats“ in ein konkretes Datum umgerechnet – und wenn ja, stimmt das?
- [ ] Gibt es Einträge, die frei erfunden sind?
- [ ] Stimmt die Tabelle in der Mail noch mit der Tabelle davor überein (Namen, Termine, nichts weggefallen)?

### Für Schnelle

- Lass dir die Aufgaben als **Checkliste** zum Abhaken ausgeben (z. B. mit ☐, nach Person sortiert). Tipp: Schreib dazu, dass fehlende Personen oder Termine als „offen“ erscheinen sollen und Erledigtes nicht hineingehört.
- Frag: „Welche Punkte aus der Besprechung haben noch keinen Verantwortlichen? Formuliere zu jedem eine kurze Rückfrage.“
- Lass dir eine Tagesordnung für die **nächste** Besprechung vorschlagen, basierend auf den offenen Punkten. Prüfe: Hat der KI-Assistent ein Datum ausgerechnet? Ist die Kaffeemaschine drin?

---

## Station D: Unordentliche Tabelle bereinigen

**Datei:** [lieferantenliste_unsortiert.csv](../07_Beispielmaterial/lieferantenliste_unsortiert.csv) (Lieferantenliste, Trennzeichen Semikolon)

**Szenario:** Die Lieferantenliste wurde über Jahre von verschiedenen Leuten gepflegt. Datumsformate, Schreibweisen und Einträge sind kreuz und quer, manche Firmen stehen doppelt drin (**Dubletten**), manche Angaben fehlen. Du sollst aufräumen.

> **Achtung bei Zahlen und Tabellen:** Hier macht der KI-Assistent besonders gern Fehler – er kann Zeilen verschlucken, Werte vertauschen oder beim Zählen danebenliegen. Prüfe hier **besonders genau**.

### Basis

```
Hier ist eine Lieferantenliste als CSV (Trennzeichen: Semikolon).
Bitte analysiere sie zuerst, OHNE etwas zu ändern:
1. Wie viele Zeilen (ohne Kopfzeile) hat die Liste?
2. Welche Probleme siehst du? (z. B. unterschiedliche Datumsformate, Schreibweisen, Dubletten, fehlende Werte)
3. Liste mögliche Dubletten auf, mit Begründung.
```

### Weiter

```
Bereinige jetzt die Liste nach diesen Regeln:
- Datumsformat überall TT.MM.JJJJ
- Firmennamen einheitlich schreiben (gleiche Firma = gleiche Schreibweise)
- Dubletten zusammenführen; wenn sich Angaben widersprechen, beide Werte behalten und markieren
- Fehlende Werte NICHT erfinden, sondern als "FEHLT" kennzeichnen
- Neue Spalte "Hinweis" für alles, was ich manuell prüfen sollte

Gib das Ergebnis als Tabelle aus. Nenne danach: Anzahl Zeilen vorher, Anzahl Zeilen nachher, und welche Zeilen zusammengeführt wurden.
```

Danach zum Beispiel:

```
Gib mir die bereinigte Liste noch einmal als CSV mit Semikolon als Trennzeichen, damit ich sie in Excel öffnen kann.
```

### Prüfschritt (Pflicht!)

- [ ] **Zeilen zählen:** Stimmt die Anzahl „vorher“ mit der Originaldatei überein? (Im Texteditor mit Strg + Ende ans Dateiende springen – unten in der Statusleiste steht die Zeilennummer. Die Kopfzeile mit den Spaltennamen nicht mitzählen. Steht der Cursor danach in einer leeren letzten Zeile, zählt auch diese nicht mit. Also: Nummer der letzten Zeile mit Text minus 1. Frag den KI-Assistenten außerdem, ob er Zeilennummern mit oder ohne Kopfzeile angibt.)
- [ ] **Rechnung prüfen:** Zeilen vorher – zusammengeführte Dubletten = Zeilen nachher?
- [ ] **Stichprobe:** Nimm dir drei Lieferanten und vergleiche jede Angabe (Name, Datum, Kontakt, Werte) mit dem Original.
- [ ] **Erfundenes?** Steht irgendwo ein Wert, der im Original fehlte (z. B. eine ausgedachte Telefonnummer oder ein Datum)?
- [ ] **Dubletten:** Sind die zusammengeführten Einträge wirklich dieselbe Firma?
- [ ] **CSV = Tabelle?** Hat die CSV genauso viele Zeilen wie die Tabelle, und stehen dieselben Hinweise drin?

### Für Schnelle

- Frag: „Welche Spalten fehlen in dieser Liste, die man für eine ordentliche Lieferantenverwaltung bräuchte? Nenne die 5 wichtigsten mit je einem Satz Begründung.“
- Lass dir die Summe der Jahresumsätze nach Entfernen der Dubletten bilden – mit allen Einzelwerten als Tabelle – und rechne sie in Excel mit =SUMME nach. Stimmt sie?
- Lass dir eine kurze **Anleitung** schreiben, wie die Liste künftig einheitlich gepflegt werden soll (Regeln für Schreibweisen, Datumsformat, Pflichtfelder).
- Lass dir erklären, wie du die Bereinigung **selbst in Excel** machen würdest (z. B. Duplikate entfernen, Text in Spalten). Oft ist das bei großen Tabellen der verlässlichere Weg – der KI-Assistent hilft dir dabei mit der Anleitung. Probier die Anleitung in Excel aus: Wie viele Zeilen entfernt „Duplikate entfernen“? Richtig wären 4 (27 → 23).

---

## Reflexionsfragen

Nimm dir in der Auswertungsrunde oder direkt danach zwei Minuten und beantworte für dich (oder mit deinem Teampartner):

1. Wie viel Zeit hätte dich diese Aufgabe **ohne** KI gekostet? Und wie viel mit (inklusive Prüfen)?
2. Wo hat der KI-Assistent einen **Fehler** gemacht oder etwas weggelassen? Hättest du den ohne Prüfschritt bemerkt?
3. Welche Art von Dokument aus **deinem** Arbeitsalltag könntest du so bearbeiten?
4. Welche deiner echten Dokumente wären auf der [Daten-Ampel](../03_Daten-Ampel.md) **gelb oder rot** – und was heißt das für dich?

---

## Meine Notizen

**Station(en), die ich gemacht habe:** ______________________________

**Mein bester Prompt dieser Übung:**

```




```

**Was der KI-Assistent gut konnte:**

&nbsp;

&nbsp;

**Wo er danebenlag:**

&nbsp;

&nbsp;

**Eine Aufgabe aus meinem Job, bei der ich das ausprobieren will:**

&nbsp;

&nbsp;

---

Weiter geht es mit [Übung 4: Deine eigene Aufgabe](Uebung_4_Eigene_Aufgabe.md). Zurück zur [Übersicht](../README.md).
