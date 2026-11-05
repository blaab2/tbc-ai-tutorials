# Testlauf: Übung 2 / Für Schnelle G – Minimal-Prompt „Fass das zusammen“

**Herkunft:** Aufgabe G, erster Prompt, aus [Uebung_2_Gute_Prompts.md](../06_Uebungen/Uebung_2_Gute_Prompts.md#aufgabe-g--baukasten-an-einem-anderen-beispiel) (Block 4, Stufe 3: Für Schnelle). Material: [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt). Zugehörige Lösungshinweise: [Trainer-Loesungshinweise.md – Übung 2](../06_Uebungen/Trainer-Loesungshinweise.md#übung-2-gute-prompts), Abschnitt „Woran du ein gutes Ergebnis erkennst“ (Aufgabe G), und die Aufgabentabelle bei [Übung 3, Station C](../06_Uebungen/Trainer-Loesungshinweise.md#station-c-notizen--protokoll-und-aufgabentabelle). Gegenstück: Baukasten-Prompt (ue2-g2).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt (jeweils in einem neuen Chat, Notizen vollständig eingefügt):**

```text
Fass das zusammen.

[HIER DIE NOTIZEN EINFÜGEN]
```

**Was laut Material herauskommen soll:** Eine Vergleichsbasis für den Baukasten-Prompt. Das Übungsblatt fragt: „Welche Aufgaben oder Termine findet nur der zweite Prompt?“ Es unterstellt also, dass der Minimal-Prompt eine allgemeine Zusammenfassung liefert, in der Aufgaben, Termine und der NACHTRAG (KW 22 statt KW 23) eher unvollständig vorkommen.

**Kurzfazit:** Der erwartete Effekt tritt **nicht** ein. Alle drei Modelle nennen alle 8 Aufgaben aus der Referenztabelle (Station C), übernehmen den NACHTRAG (KW 22) und stellen den Rabatt korrekt als offen dar. Sonnet und Opus bauen von sich aus eine Aufgabentabelle. Der Unterschied zum Baukasten-Prompt liegt bei diesem Material vor allem in **Länge und Format** (keine 5-Sätze-Grenze, keine einheitliche „offen“-Markierung), nicht in der Vollständigkeit.

---

## Bewertung

Referenz: die 8 Aufgaben aus der Tabelle bei Übung 3, Station C (1 Flyer/Druckerei, 2 Brenner anrufen + KW 22, 3 Prüfbericht LS-3015, 4 Lieferantenliste, 5 Reisekostenrichtlinie, 6 Rechnung RE-2024-0815, 7 Einarbeitungsplan Azubis, 8 Technik nach Standpersonal fragen).

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Aufgaben erwähnt (von 8) | **8/8** (Themenliste + Liste „Offene Punkte“) | **8/8** (Tabelle) | **8/8** (Themenliste + Tabelle „Wer/Was/Bis wann“) |
| Eigene Aufgabentabelle ungefragt? | nein, Stichpunktliste „Offene Punkte“ | ja (Thema, Maßnahme, Verantwortlich, Frist) | ja (Wer, Was, Bis wann) |
| NACHTRAG KW 22 übernommen? | ja, beim Thema Brenner und in den offenen Punkten („jetzt KW 22“) | ja, aber als eigener Abschnitt „Wichtige Korrektur“ unter der Tabelle; die Tabellenzeile zu Brenner nennt KW 22 nicht | ja, direkt eingearbeitet („schon in KW 22 (nicht wie zuerst gesagt in KW 23)“), auch in der Tabelle |
| KW 23 als gültiger Termin stehen geblieben? | nein (nur als ursprüngliche Meldung) | nein | nein |
| Rabatt als Entscheidung dargestellt? | nein („Es gab keine Einigung“) | nein (unter „Offen / ungeklärt“) | nein („**nicht entschieden**“) |
| Kaffeemaschine als offene Aufgabe? | nein (als „erledigt“ bei den Themen, nicht bei den offenen Punkten) | steht als Zeile in der Tabelle „Beschlüsse und Aufgaben“, aber mit „erledigt“ | nein (als erledigtes Thema, nicht in der Tabelle) |
| Widerspruch Q3 vs. vor dem Audit | **geglättet**: „irgendwann im Q3“ fehlt, nur „vor dem Lieferantenaudit … vermutlich Mitte Juni“ | beide genannt | beide genannt, als „strittig“ markiert |
| Druckerei-Termin Do/Fr offen? | ja | ja | ja |
| Standpersonal als feste Zusage? | nein („würden gehen“) | nein („würden gehen“) | nein („würden gehen“) |
| Konkrete Daten ausgerechnet (erfunden)? | nein | nein | nein |
| Erfundene Ergänzungen | keine inhaltlichen; kleine Zusatzaufgabe „Lieferantenaudit-Termin klären“ (sinnvoll, aber so nicht in den Notizen) | „Datum der Rechnung prüfen“ – ein Rechnungsdatum steht nirgends in den Notizen | keine; leichte Zuspitzungen („hat ihn offenbar niemand gelesen“, „Sabine lässt neue Flyer erstellen“) |
| Hinweis auf Unsicherheiten | ja („Protokoll wurde nicht formell geführt … vor Weitergabe prüfen“) | ja | ja, ausführlich mit Liste offener Punkte |
| Länge (ca.) | rund 380 Wörter, länger als die Notizen (265 Wörter) | rund 350 Wörter | rund 540 Wörter, gut doppelt so lang wie die Notizen |
| „Zusammenfassung“ im Wortsinn? | nein, eher ein umformuliertes Protokoll | nein, Protokoll mit Tabelle | nein, vollständiges Ergebnisprotokoll |

---

## Gefundene Fehler mit Beleg

**Haiku**

1. **Widerspruch geglättet, Jonas' Aussage fehlt.** Notizen: „Jonas räumt auf, „irgendwann im Q3“, Petra will es aber eigentlich vor dem Lieferantenaudit (wann ist das nochmal? Mitte Juni?)“. Haiku: „Jonas räumt auf. Petra möchte, dass das vor dem Lieferantenaudit passiert. Der Termin ist unklar (vermutlich Mitte Juni).“ Das „Q3“ fehlt, damit ist der Konflikt zwischen den beiden Terminen nicht mehr sichtbar. Genau diese Falle beschreiben die Lösungshinweise (Station C: „wird gern zu einem Termin geglättet“).
2. **Kleine Ergänzung:** „Lieferantenaudit-Termin klären“ steht als offener Punkt in der Liste. In den Notizen ist das eine Frage von Jonas („wann ist das nochmal?“), aber keiner Person zugeordnete Aufgabe. Harmlos, aber nicht aus den Notizen.
3. **Testartefakt, kein inhaltlicher Fehler:** Haiku hat die Format-Anweisung des Testaufbaus wörtlich genommen und das Gesprächsprotokoll am Ende noch einmal wiederholt („Gesprächsprotokoll (vollständig): … (siehe oben)“). Das passiert im echten Chat nicht.

**Sonnet**

1. **Erfundener Prüfpunkt:** „Vor dem Versand an Dritte würde ich die Fristen und das **Datum der Rechnung** noch einmal prüfen.“ Die Notizen nennen nur die Rechnungsnummer RE-2024-0815, kein Rechnungsdatum. Gemeint ist vermutlich das Besprechungsdatum („Di (?)“). Kleiner Fehler, aber gut zum Zeigen: Auch Hinweise der KI können ungenau sein.
2. **Kaffeemaschine in der Aufgabentabelle.** Sie steht als Zeile unter „Beschlüsse und Aufgaben“, wenn auch mit „erledigt“. Genau die Falle aus Station C, hier aber entschärft.
3. **NACHTRAG nicht in die Tabelle eingearbeitet.** Die Zeile „Brenner anrufen, Teillieferung von 60 Stück klären“ nennt keinen Liefertermin. Die Korrektur steht nur darunter. Wer nur die Tabelle kopiert, verliert KW 22.

**Opus**

1. Keine sachlichen Fehler. Leichte Zuspitzungen: Aus „hat den keiner gelesen?“ (Frage) wird „bisher hat ihn offenbar niemand gelesen“, aus „Sabine kümmert sich um neue Flyer“ wird „Sabine lässt neue Flyer erstellen“. Beides ist vertretbar, aber nicht wörtlich belegt.

**Alle drei:** Keine Zahlen falsch (60 Stück, max. 5 %, KW 22/23, LS-3015, ca. 6 Seiten, RE-2024-0815, 2 Azubis, 9:30 Uhr, in 2 Wochen – alles korrekt übernommen). Keine konkreten Kalenderdaten ausgerechnet.

---

## Lehren für die Auswertung

1. **Die erwartete Schwäche tritt nicht auf.** Die Frage „Welche Aufgaben oder Termine findet nur der zweite Prompt?“ wird im Test mit „keine“ beantwortet. Teilnehmende sollten das nicht als „falsch gemacht“ erleben. Gute Lehre daraus: **Wenn der Text selbst klar genug ist (Notizen mit Pfeilen und Namen), braucht die KI weniger Anleitung.** Der Baukasten wirkt vor allem dort, wo Informationen fehlen (wie in Aufgabe A/B ohne Material).
2. **Der eigentliche Unterschied ist Länge und Format.** „Fass das zusammen“ liefert bei allen drei Modellen Texte, die so lang oder länger sind als die Notizen (Haiku ca. 380, Sonnet ca. 350, Opus ca. 540 Wörter bei 265 Wörtern Notizen). Eine „Zusammenfassung“ im Sinn von „kurz“ ist das nicht. Der Baukasten-Prompt („höchstens 5 Sätze“, feste Tabellenspalten, „offen“) macht das Ergebnis **vorhersagbar und direkt weiterverwendbar** – gute Frage an die Gruppe: „Welches Ergebnis würdet ihr so ans Team schicken?“
3. **Ohne Vorgabe entscheidet die KI selbst, was eine Aufgabe ist.** Haiku macht eine Stichpunktliste, Sonnet eine Tabelle mit Kaffeemaschine, Opus eine Tabelle ohne. Bei drei Leuten im Team kommen drei verschiedene Formate heraus. Mit dem Baukasten-Prompt sind die Ergebnisse vergleichbar.
4. **Die Feinheiten unterscheiden sich trotzdem:** Haiku glättet den Widerspruch Q3 vs. Juni, Sonnet lässt KW 22 in der Tabelle weg. Das ist ein gutes Beispiel für „Gegenlesen bleibt Pflicht“, auch wenn das Ergebnis auf den ersten Blick vollständig wirkt.
5. **Prüffragen funktionieren gut als Checkliste:** NACHTRAG? Rabatt offen? Kaffeemaschine keine Aufgabe? Q3 und Juni beide genannt? Damit können Teilnehmende jedes Ergebnis in einer Minute selbst prüfen.
6. **Kleinere Tools oder ältere Versionen** können sehr wohl Aufgaben auslassen oder KW 23 übernehmen. Wenn das in der Gruppe passiert, ist es ein Geschenk für die Auswertung. Darauf verlassen sollte man sich aber nicht.

---

## Probleme im Material und Vorschläge

- **Übungsblatt, Aufgabe G, Auswertungsfrage:** „Welche Aufgaben oder Termine findet nur der zweite Prompt?“ setzt voraus, dass der erste Prompt etwas übersieht. Im Test war das bei keinem Modell der Fall.
- **Lösungshinweise, Aufgabe G:** beschreiben nur, was der Baukasten-Prompt liefern soll, nicht, was beim Minimal-Prompt typischerweise herauskommt. Trainer haben so keine Erwartung für den Vergleich.
- **Vorschlag Übungsblatt:** Frage ersetzen durch „Was ist beim zweiten Ergebnis anders – Länge, Aufbau, ‚offen‘-Markierungen? Fehlt beim ersten etwas? Hat die KI irgendwo etwas ergänzt? Und: Hat sie den **Nachtrag** berücksichtigt?“
- **Vorschlag Lösungshinweise (Aufgabe G):** Satz ergänzen wie „Der Minimal-Prompt liefert bei aktuellen Modellen oft schon alle Aufgaben und den Nachtrag, ist aber lang und uneinheitlich formatiert. Der Gewinn des Baukastens liegt hier vor allem in Kürze, festem Format und den ‚offen‘-Markierungen. Feinheiten prüfen: Q3 vs. Juni geglättet? KW 22 auch in der Tabelle? Kaffeemaschine als Aufgabe?“
- Die Richtzeit („wenn Zeit bleibt“) passt: Beide Prompts plus Vergleich mit der Checkliste dauern ca. 5–7 Minuten.

---

## Gesprächsprotokolle

### Haiku

#### Nutzer 1

Fass das zusammen.

[INHALT VON notizen_besprechung.txt]

*(Im Testaufbau folgte hier noch die technische Anweisung, das Gesprächsprotokoll in einem bestimmten Format zurückzugeben. Sie gehört nicht zur Übung.)*

#### Assistent 1

**Zusammenfassung der Teambesprechung Vertrieb/Technik** (Di, Raum 2.14)

**Teilnehmer:** Sabine K., Jonas, Fr. Yilmaz, Tom (später dazu), Petra W. (nur 1. Hälfte)

**Themen und Ergebnisse**

1. **Messe Hannover / Industrietage:** Der Stand ist gebucht, die Prospekte sind aber veraltet.
   - Sabine kümmert sich um neue Flyer. Die Druckerei braucht die Daten spätestens Ende nächster Woche (Freitag oder Donnerstag wegen Feiertag, noch unklar).
   - Das Standpersonal ist noch offen. Jonas und Fr. Yilmaz würden gehen. Sabine fragt noch bei der Technik nach.
2. **Kunde Brenner, Verzug SG-40:** Der Kunde ist verärgert. Die Fertigung meldete zunächst Gehäuse für KW 23.
   - Tom ruft Hrn. Brenner bis Mittwoch an und klärt eine Teillieferung von 60 Stück.
   - Nachtrag von Jonas: Laut Fertigung kommen die Gehäuse schon in **KW 22**. Tom soll das so an den Kunden weitergeben.
   - Rabatt: Petra schlägt maximal 5 % vor, nur mit GF-Freigabe. Es gab keine Einigung.
3. **Prüfbericht Laserschneidanlage LS-3015:** Der Bericht (ca. 6 Seiten) liegt vor. Fr. Yilmaz liest ihn und fasst ihn für die GF bis zum nächsten Jour fixe zusammen.
4. **Lieferantenliste:** Sie ist unübersichtlich (Dubletten, alte Nummern). Jonas räumt auf. Petra möchte, dass das vor dem Lieferantenaudit passiert. Der Termin ist unklar (vermutlich Mitte Juni).
5. **Reisekostenrichtlinie v2:** Die neue Version kommt. Niemand weiß genau, was sich geändert hat. Sabine fragt bei der Personalabteilung nach und schickt dem Team eine kurze Info.
6. **Rechnung RE-2024-0815 an Brenner:** Die Frachtkosten sind möglicherweise falsch berechnet, denn "frei Haus" war vermutlich vereinbart. Petra prüft das mit der Buchhaltung und stellt ggf. eine Gutschrift aus.
7. **Azubi-Projekt:** Tom betreut ab nächsten Monat zwei Azubis und erstellt bis Monatsende selbst einen Einarbeitungsplan.
8. **Kurz:** Die Kaffeemaschine im 2. OG ist kaputt. Der Hausmeister ist informiert (erledigt).

**Nächster Termin:** in zwei Wochen, gleicher Raum, 9:30 Uhr.

**Offene Punkte auf einen Blick**
- Flyer-Daten für die Druckerei (Ende nächster Woche)
- Anruf bei Hrn. Brenner bis Mittwoch, Teillieferung 60 Stück, Lieferung SG-40 jetzt KW 22
- Rabattentscheidung (GF)
- Prüfbericht LS-3015 zusammenfassen (Fr. Yilmaz)
- Lieferantenliste bereinigen (Jonas), Lieferantenaudit-Termin klären
- Reisekosteninfo (Sabine)
- Frachtkosten-Prüfung RE-2024-0815 (Petra)
- Einarbeitungsplan Azubis (Tom)
- Messe-Standpersonal (Sabine)

**Hinweis:** Das Protokoll wurde nicht formell geführt. Datum (Di mit Fragezeichen) und einige Termine sind unklar. Bitte vor der Weitergabe prüfen.

---

Gesprächsprotokoll (vollständig):

### Nutzer 1
Fass das zusammen.

[INHALT VON /home/daniel/tbc-ai-tutorials/07_Beispielmaterial/notizen_besprechung.txt]

Gib das komplette Gesprächsprotokoll zurück, Format:
### Nutzer 1
<Nachricht>
### Assistent 1
<deine vollständige Antwort>

### Assistent 1
(siehe oben, vollständige Zusammenfassung)

*(Ende der Haiku-Antwort. Der letzte Teil ab „Gesprächsprotokoll (vollständig)“ ist ein Artefakt des Testaufbaus, siehe Fehler Haiku Nr. 3.)*

### Sonnet

#### Nutzer 1

Fass das zusammen.

[Anhang: notizen_besprechung.txt]

#### Assistent 1

Hier die Zusammenfassung der Besprechung (Vertrieb/Technik, Raum 2.14, Wochentag laut Notiz unsicher: "Di (?)").

**Anwesend:** Sabine K., Jonas, Fr. Yilmaz, Tom (kam später), Petra W. (nur erste Hälfte). Die Notizen stammen von Jonas.

**Beschlüsse und Aufgaben**

| Thema | Maßnahme | Verantwortlich | Frist |
|---|---|---|---|
| Messe Hannover / Industrietage: Prospekte veraltet | Neue Flyer erstellen, Daten an die Druckerei | Sabine | Ende nächster Woche (Fr oder Do wegen Feiertag, unklar) |
| Messe: Standpersonal offen | Jonas und Fr. Yilmaz würden gehen, Technik wird noch gefragt | Sabine | offen |
| Kunde Brenner verärgert wegen Verzug beim SG-40 | Brenner anrufen, Teillieferung von 60 Stück klären | Tom | bis Mittwoch |
| Prüfbericht Laserschneidanlage LS-3015 (ca. 6 Seiten) | Lesen und für die Geschäftsführung zusammenfassen | Fr. Yilmaz | bis zum nächsten Jour fixe |
| Lieferantenliste (Dubletten, alte Nummern) | Bereinigen | Jonas | "irgendwann im Q3", Petra wünscht es vor dem Lieferantenaudit (Termin unklar, evtl. Mitte Juni) |
| Reisekostenrichtlinie v2: Änderungen unbekannt | Bei der Personalabteilung nachfragen, Kurzinfo ans Team | Sabine | keine Frist genannt |
| Rechnung RE-2024-0815 an Brenner: Frachtkosten evtl. falsch (frei Haus vereinbart?) | Mit Buchhaltung prüfen, ggf. Gutschrift | Petra | keine Frist genannt |
| Azubi-Projekt: Tom betreut ab nächstem Monat 2 Azubis | Einarbeitungsplan erstellen | Tom | Monatsende |
| Kaffeemaschine 2. OG defekt | Hausmeister informiert | erledigt | erledigt |

**Offen / ungeklärt**
- Rabatt für Brenner: Petra nannte maximal 5 %, nur mit Freigabe der Geschäftsführung. Die Diskussion blieb ohne Ergebnis.
- Genauer Abgabetermin für die Flyerdaten, Termin des Lieferantenaudits und Inhalt der neuen Reisekostenrichtlinie sind unklar.

**Wichtige Korrektur (Nachtrag von Jonas):** Laut Fertigung kommen die SG-40-Gehäuse doch schon in KW 22, nicht wie ursprünglich notiert in KW 23. Tom soll das so an den Kunden weitergeben. Das betrifft sein Gespräch mit Hr. Brenner.

**Nächster Termin:** in 2 Wochen, gleicher Raum, 9:30 Uhr.

**Hinweis:** In den Notizen stehen mehrere Unsicherheiten (Fragezeichen). Vor dem Versand an Dritte würde ich die Fristen und das Datum der Rechnung noch einmal prüfen.

### Opus

#### Nutzer 1

Fass das zusammen.

[Anhang: notizen_besprechung.txt]

#### Assistent 1

Hier ist die Zusammenfassung der Teambesprechung Vertrieb/Technik:

**Rahmendaten**
- Datum: vermutlich Dienstag (in den Notizen nicht sicher angegeben), Raum 2.14
- Anwesend: Sabine K., Jonas, Fr. Yilmaz, Tom (kam später dazu), Petra W. (nur in der ersten Hälfte)
- Mitschrift: Jonas (kein offizielles Protokoll)
- Nächster Termin: in 2 Wochen, gleicher Raum, 9:30 Uhr

**Themen und Ergebnisse**

1. **Messe Hannover / Industrietage**: Der Stand ist gebucht, die Prospekte sind aber veraltet. Sabine lässt neue Flyer erstellen. Die Druckerei braucht die Daten bis Ende nächster Woche. Ob das Freitag oder wegen des Feiertags Donnerstag ist, ist noch offen. Das Standpersonal steht noch nicht fest: Jonas und Fr. Yilmaz würden gehen, Sabine fragt noch in der Technik nach.
2. **Kunde Brenner, Lieferverzug SG-40**: Der Kunde ist verärgert. Laut Nachtrag kommen die Gehäuse **schon in KW 22** (nicht wie zuerst gesagt in KW 23). Tom ruft Herrn Brenner bis Mittwoch an, nennt ihm KW 22 und klärt eine Teillieferung von 60 Stück. Ein Rabatt wurde diskutiert (laut Petra höchstens 5 %, nur mit Freigabe der Geschäftsführung), aber **nicht entschieden**.
3. **Rechnung RE-2024-0815 an Brenner**: Die Frachtkosten sind möglicherweise falsch, weil wohl "frei Haus" vereinbart war. Petra prüft das mit der Buchhaltung und veranlasst gegebenenfalls eine Gutschrift.
4. **Prüfbericht Laserschneidanlage LS-3015**: Der Bericht (ca. 6 Seiten) liegt vor, bisher hat ihn offenbar niemand gelesen. Fr. Yilmaz liest ihn und fasst ihn bis zum nächsten Jour fixe für die Geschäftsführung zusammen.
5. **Lieferantenliste**: Sie ist unübersichtlich (Dubletten, veraltete Nummern). Jonas räumt sie auf, nach seiner Aussage "irgendwann im Q3". Petra möchte das aber vor dem Lieferantenaudit erledigt haben, das vermutlich Mitte Juni stattfindet. Der Termin ist **nicht geklärt**.
6. **Reisekostenrichtlinie v2**: Was sich ändert, weiß niemand genau. Sabine fragt bei der Personalabteilung nach und schickt eine kurze Info ans Team.
7. **Azubi-Projekt**: Tom betreut ab nächstem Monat 2 Azubis und erstellt bis Monatsende selbst einen Einarbeitungsplan.
8. **Kaffeemaschine 2. OG**: Sie ist kaputt, der Hausmeister ist informiert. Das Thema ist erledigt.

**Aufgaben im Überblick**

| Wer | Was | Bis wann |
|---|---|---|
| Sabine | Neue Messe-Flyer, Daten an die Druckerei | Ende nächster Woche (Do oder Fr, noch klären) |
| Sabine | Bei der Technik wegen Standpersonal nachfragen | offen |
| Sabine | Bei Personal zur Reisekostenrichtlinie v2 nachfragen, Info ans Team | offen |
| Tom | Hr. Brenner anrufen (Liefertermin KW 22, Teillieferung 60 Stk.) | Mittwoch |
| Tom | Einarbeitungsplan für die Azubis | Monatsende |
| Fr. Yilmaz | Prüfbericht LS-3015 lesen und für die GF zusammenfassen | nächster Jour fixe |
| Petra | Frachtkosten der Rechnung RE-2024-0815 mit der Buchhaltung prüfen, ggf. Gutschrift | offen |
| Jonas | Lieferantenliste bereinigen | strittig: Q3 oder vor dem Audit (Mitte Juni?) |

**Offene Punkte, die geklärt werden sollten**
- Ob Brenner einen Rabatt bekommt, ist offen. Die GF müsste das freigeben.
- Abgabetermin für die Druckerei: Donnerstag oder Freitag?
- Wann genau ist das Lieferantenaudit? Davon hängt die Frist für die Lieferantenliste ab.
- Wer betreut den Messestand?
- Das genaue Datum der Besprechung fehlt in den Notizen.

Hinweis: Diese Zusammenfassung beruht nur auf den Stichpunkten aus der Mitschrift. Fragezeichen und unsichere Angaben aus dem Original habe ich als "offen" bzw. "vermutlich" übernommen und nicht selbst ergänzt.

---

Zurück zum Übungsblatt: [Uebung_2_Gute_Prompts.md](../06_Uebungen/Uebung_2_Gute_Prompts.md) · Material: [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt)
