# Testlauf: Übung 3 / Upload-Ersatz – Dokument einfügen und Vollständigkeit prüfen

**Herkunft:** Abschnitt „Falls der Upload nicht funktioniert“ aus [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#falls-der-upload-nicht-funktioniert). Die Kontrollfrage stammt aus [Trainer-Loesungshinweise.md – Übung 3](../06_Uebungen/Trainer-Loesungshinweise.md#übung-3-dokumente-und-tabellen), Abschnitt „Stolpersteine bei allen Stationen“: „Bei sehr langen Texten nachfragen: ‚Was ist der letzte Satz des Dokuments?‘ – so prüfst du, ob alles angekommen ist.“ Material: [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md) (143 Zeilen, 1.847 Wörter laut `wc -w`).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt 1 (Vorlage aus dem Übungsblatt, Platzhalter durch den vollständigen Dateiinhalt ersetzt):**

```text
Hier ist das Dokument, um das es geht:

"""
[INHALT VON pruefbericht_lang.md]
"""

Bitte lies es vollständig und bestätige kurz, dass du es hast. Warte dann auf meine Frage.
```

**Prompt 2 (Kontrollfrage aus den Lösungshinweisen):**

```text
Was ist der letzte Satz des Dokuments?
```

**Was laut Material herauskommen soll:** Turn 1: Eine kurze Bestätigung ohne ungefragte Zusammenfassung, dann Warten. Turn 2: Der letzte Satz des Dokuments. Er muss mit dem tatsächlichen Dateiende übereinstimmen.

**Tatsächliches Dateiende (per `tail -n 8`):**

```text
**Empfehlung:** Die Fertigungstechnik empfiehlt der Geschäftsführung, die Anlage **unter Vorbehalt abzunehmen**. […] Es wird vorgeschlagen, bis zur Erledigung dieser Punkte einen Einbehalt von 5 % des Kaufpreises von der Schlusszahlung zu vereinbaren.

Frank Albers, Fertigungstechnik
```

Die letzte Zeile der Datei ist also **kein Satz**, sondern eine Unterschriftszeile. Der letzte echte Satz steht direkt davor. Die Kontrollfrage hat damit zwei richtige Antworten.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Turn 1: Bestätigung erhalten? | ja | ja | ja |
| Turn 1: Länge (Wörter, per `python3`) | 24 | 45 | 64 |
| Turn 1: ungefragte Zusammenfassung? | **nein**. Nur Titel, Nummer, Anlage | **ansatzweise**. Gliederung der 7 Abschnitte in einem Satz | **ja, leicht**. Nummer, Version, Status, Abschnitte, zwei Tabellen, Unterzeichner, also 5 Sätze |
| Turn 1: wartet auf die Frage? | ja | ja | ja |
| Turn 1: Angaben stimmen mit Quelle? | ja | ja | ja (Version 1.0, „Entwurf zur Freigabe“, 7 Abschnitte, 2 Tabellen in Abschnitt 4, Unterzeichner geprüft) |
| Turn 2: letzte Zeile „Frank Albers, Fertigungstechnik“ genannt? | ja, als „letzter Text“ | ja, als „letzter Satz“ | ja, ausdrücklich als „kein Satz“ eingeordnet |
| Turn 2: letzter Satz „Es wird vorgeschlagen, … zu vereinbaren.“ wörtlich korrekt? | ja | ja | ja |
| Turn 2: Unterscheidung Satz / Unterschrift | ja, sauber | unsauber: nennt die Unterschrift „den letzten Satz“ und den echten Satz nur als „falls Sie … meinen“ | am klarsten |
| Erfundenes? | nein | nein | nein |
| Anrede | du | Sie | Sie |
| Kontrollfrage zeigt Vollständigkeit? | ja | ja | ja |

**Kurz:** Die Übung funktioniert. Alle drei Modelle haben das ganze Dokument erhalten und nennen das Dateiende korrekt und wörtlich. Unterschiede gibt es nur beim Stil. Haiku hält sich am genauesten an „bestätige kurz“. Opus fasst ungefragt zusammen, nennt dabei aber schon den Unterzeichner vom Dokumentende. Das ist ein frühes Zeichen, dass alles angekommen ist. Beim Kriterium „letzter Satz muss exakt mit dem Dateiende übereinstimmen“ muss der Trainer aufpassen: Die Datei endet mit einer Unterschrift und nicht mit einem Satz. Deshalb geben die Modelle zwei Antworten.

---

## Gefundene Fehler mit Beleg

- **Keine sachlichen Fehler, keine Halluzinationen.** Alle Zitate in Turn 2 stimmen Wort für Wort mit dem letzten Absatz von Abschnitt 7 und der letzten Zeile der Datei überein (geprüft per `tail`).
- Opus, Turn 1: Die Angaben „Version 1.0“, „Status: Entwurf zur Freigabe“ und „Dokument-Nr. PB-2024-017“ stehen in Zeile 4 der Datei. „Sieben Abschnitte“ stimmt (Überschriften `## 1.` bis `## 7.`). Die zwei Tabellen stehen in Abschnitt 4 und sind korrekt. „Unterzeichnet von Frank Albers, Fertigungstechnik“ entspricht der letzten Zeile. Alles korrekt.
- Sonnet, Turn 2: Die Begriffe sind ungenau. Die Unterschriftszeile wird als „letzter Satz“ bezeichnet. Das ist kein inhaltlicher Fehler, kann Teilnehmende aber verwirren, wenn sie den Wortlaut mit dem Original vergleichen.
- Kleinere Abweichung vom Auftrag „bestätige kurz“: Sonnet und vor allem Opus liefern eine Inhaltsübersicht, die niemand verlangt hat. Für die Übung schadet das nicht, es verbraucht aber Lesezeit.

---

## Lehren für die Auswertung

1. **„Ich habe es vollständig gelesen“ beweist nichts.** Alle drei Modelle sagen das. Sie würden es auch dann sagen, wenn der Text beim Einfügen abgeschnitten worden wäre. Erst die Kontrollfrage mit dem Abgleich am Original zeigt, ob alles angekommen ist. Genau das ist die Lehre: Behauptungen der KI prüfen, nicht glauben.
2. **Den Abgleich selbst machen.** Die Antwort auf „Was ist der letzte Satz?“ hilft nur, wenn man das echte Dateiende kennt. Teilnehmende sollen die Datei im Editor öffnen, ans Ende scrollen (Strg + Ende) und den Satz vergleichen.
3. **Das Dokument endet mit einer Unterschrift, nicht mit einem Satz.** Das ist realistisch, viele Berichte, Mails und Verträge enden so. Alle Modelle haben das sinnvoll gelöst. Es lohnt sich aber, kurz darauf hinzuweisen, damit niemand denkt, die KI habe „falsch“ geantwortet.
4. **„Kurz bestätigen“ wird unterschiedlich verstanden.** Das kleinste Modell hält sich am besten daran, das größte erzählt am meisten. Daran sieht man gut: Wer wirklich nur eine Bestätigung will, schreibt „Antworte nur mit ‚Erhalten‘“.
5. **In diesem Test trat kein Abschneiden auf.** Bei rund 1.850 Wörtern ist das bei aktuellen Tools normal. Der eigentliche Fehlerfall (Text unvollständig, KI merkt es nicht) lässt sich so nicht vorführen. Wer ihn zeigen will, fügt absichtlich nur die erste Hälfte ein und stellt dann die Kontrollfrage: Die KI nennt dann einen Satz aus der Mitte als „letzten Satz“, ohne zu warnen.

---

## Gesprächsprotokolle

### Haiku

**Nutzer 1**

Hier ist das Dokument, um das es geht: """[INHALT VON /home/daniel/tbc-ai-tutorials/07_Beispielmaterial/pruefbericht_lang.md]"""

Bitte lies es vollständig und bestätige kurz, dass du es hast. Warte dann auf meine Frage.

**Assistent 1**

Ich habe das Dokument vollständig gelesen. Es ist der Abnahmeprüfbericht PB-2024-017 zur Laserschneidanlage LS-3015 (Nordlicht Technik GmbH, Halle 3). Ich warte auf deine Frage.

**Nutzer 2**

Was ist der letzte Satz des Dokuments?

**Assistent 2**

Der letzte Text im Dokument ist die Signatur „Frank Albers, Fertigungstechnik“ (Unterschriftszeile am Ende).

Der letzte inhaltliche Satz des Fließtexts steht im Abschnitt 7 (Zusammenfassung und Empfehlung): „Es wird vorgeschlagen, bis zur Erledigung dieser Punkte einen Einbehalt von 5 % des Kaufpreises von der Schlusszahlung zu vereinbaren.“

### Sonnet

**Nutzer 1**

Hier ist das Dokument, um das es geht:

"""
[INHALT VON /home/daniel/tbc-ai-tutorials/07_Beispielmaterial/pruefbericht_lang.md]
"""

Bitte lies es vollständig und bestätige kurz, dass du es hast. Warte dann auf meine Frage.

**Assistent 1**

Ich habe das Dokument vollständig gelesen: den Abnahmeprüfbericht PB-2024-017 zur Laserschneidanlage LS-3015 (Nordlicht Technik GmbH, Halle 3). Er enthält 7 Abschnitte, von Anlass und Prüfumfang über die Einzelergebnisse und Messwerttabellen bis zur wirtschaftlichen Betrachtung, den offenen Punkten und der Empfehlung. Ich warte auf Ihre Frage.

**Nutzer 2**

Was ist der letzte Satz des Dokuments?

**Assistent 2**

Der letzte Satz des Dokuments ist die Unterschriftszeile am Ende des Berichts:

**„Frank Albers, Fertigungstechnik"**

Falls Sie den letzten inhaltlichen Satz meinen, steht dieser im Abschnitt 7 (Empfehlung): „Es wird vorgeschlagen, bis zur Erledigung dieser Punkte einen Einbehalt von 5 % des Kaufpreises von der Schlusszahlung zu vereinbaren."

### Opus

**Nutzer 1**

Hier ist das Dokument, um das es geht:

"""
[INHALT VON /home/daniel/tbc-ai-tutorials/07_Beispielmaterial/pruefbericht_lang.md]
"""

Bitte lies es vollständig und bestätige kurz, dass du es hast. Warte dann auf meine Frage.

**Assistent 1**

Ich habe das Dokument vollständig gelesen. Es ist der Abnahmeprüfbericht für die Laserschneidanlage LS-3015 der (fiktiven) Nordlicht Technik GmbH, Dokument-Nr. PB-2024-017, Version 1.0, Status „Entwurf zur Freigabe“. Er hat sieben Abschnitte, von „Anlass und Ziel der Prüfung“ bis „Zusammenfassung und Empfehlung“. Dazu gehören zwei Tabellen mit Messwerten und Kennwerten aus dem Dauerlauf. Unterzeichnet ist er von Frank Albers, Fertigungstechnik.

Ich warte auf Ihre Frage.

**Nutzer 2**

Was ist der letzte Satz des Dokuments?

**Assistent 2**

Der letzte vollständige Satz steht am Ende der Empfehlung in Abschnitt 7:

„Es wird vorgeschlagen, bis zur Erledigung dieser Punkte einen Einbehalt von 5 % des Kaufpreises von der Schlusszahlung zu vereinbaren.“

Danach kommt nur noch die Unterschriftszeile „Frank Albers, Fertigungstechnik“. Das ist kein Satz, sondern die Angabe, wer den Bericht erstellt hat.
