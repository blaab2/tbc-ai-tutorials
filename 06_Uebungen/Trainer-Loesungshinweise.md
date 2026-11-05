# Trainer-Lösungshinweise zu den Übungen 1–4

**Nur für dich als Trainer – nicht an die Teilnehmenden austeilen.**

Dieses Dokument ergänzt den [Trainer-Leitfaden](../01_Trainer-Leitfaden.md). Zu jeder Übung findest du: Musterprompts, Merkmale eines guten Ergebnisses, typische Stolpersteine, Hilfen für Langsame und Zusatzaufgaben für Schnelle.

**Wichtiger Grundsatz:** Die Ergebnisse des KI-Assistenten unterscheiden sich von Mal zu Mal und von Werkzeug zu Werkzeug. Es gibt keine „eine richtige“ Antwort. Bewerte deshalb nicht den Wortlaut, sondern ob die Kriterien unten erfüllt sind – und vor allem, **ob die Teilnehmenden geprüft haben**. Teste alle Übungen vor dem Termin einmal selbst mit [KI-TOOL].

**Was in unseren Testläufen tatsächlich herauskam** (jede Aufgabe mit drei Modellen, inkl. typischer Fehler und Modellunterschiede), steht in [Erwartete Ergebnisse](Erwartete_Ergebnisse.md); die Protokolle findest du in [09_Testlaeufe](../09_Testlaeufe/README.md). Einige Erwartungen unten sind danach angepasst.

Übersicht:

- [Übung 1: Texte schreiben](#übung-1-texte-schreiben) (Block 3, 0:30–1:00)
- [Übung 2: Gute Prompts](#übung-2-gute-prompts) (Block 4, 1:00–1:30)
- [Übung 3: Dokumente und Tabellen](#übung-3-dokumente-und-tabellen) (Block 5, 1:40–2:20)
- [Übung 4: Eigene Aufgabe](#übung-4-eigene-aufgabe) (Block 6, 2:20–2:50)
- [Allgemeine Hilfen beim Herumgehen](#allgemeine-hilfen-beim-herumgehen)

---

## Übung 1: Texte schreiben

Übungsblatt: [Uebung_1_Texte_schreiben.md](Uebung_1_Texte_schreiben.md) · Material: [kundenmail_beschwerde.txt](../07_Beispielmaterial/kundenmail_beschwerde.txt)

### Was in der Kundenmail steckt (zum Abgleichen)

Herr Brenner (Brenner Gerätebau GmbH, fiktiv) schreibt wegen Auftrag **4711-NT**, 120 Steuergehäuse **SG-40**. Eine gute Antwort muss auf **alle fünf Anliegen** eingehen:

1. Lieferverzug: zugesagt KW 18, jetzt KW 21, nichts angekommen; keine Information, zweimal vertröstet.
2. Forderung nach einem **verbindlichen, schriftlichen Liefertermin**.
3. Bereitschaft zu einer **Teillieferung von 60 Stück**.
4. Forderung nach **mindestens 10 % Nachlass**.
5. Nebenthema: **Rechnung RE-2024-0815**, Frachtkosten 85 € trotz vereinbarter Lieferung frei Haus.

Dazu: Frist **bis Mittwoch**, Drohung mit Lieferantenwechsel, aber auch: acht Jahre gute Zusammenarbeit (gut für den Ton der Antwort).

### Musterprompts

Der Startprompt aus dem Übungsblatt reicht. Wenn jemand ein schwaches Ergebnis hat, hilft diese Ergänzung:

```
Bitte prüfe deinen Entwurf: Geht er auf alle Anliegen des Kunden ein?
Liste die Anliegen aus der Kundenmail auf und markiere ehrlich je Anliegen:
erfüllt / nur teilweise / fehlt – mit dem passenden Satz aus deinem Entwurf.
Für alles, was wir noch klären müssen (Termin, Teillieferung, Nachlass, Rechnung),
setze einen Platzhalter. Achte auf die Frist bis Mittwoch.
Gib danach den überarbeiteten Entwurf vollständig aus.
```

Für die Ton-Varianten (Aufgabe B) zusätzlich:

```
Zeig mir die förmliche und die wärmere Version nebeneinander in einer Tabelle, Satz für Satz.
```

### Woran du ein gutes Ergebnis erkennst

- Entschuldigung ohne Ausreden und ohne Schuldzuweisung an Fertigung oder Lieferanten.
- Alle fünf Anliegen sind angesprochen, mindestens mit „prüfen wir und melden uns bis …“.
- **Keine erfundenen Zusagen:** kein konkreter Liefertermin, kein Rabatt in Prozent, keine Gutschrift – stattdessen Platzhalter wie [NEUER LIEFERTERMIN].
- Konkreter nächster Schritt (Rückruf, Termin bis Mittwoch).
- Höchstens ca. 150 Wörter, Sie-Form, Auftragsnummer genannt (Betreff genügt).
- Selbstprüfung (Ergänzungsprompt oben): Die KI markiert auch Lücken. Wenn alles abgehakt ist, selbst gegenlesen – steht z. B. „voraussichtlich“ im Text, obwohl der Kunde genau das ablehnt?
- Übersetzung (Aufgabe C): Auftragsnummer, Stückzahl, KW-Angaben und Platzhalter sind erhalten; die Rückübersetzung zeigt keine neuen oder verlorenen Zusagen. Achtung: „KW 18“ wird meist zu „calendar week 18“, manchmal zu „week 18“. Beides ist verständlich, in Großbritannien aber unüblich. Besser: ein Datum oder „the week commencing [DATUM]“. Guter Diskussionspunkt.
- Wichtig: Die Übersetzung kann nur so vollständig sein wie der deutsche Entwurf. Fehlen dort schon die 60 Stück, die Rechnung oder die 10-%-Forderung, fällt das bei der Übersetzungs- und Rückübersetzungsprüfung nicht auf. Deshalb die Checkliste aus Aufgabe A vor der Übersetzung abhaken.
- Eigene Mail (Aufgabe D): Platzhalter unverändert, kein Inhalt verloren oder dazugekommen (z. B. „Druckerei wartet schon“), die 3 Stichpunkte beschreiben die tatsächlichen Änderungen, die lockere Version bleibt freundlich. Modelle ergänzen oft unverlangt einen Betreff.
- Betreffzeilen (Aufgabe E): höchstens 8 Wörter, sachlich, mit Auftragsnummer 4711-NT; keine Zusage im Betreff, die die Mail nicht hält (z. B. „Verbindlicher Liefertermin“, solange [NEUER LIEFERTERMIN] noch offen ist). Wortzahlen, die der KI-Assistent selbst angibt, nachzählen.

### Typische Stolpersteine

- **Erfundene Fakten:** Der KI-Assistent schreibt „Die Lieferung erfolgt am 24.05.“ oder „Als Entschädigung gewähren wir Ihnen 5 %“. Wenn das passiert, im Plenum kurz zeigen. Mit dem Platzhalter-Satz im Startprompt erfinden aktuelle Modelle aber meist nichts und vergessen auch die Rechnung selten (im Testlauf: keins von drei). Dann auf feinere Fehler achten: bedingte Zusagen („korrigieren wir, falls …“), Übertreibungen („Ihre Montage steht“ statt „teilweise“), fehlende Fristen, nicht aufgegriffene Mittwoch-Frist. Um den Klassiker „erfundener Termin“ zu zeigen, den Prompt einmal ohne den Absatz „Erfinde keine Fakten …“ laufen lassen (vorher testen).
- **Rechnung vergessen:** Das Nebenthema RE-2024-0815 kann unter den Tisch fallen – vor allem bei Folgevarianten (z. B. „keine Teillieferung“).
- **Tonwechsel verschiebt Zusagen (Aufgabe B):** Beim Umformulieren wird aus „prüfen wir“ schnell „ich habe mich darum gekümmert“ oder „die Lieferung kommt verbindlich am …“. Nach jeder Variante die Checkliste aus Aufgabe A erneut anwenden. Außerdem: „wärmer“ macht die Mail oft länger als 150 Wörter, beim Kürzen fällt mitunter die Anrede weg.
- **„Lockerer“ kippt** manchmal ins Vorwurfsvolle („Wo bleiben die denn?“) – Aufgabe D.
- **Betreff verspricht mehr als die Mail (Aufgabe E):** „Terminbestätigung“ oder „Rückmeldung bis Mittwoch“ im Betreff, obwohl der Termin nur als Platzhalter dasteht.
- **Perspektivwechsel (Aufgabe F):** Die Kundensicht fordert Termin, feste Ansprechperson, Erklärung und Entgegenkommen und kritisiert dabei auch Platzhalter. Bei der Überarbeitung schleichen sich dadurch neue Zusagen ein („Ich übernehme Ihren Fall persönlich“, „verbindlich bis spätestens Mittwoch“, „vereinbart war frei Haus“). Überarbeitung erneut mit der Checkliste aus Aufgabe A prüfen lassen.
- **Zu lang und zu unterwürfig:** Drei Absätze Entschuldigung, kein Inhalt. Tipp: „Kürzer, sachlicher, weniger Entschuldigung.“
- **Echte Daten in Aufgabe D:** Teilnehmende kopieren eine echte Mail mit Namen, Adressen, Preisen. Freundlich auf die [Daten-Ampel](../03_Daten-Ampel.md) hinweisen und Platzhalter zeigen.
- **Chat-Verlauf:** Wer für die Rückübersetzung keinen neuen Chat öffnet, bekommt oft einfach die deutsche Version zurück – die Prüfung ist dann wertlos.
- **Platzhalter nicht ersetzt:** Wer den Rückübersetzungs-Prompt ohne englischen Text abschickt, bekommt eine Rückfrage (im Test erfand kein Modell etwas). Bei Tools mit Memory-Funktion ggf. einen temporären Chat nutzen.

### Hilfen für Langsame

- Prompt direkt aus der Datei kopieren lassen, nicht abtippen.
- Nur Aufgabe A und **eine** Variante aus B machen – das reicht als Basis.
- Gemeinsam mit dem Teampartner auf einen Bildschirm schauen; eine Person tippt, die andere prüft mit der Checkliste.
- Satz anbieten: „Du musst nicht alles schaffen. Wichtig ist, dass du den Entwurf kritisch liest.“

### Zusatzaufgaben für Schnelle

- Aufgaben E–G auf dem Übungsblatt. Aufgabe G: Gutes Ergebnis = genau 3 Sätze per du; Sachstand (4711-NT, 120 SG-40, KW 18 → KW 21); Inhalt des Entwurfs ohne neue Zusagen; Klärungsauftrag an die Logistik: verbindlicher Termin + Teillieferung 60 Stück, rechtzeitig vor der Kundenfrist Mittwoch. Typisch: sehr lange Sätze; Nachlass/Fracht landen fälschlich im Logistik-Auftrag; Modelle schreiben „wir haben geantwortet“, obwohl nur ein Entwurf existiert.
- Zusätzlich: „Schreib eine interne Mail an die Geschäftsführung mit der Bitte um Entscheidung zum Nachlass. Stelle Pro und Contra in je 3 Punkten dar.“ (Im selben Chat wie Aufgabe A stellen.) Gutes Ergebnis: genau 3 Pro (z. B. 8 Jahre Kundenbeziehung, Drohung mit Lieferantenwechsel, eigenes Versäumnis, Stillstand beim Kunden) und 3 Contra (Margenverlust, Präzedenzfall, Alternative Teillieferung), Forderung korrekt „mindestens 10 %“, Frist Mittwoch. Der Auftragswert steht nicht in der Kundenmail – nennt die KI einen Eurobetrag für den Nachlass, ist er erfunden. Stolperstein: KW 21 ist die aktuelle Woche, kein neuer Termin. Optional: „höchstens 150 Wörter“ ergänzen.
- Oder: „Formuliere eine Antwort, falls wir die Teillieferung **nicht** leisten können. Behalte die übrigen Punkte bei.“ – Wie geht man mit schlechten Nachrichten um? Gut ist: klare Absage ohne „derzeit“/„nicht darstellen“, Platzhalter für die Begründung statt eines erfundenen Grundes, wenn möglich eine Alternative, Nachlass und Rechnung weiterhin enthalten, ggf. vorher anrufen.

---

## Übung 2: Gute Prompts

Übungsblatt: [Uebung_2_Gute_Prompts.md](Uebung_2_Gute_Prompts.md) · Prompt-Baukasten: Rolle – Kontext – Aufgabe – Format – Beispiel (siehe [Spickzettel](../05_Spickzettel.md))

### Demo-Prompts aus dem Input (Block 4, Folie 14)

Diese beiden Paare zeigst du vor der Übung live – jeweils schwachen und starken Prompt in **getrennten, neuen Chats**. Hauptbeispiel ist die Lieferantenmail (steht so auf Folie 14), die Protokoll-Variante ist die Alternative aus dem [Trainer-Leitfaden](../01_Trainer-Leitfaden.md).

**Hauptbeispiel – Mail an den Lieferanten**

Schwach:
```
Schreib eine Mail an den Lieferanten wegen der Lieferung.
```

Stark:
```
Du bist Einkäuferin bei einem kleinen technischen Hersteller. (Rolle)
Unser Lieferant hat die Lieferung von 500 Dichtungsringen zum zweiten Mal um eine Woche verschoben.
Wir brauchen sie spätestens am 15. für einen Kundenauftrag. (Kontext)
Schreib eine E-Mail, in der du um einen verbindlichen Liefertermin bis Freitag bittest. (Aufgabe)
Höchstens 120 Wörter, freundlich, aber bestimmt, mit Betreffzeile, Sie-Form. (Format)
Der Ton soll ungefähr so sein: „Wir schätzen die Zusammenarbeit, brauchen jetzt aber Verlässlichkeit.“ (Beispiel)
```

Woran die Gruppe den Unterschied sieht: Der schwache Prompt liefert eine allgemeine, oft lange Mail mit vielen Platzhaltern und Rückfragen oder – je nach Tool – erfundenen Details (Bestellnummer, Menge, Datum). Achte auf Sätze ohne Klammer, die etwas behaupten (z. B. „Fotos haben wir beigefügt“). Wer den Erfinde-Effekt sicher zeigen will: „Schreib eine fertige Mail an den Lieferanten wegen der Lieferung, ohne Platzhalter.“ – vorher testen. Der starke Prompt liefert eine fast versandfertige Mail mit Menge, Frist und klarer Bitte.

**Alternative – Protokoll aus den Besprechungsnotizen** (Material: [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt))

Schwach:
```
Schreib ein Protokoll.
```

Stark:
```
Du bist Assistenz der Teamleitung. Unten stehen meine ungeordneten Notizen aus der Teambesprechung.
Mach daraus ein kurzes Ergebnisprotokoll für das Team.
Format: 1. Beschlüsse als Stichpunkte, 2. eine Tabelle mit den Spalten Aufgabe | Verantwortlich | Termin, 3. offene Fragen.
Erfinde nichts dazu – wenn ein Verantwortlicher oder Termin fehlt, schreib „offen“.

[Notizen einfügen]
```

Den schwachen Prompt bewusst **ohne** Notizen eingeben (so steht er auf Folie 14). Dann liefert der KI-Assistent eine leere Vorlage, erfindet eine Besprechung oder fragt nach den Notizen – das zeigt, dass Kontext fehlt. Wenn du die Notizen beim schwachen Prompt mit einfügst, erkennen aktuelle Modelle die Fallen (KW 22, Rabatt offen, Kaffeemaschine erledigt) meist auch ohne Anleitung. Der Unterschied liegt dann vor allem in Format und Länge.

Worauf du beim Vergleich zeigst: Hat der starke Prompt den NACHTRAG (KW 22 statt KW 23) berücksichtigt? Steht der Rabatt als offene Frage da und nicht als Beschluss? Taucht die erledigte Kaffeemaschine nicht als Aufgabe auf? Gab es Umdeutungen (z. B. „würden gehn“ → „zugesagt“, Q3-vs.-Audit-Widerspruch aufgelöst)? (Die vollständige Aufgabenliste steht unten bei Übung 3, Station C.)

Auch der starke Prompt ist nicht fehlerfrei: Im Testlauf landete die Kaffeemaschine einmal in der Tabelle, und einmal wurde aus dem Rabatt eine erfundene Aufgabe „GF-Freigabe einholen“. Gute Gelegenheit zum Nachschärfen: „Erledigtes nicht in die Tabelle. Punkte ohne Ergebnis nur unter offene Fragen. Nimm nur Aufgaben auf, die in den Notizen jemandem zugewiesen wurden.“

### Musterprompts

Die Prompts für A–D stehen vollständig im Übungsblatt. Für Aufgabe E (eigener wiederverwendbarer Prompt) hier ein fertiges Beispiel, das du zeigen kannst, wenn jemandem nichts einfällt:

```
Rolle: Du bist eine erfahrene Assistenz der Projektleitung.

Kontext: Ich arbeite in der Projektleitung eines [ART DES UNTERNEHMENS, z. B. mittelständischen Unternehmens].
Jeden Freitag schicke ich der Geschäftsführung einen kurzen Statusbericht zu meinen Projekten.
Die Geschäftsführung will schnell sehen: Läuft alles? Wo brauche ich eine Entscheidung?

Aufgabe: Erstelle aus den Stichpunkten unten den Statusbericht dieser Woche.

Format: Pro Projekt eine Zeile in einer Tabelle mit den Spalten
Projekt | Status (grün/gelb/rot) | Was ist passiert | Nächster Schritt | Entscheidung nötig?
Darunter höchstens 3 Sätze Gesamteinschätzung. Sachlich, per du.

Wenn dir Informationen fehlen, frag nach, statt etwas zu erfinden.

Stichpunkte:
[HIER DIE STICHPUNKTE DER WOCHE – OHNE KUNDENNAMEN UND PREISE]
```

Beispiel-Stichpunkte zum Vorführen:

```
- Laserschneidanlage LS-3015: Abnahmeprüfung abgeschlossen, Bericht liegt vor, Empfehlung Abnahme unter Vorbehalt, GF muss entscheiden
- Messe Industrietage: Stand gebucht, Prospekte werden überarbeitet, Standpersonal noch offen
- Azubi-Einarbeitung: Plan in Arbeit, Start der 2 Azubis nächsten Monat, läuft nach Plan
- Lieferantenliste bereinigen: noch nicht begonnen, Termin unklar (soll vor dem Lieferantenaudit fertig sein)
```

Typisches Ergebnis: Tabelle mit gelb/gelb/grün/rot, 3 Sätze Gesamteinschätzung und angehängte Rückfragen (Audit-Datum, Vorbehalt, Standpersonal). Die KI wartet meist nicht, sondern liefert und fragt nach. Die Spalte „Entscheidung nötig?“ wird uneinheitlich gefüllt („Ja, falls …“) – wer das nicht will, ergänzt: „In der Spalte ‚Entscheidung nötig?‘ nur ‚Ja: [Frage an die GF]‘ oder ‚Nein‘.“ Testlauf: [ue2-e-muster-statusbericht.md](../09_Testlaeufe/ue2-e-muster-statusbericht.md)

### Woran du ein gutes Ergebnis erkennst

- **Vergleich A/B:** Die Teilnehmenden können konkret benennen, was der Baukasten-Prompt besser macht (passt zum Lager, erste Woche statt drei Monate, Tabelle direkt nutzbar, Willkommensnachricht dabei). Der Minimal-Prompt liefert meist einen allgemeinen Büroplan über ca. drei Monate – oft mit einer Liste von Rückfragen am Anfang oder Ende. Das Raten zeigt sich vor allem bei Dauer (3 Monate statt erste Woche) und Arbeitsplatz (Büro statt Lager).
- **Aufgabe B:** Nachricht ≤ 80 Wörter in Du-Form (nachzählen lassen, die KI-Angabe „ca. 65“ ist oft ungenau), Tabelle Mo–Fr mit genau 4 Spalten, Lagerbezug (Lagerverwaltungssystem, Wareneingang, Stapler), nur Platzhalter. Auch hier ergänzt die KI oft plausible, nicht vorgegebene Details (Treffpunkt Empfang/Haupteingang, Sicherheitsschuhe, Mittagspause) – das gehört in die Zeile „Hat die KI etwas erfunden oder vermutet?“. Kleinere Modelle übernehmen die Beispielzeile manchmal wörtlich.
- **Aufgabe C:** Der KI-Assistent stellt wirklich Fragen und wartet. Typische sinnvolle Fragen: Vorerfahrung, eingesetzte Systeme (z. B. Lagerverwaltung, Stapler), Sicherheitsunterweisungen, Ansprechpersonen, Rahmen (Arbeitszeit, Starttag, Pate). Der anschließende Plan greift die Antworten erkennbar auf (z. B. Sicherheitsunterweisung und Hochregal vor selbstständigem Arbeiten). Bonus: Die KI weist darauf hin, dass ein Staplerschein ohne betriebliche Einweisung und schriftliche Beauftragung nicht reicht.
- **Aufgabe D:** Das Ergebnis wird mit jeder Rückmeldung gezielt besser, ohne dass der Rest „zerfällt“. Typisch im Test: „Kürzer“ wirkt je nach Ausgangslänge stark oder kaum; beim Ergänzen wird gelegentlich ersetzt statt ergänzt (z. B. „Wochenrückblick“ verschwindet) oder es gehen Ansprechpersonen verloren; die „lockere“ Nachricht enthält oft geratene Details (Treffpunkt Empfang, „Arbeitsschuhe hast du“); bei „3 Punkte“ kommt manchmal ein vierter als „Bonus“. Gute Ergänzungsvorschläge: Pate/Buddy, Zugänge und PSA vor Tag 1, Pausen/Zeiterfassung/Krankmeldung, soziale Einbindung, Ziele für Woche 2.
- **Aufgabe G (Notizen):** Der Baukasten-Prompt übernimmt den NACHTRAG (Liefertermin **KW 22** statt KW 23), markiert fehlende Angaben mit „offen“ (z. B. Frist bei Standpersonal, Reisekosten, Rechnung) und kennzeichnet unklare Angaben als unklar oder widersprüchlich, statt sie zu glätten (Druckerei Do oder Fr?, Jonas' „irgendwann im Q3“ vs. „vor dem Audit, Mitte Juni?“). Abgleich mit der Tabelle bei Übung 3, Station C. Zählt die Sätze der Zusammenfassung: Im Test lagen zwei von drei Modellen bei 7 statt höchstens 5 Sätzen – gute Gelegenheit zum Nachschärfen. Der Minimal-Prompt liefert bei aktuellen Modellen oft schon alle Aufgaben und den Nachtrag, ist aber lang und uneinheitlich formatiert. Der Gewinn des Baukastens liegt hier vor allem in Kürze, festem Format und den „offen“-Markierungen.
- **Aufgabe E:** Der Prompt hat klar erkennbare feste Teile und Lücken in eckigen Klammern, enthält „frag nach, statt zu erfinden“ und ist gespeichert – und der Testlauf hält das vorgegebene Format ein. Rückfragen der KI sind ein gutes Zeichen, aber nach Daten-Ampel zu beantworten (z. B. nicht den Auftragswert nennen). Platzhalter wie [VERTRIEBSLEITUNG] verschwinden oft, wenn der Prompt nicht „Platzhalter unverändert lassen“ verlangt.
- **Aufgabe F:** Die KI nennt ≤ 5 Vorschläge, typisch sind: Format eindeutig machen, Abschnittszuordnung, Zahlen genau übernehmen, Nachfrage-Regel präzisieren, Zeitraum. Die verbesserte Version ist ca. 1,5–2-mal so lang. Teilnehmende sollen mindestens einen Vorschlag benennen, der nur länger macht (z. B. „KI nennt die Wortzahl“), und prüfen, ob „frag nach statt erfinden“ und die Lücke erhalten bleiben. Von der KI vorgeschlagene Ampel-Regeln und Beispiele gegen unsere Daten-Ampel prüfen.

### Typische Stolpersteine

- **Beide Prompts im selben Chat:** Dann „weiß“ der KI-Assistent beim zweiten Prompt schon alles – der Vergleich verwässert. Auf getrennte Chats hinweisen.
- **Bei C legt die KI manchmal sofort los** (bei aktuellen Modellen selten). Lösung: „Stopp, bitte erst die Fragen.“ Häufiger: Die KI stellt 3 Sammelfragen mit insgesamt 7–9 Teilfragen. Das ist in Ordnung; wer es kürzer will: „Stell mir genau 3 kurze Einzelfragen und warte jeweils.“
- **Beispiel wird 1:1 kopiert** (Aufgabe B) – Tipp: „Das Beispiel zeigt nur das Format.“
- **Erwartung „ein perfekter Prompt“:** Manche feilen 10 Minuten am ersten Prompt. Ermutigen, schnell zu starten und dann nachzuschärfen.
- **Rolle überschätzt:** „Du bist der beste Experte der Welt“ bringt wenig. Kontext und Format bringen meist mehr als die Rolle – das ist eine gute Erkenntnis für die Reflexion.
- **Aufgabe E zu allgemein:** „Schreib mir gute Mails“ ist nicht wiederverwendbar. Nachfragen: „Welche Mail genau, an wen, wie oft?“

### Hilfen für Langsame

- A und B gemeinsam mit dem Teampartner machen, nur einer tippt.
- Aufgabe E durch Auswahl ersetzen: Nimm das Statusbericht-Beispiel oben und passe nur zwei Lücken an.
- Den Spickzettel neben den Bildschirm legen und Baustein für Baustein abhaken.

### Zusatzaufgaben für Schnelle

- Aufgaben F und G auf dem Übungsblatt.
- „Bitte den KI-Assistenten, deinen Prompt so umzuschreiben, dass ihn auch eine Kollegin ohne Vorkenntnisse nutzen kann – mit Ausfüllhinweisen.“
- Baustein-Experiment: Denselben Prompt fünfmal laufen lassen, jedes Mal **einen** Baustein weglassen. Welcher fehlt am meisten?

---

## Übung 3: Dokumente und Tabellen

Übungsblatt: [Uebung_3_Dokumente_und_Tabellen.md](Uebung_3_Dokumente_und_Tabellen.md)

**Vorbereitung:** Stelle die Dateien aus `07_Beispielmaterial` vor dem Termin bereit (Netzlaufwerk, Download-Link oder USB-Stick). Prüfe vorab, ob Datei-Upload in [KI-TOOL] mit eurer Lizenz funktioniert. Falls nicht: Kopieren & Einfügen vorher einmal zeigen. CSV-Dateien im Texteditor öffnen lassen, **nicht** in Excel (Excel kann Datumsangaben beim Öffnen umformatieren).

**Einstieg (1:40–1:45):** Einmal live hochladen und eine Frage stellen. **Auswertung (2:12–2:20):** Pro Station eine Person fragen: „Wo lag der KI-Assistent daneben?“ Fehler feiern, nicht verstecken.

### Station A: Prüfbericht zusammenfassen

Material: [pruefbericht_lang.md](../07_Beispielmaterial/pruefbericht_lang.md) – Abnahmeprüfbericht der Laserschneidanlage **LS-3015** (PB-2024-017, ca. 1.850 Wörter).

#### Kernfakten zum Abgleichen

| Thema | Laut Bericht |
|---|---|
| Entscheidung | Geschäftsführung soll über formale Abnahme entscheiden; mit Abnahme Gefahrübergang und Schlusszahlung **30 %** des Kaufpreises fällig |
| Empfehlung | **Abnahme unter Vorbehalt** mit drei Bedingungen: (1) Software-Update 4.3 bis verbindlichem Termin, (2) Wartungsplan um Schutzglas-Intervall ergänzen, (3) getrennte Messung der Leistungsaufnahme ohne Absaugung; **Einbehalt 5 %** des Kaufpreises bis zur Erledigung |
| Taktzeiten | A: 82 s (≤ 95 s), B: 64 s (≤ 70 s), C: **41 s (≤ 40 s, knapp nicht erfüllt)** |
| Verfügbarkeit | 96,2 % (gefordert ≥ 95 %; nachgerechnet 96,15 %, also eher 96,1 % – Bonus-Prüfpunkt, ändert nichts am Ergebnis), Dauerlauf 80 h, Stillstände 35 min + 2 h 10 min + 20 min |
| Energie | 31 kW im Schneidbetrieb inkl. Absaugung, zugesagt „unter 30 kW“ → **unklar**; rund 60 % weniger als Altanlage |
| Staub | verzinktes Blech: **92 %** des internen Richtwerts; Wiederholungsmessung (Sommer, offene Tore) steht aus; Fachkraft für Arbeitssicherheit: vorläufig frei, Messung nach 3 Monaten wiederholen |
| Wirtschaftlichkeit | ca. **85.000 € / Jahr** Ersparnis, ohne Schulungen, Absaugung, Schutzgläser; Bearbeitungszeit rund 45 % kürzer, voraussichtlich Einschicht- statt Zweischichtbetrieb |
| Schulung | nur 2 Bediener geschult, mind. 2 weitere nötig, nicht im Vertrag |
| Software | Version 4.2, Update 4.3 angekündigt (behebt ERP-Übergabefehler), **kein Termin**; bis dahin teils manuelle Übertragung |

#### Versteckte Prüfpunkte (gut für die Auswertung)

- **Kaufpreis steht nicht im Bericht.** Fragt jemand „Wie viel Geld behalten wir ein?“, muss die richtige Antwort lauten: 5 % des Kaufpreises, Betrag nicht angegeben. Nennt der KI-Assistent einen Eurobetrag, ist er **erfunden** – gute Halluzinations-Probe. Aktuelle Modelle geben es bei dieser direkten Frage aber oft korrekt zu (Testlauf: alle drei haben bestanden). Wer eine erfundene Zahl provozieren will, fragt mit Druck: „Schreib eine Mail an die Buchhaltung mit dem genauen Einbehalt in Euro“ oder „Antworte nur mit dem Eurobetrag“ (vorab im eigenen Tool testen). Auch als Annahme gekennzeichnete Rechenbeispiele (z. B. „bei 400.000 € wären das 20.000 €“) ansprechen.
- **Widerspruch in der Messwerttabelle (Abschnitt 4):** Prüfteil B, Schlitzbreite: Toleranz ±0,10 mm, größte Abweichung **0,13 mm** – trotzdem als „i. O.“ bewertet. Der Bericht behauptet in Abschnitt 7, alle Maße lägen in der Toleranz. In der Zusammenfassung übernehmen KI-Assistenten meist das Fazit „alle Maße in Toleranz“ (starke Modelle melden den Widerspruch manchmal von selbst). Auf die Nachfrage „Gibt es Widersprüche?“ oder mit dem Prüfprompt „Rechne jede Zeile einzeln nach“ finden sie die Schlitzbreite dagegen oft (im Testlauf 3 von 3). Gerade dieser Kontrast ist die Lehre. Sehr gutes Beispiel dafür, dass Zusammenfassungen dem Text glauben, statt nachzurechnen.
- **Risiko, das in der Empfehlung fehlt:** Schutzglas (ca. 60 €) muss bei verzinktem Material öfter gewechselt werden, nur **2 Stück auf Lager**, Lieferzeit **3–6 Wochen**. Das ist ein echtes Stillstandsrisiko, taucht aber in Abschnitt 7 nicht als eigener Punkt auf.
- **Altanlage ohne Wartungsvertrag** als Reserve – wird oft übersehen.
- **Sicherheitsthema in Abschnitt 6:** Fernwartungs-Zugangsdaten sollen nicht per E-Mail kommen – schöne Brücke zur Daten-Ampel (Zugangsdaten = rot).

#### Musterprompts

Startprompts aus dem Übungsblatt. Zusätzlich gut für die Prüfung:

```
Nenne zu jeder Aussage deiner Zusammenfassung den Abschnitt im Bericht, aus dem sie stammt.
```

```
Überprüfe die Messwerttabelle in Abschnitt 4: Liegen alle Abweichungen wirklich innerhalb der Toleranz?
Rechne jede Zeile einzeln nach.
```

Hinweis: Das Wort „wirklich“ lenkt. Neutrale Vergleichsvariante: „Prüfe jede Zeile der Messwerttabelle in Abschnitt 4 gegen die Toleranzregel aus Abschnitt 3.1. Gib pro Zeile in Toleranz oder außerhalb an.“

#### Woran du ein gutes Ergebnis erkennst

- Genau 5 Sätze, Empfehlung „Abnahme unter Vorbehalt“ und Einbehalt 5 % sind enthalten.
- Offene Risiken: mindestens Taktzeit C, Leistungsaufnahme, Staubmessung, Wartungsplan, Software-Update, Schulung; Bonus: Schutzglas-Lieferzeit, Widerspruch Schlitzbreite.
- Keine erfundenen Beträge, Termine oder Namen.
- Die Teilnehmenden haben drei Aussagen im Original gefunden.
- Weiter: Zitat per Strg+F im Original auffindbar; „keine Angabe“ statt erfundener Schweregrade; jeden genannten Widerspruch im Original prüfen, denn auch Widerspruchslisten können erfundene Punkte enthalten (Beispiel aus dem Test: „Abschnitt 7 nennt die Leistungsaufnahme nicht“ – falsch).

#### Typische Stolpersteine (Station A)

- **Mehr als 5 Sätze** oder sehr lange Schachtelsätze – oder eine nummerierte Liste mit Unterpunkten statt Fließtext. Nachsteuern: „Genau 5 Sätze, je höchstens 20 Wörter, keine Aufzählung, keine Überschrift.“
- **Zu positiv:** Die Zusammenfassung übernimmt das optimistische Fazit aus Abschnitt 7 und lässt die offenen Punkte weg.
- **Erfundener Eurobetrag** für den Einbehalt oder die Schlusszahlung (siehe oben). Tritt im Basis-Prompt selten auf; zuverlässiger mit der Frage aus „Für Schnelle“ („Wie viel Euro behalten wir ein?“).
- **Bezugsgröße verdreht:** „Einbehalt 5 % von der Schlusszahlung“ statt „5 % des Kaufpreises von der Schlusszahlung“. Wörtlich genommen wären das 1,5 % statt 5 % des Kaufpreises.
- **Für Schnelle – andere Zielgruppen:** Beim Umschreiben werden Aussagen sicherer formuliert als im Original („wünschen sich“ → „braucht“, „ohne Termin“ → „in den nächsten Wochen“, „interner Richtwert“ → „erlaubter Wert“), und in der Kundenfassung tauchen erfundene Zusagen auf („kein Einfluss auf Ihre Aufträge“). „45 % kürzere Bearbeitungszeit“ wird gern zu „45 % schneller“ (richtig wären ca. 82 % schneller). Hilfreicher Nachsatz: „Liste auf, was du weggelassen hast und was ich vor dem Versand prüfen muss.“
- **Für Schnelle – drei Fragen der GF:** Gute Fragen zielen auf den Update-Termin, 31 kW gegen „unter 30 kW“ (Messung ohne Absaugung), Taktzeit C und Staubmessung (beide nicht im Vorbehalt), Schutzglas-Bestand und Lieferzeit, Schulungskosten, Altanlage ohne Wartungsvertrag. Typisch sind Fragenbündel statt drei Fragen. Die Schlitzbreite nennt im Test kein Modell. Prüfen, ob behauptete Lücken im Vorbehalt stimmen (Abschnitt 7).
- **Erfundener Termin** für das Software-Update 4.3 – im Bericht steht nur „im Laufe des Quartals“, ohne festen Termin.
- **Datei nur teilweise gelesen:** Bei langen Dokumenten fehlen manchmal die hinteren Abschnitte. Test: „Was steht im letzten Abschnitt?“

### Station B: Reisekostenrichtlinie v1 vs. v2

Material: [richtlinie_reisekosten_v1.md](../07_Beispielmaterial/richtlinie_reisekosten_v1.md) und [richtlinie_reisekosten_v2.md](../07_Beispielmaterial/richtlinie_reisekosten_v2.md)

#### Die vollständige Liste der Unterschiede

Die beiden Dateien unterscheiden sich in **7 inhaltlichen Punkten**. Dazu kommt eine rein redaktionelle Änderung: die Versionsnummer im Kopf („Version 1“ → „Version 2“). Sie zählt **nicht** als inhaltliche Änderung. In der Auswertung kannst du also sagen: „Es gibt 7 Änderungen – wer hat alle gefunden?“

| Nr. | Thema / Abschnitt | v1 | v2 |
|---|---|---|---|
| 1 | 3. Genehmigung – Reisen über 2.000 € | zusätzliche Freigabe durch die **Abteilungsleitung** | zusätzliche Freigabe durch die **Geschäftsführung** |
| 2 | 4.1 Bahn – 1. Klasse | ab einer einfachen Fahrtdauer von mehr als **vier** Stunden | ab mehr als **drei** Stunden |
| 3 | 4.2 Flugzeug – Inlandsflüge | keine Regel | **neu:** Inlandsflüge nur, wenn die einfache Bahnfahrt länger als **fünf Stunden** dauern würde |
| 4 | 4.3 Privates Fahrzeug – Kilometerpauschale | **0,30 €** je km | **0,25 €** je km |
| 5 | 5. Übernachtung – Obergrenze | bis **110 €** pro Nacht (ohne Frühstück) | bis **130 €** pro Nacht (ohne Frühstück) |
| 6 | 7. Sonstige Kosten – Trinkgeld | Trinkgeld bis 10 % des Rechnungsbetrags erstattungsfähig, wenn auf dem Beleg vermerkt | Regel **ersatzlos gestrichen** |
| 7 | 8. Abrechnung – Einreichungsfrist | innerhalb von **drei Monaten** | innerhalb von **sechs Wochen** |

**Beim Lesen von Hand leicht zu übersehen:** Nr. 3 (ein ganzer Satz kommt dazu), Nr. 6 (ein ganzer Satz fällt weg) und Nr. 1 (sonst wortgleicher Satz). Aktuelle KI-Assistenten finden bei sauber hochgeladenen Dateien meist alle 7 Punkte (im Testlauf alle drei Modelle). Typische Stolpersteine sind eher: (a) eine falsche Anzahl im Begleittext (z. B. „8 Änderungen“, weil die Versionsnummer mitgezählt wird) und (b) die Deutung der gestrichenen Trinkgeld-Regel als ausdrückliches Verbot („ist selbst zu tragen“). Im Dokument steht dazu schlicht nichts mehr. Unverändert sind unter anderem: Abschnitte 1, 2, 4.4, 6 und 9, die Bahncard-Regel, Parkgebühren und digitale Belege.

**Rechenfall „Für Schnelle“ (zum Nachrechnen):** Auf dem Übungsblatt steht: 180 km hin, 180 km zurück, eine Übernachtung im Hotel für 125 € (ohne Frühstück).

| | v1 | v2 |
|---|---|---|
| Fahrtkosten (360 km) | 360 × 0,30 € = **108,00 €** | 360 × 0,25 € = **90,00 €** |
| Übernachtung (125 €) | erstattet bis 110 € → **110,00 €** | voll erstattet → **125,00 €** |
| **Summe** | **218,00 €** | **215,00 €** |

Die Verpflegung lässt sich aus den Richtlinien **nicht** ausrechnen. Beide Fassungen verweisen nur auf „die jeweils aktuellen steuerlichen Pauschalen“ und nennen keine Beträge. Nennt der KI-Assistent hier konkrete Euro-Beträge, kommen sie nicht aus dem Dokument. Sie können veraltet oder falsch sein – ein gutes Beispiel für Halluzination bzw. unbelegtes Wissen. Wichtig: Prüfe vor dem Termin selbst, ob die Zahlen in den Beispieldateien noch so stehen, falls jemand die Dateien geändert hat.

**So prüfst du die Liste selbst nach (nicht mit KI, sondern mit einem Vergleichswerkzeug):**

1. Beide Dateien in einem Vergleichswerkzeug öffnen: z. B. Word „Überprüfen → Vergleichen“, Notepad++ mit Vergleichs-Plugin, oder ein Online-Werkzeug zum Textvergleich (nur weil die Daten fiktiv sind – echte Dokumente gehören nicht in fremde Online-Dienste!).
2. Jede markierte Stelle einordnen: **inhaltlich** (Betrag, Frist, Grenze, Zuständigkeit, neue/entfallene Regel) oder nur **redaktionell** (Formulierung, Reihenfolge, Tippfehler).
3. Besonders auf Zahlen achten: Pauschalen, Kilometersätze, Übernachtungsgrenzen, Einreichungsfristen, Genehmigungsgrenzen, Bahnklasse/Flugregeln.
4. Auf **verschobene** Abschnitte achten: Wenn eine Regel in v2 an anderer Stelle steht, ist das keine inhaltliche Änderung – der KI-Assistent meldet so etwas aber oft als Änderung. (In diesen Beispieldateien gibt es keine verschobenen Abschnitte.)
5. Auf **ganz neue oder ganz gestrichene** Absätze achten – die übersieht der KI-Assistent am häufigsten, weil er nach „geänderten“ Stellen sucht.

#### Musterprompts

Startprompts aus dem Übungsblatt. Zusätzlich:

```
Gehe beide Fassungen Abschnitt für Abschnitt durch. Gib für jeden Abschnitt an:
"unverändert", "nur Formulierung geändert" oder "inhaltlich geändert" – mit kurzer Begründung.
```

#### Woran du ein gutes Ergebnis erkennst

- Tabelle mit alter und neuer Regel nebeneinander, Zahlen korrekt übernommen.
- Redaktionelle Änderungen sind nicht als inhaltliche aufgeführt.
- Die Teilnehmenden haben selbst gezählt und können sagen, wie viele der tatsächlichen Änderungen gefunden wurden.
- Für Schnelle: Rechenfall (2 × 180 km, Hotel 125 €) **selbst** nachgerechnet: 218 € (v1) gegen 215 € (v2), Verpflegung nicht aus dem Dokument berechenbar.
- Für Schnelle – FAQ: Erwartbar sind Fragen zu Frist (6 Wochen, Abschn. 8), Kilometerpauschale (0,25 €, 4.3), Hotel (130 €, 5), Inlandsflug (> 5 h Bahn, 4.2), 1. Klasse (> 3 h, 4.1) und Genehmigung (GF > 2.000 €, 3). Prüfen: jede Zahl in v2 wiederfinden, keine Verpflegungsbeträge. Häufig fehlt die Trinkgeld-Frage, weil v2 dazu schweigt. Gute Diskussionsfrage: Wie erfahren Mitarbeitende von gestrichenen Regeln?
- Für Schnelle – unklare Formulierungen: Echte Kandidaten (wörtlich aus v2): „einer einfachen Fahrtdauer“ (4.1) / „einfache Bahnfahrt länger als fünf Stunden“ (4.2) – Fahrplan oder tatsächlich?, „voraussichtliche Kosten“ und „schriftlich“ (3), „zumutbar“, „in der Regel“, „kurze Strecken“ (4.4), „erfahrungsgemäß hohen Hotelpreisen“, „großer Messen“ (5), „jeweils aktuellen steuerlichen Pauschalen“ ohne Betrag und „entsprechend gekürzt“ (6), „Originalbelegen“ vs. „Digitale Belege sind zulässig“ und „können abgelehnt werden“ (8), kein Datum (9). Fast alle Assistenten nennen auch Trinkgeld und Abteilungsleitung – beides steht nicht in v2. Gut zum Unterscheiden von Lücke vs. mehrdeutiger Formulierung. Die KI findet bei dieser Frage immer etwas (7–11 Punkte); Zitate mit Strg+F prüfen, sie sind oft gebeugt oder gekürzt.

#### Typische Stolpersteine

- Der KI-Assistent kann einzelne Änderungen übersehen – vor allem ganz neue oder gestrichene Sätze (Nr. 3, Nr. 6) – und klingt dabei völlig sicher. Gute Modelle finden bei diesem kurzen Material oft alle 7, beim Einfügen langer Texte oder mit anderen Tools kann es anders aussehen. Deshalb trotzdem selbst zählen.
- Er zählt die Versionsnummer als inhaltliche Änderung mit (dann meldet er 8) – oder nennt im Begleittext eine andere Zahl als in der Tabelle.
- Beim Rechenfall rechnet er gelegentlich mit 180 statt 360 km (im Testlauf bei keinem Modell). Häufiger: Bei der Verpflegung bringt er Steuerpauschalen aus allgemeinem Wissen mit (z. B. 14 €/28 €) und rechnet sie sogar in die Gesamtsumme ein. Die Zahlen stehen nicht im Dokument, auch wenn sie als „allgemeines Wissen“ gekennzeichnet sind.
- Die Nachprüfung („Hast du etwas übersehen?“) findet oft nichts Neues, wenn die erste Tabelle schon vollständig war. Manchmal liefert sie Scheinbefunde (z. B. „fehlendes Inkrafttreten-Datum in v2“, obwohl Abschnitt 9 unverändert ist). Lehre: Auch die Nachprüfung im Original prüfen.
- Er **erfindet** Änderungen, z. B. wenn beide Dateien beim Einfügen nicht klar getrennt sind – dann mischt er die Fassungen. Auf „ALTE FASSUNG“ / „NEUE FASSUNG“ hinweisen.
- Er verwechselt alt und neu in der Tabelle.
- Bei der Info-Mail schmuggelt er Regeln hinein, die in keiner Fassung stehen.
- Bei der Info-Mail gehen Feinheiten verloren: „zusätzlich“ bei der Freigabe durch die Geschäftsführung (die Führungskraft genehmigt weiterhin), „einfache“ Bahnfahrt bei der Inlandsflug-Regel, „ohne Frühstück“, Erstattungsgrenze statt Hotelpreis. Aus „Trinkgeld-Regel gestrichen“ wird oft „Trinkgeld wird nicht mehr erstattet“, obwohl v2 dazu nur schweigt. „Per du“ an alle führt zu Mischformen aus du und ihr.

### Station C: Notizen → Protokoll und Aufgabentabelle

Material: [notizen_besprechung.txt](../07_Beispielmaterial/notizen_besprechung.txt)

#### Erwartete Aufgabentabelle (zum Abgleichen)

| Nr. | Was | Wer | Bis wann |
|---|---|---|---|
| 1 | Neue Flyer/Prospekte für Messe, Daten an Druckerei | Sabine K. | Ende nächster Woche – **unklar**, ob Do oder Fr (Feiertag?) |
| 2 | Herrn Brenner anrufen, Teillieferung 60 Stk. klären, **Liefertermin KW 22** weitergeben | Tom | bis Mittwoch |
| 3 | Prüfbericht LS-3015 lesen und für GF zusammenfassen | Fr. Yilmaz | bis zum nächsten Jour fixe (Datum offen) |
| 4 | Lieferantenliste aufräumen (Dubletten, alte Nummern) | Jonas | **widersprüchlich:** „irgendwann im Q3“ vs. Petras Wunsch „vor dem Lieferantenaudit“ (Mitte Juni? – unklar) |
| 5 | Bei Personal zur Reisekostenrichtlinie v2 nachfragen, kurze Info ans Team | Sabine K. | offen |
| 6 | Rechnung RE-2024-0815 (Frachtkosten, frei Haus?) mit Buchhaltung prüfen, ggf. Gutschrift | Petra W. | offen |
| 7 | Einarbeitungsplan für 2 Azubis | Tom | bis Monatsende |
| 8 | Technik nach Standpersonal für Messe fragen | Sabine K. | offen |

**Weitere Inhalte:**

- **Entscheidung offen:** Rabatt für Brenner – Petra: max. 5 %, nur mit GF-Freigabe; Diskussion ohne Ergebnis. (Zum Vergleich: Der Kunde fordert in der Mail 10 %.)
- **Standpersonal Messe:** Jonas und Fr. Yilmaz würden gehen – keine feste Entscheidung.
- **Erledigt, keine Aufgabe:** Kaffeemaschine 2. OG, Hausmeister informiert.
- **Nächster Termin:** in 2 Wochen, gleicher Raum (2.14), 9:30 Uhr. Datum der Besprechung selbst unklar („Di (?)“).
- **Teilnehmende:** Sabine K., Jonas (Protokoll), Fr. Yilmaz, Tom (später dazu), Petra W. (nur erste Hälfte).
- **Keine echten Beschlüsse:** In den Notizen stehen fast nur Zuständigkeiten. Wenn der Abschnitt „Entscheidungen“ bzw. „Beschlüsse“ Aufgaben enthält, ist das in Ordnung – und ein guter Übergang zur Aufgabentabelle.
- **Zusatzzeilen sind erwünscht:** Zeilen ohne Verantwortliche wie Rabatt-Entscheidung (GF) und Besetzung Standpersonal (wer fährt?) sind kein Erfinden, sondern das eigentliche Ziel der Mail-Bitte „fehlende Verantwortliche ergänzen“. Auch die Weitergabe von KW 22 als eigene Zeile mit „Bis wann: offen“ ist richtig – der Nachtrag nennt keine Frist. Der Rabatt als Zeile „offen | offen“ ist in Ordnung, solange er nicht als Beschluss erscheint.
- **Nach Termin sortiert** ergibt sich: Brenner (Mittwoch), Flyer (Ende nächster Woche), Prüfbericht (Jour fixe) / Einarbeitungsplan (Monatsende) – Reihenfolge dieser beiden unklar –, Lieferantenliste, dann die offenen.
- **Als „bereits erledigt“ akzeptabel** (Prüfprompt unten): neben der Kaffeemaschine auch „Messestand gebucht“ und „Prüfbericht liegt vor“, solange Flyer bzw. Lesen/Zusammenfassen als offene Aufgaben bleiben.

#### Die Fallen in den Notizen

- **NACHTRAG ganz unten:** Die Gehäuse kommen laut Fertigung doch schon **KW 22**, nicht KW 23. Ein gutes Protokoll übernimmt KW 22 bzw. weist auf die Korrektur hin. Manche Ergebnisse übernehmen KW 23 aus dem Hauptteil oder nennen beides ohne Hinweis. Häufiger im Test ist die Gegenrichtung (**Übervorsicht**): Das Modell wertet den NACHTRAG als Widerspruch („KW 22 oder 23? [UNKLAR]“) statt als Korrektur der Fertigung. Richtig ist KW 22.
- **Kaffeemaschine** landet oft als offene Aufgabe in der Tabelle, obwohl sie erledigt ist.
- **Relative Termine:** „nächste Woche“, „bis Mittwoch“, „in 2 Wo“ – der KI-Assistent rechnet manchmal ein konkretes Datum aus, obwohl das Besprechungsdatum gar nicht feststeht. Das ist erfunden.
- **Widerspruch bei Jonas' Aufgabe** (Q3 vs. vor dem Audit im Juni) wird gern zu einem Termin geglättet – oder „irgendwann im Q3“ wird ganz weggelassen.
- **Jour fixe geraten:** Der „nächste Jour fixe“ wird mit dem „nächsten Termin in 2 Wo“ gleichgesetzt – steht so nicht in den Notizen.
- **Fragen werden zu Aussagen:** Aus „hat den keiner gelesen?“ wird „offenbar hat ihn niemand gelesen“.
- **Rabatt** wird manchmal als „Entscheidung: 5 % Rabatt“ dargestellt – falsch, es gab kein Ergebnis.
- **Standpersonal** wird als feste Zusage von Jonas und Fr. Yilmaz dargestellt – war aber nur „würden gehen“.
- Kleinigkeit für Aufmerksame: Petra war nur in der ersten Hälfte da. Ob sie bei allen Punkten mit ihren Aufgaben noch im Raum war, geht aus den Notizen nicht hervor. Das ist kein Fehler, aber eine gute Rückfrage.

#### Musterprompts

Startprompts aus dem Übungsblatt. Zusätzlich gut für die Prüfung:

```
Lies die Notizen noch einmal bis zum Ende, auch den Nachtrag.
Gibt es Angaben, die sich widersprechen oder später korrigiert werden? Liste sie auf.
```

```
Welche Punkte in den Notizen sind bereits erledigt und gehören deshalb NICHT in eine Aufgabenliste?
```

#### Woran du ein gutes Ergebnis erkennst

- Alle 8 Aufgaben gefunden, keine erfundene, Kaffeemaschine nicht als offen.
- KW 22 korrekt, Unklarheiten mit [UNKLAR] oder „offen“ markiert statt geraten.
- Rabatt als offene Frage, nicht als Entscheidung.
- Für Schnelle – Checkliste: dieselben 8 Aufgaben wie in der Tabelle. Erledigtes als [x] ist in Ordnung. Achten auf zugeschobene Zusatzpunkte (Rabatt, Standpersonal „bestätigen“) und darauf, ob der KW-22-Nachtrag als Korrektur übernommen wird und nicht als „Widerspruch klären“.
- Für Schnelle – Punkte ohne Verantwortliche: Rabatt Brenner (wer holt GF-Freigabe?), Standpersonal Messe (wer legt verbindlich fest?), Protokollführung („keiner so richtig“). Sinnvoll zusätzlich: Audit-Termin bzw. wer über die Frist der Lieferantenliste entscheidet, Druckerei-Termin Do/Fr. Bonus: Waren Petras Punkte noch in ihrer Anwesenheit dran? Fehler: Aufgaben mit genannter Person als „ohne Verantwortlichen“; KW 22 vs. KW 23 als offen; erledigte Kaffeemaschine. Modelle mischen oft „ohne Person“ und „ohne Termin“ – gute Diskussionsfrage.
- Für Schnelle – Tagesordnung: Enthält Rabatt Brenner, Standpersonal Messe, Flyer/Druckerei-Termin, Brenner-Lieferung (KW 22 laut Nachtrag, Teillieferung 60 Stk.), Zusammenfassung Prüfbericht LS-3015, Lieferantenliste/Audittermin, Reisekostenrichtlinie v2, Rechnung RE-2024-0815; Rahmen „in 2 Wochen, Raum 2.14, 9:30“ ohne ausgerechnetes Datum; Kaffeemaschine nicht als TOP. Zeitangaben je TOP nachrechnen (Summe stimmt oft nicht).

### Station D: Lieferantenliste bereinigen

Material: [lieferantenliste_unsortiert.csv](../07_Beispielmaterial/lieferantenliste_unsortiert.csv) – Trennzeichen Semikolon, Spalten: Lieferant; Ansprechpartner; Ort; Telefon; E-Mail; Warengruppe; Letzte Bestellung; Jahresumsatz EUR; Bewertung.

#### Eckdaten zum Abgleichen

- **27 Datenzeilen** (plus Kopfzeile).
- **4 Dubletten-Paare** → nach Bereinigung **23 Lieferanten**:

| Dublette | Zeilen (ohne Kopfzeile) | Abweichungen innerhalb des Paars |
|---|---|---|
| Müller Stahlhandel GmbH / Mueller Stahlhandel | 1 und 7 (in der Datei: 2 und 8) | Schreibweise ü/ue, Rechtsform, Telefon mit Bindestrich, Datumsformat, Betrag 48.500,00 vs. 48500 – inhaltlich gleich |
| Schmidt & Söhne KG / Schmidt und Söhne KG | 2 und 10 (3 und 11) | „&“ vs. „und“, Ort klein geschrieben, Warengruppe „Schrauben/Normteile“ vs. „Normteile“, Anrede |
| Elektro Krause / ELEKTRO KRAUSE GmbH | 3 und 14 (4 und 15) | Großschreibung, Rechtsform, Ortsschreibweise, Warengruppe „Elektrokomponenten“ vs. „Elektro“, Datum 5.1.24 vs. 05.01.2024, Betrag „31 200 €“ vs. „31.200,00“ |
| Weber Kunststofftechnik / Weber Kunststoff-Technik GmbH | 4 und 18 (5 und 19) | Bindestrich, Rechtsform, Warengruppe, **Datum widersprüchlich:** „März 2024“ vs. „2024-03-01“ (vereinbar, aber nicht eindeutig) |

KI-Assistenten und Editoren zählen meist die Kopfzeile als Zeile 1 mit (Dateizeilen) – beide Zählweisen sind richtig, wenn sie einheitlich sind.

- **Keine Dubletten** (falsche Treffer, auf die man achten sollte): Keller Dichtungstechnik und Krüger Gummiwaren (beide „Dichtungen“), Hoffmann Logistik und Braun Transporte (beide „Spedition“), Elektro Krause / Fischer Kabelkonfektion / Koch Elektronik (gleiche Gegend, ähnliche Warengruppe).

#### Typische Datenprobleme in der Datei

- **Datumsformate:** 12.03.2024 · 2024-02-28 · 5.1.24 · 7.4.2024 · 15/01/2024 · 03/02/2024 · „März 2024“ · „Dez. 2023“ · „April 2024“ · leer (Keller).
  - **Mehrdeutig:** „03/02/2024“ (Braun Transporte) kann 3. Februar oder 2. März heißen. Ein gutes Ergebnis markiert das, statt still eines zu wählen.
  - **Unvollständig:** „März 2024“, „Dez. 2023“, „April 2024“ – ein Tag lässt sich nicht ableiten. Erfindet der KI-Assistent „01.03.2024“, ist das eine Annahme, die markiert sein muss.
- **Beträge:** 48.500,00 · 48500 · 12.300 · 12300,00 · 31 200 € · 31.200,00 · 22.750,50 · 22750,5 · 9800 · 18.400,00 € · 63.200 € · 41.000 EUR · 11.300 EUR · 3.150,75 · „n/a“ (Richter) · leer (Koch). Achtung: „12.300“ heißt hier zwölftausenddreihundert, nicht zwölf Komma drei – Punkt als Tausendertrenner ist eine typische Fehlerquelle.
- **Orte:** musterhausen / MUSTERHAUSEN / Musterhausen; fiktivhausen; „Neustadt a. d. Probe“ / „Neustadt a.d. Probe“ / „Neustadt an der Probe“ / „neustadt a. d. probe“.
- **Fehlende Werte:** Ansprechpartner (Lackierwerk Ost, Schwarz Gießerei), Telefon (Becker Werkzeugbau), E-Mail (Hoffmann Logistik, Krüger Gummiwaren), Datum (Keller), Umsatz (Richter „n/a“, Koch leer), Bewertung (Bauer, Keller).
- **Bewertung uneinheitlich:** „a“ (Wolf) und „b“ (Schäfer) klein geschrieben.
- **Anreden uneinheitlich:** Herr / Hr. / Frau / ohne Anrede / mit und ohne Vorname, „Dr.“ an verschiedenen Stellen.
- **Warengruppen uneinheitlich:** Elektrokomponenten / Elektro / Elektronik; Kunststoffteile / Kunststoff; Schrauben/Normteile / Normteile.
- **Telefon:** „0000-111201“ vs. „0000 111201“.

**Kontrollwert für Schnelle (falls jemand die Summe der Jahresumsätze bildet):** Nach Entfernen der Dubletten ergeben die 21 vorhandenen Beträge **461.001,25 €** (Richter und Koch ohne Wert). Mit Dubletten käme man fälschlich auf 575.751,75 €. Weicht die KI-Summe ab: wunderbarer Moment, um zu zeigen, dass man Rechnungen besser Excel überlässt. Stimmt sie (im Testlauf bei allen drei Modellen der Fall): fragen, woher man das weiß – nur wer die Einzelwerte sieht und in Excel nachrechnet, kann es sagen. Typischer Lesefehler: „12.300“ als 12,30 € gelesen ergibt 448.713,55 €.

#### Musterprompts

Startprompts aus dem Übungsblatt. Zusätzlich hilfreich:

```
Zähle die Zeilen noch einmal einzeln durch und nummeriere sie. Stimmt deine erste Angabe?
```

```
Liste alle Stellen auf, an denen du beim Bereinigen eine Annahme getroffen hast
(z. B. ein Datum ergänzt oder ein Format gedeutet). Was davon sollte ich prüfen?
```

#### Woran du ein gutes Ergebnis erkennst

- Zeilenzahl 27 → 23, die vier richtigen Paare zusammengeführt, keine falschen.
- Fehlende Werte als „FEHLT“ markiert, nicht erfunden; mehrdeutige Daten in der Spalte „Hinweis“.
- Beträge einheitlich und **wertgleich** zum Original (Stichprobe!).
- Die Teilnehmenden haben selbst gezählt und mindestens drei Zeilen verglichen.
- Weber: 01.03.2024 aus der Dublette übernommen ist ok, wenn „März 2024“ im Hinweis steht.
- Annahmen-Prompt: Die Liste nennt mindestens 03/02/2024, 01.03.2024 bei Weber, die Nur-Monat-Daten, 5.1.24, 15/01/2024, 12.300, 31 200 €, n/a, die Rechtsform GmbH (Müller, Krause, Weber) und die gewählte Schreibweise bei Warengruppen und Anreden. Fehlt etwas: mit der Spalte „Hinweis“ abgleichen – auch die Annahmenliste kann unvollständig oder falsch sein.

#### Typische Stolpersteine (Station D)

- **Zeilen verschwinden** bei der Ausgabe, besonders bei längeren Tabellen – oder die Ausgabe bricht ab („… weitere Zeilen“). Lösung: „Gib die vollständige Tabelle ohne Auslassungen aus“ oder in zwei Teilen ausgeben lassen.
- **Falsche Zählung:** Der KI-Assistent behauptet z. B. 26 oder 28 Zeilen. Sprachmodelle zählen unzuverlässig – Brücke zur Demo aus Block 1. Bei aktuellen Modellen ist die Zählung bei dieser Listengröße oft richtig; dann zeigen: Der Prüfschritt hat es bestätigt – bei 500 Zeilen wäre das nicht sicher.
- **Zeilennummern mit/ohne Kopfzeile:** Manche Modelle nennen Datei-Zeilen (Müller = Zeile 2, wie im Texteditor), andere Datenzeilen (Müller = Zeile 1) – teils gemischt in einer Antwort. Nachfragen: „Zählst du mit oder ohne Kopfzeile? Bitte einheitlich.“ Achtung beim Prüfschritt: Die CSV endet mit einem Zeilenumbruch, Strg + Ende landet deshalb in einer leeren Zeile 29.
- **Falsche Spaltenzuordnung:** z. B. „n/a“ bei Richter als fehlendes Datum statt als fehlender Umsatz. Stichproben auf Spaltenebene machen.
- **Umformatieren verändert still:** Beim „noch einmal als CSV“ können Hinweise gekürzt werden oder wegfallen – Zeilenzahl und zwei Hinweis-Zellen gegen die Tabelle prüfen.
- **Stille Annahmen:** Datum „März 2024“ wird zu „01.03.2024“ ohne Hinweis; „03/02/2024“ wird ohne Kommentar gedeutet.
- **Beträge verfälscht:** „12.300“ wird zu 12,30 €; „22750,5“ zu 2.275.050.
- **Excel-Falle:** Wer die CSV in Excel öffnet und dann kopiert, hat evtl. schon von Excel veränderte Datumsangaben.
- **Excel-Anleitung (Für Schnelle):** „Duplikate entfernen“ nur über E-Mail löscht auch Krüger Gummiwaren, weil Hoffmann und Krüger beide eine leere E-Mail haben (Ergebnis 22 statt 23 – einmal in Excel nachstellen). Über E-Mail + Telefon wird Müller/Mueller nur gefunden, wenn vorher „0000-111201“ zu „0000 111201“ vereinheitlicht wurde. Im Test versprachen alle drei Modelle trotzdem „4 Treffer“. Gute Anleitungen: Import über Daten → Aus Text/CSV (Semikolon, UTF-8, kein Doppelklick), erst bedingte Formatierung „Doppelte Werte“, dann gezielt löschen.
- **Fehlende Spalten (Für Schnelle):** Erwartbar sind Lieferanten-/Kreditorennummer, Straße/PLZ/Land, USt-IdNr., Zahlungs- und Lieferbedingungen, Status, Zertifizierungen mit Gültigkeit, Bewertungsdatum/-kriterien, Bezugsjahr Jahresumsatz – oft 20+ Vorschläge, also nachfragen: „Welche 5 würdest du wirklich einführen?“ Achte darauf, ob Bankverbindung und Kontaktdaten mit einem Hinweis auf Vertraulichkeit/DSGVO kommen; falls nicht, guter Anlass für die Daten-Ampel.
- **Pflegeanleitung (Für Schnelle):** Gut sind TT.MM.JJJJ, offizieller Name mit Rechtsform, „&/und“ wie im offiziellen Namen, feste Liste für Warengruppen (und Orte), Betrag als Zahl ohne Währung, Bewertung als Großbuchstabe (in der Datei A–C), kein „n/a“, Pflichtfelder, Dublettenprüfung vor Neuanlage. Typische Schwächen: Widersprüche zwischen den Regeln (Pflichtfeld gegen „unbekannt bleibt leer“), Vorbelegungen wie „B“ oder 0, „Elektronik“ fällt beim Vereinheitlichen still weg, die KI legt Normformen selbst fest, statt nachzufragen.

### Allgemein für Übung 3

**Stolpersteine bei allen Stationen:**

- Upload klappt nicht oder Datei wird nur teilweise gelesen → Kopieren & Einfügen. Bei sehr langen Texten nachfragen: „Wie lauten die letzten zwei Zeilen des Dokuments, wörtlich?“ – und die Antwort mit dem Original vergleichen (Datei im Editor öffnen, Strg + Ende). Beim Prüfbericht endet das Dokument mit „… von der Schlusszahlung zu vereinbaren.“ und der Unterschrift „Frank Albers, Fertigungstechnik“. Achtung: „Ich habe alles gelesen“ sagen Modelle auch bei abgeschnittenem Text.
- Teilnehmende überspringen den Prüfschritt. Gezielt fragen: „Welche drei Aussagen hast du im Original gefunden?“
- Jemand möchte lieber ein echtes Firmendokument nehmen → Daten-Ampel prüfen, im Zweifel auf Übung 4 verschieben und anonymisieren.

**Hilfen für Langsame:**

- Station C empfehlen – sie ist am anschaulichsten und am schnellsten zu prüfen.
- Nur die Stufe „Basis“ und den Prüfschritt machen.
- Bei Upload-Problemen: Ausschnitt nehmen (z. B. nur Abschnitt 7 des Prüfberichts).

**Zusatzaufgaben für Schnelle:**

- Aufgaben „Für Schnelle“ auf dem Übungsblatt, oder eine zweite Station.
- Station A + C kombinieren: „Schreib Fr. Yilmaz' Zusammenfassung für den Jour fixe“ (Aufgabe 3 aus den Notizen) – verbindet beide Materialien. Beide Dateien ins selbe Gespräch geben. Gutes Ergebnis: Abnahme unter Vorbehalt mit den drei Bedingungen, Einbehalt 5 %, Schlusszahlung 30 %, offene Punkte wie in Station A. Kein Eurobetrag und kein ausgerechnetes Jour-fixe-Datum. Typisch: übernimmt „alle Maße in Toleranz“ (Schlitzbreite!) und wird trotz „kurz“ etwa eine Seite lang. Nachsteuern mit „höchstens 10 Zeilen“ und der Prüffrage zur Messwerttabelle.
- Station D: „Erstelle eine Excel-Anleitung, wie ich Dubletten selbst finde“ und ausprobieren.

---

## Übung 4: Eigene Aufgabe

Übungsblatt: [Uebung_4_Eigene_Aufgabe.md](Uebung_4_Eigene_Aufgabe.md)

### Deine Rolle in diesem Block

Du gehst herum – das ist der wertvollste Teil des Tutorials. Plane pro Team ca. 2–3 Minuten ein. Hab die Antworten aus der Vorab-Umfrage (siehe [Einladung und Vorbereitung](../02_Einladung_und_Vorbereitung.md)) griffbereit, damit du weißt, wer welche Aufgabe mitbringt.

**Reihenfolge beim Herumgehen:**

1. Zuerst zu Teams, die noch nicht tippen (Startprobleme).
2. Dann Daten-Ampel-Check: Was wird gerade eingegeben?
3. Dann Qualität: Ergebnis gemeinsam kritisch lesen.
4. Ab 2:43 gezielt 2–3 Teams für die Vorstellung in Block 7 ansprechen – möglichst unterschiedliche Rollen und mindestens ein Team, bei dem es **nicht** geklappt hat.

### Musterprompts für häufige Aufgaben

**Wiederkehrende Standardantwort (Verwaltung, Vertrieb):**

```
Du bist Sachbearbeiterin in der Verwaltung eines [ART DES UNTERNEHMENS].
Wir bekommen immer wieder Anfragen dieser Art: [ART DER ANFRAGE, ANONYMISIERT].
Bei uns gilt: [REGELN, FRISTEN, ZUSTÄNDIGKEITEN].
Die Antwort geht an: [EMPFÄNGER], unterschrieben von [NAME/ABTEILUNG].
Erfinde keine Regeln. Wenn etwas nicht geregelt ist, markiere es mit [KLÄREN: …].
Schreib mir eine Antwortvorlage, die ich jedes Mal anpassen kann.
Format: max. 100 Wörter, Sie-Form, Platzhalter in eckigen Klammern für alles, was sich ändert.
Stell mir zuerst bis zu 3 Rückfragen, wenn dir etwas fehlt.
```

**Excel-Hilfe (Buchhaltung, Einkauf):**

```
Ich habe in Excel eine Tabelle mit den Spalten A: [SPALTE], B: [SPALTE], C: [SPALTE].
Ich möchte in Spalte D [WAS SOLL BERECHNET/GEPRÜFT WERDEN].
Gib mir die Formel für die deutsche Excel-Version und erkläre sie Schritt für Schritt.
Nenne auch, was schiefgehen kann.
```

**Anleitung / Checkliste (Technik, Service, Personal):**

```
Du bist erfahrener Servicetechniker.
Hier sind meine Stichpunkte zu einem Ablauf, den neue Kolleginnen und Kollegen lernen müssen:
[STICHPUNKTE, OHNE KONSTRUKTIONSDETAILS]
Mach daraus eine nummerierte Schritt-für-Schritt-Anleitung in einfacher Sprache
und am Ende eine Checkliste zum Abhaken.
```

**Nachfass-Mail nach Messe/Termin (Vertrieb):**

```
Du bist erfahrener Vertriebsmitarbeiter im Außendienst.
Kontext: Auf der Messe [MESSE] habe ich mit [KUNDE] über [PRODUKT] gesprochen.
Der Kunde braucht [ANFORDERUNG, z. B. Schutzart], Bedarf ca. [MENGE] pro Jahr.
Aufgabe: Schreib eine Nachfass-Mail. Datenblätter hängen an, Angebot folgt bis [FRIST].
Format: max. 150 Wörter, Betreff, per Sie, keine Werbefloskeln, keine Preise,
Platzhalter für Anrede, Name und zwei Terminvorschläge.
Erfinde keine Produkteigenschaften und keine Gesprächsinhalte.
Stell mir zuerst Rückfragen.
```

Varianten Satz für Satz auf unterstellte Gesprächsinhalte und Produkteigenschaften prüfen.

**Mahnung Lieferverzug (Einkauf):**

```
Du bist Einkäuferin bei einem technischen Hersteller.
Kontext: Lieferant [X] hat Bestellung [BESTELLNUMMER] über [MENGE] [TEIL]
schon zweimal verschoben, zuletzt auf [KW]. Wir brauchen die Ware bis [DATUM] im Wareneingang.
Aufgabe: Schreib eine Mahnung mit der Bitte um einen verbindlichen Termin bis [FRIST].
Format: max. 80 Wörter, Betreff, Sie-Form, freundlich, aber bestimmt.
Stell mir zuerst Rückfragen.
```

Erwartung: versandfähiger Entwurf mit Platzhaltern. Typische Schwächen: „maximal die Hälfte“ wird nicht eingehalten, Fakten gehen beim Kürzen verloren, Wortzahl-Angaben der KI stimmen nicht.

**Statusbericht (Projektleitung):** siehe Beispielprompt bei Übung 2 oben.

### Woran du ein gutes Ergebnis erkennst

- Die Aufgabe ist konkret und wiederkehrend (nicht „mach meinen Job“).
- Daten-Ampel wurde **vor** dem ersten Prompt geprüft; echte Namen, Preise, Personaldaten sind ersetzt.
- Mindestens zwei Iterationsschritte.
- Das Bewertungsraster ist ehrlich ausgefüllt, auch mit „lohnt sich nicht“.
- Ein Prompt ist gespeichert.
- Bei Vorlagen: Jede Zusage (Frist, Zahlungstermin) ist gegen die echte Firmenregel geprüft. Es ist klar, welche Fälle die Vorlage **nicht** abdeckt (z. B. bereits überfällige Rechnung).

### Typische Stolpersteine

- **Keine Aufgabe dabei / Blockade:** Ideenliste nach Rollen auf dem Übungsblatt zeigen; nach der Vorab-Umfrage fragen; oder fragen: „Was hast du letzte Woche gemacht, das dich genervt hat?“ – oder den Ideen-Prompt von Folie 21 nutzen lassen, danach gemeinsam eine Idee mit grünen Daten auswählen. Achtung: Die Ideenlisten fordern teils selbst dazu auf, Preise oder Bestellungen einzufügen.
- **Aufgabe zu groß** („Unser ganzes Angebotswesen automatisieren“): auf einen Teilschritt herunterbrechen („Nur das Anschreiben zum Angebot“).
- **Aufgabe braucht rote Daten** (Personalakten, Kundenverträge, Zeichnungen): nicht verbieten und weitergehen, sondern Alternative zeigen – mit erfundenen Beispieldaten arbeiten, nur die Struktur beschreiben oder eine Vorlage statt eines fertigen Dokuments erzeugen. Unklare Fälle notieren und an [DATENSCHUTZBEAUFTRAGTE/R] bzw. [ANSPRECHPARTNER IT] weitergeben – nicht selbst rechtlich bewerten.
- **Aufgabe braucht Firmenwissen** (interne Abläufe, Preise, Systeme): Der KI-Assistent kennt die Firma nicht. Entweder Kontext mitgeben (Ampel beachten) oder akzeptieren, dass nur ein Entwurf herauskommt.
- **Enttäuschung:** „Das Ergebnis ist schlecht.“ Gemeinsam schauen: Fehlt Kontext? Fehlt das Format? Wenn es trotzdem nicht klappt: Das ist ein gültiges Ergebnis – manche Aufgaben eignen sich nicht. Ermutigen, das in Block 7 zu erzählen.
- **Ein Teampartner dominiert:** Rollen tauschen lassen – „Jetzt tippst du, und er prüft.“

### Hilfen für Langsame

- Eine Aufgabe aus der Ideenliste vorschlagen, die zur Rolle passt und nur grüne Daten braucht (z. B. Rundmail, Checkliste, Anleitung).
- Die Vorlage aus Schritt 3 gemeinsam ausfüllen – du diktierst die Fragen, die Person antwortet, der Teampartner tippt.
- Ziel herunterschrauben: „Ein brauchbarer Entwurf reicht.“

### Zusatzaufgaben für Schnelle

- Zweite Aufgabe aus der Ideenliste bearbeiten.
- Den gespeicherten Prompt vom KI-Assistenten verbessern lassen (wie Übung 2, Aufgabe F) und mit dem Teampartner tauschen: Funktioniert der Prompt auch bei jemand anderem?
- Eine kurze Anleitung für Kolleginnen und Kollegen schreiben: „So nutze ich KI für [AUFGABE]“ – geeignet für den [TIPPS-KANAL] (siehe [Nachbereitung](../08_Nachbereitung.md)).

---

## Allgemeine Hilfen beim Herumgehen

**Fragen, die fast immer weiterhelfen:**

- „Was genau willst du am Ende in der Hand haben?“
- „Was weißt du, das der KI-Assistent nicht weiß?“
- „Wie würdest du das einer neuen Kollegin erklären?“
- „Woher weißt du, dass das stimmt?“
- „Darfst du das eingeben? Was sagt die Ampel?“

**Rettungssätze für Prompts, die hängen:**

```
Stell mir zuerst 3 Fragen, bevor du antwortest.
```

```
Erfinde nichts. Wenn du etwas nicht weißt, schreib "unbekannt".
```

```
Das ist zu lang / zu allgemein. Mach es konkreter für [ZIELGRUPPE] und höchstens [LÄNGE].
```

**Technikprobleme:** Siehe Backup-Plan im Abschnitt [Troubleshooting im Trainer-Leitfaden](../01_Trainer-Leitfaden.md#6-troubleshooting) (Reserve-Logins, Beamer-Demo, Screenshots). Bei Upload-Problemen: Kopieren & Einfügen. Bei Login-Problemen: Person setzt sich zum Teampartner, beide arbeiten an einem Gerät.

**Haltung:** Fehler des KI-Assistenten sind keine Panne, sondern Lernstoff. Wer einen Fehler gefunden hat, hat die Übung verstanden.

---

Zurück zur [Übersicht](../README.md) · [Trainer-Leitfaden](../01_Trainer-Leitfaden.md) · [Daten-Ampel](../03_Daten-Ampel.md)
