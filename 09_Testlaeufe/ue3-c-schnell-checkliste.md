# Testlauf: Übung 3 / Station C Für Schnelle – Aufgaben als Checkliste

**Herkunft:** Station C, Abschnitt „Für Schnelle“, erster Punkt in [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#für-schnelle-2): „Lass dir die Aufgaben als **Checkliste** zum Abhaken ausgeben.“ Material: [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt). Zum Abgleich: [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md), Station C, „Erwartete Aufgabentabelle“ (8 Aufgaben). Zur Checkliste selbst enthalten die Lösungshinweise **keine** eigenen Hinweise.

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf:** Im selben Gespräch kam zuerst der Basis-Prompt von Station C (Protokoll), danach der Checklisten-Prompt, aus dem Übungsblatt abgeleitet:

```text
Gib mir die Aufgaben als Checkliste zum Abhaken aus.
```

Der Weiter-Prompt (Aufgabentabelle mit „offen“) wurde in diesem Testlauf **nicht** vorgeschaltet. Im Kurs machen die meisten Teilnehmenden ihn vorher, dann baut die Checkliste auf der Tabelle auf. Hier zeigt der Test, was ohne diesen Zwischenschritt herauskommt.

**Was herauskommen soll (Prüfmaßstab):** Abhakbare Liste (☐ oder `- [ ]`) mit allen 8 Aufgaben aus der Tabelle in den Lösungshinweisen, jeweils mit Wer und Bis wann:

1. Sabine K.: neue Flyer, Daten an Druckerei, Ende nächster Woche (Do oder Fr unklar)
2. Tom: Herrn Brenner anrufen, Teillieferung 60 Stk. klären, **KW 22** weitergeben, bis Mittwoch
3. Fr. Yilmaz: Prüfbericht LS-3015 lesen und für GF zusammenfassen, bis zum nächsten Jour fixe
4. Jonas: Lieferantenliste aufräumen, widersprüchlich: „irgendwann im Q3“ oder vor dem Audit (Mitte Juni?)
5. Sabine K.: bei Personal zur Reisekostenrichtlinie v2 nachfragen, Info ans Team, Termin offen
6. Petra W.: Rechnung RE-2024-0815 mit Buchhaltung prüfen, ggf. Gutschrift, Termin offen
7. Tom: Einarbeitungsplan für 2 Azubis, bis Monatsende
8. Sabine K.: Technik nach Standpersonal fragen, Termin offen

Dazu: keine erfundenen Aufgaben, niemandem eine Aufgabe zuschieben, Kaffeemaschine nicht als offene Aufgabe, keine ausgerechneten Daten, Rabatt nicht als Aufgabe einer bestimmten Person.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Checkbox-Format | ja (`- [ ]`, flache Liste mit Namen vorn) | ja (`- [ ]`, nach Person gruppiert) | ja (`- [ ]`, nach Person gruppiert) |
| Alle 8 Aufgaben enthalten | ja (8/8) | ja (8/8) | ja (8/8, Toms Anruf auf 3 Häkchen verteilt) |
| Wer bei jeder Aufgabe richtig | ja bei den 8, aber **zwei Zusatzpunkte mit zugeschobener Zuständigkeit** | ja | ja |
| Bis wann übernommen | ja, wo genannt | ja, wo genannt | ja, wo genannt, Fristen fett |
| „offen“ / Hinweis, wo kein Termin genannt | nein (Termin fehlt einfach) | nein (Termin fehlt einfach) | nein (Termin fehlt einfach; in Turn 1 noch „kein Termin genannt“) |
| KW 22 bei Brenner | **unscharf:** „KW 22 laut Nachtrag, KW 23 laut Fertigung; Widerspruch klären“ | ja („laut Nachtrag: KW 22, nicht KW 23“) | ja (eigener Punkt „KW 22 mitteilen“) |
| Widerspruch bei Jonas markiert | ja | ja ([UNKLAR]) | ja ([UNKLAR], mit „Mitte Juni?“) |
| Rabatt nicht als Entscheidung | ja, aber **Petra W. / GF zugeschoben** | ja („Ohne klare Zuständigkeit“) | ja („Noch ohne Verantwortliche/n“) |
| Standpersonal nicht als feste Zusage | **nein:** „Jonas / Frau Yilmaz: Standpersonal bestätigen“ | ja (ohne Zuständigkeit, „würden gehen“) | ja (nur Sabines Nachfrage als Aufgabe) |
| Kaffeemaschine | als `[x]` erledigt aufgeführt | als `[x]` unter „Erledigt“ | als `[x]` unter „Schon erledigt“ |
| Keine erfundenen Aufgaben / Daten | **nein:** „Alle: Nächster Termin“ als Aufgabe, Standpersonal-Bestätigung | ja | ja |
| Anzahl offener Häkchen | 12 | 10 | 11 |
| Ergebnis | **teilweise** (vollständig, aber aufgebläht und mit zugeschobenen Aufgaben) | **bestanden** | **bestanden** (am klarsten bei KW 22) |

Die Anzahl der Häkchen ist von Hand nachgezählt: Haiku 12 offene + 1 erledigt, Sonnet 10 + 1, Opus 11 + 1. Mehr Häkchen als 8 sind nicht automatisch falsch (Opus teilt Toms Anruf in drei Schritte, Sonnet und Opus listen den Rabatt ohne Person). Bei Haiku kommen die zusätzlichen Häkchen aber durch erfundene oder zugeschobene Punkte zustande.

## Gefundene Fehler mit Beleg

**Kein Modell hat eine der 8 Aufgaben vergessen, kein Modell hat ein konkretes Datum ausgerechnet.** Alle Personen bei den 8 Aufgaben stimmen. Die Fehler betreffen Zusatzpunkte und die Brenner-Korrektur.

**Haiku:**

- **Rabatt einer Person zugeschoben.** Checkliste: „**Petra W. / GF:** Rabattfrage für Brenner … klären“. Notizen: „Rabatt?? Petra: max 5 %, nur mit GF-Freigabe. Diskussion, kein Ergebniss“. Petra hat nur eine Grenze genannt, niemand hat die Klärung übernommen. Genau das fragt der Prüfschritt: „Hat der KI-Assistent jemandem eine Aufgabe zugeschoben, die so nicht in den Notizen steht?“
- **Standpersonal als Aufgabe von Jonas und Fr. Yilmaz.** Checkliste: „**Jonas / Frau Yilmaz:** Standpersonal Messe bestätigen“. Notizen: „Jonas + Fr. Yilmaz würden gehn, Sabine fragt noch Technik“. Eine Bestätigungsaufgabe für die beiden steht nirgends. Das ist die Falle „Standpersonal als feste Zusage“ aus den Lösungshinweisen, hier in abgeschwächter Form.
- **Nächster Termin als Aufgabe.** „**Alle:** Nächster Termin in 2 Wochen, Raum 2.14, 9:30 Uhr“ ist eine Information, keine Aufgabe zum Abhaken.
- **KW 22 als offener Widerspruch.** Checkliste: „KW 22 laut Nachtrag, KW 23 laut Fertigung; Widerspruch klären“. Notizen: „NACHTRAG (Jonas): laut Fertigung kommen die SG-40 Gehäuse **doch schon KW 22**, Tom bitte so an Kunde weitergeben“. Der Nachtrag korrigiert die alte Angabe ausdrücklich und sagt Tom, was er tun soll. Haiku macht daraus einen Widerspruch, den Tom erst klären soll. Schon im Protokoll (Turn 1) schreibt Haiku „KW 22 [UNKLAR: welcher Termin gilt]“. KW 22 ist zwar genannt, die Botschaft an Tom ist aber falsch.
- Kleinigkeit, Turn 1: „Petra … stellt ggf. eine Gutschrift aus“. In den Notizen steht nur „Petra prüft mit Buchhaltung, ggf Gutschrift“, wer die Gutschrift ausstellt, steht dort nicht.

**Sonnet:**

- Keine sachlichen Fehler. Die KW 22 steht in Klammern hinter dem Anruf („laut Nachtrag: Gehäuse kommen KW 22, nicht KW 23“). Dass Tom die KW 22 **weitergeben** soll, steht nicht ausdrücklich da, geht aber aus dem Zusammenhang hervor.
- Turn 1, Deutung: „der Nachtrag steht aber nach dem Besprechungsende“. Er steht nur im Text nach dem nächsten Termin. Ob er nach der Besprechung entstand, sagen die Notizen nicht. Folgenlos, weil Sonnet in der Checkliste trotzdem KW 22 übernimmt.

**Opus:**

- Keine sachlichen Fehler. Toms Aufgabe ist in drei Häkchen zerlegt (anrufen bis Mittwoch, Teillieferung, KW 22 mitteilen). Das ist feiner als die Mustertabelle, aber korrekt.
- Turn 1, übervorsichtig: „Protokoll: J. [UNKLAR – vermutlich Jonas]“. Der Nachtrag ist mit „(Jonas)“ gezeichnet, die Lösungshinweise führen Jonas als Protokollführer. Kein Fehler, aber unnötiges [UNKLAR].

**Alle drei:**

- **Kaffeemaschine steht drin, aber als erledigt (`[x]`).** Laut Lösungshinweisen ist das in Ordnung („Kaffeemaschine nicht als offen“). Wer streng „nur offene Aufgaben“ will, muss das in den Prompt schreiben.
- **Kein „offen“ bei fehlenden Terminen.** Bei Reisekostenrichtlinie, Rechnung und Technik-Nachfrage steht einfach kein Termin. Das ist nicht falsch, weil der Checklisten-Prompt kein „offen“ verlangt. Man übersieht beim Abhaken aber leicht, dass hier eine Frist fehlt.

## Lehren für die Auswertung

1. **Die Checkliste ist im Kern eine Umformatierung, darum klappt sie gut.** Alle drei Modelle finden alle 8 Aufgaben mit den richtigen Personen. Das Protokoll aus Turn 1 hat die Arbeit schon gemacht. Gute Botschaft: Ein geprüftes Zwischenergebnis lässt sich verlässlich in ein anderes Format bringen.
2. **Die Fehler stecken in den Zusatzpunkten.** Haiku „füllt auf“: Rabatt bekommt Petra und die GF, Standpersonal bekommen Jonas und Fr. Yilmaz, der nächste Termin wird zur Aufgabe für alle. Frage an die Runde: „Steht bei jedem Häkchen die Person auch so in den Notizen?“ Das ist genau der zweite Punkt im Prüfschritt und lässt sich hier gut zeigen.
3. **Korrektur oder Widerspruch?** Der Nachtrag zu KW 22 ist eine eindeutige Korrektur mit Auftrag an Tom. Opus und Sonnet übernehmen ihn, Haiku macht daraus „Widerspruch klären“. Gute Diskussion: Wenn der KI-Assistent alles mit [UNKLAR] markiert, ist das auch nicht hilfreich. Unklar ist nur, was wirklich unklar ist (z. B. Do oder Fr, Q3 oder vor dem Audit).
4. **Was fehlt, sieht man nicht.** Ohne den Weiter-Prompt („schreib ‚offen‘“) lassen alle Modelle fehlende Termine einfach weg. Tipp für die Runde: Den Prompt ergänzen um „Wenn Person oder Termin fehlen, schreib ‚offen‘. Nimm Erledigtes nicht auf.“ Oder die Checkliste aus der fertigen Aufgabentabelle erzeugen lassen.
5. **Format hängt vom Ziel ab.** `- [ ]` wird nur in Programmen mit Markdown zu Kästchen. Wer die Liste in Word, Outlook oder Teams einfügt, sieht womöglich „- [ ]“ als Text. Dann im Prompt „mit ☐ als Kästchen“ verlangen. Kurz zeigen, wie die Liste im eigenen [KI-TOOL] aussieht.
6. **Gruppiert nach Person ist praktischer.** Sonnet und Opus sortieren nach Person, jeder sieht seine Punkte auf einen Blick. Haiku liefert eine flache Liste. Wer eine bestimmte Ordnung will (nach Person oder nach Termin), muss sie nennen.
7. **Zeit:** Die Checkliste entsteht in Sekunden. Der Abgleich mit der Tabelle in den Lösungshinweisen dauert 2–3 Minuten. Passt als Zusatzaufgabe.

---

## Gesprächsprotokoll: Haiku

### Nutzer 1

Hier sind meine Stichpunkt-Notizen aus einer Teambesprechung. Sie sind unordentlich.
Mach daraus ein sauberes Protokoll mit diesen Abschnitten:
1. Teilnehmende
2. Besprochene Themen (je 1–3 Sätze)
3. Entscheidungen
4. Offene Fragen

Erfinde nichts dazu. Wenn etwas in den Notizen unklar ist, markiere es mit [UNKLAR].

[INHALT VON /home/daniel/tbc-ai-tutorials/07_Beispielmaterial/notizen_besprechung.txt]

```
Teambesprechung Vertrieb/Technik  -- Di (?), Raum 2.14
anw.: Sabine K., Jonas, Fr. Yilmaz, Tom (später dazu), Petra W. (nur 1. hälfte)
protokoll: keiner so richtig, hab mitgeschrieben -- J.

- Messe Hannover / Industrietage: Stand ist gebucht, aber Prospekte veraltet!!
  -> Sabine kümmert sich um neue Flyer, Druckerei braucht Daten spätestens Ende nächster Woche (Fr? oder Do wg Feiertag??)
- Kunde Brenner sauer wg. SG-40 Verzug (siehe Mail), Fertigung sagt Gehäuse kommen KW 23
  -- Tom ruft Hr. Brenner bis Mittwoch an + klärt Teillieferung 60 Stk
  -- Rabatt?? Petra: max 5 %, nur mit GF-Freigabe. Diskussion, kein Ergebniss
- Prüfbericht Laserschneidanlage LS-3015 liegt vor (ca 6 Seiten.., hat den keiner gelesen?)
  -> Fr. Yilmaz liest + fasst zusammen für GF, bis zum nächsten Jour fixe
- Lieferantenliste ist chaos, Dubletten, alte Nummern usw.
  -> Jonas räumt auf, "irgendwann im Q3", Petra will es aber eigentlich vor dem Lieferantenaudit (wann ist das nochmal? Mitte Juni?)
- neue Reisekostenrichtlinie v2 kommt, was hat sich geändert? keiner weiss es genau
  -> Sabine fragt bei Personal nach + schickt kurze Info ans Team
- Rechnung RE-2024-0815 an Brenner: Frachtkosten evtl falsch, frei Haus war vereinbart(?)
  -> Petra prüft mit Buchhaltung, ggf Gutschrift
- Azubi-Projekt: Tom betreut ab nä. Monat 2 Azubis, braucht Einarbeitungsplan -> Tom selbst, bis Monatsende
- Kurz: Kaffeemaschine 2. OG kaputt, Hausmeister infomiert (erledigt)
- Messe: Standpersonal noch offen, Jonas + Fr. Yilmaz würden gehn, Sabine fragt noch Technik

Nächster Termin: in 2 Wo, gleicher Raum, 9:30
NACHTRAG (Jonas): laut Fertigung kommen die SG-40 Gehäuse doch schon KW 22, Tom bitte so an Kunde weitergeben
```

### Assistent 1

**Protokoll Teambesprechung Vertrieb/Technik**
Datum: [UNKLAR] (Notiz nennt nur "Di (?)"), Raum 2.14

**1. Teilnehmende**
- Sabine K.
- Jonas
- Fr. Yilmaz
- Petra W. (nur 1. Hälfte)
- Tom (ab einem späteren Zeitpunkt)

Protokollführung: Jonas (J.), laut Notiz ohne formelle Protokollierung.

**2. Besprochene Themen**

- **Messe Hannover / Industrietage:** Der Stand ist gebucht, die Prospekte sind aber veraltet. Die Druckerei braucht die Daten spätestens Ende nächster Woche [UNKLAR: Freitag oder Donnerstag, wegen Feiertag]. Das Standpersonal ist noch offen.
- **Kunde Brenner, Verzug SG-40:** Der Kunde ist verärgert. Die Fertigung nennt KW 23 als Liefertermin für die Gehäuse, ein Nachtrag von Jonas nennt KW 22 [UNKLAR: welcher Termin gilt]. Eine Teillieferung von 60 Stück wird geprüft.
- **Rabatt für Brenner:** Petra nennt maximal 5 %, nur mit GF-Freigabe. Es gab keine Einigung.
- **Prüfbericht Laserschneidanlage LS-3015:** Der Bericht (ca. 6 Seiten) liegt vor. Ob ihn jemand gelesen hat, ist unklar.
- **Lieferantenliste:** Die Liste ist unübersichtlich (Dubletten, alte Nummern). Petra möchte die Bereinigung vor dem Lieferantenaudit, dessen Termin [UNKLAR: vermutlich Mitte Juni] ist.
- **Reisekostenrichtlinie v2:** Die neue Richtlinie kommt, welche Änderungen gelten, ist im Team unbekannt.
- **Rechnung RE-2024-0815 an Brenner:** Die Frachtkosten könnten falsch sein. Ob "frei Haus" vereinbart war, ist [UNKLAR].
- **Azubi-Projekt:** Tom betreut ab dem nächsten Monat 2 Azubis und braucht dafür einen Einarbeitungsplan.
- **Kaffeemaschine 2. OG:** defekt, der Hausmeister ist informiert (erledigt).

**3. Entscheidungen**
- Sabine erstellt die neuen Flyer für die Messe.
- Tom ruft Herrn Brenner bis Mittwoch an und klärt die Teillieferung über 60 Stück.
- Frau Yilmaz liest den Prüfbericht LS-3015 und fasst ihn für die GF zusammen, bis zum nächsten Jour fixe.
- Sabine fragt bei der Personalabteilung nach der Reisekostenrichtlinie v2 und informiert das Team.
- Petra prüft die Rechnung RE-2024-0815 mit der Buchhaltung und stellt ggf. eine Gutschrift aus.
- Tom erstellt den Einarbeitungsplan für die Azubis bis Monatsende.
- Jonas räumt die Lieferantenliste auf. Der Zeitpunkt ist mit "irgendwann im Q3" nicht verbindlich.
- Nächster Termin: in 2 Wochen, Raum 2.14, 9:30 Uhr (Datum [UNKLAR]).

Hinweis: Die Notizen enthalten keine ausdrücklichen Beschlüsse. Die Punkte oben sind Zusagen, die in der Besprechung genannt wurden.

**4. Offene Fragen**
- Datum der Besprechung [UNKLAR]
- Abgabetermin der Flyer-Daten: Freitag oder Donnerstag [UNKLAR]
- Liefertermin SG-40: KW 22 oder KW 23 [UNKLAR]
- Rabatt an Brenner: keine Einigung, GF-Freigabe nötig
- Frachtkosten und "frei Haus" bei Rechnung RE-2024-0815 [UNKLAR]
- Termin des Lieferantenaudits [UNKLAR]
- Standpersonal Messe: Jonas und Frau Yilmaz würden gehen, Technik ist noch nicht geklärt
- Inhalt der Reisekostenrichtlinie v2 ist unbekannt
- Wer künftig protokolliert, ist nicht geregelt

### Nutzer 2

Gib mir die Aufgaben als Checkliste zum Abhaken aus.

Gib das komplette Gesprächsprotokoll zurück, Format:
### Nutzer 1
<Nachricht>
### Assistent 1
<deine vollständige Antwort>
(usw. für jede Nachricht)

> Hinweis zum Testlauf: Die letzten Zeilen ab „Gib das komplette Gesprächsprotokoll zurück“ sind eine technische Anweisung der Testumgebung und gehören nicht zur Übung.

### Assistent 2

- [ ] **Sabine K.:** Neue Flyer für die Messe Hannover / Industrietage erstellen, Daten an die Druckerei bis Ende nächster Woche liefern [UNKLAR: Freitag oder Donnerstag]
- [ ] **Tom:** Herrn Brenner bis Mittwoch anrufen, Teillieferung über 60 Stück klären
- [ ] **Tom:** Kunde Brenner den SG-40-Liefertermin mitteilen (KW 22 laut Nachtrag, KW 23 laut Fertigung; Widerspruch klären)
- [ ] **Frau Yilmaz:** Prüfbericht LS-3015 lesen und für die GF zusammenfassen, bis zum nächsten Jour fixe
- [ ] **Jonas:** Lieferantenliste aufräumen (Zeitpunkt "irgendwann im Q3"; Petra möchte vor dem Lieferantenaudit [UNKLAR: Termin])
- [ ] **Sabine K.:** Bei der Personalabteilung nach der Reisekostenrichtlinie v2 fragen und das Team informieren
- [ ] **Petra W.:** Rechnung RE-2024-0815 an Brenner mit der Buchhaltung prüfen (Frachtkosten, "frei Haus"), ggf. Gutschrift
- [ ] **Tom:** Einarbeitungsplan für die 2 Azubis erstellen, bis Monatsende
- [ ] **Sabine K.:** Bei der Technik nachfragen, wer das Standpersonal der Messe übernimmt
- [ ] **Jonas / Frau Yilmaz:** Standpersonal Messe bestätigen (Teilnahme noch offen)
- [ ] **Petra W. / GF:** Rabattfrage für Brenner (max. 5 %, nur mit GF-Freigabe) klären, bisher ohne Ergebnis
- [x] Hausmeister wegen Kaffeemaschine 2. OG informiert (erledigt)
- [ ] **Alle:** Nächster Termin in 2 Wochen, Raum 2.14, 9:30 Uhr

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1

Hier sind meine Stichpunkt-Notizen aus einer Teambesprechung. Sie sind unordentlich.
Mach daraus ein sauberes Protokoll mit diesen Abschnitten:
1. Teilnehmende
2. Besprochene Themen (je 1–3 Sätze)
3. Entscheidungen
4. Offene Fragen

Erfinde nichts dazu. Wenn etwas in den Notizen unklar ist, markiere es mit [UNKLAR].

[Inhalt der Datei notizen_besprechung.txt: Notizen zur Teambesprechung Vertrieb/Technik, Raum 2.14]

### Assistent 1

# Protokoll Teambesprechung Vertrieb/Technik

**Datum:** Dienstag [UNKLAR, in den Notizen mit "(?)" markiert]
**Ort:** Raum 2.14
**Protokoll:** Jonas (kein offizieller Protokollführer, hat mitgeschrieben)

## 1. Teilnehmende
- Sabine K.
- Jonas
- Fr. Yilmaz
- Tom (kam später dazu)
- Petra W. (nur in der ersten Hälfte anwesend)

## 2. Besprochene Themen

**Messe Hannover / Industrietage**
Der Stand ist gebucht, die Prospekte sind aber veraltet. Sabine kümmert sich um neue Flyer. Die Druckerei braucht die Daten spätestens Ende nächster Woche [UNKLAR: Freitag oder Donnerstag wegen Feiertag]. Das Standpersonal ist noch offen: Jonas und Fr. Yilmaz würden mitfahren, Sabine fragt noch bei der Technik nach.

**Kunde Brenner / SG-40-Verzug**
Der Kunde ist wegen des Lieferverzugs beim SG-40 verärgert (siehe Mail). Laut Fertigung kommen die Gehäuse in KW 23. Laut Nachtrag von Jonas kommen sie doch schon in KW 22 [UNKLAR: Die Notizen enthalten zwei Angaben, KW 22 laut Nachtrag ist die jüngere]. Tom ruft Hr. Brenner bis Mittwoch an und klärt eine Teillieferung von 60 Stück. Über einen Rabatt wurde diskutiert: Petra nannte max. 5 %, nur mit Freigabe der Geschäftsführung.

**Prüfbericht Laserschneidanlage LS-3015**
Der Bericht (ca. 6 Seiten) liegt vor, offenbar hat ihn bisher niemand gelesen. Fr. Yilmaz liest ihn und fasst ihn für die Geschäftsführung zusammen, bis zum nächsten Jour fixe.

**Lieferantenliste**
Die Liste ist unordentlich (Dubletten, alte Nummern). Jonas räumt sie auf, laut ihm "irgendwann im Q3". Petra möchte es eigentlich vor dem Lieferantenaudit erledigt haben.

**Reisekostenrichtlinie v2**
Die neue Version kommt, niemand weiß genau, was sich geändert hat. Sabine fragt bei der Personalabteilung nach und schickt dem Team eine kurze Info.

**Rechnung RE-2024-0815 an Brenner**
Die Frachtkosten sind eventuell falsch berechnet, vereinbart war möglicherweise "frei Haus" [UNKLAR: In den Notizen mit "(?)" markiert]. Petra prüft mit der Buchhaltung, gegebenenfalls folgt eine Gutschrift.

**Azubi-Projekt**
Tom betreut ab nächstem Monat 2 Azubis und braucht dafür einen Einarbeitungsplan. Diesen erstellt er selbst bis Monatsende.

**Sonstiges**
Die Kaffeemaschine im 2. OG ist kaputt. Der Hausmeister ist informiert (erledigt).

## 3. Entscheidungen
- Sabine kümmert sich um neue Flyer für die Messe.
- Tom ruft Hr. Brenner bis Mittwoch an und klärt die Teillieferung von 60 Stück.
- Fr. Yilmaz liest den Prüfbericht LS-3015 und fasst ihn für die Geschäftsführung bis zum nächsten Jour fixe zusammen.
- Jonas räumt die Lieferantenliste auf [UNKLAR: Termin, "irgendwann im Q3" vs. Petras Wunsch vor dem Audit].
- Sabine fragt bei Personal wegen der Reisekostenrichtlinie v2 nach und informiert das Team.
- Petra prüft die Rechnung RE-2024-0815 mit der Buchhaltung.
- Tom erstellt bis Monatsende den Einarbeitungsplan für die Azubis.
- Nächster Termin: in 2 Wochen, gleicher Raum, 9:30 Uhr.

Ein Beschluss zum Rabatt wurde ausdrücklich nicht gefasst.

## 4. Offene Fragen
- Rabatt für Brenner: Diskussion ohne Ergebnis. Petra: max. 5 %, nur mit GF-Freigabe.
- Liefertermin SG-40-Gehäuse: KW 22 oder KW 23? Tom soll laut Nachtrag KW 22 weitergeben, der Nachtrag steht aber nach dem Besprechungsende.
- Abgabefrist Flyerdaten: Freitag oder Donnerstag?
- Zeitpunkt der Lieferantenlisten-Bereinigung: Q3 oder vor dem Lieferantenaudit? Wann ist das Audit (Mitte Juni?)?
- Frachtkosten Brenner: War "frei Haus" vereinbart?
- Standpersonal Messe: Rückmeldung der Technik steht aus.
- Änderungen in der Reisekostenrichtlinie v2: unbekannt.
- Datum der Besprechung: Dienstag?

### Nutzer 2

Gib mir die Aufgaben als Checkliste zum Abhaken aus.

### Assistent 2

## Aufgaben-Checkliste

**Sabine**
- [ ] Neue Flyer für die Messe Hannover / Industrietage erstellen, Daten an die Druckerei (Ende nächster Woche, Fr oder Do [UNKLAR])
- [ ] Bei der Technik wegen Standpersonal nachfragen
- [ ] Bei Personal nach den Änderungen der Reisekostenrichtlinie v2 fragen und kurze Info ans Team schicken

**Tom**
- [ ] Hr. Brenner bis Mittwoch anrufen, Teillieferung von 60 Stück klären (laut Nachtrag: Gehäuse kommen KW 22, nicht KW 23)
- [ ] Einarbeitungsplan für 2 Azubis erstellen, bis Monatsende

**Fr. Yilmaz**
- [ ] Prüfbericht Laserschneidanlage LS-3015 (ca. 6 Seiten) lesen und für die Geschäftsführung zusammenfassen, bis zum nächsten Jour fixe

**Jonas**
- [ ] Lieferantenliste aufräumen (Dubletten, alte Nummern), Termin [UNKLAR: "irgendwann im Q3" oder vor dem Lieferantenaudit]

**Petra**
- [ ] Rechnung RE-2024-0815 mit der Buchhaltung prüfen (Frachtkosten, ggf. Gutschrift)

**Ohne klare Zuständigkeit**
- [ ] Rabatt für Brenner klären (max. 5 %, nur mit GF-Freigabe) [UNKLAR: wer]
- [ ] Standpersonal für die Messe festlegen (Jonas und Fr. Yilmaz würden gehen)

**Erledigt**
- [x] Kaffeemaschine 2. OG: Hausmeister informiert

---

## Gesprächsprotokoll: Opus

### Nutzer 1

Hier sind meine Stichpunkt-Notizen aus einer Teambesprechung. Sie sind unordentlich.
Mach daraus ein sauberes Protokoll mit diesen Abschnitten:
1. Teilnehmende
2. Besprochene Themen (je 1–3 Sätze)
3. Entscheidungen
4. Offene Fragen

Erfinde nichts dazu. Wenn etwas in den Notizen unklar ist, markiere es mit [UNKLAR].

[Anhang: notizen_besprechung.txt]

### Assistent 1

# Protokoll – Teambesprechung Vertrieb/Technik

**Datum:** Dienstag [UNKLAR – im Original mit „(?)“ markiert, ein Datum fehlt]
**Ort:** Raum 2.14
**Protokoll:** J. [UNKLAR – vermutlich Jonas, das steht aber nicht ausdrücklich da]

---

## 1. Teilnehmende

- Sabine K.
- Jonas
- Frau Yilmaz
- Tom (kam später dazu)
- Petra W. (nur in der ersten Hälfte dabei)

---

## 2. Besprochene Themen

**a) Messe Hannover / Industrietage**
Der Messestand ist gebucht, die Prospekte sind aber veraltet. Die Druckerei braucht die Daten für neue Flyer spätestens Ende nächster Woche. Ob das Freitag ist oder wegen eines Feiertags schon Donnerstag, ist [UNKLAR].

