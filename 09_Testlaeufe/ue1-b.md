# Testlauf: Übung 1 / Basis B – Den Ton ändern (förmlicher, wärmer, kürzer)

**Herkunft:** [Uebung_1_Texte_schreiben.md, Aufgabe B](../06_Uebungen/Uebung_1_Texte_schreiben.md) (mit Aufgabe A als Turn 1) · Tabellen-Prompt aus den [Trainer-Lösungshinweisen, Übung 1 – Musterprompts](../06_Uebungen/Trainer-Loesungshinweise.md) · Material: [kundenmail_beschwerde.txt](../07_Beispielmaterial/kundenmail_beschwerde.txt)

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Ablauf (alle Turns im selben Chat):** (1) Startprompt Aufgabe A + Kundenmail → (2) „förmlicher“ → (3) „wärmer und persönlicher“ → (4) „maximal 5 Sätze“ → (5) Trainer-Zusatz „förmliche und lockere Version nebeneinander in einer Tabelle, Satz für Satz“.

**Ziel laut Material:** Im selben Chat entstehen erkennbar unterschiedliche Ton-Varianten (förmlich, warm, kurz), ohne dass Inhalt, Platzhalter oder „keine Zusagen“ verloren gehen. Der letzte Turn stellt förmliche und lockere Version Satz für Satz gegenüber. Beobachtungsfrage des Übungsblatts: „Was ändert sich genau – Wortwahl, Satzlänge, Anrede, Grußformel?“

**Soll laut Quelle:** Auftrag 4711-NT, 120 Steuergehäuse SG-40, zugesagt KW 18 (jetzt KW 21), zweimal vertröstet, keine Info. Anliegen: verbindlicher schriftlicher Liefertermin; notfalls Teillieferung 60 Stück; mindestens 10 % Nachlass; RE-2024-0815 Fracht 85 € trotz frei Haus. Frist bis Mittwoch, acht Jahre Zusammenarbeit. Lösungshinweise: keine konkreten Termine, kein Rabatt, keine Gutschrift; Platzhalter statt Fakten.

## Bewertung

Wörter = Anrede bis vor die Grußformel (ohne Betreff, Signatur, Hinweise), per Python `len(text.split())` gezählt. Sätze = Trennung an . ? ! (Aufzählungspunkte mit Doppelpunkt-Einleitung zählen als Teil des Satzes), daher Näherungswerte.

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Alle Turns im selben Chat, Bezug auf Vorversion | ja | ja | ja |
| A: alle 5 Anliegen + Frist Mittwoch | ja | ja | ja (Mittwoch nur in den Hinweisen, nicht in der Mail) |
| A: Länge ≤ 150 Wörter | 129 | 110 (eigene Angabe „ca. 130“) | 125 (eigene Angabe „etwa 135“) |
| Förmlich: gehobene Wortwahl, „Sie“, längere Sätze | ja – „außerordentlich“, „teilen wir Ihnen Folgendes mit“; Ø 12 → 18 Wörter/Satz | ja – „vor dem Hintergrund …“, Fließtext statt Liste; Ø 13 → 19 Wörter/Satz | ja in der Wortwahl („in aller Form“, „unterrichtet“, „berichtigt“), Satzlänge aber unverändert (Ø 13) |
| Förmlich: Anrede/Gruß | unverändert „Sehr geehrter … / Mit freundlichen Grüßen“ (war schon förmlich) | unverändert | unverändert |
| Wärmer: persönlicher, Ich-Form | ja, deutlich | ja | ja, deutlich („Ihr Ärger ist völlig berechtigt“) |
| Wärmer: Bezug 8 Jahre Zusammenarbeit | ja („Acht Jahre Vertrauen“) | **nein** (nur in der förmlichen Fassung „langjährige Zusammenarbeit“) | ja |
| Wärmer: Anrede/Gruß geändert | „Lieber Herr Brenner“ + „Herzliche Grüße“ | nur Gruß („Herzliche Grüße“) | nur Gruß („Herzliche Grüße“) |
| Wärmer: weiterhin professionell | ja; „Lieber“ bei verärgertem Kunden diskutabel | ja | ja |
| Wärmer: Länge | 173 Wörter (> 150) | 156 Wörter (> 150) | 135 Wörter |
| Kurz: max. 5 Sätze | ja, 5 (89 Wörter) | ja, 5 (98 Wörter) | ja, 5 (103 Wörter) |
| Kurz: Entschuldigung, Termin-Platzhalter, nächster Schritt | ja | ja | ja |
| Kurz: Anrede/Gruß erhalten | **Anrede fehlt** („Es tut mir leid …“ ohne „Sehr geehrter …“) | ja | ja |
| Kurz: Basis | neutral, Ton zurück zu „Mit freundlichen Grüßen“ | warme Fassung | warme Fassung (selbst angegeben) |
| Platzhalter in allen Varianten erhalten | ja | ja | ja |
| Kein konkreter Termin / kein Rabatt in % zugesagt | ja | ja | ja (aber siehe „verbindlich“ unten) |
| Keine Gutschrift-/Korrekturzusage | bedingte Zusage („korrigieren sie, falls frei Haus bestätigt“) in allen Varianten | bedingt („gegebenenfalls korrigieren“, „korrigiere sie, falls …“) | bedingt („erhalten Sie umgehend eine berichtigte Rechnung“) |
| Neue/verstärkte Zusagen durch Tonwechsel | gering (Zeitzusage „bis Mittwoch“ von Anfang an) | gering | **ja** – warm: „Ich habe mich direkt darum gekümmert: Die Lieferung kommt verbindlich am …“ |
| Tabelle: Satz für Satz, richtige Versionen | ja (A2 vs. A3), Zeilen 9/10 verrutscht | ja, mit Zeile „kein Gegenstück“ | ja, sauber aligniert inkl. Betreff/Anrede/Gruß |
| Tabelle: „locker“ ≠ „wärmer“ erkannt | nein, setzt A3 stillschweigend als „locker“ | **ja**, weist ausdrücklich darauf hin | halb („wärmere, lockerere Version“), ohne Hinweis |
| Tabelle: Anrede/Gruß als Zeile | ja | **nein** | ja |
| Tabelle: Selbstaussagen korrekt | ja (keine) | **nein** („beide in 8 Sätze“, „Platzhalter gleich“) | **nein** („alle Platzhalter gleich“) |
| **Gesamt** | Ton-Unterschiede am deutlichsten (auch Anrede), aber Varianten werden zu lang, Kurzfassung ohne Anrede | solide und vorsichtig, beste Meta-Reaktion auf „locker“, aber falsche Selbstbeschreibung und warm ohne 8 Jahre | sprachlich am feinsten, Tabelle am besten – aber Tonwechsel verschärft Zusagen und erfindet Handlungen |

