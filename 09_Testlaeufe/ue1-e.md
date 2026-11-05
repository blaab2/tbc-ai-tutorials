# Testlauf: Übung 1 / Für Schnelle E – Drei Betreffzeilen

**Herkunft:** [Übung 1: Texte schreiben](../06_Uebungen/Uebung_1_Texte_schreiben.md), Abschnitt „Stufe 3: Für Schnelle“, Aufgabe E.
Material: [kundenmail_beschwerde.txt](../07_Beispielmaterial/kundenmail_beschwerde.txt) · Trainer-Hinweise: [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md), Abschnitt „Übung 1: Texte schreiben“ (zu Aufgabe E dort nur: „Aufgaben E–G auf dem Übungsblatt“).

> **Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Getesteter Ablauf:** Im selben Chat zuerst der Startprompt aus Aufgabe A (mit der Kundenmail), danach der Prompt aus Aufgabe E unverändert:

```text
Schlage mir 3 kurze, sachliche Betreffzeilen für meine Antwort an den
Kunden vor. Maximal 8 Wörter pro Betreff.
```

**Prüfkriterien:** genau 3 Betreffzeilen; jede höchstens 8 Wörter (nachgezählt); sachlich, keine Großbuchstaben-/Ausrufezeichen-Dramatik (Gegenbeispiel: der Kundenbetreff „WIE LANGE NOCH???“); idealerweise Auftragsnummer 4711-NT oder SG-40 enthalten; keine Zusagen im Betreff, die die Mail nicht trägt (z. B. kein konkretes Lieferdatum).

---

## Bewertung

Wortzählung per Python (Leerzeichen-getrennt, Gedankenstrich „–“ nicht als Wort gezählt):

```
python3 -c "for s in ['Auftrag 4711-NT: Stand und neuer Liefertermin', ...]: print(len([w for w in s.split() if w!='–']), s)"
```

| Modell | Betreff | Wörter | Nummer enthalten | Sachlich | Zusage-Risiko |
|---|---|---|---|---|---|
| Haiku | 1. Auftrag 4711-NT: Stand und neuer Liefertermin | 6 | 4711-NT | ja | leicht: „neuer Liefertermin“ – in der Mail nur Platzhalter |
| Haiku | 2. Ihre Lieferung SG-40: Rückmeldung bis Mittwoch | 6 | SG-40 | ja | ja: kündigt Rückmeldung bis Mittwoch an, obwohl die Mail selbst die Rückmeldung ist |
| Haiku | 3. Steuergehäuse SG-40 und Rechnung RE-2024-0815 | 5 | SG-40, RE-2024-0815 | ja | keins |
| Sonnet | 1. Auftrag 4711-NT: Liefertermin und nächste Schritte | 6 | 4711-NT | ja | keins |
| Sonnet | 2. Ihre Steuergehäuse SG-40: Entschuldigung und Terminbestätigung | 6 | SG-40 | ja | ja: „Terminbestätigung“ – nur haltbar, wenn [NEUER LIEFERTERMIN] ausgefüllt ist |
| Sonnet | 3. Auftrag 4711-NT: Verbindlicher Liefertermin und Rechnungsprüfung | 6 | 4711-NT | ja | ja: „Verbindlicher Liefertermin“ – dito |
| Opus | 1. Auftrag 4711-NT: Liefertermin und nächste Schritte | 6 | 4711-NT | ja | keins |
| Opus | 2. Ihre Nachricht zu Auftrag 4711-NT – Entschuldigung und Stand | 8 (9 mit „–“) | 4711-NT | ja | keins |
| Opus | 3. Steuergehäuse SG-40: verbindlicher Liefertermin und Rechnungsprüfung | 6 (Opus sagt 7) | SG-40 | ja | ja, aber von Opus selbst benannt |

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Genau 3 Betreffzeilen | ja | ja | ja |
| Alle ≤ 8 Wörter | ja (5–6) | ja (6) | ja (6–8), Selbstzählung einmal falsch |
| Sachlich, keine Dramatik | ja | ja | ja |
| Auftragsnummer / SG-40 enthalten | 3/3 | 3/3 | 3/3 |
| Keine ungedeckte Zusage | 2 von 3 unkritisch („Rückmeldung bis Mittwoch“ problematisch) | 1 von 3 unkritisch (2× „Terminbestätigung/verbindlicher Termin“) | 2 von 3 unkritisch, Risiko bei Nr. 3 selbst erklärt |
| Zusatznutzen | – | – | Empfehlung + Begründung, Wortzahlen angegeben |

**Gesamturteil:** Die Aufgabe funktioniert wie gedacht – alle drei Modelle liefern formal korrekte, sachliche Betreffzeilen mit Auftragsnummer. Die Lernchance liegt nicht in der Form, sondern im **Inhalt**: Mehrere Betreffs versprechen etwas („verbindlicher Liefertermin“, „Terminbestätigung“, „Rückmeldung bis Mittwoch“), das die Mail nur als Platzhalter enthält.

