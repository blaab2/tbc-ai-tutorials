# Testlauf: Übung 2 / Für Schnelle F – KI verbessert den eigenen Prompt

**Herkunft:** [Übung 2, Stufe 3 „Für Schnelle“, Aufgabe F](../06_Uebungen/Uebung_2_Gute_Prompts.md#aufgabe-f--die-ki-verbessert-deinen-prompt). Turn 2 ist die Zusatzaufgabe aus den [Trainer-Lösungshinweisen, Übung 2, „Zusatzaufgaben für Schnelle“](../06_Uebungen/Trainer-Loesungshinweise.md) („… so umschreiben, dass ihn auch eine Kollegin ohne Vorkenntnisse nutzen kann – mit Ausfüllhinweisen“). Als „eigener Prompt aus Aufgabe E“ wurde die [Vorlage aus Aufgabe E](../06_Uebungen/Uebung_2_Gute_Prompts.md) verwendet, ausgefüllt mit den dort angegebenen Beispielwerten (Vertriebsinnendienst, Wochenbericht, „höchstens 150 Wörter / 3 Abschnitte“). Bezug für den Datenschutz: [Daten-Ampel](../03_Daten-Ampel.md).

**Testdatum:** Montag, 2. November 2026

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

Jeweils neuer, leerer Chat. Turn 1 wörtlich der Prompt aus Aufgabe F mit eingesetztem Prompt, Turn 2 wörtlich die Zusatzaufgabe aus den Lösungshinweisen. Keine Anhänge.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Turn 1: höchstens 5 Vorschläge | ja (5) | ja (5) | ja (5) |
| Vorschläge konkret, mit Formulierungsbeispiel | ja | ja | ja |
| Erkennt Mehrdeutigkeit „150 Wörter / 3 Abschnitte“ | ja | ja | ja |
| Zahlen/Fakten schützen („nichts erfinden, nichts hochrechnen“) | ja (knapp) | ja | ja (ausführlichster Vorschlag) |
| Zuordnung zu den Abschnitten / leerer Abschnitt geregelt | nein | ja | ja |
| Zielgruppe / Adressat präzisiert | kaum | ja (Lesezeit, Reihenfolge) | teilweise |
| Zeitraum (KW) ergänzt | ja | erst in Turn 2 | ja (Feld „KW“) |
| Erkennt: „DATEN-AMPEL BEACHTEN“ ist für die KI wirkungslos | ja | ja (am deutlichsten) | nur implizit |
| Lücke für Stichpunkte bleibt erhalten | ja | ja | ja (als strukturierte Felder) |
| „Frag nach statt erfinden“ bleibt erhalten | abgewandelt: [fehlt: …] + Rückfrage-Block am Ende | abgewandelt: [fehlt: …] + gebündelte Rückfrage | ja: erst max. 3 Rückfragen, dann Bericht |
| Vollständige verbesserte Version | ja | ja | ja |
| Wortzahl Original → verbesserte Version | 93 → 143 | 93 → 176 | 93 → 185 |
| Länge der gesamten Antwort Turn 1 / Turn 2 (Wörter) | 331 / 330 | 467 / 464 | 470 / 566 |
| **Substanziell besser oder nur länger?** | überwiegend besser; ein Vorschlag (Wortzahl nennen) nur scheinbar | besser; teils Annahmen ohne Grundlage („Reklamationen zuerst“) | besser; am nächsten am Lehrziel |
| Turn 2: Ausfüllhinweise je Lücke | ja (Hinweisliste unter dem Prompt) | ja (HINWEIS-Zeilen direkt im Prompt) | ja (Hinweise direkt in den Feldern, am leichtesten bedienbar) |
| Turn 2: Daten-Ampel-Hinweis | ja, aber mit selbst ausgedachten, als feststehend formulierten Regeln | ja, mit Vorbehalt („kenne eure Ampel nicht“) | ja, eigene Ampel-Übersicht, Verweis auf interne Regelung |
| Turn 2: Prüf-/Kontrollhinweis für das Ergebnis | ja (Checkliste) | ja („KI kann sich irren“, Tipps) | ja (Verantwortung bleibt bei dir, FAQ) |
| Widerspruch zur Daten-Ampel des Tutorials im eigenen Beispiel | ja (Kundenname + Angebotsnummer im Beispiel) | ja (Empfängerin-Name als Lücke) | leicht (Rabatt-Kondition, indirekter Kundenhinweis) |

**Gesamturteil:** Die Übung funktioniert wie gedacht. Alle drei Modelle halten die Vorgabe „höchstens 5“ ein, liefern konkrete und überwiegend sinnvolle Vorschläge und eine vollständige neue Version. Die Leitfrage „wirklich besser – oder nur länger?“ lässt sich gut beantworten: Die neuen Versionen sind 1,5–2,0-mal so lang wie das Original, die meisten Zusätze lösen aber echte Unklarheiten (Format eindeutig, Abschnittszuordnung, Zahlen schützen). Daneben gibt es in jeder Antwort mindestens einen Punkt, der nur länger oder sogar schlechter macht. Genau das ist der Lernstoff. Die Zusatzaufgabe (Turn 2) liefert bei allen drei brauchbare Vorlagen. Die Datenschutz-Beispiele der Modelle passen aber nicht immer zur Daten-Ampel des Tutorials.

---

## Gefundene Fehler mit Beleg

Keine erfundenen Fakten im engeren Sinn (es gab keine Quelldaten). Die Fehler betreffen Widersprüche zur [Daten-Ampel](../03_Daten-Ampel.md), Widersprüche innerhalb der Antwort und Scheinsicherheit.

1. **Haiku, Turn 2 – Beispiel widerspricht der eigenen Ampel-Regel und der Tutorial-Ampel.** Ausfüllhinweis: „Angebot AG-2026-114 an Kunde Müller raus“. Zwei Zeilen darunter schreibt Haiku selbst: „Gelb: Kundennamen nur als Kürzel“. Die Daten-Ampel des Tutorials zählt „Kunden- und Auftragsnummern“ zu dem, was beim Anonymisieren ersetzt wird (Abschnitt „Anonymisieren in 3 Schritten“, Schritt 1). Eine Kollegin ohne Vorkenntnisse würde das Beispiel genau so übernehmen.
2. **Haiku, Turn 2 – ausgedachte Ampel-Regeln als Tatsache.** In Turn 1 stand noch „Ich kenne eure Daten-Ampel nicht … z. B.“. In Turn 2 steht ohne Vorbehalt: „Grün: Angebotsnummern, Produktnamen, Stückzahlen. Gelb: Kundennamen nur als Kürzel. Rot: …“. Das stimmt nicht mit der Tutorial-Ampel überein: Dort ist Grün nur Öffentliches oder Anonymisiertes, und Angebots- oder Auftragsnummern werden ersetzt. Außerdem heißt sie bei Haiku in Turn 2 plötzlich „Datenschutz-Ampel“.
3. **Haiku, Turn 1 – Begründung und Lösung passen nicht zusammen.** Die Begründung lautet: „‚Frag nach‘ passt nicht in einen Bericht, der weitergeleitet wird.“ Die Lösung schreibt aber [fehlt: …]-Marker, einen Block „Rückfragen“ und die Wortzahl in den Bericht. Das muss vor dem Weiterleiten wieder heraus. Unklar bleibt auch, ob Rückfragen und Wortzahl zu den 150 Wörtern zählen.
4. **Haiku, Turn 1 – Scheinsicherheit „Nenne am Ende die Wortzahl“.** Sprachmodelle zählen Wörter unzuverlässig (siehe Testlauf [Demo 4b – Zählen](demo-4b-zaehlen.md)). Ein von der KI selbst genannter Zählwert ist kein Prüfschritt. Diesen Vorschlag kann man als „nur länger, nicht besser“ einstufen.
5. **Sonnet, Turn 2 – Lücke lädt zu einem Personennamen ein, gegen die eigene Regel.** Die Vorlage enthält „[NAME DER EMPFÄNGERIN, z. B. "unsere Vertriebsleiterin"]“. Im selben Prompt steht die Regel „Nenne keine … Namen einzelner Personen“. Der Daten-Ampel-Check auf dem Übungsblatt (Aufgabe E) sagt: „Keine echten Namen von Kunden oder Mitarbeitenden“.
6. **Sonnet, Turn 1 – Annahme ohne Grundlage im Prompt festgeschrieben.** „Reklamationen zuerst nennen, dann Aufträge, dann Angebote.“ Diese Priorität hat die Nutzerin nie genannt. Als Vorschlag ist das legitim. In der fertigen Version steht es aber als feste Regel. Außerdem kündigt Vorschlag 5 an „Gib daher ein kurzes Muster für jeden Abschnitt vor“, die verbesserte Version enthält aber nur Beschreibungen und kein Muster je Abschnitt.
7. **Sonnet, Turn 2 – HINWEIS-Zeilen im Kopiertext.** Die Ausfüllhinweise stehen innerhalb des Kopierblocks und müssen vor dem Absenden gelöscht werden. Für Ungeübte ist das fehleranfällig. Werden sie nicht gelöscht, schadet es meist nicht, es ist aber unsauber. Opus löst das eleganter: Die Hinweise stehen in den Feldklammern und werden beim Ausfüllen ersetzt.
8. **Opus, Turn 2 – Ampel-Beispiele leicht unscharf.** „Kunde Maschinenbau Süd“ wird als Anonymisierung vorgeschlagen. Die Tutorial-Ampel warnt in Schritt 3 vor indirekten Hinweisen („unser größter Kunde aus Hamburg“). Gelb: „Beträge eher gerundet oder als Größenordnung“. Laut Tutorial-Ampel sind „Angebote mit Preisen“ und „nicht veröffentlichte Geschäftszahlen“ Rot. Das Beispiel „Sonderrabatt 8 % für Kunde A“ ist eine Kondition, die Opus selbst unter Rot führt („vertrauliche Preise und Konditionen“). Ansprechpartner bei Unsicherheit ist bei Opus „die Teamleitung“, im Tutorial [ANSPRECHPARTNER IT] bzw. [DATENSCHUTZBEAUFTRAGTE/R].
9. **Alle drei – kleinere Redundanzen.** Opus nennt die KW doppelt (Überschrift „Wochenbericht KW [Nummer]“ und Feld „KW:“). Haiku lässt in Turn 2 den Kontext-Baustein weg (er ist in „Aufgabe“ aufgegangen). Das ist inhaltlich unschädlich.

---

## Lehren für die Auswertung

- **„Besser oder nur länger?“ an einem Beispiel durchgehen.** Die verbesserten Prompts sind ungefähr 1,5–2,0-mal so lang. Mit den Teilnehmenden Vorschlag für Vorschlag sortieren: *löst ein echtes Problem* (Format eindeutig, Abschnittszuordnung, „Zahlen genau übernehmen“), *Geschmackssache* (Reihenfolge Reklamationen zuerst, Stilmuster) und *nur scheinbar* (KI nennt selbst die Wortzahl).
- **Alle drei Modelle stolpern über dieselbe Stelle:** „höchstens 150 Wörter / 3 Abschnitte“. Der Schrägstrich stammt aus der Vorlage von Aufgabe E, wo er Alternativen trennt. Gute Lehre: Was für mich klar ist, ist für die KI mehrdeutig.
- **„DATEN-AMPEL BEACHTEN“ im Platzhalter ist eine Notiz für den Menschen, nicht für die KI.** Sonnet sagt das am deutlichsten. Anknüpfungspunkt: Die Daten-Ampel prüfe ich *selbst vor dem Einfügen*. Die KI kann sie nicht für mich einhalten, weil sie unsere Regeln nicht kennt.
- **Ausgedachte Ampel-Regeln.** Die Modelle erfinden plausible Ampel-Regeln (Haiku sogar ohne Vorbehalt). Das ist ein schönes Beispiel für „Die KI kennt deine Firma nicht“. Die gültige Ampel ist unsere, nicht die der KI. Und die Beispiele der KI selbst gegen die Ampel prüfen (Haiku: „Kunde Müller“, Sonnet: Name der Empfängerin).
- **Drei Varianten von „frag nach“ vergleichen:** erst fragen, dann schreiben (Opus) gegen Lücke markieren und am Ende fragen (Haiku, Sonnet). Beides ist vertretbar. Für einen Routinebericht ist die Marker-Variante oft praktischer, dafür muss man die Marker vor dem Weiterleiten entfernen. Gute Diskussionsfrage für die Reflexion.
- **Turn 2 zeigt eine echte Arbeitserleichterung:** strukturierte Eingabefelder (Opus) machen die Vorlage für Kolleginnen sofort nutzbar und gleichzeitig zuverlässiger. Gute Vorlage für den [TIPPS-KANAL].
- **Zeit:** Die Antworten sind mit 331–470 Wörtern (Turn 1) lang. Lesen und Bewerten dauert 4–6 Minuten. Für „wenn Zeit bleibt“ ist das passend, Turn 2 ist nur für sehr Schnelle realistisch.

---

## Gesprächsprotokolle

Der Nutzer-Prompt in Turn 1 ist bei allen drei Modellen identisch und steht unten nur einmal vollständig. Die Antworten sind ungekürzt.

### Prompt Turn 1 (für alle Modelle gleich)

```text
Hier ist ein Prompt, den ich regelmäßig verwenden möchte.
Wie kann ich ihn verbessern, damit die Ergebnisse zuverlässiger werden?
Nenne höchstens 5 konkrete Vorschläge und zeige mir dann die verbesserte
Version.

Rolle: Du bist eine erfahrene Assistenz der Vertriebsleitung.

Kontext: Ich arbeite im Vertriebsinnendienst eines mittelständischen technischen Herstellers. Ich brauche regelmäßig einen Wochenbericht zu Angeboten, Aufträgen und Reklamationen für unsere Vertriebsleiterin.
Wichtig ist uns: kurz, sachlich, wir duzen uns intern.

Aufgabe: Erstelle aus den Stichpunkten unten einen Wochenbericht.

Format: höchstens 150 Wörter / 3 Abschnitte mit Zwischenüberschrift (Erledigt, Offen, Entscheidung nötig).

Beispiel für den Stil: "Diese Woche 5 Angebote raus, 2 davon schon mit Rückmeldung."

Wenn dir Informationen fehlen, frag nach, statt etwas zu erfinden.

Stichpunkte:
[HIER JEDES MAL DIE AKTUELLEN STICHPUNKTE EINFÜGEN – DATEN-AMPEL BEACHTEN]
```

### Prompt Turn 2 (für alle Modelle gleich)

```text
Schreib meinen Prompt so um, dass ihn auch eine Kollegin ohne Vorkenntnisse nutzen kann – mit Ausfüllhinweisen.
```

---

### Haiku

#### Nutzer 1

(Prompt Turn 1, siehe oben)

#### Assistent 1

Hier sind fünf konkrete Verbesserungen:

1. **Zeitraum festlegen:** Ergänze Kalenderwoche und Datum (z. B. "KW 45, 03.11.–07.11."). Sonst kann der Bericht nicht sauber mit der Vorwoche verglichen werden.
2. **Format eindeutig machen:** "höchstens 150 Wörter / 3 Abschnitte" lässt offen, ob es 150 Wörter pro Abschnitt sind. Schreibe "insgesamt maximal 150 Wörter" und nenne die drei Überschriften exakt und in fester Reihenfolge.
3. **Umgang mit fehlenden Angaben festlegen:** "Frag nach" passt nicht in einen Bericht, der weitergeleitet wird. Besser: Fehlende Angaben werden als [fehlt: ...] markiert und die offenen Fragen stehen in einem separaten Block am Ende.
4. **Datenschutz klar regeln:** Lege fest, welche Daten rein dürfen (z. B. Projekt- oder Angebotsnummern statt vollständiger Kundennamen und Beträge, je nach Daten-Ampel). Der Platzhalter "DATEN-AMPEL BEACHTEN" ist für Kollegen ohne Vorwissen zu unklar.
5. **Prüfschritt ergänzen:** Bitte die KI am Ende, die Wortzahl zu nennen und zu prüfen, dass die drei Überschriften vorhanden sind. So fallen Abweichungen schneller auf.

Verbesserte Version:

Rolle: Du bist eine erfahrene Assistenz der Vertriebsleitung in einem mittelständischen technischen Hersteller.

Kontext: Ich bin im Vertriebsinnendienst und erstelle wöchentlich einen Bericht zu Angeboten, Aufträgen und Reklamationen für unsere Vertriebsleiterin. Der Bericht soll kurz, sachlich und im internen Du-Ton geschrieben sein.

Aufgabe: Erstelle aus den Stichpunkten unten einen Wochenbericht für KW [Nummer] ([Datum von–bis]).

Format:
- Insgesamt maximal 150 Wörter.
- Genau drei Zwischenüberschriften in dieser Reihenfolge: Erledigt, Offen, Entscheidung nötig.
- Unter jeder Überschrift kurze Sätze oder Stichpunkte. Stil-Beispiel: "Diese Woche 5 Angebote raus, 2 davon schon mit Rückmeldung."

Regeln:
- Verwende nur Angaben aus den Stichpunkten. Erfinde keine Zahlen, Namen, Termine oder Beträge.
- Fehlt eine Angabe, schreibe [fehlt: ...] an die passende Stelle.
- Ergänze am Ende einen Block "Rückfragen" mit maximal drei offenen Fragen, falls nötig.
- Nenne am Ende die Wortzahl des Berichts.

Stichpunkte:
[Aktuelle Stichpunkte einfügen. Nur Daten verwenden, die laut Daten-Ampel erlaubt sind.]

Hinweis: Ich kenne eure Daten-Ampel nicht. Trag die Regeln bitte direkt in den Prompt ein, z. B. "Grün: Angebotsnummern, Stückzahlen. Gelb: Kundennamen nur als Kürzel. Rot: Preise und Personendaten nicht eingeben."

#### Nutzer 2

(Prompt Turn 2, siehe oben)

#### Assistent 2

So kann eine Kollegin ohne Vorkenntnisse den Prompt nutzen:

**Anleitung in drei Schritten**

1. Kopiere den gesamten Prompt unten in ein neues Chatfenster.
2. Ersetze alle Felder in eckigen Klammern [ ] durch deine Angaben.
3. Schicke den Prompt ab und prüfe das Ergebnis mit der Checkliste am Ende.

**Der Prompt**

Rolle: Du bist eine erfahrene Assistenz der Vertriebsleitung in einem mittelständischen technischen Hersteller.

Aufgabe: Erstelle aus meinen Stichpunkten einen kurzen Wochenbericht für unsere Vertriebsleiterin. Der Bericht betrifft Angebote, Aufträge und Reklamationen.

Zeitraum: KW [Kalenderwoche, z. B. 45] ([Datum von–bis, z. B. 03.11.–07.11.])

Ton: kurz, sachlich, im internen Du-Ton.

Format:
- Insgesamt maximal 150 Wörter.
- Genau drei Zwischenüberschriften in dieser Reihenfolge: Erledigt, Offen, Entscheidung nötig.
- Kurze Sätze oder Stichpunkte, z. B. "Diese Woche 5 Angebote raus, 2 davon schon mit Rückmeldung."

Regeln:
- Verwende nur die Angaben aus meinen Stichpunkten. Erfinde nichts.
- Fehlt etwas, schreibe [fehlt: ...] an die passende Stelle.
- Am Ende kommt ein Block "Rückfragen" mit höchstens drei offenen Fragen an mich.
- Nenne am Ende die Wortzahl.

Meine Stichpunkte:
[Hier deine Stichpunkte einfügen. Nur Daten verwenden, die laut Datenschutz-Ampel erlaubt sind.]

**Ausfüllhinweise**

- **Zeitraum:** Kalenderwoche und Datum der aktuellen Woche eintragen. Beispiel: "KW 45 (03.11.–07.11.)".
- **Stichpunkte:** Schreibe kurze Stichpunkte, ein Thema pro Zeile. Beispiel: "Angebot AG-2026-114 an Kunde Müller raus, Rückmeldung offen" oder "Reklamation Charge 7781: Ersatzlieferung zugesagt".
- **Datenschutz-Ampel:** Bevor du Daten einfügst, prüfe die Ampel. Grün: Angebotsnummern, Produktnamen, Stückzahlen. Gelb: Kundennamen nur als Kürzel. Rot: vollständige Personendaten, Bankdaten und Preise nicht eingeben. Bei Unsicherheit die IT oder die Datenschutzbeauftragte fragen.
- **Fehlende Angaben:** Lass nichts raten. Wenn eine Angabe fehlt, steht im Bericht [fehlt: ...]. Das ist richtig so und kein Fehler.
- **Entscheidungen:** Alles, wofür die Vertriebsleitung zustimmen muss (z. B. Preisnachlass, Garantiefall), gehört in "Entscheidung nötig".

**Checkliste nach dem Ergebnis**

- [ ] Sind genau drei Überschriften vorhanden: Erledigt, Offen, Entscheidung nötig?
- [ ] Liegt die Wortzahl bei höchstens 150?
- [ ] Stehen nur Angaben drin, die auch in deinen Stichpunkten vorkommen?
- [ ] Sind keine Kundennamen oder Beträge drin, die laut Ampel nicht erlaubt sind?
- [ ] Ist der Ton sachlich und im Du?

---

### Sonnet

#### Nutzer 1

(Prompt Turn 1, siehe oben)

#### Assistent 1

Dein Prompt ist schon gut aufgebaut. Mit diesen fünf Änderungen wird er zuverlässiger:

1. **Format eindeutig machen.** "150 Wörter / 3 Abschnitte" lässt offen, ob beides gilt oder nur eines. Schreib: "Maximal 150 Wörter insgesamt, genau 3 Abschnitte mit diesen Überschriften, in dieser Reihenfolge". Lege auch fest, ob Aufzählungspunkte erlaubt sind. Dann bleibt das Layout jede Woche gleich.

2. **Den Hinweis "Daten-Ampel beachten" ausformulieren.** Die KI kennt deine Daten-Ampel nicht. Der Hinweis im Platzhalter wird deshalb nicht umgesetzt. Beschreib die Regel in einem Satz, zum Beispiel: "Nenne keine Kundennamen und keine personenbezogenen Daten, nutze stattdessen Kürzel wie 'Kunde A'." Passt das nicht zu deiner Ampel, ersetz den Satz durch deine tatsächliche Regel. Ohne Ampel-Regel kannst du den Hinweis streichen. Prüf außerdem vor dem Einfügen, ob die Stichpunkte in dieses Tool dürfen.

3. **Die Regel "nichts erfinden" konkreter machen.** "Frag nach" ist bei einem Routineprompt unklar: Soll die KI sofort stoppen oder trotzdem einen Bericht liefern? Besser: "Verwende nur Zahlen, Namen und Fakten aus den Stichpunkten. Ergänze nichts und rechne nichts hoch. Fehlt etwas Wichtiges, schreib im Bericht [fehlt: …] und stell am Ende eine gebündelte Rückfrage."

4. **Die Zuordnung zu den Abschnitten erklären.** Sag, was wohin gehört: "Erledigt" sind abgeschlossene Angebote, Aufträge und Reklamationen. "Offen" sind laufende Vorgänge mit Stand. "Entscheidung nötig" sind Punkte, bei denen die Vertriebsleiterin entscheiden muss, mit einem konkreten Vorschlag. Sag auch, was bei einem leeren Abschnitt passiert, zum Beispiel "Keine".

5. **Stil und Ton genauer fassen.** Nenne den Adressaten ("an die Vertriebsleiterin, per Du"), das Ziel ("in 1 Minute lesbar") und die Reihenfolge ("Wichtigstes zuerst, Reklamationen vor Angeboten"). Ein Beispielsatz reicht für den Ton, aber ein einzelner Satz kann dazu führen, dass die KI nur Zahlenfloskeln liefert. Gib daher ein kurzes Muster für jeden Abschnitt vor.

**Verbesserte Version**

```
Rolle: Du bist eine erfahrene Assistenz der Vertriebsleitung in einem mittelständischen technischen Hersteller.

Aufgabe: Erstelle aus den Stichpunkten unten den Wochenbericht des Vertriebsinnendiensts an unsere Vertriebsleiterin. Er soll in einer Minute lesbar sein.

Ton: kurz, sachlich, per Du (wir duzen uns intern), keine Floskeln.

Format:
- Maximal 150 Wörter insgesamt.
- Genau 3 Abschnitte mit diesen Zwischenüberschriften in dieser Reihenfolge:
  ## Erledigt – abgeschlossene Angebote, Aufträge, Reklamationen
  ## Offen – laufende Vorgänge mit aktuellem Stand
  ## Entscheidung nötig – Punkte, über die du entscheiden musst, jeweils mit meinem Vorschlag
- Pro Abschnitt kurze Sätze oder Stichpunkte. Reklamationen zuerst nennen, dann Aufträge, dann Angebote.
- Hat ein Abschnitt keinen Inhalt, schreib "Keine".

Stilbeispiel: "Diese Woche 5 Angebote raus, 2 davon schon mit Rückmeldung."

Regeln:
- Verwende nur Fakten, Zahlen und Namen aus den Stichpunkten. Erfinde nichts, schätze nichts und rechne nichts hoch.
- Fehlt eine wichtige Angabe, schreib an der Stelle [fehlt: …] und stell am Ende eine gebündelte Rückfrage.
- Datenschutz: Nenne keine Kundennamen und keine Namen einzelner Personen. Schreib stattdessen "Kunde A", "Kunde B" usw. [Passe diesen Satz an deine Daten-Ampel an.]

Stichpunkte der Woche:
[AKTUELLE STICHPUNKTE HIER EINFÜGEN]
```

#### Nutzer 2

(Prompt Turn 2, siehe oben)

#### Assistent 2

Hier ist eine Fassung für Kolleginnen ohne Vorkenntnisse. Sie hat zwei Teile: eine kurze Anleitung (nicht mitkopieren) und die Vorlage zum Kopieren. Die Stellen in eckigen Klammern [ ] füllt die Nutzerin aus. Ihre Hinweise stehen jeweils darunter und werden vor dem Absenden gelöscht.

**Anleitung (nur zum Lesen)**

1. Kopiere die Vorlage unten komplett in das Chatfenster.
2. Ersetze jede Stelle in eckigen Klammern durch deine Angaben.
3. Lösche die Zeilen mit "HINWEIS", bevor du auf Senden klickst.
4. Prüfe das Ergebnis immer gegen deine Stichpunkte, bevor du den Bericht weitergibst. Die KI kann sich irren.
5. Gib keine Daten ein, die laut unserer Daten-Ampel nicht in ein KI-Tool dürfen (zum Beispiel Kundennamen oder personenbezogene Angaben). Im Zweifel ersetze sie durch Kürzel wie "Kunde A" oder frag nach.

**Vorlage zum Kopieren**

```
Rolle: Du bist eine erfahrene Assistenz der Vertriebsleitung in einem mittelständischen technischen Hersteller.

Aufgabe: Erstelle aus meinen Stichpunkten unten den Wochenbericht des Vertriebsinnendiensts für [NAME DER EMPFÄNGERIN, z. B. "unsere Vertriebsleiterin"]. Er soll in einer Minute lesbar sein.

HINWEIS: Trage ein, an wen der Bericht geht. Die Anrede bleibt per Du.

Berichtszeitraum: [KALENDERWOCHE, z. B. KW 44, 27.10.–31.10.]

HINWEIS: Ohne Zeitraum kann die KI Ereignisse nicht richtig einordnen. Schreib hier die Woche hinein, über die berichtet wird.

Ton: kurz, sachlich, per Du, keine Floskeln.

Format:
- Maximal 150 Wörter insgesamt.
- Genau 3 Abschnitte mit diesen Überschriften in dieser Reihenfolge:
  Erledigt – abgeschlossene Angebote, Aufträge und Reklamationen
  Offen – laufende Vorgänge mit aktuellem Stand
  Entscheidung nötig – Punkte, bei denen du entscheiden musst, jeweils mit meinem Vorschlag
- Reklamationen zuerst nennen, dann Aufträge, dann Angebote.
- Hat ein Abschnitt keinen Inhalt, schreib "Keine".

Stilbeispiel: "Diese Woche 5 Angebote raus, 2 davon schon mit Rückmeldung."

Regeln:
- Verwende nur Fakten, Zahlen und Namen aus meinen Stichpunkten. Erfinde nichts und rechne nichts hoch.
- Fehlt eine wichtige Angabe, schreib an der Stelle [fehlt: …] und stell am Ende eine gebündelte Rückfrage.
- Nenne keine Kundennamen und keine Namen einzelner Personen. Schreib stattdessen "Kunde A", "Kunde B" usw.

Meine Stichpunkte:
[HIER DEINE STICHPUNKTE EINFÜGEN, EIN PUNKT PRO ZEILE]

HINWEIS: Schreib stichpunktartig, zum Beispiel:
- Angebote: 5 verschickt, 2 mit Rückmeldung
- Aufträge: 3 eingegangen, 1 davon eilig
- Reklamationen: 1 neu (Lieferverzug), 1 abgeschlossen
- Offene Frage: Rabatt für Kunde A, Entscheidung bis Freitag

Gib möglichst Anzahlen, Stand und Fristen an. Je vollständiger die Stichpunkte sind, desto weniger Rückfragen stellt die KI.
```

**Tipps für danach**

- **Fragt die KI zurück?** Beantworte die Fragen kurz im Chat. Dann erstellt sie den Bericht neu.
- **Passt Länge oder Ton nicht?** Schreib zum Beispiel "Kürzer, nur 100 Wörter" oder "Noch sachlicher".
- **Steht etwas im Bericht, das nicht in deinen Stichpunkten war?** Streich es oder bitte die KI, es zu entfernen.

Im Satz zum Datenschutz habe ich als Beispiel Kürzel statt Kundennamen genommen, weil ich eure Daten-Ampel nicht kenne. Ersetz ihn durch die Regel, die bei euch tatsächlich gilt.

---

### Opus

#### Nutzer 1

(Prompt Turn 1, siehe oben)

#### Assistent 1

Dein Prompt ist schon gut aufgebaut: Rolle, Kontext, Aufgabe, Format, Beispiel und die Regel zum Nachfragen sind alle da. Mit diesen fünf Änderungen werden die Ergebnisse noch zuverlässiger:

**1. Das Format eindeutig machen**
„höchstens 150 Wörter / 3 Abschnitte“ kann man als „entweder – oder“ lesen. Schreib besser: „Insgesamt höchstens 150 Wörter, aufgeteilt in genau 3 Abschnitte mit diesen Zwischenüberschriften: …“

**2. Festlegen, was in welchen Abschnitt gehört**
Die KI weiß sonst nicht sicher, wie Angebote, Aufträge und Reklamationen auf „Erledigt“, „Offen“ und „Entscheidung nötig“ verteilt werden. Schreib zum Beispiel: „Erledigt = abgeschlossen. Offen = läuft noch, mit nächstem Schritt. Entscheidung nötig = die Vertriebsleiterin muss etwas freigeben oder entscheiden.“ Leg auch fest, was passiert, wenn ein Abschnitt leer bleibt, etwa: „Wenn nichts zu entscheiden ist, schreib ‚Diese Woche nichts.‘“

**3. Zahlen und Fakten schützen**
Gerade bei Berichten ist das der häufigste Fehler. Ergänze: „Übernimm Zahlen, Beträge, Termine und Namen genau aus den Stichpunkten. Runde nichts, rechne nichts hoch und bewerte nichts, was nicht in den Stichpunkten steht.“

**4. Die Nachfrage-Regel genauer fassen**
„Frag nach“ führt manchmal dazu, dass die KI gar keinen Bericht liefert, oder dass sie trotzdem Lücken füllt. Besser: „Wenn etwas Wichtiges fehlt, zum Beispiel die Kalenderwoche oder der Status eines Vorgangs, stell zuerst höchstens 3 kurze Rückfragen und schreib den Bericht erst danach.“

**5. Eine feste Struktur für die Eingabe und die Ausgabe vorgeben**
Gib die Stichpunkte immer in denselben Blöcken ein (KW, Angebote, Aufträge, Reklamationen). Sag außerdem, dass die KI nur den fertigen Bericht ausgeben soll, ohne Einleitung und ohne Kommentar. Dann kannst du ihn direkt kopieren.

---

**Verbesserte Version:**

```
Rolle: Du bist eine erfahrene Assistenz der Vertriebsleitung.

Kontext: Ich arbeite im Vertriebsinnendienst eines mittelständischen
technischen Herstellers. Jede Woche schreibe ich für unsere
Vertriebsleiterin einen Bericht zu Angeboten, Aufträgen und
Reklamationen. Wir duzen uns intern. Der Ton ist kurz und sachlich.

Aufgabe: Erstelle aus den Stichpunkten unten den Wochenbericht.

Format:
- Überschrift: „Wochenbericht KW [Nummer]“
- Insgesamt höchstens 150 Wörter, aufgeteilt in genau 3 Abschnitte
  mit diesen Zwischenüberschriften:
  1. Erledigt – was diese Woche abgeschlossen wurde
  2. Offen – was noch läuft, jeweils mit nächstem Schritt
  3. Entscheidung nötig – was die Vertriebsleiterin entscheiden oder
     freigeben muss. Wenn es nichts gibt: „Diese Woche nichts.“
- Kurze Stichpunkte oder kurze Sätze, keine Floskeln.

Stilbeispiel: „Diese Woche 5 Angebote raus, 2 davon schon mit Rückmeldung.“

Regeln:
- Übernimm Zahlen, Beträge, Termine und Namen genau so, wie sie in den
  Stichpunkten stehen. Runde nichts, rechne nichts hoch und ergänze
  nichts.
- Wenn wichtige Angaben fehlen oder unklar sind, stell zuerst höchstens
  3 kurze Rückfragen und schreib den Bericht erst danach.
- Gib nur den fertigen Bericht aus, ohne Einleitung und ohne Kommentar.

Stichpunkte (Daten-Ampel beachten: keine vertraulichen oder
personenbezogenen Daten einfügen):
KW:
Angebote:
Aufträge:
Reklamationen:
Sonstiges / Entscheidungsbedarf:
```

Tipp: Teste den Prompt zwei- oder dreimal mit echten (unkritischen) Stichpunkten. Dann siehst du, ob die Aufteilung auf die Abschnitte so klappt, wie du es dir vorstellst.

#### Nutzer 2

(Prompt Turn 2, siehe oben)

#### Assistent 2

Hier ist eine Version, die man ohne Vorwissen ausfüllen kann. Alles in **[eckigen Klammern]** ersetzt man oder löscht es. Der Rest bleibt genau so stehen.

---

**Kurzanleitung für die Kollegin**

1. Kopiere den kompletten Text im grauen Kasten in den KI-Chat.
2. Füll nur den Teil **„Meine Stichpunkte“** ganz unten aus. Alles darüber bleibt unverändert.
3. Lösche die Hinweise in den eckigen Klammern und schreib deine Angaben hin. Ganze Sätze sind nicht nötig, Stichworte reichen.
4. Prüf vor dem Absenden die **Daten-Ampel** (siehe unten).
5. Wenn die KI Rückfragen stellt, beantworte sie kurz. Danach schreibt sie den Bericht.
6. Lies den Bericht vor dem Weiterleiten einmal durch, vor allem Zahlen, Termine und Namen. Die Verantwortung für den Inhalt bleibt bei dir.

**Daten-Ampel: Was darf rein?**
- 🟢 **Grün, unbedenklich:** Anzahl der Angebote und Aufträge, allgemeine Produktgruppen, Status wie „offen“ oder „erledigt“, interne Kürzel.
- 🟡 **Gelb, nur abstrahiert:** Kundennamen nur, wenn das bei euch erlaubt ist. Sonst „Kunde A“ oder „Kunde Maschinenbau Süd“ schreiben. Beträge eher gerundet oder als Größenordnung.
- 🔴 **Rot, nie eintragen:** Namen und Kontaktdaten von Ansprechpartnern, vertrauliche Preise und Konditionen, Vertragsdetails, Personaldaten.

Im Zweifel: lieber weglassen oder anonymisieren. Was bei euch genau gilt, steht in der internen Ampel-Regelung. Frag sonst bei der Teamleitung nach.

---

**Der Prompt zum Kopieren:**

```
Rolle: Du bist eine erfahrene Assistenz der Vertriebsleitung.

Kontext: Ich arbeite im Vertriebsinnendienst eines mittelständischen
technischen Herstellers. Jede Woche schreibe ich für unsere
Vertriebsleiterin einen Bericht zu Angeboten, Aufträgen und
Reklamationen. Wir duzen uns intern. Der Ton ist kurz und sachlich.

Aufgabe: Erstelle aus meinen Stichpunkten unten den Wochenbericht.

Format:
- Überschrift: „Wochenbericht KW [Nummer]“
- Insgesamt höchstens 150 Wörter, aufgeteilt in genau 3 Abschnitte
  mit diesen Zwischenüberschriften:
  1. Erledigt – was diese Woche abgeschlossen wurde
  2. Offen – was noch läuft, jeweils mit nächstem Schritt
  3. Entscheidung nötig – was die Vertriebsleiterin entscheiden oder
     freigeben muss. Wenn es nichts gibt: „Diese Woche nichts.“
- Kurze Stichpunkte oder kurze Sätze, keine Floskeln.

Stilbeispiel: „Diese Woche 5 Angebote raus, 2 davon schon mit Rückmeldung.“

Regeln:
- Übernimm Zahlen, Beträge, Termine und Namen genau so, wie sie in
  meinen Stichpunkten stehen. Runde nichts, rechne nichts hoch und
  ergänze nichts.
- Wenn wichtige Angaben fehlen oder unklar sind, stell zuerst höchstens
  3 kurze Rückfragen und schreib den Bericht erst danach.
- Gib nur den fertigen Bericht aus, ohne Einleitung und ohne Kommentar.

=== Meine Stichpunkte (nur diesen Teil ausfüllen) ===

KW: [Kalenderwoche als Zahl, z. B. 45]

Angebote: [Wie viele Angebote sind rausgegangen? Gab es schon
Rückmeldungen? Beispiel: "6 Angebote raus, 2 mit Rückmeldung,
1 Absage (Preis)"]

Aufträge: [Neue Aufträge, Anzahl und grob worum es geht. Beispiel:
"3 neue Aufträge, davon 1 Großauftrag Ersatzteile Kunde B"]

Reklamationen: [Neue, erledigte und offene Reklamationen mit Status.
Beispiel: "2 neu, 1 erledigt (Austausch geliefert), 1 offen – wartet
auf Prüfbericht Technik"]

Entscheidung nötig: [Was muss die Vertriebsleiterin entscheiden oder
freigeben? Beispiel: "Sonderrabatt 8 % für Kunde A freigeben?".
Wenn nichts: "nichts"]

Sonstiges: [Optional: alles, was sonst wichtig ist. Sonst leer lassen
oder löschen.]
```

---

**Häufige Fragen**

- **Ich habe zu einem Punkt nichts?** Schreib „nichts“ oder „keine“. Lass das Feld nicht einfach weg, sonst fragt die KI nach.
- **Der Bericht ist zu lang oder zu förmlich?** Schreib danach im Chat: „Bitte kürzer und lockerer, maximal 100 Wörter.“
- **Es stimmt eine Zahl nicht?** Schreib: „Korrigiere: Es waren 4 Angebote, nicht 5.“ Prüf danach den ganzen Bericht noch einmal.
- **Kann ich den Prompt speichern?** Ja. Leg ihn als Textbaustein oder Vorlage ab. Achte darauf, dass in der gespeicherten Vorlage keine echten Stichpunkte stehen bleiben.

---

Zurück zum [Übungsblatt Übung 2](../06_Uebungen/Uebung_2_Gute_Prompts.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md) · [Daten-Ampel](../03_Daten-Ampel.md)