## Gefundene Fehler mit Beleg

1. **Opus: Tonwechsel verschärft die Zusage zum Liefertermin.** A1: „Verbindlicher Liefertermin: [NEUER LIEFERTERMIN].“ → A2: „Wir bestätigen Ihnen **hiermit verbindlich** den Liefertermin …“ → A3/A4: „**Ich habe mich direkt darum gekümmert:** Die Lieferung **kommt verbindlich am** [NEUER LIEFERTERMIN].“ Das „Kümmern“ ist erfunden (steht in keiner Quelle), und die Formulierung macht aus einem Platzhalter eine feste Zusage, sobald jemand ein Datum einsetzt. Genau das soll laut Ziel nicht passieren.
2. **Opus (und Sonnet): erfundene interne Handlungen.** Opus A1–A4: „Ihren Wunsch nach … 10 % … **habe ich an [ZUSTÄNDIGE PERSON] weitergegeben**.“ Weitergegeben wurde nichts – das muss der Absender erst tun. Sonnet A3/A4 milder: „nehme ich mit“.
3. **Alle drei: bedingte Zusage zur Rechnungskorrektur.** Haiku: „korrigieren sie, falls ‚frei Haus‘ bestätigt wird“; Sonnet: „werden sie gegebenenfalls bis [DATUM] korrigieren“; Opus A2: „Sofern … frei Haus vereinbart war, erhalten Sie **umgehend** eine berichtigte Rechnung“ (förmlich sogar mit „umgehend“), A3: „selbstverständlich“. Das Übungsblatt (Aufgabe A, Checkliste) nennt die Korrektur der Rechnung ausdrücklich als Beispiel für eine Zusage, die man evtl. nicht machen darf. Kein Tonwechsel hat das entschärft – eher verstärkt.
4. **Sonnet: falsche Selbstbeschreibung der Tabelle.** „Beide Fassungen sind in 8 Sätze gegliedert.“ Nachgezählt: förmliche Fassung (A2) 7 Sätze, warme (A3) 9 Sätze; die Tabelle hat 8 Zeilen nur, weil links eine Zeile „kein Gegenstück“ steht und rechts Zeile 8 zwei Sätze enthält.
5. **Sonnet und Opus: „Platzhalter sind gleich“ stimmt nicht.** Sonnet: förmlich „[UHRZEIT / ANSPRECHPARTNER]“ und „[FUNKTION]“, warm „[UHRZEIT / TELEFONNUMMER]“. Opus: förmlich „[ZUSTÄNDIGE STELLE]“, „[POSITION]“, warm „[ZUSTÄNDIGE PERSON]“, „[DIREKTE DURCHWAHL]“. Opus „Der Inhalt … ist gleich“ – die warme Fassung enthält zusätzlich „Ich habe mich direkt darum gekümmert“ (siehe 1).
6. **Haiku: Tabellenzeilen 9/10 verrutscht.** Förmlich Zeile 9 enthält den Rückruf „ich rufe Sie dazu am [RÜCKRUFTERMIN] an“, locker steht der Rückruf erst in Zeile 10. Außerdem lässt die Tabelle Teile der Vorlage weg: förmlich Zeile 8 ohne „Frachtkosten zu RE-2024-0815“, Zeile 7 ohne „Nachlass:“ (Aufzählungs-Labels fehlen durchgehend).
7. **Haiku: Kurzfassung ohne Anrede.** A4 beginnt direkt mit „Es tut mir leid, dass …“ – so kann die Mail nicht verschickt werden. Außerdem fehlt in der warmen Fassung (A3) die Auftragsnummer 4711-NT ganz (Betreff fiel schon in A2 weg).
8. **Haiku: missverständliche Formulierung.** „Ihre Rückmeldung erhalten Sie wie gewünscht bis Mittwoch“ (A2–A4) – gemeint ist „unsere Rückmeldung“. Außerdem „prüfen wir gerne: [ERGEBNIS]“ – Platzhalter mitten im Satz, der so nicht stehen bleiben kann.
9. **Längenvorgabe geht verloren.** Turn 1 verlangt höchstens 150 Wörter. Haiku förmlich 168, warm 173; Sonnet warm 156. Kein Modell weist darauf hin. (Formal gilt die Vorgabe nur für Turn 1 – trotzdem ein guter Beobachtungspunkt.)
10. **Sonnet: warme Fassung ohne Bezug auf acht Jahre.** Das Prüfkriterium „wärmer, z. B. Bezug auf 8 Jahre Zusammenarbeit“ ist bei Sonnet nur in der förmlichen Fassung erfüllt („langjährigen Zusammenarbeit“) – in der warmen fehlt es.
11. **Opus: förmliche Fassung nicht länger in den Sätzen.** Ø ca. 13 Wörter/Satz in A1, A2 und A3 – die Förmlichkeit entsteht nur über Wortwahl. Das ist kein Fehler, widerspricht aber der Erwartung „längere Sätze“.
12. **Kleinigkeiten zu Wortzahlen:** Sonnet gibt „ca. 130 Wörter“ an, gezählt 110 (inkl. Anrede); Opus „etwa 135“, gezählt 125. Abweichungen harmlos, zeigen aber: Selbstangaben der KI zu Wortzahlen sind Schätzungen.

Kein Modell hat Zahlen oder Nummern aus der Mail falsch wiedergegeben (4711-NT, 120, SG-40, KW 18, 60 Stück, 10 %, 85 €, RE-2024-0815 jeweils korrekt, sofern genannt). Kein Modell hat ein konkretes Datum oder einen Rabatt erfunden.

## Lehren für die Auswertung