**b) Kunde Brenner – Lieferverzug SG-40**
Herr Brenner ist wegen des Lieferverzugs beim SG-40 verärgert (siehe Mail). Laut Fertigung kamen die Gehäuse zuerst in KW 23. Ein Nachtrag sagt jetzt KW 22 (siehe Entscheidungen). Eine Teillieferung über 60 Stück soll geklärt werden.

**c) Rabatt für Kunde Brenner**
Ein Rabatt wurde diskutiert. Laut Petra sind höchstens 5 % möglich, und nur mit Freigabe der Geschäftsführung. Es gab kein Ergebnis.

**d) Prüfbericht Laserschneidanlage LS-3015**
Der Prüfbericht liegt vor (ca. 6 Seiten). Offenbar hat ihn noch niemand gelesen [UNKLAR – in den Notizen nur als Frage formuliert].

**e) Lieferantenliste**
Die Lieferantenliste ist unordentlich: Es gibt Dubletten, alte Nummern usw. Strittig ist der Zeitpunkt der Bereinigung: Jonas nannte „irgendwann im Q3“, Petra möchte sie vor dem Lieferantenaudit haben.

**f) Neue Reisekostenrichtlinie v2**
Version 2 der Reisekostenrichtlinie kommt. Was sich geändert hat, wusste niemand genau.

