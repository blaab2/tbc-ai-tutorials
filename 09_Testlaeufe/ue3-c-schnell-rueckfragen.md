# Testlauf: Übung 3 / Station C Für Schnelle – Punkte ohne Verantwortliche + Rückfragen

**Herkunft:** Station C, Abschnitt „Für Schnelle“, zweiter Punkt in [Uebung_3_Dokumente_und_Tabellen.md](../06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md#für-schnelle-2): „Frag: ‚Welche Punkte aus der Besprechung haben noch keinen Verantwortlichen? Formuliere zu jedem eine kurze Rückfrage.‘“ Material: [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt). Die [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md) (Übung 3, Station C) enthalten eine erwartete Aufgabentabelle und die „Fallen in den Notizen“, aber **keinen eigenen Erwartungswert** für diese Zusatzfrage.

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf:** Im selben Gespräch kam zuerst der Basis-Prompt von Station C (Protokoll mit vier Abschnitten), danach die Testfrage:

```text
Welche Punkte aus der Besprechung haben noch keinen Verantwortlichen? Formuliere zu jedem eine kurze Rückfrage.
```

**Was herauskommen soll (Prüfmaßstab dieses Testlaufs):** Eine Liste der Punkte ohne Verantwortliche bzw. ohne Ergebnis, je mit einer kurzen Rückfrage. Aus den Notizen ergeben sich:

- **Rabatt für Brenner** – „Diskussion, kein Ergebniss“, niemand soll die GF-Freigabe holen (Pflicht)
- **Standpersonal Messe** – „Jonas + Fr. Yilmaz würden gehn“, keine feste Zusage; Sabine fragt nur die Technik (Pflicht)
- **Protokollführung** – „keiner so richtig, hab mitgeschrieben -- J.“ (Pflicht)
- **Audit-Termin** („wann ist das nochmal? Mitte Juni?“) und damit die strittige Frist der Lieferantenliste (sinnvoll)
- **Druckerei-Termin** („Fr? oder Do wg Feiertag??“) – Sabine macht die Flyer, wer den Termin klärt, steht nicht da (sinnvoll)
- optional: Ob Petra (nur 1. Hälfte) bei ihren Punkten noch anwesend war (laut Lösungshinweisen „eine gute Rückfrage“)

**Fehler wäre:** Aufgaben mit genannter Person (Flyer/Sabine, Anruf/Tom, Prüfbericht/Fr. Yilmaz, Lieferantenliste/Jonas, Reisekosten/Sabine, Rechnung/Petra, Einarbeitungsplan/Tom) als „ohne Verantwortlichen“ führen, oder die erledigte Kaffeemaschine als offenen Punkt.

---

## Bewertung

Turn 1 (Protokoll) zur Einordnung: Alle drei Modelle listen die Teilnehmenden korrekt, stellen den Rabatt als **offen** dar (nicht als Entscheidung) und führen die Kaffeemaschine als erledigt. Unterschied beim NACHTRAG: Sonnet und Opus übernehmen KW 22 mit Hinweis auf die Korrektur. Haiku nennt KW 22 nur im Nachtrag, markiert ihn als „[UNKLAR] … nicht bestätigt“ und führt KW 22 vs. KW 23 als offene Frage. Keine konkreten Daten aus relativen Terminen errechnet (keine Erfindung).

| Kriterium (Turn 2) | Haiku | Sonnet | Opus |
|---|---|---|---|
| Anzahl genannter Punkte | 5 (+ Hinweis) | 6 (+ Hinweis) | 6 (+ Hinweis) |
| Rabatt Brenner / GF-Freigabe | ja | ja (plus: vor Toms Anruf?) | ja (mit „bis wann“) |
| Standpersonal Messe | ja | ja | ja |
| Protokollführung („keiner so richtig“) | ja | ja | ja |
| Audit-Termin | ja | ja (mit Frist der Lieferantenliste) | ja, Frist der Lieferantenliste als eigener Punkt |
| Druckerei-Termin Do/Fr | **nein** | ja | ja |
| SG-40 KW 22 vs. KW 23 | nein (aber in Turn 1 als offen) | ja, als offen (überzogen, s. u.) | nein (richtig, KW 22 gilt laut Nachtrag) |
| Petra nur 1. Hälfte | nein | nein | nein |
| Aufgaben mit Person fälschlich als „ohne Verantwortlichen“ | nein | nein | nein |
| Konstruierte / schwache Punkte | „Nächster Termin – Teilnehmende offen“ | Lieferzeit SG-40 | keine |
| Rückfragen kurz und adressierbar | ja | ja | ja (wörtlich formuliert) |
| Hinweis, welche Punkte einen Verantwortlichen haben | teilweise (nur Lieferantenliste, Reisekosten) | ja, vollständig | ja, vollständig inkl. Kaffeemaschine |
| Ergebnis | **brauchbar** | **gut** | **sehr gut** |

---

## Gefundene Fehler mit Beleg

Keines der Modelle hat einer Aufgabe mit genannter Person den Verantwortlichen abgesprochen. Der im Prüfmaßstab genannte Hauptfehler kam **nicht** vor. Gefunden wurden kleinere Ungenauigkeiten.

**Haiku**

1. **Erfundener Punkt „Teilnehmende offen“ (Turn 2, Nr. 5):** „Nächster Termin. Wochentag und Teilnehmende sind offen.“ In den Notizen steht nur „Nächster Termin: in 2 Wo, gleicher Raum, 9:30“. Dass die Teilnehmenden offen sind, steht nirgends. Die Rückfrage „Wer lädt ein?“ ist sinnvoll, die Begründung ist aber konstruiert.
2. **Druckerei-Termin fehlt in Turn 2**, obwohl Haiku ihn in Turn 1 selbst als offene Frage führt („Abgabetermin Druckdaten Messe: Freitag oder Donnerstag [UNKLAR]“).
3. **NACHTRAG abgewertet (Turn 1):** „[UNKLAR, KW 22 widerspricht der zuvor genannten KW 23 und ist nicht bestätigt]“. Der Nachtrag sagt aber „laut Fertigung kommen die SG-40 Gehäuse doch schon KW 22“. Das ist eine Korrektur aus derselben Quelle, kein offener Widerspruch. Laut Lösungshinweisen soll ein gutes Protokoll KW 22 übernehmen.
4. **Überinterpretation (Turn 1):** „Der Hausmeister ist informiert und hat den Vorgang erledigt.“ In den Notizen steht „Hausmeister infomiert (erledigt)“. Erledigt ist die Meldung, nicht unbedingt die Reparatur.
5. Kleinigkeit: Tippfehler „AuditTermin“.

**Sonnet**

1. **Lieferzeit SG-40 als „ohne Verantwortlichen“ (Turn 2, Nr. 2):** „Wer bestätigt bei der Fertigung den Termin verbindlich?“ Die Notizen nennen die Fertigung als Quelle für KW 22 und Tom als den, der es weitergibt („Tom bitte so an Kunde weitergeben“). Eine weitere Bestätigung ist nicht offen geblieben, das ist vorsichtig, aber konstruiert. Didaktisch nicht schädlich, aber kein echter offener Punkt.
2. **Kaffeemaschine unter „Entscheidungen“ (Turn 1):** „Die Kaffeemaschine wurde gemeldet, der Hausmeister ist informiert.“ Das ist keine Entscheidung, aber auch keine offene Aufgabe. Kleiner Strukturfehler.

**Opus**

1. **Ungenaue Formulierung (Turn 1, b):** „Laut Fertigung kamen die Gehäuse zuerst in KW 23.“ Gemeint ist „sollten kommen“, die Gehäuse sind noch nicht da. Inhaltlich sonst korrekt.
2. In Turn 2 kein sachlicher Fehler gefunden. Opus unterscheidet sauber zwischen „kein Verantwortlicher“ und „nur unvollständig“ (Frist der Lieferantenliste: Jonas hat die Aufgabe, aber wer die Frist entscheidet, ist offen).

**Alle drei:** Die laut Lösungshinweisen „gute Rückfrage“ zu Petra (nur 1. Hälfte anwesend, waren ihre Aufgaben noch besprochen?) stellt keines der Modelle.

---

## Lehren für die Auswertung

- **Die Übung funktioniert:** Die drei Pflichtpunkte (Rabatt, Standpersonal, Protokollführung) finden alle Modelle. Der befürchtete Fehler (Tom oder Sabine als „ohne Verantwortlichen“ führen) trat in diesem Test nicht auf. Andere Tools können ihn trotzdem machen, deshalb mit der Aufgabentabelle aus den Lösungshinweisen abgleichen lassen.
- **„Kein Verantwortlicher“ wird weit ausgelegt:** Alle Modelle nehmen auch Punkte ohne Termin oder ohne Entscheidung mit (Audit-Termin, Druckerei-Termin, Frist der Lieferantenliste). Das ist meist nützlich. Gute Frage an die Gruppe: „Ist das wirklich ein Punkt ohne Verantwortlichen, oder ein Punkt ohne Termin?“ Opus trennt das ausdrücklich („keinen Verantwortlichen oder nur einen unvollständigen“).
- **Vorsicht vor konstruierten Lücken:** Haiku erfindet „Teilnehmende offen“, Sonnet macht aus der Korrektur KW 22 eine offene Frage. Lehre: Auch bei Rückfragen prüfen, ob die Lücke wirklich in den Notizen steht (Strg+F nach „KW 22“, „Teilnehmende“).
- **Folgefehler aus Turn 1:** Wer in Turn 1 den NACHTRAG als unsicher markiert (Haiku), schleppt das weiter. Ein gutes Beispiel, warum der Prüfschritt nach dem Protokoll Pflicht ist.
- **Rückfragen sind direkt nutzbar:** Die Rückfragen von Opus sind wörtlich formuliert und adressiert („Klärt Sabine mit der Druckerei …?“). Teilnehmende können sie direkt in die Mail aus „Weiter“ übernehmen.
- **Was keiner findet:** Petras Anwesenheit nur in der ersten Hälfte. Trainer kann das als „Bonus für Aufmerksame“ nachreichen: Die KI liest, was dasteht, denkt aber selten über Kontext wie Anwesenheit nach.
- **Zeit:** Eine Frage, eine Antwort, Prüfung in ca. 5 Minuten möglich. Passt als Aufgabe für Schnelle.

---

## Gesprächsprotokoll: Claude Haiku

### Nutzer 1

Hier sind meine Stichpunkt-Notizen aus einer Teambesprechung. Sie sind unordentlich. Mach daraus ein sauberes Protokoll mit diesen Abschnitten: 1. Teilnehmende, 2. Besprochene Themen (je 1–3 Sätze), 3. Entscheidungen, 4. Offene Fragen. Erfinde nichts dazu. Wenn etwas in den Notizen unklar ist, markiere es mit [UNKLAR]. [Anhang: notizen_besprechung.txt]

### Assistent 1

**Protokoll Teambesprechung Vertrieb/Technik**

**Datum und Ort:** Di [UNKLAR, Datum nur mit "(?)" angegeben], Raum 2.14

**1. Teilnehmende**
- Sabine K.
- Jonas
- Fr. Yilmaz
- Tom (kam später dazu)
- Petra W. (nur 1. Hälfte)

Protokoll: Jonas (Kürzel "J.") hat mitgeschrieben. Ein offizielles Protokoll gab es nicht [UNKLAR, ob J. = Jonas].

**2. Besprochene Themen**
- **Messe Hannover / Industrietage:** Der Messestand ist gebucht, die Prospekte sind aber veraltet. Die Druckerei braucht die Daten spätestens Ende nächster Woche [UNKLAR, Freitag oder Donnerstag].
- **Kunde Brenner, Verzug SG-40:** Der Kunde ist verärgert über die Lieferverzögerung. Laut Fertigung sollen die Gehäuse in KW 23 kommen. Eine Teillieferung von 60 Stück wird geprüft. Zum Rabatt sagte Petra, maximal 5 % seien möglich, nur mit GF-Freigabe. Eine Einigung gab es nicht.
- **Prüfbericht Laserschneidanlage LS-3015:** Der Bericht (ca. 6 Seiten) liegt vor. Unklar ist, ob ihn bisher jemand gelesen hat.
- **Lieferantenliste:** Die Liste ist unübersichtlich (Dubletten, alte Nummern). Sie soll bereinigt werden. Petra möchte dies vor dem Lieferantenaudit erledigt haben. Der Termin des Audits ist unklar (vermutlich Mitte Juni [UNKLAR]).
- **Reisekostenrichtlinie v2:** Eine neue Version kommt. Niemand weiß genau, was sich geändert hat.
- **Rechnung RE-2024-0815 an Brenner:** Die Frachtkosten sind möglicherweise falsch berechnet. Vereinbart war laut Notiz wohl "frei Haus" [UNKLAR, ob dies verbindlich vereinbart war].
- **Azubi-Projekt:** Tom betreut ab nächstem Monat zwei Auszubildende und braucht dafür einen Einarbeitungsplan.
- **Messe Standpersonal:** Noch offen. Jonas und Fr. Yilmaz würden teilnehmen, Sabine fragt noch bei der Technik nach.
- **Kaffeemaschine im 2. OG:** Defekt. Der Hausmeister ist informiert und hat den Vorgang erledigt.

**3. Entscheidungen**
- Sabine erstellt neue Flyer für die Messe.
- Tom ruft Herrn Brenner bis Mittwoch an und klärt die Teillieferung von 60 Stück.
- Fr. Yilmaz liest den Prüfbericht LS-3015 und fasst ihn bis zum nächsten Jour fixe für die GF zusammen.
- Jonas bereinigt die Lieferantenliste ("irgendwann im Q3" [UNKLAR, Petra wünscht einen früheren Termin]).
- Sabine fragt bei der Personalabteilung zur Reisekostenrichtlinie nach und informiert das Team.
- Petra prüft die Rechnung RE-2024-0815 mit der Buchhaltung und erstellt bei Bedarf eine Gutschrift.
- Tom erstellt den Einarbeitungsplan für die Azubis bis Monatsende.
- Nachtrag von Jonas: Laut Fertigung kommen die SG-40-Gehäuse bereits in KW 22. Tom soll dies dem Kunden so mitteilen [UNKLAR, KW 22 widerspricht der zuvor genannten KW 23 und ist nicht bestätigt].

**4. Offene Fragen**
- Rabatt für Herrn Brenner: Kein Ergebnis. Ist eine GF-Freigabe nötig und wird ein Rabatt angeboten?
- Liefertermin SG-40: KW 22 (Nachtrag) oder KW 23 (ursprüngliche Angabe) [UNKLAR].
- Abgabetermin Druckdaten Messe: Freitag oder Donnerstag [UNKLAR].
- Termin des Lieferantenaudits [UNKLAR].
- Inhalt der Reisekostenrichtlinie v2: Was hat sich geändert?
- Frachtkosten laut Rechnung RE-2024-0815: Gilt "frei Haus" [UNKLAR]?
- Standpersonal für die Messe: Wer nimmt endgültig teil [UNKLAR]?
- Datum des nächsten Termins: In zwei Wochen, 9:30 Uhr, Raum 2.14. Der Wochentag ist nicht angegeben [UNKLAR].

### Nutzer 2

Welche Punkte aus der Besprechung haben noch keinen Verantwortlichen? Formuliere zu jedem eine kurze Rückfrage.

### Assistent 2

Diese Punkte haben keine klar benannte verantwortliche Person:

1. **Rabatt für Herrn Brenner.** Petra nannte maximal 5 %, nur mit GF-Freigabe. Ein Ergebnis gab es nicht.
   Rückfrage: Wer holt die GF-Freigabe ein, und soll ein Rabatt im Gespräch mit Herrn Brenner überhaupt angeboten werden?

2. **Standpersonal für die Messe.** Jonas und Fr. Yilmaz würden teilnehmen, das ist aber nicht bestätigt. Sabine fragt nur bei der Technik nach.
   Rückfrage: Wer bestätigt das Standpersonal verbindlich, und bis wann?

3. **Termin des Lieferantenaudits.** Petra möchte die Lieferantenliste vorher bereinigt haben. Der Termin ist unklar, und niemand ist dafür benannt, ihn zu klären.
   Rückfrage: Wer klärt den AuditTermin, damit die Bereinigung der Lieferantenliste darauf abgestimmt werden kann?

4. **Protokoll der Besprechung.** Es gab keine verantwortliche Person ("keiner so richtig"). Jonas hat nur Notizen gemacht.
   Rückfrage: Wer schreibt das Protokoll sauber aus und verteilt es an das Team?

5. **Nächster Termin.** Wochentag und Teilnehmende sind offen.
   Rückfrage: Wer lädt zum Termin in zwei Wochen ein?

Hinweis: Die Lieferantenliste (Jonas) und die Reisekostenrichtlinie (Sabine) haben zwar Verantwortliche, der Zeitpunkt ist aber offen. Der Zeitpunkt der Lieferantenliste ist mit "Q3" und dem Wunsch vor dem Audit widersprüchlich.

---

## Gesprächsprotokoll: Claude Sonnet

### Nutzer 1

Hier sind meine Stichpunkt-Notizen aus einer Teambesprechung. Sie sind unordentlich.
Mach daraus ein sauberes Protokoll mit diesen Abschnitten:
1. Teilnehmende
2. Besprochene Themen (je 1–3 Sätze)
3. Entscheidungen
4. Offene Fragen

Erfinde nichts dazu. Wenn etwas in den Notizen unklar ist, markiere es mit [UNKLAR].

[Inhalt der Datei notizen_besprechung.txt wie angehängt]

### Assistent 1

# Protokoll Teambesprechung Vertrieb/Technik

**Datum:** Dienstag [UNKLAR, in den Notizen steht "Di (?)"]
**Ort:** Raum 2.14
**Protokoll:** J. (Jonas), nach eigener Angabe hat sich niemand dafür gemeldet

## 1. Teilnehmende
- Sabine K.
- Jonas
- Fr. Yilmaz
- Tom (kam später dazu)
- Petra W. (nur in der ersten Hälfte anwesend)

## 2. Besprochene Themen

**Messe Hannover / Industrietage**
Der Stand ist gebucht, die Prospekte sind aber veraltet. Sabine kümmert sich um neue Flyer. Die Druckerei braucht die Daten spätestens Ende nächster Woche [UNKLAR: Freitag oder Donnerstag wegen Feiertag]. Das Standpersonal ist noch offen: Jonas und Fr. Yilmaz würden gehen, Sabine fragt noch bei der Technik nach.

**Kunde Brenner, Verzug SG-40**
Der Kunde ist wegen des Lieferverzugs verärgert (siehe Mail). Die Fertigung nannte zunächst KW 23 für die Gehäuse. Laut Nachtrag von Jonas kommen sie doch schon in KW 22, und Tom soll das so an den Kunden weitergeben. Tom ruft Hr. Brenner bis Mittwoch an und klärt eine Teillieferung von 60 Stück. Ein Rabatt wurde diskutiert: Petra nannte max. 5 %, nur mit Freigabe der Geschäftsführung. Ein Ergebnis gab es nicht.

**Prüfbericht Laserschneidanlage LS-3015**
Der Bericht (ca. 6 Seiten) liegt vor, offenbar hat ihn noch niemand gelesen. Fr. Yilmaz liest ihn und fasst ihn für die Geschäftsführung zusammen, bis zum nächsten Jour fixe.

**Lieferantenliste**
Die Liste enthält Dubletten und alte Nummern. Jonas räumt sie auf, nach seiner Aussage "irgendwann im Q3". Petra möchte es eigentlich vor dem Lieferantenaudit erledigt haben. Der Audittermin ist nicht bekannt [UNKLAR: evtl. Mitte Juni].

**Reisekostenrichtlinie v2**
Die neue Version kommt, aber niemand weiß genau, was sich geändert hat. Sabine fragt bei der Personalabteilung nach und schickt dem Team eine kurze Info.

**Rechnung RE-2024-0815 an Brenner**
Die Frachtkosten sind eventuell falsch berechnet, vereinbart war möglicherweise "frei Haus" [UNKLAR: In den Notizen steht dazu ein Fragezeichen]. Petra prüft das mit der Buchhaltung, gegebenenfalls gibt es eine Gutschrift.

**Azubi-Projekt**
Tom betreut ab nächstem Monat zwei Azubis und braucht dafür einen Einarbeitungsplan. Diesen erstellt er selbst bis Monatsende.

**Sonstiges**
Die Kaffeemaschine im 2. OG ist kaputt. Der Hausmeister wurde informiert, damit ist das erledigt.

## 3. Entscheidungen
- Sabine übernimmt die neuen Flyer für die Messe.
- Tom ruft Hr. Brenner bis Mittwoch an und klärt die Teillieferung (60 Stück).
- Fr. Yilmaz fasst den Prüfbericht LS-3015 für die Geschäftsführung zusammen (bis zum nächsten Jour fixe).
- Jonas räumt die Lieferantenliste auf [UNKLAR: Zeitpunkt, siehe Offene Fragen].
- Sabine klärt die Reisekostenrichtlinie v2 mit dem Personalbereich und informiert das Team.
- Petra prüft die Rechnung RE-2024-0815 mit der Buchhaltung.
- Tom erstellt den Einarbeitungsplan für die Azubis bis Monatsende.
- Die Kaffeemaschine wurde gemeldet, der Hausmeister ist informiert.

Nächster Termin: in 2 Wochen, gleicher Raum, 9:30 Uhr.

## 4. Offene Fragen
- Rabatt für Brenner: Es gab keine Einigung. Maximal 5 % und nur mit GF-Freigabe, sonst offen.
- Frist für die Flyer-Daten an die Druckerei: Freitag oder Donnerstag?
- Zeitplan der Lieferantenliste: Jonas plant "irgendwann im Q3", Petra will sie vor dem Lieferantenaudit. Wann findet das Audit statt?
- Standpersonal Messe: Bestätigung von Jonas und Fr. Yilmaz, Rückmeldung der Technik steht aus.
- Inhalt der Reisekostenrichtlinie v2: Was hat sich geändert?
- Rechnung RE-2024-0815: Was wurde mit Brenner zu den Frachtkosten vereinbart?
- Lieferzeit SG-40: KW 22 (laut Nachtrag) oder KW 23 (laut Fertigung)? Bitte bei der Fertigung bestätigen lassen, bevor Tom den Kunden informiert.
- Wochentag und Datum der Besprechung.

### Nutzer 2

Welche Punkte aus der Besprechung haben noch keinen Verantwortlichen? Formuliere zu jedem eine kurze Rückfrage.

### Assistent 2

Aus den Notizen haben diese Punkte noch keinen klaren Verantwortlichen:

1. **Rabatt für Brenner (max. 5 %, GF-Freigabe nötig)**
   Rückfrage: Wer klärt mit der Geschäftsführung, ob und in welcher Höhe ein Rabatt angeboten wird? Soll das vor Toms Anruf bei Hr. Brenner passieren?

2. **Lieferzeit SG-40 (KW 22 oder KW 23)**
   Rückfrage: Wer bestätigt bei der Fertigung den Termin verbindlich? Tom soll ihn zwar weitergeben, die Klärung selbst ist aber niemandem zugeordnet.

3. **Frist für die Flyer-Daten an die Druckerei (Freitag oder Donnerstag)**
   Rückfrage: Wer klärt bei der Druckerei den genauen Abgabetermin? Sabine, die die Flyer macht, vielleicht gleich mit?

4. **Standpersonal Messe**
   Rückfrage: Wer entscheidet am Ende über die Besetzung? Sabine fragt zwar die Technik, aber wer bestätigt Jonas und Fr. Yilmaz?

5. **Termin des Lieferantenaudits**
   Rückfrage: Wer klärt den Termin? Und wer entscheidet, ob Jonas die Liste früher als "irgendwann im Q3" aufräumen muss, wie Petra es möchte?

6. **Protokollführung**
   Rückfrage: Wer führt künftig das Protokoll? Diesmal hat es Jonas übernommen, weil sich sonst niemand gekümmert hat.

Alle übrigen Punkte (Flyer, Anruf bei Brenner, Prüfbericht, Reisekostenrichtlinie, Rechnung RE-2024-0815, Einarbeitungsplan) haben einen Verantwortlichen.

---

## Gesprächsprotokoll: Claude Opus

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

**Datum:** Dienstag [UNKLAR – Wochentag in den Notizen mit „?“ versehen, kein Datum angegeben]
**Ort:** Raum 2.14
**Protokoll:** J. (laut Nachtrag vermutlich Jonas) [UNKLAR – nicht offiziell festgelegt, „keiner so richtig“]

---

## 1. Teilnehmende

- Sabine K.
- Jonas
- Fr. Yilmaz
- Tom (kam später dazu)
- Petra W. (nur in der ersten Hälfte anwesend)

---

## 2. Besprochene Themen

**a) Messe Hannover / Industrietage**
Der Messestand ist gebucht, die Prospekte sind aber veraltet. Die Druckerei braucht die Daten für neue Flyer bis spätestens Ende nächster Woche (Freitag oder wegen eines Feiertags schon Donnerstag [UNKLAR]). Wer am Stand arbeitet, ist noch offen. Jonas und Fr. Yilmaz würden gehen.