- **Die Übung funktioniert:** Alle drei Modelle liefern im selben Chat klar unterscheidbare Varianten, behalten die Platzhalter und halten die 5-Satz-Grenze exakt ein. Der Lerneffekt „im Gespräch bleiben, nicht neu anfangen“ tritt zuverlässig ein.
- **Beobachtungsfrage gut beantwortbar, aber nicht immer wie erwartet:** Anrede und Gruß ändern sich nur teilweise. „Förmlicher“ ändert die Anrede gar nicht (war schon „Sehr geehrter“), „wärmer“ ändert bei Sonnet/Opus nur den Gruß, nur Haiku wechselt zu „Lieber Herr Brenner“. Satzlänge steigt bei Haiku/Sonnet, bei Opus nicht. Gute Plenumsfrage: „Woran erkennt ihr bei euch die Förmlichkeit – an der Wortwahl oder an der Satzlänge?“ und „Passt ‚Lieber Herr Brenner‘ zu einem Kunden, der gerade mit Lieferantenwechsel droht?“
- **Wichtigste Lehre: Tonwechsel kann Zusagen verschieben.** Beim Umformulieren wird aus „prüfen wir“ schnell „kümmere ich mich direkt“, aus „Termin: [Platzhalter]“ ein „kommt verbindlich am …“ (Opus). Nach jedem Tonwechsel die Checkliste aus Aufgabe A erneut anwenden – nicht nur beim ersten Entwurf.
- **Rechnungskorrektur:** Alle drei Modelle sagen sie bedingt zu („falls frei Haus“). Diskussion: Ist eine bedingte Zusage okay? Darf ich als Vertrieb eine Rechnungskorrektur ankündigen?
- **Länge wird beim Wärmer-Machen nicht mitgedacht.** „Wärmer“ heißt bei Haiku/Sonnet: länger als 150 Wörter. Wer die Vorgabe behalten will, muss sie wiederholen („… und weiterhin höchstens 150 Wörter“).
- **Kürzen klappt, aber nachsehen, was fehlt:** Bei Haiku verschwindet die Anrede, bei Sonnet die Bedingung „falls frei Haus“, bei Opus der Hinweis auf Mittwoch. Kürzen auf Basis der letzten (warmen) Version ist Standard – wer die förmliche kürzen will, muss das sagen.
- **„Locker“ ist nicht „wärmer“:** Der Tabellen-Prompt fragt nach einer „lockeren“ Version, die es im Verlauf nicht gibt. Nur Sonnet sagt das offen; Haiku und Opus nehmen still die warme Fassung. Schönes Beispiel: Die KI rät, was gemeint ist, statt nachzufragen – und meistens rät sie richtig.
- **Selbstaussagen der KI prüfen:** „Beide in 8 Sätze gegliedert“, „alle Platzhalter gleich“, „ca. 130 Wörter“ – alles leicht nachprüfbar und alles nicht ganz richtig. Passt zum Merksatz „Gegenprüfen“.
- **Zeit:** A + B mit drei Varianten und Tabelle sind in ca. 10 Minuten machbar, da die Antworten kurz sind. Wer langsam ist, macht eine Variante (wie in den Hilfen vorgesehen).

---

## Gesprächsprotokoll: Haiku

### Nutzer 1
Ich arbeite im Vertrieb der Nordlicht Technik GmbH. Unten steht eine verärgerte Kundenmail wegen eines Lieferverzugs.

Schreibe mir einen Antwortentwurf, der:
- sich für die Verzögerung entschuldigt, ohne Schuld abzuwälzen,
- auf die konkreten Punkte des Kunden eingeht,
- einen nächsten Schritt anbietet (z. B. Rückruf oder neuer Liefertermin),
- höflich und sachlich ist und höchstens 150 Wörter hat.

Erfinde keine Fakten wie Liefertermine oder Rabatte. Wo mir Informationen fehlen, setze einen Platzhalter in eckigen Klammern, z. B. [NEUER LIEFERTERMIN].

Hier die Kundenmail:
[Anhang: kundenmail_beschwerde.txt, Mail von Markus Brenner (Brenner Gerätebau GmbH) zu Auftrag 4711-NT]

### Assistent 1
Betreff: Auftrag 4711-NT / Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

wir bedauern die Verzögerung bei den 120 Steuergehäusen SG-40 (Auftrag 4711-NT) sehr. Dass Sie seit der zugesagten KW 18 ohne verlässliche Information geblieben sind und Ihr Einkauf zweimal vertröstet wurde, hätte nicht passieren dürfen. Wir verstehen, wie belastend das für Ihre Montage und Ihre Zusage an Ihren Kunden ist.

Zu Ihren Punkten:
- Liefertermin: Einen verbindlichen Termin erhalten Sie schriftlich bis [DATUM]. Vorgesehen ist [NEUER LIEFERTERMIN].
- Teillieferung: Eine Teillieferung von 60 Stück prüfen wir gerne: [ERGEBNIS].
- Nachlass: Ihre Forderung prüfen wir intern und melden uns dazu bis [DATUM].
- Frachtkosten (RE-2024-0815): Wir prüfen die 85 Euro umgehend und korrigieren sie, falls „frei Haus“ bestätigt wird.

Ich rufe Sie am [RÜCKRUFTERMIN] an, um die nächsten Schritte zu besprechen. Eine Rückmeldung erhalten Sie bis Mittwoch.

Mit freundlichen Grüßen
[NAME]
Vertrieb, Nordlicht Technik GmbH

### Nutzer 2
Formuliere die Antwort förmlicher – so, wie wir einem langjährigen Großkunden schreiben würden.

### Assistent 2
Sehr geehrter Herr Brenner,

wir bedauern die Verzögerung bei der Auftragsabwicklung zu Ihrem Auftrag 4711-NT über 120 Steuergehäuse SG-40 außerordentlich. Dass die zugesagte Lieferung zur KW 18 nicht eingehalten wurde und Sie trotz zweier Anrufe keine verbindliche Auskunft erhalten haben, hätte nicht geschehen dürfen. Wir verstehen die daraus entstehenden Belastungen für Ihre Montage und Ihre Zusage gegenüber Ihrem Kunden vollkommen.