**g) Rechnung RE-2024-0815 an Brenner**
Die Frachtkosten auf der Rechnung sind möglicherweise falsch, weil wohl „frei Haus“ vereinbart war [UNKLAR – im Original mit „(?)“ markiert]. Falls nötig, gibt es eine Gutschrift.

**h) Azubi-Projekt**
Tom betreut ab nächstem Monat zwei Azubis und braucht dafür einen Einarbeitungsplan.

**i) Kaffeemaschine 2. OG**
Die Kaffeemaschine ist kaputt. Der Hausmeister ist informiert, das Thema ist erledigt.

**j) Messe – Standpersonal**
Das Standpersonal steht noch nicht fest. Jonas und Frau Yilmaz würden gehen. Sabine fragt noch bei der Technik nach.

---

## 3. Entscheidungen / Vereinbarungen

| Thema | Vereinbarung | Verantwortlich | Termin |
|---|---|---|---|
| Messe-Flyer | Neue Flyer erstellen, Daten an die Druckerei | Sabine | Ende nächster Woche (Do oder Fr [UNKLAR]) |
| Kunde Brenner | Herrn Brenner anrufen, Teillieferung von 60 Stück klären | Tom | bis Mittwoch |
| Kunde Brenner (Nachtrag) | Dem Kunden mitteilen, dass die SG-40-Gehäuse laut Fertigung schon in **KW 22** kommen (nicht KW 23) | Tom | [UNKLAR – kein eigener Termin, vermutlich beim Anruf] |
| Prüfbericht LS-3015 | Bericht lesen und für die Geschäftsführung zusammenfassen | Frau Yilmaz | bis zum nächsten Jour fixe |
| Lieferantenliste | Liste bereinigen | Jonas | [UNKLAR – „irgendwann im Q3“ oder vor dem Lieferantenaudit] |
| Reisekostenrichtlinie v2 | Bei der Personalabteilung nachfragen, kurze Info ans Team schicken | Sabine | kein Termin genannt |
| Rechnung RE-2024-0815 | Frachtkosten mit der Buchhaltung prüfen, falls nötig Gutschrift | Petra | kein Termin genannt |
| Azubi-Projekt | Einarbeitungsplan erstellen | Tom | bis Monatsende |
| Messe-Standpersonal | Bei der Technik nach Standpersonal fragen | Sabine | kein Termin genannt |