**b) Kunde Brenner – Lieferverzug SG-40**
Herr Brenner ist wegen des Lieferverzugs beim SG-40 verärgert (siehe Mail). Laut Fertigung kamen die Gehäuse zuerst in KW 23. Laut Nachtrag von Jonas kommen sie jetzt doch schon in **KW 22**. Ein möglicher Rabatt wurde besprochen. Petra nannte als Rahmen höchstens 5 % und nur mit Freigabe der GF. Ein Ergebnis gab es nicht.

**c) Prüfbericht Laserschneidanlage LS-3015**
Der Prüfbericht liegt vor (ca. 6 Seiten). Offenbar hat ihn noch niemand gelesen [UNKLAR].

**d) Lieferantenliste**
Die Lieferantenliste ist unübersichtlich: Sie enthält Dubletten, alte Nummern usw. Jonas hat „irgendwann im Q3“ als Zeitraum genannt. Petra möchte die Bereinigung aber vor dem Lieferantenaudit haben (Termin vermutlich Mitte Juni [UNKLAR]).

**e) Neue Reisekostenrichtlinie v2**
Eine neue Version der Reisekostenrichtlinie kommt. Was sich ändert, wusste niemand genau.

**f) Rechnung RE-2024-0815 an Brenner**
Die Frachtkosten auf der Rechnung sind möglicherweise falsch, da vermutlich „frei Haus“ vereinbart war [UNKLAR].