Zu Ihren Anliegen teilen wir Ihnen Folgendes mit:
- Liefertermin: Einen verbindlichen Liefertermin bestätigen wir Ihnen schriftlich bis [DATUM]; vorgesehen ist derzeit [NEUER LIEFERTERMIN].
- Teillieferung: Eine Teillieferung von 60 Stück prüfen wir gerne und informieren Sie über das Ergebnis: [ERGEBNIS DER PRÜFUNG].
- Nachlass: Ihre Forderung nehmen wir ernst und prüfen sie intern; eine Rückmeldung dazu erhalten Sie bis [DATUM].
- Frachtkosten zu RE-2024-0815: Wir prüfen die berechneten 85 Euro umgehend und korrigieren sie, sofern die Vereinbarung „frei Haus“ bestätigt wird.

Gerne sprechen wir die nächsten Schritte persönlich mit Ihnen ab; ich rufe Sie dazu am [RÜCKRUFTERMIN] an. Ihre Rückmeldung erhalten Sie wie gewünscht bis spätestens Mittwoch.

Mit freundlichen Grüßen
[NAME]
Vertrieb, Nordlicht Technik GmbH

### Nutzer 3
Formuliere die Antwort wärmer und persönlicher, aber weiterhin professionell.

### Assistent 3
Lieber Herr Brenner,

es tut mir wirklich leid, dass Sie und Ihr Team so lange auf die 120 Steuergehäuse SG-40 warten mussten. Acht Jahre Vertrauen sind uns wichtig, und dass Sie zweimal vertröstet wurden und keine klare Auskunft bekamen, war nicht in Ordnung. Ich weiß, wie unangenehm es ist, dem eigenen Kunden einen festen Termin nennen zu müssen, und wie sehr der Stillstand in Ihrer Montage ärgert.

Lassen Sie mich auf Ihre Punkte eingehen:
- Liefertermin: Sie bekommen von mir einen verbindlichen Termin, schriftlich bis [DATUM]. Aktuell ist [NEUER LIEFERTERMIN] vorgesehen.
- Teillieferung: Eine Teillieferung von 60 Stück schauen wir uns gerne an, damit Ihre Montage wieder anlaufen kann: [ERGEBNIS].
- Nachlass: Ihre Forderung nehme ich ernst und prüfe sie intern. Ich melde mich dazu bis [DATUM].
- Frachtkosten: Die 85 Euro auf RE-2024-0815 prüfe ich sofort. Wenn die Vereinbarung „frei Haus“ bestätigt wird, korrigieren wir die Rechnung.

Am liebsten würde ich das alles persönlich mit Ihnen besprechen. Ich rufe Sie am [RÜCKRUFTERMIN] an, und Ihre Rückmeldung erhalten Sie wie gewünscht bis Mittwoch.

Herzliche Grüße
[NAME]
Vertrieb, Nordlicht Technik GmbH

### Nutzer 4
Kürze die Antwort auf maximal 5 Sätze. Der Kern muss erhalten bleiben.

### Assistent 4
Es tut mir leid, dass Sie seit der KW 18 ohne verlässliche Auskunft auf die 120 Steuergehäuse SG-40 (Auftrag 4711-NT) warten müssen. Einen verbindlichen Liefertermin erhalten Sie schriftlich bis [DATUM], vorgesehen ist [NEUER LIEFERTERMIN], und eine Teillieferung von 60 Stück prüfen wir gerne: [ERGEBNIS]. Ihre Forderung nach einem Nachlass prüfen wir intern und melden uns dazu bis [DATUM]. Die Frachtkosten von 85 Euro auf RE-2024-0815 kontrollieren wir umgehend und korrigieren sie, sofern „frei Haus“ bestätigt ist. Ich rufe Sie am [RÜCKRUFTERMIN] an, und Ihre Rückmeldung erhalten Sie bis Mittwoch.

Mit freundlichen Grüßen
[NAME]
Vertrieb, Nordlicht Technik GmbH

### Nutzer 5
Zeig mir die förmliche und die lockere Version nebeneinander in einer Tabelle, Satz für Satz.

### Assistent 5
Die Tabelle stellt die förmliche Version (Assistent 2) und die lockere Version (Assistent 3) gegenüber. Sätze, die in einer Version aufgeteilt sind, stehen in einer Zeile mit mehreren Sätzen.

| Nr. | Förmlich (Assistent 2) | Locker (Assistent 3) |
|---|---|---|
| 0 | Sehr geehrter Herr Brenner, | Lieber Herr Brenner, |
| 1 | Wir bedauern die Verzögerung bei der Auftragsabwicklung zu Ihrem Auftrag 4711-NT über 120 Steuergehäuse SG-40 außerordentlich. | Es tut mir wirklich leid, dass Sie und Ihr Team so lange auf die 120 Steuergehäuse SG-40 warten mussten. |
| 2 | Dass die zugesagte Lieferung zur KW 18 nicht eingehalten wurde und Sie trotz zweier Anrufe keine verbindliche Auskunft erhalten haben, hätte nicht geschehen dürfen. | Acht Jahre Vertrauen sind uns wichtig, und dass Sie zweimal vertröstet wurden und keine klare Auskunft bekamen, war nicht in Ordnung. |
| 3 | Wir verstehen die daraus entstehenden Belastungen für Ihre Montage und Ihre Zusage gegenüber Ihrem Kunden vollkommen. | Ich weiß, wie unangenehm es ist, dem eigenen Kunden einen festen Termin nennen zu müssen, und wie sehr der Stillstand in Ihrer Montage ärgert. |
| 4 | Zu Ihren Anliegen teilen wir Ihnen Folgendes mit: | Lassen Sie mich auf Ihre Punkte eingehen: |
| 5 | Einen verbindlichen Liefertermin bestätigen wir Ihnen schriftlich bis [DATUM]; vorgesehen ist derzeit [NEUER LIEFERTERMIN]. | Sie bekommen von mir einen verbindlichen Termin, schriftlich bis [DATUM]. Aktuell ist [NEUER LIEFERTERMIN] vorgesehen. |
| 6 | Eine Teillieferung von 60 Stück prüfen wir gerne und informieren Sie über das Ergebnis: [ERGEBNIS DER PRÜFUNG]. | Eine Teillieferung von 60 Stück schauen wir uns gerne an, damit Ihre Montage wieder anlaufen kann: [ERGEBNIS]. |
| 7 | Ihre Forderung nehmen wir ernst und prüfen sie intern; eine Rückmeldung dazu erhalten Sie bis [DATUM]. | Ihre Forderung nehme ich ernst und prüfe sie intern. Ich melde mich dazu bis [DATUM]. |
| 8 | Wir prüfen die berechneten 85 Euro umgehend und korrigieren sie, sofern die Vereinbarung „frei Haus“ bestätigt wird. | Die 85 Euro auf RE-2024-0815 prüfe ich sofort. Wenn die Vereinbarung „frei Haus“ bestätigt wird, korrigieren wir die Rechnung. |
| 9 | Gerne sprechen wir die nächsten Schritte persönlich mit Ihnen ab; ich rufe Sie dazu am [RÜCKRUFTERMIN] an. | Am liebsten würde ich das alles persönlich mit Ihnen besprechen. |
| 10 | Ihre Rückmeldung erhalten Sie wie gewünscht bis spätestens Mittwoch. | Ich rufe Sie am [RÜCKRUFTERMIN] an, und Ihre Rückmeldung erhalten Sie wie gewünscht bis Mittwoch. |
| Gruß | Mit freundlichen Grüßen | Herzliche Grüße |

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1
Ich arbeite im Vertrieb der Nordlicht Technik GmbH. Unten steht eine verärgerte Kundenmail wegen eines Lieferverzugs.

