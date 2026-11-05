# Testlauf: Übung 2 / Basis B – Baukasten-Prompt Willkommensnachricht + Plan

**Herkunft:** Aufgabe B aus [Uebung_2_Gute_Prompts.md](../06_Uebungen/Uebung_2_Gute_Prompts.md#aufgabe-b--derselbe-auftrag-mit-dem-baukasten) (Block 4). Kein Zusatzmaterial. Zugehörige Lösungshinweise: [Trainer-Loesungshinweise.md – Übung 2](../06_Uebungen/Trainer-Loesungshinweise.md#übung-2-gute-prompts). Gegenstück: Testlauf zu Aufgabe A (Minimal-Prompt, `ue2-a.md`).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt:** Baukasten-Prompt aus dem Übungsblatt, unverändert, in einem neuen Chat (siehe Gesprächsprotokolle unten).

**Was eine gute Antwort enthalten muss:** herzliche Willkommensnachricht in Du-Form, höchstens 80 Wörter; Wochenplan als Tabelle mit genau den Spalten Tag | Vormittag | Nachmittag | Ansprechperson für Montag bis Freitag; erkennbarer Lagerbezug (Lagerverwaltungssystem, Wareneingang, Stapler/Sicherheit); Namen nur als Platzhalter; kein Widerspruch zur Arbeitszeit 7–15:30 Uhr; keine erfundenen Personennamen. Die Lösungshinweise nennen als Merkmale für den A/B-Vergleich: „passt zum Lager, Tabelle direkt nutzbar, Platzhalter statt erfundener Namen“.

---

## Bewertung

Wortzahlen per `python3` gezählt (`len(text.split())`), einmal nur der Nachrichtentext, einmal inklusive Anrede, Gruß und Signatur-Platzhalter.

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Wortzahl Text / mit Anrede+Gruß | 56 / 62 | 68 / 74 (Modell sagt „ca. 65“) | 56 / 64 (Modell sagt „ca. 65“) |
| ≤ 80 Wörter | ja | ja | ja |
| Du-Form, herzlicher Ton | ja | ja | ja |
| Tabelle mit genau den 4 Spalten | ja | ja | ja |
| Montag–Freitag vollständig | ja | ja | ja |
| Lagerverwaltungssystem | ja (Di) | ja (Mo Zugang, Mi Buchungen) | ja (Mo Zugang, Di Buchen) |
| Wareneingang | ja (Di und Mi, doppelt) | ja (Di) | ja (Di) |
| Stapler / Flurförderzeuge | **nein** – nur „Arbeitssicherheit“ aus dem Beispiel | ja (Do, inkl. Berechtigungsnachweis prüfen) | ja (Di, „falls ein Staplerschein vorliegt“) |
| Vorerfahrung berücksichtigt | kaum (Fr „eigenständige Kommissionierung“) | ja (Nachweis prüfen statt Neuschulung) | ja (Tipp „Seine Erfahrung nutzen“) |
| Namen nur als Platzhalter | ja | ja | ja |
| Erfundene Personennamen | keine | keine | keine |
| Arbeitszeit 7–15:30 | genannt, kein Widerspruch | genannt, Treffpunkt 7:00 Uhr | genannt, Treffpunkt 7 Uhr |
| Vermutete Details (nicht im Prompt) | [NAME SCHICHTLEITUNG], Scanner | Haupteingang, Sicherheitsschuhe mitbringen, „inkl. Mittagspause“, E-Mail/Zeiterfassung | Empfang, ERP, Personalabteilung, Fertigung, Paketdienste/Speditionen |
| Zusatznutzen | – | 3 Hinweise (Pflichtunterweisungen dokumentieren, Pate) | 4 Tipps + Rückfrage-Angebot |
| Lesbarkeit der Tabelle | kurz, sehr übersichtlich | mittel | Zellen sehr voll, bis 3 Ansprechpersonen je Zeile |
| Gesamturteil | brauchbar, etwas generisch | sehr gut | sehr gut, aber lang |

---

## Gefundene Fehler mit Beleg

1. **Kein Modell hat Personennamen erfunden.** Alle setzen Platzhalter ([VORNAME], [NAME TEAMLEITUNG], [NAME PATE/PATIN] usw.). Das Ziel der Übung wird in allen drei Läufen erreicht.
2. **Alle halten die 80-Wort-Grenze sicher ein** (56–68 Wörter Text). Die Selbstangaben „ca. 65“ von Sonnet (tatsächlich 68 bzw. 74) und Opus (tatsächlich 56 bzw. 64) sind nur ungefähr – kein echter Fehler, aber ein schöner Beleg dafür, dass Wortzahl-Angaben der KI nachgezählt werden sollten (Anknüpfung an Demo 4b „Zählen“).
3. **Haiku: Stapler fehlt, Beispielzeile 1:1 übernommen.** Die Montagszeile ist wörtlich das Beispiel aus dem Prompt („Begrüßung, Rundgang, Arbeitssicherheit | Arbeitsplatz einrichten, Zugänge testen“). Flurförderzeuge/Stapler kommen nicht vor; Wareneingang steht Dienstag und Mittwoch doppelt. Die Vorerfahrung des Kollegen spielt kaum eine Rolle.
4. **Vermutete Details statt Fakten (kein Fehler im engeren Sinn, aber Prüfpunkt).** Sonnet: „Komm am Montag um 7:00 Uhr zum Haupteingang. Ich hole dich dort ab. Bring bitte Sicherheitsschuhe mit“ und „Arbeitszeit … (inklusive Mittagspause)“. Opus: „Am Montag um 7 Uhr holen wir dich am Empfang ab“, „Lagerverwaltungssystem/ERP“, „Paketdienste und Speditionen“. Nichts davon stand im Prompt. Es sind plausible Annahmen, die vor dem Versand geprüft werden müssen – genau die Frage „Hat die KI etwas erfunden oder vermutet?“ aus der Vergleichstabelle.
5. **Kleinere sprachliche/inhaltliche Unschärfen.**
   - Opus: „Mitlaufen bei der Pate/Patin“ (Grammatik).
   - Sonnet: Donnerstag hat nur eine Ansprechperson ([NAME SICHERHEITSBEAUFTRAGTE/R]), obwohl vormittags Versand/Spediteure dran sind – die Staplereinweisung durch Sicherheitsbeauftragte ist zudem in vielen Betrieben Sache einer beauftragten Person für Flurförderzeuge.
   - Opus: bis zu drei Ansprechpersonen in einer Zelle – formal korrekt, aber schwerer nutzbar als eine Person pro Tag.
6. **Testartefakt (nicht im Material):** Im Haiku-Protokoll steht in „Nutzer 1“ zusätzlich die Testanweisung „Gib das komplette Gesprächsprotokoll zurück …“. Diese gehört nicht zum Übungsprompt und hat das Ergebnis nicht erkennbar beeinflusst.

---

## Lehren für die Auswertung

- **Die Übung funktioniert wie gedacht.** Alle drei Modelle liefern mit dem Baukasten-Prompt direkt nutzbare, lagerbezogene Ergebnisse im gewünschten Format – der Kontrast zu Aufgabe A dürfte deutlich sein.
- **Das Beispiel wirkt – manchmal zu stark.** Haiku übernimmt die Beispielzeile wörtlich. Gute Lehre: Ein Beispiel zeigt die Form, kann aber auch den Inhalt „festnageln“. Wer mehr will, schreibt dazu „Beispiel nur für das Format“.
- **Platzhalter-Anweisung wirkt zuverlässig.** Kein erfundener Name in drei Läufen. Zeigen: Ein einziger Satz im Format-Baustein verhindert das Erfinden.
- **Aber: Vermutungen wandern in die Details.** Haupteingang, Empfang, Sicherheitsschuhe, Mittagspause, ERP – plausibel, aber nicht vorgegeben. Ideal, um die Zeile „Hat die KI etwas erfunden oder vermutet?“ zu füllen: Auch ein guter Prompt entbindet nicht vom Gegenlesen.
- **Mehr Modell = mehr Text.** Opus liefert Tipps und eine Rückfrage, die Tabelle wird aber sehr voll. Gesprächsanlass: „Ist mehr immer besser?“ Brücke zu Aufgabe D („Kürzer bitte – halbe Seite“).
- **Wortzahlen nachzählen.** Beide „ca. 65“-Angaben liegen daneben, die Grenze wird trotzdem eingehalten. Wer eine harte Grenze braucht, zählt selbst (Textverarbeitung).
- **Zeit:** Prompt einfügen und lesen dauert 2–3 Minuten; die Richtzeit von 8 Minuten für A + B + Vergleich ist realistisch, bei Opus-ähnlich langen Antworten eher knapp.

---

## Gesprächsprotokolle

### Haiku

#### Nutzer 1

```text
Rolle: Du bist eine erfahrene Teamleiterin in einem kleinen technischen Herstellerbetrieb.

Kontext: Wir sind die Nordlicht Technik GmbH, ca. 80 Mitarbeitende. Am Montag fängt ein neuer Kollege im Lager an. Er hat schon Erfahrung in der Lagerlogistik, kennt aber unsere Abläufe und Systeme noch nicht. Arbeitszeit: Montag bis Freitag, 7 bis 15:30 Uhr.

Aufgabe: Erstelle
1. eine kurze, herzliche Willkommensnachricht an ihn (höchstens 80 Wörter, wir duzen uns),
2. einen Einarbeitungsplan für seine erste Woche.

Format: Den Plan als Tabelle mit den Spalten Tag | Vormittag | Nachmittag | Ansprechperson. Für Namen setze Platzhalter wie [NAME TEAMLEITUNG].

Beispiel für eine Tabellenzeile:
Montag | Begrüßung, Rundgang, Arbeitssicherheit | Arbeitsplatz einrichten, Zugänge testen | [NAME TEAMLEITUNG]

Gib das komplette Gesprächsprotokoll zurück, Format:
### Nutzer 1
<Nachricht>
### Assistent 1
<deine vollständige Antwort>
(usw. für jede Nachricht)
```

#### Assistent 1

Hallo [VORNAME],

herzlich willkommen bei der Nordlicht Technik GmbH! Schön, dass du am Montag bei uns im Lager anfängst. Deine Erfahrung in der Lagerlogistik wird uns sicher weiterhelfen, und unsere Abläufe und Systeme lernst du Schritt für Schritt kennen. Lass dir Zeit und frag einfach nach, egal wie klein die Frage dir erscheint. Wir freuen uns auf dich!

Viele Grüße
[NAME TEAMLEITUNG]

**Einarbeitungsplan Woche 1** (Arbeitszeit 7:00 bis 15:30 Uhr)

Tag | Vormittag | Nachmittag | Ansprechperson
--- | --- | --- | ---
Montag | Begrüßung, Rundgang, Arbeitssicherheit | Arbeitsplatz einrichten, Zugänge testen | [NAME TEAMLEITUNG]
Dienstag | Einweisung in unser Lagerverwaltungssystem (Grundlagen) | Wareneingang begleiten, Abläufe kennenlernen | [NAME TEAMLEITUNG]
Mittwoch | Wareneingang und Warenprüfung mit Kollegen | Kommissionierung begleiten, Scanner und Prozesse üben | [NAME SCHICHTLEITUNG]
Donnerstag | Verpackung und Versand, Verladung | Erste Aufträge unter Anleitung bearbeiten | [NAME SCHICHTLEITUNG]
Freitag | Eigenständige Kommissionierung mit Rückfragen | Wochenrückblick mit Teamleitung, Fragen und Feedback | [NAME TEAMLEITUNG]

---

### Sonnet

#### Nutzer 1

```text
Rolle: Du bist eine erfahrene Teamleiterin in einem kleinen technischen Herstellerbetrieb.

Kontext: Wir sind die Nordlicht Technik GmbH, ca. 80 Mitarbeitende. Am Montag fängt ein neuer Kollege im Lager an. Er hat schon Erfahrung in der Lagerlogistik, kennt aber unsere Abläufe und Systeme noch nicht. Arbeitszeit: Montag bis Freitag, 7 bis 15:30 Uhr.

Aufgabe: Erstelle
1. eine kurze, herzliche Willkommensnachricht an ihn (höchstens 80 Wörter, wir duzen uns),
2. einen Einarbeitungsplan für seine erste Woche.

Format: Den Plan als Tabelle mit den Spalten Tag | Vormittag | Nachmittag | Ansprechperson. Für Namen setze Platzhalter wie [NAME TEAMLEITUNG].

Beispiel für eine Tabellenzeile:
Montag | Begrüßung, Rundgang, Arbeitssicherheit | Arbeitsplatz einrichten, Zugänge testen | [NAME TEAMLEITUNG]
```

#### Assistent 1

**1. Willkommensnachricht**

Hallo [VORNAME],

herzlich willkommen bei der Nordlicht Technik GmbH! Wir freuen uns sehr, dass du ab Montag unser Lagerteam verstärkst. Deine Erfahrung in der Lagerlogistik ist bei uns Gold wert. Unsere Abläufe und Systeme lernst du in der ersten Woche in Ruhe kennen, wir nehmen uns Zeit für dich. Komm am Montag um 7:00 Uhr zum Haupteingang. Ich hole dich dort ab. Bring bitte Sicherheitsschuhe mit, falls du welche hast.

Bis Montag!
[NAME TEAMLEITUNG]

(Wortzahl: ca. 65)

**2. Einarbeitungsplan für die erste Woche**

Arbeitszeit: Montag bis Freitag, 7:00 bis 15:30 Uhr (inklusive Mittagspause).

| Tag | Vormittag | Nachmittag | Ansprechperson |
|---|---|---|---|
| Montag | Begrüßung, Rundgang durch Betrieb und Lager, Arbeitssicherheit (Fluchtwege, Brandschutz, Erste Hilfe) | Arbeitsplatz einrichten, Zugänge testen (Lagerverwaltungssystem, E-Mail, Zeiterfassung), Persönliche Schutzausrüstung ausgeben | [NAME TEAMLEITUNG] |
| Dienstag | Wareneingang: Ablauf, Lieferscheinprüfung, Sichtkontrolle und Reklamationen kennenlernen | Einlagerung und Lagerplatzsystem; Wareneingang gemeinsam mit Kollegin/Kollege durchführen | [NAME KOLLEGE WARENEINGANG] |
| Mittwoch | Lagerverwaltungssystem: Bestandsabfragen, Buchungen, Umlagerungen (zuerst unter Anleitung) | Kommissionierung: Aufträge zusammenstellen, Verpackung und Kennzeichnung | [NAME KOLLEGE KOMMISSIONIERUNG] |
| Donnerstag | Warenausgang und Versand: Versandpapiere, Zusammenarbeit mit Spediteuren | Flurförderzeuge: Berechtigungsnachweis prüfen, ggf. Einweisung und Übungsfahrt mit Sicherheitsbeauftragten | [NAME SICHERHEITSBEAUFTRAGTE/R] |
| Freitag | Selbstständiges Arbeiten mit Begleitung: Kommissionieren und Buchen, Inventur- und Bestandskontrolle kennenlernen | Feedbackgespräch (Was lief gut, was ist unklar?), Ziele für die nächsten Wochen vereinbaren | [NAME TEAMLEITUNG] |

**Hinweise:**
- Namen, Systeme und Schulungsinhalte bitte an eure tatsächlichen Gegebenheiten anpassen.
- Pflichtunterweisungen (Arbeitssicherheit, Flurförderzeuge) vor der ersten selbstständigen Tätigkeit dokumentieren und unterschreiben lassen.
- Am besten benennst du eine feste Patin oder einen festen Paten für die Woche, der bei Fragen jederzeit ansprechbar ist.

---

### Opus

#### Nutzer 1

```text
Rolle: Du bist eine erfahrene Teamleiterin in einem kleinen technischen
Herstellerbetrieb.

Kontext: Wir sind die Nordlicht Technik GmbH, ca. 80 Mitarbeitende.
Am Montag fängt ein neuer Kollege im Lager an. Er hat schon Erfahrung
in der Lagerlogistik, kennt aber unsere Abläufe und Systeme noch nicht.
Arbeitszeit: Montag bis Freitag, 7 bis 15:30 Uhr.

Aufgabe: Erstelle
1. eine kurze, herzliche Willkommensnachricht an ihn (höchstens 80 Wörter,
   wir duzen uns),
2. einen Einarbeitungsplan für seine erste Woche.

Format: Den Plan als Tabelle mit den Spalten Tag | Vormittag | Nachmittag |
Ansprechperson. Für Namen setze Platzhalter wie [NAME TEAMLEITUNG].

Beispiel für eine Tabellenzeile:
Montag | Begrüßung, Rundgang, Arbeitssicherheit | Arbeitsplatz einrichten,
Zugänge testen | [NAME TEAMLEITUNG]
```

#### Assistent 1

Gern, hier sind die Willkommensnachricht und der Plan für die erste Woche.

**1. Willkommensnachricht**

> Hallo [NAME NEUER KOLLEGE],
>
> herzlich willkommen bei Nordlicht Technik! Wir freuen uns sehr, dass du ab Montag unser Lagerteam verstärkst. Deine Erfahrung in der Lagerlogistik hilft uns sehr. Unsere Abläufe und Systeme zeigen wir dir in Ruhe. Am Montag um 7 Uhr holen wir dich am Empfang ab. Frag jederzeit nach, wir sind für dich da. Auf eine gute Zusammenarbeit!
>
> Viele Grüße
> [NAME TEAMLEITUNG]

*(ca. 65 Wörter)*

**2. Einarbeitungsplan für die erste Woche** (Arbeitszeit jeweils 7:00–15:30 Uhr)

| Tag | Vormittag | Nachmittag | Ansprechperson |
|---|---|---|---|
| **Montag** | Begrüßung am Empfang, Vorstellung im Team, Rundgang durch Lager und Betrieb, Arbeitsschutz-Unterweisung (Fluchtwege, Erste Hilfe, Schutzausrüstung ausgeben) | Arbeitsplatz einrichten, Zugänge testen (PC, Lagerverwaltungssystem/ERP, Zeiterfassung, E-Mail), Organisatorisches mit der Personalabteilung | [NAME TEAMLEITUNG], [NAME PERSONALABTEILUNG], [NAME SICHERHEITSFACHKRAFT] |
| **Dienstag** | Wareneingang: Annahme, Prüfung der Lieferscheine, Qualitätskontrolle, Buchen im System, Mitlaufen bei der Pate/Patin | Lagerordnung und Lagerplatzsystem kennenlernen, Einlagern unter Anleitung; Einweisung in Flurförderzeuge (Stapler, Hubwagen), falls ein Staplerschein vorliegt | [NAME PATE/PATIN], [NAME STAPLERBEAUFTRAGTE/R] |
| **Mittwoch** | Kommissionierung: Pickaufträge, Scanner bedienen, Materialbereitstellung für die Produktion | Schnittstelle Produktion: Rundgang durch die Fertigung, Abläufe bei Materialanforderungen und Rücklieferungen | [NAME PATE/PATIN], [NAME ANSPRECHPERSON PRODUKTION] |
| **Donnerstag** | Warenausgang und Versand: Verpackung, Versandpapiere, Abläufe mit den Paketdiensten und Speditionen | Bestandsführung: Inventurregeln, Umgang mit Fehlbeständen und Reklamationen, Schnittstelle zum Einkauf | [NAME PATE/PATIN], [NAME ANSPRECHPERSON EINKAUF/VERSAND] |
| **Freitag** | Eigenständig arbeiten im Wareneingang oder in der Kommissionierung, die Pate/Patin bleibt in der Nähe | Feedbackgespräch zur ersten Woche: offene Fragen, Eindrücke, Ziele für die nächsten Wochen festlegen | [NAME TEAMLEITUNG], [NAME PATE/PATIN] |

**Tipps zur Umsetzung:**
- **Fester Pate oder feste Patin:** Eine erfahrene Lagerkraft als feste Ansprechperson für die ganze Woche gibt Sicherheit.
- **Zugänge vorher anlegen:** Bitte vor Montag mit der IT klären, damit die Logins am ersten Tag funktionieren.
- **Arbeitskleidung und Sicherheitsschuhe:** Größen am besten vorab erfragen.
- **Seine Erfahrung nutzen:** Frag ihn ruhig, wie er Abläufe aus seinem früheren Betrieb kennt. Daraus ergeben sich oft gute Verbesserungsideen.

Soll ich den Plan noch an eure Bereiche anpassen, zum Beispiel wenn bei euch Wareneingang und Versand zusammengelegt sind, oder daraus eine druckbare Checkliste machen?