---

## Gefundene Fehler mit Beleg

1. **Opus zählt falsch (Nr. 3):** „Steuergehäuse SG-40: verbindlicher Liefertermin und Rechnungsprüfung (7 Wörter)“ – tatsächlich 6 Wörter (Steuergehäuse / SG-40: / verbindlicher / Liefertermin / und / Rechnungsprüfung). Die Grenze wird nicht verletzt, aber die selbst angegebene Zahl stimmt nicht. Nr. 2 „(8 Wörter)“ stimmt nur, wenn man den Gedankenstrich nicht mitzählt. Gute Brücke zur [Zähl-Demo](demo-4b-zaehlen.md): Zahlenangaben des Modells über den eigenen Text nachprüfen.
2. **Sonnet Nr. 2 und 3 / Opus Nr. 3 – Zusage im Betreff:** „Terminbestätigung“ bzw. „Verbindlicher Liefertermin“. Im Entwurf steht der Termin nur als `[NEUER LIEFERTERMIN]`. Wird die Mail verschickt, bevor der Platzhalter ausgefüllt ist (was Opus in Aufgabe A ausdrücklich als Option empfiehlt), verspricht der Betreff etwas, das der Text nicht hält – bei einem Kunden, der genau „nicht wieder voraussichtlich“ fordert. Opus weist selbst darauf hin („Variante 3 passt nur, wenn der verbindliche Termin bereits in der Mail steht“), Sonnet nicht.
3. **Haiku Nr. 2 – „Rückmeldung bis Mittwoch“:** Die Antwort *ist* die Rückmeldung, die der Kunde bis Mittwoch erwartet. Als Betreff wirkt das wie eine weitere Vertröstung – genau das, worüber sich Herr Brenner beschwert („zweimal … vertröstet“). Zudem ist im Entwurf von Haiku der Mittwoch an einen Platzhalter `[DATUM]` gekoppelt – Zusage ohne gesicherte Grundlage.
4. **Haiku Nr. 3 – Vermischung zweier Vorgänge (gering):** Laut Kundenmail gehört RE-2024-0815 zur *Ersatzteillieferung vom letzten Monat*, nicht zum Auftrag 4711-NT. „Steuergehäuse SG-40 und Rechnung RE-2024-0815“ ist sachlich nicht falsch (zwei Themen), kann beim Empfänger aber den Eindruck erwecken, die Rechnung betreffe die Gehäuse.
5. **Keine erfundenen Fakten:** Kein Modell nennt im Betreff ein Datum, einen Rabatt oder eine Gutschrift. Alle Nummern (4711-NT, SG-40, RE-2024-0815) stimmen mit der Quelle überein.

Nebenbefund aus Aufgabe A (nicht Gegenstand dieser Prüfung): Opus' Entwurf enthält keine Betreffzeile – Aufgabe E ist dann tatsächlich nötig. Haiku und Sonnet hatten bereits in A einen Betreff gesetzt; beide wiederholen diesen in E in ähnlicher Form.

---

## Lehren für die Auswertung

- **Betreff = kleinste Zusage.** Der Betreff wird zuerst gelesen. Fragen an die Gruppe: „Würdest du ‚Verbindlicher Liefertermin‘ in den Betreff schreiben, wenn im Text noch [NEUER LIEFERTERMIN] steht?“ Merksatz: Der Betreff darf nichts versprechen, was die Mail nicht hält.
- **Selbstauskünfte nachzählen.** Opus liefert Wortzahlen mit – eine davon ist falsch. Das wirkt gründlich, ist aber nicht verlässlich. Kurzer Rückgriff auf die Zähl-Demo aus Block 1.
- **Kontrast zum Kundenbetreff zeigen:** „WIE LANGE NOCH??? Auftrag 4711-NT / Steuergehäuse“ vs. „Auftrag 4711-NT: Liefertermin und nächste Schritte“ – Auftragsnummer vorn erleichtert das Zuordnen im Postfach, deeskaliert und ist sachlich.
- **Auswahl ist Arbeit des Menschen.** Drei Vorschläge sind ein Menü, keine Entscheidung. Opus empfiehlt von sich aus Variante 1 mit Begründung – eine gute Vorlage für die Nachfrage „Welchen würdest du nehmen und warum?“.
- **Gleicher Chat nötig.** Der Prompt „für meine Antwort“ funktioniert nur, weil der Entwurf aus Aufgabe A im selben Chat steht. Wer einen neuen Chat öffnet, bekommt generische Betreffs ohne Auftragsnummer.
- Modellunterschiede sind hier gering; die Aufgabe eignet sich gut als schneller Zusatz (2–3 Minuten).

