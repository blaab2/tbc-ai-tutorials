# Testlauf: Übung 2 / Basis A – Minimal-Prompt Einarbeitungsplan

**Herkunft:** Aufgabe A aus [Uebung_2_Gute_Prompts.md](../06_Uebungen/Uebung_2_Gute_Prompts.md#aufgabe-a--der-minimal-prompt) (Block 4, Stufe 1: Basis). Kein Material nötig. Zugehörige Lösungshinweise: [Trainer-Loesungshinweise.md – Übung 2](../06_Uebungen/Trainer-Loesungshinweise.md#übung-2-gute-prompts), Abschnitt „Woran du ein gutes Ergebnis erkennst“ (Vergleich A/B).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt (jeweils in einem neuen Chat, getrennt von Aufgabe B):**

```text
Schreib einen Einarbeitungsplan.
```

**Was laut Material herauskommen soll:** Eine Vergleichsbasis für Aufgabe B. Erwartet wird ein allgemeiner Büro- oder Konzernplan ohne Bezug zum Lager oder zum kleinen Betrieb. Die Willkommensnachricht fehlt, weil die KI nichts davon weiß. Möglich sind auch Rückfragen statt eines Plans. Der Punkt der Übung: Die KI muss raten.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Passt zu Lager / kleinem Betrieb? | **nein**. Ausdrücklich „für neue Mitarbeitende **im Büro**“ | **nein**. Beispiele Vertrieb, Buchhaltung, IT, Kundenservice | **nein**. Beispiele Sachbearbeitung, Vertrieb, Buchhaltung; Schreibtisch, ERP/CRM. Erwähnt immerhin Arbeitsschutz, Brandschutz und Lieferanten |
| Eher Büro- oder Konzernplan? | Büro, mit Konzernzügen (Intranet, Facility, Unternehmensleitbild, Compliance, Ticketsystem) | Büro mit eigener HR-Abteilung | Konzernzüge: eigene Abteilungen Personal, IT, Office/Facility; Organigramm, Freigabeprozesse |
| Zeitraum | 90 Tage (angenommen) | 3 Monate (angenommen) | bis Ende der Probezeit, Phasen bis Monat 3+ (angenommen) |
| Passt der Zeitraum zum Auftrag „erste Woche“? | nein, die erste Woche ist nur eine Phase | nein, aber Woche 1 als eigene Tabelle | nein, aber Tag 1 und Woche 1 gesondert |
| Willkommensnachricht | fehlt (wie erwartet) | fehlt. Steht nur als Punkt auf der To-do-Liste („Willkommensmail … vorbereiten“) | fehlt. Steht nur als Punkt auf der To-do-Liste („Willkommens-E-Mail … schicken“) |
| Rückfragen? | ja, aber nur nebenbei im Fließtext (Rolle, Abteilung, Probezeit, Tools) | ja, 5 nummerierte Fragen **plus** Plan | ja, 7 nummerierte Fragen **plus** Plan |
| Nur Rückfragen, kein Plan? | nein | nein | nein |
| Format direkt nutzbar? | nein, Stichpunkt-Listen, keine Namen- oder Datumsfelder | teilweise, Woche 1 als Tabelle mit „Verantwortlich“, Checkliste | am ehesten als **Vorlage**: Kopffelder mit Platzhaltern, Tabellen mit Spalte „Erledigt“. Inhaltlich aber nicht für das Lager |
| Erfundene Namen oder Firmendaten? | nein | nein | nein (Platzhalter wie [Name], [Aufgabe 1]) |
| Stille Annahmen | Büro, 90 Tage, Pate, Facility/IT/Personal vorhanden | 3 Monate, HR-Abteilung, Pate | Personal-, IT- und Facility-Abteilung, Probezeit, Mittagessen mit Team |
| Anrede | du | du | Sie |
| Länge (Wörter, per `python3`) | ca. 275 | ca. 365 | ca. 530 |
| Nacharbeit für die Lager-Situation | fast komplett neu | fast komplett neu | fast komplett neu, Struktur weiter verwendbar |

**Kurz:** Die Erwartung aus dem Material trifft bei allen drei Modellen zu. Alle liefern einen allgemeinen Büroplan über etwa drei Monate. Lager, Stapler, Sicherheitsschuhe, Lagerverwaltung oder Schichtzeiten kommen nirgends vor. Die Willkommensnachricht fehlt. Abweichend vom Material liefert aber **kein** Modell nur Rückfragen. Alle liefern einen Plan, und Sonnet und Opus stellen zusätzlich ausdrücklich Fragen.

---

## Gefundene Fehler mit Beleg

Bei einem Minimal-Prompt gibt es keine Quelle, gegen die man Fakten prüfen könnte. „Fehler“ sind hier vor allem **Annahmen**, die die KI ohne Nachfrage trifft, und kleine innere Widersprüche.

1. **Alle drei – Zeitraum selbst festgelegt:** Der eigentliche Auftrag (Übungsblatt: „einen Plan für die erste Woche“) steht nicht im Prompt. Alle Modelle nehmen deshalb drei Monate an: Haiku „Vorlage für die ersten 90 Tage“, Sonnet „Dauer: 3 Monate“, Opus „Phase 5: Bis zum Ende der Probezeit“. Für die Situation ist das am Bedarf vorbei. Das ist der deutlichste Beleg für „die KI muss raten“.
2. **Alle drei – Bürosetting angenommen:** Haiku schreibt es ausdrücklich („für neue Mitarbeitende im Büro“). Sonnet und Opus zeigen es durch ihre Beispiele (Vertrieb, Buchhaltung, Sachbearbeitung Einkauf), durch „Schreibtisch, Telefon“ und „ERP-System, CRM“. Für einen Lagermitarbeiter fehlen z. B. Staplerschein, persönliche Schutzausrüstung, Lagerverwaltungssystem, Wareneingang und Kommissionierung.
3. **Konzernstrukturen angenommen:** Opus verteilt Aufgaben auf „Personal“, „IT“ und „Office/Facility“. Sonnet setzt eine „HR“-Abteilung voraus. Haiku nennt „Ansprechpersonen für IT, Personal und Facility“, „Intranet“, „Unternehmensleitbild“ und „Ticketsystem“. In einem Betrieb mit ca. 80 Mitarbeitenden (Nordlicht Technik, Aufgabe B) gibt es diese Abteilungen oft nicht getrennt.
4. **Willkommensnachricht – leicht zu übersehen:** Sonnet („Willkommensmail mit Ablauf des ersten Tages“) und Opus („Willkommens-E-Mail mit Infos zum ersten Tag schicken“) erwähnen sie als **To-do**, schreiben sie aber nicht. Teilnehmende könnten beim Überfliegen meinen, sie sei „dabei“.
5. **Haiku – innerer Widerspruch:** Unter „Phase 4: Eigenverantwortung (Monat 3)“ steht „Zwischenbewertung nach etwa 6 bis 8 Wochen“. 6 bis 8 Wochen liegen aber in Monat 2. Klein, zeigt aber, dass auch allgemeine Pläne nicht ungeprüft stimmen.
6. **Haiku – Testartefakt, kein Modellverhalten:** Am Ende der Haiku-Antwort steht ein „Hinweis zur Aufgabe“ über ultracode und Subagenten. Das kommt aus der Testumgebung und würde in [KI-TOOL] nicht erscheinen. Er ist im Protokoll unten vollständig enthalten, für die Bewertung aber nicht relevant.
7. **Keine erfundenen Namen, Firmen oder Zahlen:** Kein Modell erfindet einen Firmennamen, eine Person oder konkrete Daten. Opus setzt sogar von sich aus Platzhalter ([Name], [TT.MM.JJJJ]). Im Lösungshinweis steht, dass der Baukasten-Prompt besser ist, weil er „Platzhalter statt erfundener Namen“ bringt. **Gegenüber diesem A-Ergebnis trägt das Argument nicht.** Der Unterschied liegt hier in Passung und Format, nicht im Erfinden.

---

## Lehren für die Auswertung

- **Die Übung funktioniert wie gedacht.** Der Kontrast zu Aufgabe B ist deutlich: kein Lager, falscher Zeitraum, keine Willkommensnachricht, keine Tabelle im gewünschten Format. Die Vergleichstabelle im Übungsblatt lässt sich mit A-Ergebnissen gut ausfüllen.
- **„Die KI rät“ an einem Beispiel zeigen:** Am besten an der Dauer. Niemand hat „3 Monate“ gesagt, alle drei Modelle haben es angenommen. Und am Arbeitsplatz: Haiku schreibt ausdrücklich „im Büro“. Das ist eine Annahme, keine Bosheit, genau wie im Übungsblatt („Ihr fehlten einfach die Informationen“).
- **Zur Frage „Hat die KI etwas erfunden oder vermutet?“:** Viele werden antworten „nein, nichts erfunden“, weil keine Namen erfunden wurden. Dann nachfragen: *Was hat sie vermutet?* Büro, drei Monate, Personalabteilung, Pate, Probezeit. Vermuten ist die häufigere und leisere Form des Ratens.
- **Rückfragen sind ein Pluspunkt, kein Fehler.** Sonnet und Opus fragen nach Stelle, Dauer, Vorkenntnissen und Ansprechpersonen. Das ist eine gute Brücke zu Aufgabe C („Stell mir zuerst 3 Fragen“). Die KI weiß selbst, was ihr fehlt. Mit Aufgabe C macht man daraus Methode, statt einen langen Plan zu bekommen, den man wegwirft.
- **Länge ist kein Qualitätsmerkmal.** Opus liefert mit ca. 530 Wörtern den ausführlichsten und professionellsten Plan. Für das Lager ist er aber genauso unpassend wie der kürzere von Haiku. Gut für die Erkenntnis: „sieht gut aus“ heißt nicht „passt zu mir“.
- **Modellunterschiede:** Haiku liefert eine schlichte Stichpunkt-Vorlage und fragt nur nebenbei. Sonnet liefert Struktur plus Fragenliste. Opus liefert eine ausfüllbare Vorlage mit Tabellen, Gesprächsterminen und Tipps und wechselt in die Sie-Form. Wer ein einfacheres Tool nutzt, bekommt eher Haiku-artige Ergebnisse. Der Kontrast zu B ist dort noch größer.
- **Zeit:** Prompt eintippen dauert Sekunden, die Antwort ist schnell da. Das Lesen langer Antworten (bis ca. 530 Wörter, Opus) kostet aber 2–3 Minuten. Empfehlung: Teilnehmende sollen A nur überfliegen und auf drei Dinge achten: Lager? Erste Woche? Willkommensnachricht? Dann passt A+B gut in die Übungszeit.
- **Achtung bei Tools mit Gedächtnis:** Wenn [KI-TOOL] eine Erinnerungs- oder Personalisierungsfunktion hat (z. B. gespeicherte Angaben zur Person oder Firma), kann auch der Minimal-Prompt plötzlich zum Lager passen. Dann den Effekt ansprechen, statt die Übung als „gescheitert“ zu werten. Vorher im Schulungs-Account prüfen.

---

## Probleme im Material und Vorschläge

- **„manchmal sogar Rückfragen“ präzisieren:** In [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md#woran-du-ein-gutes-ergebnis-erkennst) steht: „Der Minimal-Prompt liefert oft einen allgemeinen Büro- oder Konzernplan, manchmal sogar Rückfragen.“ In allen drei Läufen kam **beides zusammen**: ein Plan und Rückfragen. Nur Rückfragen ohne Plan kamen nicht vor. Vorschlag:
  > „Der Minimal-Prompt liefert meist einen allgemeinen Büroplan über ca. drei Monate – oft mit einer Liste von Rückfragen am Anfang oder Ende. Das Raten zeigt sich vor allem bei Dauer (3 Monate statt erste Woche) und Arbeitsplatz (Büro statt Lager).“
- **Argument „Platzhalter statt erfundener Namen“ abschwächen:** Gleiche Stelle in den Lösungshinweisen. Im Test hat kein Modell bei A Namen erfunden, Opus nutzt selbst Platzhalter. Vorschlag: „(passt zum Lager, erste Woche statt drei Monate, Tabelle direkt nutzbar, Willkommensnachricht dabei)“ statt „(passt zum Lager, Tabelle direkt nutzbar, Platzhalter statt erfundener Namen)“.
- **Vergleichstabelle im Übungsblatt ergänzen (optional):** In [Uebung_2_Gute_Prompts.md](../06_Uebungen/Uebung_2_Gute_Prompts.md#vergleicht-die-ergebnisse-von-a-und-b) die Frage „Hat die KI etwas erfunden oder vermutet?“ um ein Beispiel ergänzen: „Hat die KI etwas erfunden oder vermutet? (z. B. Dauer, Abteilung, Büro statt Lager)“. Dann suchen Teilnehmende nicht nur nach erfundenen Namen.
- **Lesehinweis bei Aufgabe A (optional):** Hinter „Schau dir das Ergebnis an.“ ergänzen: „Achte besonders darauf: Geht es ums Lager? Um die erste Woche?“ Das spart Lesezeit bei langen Antworten.
- Sonst ist die Aufgabe klar formuliert. Der Hinweis „Ja, die Willkommensnachricht fehlt“ nimmt Verwirrung vorweg, und das erwartete Ergebnis tritt zuverlässig ein.

---

## Gesprächsprotokolle

### Haiku

#### Nutzer 1

Schreib einen Einarbeitungsplan.

#### Assistent 1

Gern. Ein allgemeingültiger Einarbeitungsplan für neue Mitarbeitende im Büro lässt sich gut in vier Phasen gliedern. Wenn du mir Rolle, Abteilung, Dauer der Probezeit und Firmenspezifika (Tools, Ansprechpersonen) nennst, passe ich ihn gezielt an.

**Einarbeitungsplan (Vorlage für die ersten 90 Tage)**

**Phase 1: Ankommen (Tag 1 bis 5)**
- Begrüßung durch die Führungskraft und Vorstellung im Team
- Arbeitsplatz, Hardware, Zugänge (E-Mail, Telefon, Intranet, Dateiablage) einrichten
- Gemeinsamer Rundgang: Räume, Küche, Sanitär, Ansprechpersonen für IT, Personal und Facility
- Lesen der wichtigsten internen Unterlagen: Organigramm, Unternehmensleitbild, Verhaltensregeln, Datenschutz- und Sicherheitsrichtlinien
- Erstes Gespräch mit der Führungskraft: Erwartungen, Ziele und Fragen klären

**Phase 2: Orientierung (Woche 2 bis 4)**
- Einweisung in die eigenen Aufgaben und Prozesse anhand konkreter Beispiele
- Schulung in den wichtigsten Werkzeugen (Software, Vorlagen, Ablagestruktur, Ticketsystem)
- Hospitationen bei Kolleginnen und Kollegen aus angrenzenden Bereichen
- Tägliche kurze Rücksprache mit einer festen Patin oder einem festen Paten
- Erste kleine, begleitete Aufgaben übernehmen

**Phase 3: Selbstständigkeit (Monat 2)**
- Eigenständige Bearbeitung klar umrissener Aufgaben, bei Bedarf mit Rückfrage
- Wöchentliches Feedbackgespräch mit der Führungskraft
- Teilnahme an Team-Meetings und Projektabstimmungen
- Vertiefende Schulungen (z. B. Fachthemen, Kundenprozesse, Compliance)
- Selbstreflexion: Was läuft gut, wo brauche ich noch Unterstützung?

**Phase 4: Eigenverantwortung (Monat 3)**
- Übernahme eines eigenen Aufgabenbereichs mit definierten Zielen
- Zwischenbewertung nach etwa 6 bis 8 Wochen, gemeinsam mit der Führungskraft
- Festlegung von Entwicklungszielen für die nächsten Monate
- Abschlussgespräch zum Ende der Einarbeitung (Feedback in beide Richtungen)

**Checkliste für die Führungskraft**
- Vor Arbeitsbeginn: Zugänge beantragt, Arbeitsplatz bereit, Pate benannt
- Nach einer Woche: erstes Feedbackgespräch
- Nach 30, 60 und 90 Tagen: Zwischenstand und Ziele überprüfen
- Am Ende: Einarbeitung dokumentieren und abschließen

Wenn du mir sagst, für welche Position der Plan gedacht ist, kann ich die Inhalte konkreter formulieren.

---

Hinweis zur Aufgabe: In diesem Lauf wurden keine Dateien angehängt und keine Tools verwendet. Die Prüfung mit ultracode, Sonnet, Haiku oder Opus sowie das Dokumentieren erwarteter Ergebnisse konnte ich von diesem Subagenten aus nicht ausführen, da mir dafür kein Modellaufruf zur Verfügung steht.

*(Anmerkung Testlauf: Der letzte Absatz „Hinweis zur Aufgabe“ stammt aus der Testumgebung und gehört nicht zur eigentlichen Antwort.)*

### Sonnet

#### Nutzer 1

Schreib einen Einarbeitungsplan.

#### Assistent 1

Gerne! Damit der Plan wirklich zu euch passt, brauche ich ein paar Angaben. Bis dahin hier ein allgemein verwendbarer Entwurf, den du anpassen kannst.

**Kurz zu klären (bitte antworten, dann passe ich den Plan an):**
1. Für welche Position bzw. Abteilung ist der Plan (z. B. Vertrieb, Buchhaltung, IT, Kundenservice)?
2. Wie lange soll die Einarbeitung dauern (z. B. 4 Wochen, 3 oder 6 Monate)?
3. Wie viel Erfahrung bringt die neue Person mit (Berufseinsteiger/in oder erfahren)?
4. Arbeitet die Person vor Ort, remote oder hybrid?
5. Wer ist Ansprechperson bzw. Pate/Patin, und wie groß ist das Team?

---

## Allgemeiner Einarbeitungsplan (Dauer: 3 Monate)

### Vor dem ersten Arbeitstag
- Arbeitsvertrag und Unterlagen vollständig abgeschlossen
- Arbeitsplatz, Hardware, Zugänge (E-Mail, Software, Zutritt) vorbereitet
- Team informiert, Pate/Patin benannt
- Willkommensmail mit Ablauf des ersten Tages (Uhrzeit, Ort, Ansprechperson)

### Woche 1: Ankommen und Orientierung
| Tag | Inhalt | Verantwortlich |
|---|---|---|
| Tag 1 | Begrüßung, Rundgang, Vorstellung im Team, Arbeitsplatz einrichten, Zugänge testen | Führungskraft, Pate/Patin |
| Tag 1 | Organisatorisches: Arbeitszeiten, Urlaub, Krankmeldung, Datenschutz, Arbeitssicherheit | HR |
| Tag 2–3 | Überblick Unternehmen: Struktur, Produkte/Dienstleistungen, Kunden, Werte | Führungskraft |
| Tag 3–4 | Kennenlernen der wichtigsten Kolleginnen und Kollegen und Schnittstellen | Pate/Patin |
| Tag 5 | Erstes Feedbackgespräch: Wie läuft der Start? Offene Fragen? | Führungskraft |

### Woche 2–4: Grundlagen lernen
- Einführung in Tools, Systeme und Prozesse der eigenen Abteilung
- Mitlaufen und Hospitieren bei Kolleginnen und Kollegen
- Erste kleine, klar umrissene Aufgaben mit enger Begleitung
- Lektüre wichtiger Dokumente (Prozessbeschreibungen, Richtlinien, Handbücher)
- Ende Woche 4: Feedbackgespräch, Ziele für Monat 2 festlegen

### Monat 2: Selbstständiger arbeiten
- Eigene Aufgabenbereiche schrittweise übernehmen
- Erste Mitarbeit in Projekten oder im laufenden Tagesgeschäft
- Regelmäßige kurze Abstimmungen (z. B. wöchentlich 30 Minuten mit der Führungskraft)
- Fachliche Schulungen oder Weiterbildungen besuchen
- Ende Monat 2: Zwischengespräch mit Zielabgleich

### Monat 3: Verantwortung übernehmen
- Eigenverantwortliche Bearbeitung des Aufgabenbereichs
- Verbesserungsvorschläge einbringen
- Pate/Patin zieht sich schrittweise zurück
- Ende Monat 3: Abschlussgespräch zur Einarbeitung (Probezeit-Zwischenbilanz), gemeinsame Zielvereinbarung für die nächsten Monate

### Checkliste für den Erfolg
- [ ] Alle Zugänge und Arbeitsmittel am Tag 1 funktionsfähig
- [ ] Pate/Patin fest eingeplant (mit Zeitbudget)
- [ ] Feedbackgespräche terminiert (Woche 1, Woche 4, Monat 2, Monat 3)
- [ ] Lernziele pro Phase schriftlich festgehalten
- [ ] Neue Person kennt alle wichtigen Ansprechpersonen

Sag mir einfach die Angaben zu den Fragen oben, dann mache ich daraus einen konkreten Plan mit Namen, Terminen und fachlichen Inhalten für eure Abteilung.

### Opus

#### Nutzer 1

Schreib einen Einarbeitungsplan.

#### Assistent 1

Gern. Damit der Plan wirklich passt, brauche ich noch ein paar Angaben. Ich gebe Ihnen schon jetzt eine allgemeine Vorlage, die Sie direkt verwenden oder anpassen können.

**Diese Angaben helfen mir beim Anpassen:**
1. **Um welche Stelle geht es?** (z. B. Sachbearbeitung Einkauf, Vertrieb Innendienst, Buchhaltung, Technik)
2. **Wie heißt die Abteilung und wie groß ist das Unternehmen?**
3. **Wie lange soll die Einarbeitung dauern?** (z. B. 4 Wochen, 3 Monate, bis Ende der Probezeit)
4. **Welche Vorkenntnisse bringt die neue Person mit?** (Berufseinsteiger oder erfahrene Fachkraft)
5. **Wer ist beteiligt?** (Führungskraft, Pate/Patin, Kolleginnen und Kollegen, IT, Personalabteilung)
6. **Welche Programme und Abläufe sind wichtig?** (z. B. ERP-System, CRM, interne Freigabeprozesse)
7. **Gibt es Pflichtschulungen?** (Datenschutz, Arbeitssicherheit, IT-Sicherheit, Compliance)

---

## Einarbeitungsplan (Vorlage)

**Neue Mitarbeiterin / neuer Mitarbeiter:** [Name]
**Position:** [Stellenbezeichnung]
**Abteilung:** [Abteilung]
**Startdatum:** [TT.MM.JJJJ]
**Führungskraft:** [Name]
**Pate/Patin:** [Name]
**Ende der Probezeit:** [TT.MM.JJJJ]

---

### Phase 0: Vor dem ersten Arbeitstag
| Aufgabe | Verantwortlich | Erledigt |
|---|---|---|
| Arbeitsvertrag und Personalunterlagen vollständig | Personal | ☐ |
| Arbeitsplatz einrichten (Schreibtisch, Telefon, Schlüssel/Zugangskarte) | Office/Facility | ☐ |
| Laptop, E-Mail-Konto und Zugänge zu den Programmen anlegen | IT | ☐ |
| Team über den Neuzugang informieren | Führungskraft | ☐ |
| Paten/Patin benennen | Führungskraft | ☐ |
| Willkommens-E-Mail mit Infos zum ersten Tag schicken (Uhrzeit, Ansprechpartner, Anfahrt) | Führungskraft | ☐ |

### Phase 1: Erster Tag
| Zeit | Inhalt | Verantwortlich |
|---|---|---|
| Vormittag | Begrüßung, Vorstellung im Team, Rundgang | Führungskraft |
| Vormittag | Arbeitsplatz, IT-Einweisung, Passwörter, Telefon | IT / Pate |
| Mittag | Gemeinsames Mittagessen mit dem Team | Pate |
| Nachmittag | Überblick über das Unternehmen, Organigramm, Ziele der Abteilung | Führungskraft |
| Nachmittag | Organisatorisches: Arbeitszeiten, Urlaub, Krankmeldung, Zeiterfassung | Personal |

### Phase 2: Erste Woche
- Pflichtunterweisungen: Arbeitsschutz, Brandschutz, Datenschutz, IT-Sicherheit
- Einführung in die wichtigsten Programme und Ablagestrukturen
- Kennenlernen der wichtigsten Schnittstellen (andere Abteilungen, Kunden, Lieferanten)
- Mitlaufen bei Kolleginnen und Kollegen
- Erste einfache Aufgaben unter Anleitung
- **Ende der Woche:** kurzes Feedbackgespräch mit der Führungskraft (Wie war der Start? Was fehlt noch?)

### Phase 3: Wochen 2 bis 4
- Schrittweise Übernahme eigener Aufgaben: [Aufgabe 1], [Aufgabe 2], [Aufgabe 3]
- Vertiefung in Fachprozesse und Arbeitsanweisungen
- Teilnahme an Teambesprechungen und regelmäßigen Terminen
- Wöchentlicher kurzer Austausch mit dem Paten/der Patin
- **Ende des ersten Monats:** Zwischengespräch, erste Ziele für die nächsten Monate festlegen

### Phase 4: Monat 2 bis 3
- Selbstständige Bearbeitung der Kernaufgaben
- Übernahme erster eigener Verantwortungsbereiche oder Projekte
- Fachschulungen nach Bedarf
- **Nach 3 Monaten:** Feedbackgespräch (Stand der Einarbeitung, Stärken, Unterstützungsbedarf)

### Phase 5: Bis zum Ende der Probezeit
- Volle Übernahme der Aufgaben laut Stellenbeschreibung
- Rückblick auf die vereinbarten Ziele
- **Probezeitgespräch:** Bewertung beider Seiten, Ziele und Weiterbildung für die nächste Zeit

---

### Gesprächstermine im Überblick
| Zeitpunkt | Gespräch | Teilnehmende |
|---|---|---|
| Ende Woche 1 | Erstes Feedback | Führungskraft, neue Person |
| Ende Monat 1 | Zwischengespräch, Ziele | Führungskraft, neue Person |
| Ende Monat 3 | Entwicklungsgespräch | Führungskraft, neue Person |
| Vor Ende der Probezeit | Probezeitgespräch | Führungskraft, ggf. Personal |

### Tipps für eine gute Einarbeitung
- **Nicht alles auf einmal:** Informationen lieber auf mehrere Tage verteilen.
- **Feste Ansprechperson:** Ein Pate oder eine Patin senkt die Hemmschwelle, Fragen zu stellen.
- **Schriftliche Unterlagen:** Eine Checkliste oder ein kleines Handbuch mit den wichtigsten Abläufen, Kontakten und Abkürzungen hilft sehr.
- **Feedback in beide Richtungen:** Fragen Sie die neue Person auch, was an der Einarbeitung verbessert werden kann.

---

Wenn Sie mir sagen, für welche Stelle und welchen Zeitraum der Plan gedacht ist, mache ich daraus einen konkreten Plan mit den passenden Aufgaben, Programmen und Ansprechpersonen. Auf Wunsch auch als Checkliste zum Abhaken oder als Tabelle, die Sie in Word oder Excel übernehmen können.