**g) Azubi-Projekt**
Tom betreut ab nächstem Monat zwei Azubis und braucht dafür einen Einarbeitungsplan.

**h) Sonstiges: Kaffeemaschine 2. OG**
Die Kaffeemaschine im 2. OG ist kaputt. Der Hausmeister wurde informiert (erledigt).

---

## 3. Entscheidungen / Vereinbarte Aufgaben

| Nr. | Aufgabe | Verantwortlich | Termin |
|---|---|---|---|
| 1 | Neue Flyer für die Messe erstellen, Daten an die Druckerei | Sabine | Ende nächster Woche (Do oder Fr [UNKLAR]) |
| 2 | Bei der Technik nachfragen, wer als Standpersonal zur Messe kann | Sabine | – |
| 3 | Herrn Brenner anrufen, Teillieferung von 60 Stück klären, neuen Gehäusetermin **KW 22** mitteilen (laut Nachtrag) | Tom | bis Mittwoch |
| 4 | Prüfbericht LS-3015 lesen und für die GF zusammenfassen | Fr. Yilmaz | bis zum nächsten Jour fixe |
| 5 | Lieferantenliste bereinigen | Jonas | „irgendwann im Q3“, Petra wünscht vor dem Lieferantenaudit [UNKLAR – Termin nicht abgestimmt] |
| 6 | Bei Personal nach den Änderungen der Reisekostenrichtlinie v2 fragen, kurze Info ans Team | Sabine | – |
| 7 | Frachtkosten der Rechnung RE-2024-0815 mit der Buchhaltung prüfen, ggf. Gutschrift | Petra | – |
| 8 | Einarbeitungsplan für die Azubis erstellen | Tom | bis Monatsende |
| 9 | Kaffeemaschine: Hausmeister informiert | – | erledigt |

