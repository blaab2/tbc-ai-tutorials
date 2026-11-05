# Testlauf: Demo-Alternative Block 4 – Schwacher Prompt: Protokoll

**Herkunft:** Demo-Prompts aus dem Input (Block 4, Folie 14), Abschnitt „Alternative – Protokoll aus den Besprechungsnotizen“ in [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md). Der gleiche schwache Prompt steht auch im [Trainer-Leitfaden](../01_Trainer-Leitfaden.md) (Block 4). Material: [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt). Erwartete Aufgabenliste zum Abgleich: Übung 3, Station C in den Lösungshinweisen.

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt (neuer Chat):**
```
Schreib ein Protokoll.

[Inhalt von notizen_besprechung.txt]
```

**Wichtig zum Testaufbau:** Auf Folie 14 und im Trainer-Leitfaden steht der schwache Prompt **ohne** Notizen. Für diesen Test wurden die Notizen trotzdem angehängt, damit der Vergleich mit dem starken Prompt fair ist. Ohne Notizen hätte der KI-Assistent nichts, woraus er ein Protokoll machen kann. Er würde dann eine leere Vorlage liefern, ein Protokoll erfinden oder nach den Notizen fragen.

**Ziel laut Material:** Kontrast zum starken Prompt. Mit dem schwachen Prompt sollen die drei Fallen eher übersehen werden: Nachtrag KW 22, Rabatt offen, Kaffeemaschine erledigt.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Nachtrag berücksichtigt (KW 22 statt KW 23) | ja (KW 23 nur als „zunächst“) | ja, auch in der Aufgabentabelle | ja, auch in der Aufgabentabelle, plus eigener Hinweis |
| Rabatt als offen dargestellt (kein Beschluss) | ja („keine Einigung“) | ja („kein Ergebnis“, unter „Offene Punkte“) | ja („keine Entscheidung“, Aufgabe mit [offen]) |
| Kaffeemaschine nicht als Aufgabe | ja (nur „Sonstiges … erledigt“) | ja (nicht in der Tabelle) | ja (nicht in der Tabelle) |
| Erfundene Termine/Daten | keine | keine | keine |
| Alle 8 Aufgaben aus Station C enthalten | ja (im Fließtext, keine Tabelle) | ja (Tabelle) | ja (Tabelle, plus Rabatt als 9. Zeile) |
| Unsicheres markiert (Do/Fr, Audit Mitte Juni?, frei Haus?) | ja, im Text | ja, eckige Klammern + Liste offener Punkte | ja, [offen]-Marker überall |
| Widerspruch Q3 vs. Audit sauber dargestellt | ja | ja („Widerspruch“, „[klären]“) | teilweise – in der Tabelle zu „vor dem Audit, spätestens Q3“ aufgelöst |
| Kleine Überinterpretationen | wenige | wenige | einige |
| Länge / Format | kurz, nur Gliederung nach Punkten | lang, Gliederung + Tabelle + offene Punkte + Hinweis | am längsten, Kopf-Tabelle + Gliederung + Tabelle + Hinweise + Rückfrage |
| **Gezeigter Fehler tritt auf (Fallen übersehen)** | **nein** | **nein** | **nein** |

---

## Gefundene Fehler mit Beleg

Keines der drei Modelle tappt in eine der drei geplanten Fallen. Es gibt keine erfundenen Termine, Prozentsätze oder Personen. Gefunden wurden nur kleine Überinterpretationen:

**Haiku**
1. *„Petra prüft das mit der Buchhaltung und stellt ggf. eine Gutschrift aus.“* In den Notizen steht nur „Petra prüft mit Buchhaltung, ggf Gutschrift“. Wer die Gutschrift ausstellt, steht dort nicht.
2. *„Sabine erstellt neue Flyer.“* In den Notizen steht „Sabine kümmert sich um neue Flyer“. Das ist eine leichte Zuspitzung, inhaltlich vertretbar.
3. Beim Nachtrag fehlt der Name: *„Diese Information soll an den Kunden weitergegeben werden.“* In den Notizen steht ausdrücklich „Tom bitte so an Kunde weitergeben“.