**Nicht entschieden:** der Rabatt für Brenner (siehe offene Fragen).

**Nächster Termin:** in 2 Wochen, gleicher Raum (2.14), 9:30 Uhr

---

## 4. Offene Fragen

1. **Datum der Besprechung:** War sie am Dienstag? Welches Datum genau? [UNKLAR]
2. **Abgabe an die Druckerei:** Freitag oder wegen des Feiertags schon Donnerstag? [UNKLAR]
3. **Rabatt für Brenner:** Gibt es einen Rabatt (höchstens 5 %, nur mit Freigabe der Geschäftsführung)? Es gab kein Ergebnis.
4. **Lieferantenliste – Termin:** Q3 oder vor dem Lieferantenaudit? Wann ist das Audit? (In den Notizen steht „Mitte Juni?“) [UNKLAR]
5. **Reisekostenrichtlinie v2:** Was hat sich geändert? (Sabine klärt das mit der Personalabteilung.)
6. **Rechnung RE-2024-0815:** War wirklich „frei Haus“ vereinbart? [UNKLAR]
7. **Messe-Standpersonal:** Wer aus der Technik kommt dazu? Ist die Besetzung mit Jonas und Frau Yilmaz fest?
8. **Prüfbericht LS-3015:** Hat ihn wirklich noch niemand gelesen? (In den Notizen nur als Frage.)