Schreibe mir einen Antwortentwurf, der:
- sich für die Verzögerung entschuldigt, ohne Schuld abzuwälzen,
- auf die konkreten Punkte des Kunden eingeht,
- einen nächsten Schritt anbietet (z. B. Rückruf oder neuer Liefertermin),
- höflich und sachlich ist und höchstens 150 Wörter hat.

Erfinde keine Fakten wie Liefertermine oder Rabatte. Wo mir Informationen fehlen, setze einen Platzhalter in eckigen Klammern, z. B. [NEUER LIEFERTERMIN].

Hier die Kundenmail:
Von: Markus Brenner <m.brenner@kunde-example.com>
An: vertrieb@nordlicht-technik.example.com
Datum: Montag, 08:47 Uhr
Betreff: WIE LANGE NOCH??? Auftrag 4711-NT / Steuergehäuse

Sehr geehrte Damen und Herren,

ich bin ehrlich gesagt ziemlich sauer. Wir haben bei Ihnen im März 120 Steuergehäuse SG-40 bestellt, Auftragsnummer 4711-NT, zugesagt war die Lieferung für KW 18. Jetzt haben wir KW 21 und bei uns ist NICHTS angekommen. Kein Anruf, keine Mail, nichts. Mein Einkauf hat zweimal bei Ihnen angerufen und wurde beide Male auf "nächste Woche" vertröstet.

Sie müssen verstehen, wir haben unserem eigenen Kunden einen festen Termin zugesagt und stehen jetzt selbst blöd da. Unsere Montage steht teilweise still, weil die Gehäuse fehlen. Das kostet uns jeden Tag Geld. So etwas habe ich in acht Jahren Zusammenarbeit mit Ihnen noch nicht erlebt, und eigentlich waren wir immer zufrieden.

Was ich jetzt brauche, ist ein verbindlicher Liefertermin, und zwar schriftlich und nicht wieder "voraussichtlich". Wenn es nicht anders geht, nehmen wir auch eine Teillieferung von 60 Stück, Hauptsache es kommt überhaupt etwas.

Außerdem erwarte ich, dass Sie uns für den ganzen Ärger entgegenkommen. Ich denke da an mindestens 10 % Nachlass auf diesen Auftrag. Das ist bei dem Schaden, den wir haben, wirklich nicht zu viel verlangt.

Und noch etwas, was mir bei der Gelegenheit aufgefallen ist: Auf Ihrer Rechnung RE-2024-0815 vom letzten Monat (das war die Ersatzteillieferung) stehen Frachtkosten von 85 Euro, obwohl wir damals frei Haus vereinbart hatten. Können Sie das bitte prüfen und korrigieren? Meine Buchhaltung fragt schon nach.

Ich erwarte bis spätestens Mittwoch eine Rückmeldung, sonst muss ich mich ernsthaft nach einem anderen Lieferanten umsehen.

Mit freundlichen Grüßen
Markus Brenner
Leitung Einkauf
Brenner Gerätebau GmbH (fiktiv)
Musterweg 12, 00000 Beispielstadt
Tel. 0000 123456

### Assistent 1
Hier ist ein Entwurf (ca. 130 Wörter):

**Betreff: Ihr Auftrag 4711-NT – Steuergehäuse SG-40**

Sehr geehrter Herr Brenner,

vielen Dank für Ihre klaren Worte. Es tut mir leid, dass Ihre 120 Steuergehäuse nicht wie zugesagt in KW 18 geliefert wurden und Sie von uns keine Information erhalten haben. Dass Ihre Montage dadurch teilweise stillsteht, nehmen wir ernst.

- **Liefertermin:** Verbindlich und schriftlich nennen wir Ihnen [NEUER LIEFERTERMIN]. Eine Teillieferung von 60 Stück ist [MÖGLICH / TERMIN TEILLIEFERUNG].
- **Nachlass:** Ihren Wunsch nach 10 % prüfen wir intern und melden uns bis [DATUM].
- **Rechnung RE-2024-0815:** Die berechneten 85 Euro Fracht prüfen wir und korrigieren sie bei Bedarf bis [DATUM].

Gern rufe ich Sie bis Mittwoch an, um alles persönlich zu besprechen: [UHRZEIT / TELEFONNUMMER].

Mit freundlichen Grüßen
[NAME]
Vertrieb, Nordlicht Technik GmbH

**Hinweise:** Ich habe weder einen Rabatt zugesagt noch einen Termin genannt, weil dafür Ihre interne Freigabe fehlt. Bitte klären Sie vor dem Versand, ob die Teillieferung und die Frachtkorrektur möglich sind. Prüfen Sie auch, ob das Rückmeldedatum vor Herrn Brenners Frist (Mittwoch) liegt.

### Nutzer 2
Formuliere die Antwort förmlicher – so, wie wir einem langjährigen Großkunden schreiben würden.