**Sonnet**
1. *„Offenbar hat ihn bisher niemand gelesen.“* In den Notizen steht das als Frage: „hat den keiner gelesen?“. Opus macht das genauso.
2. *„Protokoll: Jonas“*: In den Notizen steht nur „J.“. Wegen „NACHTRAG (Jonas)“ ist das plausibel, aber trotzdem eine Schlussfolgerung. Opus macht das genauso, Haiku schreibt korrekt „J.“.
3. Sonnet nennt fast jeden Punkt **„Beschluss“**, auch reine Zuständigkeiten wie „Sabine kümmert sich um neue Flyer“. Das ist nicht falsch, aber der Begriff wird verwässert.
4. Hinweis zum Testaufbau, kein Modellfehler: In Sonnets Gesprächsprotokoll ist die Format-Anweisung des Testskripts mit in der Nutzernachricht gelandet. Das Ergebnis hat das nicht sichtbar beeinflusst.

**Opus**
1. *„Jonas und Fr. Yilmaz haben zugesagt.“* In den Notizen steht „Jonas + Fr. Yilmaz würden gehn“. Das ist eine Bereitschaft, keine Zusage. Opus macht daraus eine stärkere Aussage.
2. *„Für den Stand ist noch nicht genug Personal eingeplant.“* In den Notizen steht nur „Standpersonal noch offen“. Dass es „nicht genug“ ist, steht dort nicht.
3. Aufgabe 7 in der Tabelle: *„vor dem Lieferantenaudit [offen: Termin], spätestens Q3“*. Damit wird der Widerspruch aufgelöst. In den Notizen steht nur: Jonas sagt „irgendwann im Q3“, Petra will es „eigentlich vor dem Audit“. Eine Einigung steht dort nicht. Wenn das Audit Mitte Juni ist, ist „spätestens Q3“ außerdem die falsche Grenze. Im Fließtext stellt Opus den Punkt dagegen richtig dar.
4. *„Sabine lässt neue Flyer machen“* und *„Herr Brenner hat sich … beschwert (siehe seine E-Mail)“*: Das sind leichte Umdeutungen („kümmert sich“, „sauer … siehe Mail“). Inhaltlich unproblematisch.

**Tritt der Demo-Fehler auf?** **Nein.** Auch mit dem schwachen Prompt übernehmen alle drei Modelle den Nachtrag (KW 22), stellen den Rabatt als offen dar und führen die Kaffeemaschine nicht als Aufgabe. Sonnet und Opus liefern von sich aus sogar eine Aufgabentabelle und eine Liste offener Punkte. Das ist fast genau das, was der starke Prompt verlangt. Die Erwartung in den Lösungshinweisen („Fallen werden eher übersehen“) bestätigt sich in diesem Test nicht.

---

## Lehren für die Auswertung

1. **Wenn die Notizen dabei sind, reicht dem Modell oft schon der schwache Prompt.** Die Fallen sind für aktuelle Modelle zu offensichtlich: Der NACHTRAG ist groß geschrieben, „kein Ergebniss“ und „(erledigt)“ stehen wörtlich da. Wer den Kontrast an den Fallen zeigen will, wird wahrscheinlich enttäuscht.
2. **Der echte Unterschied ist die Vorhersagbarkeit, nicht die Richtigkeit.** Drei Modelle liefern drei verschiedene Formate: Haiku ohne Tabelle, Sonnet mit Tabelle und Liste offener Punkte, Opus mit Kopf-Tabelle, Hinweisen und Rückfrage. Dazu kommen sehr unterschiedliche Längen. Mit dem starken Prompt bestimmt man das Format selbst und bekommt jedes Mal dieselbe Struktur. Das ist eine gute und ehrliche Lehre: „Ohne Vorgabe entscheidet die KI, wie das Ergebnis aussieht.“
3. **Der wirksamere schwache Prompt ist der ohne Notizen**, so wie er auf Folie 14 steht. Dann zeigt sich die eigentliche Schwäche, fehlender Kontext, sofort: Das Modell liefert eine Vorlage mit Platzhaltern, erfindet eine Besprechung oder fragt nach. Das ist für die Gruppe viel deutlicher als ein Vergleich zweier fast gleich guter Protokolle.
4. **Kleine Überinterpretationen gibt es trotzdem.** Beispiele: „würden gehn“ wird zu „zugesagt“ (Opus), „hat den keiner gelesen?“ wird zu „niemand hat ihn gelesen“ (Sonnet, Opus), und in einer Tabelle wird ein Widerspruch aufgelöst (Opus). Damit lässt sich gut zeigen, wozu „Erfinde nichts dazu“ im starken Prompt gut ist und warum man trotzdem gegenlesen muss.
5. **Ein großes Modell ist nicht automatisch genauer.** Gerade das ausführlichste Modell (Opus) deutet am meisten um, weil es mehr formuliert. Haiku bleibt am nächsten an den Notizen.