**Hinweis:** Zum Rabatt für Brenner wurde **keine Entscheidung** getroffen.

---

## 4. Offene Fragen

- Rabatt für Brenner: Gibt es einen, und wenn ja, wie hoch (max. 5 %)? Wer holt die GF-Freigabe ein?
- Abgabetermin für die Druckdaten: Donnerstag oder Freitag (Feiertag)? [UNKLAR]
- Standpersonal für die Messe ist noch nicht festgelegt (Rückmeldung der Technik steht aus).
- Wann genau ist das Lieferantenaudit (Mitte Juni?) [UNKLAR], und bis wann muss die Lieferantenliste bereinigt sein?
- War für Brenner tatsächlich „frei Haus“ vereinbart? [UNKLAR]
- Was ändert sich in der Reisekostenrichtlinie v2?
- Datum der Besprechung [UNKLAR]

---

**Nächster Termin:** in 2 Wochen, gleicher Raum (2.14), 9:30 Uhr

### Nutzer 2

Welche Punkte aus der Besprechung haben noch keinen Verantwortlichen? Formuliere zu jedem eine kurze Rückfrage.

### Assistent 2

Laut den Notizen haben diese Punkte keinen Verantwortlichen oder nur einen unvollständigen:

**1. Rabatt für Kunde Brenner**
Diskutiert, aber ohne Ergebnis. Niemand wurde benannt, der eine Entscheidung herbeiführt oder die GF-Freigabe einholt.
> *Rückfrage:* „Wer klärt bis wann, ob Brenner einen Rabatt bekommt (max. 5 %), und holt dafür die Freigabe der GF ein?“