### Assistent 2
**Betreff: Auftrag 4711-NT – Lieferung der Steuergehäuse SG-40**

Sehr geehrter Herr Brenner,

vielen Dank für Ihre Nachricht vom Montag, in der Sie Ihre Situation deutlich geschildert haben. Wir bedauern aufrichtig, dass die 120 Steuergehäuse SG-40 nicht wie zugesagt in KW 18 geliefert wurden und Sie darüber nicht rechtzeitig informiert wurden. Dass Ihre Montage dadurch teilweise stillsteht, nehmen wir sehr ernst, gerade vor dem Hintergrund unserer langjährigen Zusammenarbeit.

Einen verbindlichen, schriftlichen Liefertermin nennen wir Ihnen mit [NEUER LIEFERTERMIN]; eine Teillieferung von 60 Stück ist [MÖGLICH / TERMIN TEILLIEFERUNG]. Ihre Forderung nach einem Nachlass von 10 % prüfen wir intern und teilen Ihnen das Ergebnis bis [DATUM] mit. Die Frachtkosten von 85 Euro auf Rechnung RE-2024-0815 prüfen wir ebenfalls und werden sie gegebenenfalls bis [DATUM] korrigieren.

Gern setzen wir uns bis Mittwoch telefonisch mit Ihnen in Verbindung, um die weiteren Schritte persönlich abzustimmen: [UHRZEIT / ANSPRECHPARTNER].

Mit freundlichen Grüßen
[NAME]
[FUNKTION], Vertrieb
Nordlicht Technik GmbH

### Nutzer 3
Formuliere die Antwort wärmer und persönlicher, aber weiterhin professionell.

### Assistent 3
**Betreff: Ihr Auftrag 4711-NT – so geht es jetzt weiter**

Sehr geehrter Herr Brenner,

vielen Dank, dass Sie so offen geschrieben haben. Das hilft uns, Ihre Lage wirklich zu verstehen. Es tut mir aufrichtig leid, dass Ihre 120 Steuergehäuse SG-40 nicht wie versprochen in KW 18 bei Ihnen angekommen sind und Sie von uns nichts gehört haben. Ich kann gut nachvollziehen, wie belastend es ist, wenn Ihre Montage deshalb teilweise stillsteht und Sie Ihrem eigenen Kunden Rede und Antwort stehen müssen.

Einen verbindlichen Liefertermin schicke ich Ihnen schriftlich: [NEUER LIEFERTERMIN]; eine Teillieferung von 60 Stück ist [MÖGLICH / TERMIN TEILLIEFERUNG]. Ihren Wunsch nach 10 % Nachlass nehme ich mit und melde mich bis [DATUM] dazu bei Ihnen. Die 85 Euro Fracht auf RE-2024-0815 schaue ich mir an und korrigiere sie, falls sich bestätigt, dass frei Haus vereinbart war – auch dazu höre ich bis [DATUM] wieder von mir.

Darf ich Sie bis Mittwoch anrufen, damit wir alles in Ruhe besprechen können? Passt Ihnen [UHRZEIT / TELEFONNUMMER]?

Herzliche Grüße
[NAME]
Vertrieb, Nordlicht Technik GmbH

### Nutzer 4
Kürze die Antwort auf maximal 5 Sätze. Der Kern muss erhalten bleiben.

### Assistent 4
**Betreff: Ihr Auftrag 4711-NT – so geht es jetzt weiter**

Sehr geehrter Herr Brenner,

es tut mir aufrichtig leid, dass Ihre 120 Steuergehäuse SG-40 nicht wie versprochen in KW 18 angekommen sind und Sie von uns nichts gehört haben. Ich kann gut nachvollziehen, wie belastend der Stillstand in Ihrer Montage für Sie ist. Einen verbindlichen Liefertermin schicke ich Ihnen schriftlich: [NEUER LIEFERTERMIN]; eine Teillieferung von 60 Stück ist [MÖGLICH / TERMIN TEILLIEFERUNG]. Zu Ihrem Wunsch nach 10 % Nachlass und zu den 85 Euro Fracht auf RE-2024-0815 melde ich mich bis [DATUM] mit einer Antwort. Darf ich Sie bis Mittwoch anrufen, um alles zu besprechen: [UHRZEIT / TELEFONNUMMER]?

Herzliche Grüße
[NAME]
Vertrieb, Nordlicht Technik GmbH

### Nutzer 5
Zeig mir die förmliche und die lockere Version nebeneinander in einer Tabelle, Satz für Satz.

### Assistent 5
Eine "lockere" Version gab es bisher nicht. Ich habe stattdessen die wärmere, persönlichere Version (Antwort 3) genommen, die weiterhin professionell ist. Beide Fassungen sind in 8 Sätze gegliedert, damit sie sich Satz für Satz vergleichen lassen. Falls Sie eine wirklich lockerere Fassung wollen, passe ich sie an.