---

## Gesprächsprotokolle

### Haiku

#### Nutzer 1

Ich arbeite im Vertrieb der Nordlicht Technik GmbH. Unten steht eine verärgerte Kundenmail wegen eines Lieferverzugs.

Schreibe mir einen Antwortentwurf, der:
- sich für die Verzögerung entschuldigt, ohne Schuld abzuwälzen,
- auf die konkreten Punkte des Kunden eingeht,
- einen nächsten Schritt anbietet (z. B. Rückruf oder neuer Liefertermin),
- höflich und sachlich ist und höchstens 150 Wörter hat.

Erfinde keine Fakten wie Liefertermine oder Rabatte. Wo mir Informationen fehlen, setze einen Platzhalter in eckigen Klammern, z. B. [NEUER LIEFERTERMIN].

Hier die Kundenmail: [Inhalt der Datei kundenmail_beschwerde.txt, Absender Markus Brenner, Brenner Gerätebau GmbH]

#### Assistent 1

**Betreff: Auftrag 4711-NT / Steuergehäuse SG-40**

Sehr geehrter Herr Brenner,

vielen Dank für Ihre Nachricht. Es tut mir sehr leid, dass die Lieferung der 120 Steuergehäuse SG-40 (Auftrag 4711-NT) nicht wie zugesagt in KW 18 erfolgt ist, dass Sie auf Rückmeldungen warten mussten und dass Ihre Montage dadurch stillsteht. Das nehmen wir sehr ernst.

Wir klären den aktuellen Stand Ihres Auftrags und melden uns bis Mittwoch, [DATUM], bei Ihnen. Eine Teillieferung von 60 Stück prüfen wir ebenfalls. Den verbindlichen, schriftlichen Liefertermin bestätigen wir Ihnen: [NEUER LIEFERTERMIN].

Ihren Wunsch nach einem Entgegenkommen nehmen wir ernst; das besprechen wir gern persönlich. Die Frachtkosten auf Rechnung RE-2024-0815 prüfen wir und korrigieren sie, sofern die frei-Haus-Vereinbarung bestätigt ist.

Ich rufe Sie am [WUNSCHTERMIN] unter [TELEFONNUMMER] an, um die nächsten Schritte abzustimmen.

Mit freundlichen Grüßen
[IHR NAME]
Vertrieb, Nordlicht Technik GmbH

#### Nutzer 2

Schlage mir 3 kurze, sachliche Betreffzeilen für meine Antwort an den Kunden vor. Maximal 8 Wörter pro Betreff.

#### Assistent 2

1. Auftrag 4711-NT: Stand und neuer Liefertermin
2. Ihre Lieferung SG-40: Rückmeldung bis Mittwoch
3. Steuergehäuse SG-40 und Rechnung RE-2024-0815

---

### Sonnet

#### Nutzer 1

Ich arbeite im Vertrieb der Nordlicht Technik GmbH. Unten steht eine verärgerte Kundenmail wegen eines Lieferverzugs.

Schreibe mir einen Antwortentwurf, der:
- sich für die Verzögerung entschuldigt, ohne Schuld abzuwälzen,
- auf die konkreten Punkte des Kunden eingeht,
- einen nächsten Schritt anbietet (z. B. Rückruf oder neuer Liefertermin),
- höflich und sachlich ist und höchstens 150 Wörter hat.

Erfinde keine Fakten wie Liefertermine oder Rabatte. Wo mir Informationen fehlen, setze einen Platzhalter in eckigen Klammern, z. B. [NEUER LIEFERTERMIN].

Hier die Kundenmail:
[Inhalt von kundenmail_beschwerde.txt: Markus Brenner, Brenner Gerätebau GmbH, Auftrag 4711-NT, 120 Steuergehäuse SG-40, zugesagt KW 18, jetzt KW 21 nichts geliefert, kein Anruf, zweimal vertröstet, Montage steht teilweise still, fordert verbindlichen schriftlichen Liefertermin, akzeptiert notfalls Teillieferung von 60 Stück, fordert mindestens 10 % Nachlass, bemängelt 85 Euro Fracht auf Rechnung RE-2024-0815 trotz vereinbarter Lieferung frei Haus, erwartet Rückmeldung bis Mittwoch.]

#### Assistent 1

Betreff: Ihr Auftrag 4711-NT – Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

bitte entschuldigen Sie die Verspätung Ihrer 120 Steuergehäuse SG-40 und dass Sie darüber nicht von uns informiert wurden. Dass Ihre Montage dadurch teilweise stillsteht, bedauern wir sehr.