---

## Gesprächsprotokolle

### Haiku

#### Nutzer 1
Schreib ein Protokoll.

[Anhang: notizen_besprechung.txt]

#### Assistent 1

**Protokoll: Teambesprechung Vertrieb/Technik**

- **Ort:** Raum 2.14
- **Termin:** Dienstag (Datum in den Notizen mit "(?)" markiert)
- **Anwesend:** Sabine K., Jonas, Fr. Yilmaz, Tom (später dazu), Petra W. (nur 1. Hälfte)
- **Protokollführung:** J. (Mitschrift, kein formelles Protokoll)

**1. Messe Hannover / Industrietage**
- Der Stand ist gebucht, die Prospekte sind aber veraltet.
- Maßnahme: Sabine erstellt neue Flyer. Die Druckerei braucht die Daten spätestens Ende nächster Woche. Ob das Freitag oder Donnerstag ist, ist wegen eines Feiertags unklar.
- Standpersonal: Jonas und Fr. Yilmaz würden teilnehmen. Sabine klärt noch, ob die Technik weitere Personen stellt.

**2. Kunde Brenner: Verzug bei SG-40**
- Der Kunde ist verärgert (siehe Mail). Die Fertigung hatte die Gehäuse zunächst für KW 23 angekündigt.
- Nachtrag von Jonas: Laut Fertigung kommen die Gehäuse bereits in KW 22. Diese Information soll an den Kunden weitergegeben werden.
- Maßnahme: Tom ruft Hr. Brenner bis Mittwoch an und klärt eine Teillieferung von 60 Stück.
- Rabatt: Petra nennt maximal 5 %, nur mit Freigabe der Geschäftsführung. Es gab keine Einigung.

**3. Prüfbericht Laserschneidanlage LS-3015**
- Der Bericht (ca. 6 Seiten) liegt vor. Unklar, ob ihn schon jemand gelesen hat.
- Maßnahme: Fr. Yilmaz liest den Bericht und fasst ihn für die GF zusammen, bis zum nächsten Jour fixe.

**4. Lieferantenliste**
- Die Liste ist unübersichtlich (Dubletten, alte Nummern).
- Maßnahme: Jonas räumt auf, "irgendwann im Q3". Petra möchte das früher erledigt haben, vor dem Lieferantenaudit. Der Termin des Audits ist unklar, vermutlich Mitte Juni.

**5. Neue Reisekostenrichtlinie (v2)**
- Es ist nicht klar, was sich geändert hat.
- Maßnahme: Sabine fragt bei der Personalabteilung nach und informiert das Team.

**6. Rechnung RE-2024-0815 an Brenner**
- Die Frachtkosten könnten falsch sein. Vereinbart war möglicherweise "frei Haus".
- Maßnahme: Petra prüft das mit der Buchhaltung und stellt ggf. eine Gutschrift aus.

**7. Azubi-Projekt**
- Tom betreut ab nächstem Monat 2 Azubis.
- Maßnahme: Tom erstellt selbst bis Monatsende einen Einarbeitungsplan.

**8. Sonstiges**
- Die Kaffeemaschine im 2. OG ist kaputt. Der Hausmeister ist informiert, erledigt.

**Nächster Termin:** in 2 Wochen, gleicher Raum (2.14), 9:30 Uhr.

---

### Sonnet

#### Nutzer 1
Schreib ein Protokoll.

