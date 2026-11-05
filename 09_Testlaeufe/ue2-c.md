# Testlauf: Übung 2 / Weiter C – „Stell mir zuerst 3 Fragen“

**Herkunft:** [Übung 2, Aufgabe C – „Stell mir zuerst 3 Fragen“](../06_Uebungen/Uebung_2_Gute_Prompts.md#aufgabe-c--stell-mir-zuerst-3-fragen). Lösungshinweise: [Trainer-Loesungshinweise.md – Übung 2](../06_Uebungen/Trainer-Loesungshinweise.md#übung-2-gute-prompts) („Woran du ein gutes Ergebnis erkennst“, Punkt Aufgabe C; „Typische Stolpersteine“, Punkt „Bei C antwortet die KI sofort mit einem Plan“). Neuer Chat, ohne Vorlauf. Anhänge: keine.

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt (Turn 1, neuer Chat):**

```text
Ich möchte einen Einarbeitungsplan für einen neuen Kollegen im Lager
unseres kleinen Technikbetriebs erstellen.

Bevor du anfängst: Stell mir zuerst 3 Fragen, die du brauchst, um einen
wirklich passenden Plan zu schreiben. Warte auf meine Antworten.
```

**Turn 2 (fiktive Antworten, für alle Modelle gleich):** Drei Jahre Erfahrung im Logistikzentrum, kennt Handscanner und eine Lagerverwaltungssoftware, aber nicht „unser System“; Staplerschein vorhanden; Sicherheitsunterweisung und Hochregal-Einweisung fehlen noch; Ansprechperson [NAME TEAMLEITUNG], Pate [NAME KOLLEGE LAGER]; Mo–Fr 7–15:30 Uhr; Start Montag.

**Ziel laut Material:** Der KI-Assistent stellt wirklich (genau) 3 sinnvolle Fragen und wartet. Nach den Antworten entsteht ein Plan, der die Antworten aufgreift (Staplerschein vorhanden, Sicherheitsunterweisung und Hochregal noch offen, Pate, 7–15:30 Uhr) und Platzhalter statt erfundener Namen verwendet.

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Turn 1: genau 3 nummerierte Fragen | ja | ja | ja |
| Turn 1: kein Plan, wartet auf Antworten | ja | ja | ja |
| „Stopp, bitte erst die Fragen.“ nötig | nein | nein | nein |
| Fragen sind Sammelfragen (Teilfragen je Nummer, grob gezählt) | ja, ca. 8 Teilfragen (Frage 3 allein: 4) | ja, ca. 7 (Fragen + Aufzählung, was gebraucht wird) | ja, ca. 9 (9 Fragezeichen) |
| Deckt typische Fragen ab: Vorerfahrung / Systeme | ja | ja | ja |
| … Stapler / Sicherheitsunterweisungen | ja (inkl. Hochregal, Gefahrstoffe) | ja (inkl. Brandschutz, Erste Hilfe, Hochregal) | ja (inkl. Brandschutz, Gefahrstoffe) |
| … Ansprechperson / Pate / Arbeitszeit / Start | ja | ja | ja |
| Begründet, wozu die Frage dient | kaum | ja („Davon hängt ab, wie tief ich … anfange“) | teilweise |
| Anrede (Nutzer duzt) | du/euch | Sie | Sie |
| Turn 2: Erfahrung berücksichtigt (keine Lagergrundlagen) | ja | ja, ausdrücklich | ja, ausdrücklich |
| … Staplerschein vorhanden aufgegriffen | ja (nur „Kopie in den Personalordner“) | ja, plus Stapler-Einweisung im Betrieb und „Betriebserlaubnis vom Arbeitgeber“ | ja, plus Stapler-Einweisung und **schriftliche Beauftragung** |
| … Sicherheitsunterweisung am Montag, dokumentiert | ja | ja | ja |
| … Hochregal-Einweisung, erst danach selbstständig | ja (Mi) | ja (Mi) | ja (Di) |
| … Pate eingeplant | ja | ja | ja |
| … Arbeitszeit 7–15:30 Uhr eingehalten | ja | ja | ja (Zeitblöcke lückenlos 7:00–15:30) |
| … Mittagspause eingeplant | nur Mittwoch | ja, jeden Tag (45 Min.) | ja, jeden Tag (30 Min.) |
| Platzhalter statt erfundener Namen | ja | ja | ja (zusätzlich [NAME NEUER KOLLEGE], [DATUM]) |
| Annahmen gekennzeichnet | nein | ja („nach Annahme eingesetzt“) | ja („z. B.“, „falls vorhanden“, Tipps zur Anpassung) |
| Hinweis auf Fachkraft für Arbeitssicherheit / BG | nein | ja | ja |
| Länge Turn 2 | ca. 1 Seite, Stichpunkte | ca. 2–3 Seiten, 5 Tabellen | ca. 3 Seiten, 5 Tabellen + Feedbackfragen |
| **Gesamt** | **gut** – Übung funktioniert, Plan solide, aber Stapler-Einweisung fehlt | **sehr gut** | **sehr gut**, fachlich am genauesten |

## Gefundene Fehler mit Beleg

**Verhalten in Turn 1: keine Abweichung.** Alle drei Modelle stellen genau drei nummerierte Fragen, liefern keinen Plan und kündigen an, auf die Antworten zu warten. Der in den Lösungshinweisen genannte Stolperstein („Bei C antwortet die KI sofort mit einem Plan“) trat **bei keinem Modell** auf; der Folgeprompt „Stopp, bitte erst die Fragen.“ war nicht nötig.

**Erfundene Fakten oder falsche Zahlen: keine.** Die Angaben aus Turn 2 (3 Jahre Erfahrung, Staplerschein, Sicherheitsunterweisung, Hochregal, beide Platzhalter, Mo–Fr 7–15:30 Uhr, Start Montag) werden von allen drei Modellen korrekt übernommen. Alle Zeitangaben liegen zwischen 7:00 und 15:30 Uhr. Bei Opus sind die Zeitblöcke an allen fünf Tagen lückenlos und überschneidungsfrei (nachgeprüft). Arbeitszeit 8,5 Std. brutto: mit 30 Min. Pause (Opus) 8 Std., mit 45 Min. Pause (Sonnet) 7,75 Std. – beides vereinbar mit der Pausenregel des Arbeitszeitgesetzes (§ 4: ab 6 Std. mindestens 30 Min.).

Beobachtungen, die man kennen sollte:

1. **„3 Fragen“ werden zu Sammelfragen (alle Modelle).** Jede Nummer bündelt mehrere Teilfragen. Haiku Frage 3: „Wer ist die Ansprechperson …, wer begleitet ihn praktisch als Pate, welche Arbeitszeiten gelten, und an welchem Wochentag beginnt er?“ – das sind vier Fragen unter einer Nummer. Opus stellt insgesamt neun Fragen mit Fragezeichen. Formal ist der Auftrag erfüllt, inhaltlich fragt die KI eher 7–9 Dinge ab. Das ist sinnvoll, macht das Beantworten aber länger, als „3 Fragen“ vermuten lässt.
2. **Haiku: betriebliche Stapler-Einweisung und Beauftragung fehlen.** Haiku greift den Staplerschein nur über „Staplerschein-Kopie und Unterlagen im Personalordner“ auf und lässt den Kollegen am Donnerstag „ganztägig“ im laufenden Betrieb mitarbeiten, ohne Einweisung in die betriebseigenen Stapler. Sonnet („Staplereinweisung im Betrieb … Staplerschein und Betriebserlaubnis vom Arbeitgeber prüfen und dokumentieren“) und Opus („Ein Staplerschein allein reicht nicht. Der Arbeitgeber muss ihn **schriftlich beauftragen** …“) nennen den Punkt. Opus' Aussage stimmt mit der DGUV Vorschrift 68 überein (Flurförderzeuge: Fahren nur mit schriftlicher Beauftragung durch den Unternehmer). Sonnets Begriff „Betriebserlaubnis“ ist unüblich (gemeint ist der Fahrauftrag bzw. die Beauftragung), in der Sache aber richtig.
3. **Haiku: Kleinigkeiten.** Eine Mittagspause steht nur am Mittwoch; am Freitag liegt „Gemeinsame Auswertung der Woche“ auf „Mittag“. „Praktische Einweisung am Hochregal-Bediengerät bzw. am Regal“ unterstellt ein Regalbediengerät, das der Nutzer nicht erwähnt hat (das „bzw.“ schwächt es ab). Die Perspektive wechselt („die Sicherheitsunterweisung bei euch“ und im nächsten Satz „Unser System“).
4. **Sonnet: uneinheitliche Verantwortlich-Spalte.** Mal „[NAME KOLLEGE LAGER]“, mal „Pate“. Die Hochregal-Einweisung liegt bei „[NAME TEAMLEITUNG] bzw. dafür Befugte“, obwohl der Nutzer das nicht festgelegt hat. Sonnet weist darauf aber selbst hin („Die Pausenzeiten, die Verantwortlichen für die Hochregal-Einweisung … habe ich nach Annahme eingesetzt“).
5. **Opus: Annahmen über den Betrieb**, z. B. „ESD-Schutz, Seriennummern“ und Gespräche mit „Einkauf, Vertrieb/Auftragsannahme, Technik/Werkstatt“. Diese stehen als „z. B.“ da und passen zu einem Technikbetrieb, sind aber nicht aus den Antworten abgeleitet.
6. **Anrede:** Der Nutzer duzt. Haiku duzt zurück, Sonnet und Opus siezen. Das ist kein Fehler, aber ein Beispiel dafür, dass ohne Vorgabe jedes Tool seinen eigenen Ton wählt.

## Lehren für die Auswertung

- **Die Technik funktioniert zuverlässig.** Bei allen drei Modellen kamen genau 3 Fragen und kein vorschneller Plan. Den Stolperstein „KI legt sofort los“ kann man erwähnen, sollte ihn aber nicht als Regelfall ankündigen. Bei anderen Tools oder älteren Versionen kann er trotzdem auftreten.
- **Die Fragen sind fast identisch** (Vorerfahrung, Nachweise/Unterweisungen, Rahmen mit Ansprechperson, Pate, Zeiten, Start). Gute Auswertungsfrage dazu: „Hättet ihr selbst an den Staplerschein und die Hochregal-Einweisung gedacht?“ So sieht man, was die Technik leistet: Die KI bringt die Checkliste mit, der Mensch liefert die Fakten.
- **Sammelfragen zeigen:** „3 Fragen“ heißt für die KI eher „3 Themen“. Wer kurz antworten will, kann schreiben: „Stell mir genau 3 kurze Einzelfragen, nacheinander, und warte jeweils.“ Das ist gut als Variante für Schnelle.
- **Antworten wirken sich sichtbar aus.** Alle Pläne übernehmen „hat Erfahrung“, also Fokus auf „unser System“ statt Grundlagen, und setzen Sicherheitsunterweisung und Hochregal vor das selbstständige Arbeiten. Gut zum Zeigen: Vergleich mit dem Minimal-Prompt aus Aufgabe A.
- **Fachliche Tiefe unterscheidet sich.** Nur Sonnet und Opus erkennen, dass ein Staplerschein ohne betriebliche Einweisung und Beauftragung nicht reicht. Lehre: Auch ein guter Plan muss von jemandem mit Fachwissen geprüft werden. Sonnet und Opus empfehlen das selbst (Fachkraft für Arbeitssicherheit/BG).
- **Länge:** Sonnet und Opus liefern 2–3 Seiten. In den 5 Minuten Richtzeit (Fragen beantworten und Plan lesen) wird das knapp. Wer Zeit sparen will, ergänzt in Turn 2 „höchstens eine Seite“ – oder geht direkt zu Aufgabe D („Kürzer bitte …“).

---

## Gesprächsprotokoll: Haiku

### Nutzer 1

```text
Ich möchte einen Einarbeitungsplan für einen neuen Kollegen im Lager
unseres kleinen Technikbetriebs erstellen.

Bevor du anfängst: Stell mir zuerst 3 Fragen, die du brauchst, um einen
wirklich passenden Plan zu schreiben. Warte auf meine Antworten.
```

### Assistent 1

Gerne. Damit der Plan wirklich zu eurem Lager und zu dem neuen Kollegen passt, brauche ich noch drei Informationen:

1. **Vorkenntnisse:** Welche Erfahrung bringt er mit (z. B. Lagerarbeit, Staplerfahren, Handscanner, Lagerverwaltungssoftware), und welche davon ist in eurem Betrieb neu?
2. **Pflichtunterweisungen und Qualifikationen:** Hat er bereits einen Staplerschein, und welche Sicherheitsunterweisungen oder hausinternen Einweisungen (z. B. Regalbediengerät, Hochregal, Gefahrstoffe) muss er bei euch noch absolvieren?
3. **Rahmen:** Wer ist die Ansprechperson für die Einarbeitung, wer begleitet ihn praktisch als Pate, welche Arbeitszeiten gelten, und an welchem Wochentag beginnt er?

Sobald ich deine Antworten habe, erstelle ich den Plan für die erste Woche.

### Nutzer 2

```text
Hier meine Antworten:
1. Er hat drei Jahre Erfahrung in einem Logistikzentrum, kennt Handscanner und eine Lagerverwaltungssoftware, aber nicht unser System.
2. Einen Staplerschein hat er, die Sicherheitsunterweisung bei uns und die Einweisung in unser Hochregal braucht er noch.
3. Ansprechperson ist [NAME TEAMLEITUNG], als Pate begleitet ihn [NAME KOLLEGE LAGER]. Arbeitszeit ist Montag bis Freitag, 7 bis 15:30 Uhr, Start ist am Montag.
Bitte erstelle jetzt den Einarbeitungsplan für die erste Woche.
```

### Assistent 2

**Einarbeitungsplan – Woche 1 (Lager)**
Neuer Kollege, Start Montag, Arbeitszeit Mo–Fr 7:00–15:30 Uhr
Ansprechperson: [NAME TEAMLEITUNG] | Pate: [NAME KOLLEGE LAGER]

**Ausgangslage:** Drei Jahre Erfahrung in einem Logistikzentrum, Handscanner und Lagerverwaltungssoftware bekannt, Staplerschein vorhanden. Offen sind die Sicherheitsunterweisung bei euch und die Einweisung ins Hochregal. Unser System und unsere Abläufe sind neu für ihn.

**Montag – Ankommen und Sicherheit**
- 7:00 Uhr: Empfang durch [NAME TEAMLEITUNG], Rundgang über das Gelände, Sozialräume, Spinde, Zutrittskarte
- 8:00 Uhr: Sicherheitsunterweisung (Verhalten im Lager, Fluchtwege, Meldeketten, Erste Hilfe, Ansprechpersonen)
- 10:00 Uhr: Unterschriften für Unterweisungen, Arbeitsschutzunterlagen, Schlüssel- und Zugangsregelung
- 11:00 Uhr: Einführung in unsere Organisation: Ablauf eines Arbeitstags, Schichtübergabe, Kommunikationswege
- Nachmittag: Begleiteter Lagerrundgang mit [NAME KOLLEGE LAGER] (Zonen, Warenannahme, Versand, Kommissionierbereich)
- 15:00 Uhr: Kurze Rückmeldung mit der Teamleitung, offene Fragen notieren

**Dienstag – Unser System kennenlernen**
- 7:00 Uhr: Kurzes Tagesbriefing
- Vormittag: Einweisung in unsere Lagerverwaltungssoftware: Anmeldung, Artikelstamm, Lagerplätze, Buchungsarten (Wareneingang, Umlagerung, Entnahme, Inventur)
- Nachmittag: Übung am System unter Anleitung des Paten, z. B. Test-Buchungen oder Wareneingang mit Begleitung
- Abschluss: Fragenliste für den Paten, Checkliste abhaken

**Mittwoch – Hochregal-Einweisung**
- 7:00 Uhr: Briefing
- Vormittag: Theoretische Einweisung in unser Hochregal: Regalsystem, Tragfähigkeiten, Lagerplatzlogik, Beschädigungen melden
- Mittag: Pause
- Nachmittag: Praktische Einweisung am Hochregal-Bediengerät bzw. am Regal durch [NAME KOLLEGE LAGER]; Dokumentation der Einweisung und Unterschrift
- Hinweis: Erst nach erfolgter Einweisung selbstständig im Hochregal arbeiten

**Donnerstag – Praxis unter Begleitung**
- 7:00 Uhr: Briefing
- Ganztägig: Mitarbeit im laufenden Betrieb (Wareneingang, Kommissionierung, Versand) mit dem Paten an seiner Seite
- Zwischendurch: Fragen direkt stellen, Abläufe gegenlesen
- 15:00 Uhr: Kurzes Feedbackgespräch mit dem Paten

**Freitag – Selbstständiger werden und Wochenabschluss**
- 7:00 Uhr: Briefing
- Vormittag: Einzelne Vorgänge selbstständig durchführen, der Pate kontrolliert stichprobenartig
- Mittag: Gemeinsame Auswertung der Woche
- 14:30 Uhr: Gespräch mit [NAME TEAMLEITUNG]: Was lief gut, was fehlt noch, Ziele für Woche 2
- 15:00 Uhr: Wochenabschluss, Zugänge und Unterlagen prüfen, Dank ans Team

**Checkliste Woche 1**
- [ ] Sicherheitsunterweisung absolviert und unterschrieben
- [ ] Hochregal-Einweisung absolviert und dokumentiert
- [ ] Staplerschein-Kopie und Unterlagen im Personalordner
- [ ] Zugang zur Lagerverwaltungssoftware eingerichtet und getestet
- [ ] Ansprechpersonen und Notfallkontakte bekannt
- [ ] Erstes Feedbackgespräch am Freitag geführt

**Hinweise für die Umsetzung**
- Der Pate sollte in Woche 1 möglichst immer erreichbar sein; Pausen und Zeitplan sind mit ihm abzustimmen.
- Der Plan lässt sich nach dem Freitagsgespräch für Woche 2 erweitern.

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1

```text
Ich möchte einen Einarbeitungsplan für einen neuen Kollegen im Lager unseres kleinen Technikbetriebs erstellen.

Bevor du anfängst: Stell mir zuerst 3 Fragen, die du brauchst, um einen wirklich passenden Plan zu schreiben. Warte auf meine Antworten.
```

### Assistent 1

Gerne. Das sind meine drei Fragen:

1. **Welche Vorerfahrung bringt der neue Kollege mit?** Zum Beispiel Lagererfahrung, Handscanner, Lagerverwaltungssoftware oder Kenntnisse im Technikbereich. Davon hängt ab, wie tief ich bei den Grundlagen anfange.
2. **Welche Berechtigungen und Pflichtunterweisungen hat er schon, und welche fehlen noch?** Ich denke an Staplerschein, Sicherheitsunterweisung, Brandschutz, Erste Hilfe und Einweisung in besondere Lagerbereiche wie Hochregal oder Gefahrstoffe.
3. **Wer begleitet ihn, und wie sieht der Rahmen aus?** Ich brauche die Ansprechperson, einen möglichen Paten, die Arbeitszeiten und den Starttermin. Dann kann ich Zeiten, Verantwortlichkeiten und Feedbackgespräche konkret einplanen.

Sobald ich Ihre Antworten habe, schreibe ich den Plan.

### Nutzer 2

```text
Hier meine Antworten:
1. Er hat drei Jahre Erfahrung in einem Logistikzentrum, kennt Handscanner und eine Lagerverwaltungssoftware, aber nicht unser System.
2. Einen Staplerschein hat er, die Sicherheitsunterweisung bei uns und die Einweisung in unser Hochregal braucht er noch.
3. Ansprechperson ist [NAME TEAMLEITUNG], als Pate begleitet ihn [NAME KOLLEGE LAGER]. Arbeitszeit ist Montag bis Freitag, 7 bis 15:30 Uhr, Start ist am Montag.
Bitte erstelle jetzt den Einarbeitungsplan für die erste Woche.
```

### Assistent 2

Danke, das hilft sehr. Hier ist der Plan für die erste Woche.

#### Einarbeitungsplan Lager, Woche 1

**Ansprechperson:** [NAME TEAMLEITUNG]
**Pate:** [NAME KOLLEGE LAGER]
**Arbeitszeit:** Mo bis Fr, 7:00 bis 15:30 Uhr (Pausen nach betrieblicher Regelung)

**Ausgangslage:** Er hat drei Jahre Logistikerfahrung, kennt Handscanner und eine Lagerverwaltungssoftware und hat einen Staplerschein. Neu für ihn sind unser System, unsere Sicherheitsregeln und das Hochregal. Deshalb legt der Plan den Schwerpunkt auf Sicherheit, unsere Abläufe und unser System. Allgemeine Lagergrundlagen werden nur kurz abgefragt.

**Wichtige Regel:** Bis die Einweisung ins Hochregal abgeschlossen ist, arbeitet er dort nicht selbstständig. Mit dem Stapler fährt er erst nach der Sicherheitsunterweisung, und anfangs nur mit dem Paten.

##### Montag: Ankommen und Sicherheit

| Zeit | Inhalt | Verantwortlich |
|---|---|---|
| 7:00 | Begrüßung, Kurzgespräch zu Erwartungen und Ablauf der Woche | [NAME TEAMLEITUNG] |
| 7:30 | Rundgang durch Betrieb und Lager: Wareneingang, Lagerbereiche, Versand, Pausen- und Sozialräume, Fluchtwege, Erste-Hilfe-Stellen, Feuerlöscher | [NAME KOLLEGE LAGER] |
| 9:00 | **Sicherheitsunterweisung** (Pflicht, schriftlich dokumentieren und unterschreiben lassen) | [NAME TEAMLEITUNG] |
| 10:30 | Ausgabe der persönlichen Schutzausrüstung (Sicherheitsschuhe, Handschuhe, Warnweste), Zugänge und Schlüssel | [NAME TEAMLEITUNG] |
| 11:30 | Mittagspause | |
| 12:15 | Mitlaufen mit dem Paten: Warenfluss kennenlernen, Lagerordnung, Platzsystematik | [NAME KOLLEGE LAGER] |
| 14:30 | Zugang zum Lagersystem einrichten, erster Blick auf die Oberfläche | [NAME KOLLEGE LAGER] |
| 15:15 | Kurzer Tagesrückblick (10 Minuten): Was ist offen? | Pate |

##### Dienstag: Unser System und die Abläufe

| Zeit | Inhalt | Verantwortlich |
|---|---|---|
| 7:00 | Tagesplanung mit dem Paten | Pate |
| 7:30 | Einführung in unser Lagerverwaltungssystem: Artikelstamm, Lagerplätze, Buchungen. Er kennt die Logik, daher liegt der Fokus auf den Unterschieden zu seinem bisherigen System. | Pate |
| 9:30 | Handscanner an unserem System anmelden und Funktionen testen | Pate |
| 11:30 | Mittagspause | |
| 12:15 | Wareneingang gemeinsam durchführen: Lieferschein prüfen, Menge und Zustand kontrollieren, einbuchen, einlagern | Pate |
| 14:00 | Selbst unter Aufsicht einbuchen (Übungsartikel oder unkritische Ware) | Pate |
| 15:15 | Tagesrückblick | Pate |

##### Mittwoch: Einweisung Hochregal und Staplerbetrieb

| Zeit | Inhalt | Verantwortlich |
|---|---|---|
| 7:00 | Tagesplanung | Pate |
| 7:30 | **Einweisung in das Hochregal**: Aufbau, Lastangaben und Belegungsregeln, Sicherheitsabstände, Verhalten bei Schäden, Meldewege (dokumentieren) | [NAME TEAMLEITUNG] bzw. dafür Befugte |
| 9:30 | Staplereinweisung im Betrieb: Fahrwege, Besonderheiten, Fahrzeugprüfung vor Schichtbeginn. Staplerschein und Betriebserlaubnis vom Arbeitgeber prüfen und dokumentieren. | [NAME TEAMLEITUNG] |
| 11:30 | Mittagspause | |
| 12:15 | Ein- und Auslagerungen im Hochregal mit dem Paten, anfangs nur Beobachten und Assistieren | Pate |
| 14:00 | Erste Lagerbewegungen im Hochregal unter direkter Aufsicht | Pate |
| 15:15 | Tagesrückblick | Pate |

##### Donnerstag: Kommissionieren, Versand, Qualität

| Zeit | Inhalt | Verantwortlich |
|---|---|---|
| 7:00 | Tagesplanung | Pate |
| 7:30 | Kommissionierung: Aufträge im System, Pickstrategie, Prüfung der Technikteile (Bezeichnung, Seriennummern, Zustand) | Pate |
| 9:30 | Verpackung und Versand: Verpackungsvorgaben für empfindliche Technikartikel, Versandpapiere, Übergabe an den Paketdienst | Pate |
| 11:30 | Mittagspause | |
| 12:15 | Eigenständige Kommissionieraufträge mit Stichprobenkontrolle durch den Paten | Pate |
| 14:00 | Retouren, Beschädigungen, Fehlmengen und Inventurdifferenzen: Wie melde ich sie? | Pate |
| 15:15 | Tagesrückblick | Pate |

##### Freitag: Selbstständiger arbeiten und Feedback

| Zeit | Inhalt | Verantwortlich |
|---|---|---|
| 7:00 | Tagesplanung, er schlägt selbst vor, was er heute übernimmt | Pate |
| 7:30 | Durchlauf: Wareneingang, Einlagerung, Kommissionierung und Versand überwiegend selbstständig, der Pate kontrolliert Stichproben | Pate |
| 11:30 | Mittagspause | |
| 12:15 | Weiter selbstständig, offene Fragen sammeln | Pate |
| 14:00 | **Feedbackgespräch** (30 bis 45 Minuten): Was lief gut? Wo gibt es Lücken? Ziele für Woche 2 | [NAME TEAMLEITUNG], Pate |
| 15:00 | Plan für Woche 2 festhalten | [NAME TEAMLEITUNG] |

##### Checkliste am Ende der Woche

- [ ] Sicherheitsunterweisung dokumentiert und unterschrieben
- [ ] Einweisung Hochregal durchgeführt und dokumentiert
- [ ] Staplerschein und Betriebserlaubnis geprüft und dokumentiert
- [ ] Schutzausrüstung, Zugänge und Schlüssel übergeben
- [ ] Zugang zum Lagersystem und Handscanner funktionieren
- [ ] Wareneingang, Einlagerung, Kommissionierung und Versand mindestens einmal selbst durchgeführt
- [ ] Feedbackgespräch geführt
- [ ] Themen für Woche 2 festgelegt

##### Hinweise

- **Pate entlasten:** Planen Sie für [NAME KOLLEGE LAGER] in dieser Woche weniger eigene Aufgaben ein, damit genug Zeit für die Begleitung bleibt.
- **Zeiten sind Richtwerte.** Wenn er schneller vorankommt, verschieben Sie Inhalte nach vorn. Wenn nicht, bleiben Sie lieber länger bei einem Thema, besonders bei Hochregal und Stapler.
- **Offene Punkte:** Die Pausenzeiten, die Verantwortlichen für die Hochregal-Einweisung und konkrete Übungsartikel habe ich nach Annahme eingesetzt. Bitte passen Sie sie an Ihren Betrieb an.
- **Rechtlicher Hinweis:** Die genauen Pflichten bei Unterweisungen und Dokumentation sollten Sie mit Ihrer Fachkraft für Arbeitssicherheit oder Ihrer Berufsgenossenschaft abstimmen.

Wenn Sie möchten, mache ich daraus eine druckbare Checkliste oder einen Plan für Woche 2 bis 4.

*(Überschriftenebenen der Modellantwort im Protokoll um zwei Ebenen abgesenkt, damit die Gliederung dieser Datei erhalten bleibt; Inhalt unverändert.)*

---

## Gesprächsprotokoll: Opus

### Nutzer 1

```text
Ich möchte einen Einarbeitungsplan für einen neuen Kollegen im Lager
unseres kleinen Technikbetriebs erstellen.

Bevor du anfängst: Stell mir zuerst 3 Fragen, die du brauchst, um einen
wirklich passenden Plan zu schreiben. Warte auf meine Antworten.
```

### Assistent 1

Gute Idee, erst die Eckdaten zu klären. Damit der Plan zu Ihrem Betrieb und zu Ihrem neuen Kollegen passt, brauche ich Antworten auf diese drei Fragen:

1. **Was bringt der neue Kollege mit?**
   Hat er schon in einem Lager oder in der Logistik gearbeitet? Kennt er Handscanner, Lagerverwaltungssoftware oder Warenwirtschaftssysteme? Oder fängt er in diesem Bereich ganz neu an?

2. **Welche Nachweise und Unterweisungen braucht er noch?**
   Hat er zum Beispiel schon einen Staplerschein? Welche Pflicht-Unterweisungen stehen bei Ihnen an, etwa Arbeitssicherheit, Brandschutz, Gefahrstoffe oder die Einweisung in bestimmte Regale, Maschinen oder Bereiche?

3. **Wie sieht der Rahmen aus?**
   Wer ist seine feste Ansprechperson? Gibt es einen Paten oder eine Patin aus dem Team? Wie sind die Arbeitszeiten, und an welchem Tag fängt er an?

Sobald ich Ihre Antworten habe, schreibe ich Ihnen einen konkreten Plan für die erste Woche.

### Nutzer 2

```text
Hier meine Antworten:
1. Er hat drei Jahre Erfahrung in einem Logistikzentrum, kennt Handscanner und eine Lagerverwaltungssoftware, aber nicht unser System.
2. Einen Staplerschein hat er, die Sicherheitsunterweisung bei uns und die Einweisung in unser Hochregal braucht er noch.
3. Ansprechperson ist [NAME TEAMLEITUNG], als Pate begleitet ihn [NAME KOLLEGE LAGER]. Arbeitszeit ist Montag bis Freitag, 7 bis 15:30 Uhr, Start ist am Montag.
Bitte erstelle jetzt den Einarbeitungsplan für die erste Woche.
```

### Assistent 2

Danke, das hilft sehr. Ihr neuer Kollege bringt Erfahrung mit. Der Plan muss ihm also kein Lagergrundwissen beibringen. Er soll ihm **Ihr System, Ihre Abläufe und Ihre Sicherheitsregeln** zeigen. Wichtig ist auch die richtige Reihenfolge: **Zuerst kommen Sicherheitsunterweisung und Hochregal-Einweisung, erst danach fährt er selbstständig Stapler.**

---

#### Einarbeitungsplan Lager – erste Woche

**Neuer Mitarbeiter:** [NAME NEUER KOLLEGE]
**Ansprechperson:** [NAME TEAMLEITUNG]
**Pate:** [NAME KOLLEGE LAGER]
**Arbeitszeit:** Mo–Fr, 7:00–15:30 Uhr
**Starttermin:** Montag, [DATUM]

**Ziel der Woche:** Am Freitag kennt der neue Kollege die Sicherheitsregeln und das Hochregal. Er arbeitet mit Ihrem Lagersystem und erledigt Wareneingang, Einlagerung und Kommissionierung schon weitgehend selbstständig, mit dem Paten als Rückhalt.

---

##### Montag – Ankommen und Sicherheit

| Uhrzeit | Inhalt | Wer |
|---|---|---|
| 7:00–7:30 | Begrüßung, kurze Vorstellung des Betriebs und des Teams | [NAME TEAMLEITUNG] |
| 7:30–8:30 | Organisatorisches: Schlüssel/Zugang, Spind, Arbeitskleidung und Schutzausrüstung (Sicherheitsschuhe, ggf. Handschuhe, Warnweste), Pausenregelung, Zeiterfassung | [NAME TEAMLEITUNG] |
| 8:30–10:30 | **Sicherheitsunterweisung**: Fluchtwege, Sammelplatz, Feuerlöscher, Erste Hilfe und Ersthelfer, Verkehrswege im Lager, Verhalten bei Unfällen, Gefahrstoffe (falls vorhanden). **Mit Unterschrift dokumentieren.** | [NAME TEAMLEITUNG] bzw. Sicherheitsbeauftragte/r |
| 10:30–12:00 | Rundgang durchs Lager mit dem Paten: Bereiche, Lagerplatz-Logik, Wareneingang, Versand, Ladezonen | [NAME KOLLEGE LAGER] |
| 12:00–12:30 | Mittagspause, gern gemeinsam mit dem Team | |
| 12:30–14:30 | Erster Blick ins Lagersystem: Anmeldung, Benutzerkonto, Handscanner einrichten, Grundmasken (Artikelsuche, Bestände, Lagerplätze) | [NAME KOLLEGE LAGER] |
| 14:30–15:15 | Mitlaufen beim Tagesgeschäft, Fragen sammeln | [NAME KOLLEGE LAGER] |
| 15:15–15:30 | Kurzes Abschlussgespräch: Wie war der erste Tag? Offene Fragen? | [NAME TEAMLEITUNG] |

**Vorab klären (vor Montag):** Zugangsdaten und Handscanner bereitlegen, Schutzausrüstung in der richtigen Größe besorgen, Unterweisungsunterlagen ausdrucken.

---

##### Dienstag – Hochregal und Stapler

| Uhrzeit | Inhalt | Wer |
|---|---|---|
| 7:00–9:30 | **Einweisung Hochregal**: Aufbau, Traglasten und Beschilderung, Regalprüfung und Schadensmeldung (z. B. Anfahrschäden), Verhalten im Regalgang, Personen im Gefahrenbereich. **Mit Unterschrift dokumentieren.** | [NAME KOLLEGE LAGER] / [NAME TEAMLEITUNG] |
| 9:30–11:00 | **Einweisung in Ihre Stapler**: Fahrzeugtypen, tägliche Sichtprüfung vor Fahrtbeginn, Laden/Akkuwechsel, Abstellen. Probefahrt unter Aufsicht | [NAME KOLLEGE LAGER] |
| 11:00–12:00 | Ein- und Auslagern im Hochregal **unter Aufsicht** | [NAME KOLLEGE LAGER] |
| 12:00–12:30 | Mittagspause | |
| 12:30–15:00 | **Wareneingang** im System: Lieferschein prüfen, Ware buchen, Abweichungen und Schäden melden. Erst zuschauen, dann selbst machen | [NAME KOLLEGE LAGER] |
| 15:00–15:30 | Fragen klären, Tag kurz durchsprechen | [NAME KOLLEGE LAGER] |

**Wichtig:** Ein Staplerschein allein reicht nicht. Der Arbeitgeber muss ihn **schriftlich beauftragen**, Stapler in Ihrem Betrieb zu fahren. Diese Beauftragung sollte nach der Einweisung vorliegen, bevor er allein fährt. [NAME TEAMLEITUNG] sollte das unterschreiben und zur Personalakte geben.

---

##### Mittwoch – Einlagerung und Kommissionierung

| Uhrzeit | Inhalt | Wer |
|---|---|---|
| 7:00–9:30 | Wareneingang und Einlagerung, mehr allein, der Pate in der Nähe | [NAME KOLLEGE LAGER] |
| 9:30–12:00 | **Kommissionierung**: Pickliste/Auftrag im System, Scannen, Packen, Versandvorbereitung | [NAME KOLLEGE LAGER] |
| 12:00–12:30 | Mittagspause | |
| 12:30–14:30 | Besonderheiten Ihres Betriebs: z. B. empfindliche Technikteile, ESD-Schutz, Seriennummern, Ersatzteile, Eilaufträge, Retouren | [NAME KOLLEGE LAGER] |
| 14:30–15:30 | Eigenständiges Arbeiten an einfachen Aufträgen | Neuer Kollege, Pate erreichbar |

---

##### Donnerstag – Selbstständiger arbeiten

| Uhrzeit | Inhalt | Wer |
|---|---|---|
| 7:00–12:00 | Normales Tagesgeschäft: Wareneingang, Einlagerung, Kommissionierung **weitgehend selbstständig** | Neuer Kollege, Pate erreichbar |
| 12:00–12:30 | Mittagspause | |
| 12:30–14:00 | Sonderfälle im System: Inventur/Bestandskorrektur, Umlagerung, Fehlbestände, Fehlermeldungen am Scanner | [NAME KOLLEGE LAGER] |
| 14:00–15:00 | Schnittstellen kennenlernen: kurze Gespräche mit Einkauf, Vertrieb/Auftragsannahme, Technik/Werkstatt. Wer braucht was vom Lager? | [NAME TEAMLEITUNG] organisiert |
| 15:00–15:30 | Offene Fragen sammeln | Neuer Kollege |

---

##### Freitag – Festigen und Rückblick

| Uhrzeit | Inhalt | Wer |
|---|---|---|
| 7:00–12:00 | Tagesgeschäft selbstständig, inkl. Versand und Wochenabschlussaufgaben (z. B. Ordnung, Leergut, Ladegeräte) | Neuer Kollege, Pate erreichbar |
| 12:00–12:30 | Mittagspause | |
| 12:30–13:30 | Gemeinsamer Check mit dem Paten: Was klappt schon, wo braucht er noch Übung? | [NAME KOLLEGE LAGER] |
| 13:30–14:30 | **Feedbackgespräch der ersten Woche** (siehe Fragen unten) | [NAME TEAMLEITUNG] |
| 14:30–15:30 | Restliche Aufgaben, Ausblick auf Woche 2 | Neuer Kollege |

**Fragen für das Feedbackgespräch:**
- Wie haben Sie die erste Woche erlebt?
- Was war klar, was ist noch unklar?
- Wo fühlen Sie sich schon sicher, wo noch nicht?
- Was hat Ihnen gefehlt oder hätten wir besser machen können?
- Was sind die Ziele für die nächsten Wochen?

---

##### Checkliste für die Woche

- [ ] Zugang, Schlüssel, Spind, Zeiterfassung eingerichtet
- [ ] Schutzausrüstung ausgegeben
- [ ] Sicherheitsunterweisung durchgeführt und unterschrieben
- [ ] Einweisung Hochregal durchgeführt und unterschrieben
- [ ] Staplerschein-Kopie zur Akte genommen
- [ ] Einweisung in betriebseigene Stapler erfolgt
- [ ] Schriftliche Beauftragung zum Staplerfahren unterschrieben
- [ ] Benutzerkonto Lagersystem und Handscanner eingerichtet
- [ ] Wareneingang, Einlagerung, Kommissionierung geübt
- [ ] Feedbackgespräch am Freitag geführt

---

**Tipps zur Anpassung:**
- Die Uhrzeiten sind nur ein Vorschlag. Wenn morgens die meiste Ware kommt, kann das Mitlaufen im Wareneingang auch auf den Vormittag rücken.
- Prüfen Sie bitte, ob bei Ihnen weitere Unterweisungen Pflicht sind, etwa Brandschutz, Gefahrstoffe oder Ladungssicherung. Das hängt von Ihrem Betrieb und Ihrer Gefährdungsbeurteilung ab. Ihre Fachkraft für Arbeitssicherheit oder die Berufsgenossenschaft kann das verbindlich sagen.
- Ein kurzes Gespräch mit dem Paten jeden Tag, schon 10 Minuten, beantwortet viele Fragen früh.

Soll ich daraus auch eine kompakte Version zum Ausdrucken machen oder einen Plan für die Wochen 2 bis 4 ergänzen?

*(Überschriftenebenen der Modellantwort im Protokoll um zwei Ebenen abgesenkt, damit die Gliederung dieser Datei erhalten bleibt; Inhalt unverändert.)*

---

Zurück zum [Übungsblatt Übung 2](../06_Uebungen/Uebung_2_Gute_Prompts.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md#übung-2-gute-prompts)
