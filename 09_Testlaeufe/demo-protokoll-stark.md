# Testlauf: Demo-Alternative Block 4 – Starker Prompt: Ergebnisprotokoll

**Herkunft:** Demo-Prompts aus dem Input, Block 4 (Folie 14), Abschnitt „Alternative – Protokoll aus den Besprechungsnotizen“ in [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md#demo-prompts-aus-dem-input-block-4-folie-14). Material: [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt). Abgleich mit der erwarteten Aufgabentabelle bei [Übung 3, Station C](../06_Uebungen/Trainer-Loesungshinweise.md#station-c-notizen--protokoll-und-aufgabentabelle). Übungsblatt dazu: [Uebung_2_Gute_Prompts.md](../06_Uebungen/Uebung_2_Gute_Prompts.md).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

Getestet wurde nur der **starke** Prompt (der schwache Prompt „Schreib ein Protokoll.“ ist nicht Teil dieses Testlaufs).

**Prompt:**
```
Du bist Assistenz der Teamleitung. Unten stehen meine ungeordneten Notizen aus der Teambesprechung.
Mach daraus ein kurzes Ergebnisprotokoll für das Team.
Format: 1. Beschlüsse als Stichpunkte, 2. eine Tabelle mit den Spalten Aufgabe | Verantwortlich | Termin, 3. offene Fragen.
Erfinde nichts dazu – wenn ein Verantwortlicher oder Termin fehlt, schreib „offen“.

[Notizen einfügen]
```

**Erwartet (laut Lösungshinweisen):** drei Teile; Liefertermin **KW 22** (NACHTRAG); Rabatt (max. 5 %, nur mit GF-Freigabe, kein Ergebnis) als offene Frage, nicht als Beschluss; Kaffeemaschine nicht in der Tabelle; die 8 Aufgaben aus Station C; fehlende Termine „offen“, keine ausgerechneten Kalenderdaten.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Drei Teile im vorgegebenen Format | ja | ja | ja |
| NACHTRAG übernommen (KW 22) | ja | ja – aber zusätzlich „bitte mit Fertigung bestätigen“ (unnötig, siehe Fehler 4) | ja, mit transparentem Hinweis am Ende |
| Rabatt nur als offene Frage, nicht als Beschluss | **teilweise** – steht unter „Beschlüsse“ (mit „kein Ergebnis“) **und** wird zur Aufgabe | ja | **teilweise** – steht auch unter „Beschlüsse“, aber ausdrücklich „Es gab keinen Beschluss (siehe offene Fragen)“ |
| Kaffeemaschine nicht in der Tabelle | ja | **nein** – eigene Tabellenzeile | ja |
| Die 8 Aufgaben aus Station C vollständig | ja (8 von 8) | ja (8 von 8) | ja (8 von 8) |
| Keine erfundene Aufgabe | **nein** – „Rabatt-Anfrage Brenner: GF-Freigabe einholen“ | nein, aber Kaffeemaschine als 9. Zeile | ja (genau 8 Zeilen) |
| Termine: „offen“ bzw. Wortlaut, keine errechneten Kalenderdaten | ja | ja | ja |
| Widerspruch Q3 vs. Audit sichtbar | ja | ja | ja |
| Standpersonal nicht als feste Zusage | ja („würden teilnehmen“) | ja | ja |
| „Kurz“ eingehalten | eher nein (Beschlüsse doppeln die Tabelle) | eher nein | eher nein |
| **Gesamt für die Demo** | gut, 2 Schwächen | gut, klassische Kaffeemaschinen-Falle | sehr gut |

---

## Gefundene Fehler mit Beleg

1. **Haiku – Rabatt als erfundene Aufgabe.** Tabellenzeile: „Rabatt-Anfrage Brenner: GF-Freigabe einholen | offen | offen“. In den Notizen steht nur: „Rabatt?? Petra: max 5 %, nur mit GF-Freigabe. Diskussion, kein Ergebniss“. Dass jemand die GF-Freigabe einholen soll, wurde nicht beschlossen – das ist eine hinzugedichtete Aufgabe (9 statt 8 Zeilen). Die Spalten „offen | offen“ wirken korrekt nach Prompt-Regel, verschleiern aber, dass die Aufgabe selbst erfunden ist.
2. **Haiku – Rabatt unter „Beschlüsse“.** „Rabatt Brenner: Diskutiert, kein Ergebnis. Laut Petra sind maximal 5 % möglich, und nur mit GF-Freigabe.“ Inhaltlich richtig, aber im Abschnitt Beschlüsse. Wer nur die Überschrift liest, hält es für einen Beschluss. Ähnlich: „Standpersonal Messe: noch offen“ steht ebenfalls unter Beschlüsse.
3. **Sonnet – Kaffeemaschine in der Aufgabentabelle.** Zeile „Kaffeemaschine 2. OG melden | Hausmeister informiert | erledigt“. Laut Notizen „Hausmeister infomiert (erledigt)“ – also keine Aufgabe. Genau die Falle aus den Lösungshinweisen („landet oft als offene Aufgabe in der Tabelle“). Zusätzlich steht in der Spalte „Verantwortlich“ keine Person, sondern ein Status.
4. **Sonnet – unnötige Rückfrage zu KW 22.** Unter offene Fragen: „Lieferzeit SG-40: Hier gibt es zwei Angaben … Bitte mit der Fertigung bestätigen, bevor Tom den Kunden informiert.“ Der NACHTRAG sagt aber ausdrücklich „laut Fertigung … KW 22, Tom bitte so an Kunde weitergeben“. Die Rückfrage widerspricht der Anweisung in den Notizen und dem eigenen Beschluss/der eigenen Tabellenzeile (KW 22 mitteilen). Kein Faktenfehler, aber ein widersprüchliches Protokoll.
5. **Sonnet – Tippfehler aus der Vorlage übernommen.** „Teilieferung“ (zweimal) – stammt aus den Notizen („Teilieferung 60 Stk“); Haiku und Opus korrigieren zu „Teillieferung“. Kleinigkeit.
6. **Opus – Rabatt auch unter „Beschlüsse“.** „Rabatt für Brenner: Petra hat den Rahmen genannt … Es gab keinen Beschluss (siehe offene Fragen).“ Durch den ausdrücklichen Zusatz nicht irreführend, streng genommen aber nicht im richtigen Abschnitt. Außerdem holpriger Satz in den offenen Fragen: „muss die Lieferantenliste deshalb vorher fertig sein als ‚im Q3‘?“ (gemeint: früher als Q3).
7. **Haiku – Hinweis an falscher Stelle.** „Hinweis: Der nächste Termin ist in 2 Wochen, gleicher Raum, 9:30 Uhr.“ steht unter „Offene Fragen“, ist aber keine Frage.

**Nicht gefunden (positiv):** Kein Modell hat Kalenderdaten aus „bis Mittwoch“, „Ende nächster Woche“ oder „in 2 Wo“ errechnet. Kein Modell hat KW 23 als gültigen Termin übernommen. Kein Modell hat „5 % Rabatt“ als Entscheidung formuliert. Alle markieren Do/Fr bei der Druckerei als unklar und nennen den Widerspruch Q3 vs. Audit (Mitte Juni?).

---

## Lehren für die Auswertung

- **Der starke Prompt wirkt:** Alle drei Modelle liefern das gewünschte Format, übernehmen den NACHTRAG (KW 22) und erfinden keine Daten. Das ist der Kern der Demo – im Vergleich zum schwachen Prompt gut zeigbar.
- **Aber: Ein guter Prompt ersetzt das Prüfen nicht.** Jedes Modell hat genau eine typische Schwäche aus der Fallen-Liste: Sonnet packt die erledigte Kaffeemaschine in die Tabelle, Haiku macht aus dem Rabatt eine erfundene Aufgabe, Haiku und Opus führen den Rabatt (korrekt als „kein Ergebnis“) unter „Beschlüsse“. Die drei Prüffragen aus den Lösungshinweisen treffen also tatsächlich – gut für die Gruppe, das live abzuhaken.
- **„Erfinde nichts“ wird ernst genommen – aber eng ausgelegt.** Haiku erfindet keine Namen und Termine (schreibt brav „offen | offen“), erfindet aber eine ganze Aufgabe. Lehre: Die Regel „offen statt erfinden“ schützt Felder, nicht die Zeilen selbst.
- **Vorsicht kann auch stören:** Sonnet empfiehlt, KW 22 „mit der Fertigung zu bestätigen“, obwohl die Information von der Fertigung kommt. Ein Protokoll mit Widerspruch zwischen Tabelle und offenen Fragen ist schwer zu benutzen.
- **Nachschärfen zeigen (Live-Iteration):** Ein Satz im Prompt behebt die Schwächen meist: „Erledigte Punkte nicht in die Tabelle. Punkte ohne Ergebnis nur unter offene Fragen, nicht unter Beschlüsse. Nimm nur Aufgaben auf, die in den Notizen jemandem zugewiesen wurden.“ Das ist eine gute Brücke zum Baustein „Format/Regeln“.
- **„Kurz“ ist relativ:** Alle Protokolle wiederholen die Aufgaben fast vollständig unter „Beschlüsse“. Die Notizen enthalten kaum echte Beschlüsse, fast nur Zuweisungen – die Modelle füllen den Abschnitt trotzdem. Wer es kürzer will, kann „Beschlüsse nur, wenn etwas entschieden wurde“ ergänzen.
- **Opus als Positivbeispiel für Transparenz:** Der Schlusshinweis („zwei Angaben … den neueren Stand übernommen … bitte prüfen“) zeigt, wie ein Assistent Unsicherheit sichtbar macht, ohne das Protokoll zu verwässern.

---

## Gesprächsprotokolle

### Modell: Haiku

**Nutzer 1**

Du bist Assistenz der Teamleitung. Unten stehen meine ungeordneten Notizen aus der Teambesprechung. Mach daraus ein kurzes Ergebnisprotokoll für das Team. Format: 1. Beschlüsse als Stichpunkte, 2. eine Tabelle mit den Spalten Aufgabe | Verantwortlich | Termin, 3. offene Fragen. Erfinde nichts dazu – wenn ein Verantwortlicher oder Termin fehlt, schreib „offen".

[Anhang: notizen_besprechung.txt]

**Assistent 1**

**Ergebnisprotokoll: Teambesprechung Vertrieb/Technik**
Datum: Di (genaues Datum offen), Raum 2.14
Anwesend: Sabine K., Jonas, Fr. Yilmaz, Tom (später dazu), Petra W. (nur 1. Hälfte)

**1. Beschlüsse**
- Messe Hannover / Industrietage: Der Stand ist gebucht, die Prospekte sind aber veraltet. Sabine erstellt neue Flyer.
- Kunde Brenner (SG-40-Verzug): Laut Nachtrag von Jonas kommen die Gehäuse laut Fertigung bereits in KW 22 (vorher KW 23). Tom gibt diesen Termin an den Kunden weiter und klärt die Teillieferung über 60 Stück.
- Rabatt Brenner: Diskutiert, kein Ergebnis. Laut Petra sind maximal 5 % möglich, und nur mit GF-Freigabe.
- Prüfbericht Laserschneidanlage LS-3015: Fr. Yilmaz liest den Bericht und fasst ihn für die Geschäftsführung zusammen.
- Lieferantenliste: Jonas räumt auf. Der Zeitpunkt ist unklar ("irgendwann im Q3"). Petra wünscht die Bereinigung vor dem Lieferantenaudit.
- Reisekostenrichtlinie v2: Sabine fragt bei der Personalabteilung nach und informiert das Team.
- Rechnung RE-2024-0815 an Brenner: Petra prüft mit der Buchhaltung die Frachtkosten und ggf. eine Gutschrift.
- Azubi-Projekt: Tom betreut ab nächstem Monat 2 Azubis und erstellt dafür einen Einarbeitungsplan.
- Kaffeemaschine 2. OG: erledigt (Hausmeister informiert).
- Standpersonal Messe: noch offen. Jonas und Fr. Yilmaz würden teilnehmen, Sabine klärt das noch mit der Technik.

**2. Aufgaben**

| Aufgabe | Verantwortlich | Termin |
|---|---|---|
| Neue Prospekte/Flyer für Messe Hannover erstellen | Sabine K. | offen (Daten an Druckerei Ende nächster Woche, Tag unklar: Fr oder Do) |
| Hr. Brenner anrufen, Teillieferung 60 Stk. klären, neuen Liefertermin KW 22 weitergeben | Tom | bis Mittwoch |
| Rabatt-Anfrage Brenner: GF-Freigabe einholen | offen | offen |
| Prüfbericht LS-3015 lesen und für GF zusammenfassen | Fr. Yilmaz | bis zum nächsten Jour fixe |
| Lieferantenliste bereinigen (Dubletten, alte Nummern) | Jonas | offen (irgendwann im Q3, vor Lieferantenaudit gewünscht) |
| Änderungen Reisekostenrichtlinie v2 erfragen und ans Team senden | Sabine K. | offen |
| Rechnung RE-2024-0815 (Frachtkosten) prüfen, ggf. Gutschrift | Petra W. | offen |
| Einarbeitungsplan für 2 Azubis erstellen | Tom | Monatsende |
| Standpersonal Messe klären | Sabine K. (Rückfrage bei Technik) | offen |

**3. Offene Fragen**
- Datum der Messe Hannover / Industrietage ist nicht genannt.
- Abgabetermin für Druckdaten: Freitag oder Donnerstag?
- Rabatt Brenner: Wer holt die GF-Freigabe ein, und wie wird entschieden?
- War bei Brenner "frei Haus" vereinbart? Stimmen die Frachtkosten in RE-2024-0815?
- Genaues Datum des Lieferantenaudits ("Mitte Juni?").
- Welche Änderungen enthält die Reisekostenrichtlinie v2?
- Wer übernimmt das Standpersonal auf der Messe?
- Hinweis: Der nächste Termin ist in 2 Wochen, gleicher Raum, 9:30 Uhr.

---

### Modell: Sonnet

**Nutzer 1**

Du bist Assistenz der Teamleitung. Unten stehen meine ungeordneten Notizen aus der Teambesprechung.
Mach daraus ein kurzes Ergebnisprotokoll für das Team.
Format: 1. Beschlüsse als Stichpunkte, 2. eine Tabelle mit den Spalten Aufgabe | Verantwortlich | Termin, 3. offene Fragen.
Erfinde nichts dazu – wenn ein Verantwortlicher oder Termin fehlt, schreib „offen“.

[Anhang: notizen_besprechung.txt]

**Assistent 1**

**Ergebnisprotokoll Teambesprechung Vertrieb/Technik**
Datum: Dienstag (laut Notiz unsicher), Raum 2.14
Anwesend: Sabine K., Jonas, Fr. Yilmaz, Tom (später dazu), Petra W. (nur erste Hälfte)
Protokoll: Jonas
Nächster Termin: in 2 Wochen, gleicher Raum, 9:30 Uhr

**1. Beschlüsse**
- Messe Hannover / Industrietage: Der Stand ist gebucht. Die Prospekte sind veraltet und werden neu erstellt (Sabine).
- Kunde Brenner (Verzug SG-40): Tom ruft Hr. Brenner an und klärt die Teilieferung von 60 Stück. Laut Nachtrag von Jonas kommen die Gehäuse laut Fertigung bereits in KW 22 (statt KW 23). Tom gibt diesen Stand an den Kunden weiter.
- Prüfbericht Laserschneidanlage LS-3015: Fr. Yilmaz liest ihn und fasst ihn für die Geschäftsführung zusammen.
- Lieferantenliste: Jonas räumt sie auf.
- Reisekostenrichtlinie v2: Sabine fragt bei Personal nach den Änderungen und informiert das Team kurz.
- Rechnung RE-2024-0815 an Brenner: Petra prüft die Frachtkosten mit der Buchhaltung, gegebenenfalls folgt eine Gutschrift.
- Azubi-Projekt: Tom erstellt selbst einen Einarbeitungsplan.
- Kaffeemaschine 2. OG: Der Hausmeister ist informiert (erledigt).

**2. Aufgaben**

| Aufgabe | Verantwortlich | Termin |
|---|---|---|
| Neue Flyer erstellen und Daten an die Druckerei liefern | Sabine | Ende nächster Woche (Freitag oder Donnerstag wegen Feiertag, unklar) |
| Hr. Brenner anrufen, Teilieferung 60 Stk. klären, neuen Liefertermin KW 22 mitteilen | Tom | bis Mittwoch |
| Prüfbericht LS-3015 lesen und für die GF zusammenfassen | Fr. Yilmaz | bis zum nächsten Jour fixe |
| Lieferantenliste aufräumen (Dubletten, alte Nummern) | Jonas | „irgendwann im Q3“ (Petra wünscht es vor dem Lieferantenaudit) |
| Bei Personal zur Reisekostenrichtlinie v2 nachfragen und Kurzinfo ans Team schicken | Sabine | offen |
| Rechnung RE-2024-0815 mit Buchhaltung prüfen, ggf. Gutschrift | Petra | offen |
| Einarbeitungsplan für 2 Azubis erstellen | Tom | Monatsende |
| Standpersonal Messe: Technik anfragen | Sabine | offen |
| Kaffeemaschine 2. OG melden | Hausmeister informiert | erledigt |

**3. Offene Fragen**
- Messeflyer: Ist die Abgabefrist bei der Druckerei Freitag oder Donnerstag (Feiertag)?
- Rabatt für Brenner: Petra nannte maximal 5 %, nur mit GF-Freigabe. Die Diskussion blieb ohne Ergebnis.
- Lieferantenliste: Termin offen. Jonas plant Q3, Petra möchte sie vor dem Lieferantenaudit (Termin unklar, evtl. Mitte Juni).
- Reisekostenrichtlinie v2: Was hat sich geändert? Das weiß derzeit niemand.
- Frachtkosten Brenner: Wurde „frei Haus“ vereinbart? Das ist noch nicht bestätigt.
- Messe-Standpersonal: Jonas und Fr. Yilmaz würden teilnehmen. Ob weitere Personen aus der Technik dazukommen, klärt Sabine noch. Die endgültige Besetzung ist offen.
- Lieferzeit SG-40: Hier gibt es zwei Angaben (KW 23 in den Notizen, KW 22 im Nachtrag). Bitte mit der Fertigung bestätigen, bevor Tom den Kunden informiert.
- Datum der Besprechung: Der Wochentag („Di“) ist in den Notizen mit Fragezeichen versehen.

---

### Modell: Opus

**Nutzer 1**

Du bist Assistenz der Teamleitung. Unten stehen meine ungeordneten Notizen aus der Teambesprechung.
Mach daraus ein kurzes Ergebnisprotokoll für das Team.
Format: 1. Beschlüsse als Stichpunkte, 2. eine Tabelle mit den Spalten Aufgabe | Verantwortlich | Termin, 3. offene Fragen.
Erfinde nichts dazu – wenn ein Verantwortlicher oder Termin fehlt, schreib „offen“.

[Inhalt von notizen_besprechung.txt]

**Assistent 1**

**Ergebnisprotokoll – Teambesprechung Vertrieb/Technik**
Datum: offen (laut Notiz „Di (?)“) · Raum 2.14
Anwesend: Sabine K., Jonas, Fr. Yilmaz, Tom (kam später dazu), Petra W. (nur in der ersten Hälfte)
Protokoll: Jonas (aus seinen Mitschriften)

**1. Beschlüsse**

- **Messe Hannover / Industrietage:** Der Stand ist gebucht. Die Prospekte sind veraltet, deshalb werden neue Flyer erstellt.
- **Kunde Brenner / Verzug SG-40:** Tom ruft Herrn Brenner an und klärt eine Teillieferung von 60 Stück. **Aktueller Stand laut Nachtrag:** Die Gehäuse kommen schon in **KW 22** (nicht mehr wie zuerst gesagt in KW 23). Tom gibt diesen Termin so an den Kunden weiter.
- **Rabatt für Brenner:** Petra hat den Rahmen genannt: höchstens 5 %, nur mit Freigabe der Geschäftsführung. Es gab keinen Beschluss (siehe offene Fragen).
- **Prüfbericht Laserschneidanlage LS-3015:** Fr. Yilmaz liest den Bericht und fasst ihn für die Geschäftsführung zusammen.
- **Lieferantenliste:** Jonas bereinigt die Liste (Dubletten, veraltete Nummern).
- **Reisekostenrichtlinie v2:** Sabine fragt bei der Personalabteilung nach, was sich geändert hat, und schickt dem Team eine kurze Info.
- **Rechnung RE-2024-0815 an Brenner:** Petra prüft mit der Buchhaltung, ob die Frachtkosten stimmen, und veranlasst wenn nötig eine Gutschrift.
- **Azubi-Projekt:** Tom betreut ab nächstem Monat 2 Azubis und erstellt dafür einen Einarbeitungsplan.
- **Kaffeemaschine 2. OG:** Der Hausmeister ist informiert. Erledigt.
- **Nächster Termin:** in 2 Wochen, gleicher Raum, 9:30 Uhr.

**2. Aufgaben**

| Aufgabe | Verantwortlich | Termin |
|---|---|---|
| Neue Flyer für die Messe erstellen, Druckdaten an die Druckerei liefern | Sabine K. | Ende nächster Woche (Do oder Fr ist unklar, wegen Feiertag) |
| Hr. Brenner anrufen: Liefertermin Gehäuse KW 22 mitteilen, Teillieferung 60 Stk. klären | Tom | bis Mittwoch |
| Prüfbericht LS-3015 lesen und für die GF zusammenfassen | Fr. Yilmaz | bis zum nächsten Jour fixe |
| Lieferantenliste bereinigen | Jonas | offen (Jonas: „irgendwann im Q3“; Petra wünscht: vor dem Lieferantenaudit) |
| Bei Personal nachfragen, was in der Reisekostenrichtlinie v2 neu ist, Kurzinfo ans Team | Sabine K. | offen |
| Frachtkosten Rechnung RE-2024-0815 mit Buchhaltung prüfen, ggf. Gutschrift | Petra W. | offen |
| Einarbeitungsplan für 2 Azubis erstellen | Tom | bis Monatsende |
| Bei der Technik nachfragen, wer am Messestand mitarbeitet | Sabine K. | offen |

**3. Offene Fragen**

- **Rabatt für Brenner:** Bekommt der Kunde einen Rabatt (höchstens 5 %, nur mit GF-Freigabe)? Es gab eine Diskussion, aber kein Ergebnis.
- **Abgabe bei der Druckerei:** Müssen die Daten am Donnerstag oder am Freitag dort sein (wegen Feiertag)?
- **Lieferantenaudit:** Wann ist das Audit genau (Mitte Juni?) und muss die Lieferantenliste deshalb vorher fertig sein als „im Q3“?
- **Standpersonal Messe:** Jonas und Fr. Yilmaz würden mitgehen. Ob jemand aus der Technik dazukommt, ist noch offen.
- **Rechnung RE-2024-0815:** War für Brenner wirklich „frei Haus“ vereinbart?
- **Reisekostenrichtlinie v2:** Was sich geändert hat, weiß noch niemand. Die Antwort kommt von Sabine.
- **Datum der Besprechung:** Der Wochentag ist nur mit „Di (?)“ notiert, ein genaues Datum fehlt.

*Hinweis:* Für den SG-40-Liefertermin gibt es in den Notizen zwei Angaben: zuerst KW 23, im Nachtrag von Jonas dann KW 22. Ins Protokoll habe ich den neueren Stand aus dem Nachtrag übernommen (KW 22). Bitte vor dem Versand kurz prüfen, ob das stimmt.