**2. Standpersonal für die Messe (endgültige Festlegung)**
Sabine fragt nur bei der Technik nach. Wer am Ende entscheidet und die Standbesetzung festlegt, steht nicht in den Notizen.
> *Rückfrage:* „Wer legt das Standpersonal für die Messe verbindlich fest, und bis wann?“

**3. Termin des Lieferantenaudits klären**
Der Audittermin ist unklar („Mitte Juni?“). Niemand soll ihn klären. Davon hängt aber ab, bis wann die Lieferantenliste fertig sein muss.
> *Rückfrage:* „Wer findet heraus, wann genau das Lieferantenaudit stattfindet?“

**4. Frist für die Lieferantenliste**
Jonas hat die Aufgabe, aber die Frist ist umstritten (Q3 oder vor dem Audit). Wer das entscheidet, ist offen.
> *Rückfrage:* „Wer entscheidet, ob die Lieferantenliste bis zum Audit oder erst im Q3 fertig sein muss?“

**5. Abgabetermin der Druckdaten (Donnerstag oder Freitag)**
Sabine kümmert sich um die Flyer. Niemand wurde aber ausdrücklich beauftragt, den genauen Termin mit der Druckerei zu klären.
> *Rückfrage:* „Klärt Sabine mit der Druckerei, ob die Daten am Donnerstag oder am Freitag dort sein müssen?“

**6. Protokollführung**
Laut den Notizen hat „keiner so richtig“ das Protokoll übernommen. J. hat nur mitgeschrieben.
> *Rückfrage:* „Wer verschickt dieses Protokoll ans Team, und wer schreibt beim nächsten Termin Protokoll?“

**Hinweis:** Alle anderen Punkte (Flyer, Anruf bei Brenner, Prüfbericht, Reisekostenrichtlinie, Rechnungsprüfung, Einarbeitungsplan) haben laut Notizen einen Verantwortlichen. Die Kaffeemaschine ist erledigt.