[Anhang: notizen_besprechung.txt]
Teambesprechung Vertrieb/Technik  -- Di (?), Raum 2.14
anw.: Sabine K., Jonas, Fr. Yilmaz, Tom (später dazu), Petra W. (nur 1. hälfte)
protokoll: keiner so richtig, hab mitgeschrieben -- J.

- Messe Hannover / Industrietage: Stand ist gebucht, aber Prospekte veraltet!!
  -> Sabine kümmert sich um neue Flyer, Druckerei braucht Daten spätestens Ende nächster Woche (Fr? oder Do wg Feiertag??)
- Kunde Brenner sauer wg. SG-40 Verzug (siehe Mail), Fertigung sagt Gehäuse kommen KW 23
  -- Tom ruft Hr. Brenner bis Mittwoch an + klärt Teilieferung 60 Stk
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

Gib das komplette Gesprächsprotokoll zurück, Format:
### Nutzer 1
<Nachricht>
### Assistent 1
<deine vollständige Antwort>
(usw. für jede Nachricht)

*(Anmerkung Testlauf: Die letzten fünf Zeilen sind die Format-Anweisung des Testskripts und gehören nicht zum Demo-Prompt.)*

#### Assistent 1
# Protokoll Teambesprechung Vertrieb/Technik

**Datum:** [Dienstag, genaues Datum in den Notizen nicht angegeben]
**Ort:** Raum 2.14
**Uhrzeit:** [nicht angegeben]
**Protokoll:** Jonas

**Teilnehmende:** Sabine K., Jonas, Fr. Yilmaz, Tom (kam später dazu), Petra W. (nur in der ersten Hälfte anwesend)

## Besprochene Punkte und Ergebnisse

### 1. Messe Hannover / Industrietage
- Der Stand ist gebucht. Die Prospekte sind veraltet.
- **Beschluss:** Sabine kümmert sich um neue Flyer.
- Die Druckerei braucht die Daten spätestens Ende nächster Woche. [Offen: Freitag oder Donnerstag wegen Feiertag. Bitte klären.]
- **Standpersonal:** noch offen. Jonas und Fr. Yilmaz würden teilnehmen. Sabine fragt noch bei der Technik nach.

### 2. Kunde Brenner: Lieferverzug SG-40
- Der Kunde ist verärgert über den Verzug (siehe Mail).
- Die Fertigung nannte zunächst KW 23 für die Gehäuse. **Nachtrag (Jonas):** Laut Fertigung kommen die Gehäuse doch schon in **KW 22**. Tom gibt das so an den Kunden weiter.
- **Beschluss:** Tom ruft Hr. Brenner bis Mittwoch an und klärt eine Teillieferung von 60 Stück.
- **Rabatt:** Petra nannte maximal 5 %, nur mit Freigabe der Geschäftsführung. Es gab eine Diskussion, aber **kein Ergebnis**.

### 3. Rechnung RE-2024-0815 an Brenner
- Die Frachtkosten sind möglicherweise falsch berechnet. Vereinbart war eventuell "frei Haus" [laut Notizen nicht sicher].
- **Beschluss:** Petra prüft das mit der Buchhaltung. Falls nötig, folgt eine Gutschrift.

### 4. Prüfbericht Laserschneidanlage LS-3015
- Der Bericht liegt vor (ca. 6 Seiten). Offenbar hat ihn bisher niemand gelesen.
- **Beschluss:** Fr. Yilmaz liest ihn und fasst ihn für die Geschäftsführung zusammen, bis zum nächsten Jour fixe.

### 5. Lieferantenliste
- Die Liste ist unübersichtlich (Dubletten, alte Nummern usw.).
- **Beschluss:** Jonas räumt sie auf, zeitlich "irgendwann im Q3".
- **Widerspruch:** Petra möchte die Bereinigung vor dem Lieferantenaudit (Termin unklar, evtl. Mitte Juni). Der Zeitplan muss abgestimmt werden.

### 6. Reisekostenrichtlinie v2
- Eine neue Version kommt. Niemand weiß genau, was sich geändert hat.
- **Beschluss:** Sabine fragt bei der Personalabteilung nach und schickt dem Team eine kurze Info.

