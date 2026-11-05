# Testlauf: Übung 3 / Station C Für Schnelle – Tagesordnung für die nächste Besprechung

**Herkunft:** [Übung 3, Station C, Abschnitt „Für Schnelle“](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#station-c-chaotische-notizen--protokoll-und-aufgabenliste), dritter Punkt: „Lass dir eine Tagesordnung für die **nächste** Besprechung vorschlagen, basierend auf den offenen Punkten.“ Material: [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt). Abgleich mit den [Trainer-Lösungshinweisen, Übung 3 / Station C](../06_Uebungen/Trainer-Loesungshinweise.md#station-c-notizen--protokoll-und-aufgabentabelle). Dort gibt es keinen eigenen Erwartungswert für die Tagesordnung, nur die Aufgabentabelle und die Fallen.

**Testdatum:** Montag, 2. November 2026

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

Ablauf: Zuerst lief der Basis-Prompt aus Station C (Protokoll) mit der Datei als Anhang, danach im selben Chat der Folgeprompt „Schlage mir eine Tagesordnung für die nächste Besprechung vor, basierend auf den offenen Punkten.“ Der Prompt steht so nicht wörtlich auf dem Übungsblatt, er wurde aus der Aufgabenbeschreibung abgeleitet.

---

## Erwartung (aus den Notizen abgeleitet)

Eine gute Tagesordnung enthält die offenen Punkte bzw. die Rückmeldungen zu den vergebenen Aufgaben:

| Offener Punkt | Quelle in den Notizen |
|---|---|
| Rabatt Brenner (max. 5 %, GF-Freigabe, kein Ergebnis) | „Rabatt?? Petra: max 5 %, nur mit GF-Freigabe. Diskussion, kein Ergebniss“ |
| Standpersonal Messe | „Messe: Standpersonal noch offen, Jonas + Fr. Yilmaz würden gehn, Sabine fragt noch Technik“ |
| Flyer / Druckerei (Do oder Fr?) | „Druckerei braucht Daten spätestens Ende nächster Woche (Fr? oder Do wg Feiertag??)“ |
| Brenner-Lieferung, Gehäuse KW 22 (Nachtrag), Teillieferung 60 Stk. | Hauptteil KW 23, NACHTRAG: „doch schon KW 22“ |
| Zusammenfassung Prüfbericht LS-3015 | „Fr. Yilmaz liest + fasst zusammen für GF, bis zum nächsten Jour fixe“ |
| Lieferantenliste / Audittermin | „irgendwann im Q3“ vs. „vor dem Lieferantenaudit (… Mitte Juni?)“ |
| Reisekostenrichtlinie v2 | „Sabine fragt bei Personal nach + schickt kurze Info ans Team“ |
| Rechnung RE-2024-0815 (frei Haus?) | „Petra prüft mit Buchhaltung, ggf Gutschrift“ |
| Rahmen: in 2 Wochen, Raum 2.14, 9:30 Uhr, **kein** Kalenderdatum | „Nächster Termin: in 2 Wo, gleicher Raum, 9:30“; Besprechungsdatum nur „Di (?)“ |
| **Nicht** als TOP: Kaffeemaschine | „Hausmeister infomiert (erledigt)“ |

Das Azubi-Projekt (Einarbeitungsplan bis Monatsende) ist eine vergebene Aufgabe und kann als Statuspunkt auftauchen. Das ist kein Fehler.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Rabatt Brenner | ja (TOP 3) | ja (TOP 2) | ja (TOP 2.3) |
| Standpersonal Messe | ja (TOP 2) | ja (TOP 3) | ja (TOP 3.2) |
| Flyer / Druckerei | ja (TOP 2) | ja (TOP 3) | ja (TOP 3.1) |
| Brenner-Lieferung / Teillieferung | ja, aber „KW 22 oder KW 23 klären“ | ja, „KW 22 oder KW 23“ bestätigen | ja, KW 22 aus dem Nachtrag übernommen |
| Prüfbericht-Zusammenfassung | ja (TOP 4) | ja (TOP 4) | ja (TOP 4) |
| Lieferantenliste / Audit | ja (TOP 5) | ja (TOP 5) | ja (TOP 5) |
| Reisekostenrichtlinie v2 | ja (TOP 6) | ja (TOP 1 + TOP 6, doppelt) | ja (TOP 6) |
| Rechnung RE-2024-0815 | ja (TOP 3) | ja (TOP 1 + TOP 2, doppelt) | ja (TOP 2.4) |
| Ort/Zeit 2.14, 9:30 korrekt | ja | ja | ja |
| Kein erfundenes Kalenderdatum | ja | ja | ja, sogar „[genaues Datum bitte ergänzen]“ |
| Kaffeemaschine nicht als TOP | ja | ja | ja |
| Verantwortliche je Punkt | teilweise (im Text) | teilweise (nur TOP 1) | ja, bei jedem Unterpunkt |
| Zeitplanung | keine | ja, Summe 75 Min. (nicht angegeben) | ja, 65 Min., aber „ca. 60 Minuten“ angegeben |
| Erfundene Inhalte | keine | keine | keine (Vorschläge als „Tipps“ gekennzeichnet) |
| **Gesamt** | **erfüllt** | **erfüllt** | **erfüllt, am vollständigsten** |

Gesamturteil: Alle drei Modelle liefern eine brauchbare Tagesordnung mit allen acht offenen Punkten. Keins erfindet ein Datum, keins nimmt die Kaffeemaschine auf. Die Unterschiede liegen in Struktur und Zusatznutzen, nicht in der Richtigkeit.

---

## Gefundene Fehler mit Beleg

Keine schweren Fehler. Kleinere Ungenauigkeiten:

1. **Opus: Zeitsumme stimmt nicht.** Angegeben ist „Geplante Dauer: ca. 60 Minuten“. Die TOPs addieren sich zu 5 + 15 + 10 + 10 + 10 + 5 + 5 + 5 = **65 Minuten** (mit python3 nachgerechnet). Kleiner Fehler, aber ein gutes Beispiel: Auch einfache Summen prüfen.
2. **Sonnet: Zeitsumme nicht genannt.** Die Einzelzeiten ergeben 10 + 15 + 15 + 10 + 10 + 5 + 5 + 5 = **75 Minuten**. Das sagt Sonnet nicht. Wer eine Stunde eingeplant hat, merkt es erst beim Nachrechnen.
3. **Sonnet: Doppelungen.** Rechnung RE-2024-0815 und Reisekostenrichtlinie kommen jeweils zweimal vor (TOP 1 „Rückmeldungen“ und eigener TOP 2 bzw. 6). Das ist kein inhaltlicher Fehler, kostet in der Sitzung aber Zeit.
4. **Sonnet: „ganztägig teilzunehmen“.** Gemeint ist offenbar „die ganze Sitzung“. Die Besprechung ist kein ganztägiger Termin, in den Notizen steht nur „nur 1. hälfte“.
5. **Haiku und Sonnet: KW 22 wieder offen.** Beide schreiben „KW 22 oder KW 23 klären/bestätigen“. Laut NACHTRAG gilt KW 22 („laut Fertigung kommen die SG-40 Gehäuse doch schon KW 22“). Als Prüfpunkt für die nächste Sitzung ist das vertretbar. Es zeigt aber, dass der Nachtrag schon im Protokoll nur halb übernommen wurde. Haiku hatte im Protokoll „[UNKLAR, welcher Termin gilt]“ geschrieben.
6. **Haiku: fragwürdige Begründung.** „Vorab zu klären: Datum der Besprechung und Termin des Lieferantenaudits, damit die Reihenfolge der Punkte 5 und 3 passt.“ Warum diese Termine die Reihenfolge von TOP 3 und 5 beeinflussen sollen, wird nicht erklärt. Das klingt plausibel, ist aber inhaltsleer.
7. **Haiku: Perspektive.** TOP 8 heißt „Erledigte und offene Aufgaben aus der **heutigen** Besprechung“. Gemeint ist die letzte Besprechung.
8. **Opus: kleine Zuschreibung.** „Am besten klärt Petra die GF-Freigabe vorher“ und bei TOP 2.3 „Liegt die Freigabe vor? *(Petra)*“. In den Notizen hat niemand den Auftrag, die GF-Freigabe einzuholen. Opus kennzeichnet das als Tipp, das ist in Ordnung. Wer die Tagesordnung verschickt, sollte es aber nicht als vereinbarte Aufgabe darstellen.
9. **Haiku (Protokoll, Vorstufe):** Tippfehler „Lieferantenauditons“.

**Hinweis zum Testlauf:** In der Haiku-Abschrift steht in „Nutzer 2“ eine Formatanweisung des Testskripts („Gib das komplette Gesprächsprotokoll zurück …“). Das gehört nicht zur Übung und hat das Ergebnis nicht beeinflusst.

---

## Lehren für die Auswertung

- **Die Aufgabe funktioniert wie gedacht und eignet sich gut als Erfolgserlebnis.** Alle drei Modelle liefern ohne Nacharbeit eine brauchbare Tagesordnung. Sie eignet sich zum Zeigen, wie man aus einem bereits geprüften Protokoll schnell den nächsten Schritt baut.
- **Zuerst prüfen, dann weiterbauen.** Die Tagesordnung ist nur so gut wie das Protokoll davor. Haiku und Sonnet haben die Unsicherheit KW 22/23 aus dem Protokoll in die Tagesordnung übernommen. Frage an die Gruppe: „Was gilt laut Nachtrag?“
- **Checkliste für Teilnehmende:** Sind alle acht offenen Punkte drin? Steht ein erfundenes Datum drin („Dienstag, 17. …“)? Ist die Kaffeemaschine raus? Kein Modell hat hier Fehler gemacht. Das ist kein Grund, den Prüfschritt zu überspringen.
- **Zeitangaben nachrechnen.** Opus nennt 60 Minuten, die Einzelzeiten ergeben 65. Bei Sonnet ergeben sie 75 Minuten, eine Summe nennt Sonnet nicht. Kleiner Fehler, guter Lerneffekt: KI-Zahlen auch dann prüfen, wenn sie nebensächlich wirken.
- **Mehrwert vs. Zutat.** Sonnet und Opus geben nützliche Hinweise (Protokollführung festlegen, Petra die ganze Zeit dabei haben, Brenner-Block nach vorne). Das steht so nicht in den Notizen, ist aber als Vorschlag gekennzeichnet. Unterschied zu Erfindung besprechen: Ein Vorschlag ist erlaubt, eine erfundene Tatsache nicht.
- **Modellunterschiede zeigen:** Haiku ist knapp und funktional. Sonnet bringt Zeiten, ist aber doppelt. Opus liefert die einladungsfertigste Fassung (Verantwortliche je Punkt, Platzhalter für das Datum, Angebot einer Einladungsmail). Für eine Tagesordnung reicht auch das kleine Modell.
- **Mögliche Anschlussfrage:** „Formuliere daraus eine Einladungsmail.“ Dann prüfen, ob dabei ein konkretes Datum erfunden wird. Dort liegt die eigentliche Falle (relative Termine, siehe Lösungshinweise).

---

## Gesprächsprotokolle

### Haiku

#### Nutzer 1
Hier sind meine Stichpunkt-Notizen aus einer Teambesprechung. Sie sind unordentlich.
Mach daraus ein sauberes Protokoll mit diesen Abschnitten:
1. Teilnehmende
2. Besprochene Themen (je 1–3 Sätze)
3. Entscheidungen
4. Offene Fragen

Erfinde nichts dazu. Wenn etwas in den Notizen unklar ist, markiere es mit [UNKLAR].

[Anhang: notizen_besprechung.txt]

#### Assistent 1
**Protokoll: Teambesprechung Vertrieb/Technik**

**Datum/Ort:** Dienstag [UNKLAR, Datum fehlt], Raum 2.14
**Protokoll:** [UNKLAR, ob J. für Jonas steht]

**1. Teilnehmende**
- Sabine K.
- Jonas
- Fr. Yilmaz
- Petra W. (nur erste Hälfte)
- Tom (kam später dazu)

**2. Besprochene Themen**

- **Messe Hannover / Industrietage:** Der Stand ist gebucht, die Prospekte sind aber veraltet. Die Druckerei braucht die Daten spätestens Ende nächster Woche, der genaue Tag ist [UNKLAR] (Freitag oder Donnerstag wegen Feiertag).
- **Kunde Brenner, Verzug SG-40:** Der Kunde ist verärgert. Die Fertigung nannte zunächst KW 23 für die Gehäuse, laut Nachtrag von Jonas soll es aber KW 22 sein [UNKLAR, welcher Termin gilt]. Zusätzlich geht es um eine Teillieferung von 60 Stück und einen möglichen Rabatt (Petra: maximal 5 %, nur mit GF-Freigabe). Zum Rabatt gab es keine Einigung.
- **Prüfbericht Laserschneidanlage LS-3015:** Der Bericht (ca. 6 Seiten) liegt vor. Ob er bereits gelesen wurde, ist [UNKLAR].
- **Lieferantenliste:** Die Liste ist unübersichtlich, mit Dubletten und alten Nummern. Petra möchte sie vor dem Lieferantenaudit bereinigen, der Termin ist [UNKLAR] (vermutlich Mitte Juni).
- **Reisekostenrichtlinie v2:** Eine neue Version kommt. Welche Änderungen es gibt, ist im Team [UNKLAR].
- **Rechnung RE-2024-0815 an Brenner:** Die Frachtkosten könnten falsch sein. Ob „frei Haus“ vereinbart war, ist [UNKLAR].
- **Azubi-Projekt:** Tom betreut ab dem nächsten Monat zwei Azubis und braucht dafür einen Einarbeitungsplan.
- **Messe-Standpersonal:** Noch offen. Jonas und Fr. Yilmaz würden teilnehmen, Sabine klärt die Technik-Seite.
- **Kurz:** Die Kaffeemaschine im 2. OG ist kaputt. Der Hausmeister ist informiert (erledigt).

**3. Entscheidungen / Vereinbarungen**
- Sabine kümmert sich um die neuen Flyer.
- Tom ruft Herrn Brenner bis Mittwoch an und klärt die Teillieferung (60 Stück).
- Fr. Yilmaz liest den Prüfbericht LS-3015 und fasst ihn für die GF bis zum nächsten Jour fixe zusammen.
- Jonas räumt die Lieferantenliste auf, laut Notiz „irgendwann im Q3“. Petra möchte früher; das ist nicht entschieden.
- Sabine fragt bei der Personalabteilung zur Reisekostenrichtlinie nach und informiert das Team.
- Petra prüft die Rechnung RE-2024-0815 mit der Buchhaltung und erstellt ggf. eine Gutschrift.
- Tom erstellt bis Monatsende den Einarbeitungsplan für die Azubis.
- Der Rabatt-Vorschlag wurde nicht entschieden.
- Nächster Termin: in zwei Wochen, Raum 2.14, 9:30 Uhr.

**4. Offene Fragen**
- Datum der Besprechung [UNKLAR]
- Liefertermin SG-40: KW 22 oder KW 23 [UNKLAR]
- Rabatt für Kunde Brenner (Diskussion ohne Ergebnis, GF-Freigabe nötig)
- Details zur Teillieferung von 60 Stück [UNKLAR]
- Ob „frei Haus“ mit Brenner vereinbart war [UNKLAR]
- Lesestatus des Prüfberichts LS-3015 [UNKLAR]
- Termin des Lieferantenauditons (vermutlich Mitte Juni) [UNKLAR]
- Inhalt der Reisekostenrichtlinie v2 [UNKLAR]
- Besetzung des Messe-Standpersonals
- Drucktermin für die Flyer: Freitag oder Donnerstag [UNKLAR]

#### Nutzer 2
Schlage mir eine Tagesordnung für die nächste Besprechung vor, basierend auf den offenen Punkten.

Gib das komplette Gesprächsprotokoll zurück, Format:
### Nutzer 1
<Nachricht>
### Assistent 1
<deine vollständige Antwort>
(usw. für jede Nachricht)

#### Assistent 2 (Nutzer 2 wurde oben bereits ausgeführt)

**Vorschlag Tagesordnung: nächste Besprechung in zwei Wochen, Raum 2.14, 9:30 Uhr**

1. **Begrüßung und Protokoll:** Festlegen, wer künftig protokolliert (bisher „keiner so richtig“).
2. **Messe Hannover / Industrietage:** Stand der Flyer und Druckdaten, Besetzung des Standpersonals.
3. **Kunde Brenner:**
   - Liefertermin SG-40 (KW 22 oder KW 23 klären)
   - Stand der Teillieferung (60 Stück, Rückruf von Tom)
   - Rechnung RE-2024-0815 und Frachtkosten (Ergebnis der Prüfung durch Petra)
   - Rabattfrage mit GF-Entscheidung
4. **Prüfbericht LS-3015:** Zusammenfassung von Fr. Yilmaz für die GF.
5. **Lieferantenliste:** Stand der Bereinigung, Termin des Lieferantenaudits, Priorität (Q3 oder früher).
6. **Reisekostenrichtlinie v2:** Info von Sabine nach Rückfrage bei der Personalabteilung.
7. **Azubi-Projekt:** Stand des Einarbeitungsplans von Tom.
8. **Rückblick:** Erledigte und offene Aufgaben aus der heutigen Besprechung.
9. **Sonstiges**

**Vorab zu klären:** Datum der Besprechung und Termin des Lieferantenaudits, damit die Reihenfolge der Punkte 5 und 3 passt.

---

### Sonnet

#### Nutzer 1
Hier sind meine Stichpunkt-Notizen aus einer Teambesprechung. Sie sind unordentlich.
Mach daraus ein sauberes Protokoll mit diesen Abschnitten:
1. Teilnehmende
2. Besprochene Themen (je 1–3 Sätze)
3. Entscheidungen
4. Offene Fragen

Erfinde nichts dazu. Wenn etwas in den Notizen unklar ist, markiere es mit [UNKLAR].

[Inhalt der Datei notizen_besprechung.txt: Notizen zur Teambesprechung Vertrieb/Technik, Raum 2.14, mit Anwesenden, Themen, Aufgaben und einem Nachtrag von Jonas]

#### Assistent 1
# Protokoll Teambesprechung Vertrieb/Technik

Datum: Dienstag [UNKLAR, in den Notizen steht "Di (?)"]. Ort: Raum 2.14. Protokoll: Jonas, der laut Notizen mitgeschrieben hat. Es war niemand offiziell als Protokollführer bestimmt.

## 1. Teilnehmende
- Sabine K.
- Jonas
- Fr. Yilmaz
- Tom (kam später dazu)
- Petra W. (nur in der ersten Hälfte anwesend)

## 2. Besprochene Themen

**Messe Hannover / Industrietage**
Der Stand ist gebucht, die Prospekte sind aber veraltet. Sabine kümmert sich um neue Flyer. Die Druckerei braucht die Daten spätestens Ende nächster Woche [UNKLAR: Freitag oder Donnerstag wegen eines Feiertags]. Das Standpersonal ist noch offen. Jonas und Fr. Yilmaz würden mitfahren, Sabine fragt noch bei der Technik nach.

**Kunde Brenner, Verzug SG-40**
Der Kunde ist wegen des Lieferverzugs beim SG-40 verärgert (siehe Mail). Die Fertigung nannte zunächst KW 23 für die Gehäuse. Laut Nachtrag von Jonas kommen sie nach Auskunft der Fertigung doch schon in KW 22, und Tom soll das so an den Kunden weitergeben. Tom ruft Hr. Brenner bis Mittwoch an und klärt eine Teillieferung von 60 Stück. Zu einem möglichen Rabatt sagte Petra: maximal 5 %, nur mit Freigabe der Geschäftsführung. Die Diskussion blieb ohne Ergebnis.

**Prüfbericht Laserschneidanlage LS-3015**
Der Bericht (ca. 6 Seiten) liegt vor. Offenbar hat ihn noch niemand gelesen. Fr. Yilmaz liest ihn und fasst ihn für die Geschäftsführung zusammen, bis zum nächsten Jour fixe.

**Lieferantenliste**
Die Liste ist unordentlich (Dubletten, alte Nummern usw.). Jonas räumt sie auf, nach eigener Aussage "irgendwann im Q3". Petra möchte die Bereinigung eher vor dem Lieferantenaudit haben. [UNKLAR: Datum des Audits, in den Notizen steht "Mitte Juni?"]

**Reisekostenrichtlinie v2**
Die neue Version kommt. Niemand weiß genau, was sich geändert hat. Sabine fragt bei der Personalabteilung nach und schickt dem Team eine kurze Info.

**Rechnung RE-2024-0815 an Brenner**
Die Frachtkosten sind möglicherweise falsch berechnet. [UNKLAR: ob "frei Haus" vereinbart war, die Notizen haben hier ein Fragezeichen] Petra prüft das mit der Buchhaltung, gegebenenfalls gibt es eine Gutschrift.

**Azubi-Projekt**
Tom betreut ab nächstem Monat zwei Azubis und braucht dafür einen Einarbeitungsplan. Diesen erstellt er selbst bis Monatsende.

**Sonstiges**
Die Kaffeemaschine im 2. OG ist kaputt. Der Hausmeister ist informiert (erledigt).

## 3. Entscheidungen / vereinbarte Aufgaben
Förmliche Beschlüsse sind in den Notizen nicht festgehalten. Vereinbart wurden folgende Zuständigkeiten:
- Sabine: neue Flyer für die Messe, Rückfrage bei der Technik wegen Standpersonal, Rückfrage bei der Personalabteilung zur Reisekostenrichtlinie und Info ans Team.
- Tom: Anruf bei Hr. Brenner bis Mittwoch, Klärung der Teillieferung von 60 Stück, Weitergabe des Liefertermins KW 22 (laut Nachtrag), Einarbeitungsplan für die Azubis bis Monatsende.
- Fr. Yilmaz: Prüfbericht LS-3015 lesen und für die Geschäftsführung zusammenfassen, bis zum nächsten Jour fixe.
- Jonas: Lieferantenliste aufräumen (Zeitpunkt siehe offene Fragen).
- Petra: Rechnung RE-2024-0815 mit der Buchhaltung prüfen.
- Hausmeister wegen der Kaffeemaschine informiert (erledigt).

Nächster Termin: in 2 Wochen, gleicher Raum, 9:30 Uhr.

## 4. Offene Fragen
- Konkretes Datum der Besprechung und der Abgabefrist für die Flyer-Daten an die Druckerei (Freitag oder Donnerstag?).
- Rabatt für Brenner: ja oder nein? Max. 5 % und nur mit GF-Freigabe, ohne Ergebnis diskutiert.
- Wer fährt zur Messe? Jonas und Fr. Yilmaz würden gehen, die Antwort der Technik steht aus.
- Wann wird die Lieferantenliste bereinigt, im Q3 (Jonas) oder vor dem Lieferantenaudit (Petra)? Wann ist das Audit?
- Was ändert sich in der Reisekostenrichtlinie v2?
- War "frei Haus" mit Brenner vereinbart, sind die Frachtkosten also falsch berechnet?
- Liefertermin der SG-40-Gehäuse: Der Nachtrag nennt KW 22, die Besprechungsnotizen KW 23. Der Nachtrag ist vermutlich aktueller, das sollte bestätigt werden.

#### Nutzer 2
Schlage mir eine Tagesordnung für die nächste Besprechung vor, basierend auf den offenen Punkten.

#### Assistent 2
# Vorschlag Tagesordnung nächste Teambesprechung

Termin: in 2 Wochen, Raum 2.14, 9:30 Uhr. Die Zeiten sind nur grobe Schätzungen und lassen sich anpassen.

1. **Rückmeldungen zu den letzten Aufgaben** (ca. 10 Min.)
   - Tom: Gespräch mit Hr. Brenner und Teillieferung (60 Stück)
   - Petra: Prüfung der Rechnung RE-2024-0815
   - Sabine: Auskunft der Personalabteilung zur Reisekostenrichtlinie v2

2. **Kunde Brenner** (ca. 15 Min.)
   - Liefertermin der SG-40-Gehäuse bestätigen (KW 22 oder KW 23)
   - Frachtkosten: War "frei Haus" vereinbart? Ist eine Gutschrift nötig?
   - Rabatt: Entscheidung, ob er beantragt wird (max. 5 %, nur mit GF-Freigabe). Petra sollte dabei sein, sie war beim letzten Mal nur in der ersten Hälfte da.

3. **Messe Hannover / Industrietage** (ca. 15 Min.)
   - Stand der neuen Flyer und verbindlicher Termin für die Druckerei
   - Standpersonal festlegen (Jonas, Fr. Yilmaz, Antwort der Technik)

4. **Prüfbericht LS-3015** (ca. 10 Min.)
   - Zusammenfassung von Fr. Yilmaz für die Geschäftsführung, Weiteres Vorgehen

5. **Lieferantenliste und Lieferantenaudit** (ca. 10 Min.)
   - Termin des Audits klären
   - Zeitplan für die Bereinigung abstimmen (Q3 oder vor dem Audit)

6. **Reisekostenrichtlinie v2** (ca. 5 Min.)
   - Kurzinfo zu den Änderungen, falls noch nicht per Mail verteilt

7. **Azubi-Projekt** (ca. 5 Min.)
   - Stand des Einarbeitungsplans (Frist: Monatsende)

8. **Sonstiges und nächster Termin** (ca. 5 Min.)

Vorab sinnvoll: Die Protokollführung vorher festlegen, weil sie diesmal niemand offiziell übernommen hatte. Außerdem sollte Petra im Voraus gebeten werden, ganztägig teilzunehmen, weil Rabatt, Rechnung und Audit sie direkt betreffen.

---

### Opus

#### Nutzer 1
Hier sind meine Stichpunkt-Notizen aus einer Teambesprechung. Sie sind unordentlich.
Mach daraus ein sauberes Protokoll mit diesen Abschnitten:
1. Teilnehmende
2. Besprochene Themen (je 1–3 Sätze)
3. Entscheidungen
4. Offene Fragen

Erfinde nichts dazu. Wenn etwas in den Notizen unklar ist, markiere es mit [UNKLAR].

[Anhang: notizen_besprechung.txt]

#### Assistent 1
# Protokoll Teambesprechung Vertrieb/Technik

**Datum:** Dienstag [UNKLAR: In den Notizen steht „Di (?)“, ein Datum fehlt]
**Ort:** Raum 2.14
**Protokoll:** J. (laut Notizen hat „keiner so richtig“ protokolliert, J. hat mitgeschrieben)

---

## 1. Teilnehmende

- Sabine K.
- Jonas
- Fr. Yilmaz
- Tom (kam später dazu)
- Petra W. (nur in der ersten Hälfte anwesend)

---

## 2. Besprochene Themen

**2.1 Messe Hannover / Industrietage**
Der Messestand ist gebucht, die Prospekte sind aber veraltet. Neue Flyer werden gebraucht. Die Druckerei braucht die Daten spätestens Ende nächster Woche [UNKLAR: Freitag oder wegen eines Feiertags schon Donnerstag?].

**2.2 Messe: Standpersonal**
Wer am Stand arbeitet, steht noch nicht fest. Jonas und Fr. Yilmaz würden gehen. Bei der Technik wird noch nachgefragt.

**2.3 Kunde Brenner: Lieferverzug SG-40**
Herr Brenner ist wegen des Lieferverzugs beim SG-40 verärgert (siehe Mail). Zuerst hieß es, die Gehäuse kommen in KW 23. Laut Nachtrag von Jonas meldet die Fertigung jetzt KW 22. Besprochen wurde außerdem eine Teillieferung von 60 Stück und ein möglicher Rabatt.

**2.4 Kunde Brenner: Rechnung RE-2024-0815**
Die Frachtkosten auf der Rechnung sind möglicherweise falsch, weil wahrscheinlich „frei Haus“ vereinbart war [UNKLAR: Die Vereinbarung ist in den Notizen mit „(?)“ markiert]. Eventuell wird eine Gutschrift nötig.

**2.5 Prüfbericht Laserschneidanlage LS-3015**
Der Prüfbericht liegt vor (ca. 6 Seiten). Offenbar hat ihn noch niemand gelesen.

**2.6 Lieferantenliste**
Die Lieferantenliste ist ungeordnet, unter anderem mit Dubletten und alten Nummern. Für das Aufräumen gibt es zwei Zeitvorstellungen: „irgendwann im Q3“ (Jonas) oder vor dem Lieferantenaudit (Wunsch von Petra).

**2.7 Neue Reisekostenrichtlinie v2**
Eine neue Version der Reisekostenrichtlinie kommt. Niemand weiß genau, was sich ändert.

**2.8 Azubi-Projekt**
Tom betreut ab nächstem Monat 2 Azubis und braucht dafür einen Einarbeitungsplan.

**2.9 Sonstiges: Kaffeemaschine 2. OG**
Die Kaffeemaschine im 2. OG ist kaputt. Der Hausmeister ist informiert, der Punkt ist erledigt.

---

## 3. Entscheidungen

### Vereinbarte Aufgaben

| Nr. | Aufgabe | Verantwortlich | Termin |
|---|---|---|---|
| 1 | Neue Flyer für die Messe erstellen, Daten an die Druckerei liefern | Sabine K. | Ende nächster Woche [UNKLAR: Do oder Fr] |
| 2 | Bei der Technik nach Standpersonal für die Messe fragen | Sabine K. | [UNKLAR: kein Termin genannt] |
| 3 | Herrn Brenner anrufen und Teillieferung von 60 Stück klären. Laut Nachtrag den neuen Gehäusetermin KW 22 weitergeben | Tom | bis Mittwoch |
| 4 | Frachtkosten der Rechnung RE-2024-0815 mit der Buchhaltung prüfen, ggf. Gutschrift | Petra W. | [UNKLAR: kein Termin genannt] |
| 5 | Prüfbericht LS-3015 lesen und für die GF zusammenfassen | Fr. Yilmaz | bis zum nächsten Jour fixe |
| 6 | Lieferantenliste aufräumen (Dubletten, alte Nummern) | Jonas | [UNKLAR: „irgendwann im Q3“ oder vor dem Lieferantenaudit?] |
| 7 | Bei Personal nach den Änderungen der Reisekostenrichtlinie v2 fragen und kurze Info ans Team schicken | Sabine K. | [UNKLAR: kein Termin genannt] |
| 8 | Einarbeitungsplan für 2 Azubis erstellen | Tom | bis Monatsende |

### Weitere Festlegungen

- Ein Rabatt für Brenner wäre laut Petra nur bis maximal 5 % und nur mit Freigabe der GF möglich. **Eine Entscheidung zum Rabatt gab es nicht** (Diskussion ohne Ergebnis).
- **Nächster Termin:** in 2 Wochen, gleicher Raum (2.14), 9:30 Uhr

---

## 4. Offene Fragen

1. **Rabatt für Kunde Brenner:** Gibt es einen Rabatt, und wie hoch? Diskutiert, aber ohne Ergebnis. Rahmen laut Petra: max. 5 %, nur mit GF-Freigabe.
2. **Abgabetermin der Druckdaten:** Donnerstag oder Freitag (wegen eines möglichen Feiertags)?
3. **Standpersonal Messe:** Wer kommt aus der Technik dazu? Sind Jonas und Fr. Yilmaz fest eingeplant?
4. **Termin des Lieferantenaudits:** In den Notizen steht „Mitte Juni?“, der Termin ist also nicht bestätigt. Davon hängt ab, bis wann die Lieferantenliste aufgeräumt sein muss.
5. **Zeitplan Lieferantenliste:** „Irgendwann im Q3“ (Jonas) oder vor dem Audit (Petra)? Noch nicht geklärt.
6. **Lieferbedingung Rechnung RE-2024-0815:** War „frei Haus“ wirklich vereinbart?
7. **Reisekostenrichtlinie v2:** Was ändert sich konkret? Sabine klärt das mit Personal.
8. **Gehäusetermin SG-40:** Laut Nachtrag jetzt KW 22 statt KW 23. Ob dieser Termin verbindlich ist, steht nicht in den Notizen.
9. **Datum der Besprechung:** Nur „Di (?)“ ist notiert, ein genaues Datum fehlt.

---

*Hinweis: Petra W. war nur in der ersten Hälfte da, Tom kam später dazu. Bei welchen Themen sie jeweils dabei waren, geht aus den Notizen nicht hervor [UNKLAR].*

#### Nutzer 2
Schlage mir eine Tagesordnung für die nächste Besprechung vor, basierend auf den offenen Punkten.

#### Assistent 2
# Tagesordnung: Teambesprechung Vertrieb/Technik

**Termin:** in 2 Wochen nach der letzten Besprechung, 9:30 Uhr [genaues Datum bitte ergänzen]
**Ort:** Raum 2.14
**Teilnehmende:** Sabine K., Jonas, Fr. Yilmaz, Tom, Petra W.
**Geplante Dauer:** ca. 60 Minuten (Vorschlag)

---

**TOP 1: Begrüßung und Protokoll der letzten Sitzung** (5 Min.)
- Protokoll freigeben, Unklarheiten bereinigen (z. B. Datum der letzten Besprechung)
- Festlegen, wer heute Protokoll führt

**TOP 2: Kunde Brenner** (15 Min.)
- 2.1 Ergebnis von Toms Telefonat mit Herrn Brenner: Teillieferung 60 Stück, Gehäusetermin KW 22 *(Tom)*
- 2.2 Stand der Gehäuselieferung SG-40: Ist KW 22 eingehalten worden bzw. bestätigt? *(Tom / Rückmeldung Fertigung)*
- 2.3 Rabatt: Entscheidung herbeiführen. Rahmen max. 5 %, GF-Freigabe nötig. Liegt die Freigabe vor? *(Petra)*
- 2.4 Rechnung RE-2024-0815: Ergebnis der Prüfung mit der Buchhaltung, war „frei Haus“ vereinbart, Gutschrift ja/nein? *(Petra)*

**TOP 3: Messe Hannover / Industrietage** (10 Min.)
- 3.1 Neue Flyer: Wurden die Daten rechtzeitig an die Druckerei übergeben? *(Sabine)*
- 3.2 Standpersonal festlegen: Rückmeldung der Technik, Jonas und Fr. Yilmaz verbindlich einplanen? *(Sabine)*

**TOP 4: Prüfbericht Laserschneidanlage LS-3015** (10 Min.)
- Zusammenfassung für die GF vorstellen *(Fr. Yilmaz)*
- Gibt es daraus Handlungsbedarf?

**TOP 5: Lieferantenliste und Lieferantenaudit** (10 Min.)
- 5.1 Termin des Lieferantenaudits bestätigen („Mitte Juni?“)
- 5.2 Zeitplan für das Aufräumen der Lieferantenliste verbindlich festlegen: Q3 oder vor dem Audit? *(Jonas, Petra)*

**TOP 6: Reisekostenrichtlinie v2** (5 Min.)
- Was ändert sich? Ist die Info von Personal da und schon ans Team gegangen? *(Sabine)*

**TOP 7: Azubi-Projekt** (5 Min.)
- Stand des Einarbeitungsplans für die 2 Azubis (Termin war Monatsende) *(Tom)*

**TOP 8: Verschiedenes und nächster Termin** (5 Min.)

---

**Tipps zur Vorbereitung:**
- **Petra** sollte bei TOP 2 dabei sein. In der letzten Sitzung war sie nur in der ersten Hälfte da, deshalb steht der Brenner-Block bewusst am Anfang.
- **Rabattentscheidung:** Am besten klärt Petra die GF-Freigabe vorher, damit in TOP 2.3 wirklich entschieden werden kann und nicht nur erneut diskutiert wird.
- Die Tagesordnung vorab ans Team schicken, damit alle Verantwortlichen ihren Stand mitbringen.

Möchtest du die Tagesordnung als E-Mail-Einladung formuliert haben?
