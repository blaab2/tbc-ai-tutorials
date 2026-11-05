# Testlauf: Übung 3 / Station C Basis – Notizen zu sauberem Protokoll

**Herkunft:** Station C, Stufe „Basis“ aus [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#station-c-chaotische-notizen--protokoll-und-aufgabenliste) (Block 5). Material: [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt). Zugehörige Lösungshinweise: [Trainer-Loesungshinweise.md – Station C](../06_Uebungen/Trainer-Loesungshinweise.md#station-c-notizen--protokoll-und-aufgabentabelle) („Erwartete Aufgabentabelle“, „Weitere Inhalte“).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt (jeweils in einem neuen Chat, Notizen angehängt bzw. eingefügt):**

```text
Hier sind meine Stichpunkt-Notizen aus einer Teambesprechung. Sie sind unordentlich.
Mach daraus ein sauberes Protokoll mit diesen Abschnitten:
1. Teilnehmende
2. Besprochene Themen (je 1–3 Sätze)
3. Entscheidungen
4. Offene Fragen

Erfinde nichts dazu. Wenn etwas in den Notizen unklar ist, markiere es mit [UNKLAR].
```

**Was laut Material herauskommen soll:** Ein Protokoll in 4 Abschnitten. Teilnehmende: Sabine K., Jonas (Protokoll), Fr. Yilmaz, Tom (später dazu), Petra W. (nur 1. Hälfte). Das Datum der Besprechung ist unklar („Di (?)“) und wird mit [UNKLAR] markiert, es wird kein Datum erfunden. Der Liefertermin SG-40 ist **KW 22** laut Nachtrag, die Korrektur von KW 23 soll erkennbar sein. Der Rabatt (Petra: max. 5 %, nur mit GF-Freigabe, Diskussion ohne Ergebnis) steht unter **offenen Fragen**, nicht unter Entscheidungen. Beim Standpersonal gibt es nur „würden gehen“, keine feste Zusage. Die Kaffeemaschine ist erledigt. Weitere offene Fragen: Druckerei Do oder Fr, Audit-Termin („Mitte Juni?“), Frachtkosten/frei Haus. Nächster Termin: in 2 Wochen, Raum 2.14, 9:30 Uhr.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| 4 Abschnitte wie verlangt | ja | ja | ja |
| Teilnehmende vollständig inkl. Zusätze (später dazu, nur 1. Hälfte) | ja (5 von 5) | ja (5 von 5) | ja (5 von 5) |
| Jonas als Protokollant | ja („hat mitgeschrieben“) | ja (inkl. „niemand offiziell bestimmt“) | ja (inkl. „kein offizieller Protokollführer“) |
| Datum [UNKLAR], kein erfundenes Datum | ja, nur „[UNKLAR] (Notizen nennen ‚Di (?)‘)“ | ja, „Dienstag [UNKLAR …]“ | ja, „Dienstag [UNKLAR …, kein Datum angegeben]“ |
| Nachtrag KW 22 übernommen, Korrektur erkennbar | **teilweise**: nennt beide Werte, behandelt sie aber als Widerspruch („[UNKLAR]: welches Datum gilt“) und führt den Termin als offene Frage | ja, aber verteilt: Thema Brenner nennt noch KW 23, Nachtrag als eigenes Thema, in Entscheidungen KW 22 | **ja**, sauber: „Zuerst … KW 23. Laut Nachtrag … KW 22“, plus Hinweis am Ende |
| Rabatt als offene Frage, nicht als Entscheidung | ja (Formulierung missverständlich, s. u.) | ja, zusätzlich „ausdrücklich nicht getroffen“ | ja, als Punkt 1 der offenen Fragen |
| Standpersonal ohne feste Zusage | ja („Zusage steht aber noch aus“) | ja („würden gehen“) | ja („steht noch nicht fest“) |
| Kaffeemaschine als erledigt, nicht als Aufgabe | ja, aber leicht umgedeutet (s. u.) | ja | ja |
| Offene Frage Druckerei Do/Fr | ja | ja | ja |
| Offene Frage Audit-Termin | ja | ja | ja (inkl. Zielkonflikt Jonas/Petra) |
| Offene Frage Frachtkosten / frei Haus | ja | ja | ja |
| Nächster Termin (2 Wochen, Raum 2.14, 9:30) | ja (Raum im Kopf, Termin unter offenen Fragen) | ja (unter offenen Fragen) | ja (unter Abschnitt 3, nicht als offene Frage) |
| Alle 8 Aufgaben aus der Tabelle der Lösungshinweise enthalten | ja (8 von 8) | ja (8 von 8, Standpersonal nur bei Themen/offenen Fragen) | ja (8 von 8, als Tabelle mit Frist) |
| Themen „je 1–3 Sätze“ eingehalten | fast: 1 Thema mit 4 Sätzen (Brenner) | nein: Messe und Brenner je 5 Sätze | nein: Messe 4, Brenner 6 Sätze |
| Erfundenes? | nein, nur kleine Umdeutungen | nein | nein |

**Kurz:** Alle drei Protokolle sind brauchbar, und keins erfindet ein Datum oder macht aus dem Rabatt einen Beschluss. **Opus** liefert die Fassung, die den Lösungshinweisen am nächsten kommt: KW 22 korrekt übernommen, Aufgaben als Tabelle mit Wer und Bis wann, saubere offene Fragen. **Sonnet** hat alles drin, verteilt den Nachtrag aber auf zwei Stellen. Wer nur das Thema „Brenner“ liest, sieht noch KW 23. **Haiku** erkennt den Nachtrag nicht als Korrektur, sondern als Widerspruch, und lässt die Frage offen. Das ist der Hauptunterschied zwischen den Modellen. Alle drei überschreiten bei den zwei langen Themen die Vorgabe „1–3 Sätze“.

---

## Gefundene Fehler mit Beleg

1. **Haiku – Nachtrag nicht als Korrektur erkannt.** In den Notizen steht ganz am Ende: „NACHTRAG (Jonas): laut Fertigung kommen die SG-40 Gehäuse doch schon KW 22, Tom bitte so an Kunde weitergeben“. Das „doch schon“ und der Auftrag an Tom machen klar, dass KW 22 gilt. Haiku schreibt dagegen: „laut Nachtrag von Jonas bereits KW 22 ([UNKLAR]: welches Datum gilt)“ und unter offenen Fragen: „Liefertermin SG-40-Gehäuse: KW 23 oder KW 22 ([UNKLAR], widersprüchliche Angaben)“. Gleichzeitig steht bei Tom „laut Nachtrag die Liefertermin-Information an den Kunden weitergeben“. Das widerspricht sich selbst. Haiku setzt [UNKLAR] hier zu vorsichtig, im Zweifel lieber unklar als falsch. Für die Praxis heißt das: Das Protokoll ist an der wichtigsten Stelle für den Kunden unentschieden.

2. **Haiku – Rabatt missverständlich formuliert.** Notizen: „Rabatt?? Petra: max 5 %, nur mit GF-Freigabe. Diskussion, kein Ergebniss“. Haiku unter offenen Fragen: „Freigabe durch die GF über 5 % steht aus.“ Das kann man so lesen, als gehe es um einen Rabatt **über** 5 %. Gemeint ist ein Rabatt **bis** 5 %, und auch der braucht die GF-Freigabe. Bei Themen ist es richtig („maximal 5 %, nur mit GF-Freigabe“).

3. **Haiku – Kaffeemaschine leicht umgedeutet.** Notizen: „Kaffeemaschine 2. OG kaputt, Hausmeister infomiert (erledigt)“. Haiku: „Der Hausmeister ist informiert und hat den Fall erledigt.“ Erledigt ist laut Notizen der Punkt (Hausmeister informieren), nicht unbedingt die Reparatur. Wer das Protokoll liest, könnte meinen, die Maschine sei repariert. Sonnet („informiert (erledigt)“) und Opus („Der Hausmeister wurde informiert, der Punkt ist erledigt“) bleiben näher an der Quelle.

4. **Sonnet – Nachtrag auseinandergezogen.** Unter dem Thema „Kunde Brenner“ steht nur „Laut Fertigung kommen die Gehäuse in KW 23.“ KW 22 kommt erst im eigenen Thema „Nachtrag (Jonas)“ und unter Entscheidungen/offenen Fragen. Inhaltlich richtig, aber wer nur den Abschnitt zu Brenner liest, bekommt den alten Termin. Positiv: Sonnet fragt als einziges Modell, ob die Teillieferung von 60 Stück durch KW 22 noch nötig ist, und markiert das korrekt als [UNKLAR].

5. **Sonnet – Frage als Aussage geglättet.** Notizen: „hat den keiner gelesen?“ (mit Fragezeichen). Sonnet: „offenbar hat ihn noch niemand gelesen“, ohne [UNKLAR]. Opus macht das gleich („Offenbar hat ihn noch niemand gelesen.“). Nur Haiku markiert den Punkt als [UNKLAR]. Kleinigkeit, aber ein gutes Beispiel dafür, wie aus einer Frage in den Notizen eine Feststellung im Protokoll wird.

6. **Opus – „frei Haus“ fast als Tatsache.** Notizen: „Frachtkosten evtl falsch, frei Haus war vereinbart(?)“. Opus: „möglicherweise falsch, weil ‚frei Haus‘ vereinbart war [UNKLAR: …]“. Der Satz klingt wie eine Tatsache, die Unsicherheit steht nur in der Klammer. Unter offenen Fragen fragt Opus aber richtig: „War ‚frei Haus‘ wirklich vereinbart?“

7. **Alle drei – Vorgabe „je 1–3 Sätze“ überschritten.** Nachgezählt: Haiku hat beim Thema Brenner 4 Sätze. Sonnet hat bei Messe und Brenner je 5 Sätze. Opus hat bei Messe 4 und bei Brenner 6 Sätze. Die übrigen Themen halten die Vorgabe ein. Die Modelle opfern die Längenvorgabe, um nichts wegzulassen.

8. **Alle drei – „Entscheidungen“ sind eigentlich Aufgaben.** In den Notizen gibt es keine echten Beschlüsse, nur Zuständigkeiten („Sabine kümmert sich“, „Tom ruft … an“). Alle drei Modelle füllen Abschnitt 3 trotzdem mit diesen Aufgaben. Nur Haiku sagt es offen: „In den Notizen sind keine ausdrücklichen Beschlüsse vermerkt. Vereinbart wurden folgende Aufgaben und Zuständigkeiten.“ Das ist kein Fehler, aber eine gute Diskussionsfrage (s. u.).

Nicht gefunden: kein erfundenes Datum (Besprechung, nächster Termin, Jour fixe, Audit), keine erfundene Person, keine erfundene Frist, keine Prozentzahl außer den 5 % aus den Notizen. Der Wert von 10 % aus der Kundenmail taucht nirgends auf (die Mail war nicht angehängt).

---

## Lehren für die Auswertung

- **Der Nachtrag ist der beste Prüfpunkt.** Fragt die Gruppe: „Welcher Liefertermin steht in eurem Protokoll?“ Im Test gab es drei Varianten: korrekt KW 22 (Opus), KW 22, aber über das Protokoll verteilt (Sonnet), und „unklar, KW 22 oder 23?“ (Haiku). Lehre: Nachträge am Ende von Notizen werden nicht immer als Korrektur verstanden. Wer Notizen schreibt, schreibt besser „KORREKTUR: KW 22 statt KW 23“.
- **[UNKLAR] wirkt, aber in beide Richtungen.** Die Anweisung „Erfinde nichts, markiere [UNKLAR]“ hat in allen drei Fällen erfundene Daten verhindert. Haiku zeigt die Kehrseite: Zu viel [UNKLAR] macht ein Protokoll unentschieden. Diskussion: Was ist hier wirklich unklar, und was ist nur unordentlich notiert?
- **Aus Fragen werden Aussagen.** „hat den keiner gelesen?“ wird bei Sonnet und Opus zu „offenbar hat ihn noch niemand gelesen“. „frei Haus war vereinbart(?)“ wird bei Opus fast zur Tatsache. Gut für den Prüfschritt: Notizzeilen mit Fragezeichen im Protokoll suchen.
- **Entscheidung oder Aufgabe?** Keins der Modelle findet echte Beschlüsse, weil keine drinstehen. Frage an die Gruppe: „Ist ‚Sabine kümmert sich um Flyer‘ eine Entscheidung?“ Das leitet direkt zur Stufe „Weiter“ (Aufgabentabelle) über.
- **Längenvorgaben sind weich.** „Je 1–3 Sätze“ halten die Modelle nicht ein, wenn ein Thema viele Fakten hat. Das ist harmlos, zeigt aber: Formatvorgaben immer nachprüfen.
- **Kaffeemaschine:** Kein Modell macht daraus eine Aufgabe. Der in den Lösungshinweisen genannte Stolperstein tritt in der Basis-Stufe also nicht auf. Er wird eher in der Aufgabentabelle (Stufe „Weiter“) relevant.
- **Modellunterschied:** Das größere Modell löst den Nachtrag am saubersten und liefert von sich aus eine Aufgabentabelle mit Wer/Bis wann. Das kleinere Modell ist vorsichtiger, aber weniger nützlich. Alle drei sind für ein Protokoll brauchbar, wenn man den Prüfschritt macht.

---

## Hinweise zum Material

- **Übungsblatt:** Anleitung und Prompt sind verständlich, die Basis-Stufe dauert mit Prüfen etwa 5–8 Minuten und passt in die Arbeitszeit. Der Prüfschritt im Übungsblatt bezieht sich auf die **Aufgabentabelle** (Stufe „Weiter“). Für die Basis fehlt ein Hinweis, auf den Nachtrag und den Rabatt zu achten.
- **Lösungshinweise:** Für Station C gibt es eine erwartete **Aufgabentabelle** und „Weitere Inhalte“, aber keine ausdrücklichen Prüfpunkte für das Protokoll der Basis-Stufe. Die Angaben dort (KW 22, Rabatt offen, Standpersonal nicht fest, Kaffeemaschine erledigt, nächster Termin, Teilnehmende) stimmen mit den Notizen überein und passen zu dem, was die Modelle liefern. Nicht erwähnt ist, dass ein Modell den Nachtrag als Widerspruch statt als Korrektur werten kann und dass der Abschnitt „Entscheidungen“ fast nur Aufgaben enthält.
- **Testartefakt:** Im Haiku-Protokoll enthält „Nutzer 1“ zusätzlich eine Formatanweisung des Testsystems („Gib das komplette Gesprächsprotokoll zurück …“). Sie gehört nicht zum Übungsprompt und hat das Ergebnis nicht erkennbar beeinflusst.

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

Gib das komplette Gesprächsprotokoll zurück, Format:
### Nutzer 1
<Nachricht>
### Assistent 1
<deine vollständige Antwort>
(usw. für jede Nachricht)

#### Assistent 1

**Protokoll: Teambesprechung Vertrieb/Technik**
Datum: [UNKLAR] (Notizen nennen „Di (?)“), Raum 2.14

**1. Teilnehmende**
- Sabine K.
- Jonas (hat mitgeschrieben)
- Fr. Yilmaz
- Petra W. (nur 1. Hälfte)
- Tom (kam später dazu)

**2. Besprochene Themen**

- **Messe Hannover / Industrietage:** Der Messestand ist gebucht, die Prospekte sind aber veraltet. Sabine kümmert sich um neue Flyer; die Druckerei braucht die Daten spätestens Ende nächster Woche ([UNKLAR]: Freitag oder Donnerstag wegen Feiertag). Das Standpersonal ist noch offen: Jonas und Fr. Yilmaz würden teilnehmen, Sabine fragt noch bei Technik nach.
- **Kunde Brenner, Verzug SG-40:** Herr Brenner ist verärgert über die Verzögerung. Die Fertigung nennt KW 23 für die Gehäuse, laut Nachtrag von Jonas bereits KW 22 ([UNKLAR]: welches Datum gilt). Ein Rabatt wurde diskutiert: Petra nennt maximal 5 %, nur mit GF-Freigabe. Es gab kein Ergebnis.
- **Prüfbericht Laserschneidanlage LS-3015:** Der Bericht (ca. 6 Seiten) liegt vor. Es ist [UNKLAR], ob ihn schon jemand gelesen hat. Fr. Yilmaz liest ihn und fasst ihn für die GF zusammen.
- **Lieferantenliste:** Die Liste ist unübersichtlich (Dubletten, alte Nummern). Jonas räumt sie auf, der Zeitpunkt ist „irgendwann im Q3“. Petra möchte es vor dem Lieferantenaudit, dessen Termin [UNKLAR] ist („Mitte Juni?“).
- **Reisekostenrichtlinie v2:** Die neue Version kommt, aber niemand weiß genau, was sich geändert hat. Sabine fragt bei der Personalabteilung nach und informiert das Team.
- **Rechnung RE-2024-0815 an Brenner:** Die Frachtkosten sind möglicherweise falsch. Die Notizen fragen „frei Haus war vereinbart(?)“, das ist [UNKLAR]. Petra prüft das mit der Buchhaltung, ggf. folgt eine Gutschrift.
- **Azubi-Projekt:** Tom betreut ab dem nächsten Monat 2 Azubis und braucht dafür einen Einarbeitungsplan.
- **Kurz:** Die Kaffeemaschine im 2. OG ist kaputt. Der Hausmeister ist informiert und hat den Fall erledigt.

**3. Entscheidungen**

In den Notizen sind keine ausdrücklichen Beschlüsse vermerkt. Vereinbart wurden folgende Aufgaben und Zuständigkeiten:
- **Sabine:** neue Flyer für die Messe; Anfrage bei der Personalabteilung zur Reisekostenrichtlinie und Info ans Team; Klärung des Standpersonals mit Technik.
- **Tom:** Anruf bei Herrn Brenner bis Mittwoch, Klärung der Teillieferung über 60 Stück; Einarbeitungsplan für die Azubis bis Monatsende; laut Nachtrag die Liefertermin-Information an den Kunden weitergeben.
- **Fr. Yilmaz:** Prüfbericht LS-3015 lesen und für die GF zusammenfassen, bis zum nächsten Jour fixe.
- **Jonas:** Lieferantenliste aufräumen (Zeitpunkt: Q3).
- **Petra:** Rechnung RE-2024-0815 mit der Buchhaltung prüfen, ggf. Gutschrift.

**4. Offene Fragen**
- Datum der Besprechung ([UNKLAR]: „Di (?)“).
- Abgabetermin der Druckdaten für die Flyer: Freitag oder Donnerstag ([UNKLAR]).
- Liefertermin SG-40-Gehäuse: KW 23 oder KW 22 ([UNKLAR], widersprüchliche Angaben).
- Rabatt für Kunde Brenner: kein Ergebnis; Freigabe durch die GF über 5 % steht aus.
- Frachtkosten Rechnung RE-2024-0815: Gilt „frei Haus“ ([UNKLAR])?
- Termin des Lieferantenaudits ([UNKLAR]: „Mitte Juni?“).
- Inhalte der Reisekostenrichtlinie v2 sind unbekannt.
- Standpersonal Messe: Jonas und Fr. Yilmaz sind vorgesehen, die Zusage steht aber noch aus.
- Ob der Prüfbericht LS-3015 bereits gelesen wurde ([UNKLAR]).
- Datum des nächsten Termins: „in 2 Wochen, gleicher Raum, 9:30“ ([UNKLAR]: genaues Datum fehlt).

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

[Anhang: notizen_besprechung.txt]

#### Assistent 1

**Protokoll Teambesprechung Vertrieb/Technik**

**Datum:** Dienstag [UNKLAR, in den Notizen mit "(?)" markiert]
**Ort:** Raum 2.14
**Protokoll:** Jonas (Mitschrift, niemand war offiziell als Protokollführung bestimmt)

**1. Teilnehmende**
- Sabine K.
- Jonas
- Fr. Yilmaz
- Tom (kam später dazu)
- Petra W. (nur in der ersten Hälfte anwesend)

**2. Besprochene Themen**

**Messe Hannover / Industrietage**
Der Stand ist gebucht, die Prospekte sind aber veraltet. Sabine kümmert sich um neue Flyer. Die Druckerei braucht die Daten spätestens Ende nächster Woche [UNKLAR: Freitag oder Donnerstag wegen des Feiertags]. Das Standpersonal ist noch offen. Jonas und Fr. Yilmaz würden mitfahren, Sabine fragt noch bei der Technik nach.

**Kunde Brenner, Lieferverzug SG-40**
Der Kunde ist wegen des Verzugs verärgert (siehe Mail). Laut Fertigung kommen die Gehäuse in KW 23. Tom ruft Hr. Brenner bis Mittwoch an und klärt eine Teillieferung von 60 Stück. Zum Rabatt sagte Petra, möglich seien maximal 5 %, nur mit Freigabe der Geschäftsführung. Die Diskussion dazu blieb ohne Ergebnis.

**Prüfbericht Laserschneidanlage LS-3015**
Der Bericht (ca. 6 Seiten) liegt vor, offenbar hat ihn noch niemand gelesen. Fr. Yilmaz liest ihn und fasst ihn für die Geschäftsführung zusammen, bis zum nächsten Jour fixe.

**Lieferantenliste**
Die Liste ist unübersichtlich (Dubletten, alte Nummern usw.). Jonas räumt sie auf, laut Notiz "irgendwann im Q3". Petra möchte es aber eigentlich vor dem Lieferantenaudit erledigt haben [UNKLAR: Termin des Audits, vermutlich Mitte Juni, in den Notizen mit Fragezeichen].

**Reisekostenrichtlinie v2**
Eine neue Version kommt. Niemand weiß genau, was sich geändert hat. Sabine fragt bei der Personalabteilung nach und schickt dem Team eine kurze Info.

**Rechnung RE-2024-0815 an Brenner**
Die Frachtkosten sind möglicherweise falsch berechnet, vereinbart war evtl. "frei Haus" [UNKLAR: In den Notizen mit Fragezeichen]. Petra prüft das mit der Buchhaltung, gegebenenfalls folgt eine Gutschrift.

**Azubi-Projekt**
Tom betreut ab nächstem Monat 2 Azubis und braucht dafür einen Einarbeitungsplan. Diesen erstellt er selbst bis Monatsende.

**Kaffeemaschine 2. OG**
Sie ist defekt. Der Hausmeister wurde informiert (erledigt).

**Nachtrag (Jonas)**
Laut Fertigung kommen die SG-40-Gehäuse doch schon in KW 22. Tom soll dies so an den Kunden weitergeben.

**3. Entscheidungen**
- Sabine erstellt neue Flyer für die Messe.
- Tom ruft Hr. Brenner bis Mittwoch an und klärt die Teillieferung von 60 Stück.
- Fr. Yilmaz liest den Prüfbericht LS-3015 und fasst ihn für die Geschäftsführung zusammen (bis zum nächsten Jour fixe).
- Sabine fragt bei der Personalabteilung zur Reisekostenrichtlinie v2 nach und informiert das Team.
- Petra prüft die Rechnung RE-2024-0815 mit der Buchhaltung.
- Tom erstellt den Einarbeitungsplan für die Azubis bis Monatsende.
- Jonas räumt die Lieferantenliste auf [UNKLAR: Zeitpunkt, siehe offene Fragen].
- Tom gibt gegenüber dem Kunden den aktualisierten Liefertermin KW 22 weiter (laut Nachtrag).

Eine Entscheidung zum Rabatt wurde ausdrücklich nicht getroffen.

**4. Offene Fragen**
- **Wochentag der Besprechung:** Dienstag (?) laut Notizen unsicher.
- **Abgabefrist Flyer-Daten:** Freitag oder Donnerstag (Feiertag)?
- **Rabatt für Brenner:** Kein Ergebnis. Rahmen laut Petra max. 5 % und nur mit GF-Freigabe.
- **Liefertermin SG-40:** Ursprünglich KW 23, laut Nachtrag KW 22. Der Nachtrag ersetzt offenbar die frühere Angabe [UNKLAR: ob die Teillieferung von 60 Stück damit weiter nötig ist].
- **Lieferantenliste:** Aufräumen "irgendwann im Q3" (Jonas) oder vor dem Lieferantenaudit (Petra)? Wann ist das Audit (Mitte Juni?)?
- **Reisekostenrichtlinie v2:** Was hat sich geändert?
- **Rechnung RE-2024-0815:** War "frei Haus" vereinbart? Ist eine Gutschrift nötig?
- **Standpersonal Messe:** Wer fährt? Jonas und Fr. Yilmaz würden gehen, Technik wird noch gefragt.
- **Datum der Messe:** In den Notizen nicht genannt.
- **Nächster Termin:** In 2 Wochen, gleicher Raum, 9:30 Uhr. Das genaue Datum steht nicht in den Notizen.

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

**Protokoll Teambesprechung Vertrieb/Technik**

**Datum:** Dienstag [UNKLAR: Wochentag in den Notizen mit „?“ versehen, kein Datum angegeben]
**Ort:** Raum 2.14
**Protokoll:** Jonas (hat mitgeschrieben, kein offizieller Protokollführer)

**1. Teilnehmende**

- Sabine K.
- Jonas
- Fr. Yilmaz
- Tom (kam später dazu)
- Petra W. (nur in der ersten Hälfte anwesend)

**2. Besprochene Themen**

**2.1 Messe Hannover / Industrietage**
Der Messestand ist gebucht, die Prospekte sind aber veraltet. Die Druckerei braucht die Daten für neue Flyer spätestens Ende nächster Woche [UNKLAR: Freitag oder wegen eines Feiertags schon Donnerstag]. Das Standpersonal steht noch nicht fest. Jonas und Fr. Yilmaz würden mitfahren.

**2.2 Kunde Brenner – Lieferverzug SG-40**
Herr Brenner ist wegen des Lieferverzugs beim SG-40 verärgert (siehe Mail). Zuerst hieß es, die Fertigung erwarte die Gehäuse in KW 23. Laut Nachtrag von Jonas kommen sie doch schon in KW 22. Besprochen wurden eine Teillieferung von 60 Stück und ein möglicher Rabatt. Petra nannte dafür maximal 5 %, nur mit Freigabe der GF. Die Diskussion endete ohne Ergebnis.

**2.3 Prüfbericht Laserschneidanlage LS-3015**
Der Prüfbericht (ca. 6 Seiten) liegt vor. Offenbar hat ihn noch niemand gelesen.

**2.4 Lieferantenliste**
Die Lieferantenliste ist unübersichtlich, unter anderem mit Dubletten und veralteten Nummern. Jonas will sie „irgendwann im Q3“ aufräumen. Petra möchte das aber vor dem Lieferantenaudit erledigt haben.

**2.5 Reisekostenrichtlinie v2**
Eine neue Version der Reisekostenrichtlinie kommt. Was sich ändert, weiß im Team niemand genau.

**2.6 Rechnung RE-2024-0815 an Brenner**
Die Frachtkosten auf der Rechnung sind möglicherweise falsch, weil „frei Haus“ vereinbart war [UNKLAR: Vereinbarung in den Notizen mit „?“ versehen]. Falls nötig, gibt es eine Gutschrift.

**2.7 Azubi-Projekt**
Tom betreut ab nächstem Monat zwei Auszubildende und braucht dafür einen Einarbeitungsplan.

**2.8 Sonstiges: Kaffeemaschine 2. OG**
Die Kaffeemaschine im 2. OG ist defekt. Der Hausmeister wurde informiert, der Punkt ist erledigt.

**3. Entscheidungen**

| Nr. | Was | Wer | Bis wann |
|---|---|---|---|
| 1 | Neue Flyer für die Messe erstellen und Daten an die Druckerei liefern | Sabine K. | Ende nächster Woche [UNKLAR: Do oder Fr] |
| 2 | Bei der Technik nach Standpersonal für die Messe fragen | Sabine K. | – [UNKLAR: keine Frist genannt] |
| 3 | Herrn Brenner anrufen, die Teillieferung von 60 Stück klären und den neuen Gehäusetermin **KW 22** weitergeben | Tom | Mittwoch |
| 4 | Prüfbericht LS-3015 lesen und für die GF zusammenfassen | Fr. Yilmaz | nächster Jour fixe |
| 5 | Lieferantenliste bereinigen | Jonas | „irgendwann im Q3“ [UNKLAR: Petra wünscht Erledigung vor dem Lieferantenaudit] |
| 6 | Bei der Personalabteilung nach den Änderungen der Reisekostenrichtlinie v2 fragen und eine kurze Info ans Team schicken | Sabine K. | – [UNKLAR: keine Frist genannt] |
| 7 | Frachtkosten der Rechnung RE-2024-0815 mit der Buchhaltung prüfen, ggf. Gutschrift | Petra W. | – [UNKLAR: keine Frist genannt] |
| 8 | Einarbeitungsplan für die zwei Azubis erstellen | Tom | Monatsende |

**Nächster Termin:** in 2 Wochen, gleicher Raum (2.14), 9:30 Uhr

**4. Offene Fragen**

1. **Rabatt für Kunde Brenner:** Es wurde nicht entschieden, ob es einen Rabatt gibt. Bekannt ist nur der Rahmen: maximal 5 %, nur mit GF-Freigabe.
2. **Abgabetermin Druckdaten:** Muss alles schon Donnerstag fertig sein (wegen des Feiertags) oder erst Freitag?
3. **Termin Lieferantenaudit:** Der Termin ist unklar (vermutet „Mitte Juni?“). Davon hängt ab, ob das Aufräumen der Lieferantenliste im Q3 noch rechtzeitig ist. Diesen Zielkonflikt zwischen Jonas und Petra muss noch jemand klären.
4. **Änderungen der Reisekostenrichtlinie v2:** Was sich ändert, ist noch unbekannt. Sabine fragt bei der Personalabteilung nach.
5. **Frachtkosten RE-2024-0815:** War „frei Haus“ wirklich vereinbart?
6. **Standpersonal Messe:** Die Besetzung steht noch nicht fest. Sabine fragt noch bei der Technik nach.
7. **Besprechungsdatum:** War die Besprechung wirklich an einem Dienstag, und an welchem Datum?

*Hinweis:* In den ursprünglichen Notizen stand für die SG-40-Gehäuse KW 23. Laut Nachtrag von Jonas gilt jetzt **KW 22**, deshalb wurde KW 22 übernommen.

---

Zurück zum Übungsblatt: [Uebung_3_Dokumente_und_Tabellen.md – Station C](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#station-c-chaotische-notizen--protokoll-und-aufgabenliste) · Material: [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt)