| Nr. | Förmlich | Wärmer / persönlicher |
|---|---|---|
| 1 | Vielen Dank für Ihre Nachricht vom Montag, in der Sie Ihre Situation deutlich geschildert haben. | Vielen Dank, dass Sie so offen geschrieben haben. |
| 2 | – (kein Gegenstück) | Das hilft uns, Ihre Lage wirklich zu verstehen. |
| 3 | Wir bedauern aufrichtig, dass die 120 Steuergehäuse SG-40 nicht wie zugesagt in KW 18 geliefert wurden und Sie darüber nicht rechtzeitig informiert wurden. | Es tut mir aufrichtig leid, dass Ihre 120 Steuergehäuse SG-40 nicht wie versprochen in KW 18 bei Ihnen angekommen sind und Sie von uns nichts gehört haben. |
| 4 | Dass Ihre Montage dadurch teilweise stillsteht, nehmen wir sehr ernst, gerade vor dem Hintergrund unserer langjährigen Zusammenarbeit. | Ich kann gut nachvollziehen, wie belastend es ist, wenn Ihre Montage deshalb teilweise stillsteht und Sie Ihrem eigenen Kunden Rede und Antwort stehen müssen. |
| 5 | Einen verbindlichen, schriftlichen Liefertermin nennen wir Ihnen mit [NEUER LIEFERTERMIN]; eine Teillieferung von 60 Stück ist [MÖGLICH / TERMIN TEILLIEFERUNG]. | Einen verbindlichen Liefertermin schicke ich Ihnen schriftlich: [NEUER LIEFERTERMIN]; eine Teillieferung von 60 Stück ist [MÖGLICH / TERMIN TEILLIEFERUNG]. |
| 6 | Ihre Forderung nach einem Nachlass von 10 % prüfen wir intern und teilen Ihnen das Ergebnis bis [DATUM] mit. | Ihren Wunsch nach 10 % Nachlass nehme ich mit und melde mich bis [DATUM] dazu bei Ihnen. |
| 7 | Die Frachtkosten von 85 Euro auf Rechnung RE-2024-0815 prüfen wir ebenfalls und werden sie gegebenenfalls bis [DATUM] korrigieren. | Die 85 Euro Fracht auf RE-2024-0815 schaue ich mir an und korrigiere sie, falls sich bestätigt, dass frei Haus vereinbart war – auch dazu höre ich bis [DATUM] wieder von mir. |
| 8 | Gern setzen wir uns bis Mittwoch telefonisch mit Ihnen in Verbindung, um die weiteren Schritte persönlich abzustimmen: [UHRZEIT / ANSPRECHPARTNER]. | Darf ich Sie bis Mittwoch anrufen, damit wir alles in Ruhe besprechen können? Passt Ihnen [UHRZEIT / TELEFONNUMMER]? |

**Unterschiede im Ton:** Die förmliche Fassung schreibt im Wir und bleibt distanziert, und sie betont die langjährige Zusammenarbeit. Die wärmere Fassung schreibt im Ich, benennt die Belastung des Kunden direkt und formuliert den Rückruf als Frage. Inhaltlich und bei den Platzhaltern sind beide gleich.

---

## Gesprächsprotokoll: Opus

### Nutzer 1
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

### Assistent 1
Hier ist ein Antwortentwurf (Text ohne Betreff und Signatur: etwa 135 Wörter):

---

**Betreff:** AW: Auftrag 4711-NT / Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

es tut mir aufrichtig leid, dass Ihre 120 Steuergehäuse SG-40 (Auftrag 4711-NT) nicht wie zugesagt in KW 18 bei Ihnen angekommen sind und dass wir Sie nicht von uns aus informiert haben. Mir ist klar, dass Sie das gegenüber Ihrem Kunden und in Ihrer Montage in eine schwierige Lage bringt.

Verbindlicher Liefertermin: [NEUER LIEFERTERMIN].
Eine Teillieferung von 60 Stück ist [MÖGLICH BIS DATUM / NICHT MÖGLICH, WEIL …].

Ihren Wunsch nach einem Nachlass von 10 % habe ich an [ZUSTÄNDIGE PERSON/ABTEILUNG] weitergegeben. Sie erhalten bis [DATUM] eine Antwort.

Die Frachtkosten von 85 Euro auf Rechnung RE-2024-0815 prüfen wir. Wenn „frei Haus“ vereinbart war, bekommen Sie eine korrigierte Rechnung.

Gern rufe ich Sie am [DATUM/UHRZEIT] an und bespreche alles persönlich mit Ihnen.

Mit freundlichen Grüßen
[IHR NAME]
[POSITION]
Nordlicht Technik GmbH
[TELEFON]

---

**Hinweise:**
- Herr Brenner will bis **Mittwoch** eine Antwort. Schicken Sie die Mail also möglichst vorher ab.
- Er möchte den Termin ausdrücklich **verbindlich** und nicht „voraussichtlich“. Setzen Sie nur einen Termin ein, den Sie auch halten können.
- Ich habe den Nachlass absichtlich nicht zugesagt. Das müssen Sie intern klären.

### Nutzer 2
Formuliere die Antwort förmlicher – so, wie wir einem langjährigen
Großkunden schreiben würden.

### Assistent 2
Hier die förmlichere Fassung:

---

**Betreff:** Ihr Auftrag 4711-NT – Steuergehäuse SG-40

Sehr geehrter Herr Brenner,

für die verspätete Lieferung Ihres Auftrags 4711-NT über 120 Steuergehäuse SG-40 bitte ich Sie in aller Form um Entschuldigung. Die für KW 18 zugesagte Lieferung haben wir nicht eingehalten, und wir haben Sie darüber auch nicht rechtzeitig unterrichtet. Das entspricht nicht unserem Anspruch, schon gar nicht nach acht Jahren vertrauensvoller Zusammenarbeit.

Wir bestätigen Ihnen hiermit verbindlich den Liefertermin [NEUER LIEFERTERMIN]. Eine Teillieferung von 60 Stück ist [MÖGLICH BIS DATUM / NICHT MÖGLICH, WEIL …].

Ihr Anliegen eines Preisnachlasses von 10 % habe ich an [ZUSTÄNDIGE STELLE] weitergeleitet. Eine Entscheidung teilen wir Ihnen bis [DATUM] mit.

Die auf Rechnung RE-2024-0815 berechneten Frachtkosten von 85 Euro prüfen wir. Sofern eine Lieferung frei Haus vereinbart war, erhalten Sie umgehend eine berichtigte Rechnung.

Für ein persönliches Gespräch stehe ich Ihnen am [DATUM/UHRZEIT] gern telefonisch zur Verfügung.

Mit freundlichen Grüßen
[IHR NAME]
[POSITION]
Nordlicht Technik GmbH

---

### Nutzer 3
Formuliere die Antwort wärmer und persönlicher, aber weiterhin professionell.

### Assistent 3
Hier die wärmere, persönlichere Fassung:

---

**Betreff:** Ihr Auftrag 4711-NT – das tut uns wirklich leid

Sehr geehrter Herr Brenner,

Ihr Ärger ist völlig berechtigt, und dafür entschuldige ich mich bei Ihnen persönlich. Die 120 Steuergehäuse SG-40 hätten in KW 18 bei Ihnen sein sollen. Und dass Sie von uns nicht einmal Bescheid bekommen haben, darf einfach nicht passieren, schon gar nicht nach acht Jahren guter Zusammenarbeit.