---

### Nutzer 2

Gib mir die Aufgaben als Checkliste zum Abhaken aus.

### Assistent 2

# Aufgaben-Checkliste – Teambesprechung Vertrieb/Technik

**Sabine**
- [ ] Neue Flyer für die Messe Hannover / Industrietage erstellen und die Daten an die Druckerei schicken – **bis Ende nächster Woche** (Do oder Fr [UNKLAR], wegen Feiertag)
- [ ] Bei der Personalabteilung zur Reisekostenrichtlinie v2 nachfragen und eine kurze Info ans Team schicken
- [ ] Bei der Technik nach Standpersonal für die Messe fragen

**Tom**
- [ ] Herrn Brenner anrufen wegen des SG-40-Lieferverzugs – **bis Mittwoch**
- [ ] Dabei die Teillieferung von 60 Stück klären
- [ ] Dem Kunden mitteilen, dass die SG-40-Gehäuse laut Fertigung schon in **KW 22** kommen (Nachtrag)
- [ ] Einarbeitungsplan für die 2 Azubis erstellen – **bis Monatsende**

**Frau Yilmaz**
- [ ] Prüfbericht Laserschneidanlage LS-3015 lesen und für die Geschäftsführung zusammenfassen – **bis zum nächsten Jour fixe**

**Jonas**
- [ ] Lieferantenliste bereinigen (Dubletten, alte Nummern) – Termin [UNKLAR]: „irgendwann im Q3“ oder auf Petras Wunsch vor dem Lieferantenaudit (Mitte Juni?)

**Petra**
- [ ] Frachtkosten der Rechnung RE-2024-0815 an Brenner mit der Buchhaltung prüfen und falls nötig eine Gutschrift veranlassen

**Noch ohne Verantwortliche/n**
- [ ] Rabatt für Brenner klären (höchstens 5 %, nur mit Freigabe der Geschäftsführung) – es gab kein Ergebnis, niemand ist zuständig [UNKLAR]

**Schon erledigt**
- [x] Kaffeemaschine 2. OG: Hausmeister informiert

**Nächster Termin:** in 2 Wochen, Raum 2.14, 9:30 Uhr
