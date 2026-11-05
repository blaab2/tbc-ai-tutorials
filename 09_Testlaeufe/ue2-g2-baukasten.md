# Testlauf: Übung 2 / Für Schnelle G – Baukasten-Prompt Notizen: Zusammenfassung + Aufgabentabelle

**Herkunft:** Aufgabe G, zweiter Prompt (Baukasten-Prompt), aus [Uebung_2_Gute_Prompts.md](../06_Uebungen/Uebung_2_Gute_Prompts.md#aufgabe-g--baukasten-an-einem-anderen-beispiel) (Block 4, Stufe 3: Für Schnelle). Material: [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt). Zugehörige Lösungshinweise: [Trainer-Loesungshinweise.md – Übung 2](../06_Uebungen/Trainer-Loesungshinweise.md#woran-du-ein-gutes-ergebnis-erkennst) (Punkt „Aufgabe G (Notizen)“) und die erwartete Aufgabentabelle bei [Übung 3, Station C](../06_Uebungen/Trainer-Loesungshinweise.md#station-c-notizen--protokoll-und-aufgabentabelle).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt (jeweils in einem neuen Chat, Notizen aus der Beispieldatei angehängt):**

```text
Du bist Assistenz der Teamleitung. Unten stehen ungeordnete Notizen aus
unserer Teambesprechung. Erstelle daraus:
1. eine Zusammenfassung in höchstens 5 Sätzen,
2. eine Tabelle aller Aufgaben mit den Spalten Aufgabe | Wer | Bis wann.
Wenn "Wer" oder "Bis wann" in den Notizen fehlt, schreibe "offen" –
erfinde nichts.

[HIER DIE NOTIZEN EINFÜGEN]
```

**Was laut Material herauskommen soll:** Eine Zusammenfassung in höchstens 5 Sätzen und eine vollständige Aufgabentabelle. Sie übernimmt den NACHTRAG (Gehäuse **KW 22** statt KW 23) und markiert fehlende Angaben mit „offen“. Erwartet werden 8 Aufgaben (Tabelle Station C): Flyer/Druckerei (Sabine K., Ende nächster Woche, Do oder Fr unklar), Brenner anrufen + Teillieferung 60 Stk. + KW 22 weitergeben (Tom, bis Mittwoch), Prüfbericht LS-3015 (Fr. Yilmaz, nächster Jour fixe), Lieferantenliste (Jonas, „Q3“ vs. „vor Audit, Mitte Juni?“), Reisekostenrichtlinie v2 (Sabine K., offen), Rechnung RE-2024-0815 (Petra W., offen), Einarbeitungsplan Azubis (Tom, Monatsende), Technik nach Standpersonal fragen (Sabine K., offen). Die Kaffeemaschine ist keine Aufgabe. Keine erfundenen Kalenderdaten.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Zusammenfassung ≤ 5 Sätze (gezählt per `python3`) | **ja**, 5 Sätze (ca. 97 Wörter) | **nein, 7 Sätze** (ca. 100 Wörter) | **nein, 7 Sätze** (ca. 126 Wörter) |
| NACHTRAG KW 22 übernommen | ja (Zusammenfassung + eigene Tabellenzeile) | ja (Zusammenfassung + eigene Zeile + Hinweis „Nachtrag als aktuelleren Stand behandelt“) | ja (Zusammenfassung + in Toms Anrufzeile + Hinweis) |
| Alle 8 erwarteten Aufgaben enthalten | ja | ja | ja |
| Zeilen in der Tabelle | 11 (8 + KW-22-Zeile + Rabatt + Kaffeemaschine) | 10 (8 + KW-22-Zeile + Rabatt) | 9 (8 + Rabatt) |
| Kaffeemaschine nicht als Aufgabe | **nein**: als Zeile „reparieren lassen – Hausmeister – erledigt“ | ja (ausdrücklich im Hinweis begründet) | ja (ausdrücklich im Hinweis begründet) |
| Rabatt als offene Frage, nicht als Beschluss | ja (Zeile, Wer/Bis wann „offen“; Satz „nicht entschieden“) | ja („kein Ergebnis“; Zeile mit „offen“) | ja („keine Einigung“; Zeile mit „offen“) |
| Druckerei-Termin Do/Fr als unklar markiert | ja | ja | ja |
| Widerspruch Q3 vs. Audit sichtbar | ja, aber „Mitte Juni“ fehlt in der Tabelle | ja, inkl. „evtl. Mitte Juni“ + Hinweis | ja, inkl. „evtl. Mitte Juni“ |
| Standpersonal nicht als feste Zusage | ja („Interesse signalisiert“) | ja („würden gehen“) | ja („würden mitgehen“) |
| „offen“ bei fehlenden Angaben | ja (Reisekosten, Rechnung, Standpersonal) | ja | ja |
| Erfundene Kalenderdaten | keine | keine | keine |
| Sonstige Ergänzungen/Vermutungen | „Hausmeister“ als Wer; „vermutlich zusammen mit dem Anruf bis Mittwoch“ (als Vermutung gekennzeichnet) | „Sabine kümmert sich um … das Standpersonal“ (leicht überzogen, sie fragt nur die Technik) | KW-22-Weitergabe ohne Kennzeichnung unter „bis Mittwoch“ gefasst (wie Musterlösung) |
| Zusätzliche Hinweise | 1 Hinweis (Besprechungsdatum) | 5 Hinweise, inkl. „bei der Fertigung bestätigen lassen“ | 4 Hinweise, inkl. Rückfrage zu Rabatt und Audittermin |
| Gesamt | gut, ein klarer Fehler (Kaffeemaschine) | sehr gut im Inhalt, Formatvorgabe verletzt | sehr gut im Inhalt, Formatvorgabe verletzt; am nächsten an der Musterlösung |

**Kurz:** Die Kernerwartung trifft bei allen drei Modellen zu: Der NACHTRAG wird übernommen, alle 8 Aufgaben sind da, die Unklarheiten (Do/Fr, Q3 vs. Audit) bleiben sichtbar, nichts wird in Kalenderdaten umgerechnet. Zwei Abweichungen sind aber typisch und gut für die Auswertung: Sonnet und Opus halten die Vorgabe „höchstens 5 Sätze“ **nicht** ein (je 7 Sätze), und Haiku nimmt die erledigte Kaffeemaschine in die Aufgabentabelle auf.

---

## Gefundene Fehler mit Beleg

1. **Sonnet – 7 statt höchstens 5 Sätze.** Gezählt per `python3` (Abkürzungen wie „max.“ herausgerechnet). Die Sätze 3–5 („Beim Kunden Brenner gibt es Ärger …“, „Tom soll ihn anrufen …“, „Laut Nachtrag von Jonas …“) sind kurze Einzelsätze, Satz 7 ist eine Themenaufzählung. Der Prompt verlangt ausdrücklich „eine Zusammenfassung in höchstens 5 Sätzen“.
2. **Opus – 7 statt höchstens 5 Sätze.** Gleiche Zählung. Zusätzlich hängt Opus den nächsten Termin an („Die nächste Besprechung ist in 2 Wochen …“). Inhaltlich richtig (Notizen: „Nächster Termin: in 2 Wo, gleicher Raum, 9:30“), aber über das Limit. Mit ca. 126 Wörtern ist es die längste Zusammenfassung.
3. **Haiku – Kaffeemaschine als Aufgabe.** Tabellenzeile „Kaffeemaschine 2. OG reparieren lassen | Hausmeister | erledigt (Hausmeister informiert)“. In den Notizen steht nur „Kaffeemaschine 2. OG kaputt, Hausmeister infomiert (erledigt)“. Erledigt ist die Information an den Hausmeister, nicht die Reparatur. „Reparieren lassen – Hausmeister“ ist also eine Umdeutung. Das ist genau die Falle aus Station C („Kaffeemaschine landet oft als offene Aufgabe in der Tabelle“). Haiku markiert sie immerhin als „erledigt“, nicht als offen.
4. **Haiku – „Mitte Juni“ fehlt in der Tabelle.** Bei der Lieferantenliste steht nur „Q3 (Petra wünscht vor dem Lieferantenaudit, Termin unklar)“. Die Notizen nennen „(wann ist das nochmal? Mitte Juni?)“. Der Widerspruch (Mitte Juni liegt **vor** Q3, also Juli–September) wird so schwerer erkennbar. „Mitte Juni“ taucht nur im Schlusshinweis auf.
5. **Haiku – schiefe Begründung im Hinweis.** „Das Datum der Besprechung fehlt … Deshalb lassen sich die Angaben ‚Q3‘ und ‚Mitte Juni‘ nicht sicher einordnen.“ Q3 und Mitte Juni hängen nicht vom Wochentag der Besprechung ab. Betroffen wären eher „bis Mittwoch“, „Ende nächster Woche“ und „Monatsende“ (so richtig bei Sonnet und Opus).
6. **Sonnet – leichte Überzeichnung.** „Sabine kümmert sich um neue Flyer und das Standpersonal.“ In den Notizen steht nur „Sabine fragt noch Technik“. In der Tabelle formuliert Sonnet es korrekt („Standpersonal … klären …, Technik fragen“).
7. **Abweichung von der Musterlösung, kein Fehler – KW 22 als eigene Zeile.** Haiku und Sonnet machen aus dem NACHTRAG eine eigene Aufgabe mit „Bis wann: offen“ (Haiku: „vermutlich zusammen mit dem Anruf bis Mittwoch“). Die Musterlösung (Station C, Nr. 2) fasst es mit dem Anruf zusammen und setzt „bis Mittwoch“. Streng nach den Notizen hat der Nachtrag **keine** Frist („Tom bitte so an Kunde weitergeben“). Die Lösung von Sonnet ist also die wörtlichere, Opus und die Musterlösung schließen auf Mittwoch.
8. **Abweichung, kein Fehler – Rabatt als Tabellenzeile.** Alle drei führen „Rabatt entscheiden“ mit „offen | offen“ als Aufgabe. Die Musterlösung führt den Rabatt nicht als Aufgabe, sondern unter „Entscheidung offen“. Wichtig ist nur, dass kein Beschluss daraus wird. Das ist bei allen erfüllt.
9. **Keine falschen Zahlen, Namen oder Daten.** Alle Kennungen stimmen mit den Notizen überein (SG-40, 60 Stk., KW 22/23, LS-3015, RE-2024-0815, max. 5 %, 2 Azubis, 2. OG, 9:30). Kein Modell rechnet ein Kalenderdatum aus.
10. **Testartefakt Haiku, kein Modellverhalten:** In der Haiku-Nutzernachricht steht am Ende „Gib das komplette Gesprächsprotokoll zurück, Format: …“. Das stammt aus der Testumgebung, nicht aus dem Übungsprompt. In allen drei Protokollen sind die Notizen nur als Platzhalter vermerkt (z. B. „[Anhang: notizen_besprechung.txt]“). Sie wurden vollständig übergeben.

---

## Lehren für die Auswertung

- **Die Übung funktioniert.** Der Baukasten-Prompt mit „schreibe ‚offen‘ – erfinde nichts“ führt bei allen drei Modellen zu einer brauchbaren, prüfbaren Aufgabentabelle. Der NACHTRAG wird überall übernommen. Die Frage im Übungsblatt („Hat sie den Nachtrag … berücksichtigt?“) bekommt also meist ein „ja“. Das ist ein positives Erlebnis für den Prompt-Baukasten.
- **Bestes Lernbeispiel: Sätze zählen lassen.** Zwei von drei Modellen überschreiten „höchstens 5 Sätze“, obwohl es ausdrücklich im Prompt steht. Teilnehmende sollen die Sätze **selbst zählen**. Lehre: Formatvorgaben werden oft, aber nicht immer eingehalten – prüfen statt vertrauen. Gute Nachschärfung (Brücke zu Aufgabe D): „Kürze die Zusammenfassung auf genau 5 Sätze.“
- **„Mehr“ ist nicht immer „besser“.** Opus und Sonnet liefern die inhaltlich vollständigsten Zusammenfassungen, gerade deshalb sind sie zu lang. Haiku hält das Limit ein, macht aber den Kaffeemaschinen-Fehler. Kein Modell ist in allem fehlerfrei.
- **Kaffeemaschine als Prüfpunkt:** Gezielt fragen „Steht bei euch die Kaffeemaschine in der Tabelle?“ Wenn ja: Was ist eigentlich erledigt – die Reparatur oder nur die Meldung?
- **Hinweise am Ende sind wertvoll.** Sonnet und Opus melden die Widersprüche von sich aus (KW 22/23, Q3/Audit, unklares Besprechungsdatum). Sonnet empfiehlt sogar, KW 22 vor der Weitergabe an den Kunden bei der Fertigung bestätigen zu lassen. Das ist genau die Haltung, die die Schulung vermitteln will.
- **Zur Musterlösung:** Wenn Teilnehmende den Nachtrag als eigene Zeile mit „offen“ haben, ist das kein Fehler, sondern wörtlich korrekt. Dasselbe gilt für den Rabatt als Zeile mit „offen | offen“. Nicht auf exakt 8 Zeilen bestehen, sondern auf die Inhalte achten.
- **„offen“ wird klug, nicht mechanisch gesetzt.** Bei Druckerei-Termin und Lieferantenliste schreibt kein Modell „offen“, sondern die unklare Angabe mit Kennzeichnung („unklar“, „Termin unklar“). Das ist besser als ein nacktes „offen“, weil die Information erhalten bleibt.
- **Vergleich mit dem Minimal-Prompt** („Fass das zusammen.“) wurde in diesem Testlauf nicht durchgeführt. Für die Frage „Welche Aufgaben findet nur der zweite Prompt?“ sollte der Trainer die Gegenprobe vorher selbst machen.
- **Zeit:** Lesen der Antwort und Abgleich mit den 20 Zeilen Notizen dauert ca. 4–6 Minuten. Passt als „Für Schnelle“-Aufgabe, aber nicht zusätzlich zu F in wenigen Restminuten.

---

## Probleme im Material und Vorschläge

- **Lösungshinweis G: Satzlimit nicht als Prüfpunkt genannt.** In [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md#woran-du-ein-gutes-ergebnis-erkennst) beim Punkt „Aufgabe G (Notizen)“ ergänzen:
  > „Zählt die Sätze der Zusammenfassung: Im Test lagen zwei von drei Modellen bei 7 statt höchstens 5 Sätzen. Gute Gelegenheit zum Nachschärfen (‚Kürze auf genau 5 Sätze‘).“
- **Lösungshinweis G: „markiert … mit ‚offen‘“ ist missverständlich.** Dort steht: „markiert Aufgaben ohne Person oder Frist mit ‚offen‘ – z. B. Standpersonal für die Messe, den unklaren Druckerei-Termin (Do oder Fr?) und Jonas' ‚irgendwann im Q3‘ vs. ‚vor dem Audit‘.“ Druckerei-Termin und Jonas' Aufgabe haben eine (unklare) Frist. Die Modelle schreiben dort zu Recht die Angabe plus „unklar“, nicht „offen“. Vorschlag:
  > „… markiert fehlende Angaben mit ‚offen‘ (z. B. Frist bei Standpersonal, Reisekosten, Rechnung) und kennzeichnet unklare Angaben als unklar oder widersprüchlich, statt sie zu glätten (Druckerei Do oder Fr?, Jonas' ‚irgendwann im Q3‘ vs. ‚vor dem Audit, Mitte Juni?‘).“
- **Station C, Nr. 2: Frist für KW-22-Weitergabe ist erschlossen.** In der erwarteten Aufgabentabelle (Station C) einen Satz unter „Weitere Inhalte“ ergänzen:
  > „Wird die Weitergabe von KW 22 als eigene Zeile mit ‚Bis wann: offen‘ geführt, ist das ebenfalls richtig – der Nachtrag selbst nennt keine Frist. Auch der Rabatt als Zeile mit ‚offen | offen‘ ist in Ordnung, solange er nicht als Beschluss erscheint.“
- **Übungsblatt G: getrennte Chats.** In [Uebung_2_Gute_Prompts.md](../06_Uebungen/Uebung_2_Gute_Prompts.md#aufgabe-g--baukasten-an-einem-anderen-beispiel) nach „vergleiche wieder zwei Prompts“ ergänzen: „– jeden in einem **neuen Chat**“. Sonst kennt der zweite Prompt die Notizen schon aus dem ersten (Stolperstein „Beide Prompts im selben Chat“ aus den Lösungshinweisen).
- **Übungsblatt G: Prüffragen erweitern (optional).** Hinter die Nachtrag-Frage ergänzen: „Hat sie sich an die 5 Sätze gehalten? Steht die Kaffeemaschine als Aufgabe drin?“
- Sonst ist die Aufgabe klar formuliert, und die Notizen enthalten genug Fallen für eine lebhafte Auswertung.

---

## Gesprächsprotokolle

### Haiku

#### Nutzer 1

Du bist Assistenz der Teamleitung. Unten stehen ungeordnete Notizen aus unserer Teambesprechung. Erstelle daraus:
1. eine Zusammenfassung in höchstens 5 Sätzen,
2. eine Tabelle aller Aufgaben mit den Spalten Aufgabe | Wer | Bis wann.
Wenn "Wer" oder "Bis wann" in den Notizen fehlt, schreibe "offen" – erfinde nichts.

[Notizen: Teambesprechung Vertrieb/Technik, Di (?), Raum 2.14, mit Protokoll von J.]

Gib das komplette Gesprächsprotokoll zurück, Format:
### Nutzer 1
<Nachricht>
### Assistent 1
<deine vollständige Antwort>

#### Assistent 1

**Zusammenfassung**

Die Teambesprechung Vertrieb/Technik hat mehrere offene Punkte zu Messe, Kunde Brenner, Lieferanten und Reisekosten ergeben. Dringend ist der Anruf bei Herrn Brenner bis Mittwoch wegen des Lieferverzugs bei SG-40, wobei laut Nachtrag die Gehäuse schon in KW 22 kommen sollen. Für die Messe Hannover müssen die veralteten Flyer neu gedruckt werden, die Druckerei braucht die Daten spätestens Ende nächster Woche, und das Standpersonal ist noch offen. Außerdem sind die Frachtkosten der Rechnung RE-2024-0815 zu prüfen, der Prüfbericht zur Laserschneidanlage LS-3015 zusammenzufassen und die Lieferantenliste zu bereinigen. Die Rabattfrage (max. 5 %, nur mit GF-Freigabe) wurde nicht entschieden.

**Aufgabentabelle**

| Aufgabe | Wer | Bis wann |
|---|---|---|
| Neue Flyer für Messe Hannover / Industrietage erstellen und Druckdaten liefern | Sabine K. | Ende nächster Woche (Fr oder Do, unklar) |
| Hr. Brenner wegen SG-40-Verzug anrufen und Teillieferung von 60 Stk. klären | Tom | Mittwoch |
| Kunde Brenner über Nachtrag informieren: SG-40-Gehäuse kommen laut Fertigung schon KW 22 | Tom | offen (vermutlich zusammen mit dem Anruf bis Mittwoch) |
| Rabatt für Kunde Brenner entscheiden (max. 5 %, nur mit GF-Freigabe) | offen | offen |
| Prüfbericht Laserschneidanlage LS-3015 lesen und für GF zusammenfassen | Fr. Yilmaz | Bis zum nächsten Jour fixe |
| Lieferantenliste aufräumen (Dubletten, alte Nummern) | Jonas | Q3 (Petra wünscht vor dem Lieferantenaudit, Termin unklar) |
| Neue Reisekostenrichtlinie v2 bei Personal erfragen und Info ans Team schicken | Sabine | offen |
| Rechnung RE-2024-0815 an Brenner prüfen (Frachtkosten, frei Haus?) und ggf. Gutschrift veranlassen | Petra (mit Buchhaltung) | offen |
| Einarbeitungsplan für 2 Azubis erstellen | Tom | Monatsende |
| Standpersonal für Messe Hannover klären | Sabine (Anfrage bei Technik); Jonas und Fr. Yilmaz haben Interesse signalisiert | offen |
| Kaffeemaschine 2. OG reparieren lassen | Hausmeister | erledigt (Hausmeister informiert) |

Hinweis: Das Datum der Besprechung fehlt in den Notizen ("Di (?)"). Deshalb lassen sich die Angaben "Q3" und "Mitte Juni" (Lieferantenaudit) nicht sicher einordnen.

---

### Sonnet

#### Nutzer 1

Du bist Assistenz der Teamleitung. Unten stehen ungeordnete Notizen aus unserer Teambesprechung. Erstelle daraus:
1. eine Zusammenfassung in höchstens 5 Sätzen,
2. eine Tabelle aller Aufgaben mit den Spalten Aufgabe | Wer | Bis wann.
Wenn "Wer" oder "Bis wann" in den Notizen fehlt, schreibe "offen" – erfinde nichts.

[Inhalt von notizen_besprechung.txt: Notizen der Teambesprechung Vertrieb/Technik, angehängt]

#### Assistent 1

**Zusammenfassung**

Für die Messe Hannover ist der Stand gebucht, aber die Prospekte sind veraltet. Sabine kümmert sich um neue Flyer und das Standpersonal. Beim Kunden Brenner gibt es Ärger wegen des SG-40-Verzugs. Tom soll ihn anrufen und eine Teillieferung von 60 Stück klären. Laut Nachtrag von Jonas kommen die Gehäuse schon in KW 22 statt KW 23. Über einen möglichen Rabatt (Petra: maximal 5 %, nur mit GF-Freigabe) gab es kein Ergebnis, und bei der Brenner-Rechnung RE-2024-0815 prüft Petra die Frachtkosten. Weitere Themen waren der Prüfbericht zur LS-3015, die unaufgeräumte Lieferantenliste, die neue Reisekostenrichtlinie v2 und der Einarbeitungsplan für zwei Azubis.

**Aufgaben**

| Aufgabe | Wer | Bis wann |
|---|---|---|
| Neue Flyer für die Messe Hannover erstellen und Daten an die Druckerei liefern | Sabine | Ende nächster Woche (Freitag oder Donnerstag wegen Feiertag, in den Notizen unklar) |
| Hr. Brenner anrufen und Teillieferung von 60 Stk klären | Tom | Mittwoch |
| Brenner mitteilen, dass die SG-40-Gehäuse laut Fertigung schon in KW 22 kommen (Nachtrag von Jonas) | Tom | offen |
| Entscheidung über einen Rabatt für Brenner (max. 5 %, nur mit GF-Freigabe) | offen | offen |
| Prüfbericht Laserschneidanlage LS-3015 (ca. 6 Seiten) lesen und für die GF zusammenfassen | Fr. Yilmaz | Nächster Jour fixe (Datum nicht genannt) |
| Lieferantenliste bereinigen (Dubletten, alte Nummern) | Jonas | "Irgendwann im Q3". Petra möchte es vor dem Lieferantenaudit, dessen Termin unklar ist (evtl. Mitte Juni). |
| Bei Personal klären, was sich in der Reisekostenrichtlinie v2 geändert hat, und eine kurze Info ans Team schicken | Sabine | offen |
| Rechnung RE-2024-0815 an Brenner prüfen (Frachtkosten, "frei Haus"), ggf. Gutschrift | Petra (mit Buchhaltung) | offen |
| Einarbeitungsplan für 2 Azubis erstellen (Betreuung ab nächstem Monat) | Tom | Monatsende |
| Standpersonal für die Messe klären (Jonas und Fr. Yilmaz würden gehen), Technik fragen | Sabine | offen |

**Hinweise zu Unklarheiten in den Notizen**
- Die Lieferzeit der SG-40-Gehäuse ist widersprüchlich (KW 23 in der Besprechung, KW 22 im Nachtrag). Ich habe den Nachtrag als aktuelleren Stand behandelt. Bitte bei der Fertigung bestätigen lassen, bevor Tom es dem Kunden sagt.
- Die Frist zur Lieferantenliste ist nicht eindeutig ("irgendwann im Q3" gegen den Wunsch, vor dem Audit fertig zu sein). Der Auditttermin ist nicht gesichert.
- Der Wochentag der Besprechung ist in den Notizen mit "Di (?)" nur vermutet, deshalb lassen sich "Mittwoch" und "Ende nächster Woche" nicht in konkrete Daten umrechnen.
- Das Defekt-Thema Kaffeemaschine (2. OG) ist erledigt, der Hausmeister ist informiert. Ich habe es deshalb nicht als Aufgabe aufgenommen.
- Nächster Termin: in 2 Wochen, gleicher Raum, 9:30 Uhr.

---

### Opus

#### Nutzer 1

Du bist Assistenz der Teamleitung. Unten stehen ungeordnete Notizen aus
unserer Teambesprechung. Erstelle daraus:
1. eine Zusammenfassung in höchstens 5 Sätzen,
2. eine Tabelle aller Aufgaben mit den Spalten Aufgabe | Wer | Bis wann.
Wenn "Wer" oder "Bis wann" in den Notizen fehlt, schreibe "offen" –
erfinde nichts.

[Anhang: notizen_besprechung.txt]

#### Assistent 1

**1. Zusammenfassung**

In der Teambesprechung von Vertrieb und Technik ging es zuerst um die Messe Hannover (Industrietage): Der Stand ist gebucht, aber die Prospekte sind veraltet und das Standpersonal steht noch nicht fest. Kunde Brenner ist wegen des Verzugs beim SG-40 verärgert. Laut Nachtrag kommen die Gehäuse schon in KW 22 statt KW 23. Eine Teillieferung von 60 Stück soll geklärt werden, über einen Rabatt (max. 5 %, nur mit GF-Freigabe) gab es keine Einigung. Außerdem sollen bei der Rechnung RE-2024-0815 die Frachtkosten geprüft werden, der Prüfbericht zur Laserschneidanlage LS-3015 soll für die Geschäftsführung zusammengefasst werden, und die Lieferantenliste muss bereinigt werden. Weitere Themen waren die neue Reisekostenrichtlinie v2 und die Einarbeitung von zwei Azubis. Die nächste Besprechung ist in 2 Wochen im selben Raum um 9:30 Uhr.

**2. Aufgaben**

| Aufgabe | Wer | Bis wann |
|---|---|---|
| Neue Flyer/Prospekte für die Messe erstellen, Druckdaten an die Druckerei liefern | Sabine K. | Ende nächster Woche (Fr. oder Do. wegen Feiertag – laut Notizen unklar) |
| Hr. Brenner anrufen, Teillieferung von 60 Stk. klären und neuen Gehäusetermin KW 22 mitteilen | Tom | bis Mittwoch |
| Rabatt für Brenner entscheiden (max. 5 %, nur mit GF-Freigabe) | offen | offen |
| Prüfbericht LS-3015 lesen und für die GF zusammenfassen | Fr. Yilmaz | bis zum nächsten Jour fixe |
| Lieferantenliste bereinigen (Dubletten, alte Nummern) | Jonas | „irgendwann im Q3“ (Petra wünscht: vor dem Lieferantenaudit, Termin unklar, evtl. Mitte Juni) |
| Bei Personal nach Änderungen der Reisekostenrichtlinie v2 fragen und kurze Info ans Team schicken | Sabine K. | offen |
| Frachtkosten auf Rechnung RE-2024-0815 (Brenner) mit der Buchhaltung prüfen, ggf. Gutschrift | Petra W. | offen |
| Einarbeitungsplan für 2 Azubis erstellen | Tom | Monatsende |
| Standpersonal Messe: bei der Technik nachfragen (Jonas und Fr. Yilmaz würden mitgehen) | Sabine K. | offen |

**Hinweise:**
- Das Datum der Besprechung steht nicht eindeutig in den Notizen („Di (?)“). Deshalb lassen sich Angaben wie „Ende nächster Woche“, „bis Mittwoch“ und „Monatsende“ nicht in echte Kalenderdaten umrechnen.
- Für die Gehäuse stehen zwei Termine in den Notizen: KW 23 und, laut Nachtrag von Jonas, KW 22. Ich habe den neueren Stand (KW 22) übernommen.
- Die Kaffeemaschine im 2. OG ist erledigt (Hausmeister ist informiert) und steht deshalb nicht in der Tabelle.
- Bei der Rabattfrage und beim Termin des Lieferantenaudits solltet ihr nachfragen, wer zuständig ist und wann es so weit ist.

---

Zurück zum Übungsblatt: [Übung 2: Gute Prompts – Aufgabe G](../06_Uebungen/Uebung_2_Gute_Prompts.md#aufgabe-g--baukasten-an-einem-anderen-beispiel) · Material: [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt)