### 7. Azubi-Projekt
- Tom betreut ab nächstem Monat zwei Azubis.
- **Beschluss:** Tom erstellt selbst einen Einarbeitungsplan, bis Monatsende.

### 8. Sonstiges
- Die Kaffeemaschine im 2. OG ist defekt. Der Hausmeister wurde informiert (erledigt).

## Maßnahmenübersicht

| Wer | Aufgabe | Frist |
|---|---|---|
| Sabine | Neue Flyer für die Messe erstellen und an die Druckerei liefern | Ende nächster Woche [Fr oder Do, klären] |
| Sabine | Technik wegen Standpersonal fragen | offen |
| Sabine | Bei Personal zur Reisekostenrichtlinie v2 nachfragen und Info ans Team schicken | offen |
| Tom | Hr. Brenner anrufen, Teillieferung (60 Stk) klären, neuen Liefertermin KW 22 nennen | Mittwoch |
| Tom | Einarbeitungsplan für 2 Azubis erstellen | Monatsende |
| Petra | Rechnung RE-2024-0815 mit der Buchhaltung prüfen, ggf. Gutschrift | offen |
| Fr. Yilmaz | Prüfbericht LS-3015 lesen und für die Geschäftsführung zusammenfassen | nächster Jour fixe |
| Jonas | Lieferantenliste bereinigen | Q3 oder vor dem Audit [klären] |

## Offene Punkte
1. Abgabefrist der Flyer-Daten: Freitag oder Donnerstag (Feiertag)?
2. Rabatt für Brenner: Soll bei der Geschäftsführung eine Freigabe (max. 5 %) beantragt werden? Wer macht das?
3. Termin des Lieferantenaudits und daraus folgend die Frist für die Lieferantenliste.
4. Ist "frei Haus" für Brenner tatsächlich vereinbart?
5. Genaues Datum der Sitzung für die Ablage.

## Nächster Termin
In zwei Wochen, Raum 2.14, 9:30 Uhr.

*Hinweis: Ich habe nur das übernommen, was in den Notizen steht. Unsichere Angaben sind in eckigen Klammern markiert. Die Aufgabe "Rabatt/Freigabe" habe ich keiner Person zugeordnet, weil das in den Notizen nicht entschieden wurde. Bitte vor dem Versand prüfen.*

---

### Opus

#### Nutzer 1
Schreib ein Protokoll.

[INHALT VON /home/daniel/tbc-ai-tutorials/07_Beispielmaterial/notizen_besprechung.txt]

#### Assistent 1
Hier ist ein Protokoll, das aus deinen Notizen erstellt wurde. Was in den Notizen fehlt oder unklar ist, habe ich mit **[offen]** markiert. Diese Stellen solltest du ergänzen, bevor du das Protokoll verschickst.

---

# Protokoll – Teambesprechung Vertrieb/Technik

| | |
|---|---|
| **Datum** | Dienstag, [offen: genaues Datum] |
| **Ort** | Raum 2.14 |
| **Teilnehmende** | Sabine K., Jonas, Fr. Yilmaz, Tom (kam später dazu), Petra W. (nur in der ersten Hälfte) |
| **Protokoll** | Jonas |
| **Nächster Termin** | in 2 Wochen, [offen: Datum], 9:30 Uhr, Raum 2.14 |

---

## 1. Messe Hannover / Industrietage

- Der Stand ist gebucht. Die Prospekte sind aber veraltet.
- Sabine lässt neue Flyer machen. Die Druckerei braucht die Druckdaten spätestens Ende nächster Woche. **[offen: Donnerstag oder Freitag? Wegen des Feiertags bitte klären]**
- Für den Stand ist noch nicht genug Personal eingeplant. Jonas und Fr. Yilmaz haben zugesagt. Sabine fragt noch in der Technik nach, wer mitkommen kann.

## 2. Kunde Brenner – Lieferverzug SG-40

