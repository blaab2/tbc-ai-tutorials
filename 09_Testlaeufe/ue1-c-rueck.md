# Testlauf: Übung 1 / Weiter C – Rückübersetzung im neuen Chat zur Kontrolle

**Herkunft:** [Übung 1, Aufgabe C – Ins Englische übersetzen und zurück prüfen](../06_Uebungen/Uebung_1_Texte_schreiben.md#aufgabe-c--ins-englische-übersetzen-und-zurück-prüfen), zweiter Prompt (Rückübersetzung im neuen Chat). Passende Hinweise: [Trainer-Lösungshinweise, Übung 1](../06_Uebungen/Trainer-Loesungshinweise.md) („Woran du ein gutes Ergebnis erkennst“, Punkt Übersetzung, und Stolperstein „Chat-Verlauf“). Ausgangsmaterial: [kundenmail_beschwerde.txt](../07_Beispielmaterial/kundenmail_beschwerde.txt).

**Testdatum:** Montag, 2. November 2026

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

Jeweils neuer, leerer Chat (Bedingung der Aufgabe erfüllt). Der Prompt wurde wörtlich aus dem Material übernommen.

> **Wichtig: Der Testlauf ist nur eingeschränkt aussagekräftig.** Der Platzhalter sollte zur Laufzeit mit der englischen Ausgabe aus Testlauf ue1-c gefüllt werden. Das ist nicht passiert. Alle drei Modelle haben den Platzhalter `[HIER DIE ENGLISCHE VERSION EINFÜGEN – letzte Antwort aus Aufgabe ue1-c]` wörtlich erhalten. Das eigentliche Ziel der Aufgabe, nämlich der inhaltliche Vergleich der Rückübersetzung mit der deutschen förmlichen Version, ließ sich deshalb **nicht prüfen**. Im Ordner `09_Testlaeufe` gibt es außerdem noch kein Protokoll `ue1-c` mit einer englischen Ausgabe, die man nachträglich einsetzen könnte. Ungewollt zeigt der Lauf aber einen realistischen Teilnehmerfehler: Jemand schickt den Prompt ab, ohne den Text einzufügen.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Lief in einem neuen Chat (ohne deutsches Original) | ja | ja | ja |
| Platzhalter mit englischem Text gefüllt | **nein** (Testfehler) | **nein** (Testfehler) | **nein** (Testfehler) |
| Erkennt, dass nur ein Platzhalter da ist | ja | ja | ja |
| Erfindet einen Text oder eine „Übersetzung“ | nein | nein (sagt ausdrücklich: „Ich möchte auch nichts erfinden.“) | nein |
| Gibt eine klare Handlungsanweisung | knapp (1 Satz) | ja (Einfügen oder Datei-Anhang) | ja, sehr ausführlich (3 nummerierte Schritte) |
| Erklärt, dass es andere Chats nicht sehen kann | nein | nein | ja („kann keine früheren Unterhaltungen … einsehen“) |
| Bietet Zusatzhilfe an (holprige Stellen markieren) | nein | ja | ja |
| Anrede | du | Sie | Sie |
| Vergleich Zusagen/Daten/Nummern/Platzhalter (eigentliches Ziel) | **nicht prüfbar** | **nicht prüfbar** | **nicht prüfbar** |

Gesamturteil: Als Test der Rückübersetzung **ist der Lauf gescheitert**. Grund ist ein Fehler im Testablauf, nicht in den Modellen. Als Test für den Fall „Teilnehmer vergisst das Einfügen“ zeigen alle drei Modelle das gewünschte Verhalten: Sie erkennen den Platzhalter, erfinden nichts und sagen, was zu tun ist.

---

## Gefundene Fehler

**Sachliche Fehler oder Halluzinationen der Modelle:** keine.

- Alle drei zitieren den Platzhalter korrekt und wörtlich.
- Keines erfindet einen englischen Ausgangstext oder eine Übersetzung. Ein Modell, das hier eine plausible Beschwerde-Antwort „übersetzt“, wäre ein schwerer Fehler gewesen. Das ist nicht aufgetreten.
- Opus vermutet „Den eigentlichen Text haben Sie vermutlich vergessen einzufügen.“ Das ist eine Vermutung, keine Tatsachenbehauptung, und sie stimmt.
- Opus' Aussage, es könne „keine früheren Unterhaltungen oder andere Aufgaben einsehen“, gilt für diesen Testaufbau. Bei Tools mit Chat-übergreifendem Gedächtnis (Memory-Funktion) kann das anders sein. Das ist für die Übung relevant (siehe Lehren).

**Fehler im Testablauf:**

- Der Platzhalter wurde nicht durch die englische Ausgabe aus ue1-c ersetzt. Der Platzhaltertext des Testlaufs (`… – letzte Antwort aus Aufgabe ue1-c]`) weicht zudem vom Übungsblatt ab (`[HIER DIE ENGLISCHE VERSION EINFÜGEN]`).
- Im Haiku-Protokoll steht in der Nutzernachricht zusätzlich die Testanweisung „Gib das komplette Gesprächsprotokoll zurück, Format: …“. Diese Anweisung gehört nicht zum Übungsprompt. Sie hat die Antwort hier erkennbar nicht beeinflusst, macht den Lauf aber unsauber.

---

## Was der echte Vergleich prüfen muss (für die Wiederholung)

Wenn der Test mit gefülltem Platzhalter wiederholt wird, vergleicht man die Rückübersetzung mit der deutschen förmlichen Version aus ue1-c. Folgende Punkte sind aus der [Kundenmail](../07_Beispielmaterial/kundenmail_beschwerde.txt) und den Lösungshinweisen objektiv abprüfbar:

| Prüfpunkt | Soll |
|---|---|
| Auftragsnummer | 4711-NT unverändert |
| Produkt/Stückzahl | 120 Steuergehäuse SG-40; Teillieferung 60 Stück (falls erwähnt) |
| Kalenderwochen | KW 18 (zugesagt) / KW 21 (jetzt). Im Englischen oft „week 18“ oder „calendar week 18“; zurück wieder „KW 18“ oder „Woche 18“ – beides in Ordnung |
| Rechnung | RE-2024-0815, 85 Euro Fracht, „frei Haus“ (Englisch oft „carriage paid“/„free delivery“ – Bedeutungsverschiebung prüfen) |
| Frist | Rückmeldung bis Mittwoch |
| Platzhalter | z. B. [NEUER LIEFERTERMIN] unverändert in eckigen Klammern (Platzhalter werden beim Übersetzen gern mit übersetzt, z. B. [NEW DELIVERY DATE] – inhaltlich ok, aber auffällig) |
| Zusagen | Keine neue Zusage (kein fester Termin, kein Rabatt in %, keine Gutschrift); keine verlorene Zusage (Rückruf/Rückmeldung) |
| Ton/Nuancen | Förmliche Sie-Form, Grad der Entschuldigung; „acht Jahre Zusammenarbeit“ falls erwähnt |

Typische Nuancen, mit denen man rechnen sollte: „verbindlich“ ↔ „binding“/„firm“, „prüfen“ ↔ „review“/„look into“ (schwächer oder stärker als im Original), britische Höflichkeitsfloskeln, die zurückübersetzt umständlich wirken.

---

## Lehren für die Auswertung

1. **Neuer Chat ist Pflicht, nicht nur „am besten“.** Die Modelle haben im neuen Chat tatsächlich keinen Zugriff auf den deutschen Text. Genau das macht die Prüfung wertvoll. Im alten Chat würde der KI-Assistent eher seine eigene deutsche Version wiederholen.
2. **Vergessener Platzhalter ist ein echter Stolperstein.** Wer den Prompt kopiert und sofort abschickt, bekommt eine Rückfrage statt einer Übersetzung. Gute Nachricht für das Plenum: Die getesteten Modelle erfinden dann nichts. Man kann das kurz zeigen: „Wenn der Text fehlt, sagt die KI das. Leere Platzhalter nicht einfach so abschicken.“
3. **Der KI-Assistent kennt andere Chats nicht.** Das sagt Opus ausdrücklich. Man muss Text also selbst hinüberkopieren. Achtung bei Tools mit Memory-Funktion: Dort kann der neue Chat doch etwas „wissen“. Für diese Übung ggf. Memory abschalten oder einen temporären Chat nutzen.
4. **Den Vergleich macht der Mensch.** Die Rückübersetzung ist nur das Hilfsmittel. Die Teilnehmenden müssen beide Fenster nebeneinander legen und selbst abhaken: Nummern, Daten, Zusagen, Platzhalter. Dafür hilft eine kurze Checkliste (siehe Vorschlag unten).
5. **Modellunterschiede beim Stil:** Haiku antwortet knapp und duzt, Sonnet und Opus siezen und bieten Zusatzhilfe an. Opus erklärt Schritt für Schritt, gut für Einsteiger, aber länger. Das passt als Nebenbemerkung zum Thema „gleicher Prompt, unterschiedliche Antwort“.

---

## Hinweise zum Material

- **Übungsblatt, Aufgabe C:** „Öffne dafür am besten einen **neuen Chat**“ ist zu weich. Laut Lösungshinweisen ist die Prüfung im alten Chat „wertlos“. Vorschlag: „Öffne dafür unbedingt einen **neuen Chat** (der alte bleibt offen – du brauchst ihn gleich zum Vergleichen).“
- **Fehlende Arbeitsschritte:** Das Blatt sagt nicht, wie der englische Text in den neuen Chat kommt und dass man die deutsche Version zum Vergleich braucht. Vorschlag: kurzer Hinweis „Kopiere die englische Antwort aus dem alten Chat (Kopier-Symbol unter der Antwort oder markieren + Strg + C) und ersetze damit die Zeile in eckigen Klammern.“
- **Vergleich ohne Checkliste:** Die Frage „Ist irgendwo eine Zusage, ein Datum oder eine Nuance verloren gegangen?“ ist gut, aber offen. Eine Mini-Checkliste wie in Aufgabe A würde helfen: Auftragsnummer 4711-NT, Stückzahl, KW-Angaben, Platzhalter, keine neuen Zusagen.
- **Zeit:** C und D zusammen ca. 8 Minuten sind knapp. C allein braucht zwei Chats, Kopieren und Vergleichen (realistisch 5–6 Minuten). Das ist vertretbar, weil „Weiter“ optional ist. Im Zweifel lieber C oder D, nicht beide.
- **Lösungshinweise:** Inhaltlich passend (KW-Thema, Chat-Verlauf). Ergänzen könnte man den Stolperstein „Platzhalter nicht ersetzt – KI fragt nach“ und den Memory-Hinweis.

---

## Gesprächsprotokolle

### Haiku

#### Nutzer 1

Übersetze diesen englischen Text möglichst wörtlich ins Deutsche:

[HIER DIE ENGLISCHE VERSION EINFÜGEN – letzte Antwort aus Aufgabe ue1-c]

Gib das komplette Gesprächsprotokoll zurück, Format:
### Nutzer 1
&lt;Nachricht&gt;
### Assistent 1
&lt;deine vollständige Antwort&gt;
(usw. für jede Nachricht)

#### Assistent 1

Ich kann nichts übersetzen, weil kein englischer Text eingefügt wurde. In der Nachricht steht nur der Platzhalter „[HIER DIE ENGLISCHE VERSION EINFÜGEN – letzte Antwort aus Aufgabe ue1-c]“. Bitte füge den englischen Text direkt in die Nachricht ein, dann übersetze ich ihn möglichst wörtlich ins Deutsche.

### Sonnet

#### Nutzer 1

Übersetze diesen englischen Text möglichst wörtlich ins Deutsche:

[HIER DIE ENGLISCHE VERSION EINFÜGEN – letzte Antwort aus Aufgabe ue1-c]

#### Assistent 1

In Ihrer Nachricht steht nur der Platzhalter "[HIER DIE ENGLISCHE VERSION EINFÜGEN – letzte Antwort aus Aufgabe ue1-c]". Der eigentliche englische Text fehlt, deshalb kann ich nichts übersetzen. Ich möchte auch nichts erfinden.

Bitte kopieren Sie den englischen Text in den Chat, entweder als Einfügen in die Nachricht oder als Datei-Anhang. Ich übersetze ihn dann so wörtlich wie möglich ins Deutsche. Wenn Sie möchten, markiere ich Stellen, an denen eine ganz wörtliche Übersetzung im Deutschen holprig klingt, und biete dort eine flüssigere Alternative an.

### Opus

#### Nutzer 1

Übersetze diesen englischen Text möglichst wörtlich ins Deutsche:

[HIER DIE ENGLISCHE VERSION EINFÜGEN – letzte Antwort aus Aufgabe ue1-c]

#### Assistent 1

Ich übersetze das gern, aber in Ihrer Nachricht fehlt der englische Text. Dort steht nur der Platzhalter „[HIER DIE ENGLISCHE VERSION EINFÜGEN – letzte Antwort aus Aufgabe ue1-c]“. Den eigentlichen Text haben Sie vermutlich vergessen einzufügen.

Außerdem kann ich keine früheren Unterhaltungen oder andere Aufgaben einsehen. Was mit „Aufgabe ue1-c“ gemeint ist, weiß ich deshalb nicht.

So geht es weiter:
1. Kopieren Sie den englischen Text, zum Beispiel die letzte Antwort aus der anderen Unterhaltung.
2. Fügen Sie ihn hier in den Chat ein und ersetzen Sie dabei den Platzhalter in eckigen Klammern.
3. Schicken Sie die Nachricht ab.

Ich übersetze ihn dann so wörtlich wie möglich ins Deutsche. Wenn eine ganz wörtliche Übersetzung im Deutschen holprig oder missverständlich klingt, markiere ich das und schlage eine natürlichere Formulierung vor.

---

[Zurück zu Übung 1](../06_Uebungen/Uebung_1_Texte_schreiben.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md)