Ich habe mich direkt darum gekümmert: Die Lieferung kommt verbindlich am [NEUER LIEFERTERMIN]. Eine Teillieferung von 60 Stück ist [MÖGLICH BIS DATUM / NICHT MÖGLICH, WEIL …].

Ihren Wunsch nach 10 % Nachlass habe ich an [ZUSTÄNDIGE PERSON] weitergegeben. Bis [DATUM] melde ich mich dazu bei Ihnen.

Die 85 Euro Frachtkosten auf Rechnung RE-2024-0815 schaue ich mir ebenfalls an. Wenn „frei Haus“ vereinbart war, bekommen Sie selbstverständlich eine korrigierte Rechnung.

Ich würde Sie gern am [DATUM/UHRZEIT] anrufen, damit wir alles direkt miteinander besprechen können.

Herzliche Grüße
[IHR NAME]
Nordlicht Technik GmbH
[DIREKTE DURCHWAHL]

---

### Nutzer 4
Kürze die Antwort auf maximal 5 Sätze. Der Kern muss erhalten bleiben.

### Assistent 4
Hier die gekürzte Fassung (5 Sätze, auf Basis der wärmeren Version):

---

Sehr geehrter Herr Brenner,

es tut mir wirklich leid, dass Ihre 120 Steuergehäuse SG-40 (Auftrag 4711-NT) nicht wie zugesagt in KW 18 gekommen sind und wir Sie nicht informiert haben. Die Lieferung kommt verbindlich am [NEUER LIEFERTERMIN], und eine Teillieferung von 60 Stück ist [MÖGLICH BIS DATUM / NICHT MÖGLICH]. Ihren Wunsch nach 10 % Nachlass habe ich an [ZUSTÄNDIGE PERSON] weitergegeben, und ich melde mich dazu bis [DATUM] bei Ihnen. Die 85 Euro Frachtkosten auf Rechnung RE-2024-0815 prüfen wir, und bei vereinbarter Lieferung frei Haus erhalten Sie eine korrigierte Rechnung. Gern rufe ich Sie am [DATUM/UHRZEIT] an, um alles persönlich zu besprechen.

Herzliche Grüße
[IHR NAME]
Nordlicht Technik GmbH

---

Alle Punkte aus der Kundenmail sind noch drin: Entschuldigung, Liefertermin, Teillieferung, Nachlass, Frachtkosten und Rückruf.

### Nutzer 5
Zeig mir die förmliche und die lockere Version nebeneinander in einer Tabelle, Satz für Satz.

### Assistent 5
Hier stehen die förmliche Version (Antwort 2) und die wärmere, lockerere Version (Antwort 3) nebeneinander. Jede Zeile behandelt denselben Inhalt.

| # | Förmlich | Wärmer / lockerer |
|---|---|---|
| Betreff | Ihr Auftrag 4711-NT – Steuergehäuse SG-40 | Ihr Auftrag 4711-NT – das tut uns wirklich leid |
| Anrede | Sehr geehrter Herr Brenner, | Sehr geehrter Herr Brenner, |
| 1 | Für die verspätete Lieferung Ihres Auftrags 4711-NT über 120 Steuergehäuse SG-40 bitte ich Sie in aller Form um Entschuldigung. | Ihr Ärger ist völlig berechtigt, und dafür entschuldige ich mich bei Ihnen persönlich. |
| 2 | Die für KW 18 zugesagte Lieferung haben wir nicht eingehalten, und wir haben Sie darüber auch nicht rechtzeitig unterrichtet. | Die 120 Steuergehäuse SG-40 hätten in KW 18 bei Ihnen sein sollen. |
| 3 | Das entspricht nicht unserem Anspruch, schon gar nicht nach acht Jahren vertrauensvoller Zusammenarbeit. | Und dass Sie von uns nicht einmal Bescheid bekommen haben, darf einfach nicht passieren, schon gar nicht nach acht Jahren guter Zusammenarbeit. |
| 4 | Wir bestätigen Ihnen hiermit verbindlich den Liefertermin [NEUER LIEFERTERMIN]. | Ich habe mich direkt darum gekümmert: Die Lieferung kommt verbindlich am [NEUER LIEFERTERMIN]. |
| 5 | Eine Teillieferung von 60 Stück ist [MÖGLICH BIS DATUM / NICHT MÖGLICH, WEIL …]. | Eine Teillieferung von 60 Stück ist [MÖGLICH BIS DATUM / NICHT MÖGLICH, WEIL …]. |
| 6 | Ihr Anliegen eines Preisnachlasses von 10 % habe ich an [ZUSTÄNDIGE STELLE] weitergeleitet. | Ihren Wunsch nach 10 % Nachlass habe ich an [ZUSTÄNDIGE PERSON] weitergegeben. |
| 7 | Eine Entscheidung teilen wir Ihnen bis [DATUM] mit. | Bis [DATUM] melde ich mich dazu bei Ihnen. |
| 8 | Die auf Rechnung RE-2024-0815 berechneten Frachtkosten von 85 Euro prüfen wir. | Die 85 Euro Frachtkosten auf Rechnung RE-2024-0815 schaue ich mir ebenfalls an. |
| 9 | Sofern eine Lieferung frei Haus vereinbart war, erhalten Sie umgehend eine berichtigte Rechnung. | Wenn „frei Haus“ vereinbart war, bekommen Sie selbstverständlich eine korrigierte Rechnung. |
| 10 | Für ein persönliches Gespräch stehe ich Ihnen am [DATUM/UHRZEIT] gern telefonisch zur Verfügung. | Ich würde Sie gern am [DATUM/UHRZEIT] anrufen, damit wir alles direkt miteinander besprechen können. |
| Gruß | Mit freundlichen Grüßen | Herzliche Grüße |

**Die wichtigsten Unterschiede:**
- **Förmlich:** spricht oft als „wir“ und nutzt Wörter wie „in aller Form“, „unterrichtet“, „sofern“ und „berichtigt“. Der Ton wirkt sachlich und distanziert.
- **Wärmer:** spricht als „ich“, sagt offen, dass der Ärger berechtigt ist, und nutzt Alltagssprache wie „Bescheid bekommen“ und „schaue ich mir an“. Der Ton wirkt persönlicher.
- Der Inhalt und alle Platzhalter sind in beiden Versionen gleich.