- Herr Brenner hat sich über den Lieferverzug beim SG-40 beschwert (siehe seine E-Mail).
- Zuerst hatte die Fertigung die Gehäuse für KW 23 angekündigt. **Laut einem Nachtrag kommen sie jetzt schon in KW 22.**
- Tom ruft Herrn Brenner bis Mittwoch an. Er nennt ihm KW 22 als Liefertermin und klärt, ob eine Teillieferung von 60 Stück möglich ist.
- **Rabatt:** Laut Petra sind höchstens 5 % möglich, und nur mit Freigabe der Geschäftsführung. Die Frage wurde diskutiert, **es gab aber keine Entscheidung.**

## 3. Rechnung RE-2024-0815 an Brenner

- Die Frachtkosten auf der Rechnung sind möglicherweise falsch. Vereinbart war vermutlich „frei Haus“. [offen: bitte bestätigen]
- Petra prüft das mit der Buchhaltung. Bei Bedarf wird eine Gutschrift ausgestellt.

## 4. Prüfbericht Laserschneidanlage LS-3015

- Der Prüfbericht ist da (etwa 6 Seiten). Bisher hat ihn offenbar noch niemand gelesen.
- Fr. Yilmaz liest den Bericht und schreibt bis zum nächsten Jour fixe eine Zusammenfassung für die Geschäftsführung.

## 5. Lieferantenliste

- Die Lieferantenliste ist nicht gepflegt: Es gibt doppelte Einträge und veraltete Nummern.
- Jonas räumt die Liste auf. Er plant das für Q3. Petra möchte die Liste aber vor dem Lieferantenaudit fertig haben. **[offen: Wann ist das Audit? Vermutlich Mitte Juni. Den Termin bitte noch festlegen]**

## 6. Reisekostenrichtlinie v2

- Eine neue Reisekostenrichtlinie (Version 2) kommt. Niemand im Team weiß genau, was sich ändert.
- Sabine fragt bei der Personalabteilung nach und schickt dem Team eine kurze Info.

## 7. Azubi-Projekt

- Tom betreut ab nächstem Monat 2 Auszubildende.
- Er erstellt bis Monatsende selbst einen Einarbeitungsplan.

## 8. Sonstiges

- Die Kaffeemaschine im 2. OG ist kaputt. Der Hausmeister weiß Bescheid. *(erledigt)*

---

## Aufgabenübersicht

| Nr. | Aufgabe | Zuständig | Frist |
|---|---|---|---|
| 1 | Neue Messe-Flyer erstellen, Druckdaten an die Druckerei | Sabine | Ende nächster Woche (Do/Fr – [offen]) |
| 2 | In der Technik nach Standpersonal für die Messe fragen | Sabine | [offen] |
| 3 | Herrn Brenner anrufen: Liefertermin KW 22, Teillieferung 60 Stk. klären | Tom | bis Mittwoch |
| 4 | Rabatt für Brenner klären (max. 5 %, GF-Freigabe nötig) | [offen] | [offen] |
| 5 | Frachtkosten auf RE-2024-0815 prüfen, ggf. Gutschrift | Petra mit Buchhaltung | [offen] |
| 6 | Prüfbericht LS-3015 lesen und für die GF zusammenfassen | Fr. Yilmaz | nächster Jour fixe |
| 7 | Lieferantenliste aufräumen | Jonas | vor dem Lieferantenaudit [offen: Termin], spätestens Q3 |
| 8 | Bei der Personalabteilung nach Reisekostenrichtlinie v2 fragen, Team informieren | Sabine | [offen] |
| 9 | Einarbeitungsplan für die 2 Azubis erstellen | Tom | Monatsende |

---

**Hinweise zum Schluss:**
- Der Liefertermin steht im Protokoll schon mit **KW 22**, so wie im Nachtrag. Tom sollte dem Kunden nicht mehr KW 23 nennen.
- Zur Rabattfrage fiel keine Entscheidung. Sie sollte als Punkt auf die nächste Tagesordnung oder direkt an die Geschäftsführung gehen.
- Bei einigen Aufgaben fehlt eine Frist. Bitte ergänzen, falls das in der Besprechung besprochen wurde.

Soll ich das Protokoll kürzer machen, zum Beispiel als E-Mail an alle Teilnehmenden, oder als reine Aufgabenliste?