- Liefertermin: Wir bestätigen Ihnen bis Mittwoch schriftlich den verbindlichen Termin [NEUER LIEFERTERMIN]. Eine Teillieferung von 60 Stück prüfen wir und teilen Ihnen mit, ob und wann sie möglich ist [TERMIN TEILLIEFERUNG].
- Nachlass: Ihren Wunsch haben wir an [ZUSTÄNDIGE STELLE] weitergegeben. Dazu melden wir uns [ZEITPUNKT/ENTSCHEIDUNG].
- Fracht: Wir prüfen die 85 Euro auf RE-2024-0815 gegen die vereinbarte Lieferung frei Haus und korrigieren sie bei Bestätigung [ERGEBNIS DER PRÜFUNG].

Gern rufe ich Sie vorab an: [TELEFONNUMMER / RÜCKRUFZEIT].

Mit freundlichen Grüßen
[NAME]
Vertrieb, Nordlicht Technik GmbH

#### Nutzer 2

Schlage mir 3 kurze, sachliche Betreffzeilen für meine Antwort an den Kunden vor. Maximal 8 Wörter pro Betreff.

#### Assistent 2

1. Auftrag 4711-NT: Liefertermin und nächste Schritte
2. Ihre Steuergehäuse SG-40: Entschuldigung und Terminbestätigung
3. Auftrag 4711-NT: Verbindlicher Liefertermin und Rechnungsprüfung

---

### Opus

#### Nutzer 1

Ich arbeite im Vertrieb der Nordlicht Technik GmbH. Unten steht eine
verärgerte Kundenmail wegen eines Lieferverzugs.

Schreibe mir einen Antwortentwurf, der:
- sich für die Verzögerung entschuldigt, ohne Schuld abzuwälzen,
- auf die konkreten Punkte des Kunden eingeht,
- einen nächsten Schritt anbietet (z. B. Rückruf oder neuer Liefertermin),
- höflich und sachlich ist und höchstens 150 Wörter hat.

Erfinde keine Fakten wie Liefertermine oder Rabatte. Wo mir Informationen
fehlen, setze einen Platzhalter in eckigen Klammern, z. B. [NEUER LIEFERTERMIN].

Hier die Kundenmail:
[INHALT VON /home/daniel/tbc-ai-tutorials/07_Beispielmaterial/kundenmail_beschwerde.txt]

#### Assistent 1

Hier ist ein Antwortentwurf mit rund 130 Wörtern:

---

Sehr geehrter Herr Brenner,

vielen Dank für Ihre offenen Worte. Sie haben recht: Die 120 Steuergehäuse SG-40 (Auftrag 4711-NT) haben wir nicht wie zugesagt in KW 18 geliefert. Außerdem haben wir Sie nicht rechtzeitig informiert. Dafür entschuldige ich mich ausdrücklich, zumal Ihre Montage und Ihre Zusage an Ihren eigenen Kunden davon abhängen.

Verbindlicher Liefertermin für die gesamte Menge ist der [NEUER LIEFERTERMIN]. Eine Teillieferung von 60 Stück ist [MÖGLICH AM DATUM / NICHT MÖGLICH, WEIL …].

Ihren Wunsch nach einem Nachlass habe ich an [ZUSTÄNDIGE PERSON/ABTEILUNG] weitergegeben. Sie erhalten bis [DATUM] eine Antwort.

Die Frachtkosten von 85 Euro auf der Rechnung RE-2024-0815 prüfen wir und melden uns wegen der Korrektur bei Ihnen.

Gern rufe ich Sie am [DATUM/UHRZEIT] an, um alles persönlich zu besprechen.

Mit freundlichen Grüßen
[IHR NAME]
[POSITION]
Nordlicht Technik GmbH
[TELEFON]

---

Hinweise:
- Der Kunde erwartet bis Mittwoch eine Antwort. Schicken Sie die Mail also möglichst vorher ab, auch wenn noch nicht alle Platzhalter geklärt sind. Sie können dann z. B. schreiben: „Den verbindlichen Termin bestätige ich Ihnen bis [DATUM]."
- Zum Nachlass sagt der Entwurf bewusst weder zu noch ab. Das sollte intern entschieden werden.

#### Nutzer 2

Schlage mir 3 kurze, sachliche Betreffzeilen für meine Antwort an den
Kunden vor. Maximal 8 Wörter pro Betreff.

#### Assistent 2

Hier sind drei Vorschläge:

1. Auftrag 4711-NT: Liefertermin und nächste Schritte (6 Wörter)
2. Ihre Nachricht zu Auftrag 4711-NT – Entschuldigung und Stand (8 Wörter)
3. Steuergehäuse SG-40: verbindlicher Liefertermin und Rechnungsprüfung (7 Wörter)

Ich empfehle Variante 1. Sie ist kurz und nennt die Auftragsnummer, damit Herr Brenner die Mail sofort zuordnen kann. Variante 3 passt nur, wenn der verbindliche Termin bereits in der Mail steht.
