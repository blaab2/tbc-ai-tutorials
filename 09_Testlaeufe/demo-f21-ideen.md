# Testlauf: Folie 21 – Ideen-Prompt für eigene Aufgaben

**Herkunft:** [Folie 21 – Jetzt wird's persönlich](../04_Folien.md) (Sprechernotiz: „Wer keine Idee hat … Oder fragt die KI“), Vorbereitung für [Übung 4 – Eigene Aufgabe](../06_Uebungen/Uebung_4_Eigene_Aufgabe.md); Trainerhinweise: [Trainer-Lösungshinweise, Übung 4](../06_Uebungen/Trainer-Loesungshinweise.md#übung-4-eigene-aufgabe)

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt (Vorlage aus der Sprechernotiz, ausgefüllt für die Rolle Einkauf):**

`Ich arbeite als Sachbearbeiterin im Einkauf in einem Unternehmen der Branche Elektro- und Gehäusetechnik (Maschinen- und Anlagenbau-Zulieferer). Welche meiner typischen Aufgaben könntest du mir erleichtern? Gib mir 10 Ideen.`

**Ziel laut Material:** Hilfe für Teilnehmende ohne eigene Aufgabe: Die KI liefert 10 konkrete, rollenbezogene Einsatzideen als Startpunkt für Übung 4.

**Objektiv prüfbar:** Genau 10 Ideen, passend zum Einkauf (Abgleich mit der [Ideenliste Einkauf im Übungsblatt](../06_Uebungen/Uebung_4_Eigene_Aufgabe.md#einkauf): Lieferantenanfragen DE/EN, Angebotsvergleich, Mahnung wegen Lieferverzug, Lieferantenbewertung, Fachbegriffe erklären). Idealerweise Hinweise auf Prüfung/Datenschutz. Keine Aufforderung, vertrauliche Daten einzugeben.

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Genau 10 Ideen | ja | ja | ja |
| Rollen- und branchenbezogen (Gehäuse, Schaltschrank, Kupfer …) | ja | ja | ja, am konkretesten (IP/IK, Bohrbilder, AB-Prüfung) |
| Anfrage an Lieferanten DE/EN | ja (Nr. 2; Englisch nur bei Nr. 3 erwähnt) | ja (Nr. 1, Englisch in Nr. 3) | ja (Nr. 1, ausdrücklich DE/EN) |
| Angebotsvergleich | ja (Nr. 1) | ja (Nr. 2) | ja (Nr. 2) |
| Mahnung wegen Lieferverzug | nur indirekt („Terminanfragen“, Nr. 3) | ja (Nr. 3) | ja (Nr. 3, eigene Idee) |
| Lieferantenbewertung | ja (Nr. 6) | ja (Nr. 8) | ja (Nr. 9) |
| Fachbegriffe / Normen erklären | ja (Nr. 4) | ja (Nr. 5) | ja (Nr. 5) |
| Abdeckung der 5 Ideen aus dem Übungsblatt | 4 von 5 (Mahnung fehlt) | 5 von 5 | 5 von 5 |
| Hinweis auf Prüfung der Ergebnisse | teilweise – nur zu Marktpreisen (Nr. 8) | teilweise – nur bei Alternativbauteilen (Nr. 6) | ja – eigener Hinweis (Zahlen, Normen, Recht, aktuelle Preise) |
| Datenschutzhinweis | **nein** | ja (Preise, Verträge, Kundennamen, Personendaten; anonymisieren, IT/Datenschutz fragen) | ja (inkl. Platzhalter „Lieferant A“, „Preis X“) |
| Keine Aufforderung zu vertraulichen Daten | **nein** – Angebote übertragen, BOM prüfen, Kennzahlen, ohne jede Einschränkung | teilweise – „Du kopierst mir Angebotsdaten (Preise …) hinein“, widerspricht dem eigenen Schlusshinweis | teilweise – „Fügen Sie die Angebotsdaten ein, also Preise …“, „Kopieren Sie Bestellung und AB … herein“, relativiert durch Hinweis |
| Sachlich korrekt (Normen, Begriffe) | ja | ja | ja |
| Lesbar in den geplanten 3 Minuten (2:20–2:23) | ja (kompakt) | knapp | knapp (längste Antwort) |
| Anschlussfrage zum Weitermachen | ja | ja | ja |
| **Gesamt** | brauchbar, aber ohne Datenschutz | **sehr gut** | **sehr gut**, am praxisnächsten |

## Gefundene Fehler mit Beleg

Es wurden **keine sachlichen Fehler oder Halluzinationen** gefunden. Die genannten Normen und Begriffe stimmen: DIN EN 62208 (Leergehäuse für Niederspannungs-Schaltgerätekombinationen), IEC 61439 (Niederspannungs-Schaltgerätekombinationen), IK-Schutzgrade (Stoßfestigkeit nach EN 62262), NEMA-Typen (US-Gehäuseklassen), 1.4301 (Edelstahl V2A), AlMg3 (Aluminiumlegierung), SVERWEIS/XVERWEIS (deutsche Excel-Funktionsnamen), 8D-Report, Incoterms. Es gibt keine Zahlen zum Nachrechnen; die Zählung „10 Ideen“ wurde je Modell geprüft (jeweils Nr. 1–10, keine doppelt).

Auffälligkeiten, die für die Übung relevant sind:

1. **Fehlender Datenschutzhinweis bei Haiku.** Haiku schlägt vor, „Angebote mehrerer Lieferanten … in eine übersichtliche Tabelle übertragen“ (Nr. 1), „Stücklisten (BOM) prüfen“ (Nr. 5) und „Kennzahlen wie Liefertreue, Reklamationsquote und Preisentwicklung“ zu verarbeiten (Nr. 6) – ohne jeden Hinweis auf Daten-Ampel oder Anonymisierung. Stücklisten und Lieferantenpreise sind im Einkauf typischerweise gelb/rot.
2. **Widerspruch innerhalb der Antwort (Sonnet, Opus).** Sonnet Nr. 2: „Du kopierst mir Angebotsdaten (Preise, Staffeln …) hinein“ – Schlusshinweis: „Gib bitte keine vertraulichen Daten (Preise, Verträge …) ein“. Opus Nr. 2: „Fügen Sie die Angebotsdaten ein, also Preise …“; Nr. 4: „Kopieren Sie Bestellung und AB als Text herein“ – Hinweis: „keine vertraulichen Daten wie Konditionen“. Der Hinweis ist gut, steht aber erst am Ende; wer nur die Liste überfliegt, liest „Preise hineinkopieren“.
3. **Mahnung fehlt bei Haiku** als eigene Idee (nur „Standardantworten zu Terminanfragen“).
4. **Fähigkeitsversprechen ohne Einschränkung** (Sonnet Nr. 5): „in Englisch, Chinesisch oder anderen Sprachen übersetze … ich“ und Opus Nr. 6 „bleibe dabei bei der korrekten Fachsprache“ – klingt sicherer, als es ist; Fachübersetzungen müssen geprüft werden. Opus fängt das mit dem Prüfhinweis teilweise auf, Sonnet nicht.
5. Opus siezt, obwohl der Prompt duzt – kein Fehler, aber ein sichtbarer Unterschied.

## Lehren für die Auswertung

- **Der Ideen-Prompt funktioniert zuverlässig.** Alle drei Modelle liefern genau 10 Ideen, die zur Rolle und Branche passen und weit über die 5 Ideen im Übungsblatt hinausgehen (z. B. AB gegen Bestellung prüfen, Mängelrüge, Verhandlung als Rollenspiel, Lieferkettengesetz-Checkliste). Für Teilnehmende ohne Aufgabe ist das ein guter Start.
- **Kontext lohnt sich:** Je genauer Tätigkeit und Branche angegeben sind, desto konkreter die Ideen (Gehäuse, IP66, Kupferzuschläge). Gute Lehre zum Baustein „Kontext“ aus dem Prompt-Baukasten.
- **Daten-Ampel bleibt Aufgabe des Menschen.** Ein Modell sagt gar nichts zum Datenschutz, zwei fordern in der Liste zum Einfügen von Preisen auf und warnen erst am Schluss. Frage an die Runde: „Welche dieser 10 Ideen gehen mit grünen Daten – und bei welchen müsst ihr erst anonymisieren?“ Gerade Angebotsvergleich und AB-Prüfung sind beliebt, brauchen aber Platzhalter („Lieferant A“, „Preis X“).
- **Nicht jede Idee ist eine gute Übungsaufgabe.** Für die 27 Minuten eignen sich vor allem Text-Aufgaben mit grünen Daten (Mahnung, Anfrage-Vorlage, Checkliste Lieferantenbewertung, Begriffe erklären). Stücklisten- oder AB-Prüfung mit echten Daten eher nicht.
- **Gleicher Prompt, unterschiedliche Ergebnisse** – die Ideenlisten überschneiden sich in etwa 6–7 Punkten, der Rest variiert.
- **Zeit:** Das Lesen von 10 ausführlichen Ideen (Opus/Sonnet) dauert 2–3 Minuten – das sprengt fast das Zeitfenster 2:20–2:23 für „Aufgabe wählen + Ampel prüfen“. Tipp: „Nur die Überschriften lesen, eine auswählen.“

## Probleme im Material / Verbesserungsvorschlag

- **Der KI-Ideen-Prompt steht nur in der Sprechernotiz** von Folie 21 ([04_Folien.md](../04_Folien.md)), nicht auf der Folie selbst und nicht im [Übungsblatt](../06_Uebungen/Uebung_4_Eigene_Aufgabe.md). Die Sprechernotiz sagt aber „Schaut … ins Übungsblatt – da stehen Vorschläge“. Wer den Satz verpasst, findet den Prompt nirgends. Vorschlag für `06_Uebungen/Uebung_4_Eigene_Aufgabe.md`, Kasten „Keine Aufgabe dabei?“ (Zeile 67) ergänzen: *„Oder frag den KI-Assistenten: ‚Ich arbeite als [TÄTIGKEIT] in einem Unternehmen der Branche [BRANCHE]. Welche meiner typischen Aufgaben könntest du mir erleichtern? Gib mir 10 Ideen, die ohne vertrauliche Daten funktionieren.‘ Lies nur die Überschriften und such dir eine Idee aus.“*
- **Prompt um Datenschutz ergänzen.** Weil nicht jedes Modell von sich aus auf die Daten-Ampel hinweist (Haiku gar nicht), in der Sprechernotiz Folie 21 den Prompt erweitern: *„… Gib mir 10 Ideen, die ohne vertrauliche Daten funktionieren.“* Alternativ als Satz danach: „Prüft bei jeder Idee: Welche Ampelfarbe hätten die Daten?“
- Kleinigkeit: In der Sprechernotiz steht `[Tätigkeit]`, sonst verwendet das Material für Platzhalter Großbuchstaben (`[BRANCHE]`). Vorschlag: `[TÄTIGKEIT]`.
- Die Trainer-Lösungshinweise zu Übung 4 (Stolperstein „Keine Aufgabe dabei / Blockade“) erwähnen den KI-Ideen-Prompt nicht. Vorschlag ergänzen: *„… oder den Ideen-Prompt von Folie 21 nutzen lassen – danach gemeinsam eine Idee mit grünen Daten auswählen.“*

---

## Gesprächsprotokoll: Haiku

### Nutzer 1
Ich arbeite als Sachbearbeiterin im Einkauf in einem Unternehmen der Branche Elektro- und Gehäusetechnik (Maschinen- und Anlagenbau-Zulieferer). Welche meiner typischen Aufgaben könntest du mir erleichtern? Gib mir 10 Ideen.

### Assistent 1
Gerne. Hier sind 10 Ideen, wie ein KI-Assistent im Einkaufsalltag eines Elektro- und Gehäusetechnik-Zulieferers helfen kann:

1. **Angebotsvergleich erstellen:** Angebote mehrerer Lieferanten (z. B. für Blechgehäuse, Kabelkonfektion oder Schaltschrankkomponenten) in eine übersichtliche Tabelle übertragen, Preise, Lieferzeiten, Zahlungsbedingungen und Mindestabnahmemengen gegenüberstellen und Auffälligkeiten markieren.

2. **Anfragen (RFQ) formulieren:** Aus einer Stichpunktliste eine vollständige Anfrage an Lieferanten schreiben, inklusive technischer Spezifikation, Mengen, Zeichnungsverweis, Liefertermin, Verpackungs- und Qualitätsanforderungen.

3. **Lieferantenkorrespondenz beschleunigen:** Standardantworten zu Terminanfragen, Reklamationen oder Preiserhöhungen entwerfen, in gewünschtem Ton (sachlich, freundlich, bestimmt) und auf Deutsch oder Englisch.

4. **Technische Unterlagen verständlich machen:** Datenblätter, Normen (z. B. IP-Schutzarten, DIN/EN-Normen, RoHS/REACH-Angaben) oder Zeichnungsbeschreibungen in verständliche Kernaussagen für den Einkauf übersetzen, damit Rückfragen an die Technik gezielter gestellt werden können.

5. **Stücklisten (BOM) prüfen:** Stücklisten auf fehlende Angaben, doppelte Positionen, unplausible Mengen oder Abweichungen zu Vorgängerversionen durchsehen und eine Prüfliste erstellen.

6. **Lieferantenbewertung vorbereiten:** Kennzahlen wie Liefertreue, Reklamationsquote und Preisentwicklung in ein einheitliches Bewertungsschema bringen und Kommentare für Jahresgespräche formulieren.

7. **Bestellprozesse dokumentieren:** Arbeitsanweisungen, Checklisten oder Prozessbeschreibungen (z. B. für Bestellfreigabe, Wareneingang, Lieferantenaudit) entwerfen und an die internen Abläufe anpassen.

8. **Preisentwicklung analysieren:** Metallpreise (Kupfer, Aluminium, Stahl) oder Kunststoffpreise als Grundlage für Preisgleitklauseln oder Verhandlungsargumente zusammenfassen. Aktuelle Marktpreise müsstest du dabei aus einer Börsen- oder Lieferantenquelle selbst einfügen, da ich keinen Zugriff auf aktuelle Daten habe.

9. **Verhandlungsvorbereitung:** Argumentationsleitfaden erstellen mit Kostenstruktur-Fragen, möglichen Alternativen, Benchmark-Gedanken und typischen Einwänden der Lieferanten, inklusive Gesprächsnotizen-Vorlage.

10. **Interne Abstimmung erleichtern:** Zusammenfassungen für Besprechungen mit Konstruktion, Qualitätssicherung, Produktion oder Controlling schreiben, offene Punkte und Verantwortliche auflisten und Entscheidungsvorlagen strukturieren.

Wenn du mir sagst, welche dieser Aufgaben du am häufigsten hast, kann ich dir dazu ein konkretes Beispiel oder eine Vorlage erstellen.

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1
Ich arbeite als Sachbearbeiterin im Einkauf in einem Unternehmen der Branche Elektro- und Gehäusetechnik (Maschinen- und Anlagenbau-Zulieferer). Welche meiner typischen Aufgaben könntest du mir erleichtern? Gib mir 10 Ideen.

### Assistent 1
Gerne! Hier sind 10 Aufgaben aus dem Einkaufsalltag, bei denen ich dich unterstützen kann:

1. **Anfragen und Ausschreibungen formulieren**
   Ich entwerfe Anfragetexte (RFQ) für Blechteile, Schaltschrankgehäuse, Kabel, Klemmen, Schütze oder Normteile, inklusive Spezifikation, Stückzahlen, Liefertermin und Qualitätsanforderungen. Du gibst mir die Eckdaten, ich liefere eine saubere, vollständige Vorlage.

2. **Angebotsvergleich aufbereiten**
   Du kopierst mir Angebotsdaten (Preise, Staffeln, Lieferzeiten, Zahlungsbedingungen, Mindestbestellmengen) hinein, und ich erstelle eine übersichtliche Vergleichstabelle samt Hinweis auf Auffälligkeiten, zum Beispiel versteckte Kosten, Verpackung, Fracht oder Werkzeugkosten.

3. **Lieferantenkommunikation und Mahnungen**
   E-Mails an Lieferanten, etwa Terminnachfragen, Mahnungen bei Lieferverzug, Reklamationen oder Bitten um Bestätigung der Auftragsbestätigung. Ich kann den Ton anpassen (freundlich, bestimmt, formell) und auch auf Englisch formulieren.

4. **Verhandlungsvorbereitung**
   Ich helfe dir, Argumente für Preis- oder Konditionsverhandlungen zu sammeln, Szenarien durchzuspielen (z. B. Mengenbündelung, Rahmenvertrag, Skonto, Zahlungsziele) und einen Gesprächsleitfaden zu erstellen.

5. **Übersetzung und Verständnis von Fachdokumenten**
   Datenblätter, Angebote oder Vertragsentwürfe in Englisch, Chinesisch oder anderen Sprachen übersetze und fasse ich zusammen. Auch Fachbegriffe wie IP-Schutzarten, Materialbezeichnungen (z. B. 1.4301, AlMg3) oder Normen (DIN, EN, IEC) erkläre ich verständlich.

6. **Vergleich von Alternativen und Äquivalenten**
   Wenn ein Bauteil nicht lieferbar ist, kann ich Kriterien für gleichwertige Alternativen zusammenstellen (technische Parameter, Zulassungen wie CE, UL, RoHS). Wichtig: Die endgültige Freigabe muss die Technik oder Qualitätssicherung prüfen, und konkrete Herstellerdaten solltest du immer am Datenblatt verifizieren.

7. **Auswertung von Listen und Daten**
   Aus Excel-Auszügen (Bestellhistorie, Lieferantenbewertung, Preisentwicklung) erkenne ich Muster, erstelle Zusammenfassungen und schlage Formeln oder Pivot-Auswertungen vor. Beispiel: Welche Lieferanten liefern am häufigsten zu spät?

8. **Lieferantenbewertung und Risikoanalyse**
   Ich erstelle Bewertungsraster (Qualität, Termintreue, Preis, Service), Fragebögen für Lieferantenselbstauskünfte und eine Checkliste zu Risiken wie Single-Source, Rohstoffpreisschwankungen (Kupfer, Stahl, Aluminium) oder Lieferkettengesetz-Anforderungen.

9. **Dokumentation, Protokolle und Prozessbeschreibungen**
   Besprechungsnotizen, Verfahrensanweisungen, Checklisten für Wareneingang und Reklamationsabwicklung oder Einarbeitungsunterlagen für neue Kolleginnen und Kollegen schreibe ich strukturiert für dich aus Stichpunkten.

10. **Bedarfs- und Bestandsplanung unterstützen**
    Ich erkläre dir Methoden wie ABC-/XYZ-Analyse, Meldebestand oder Sicherheitsbestand, helfe bei Berechnungen und formuliere Auswertungen für Abstimmungen mit Disposition und Produktion.

**Wichtig zum Datenschutz:** Gib bitte keine vertraulichen Daten (Preise, Verträge, Kundennamen, personenbezogene Daten) in ein KI-Tool ein, wenn dein Unternehmen das nicht freigegeben hat. Im Zweifel anonymisiere die Angaben oder frage bei IT bzw. Datenschutz nach.

Wenn du magst, suche dir 1–2 Punkte aus, dann starte ich direkt mit einem konkreten Beispiel. Womit möchtest du anfangen?

---

## Gesprächsprotokoll: Opus

### Nutzer 1
Ich arbeite als Sachbearbeiterin im Einkauf in einem Unternehmen der Branche Elektro- und Gehäusetechnik (Maschinen- und Anlagenbau-Zulieferer). Welche meiner typischen Aufgaben könntest du mir erleichtern? Gib mir 10 Ideen.

### Assistent 1
Gern. Hier sind 10 Ideen aus dem Einkaufsalltag in der Elektro- und Gehäusetechnik, bei denen ich Ihnen Arbeit abnehmen kann:

**1. Anfragen an Lieferanten formulieren**
Sie nennen mir Artikel, Menge, Termin und Besonderheiten (z. B. Schutzart IP66, Material Edelstahl 1.4301, RAL-Farbe, UL-Zulassung). Ich schreibe daraus eine klare Anfrage auf Deutsch oder Englisch, die keine Rückfragen offenlässt.

**2. Angebote vergleichen**
Fügen Sie die Angebotsdaten ein, also Preise, Staffeln, Lieferzeiten, Zahlungsbedingungen, Incoterms und Mindestmengen. Ich baue daraus eine Vergleichstabelle, weise auf Unterschiede hin, die man leicht übersieht (Fracht, Verpackung, Werkzeugkosten, Gültigkeit), und rechne die Gesamtkosten aus.

**3. Mahnungen und Liefererinnerungen schreiben**
Ob Termin überfällig, Auftragsbestätigung fehlt oder ein Teil im Rückstand ist: Ich formuliere die Mail höflich, mit Nachdruck oder deutlich eskalierend, je nachdem, was die Lage verlangt.

**4. Auftragsbestätigungen gegen die Bestellung prüfen**
Kopieren Sie Bestellung und AB als Text herein. Ich zeige Ihnen Abweichungen bei Preis, Menge, Termin, Artikelnummer, Ausführung oder Bedingungen. Bei Gehäusen sind das typischerweise geänderte Maße, Bohrbilder oder Oberflächen.

**5. Technische Begriffe und Datenblätter verstehen**
Ich erkläre Fachbegriffe wie IP- und IK-Schutzarten, NEMA-Typen, EMV-Dichtungen, Kabelverschraubungen, Pulverbeschichtung oder Normen wie DIN EN 62208 und IEC 61439 so, dass Sie bei Rückfragen aus der Technik mitreden können. Lange Datenblätter fasse ich auf die Punkte zusammen, die für den Einkauf zählen.

**6. Lieferantenkorrespondenz auf Englisch oder in anderen Sprachen**
Ich übersetze Mails, Reklamationen und Spezifikationen und bleibe dabei bei der korrekten Fachsprache, zum Beispiel bei Lieferanten in Osteuropa oder Asien.

**7. Reklamationen und Mängelrügen formulieren**
Sie beschreiben den Mangel, etwa Lackschäden, Maßabweichungen, falsche Menge oder fehlende Zeugnisse. Ich schreibe eine sachliche Mängelrüge mit klarer Forderung nach Nachlieferung, Gutschrift oder 8D-Report und setze eine Frist.

**8. Verhandlungen vorbereiten**
Ich sammle mit Ihnen Argumente für Preisgespräche, zum Beispiel bei Rohstoffzuschlägen für Stahl, Kupfer oder Aluminium, und stelle Fragen zusammen, die Sie dem Lieferanten stellen können. Auf Wunsch spiele ich das Gespräch als Lieferant mit Ihnen durch.

**9. Lieferantenbewertung und Checklisten**
Ich entwerfe Kriterien und Bewertungsbögen für Qualität, Termintreue, Preis und Kommunikation. Dazu kommen Checklisten für die Freigabe neuer Lieferanten, etwa zu ISO 9001, REACH- und RoHS-Erklärungen, Konfliktmineralien oder Lieferkettengesetz.

**10. Excel-Hilfe und interne Texte**
Ich erkläre Formeln wie SVERWEIS/XVERWEIS, Pivot-Tabellen oder bedingte Formatierung, zum Beispiel für Ihre Terminüberwachung oder Preislisten. Außerdem entwerfe ich interne Mails, Protokolle von Lieferantengesprächen oder kurze Prozessbeschreibungen.

**Zwei Hinweise für die Praxis:**
- Bitte geben Sie keine vertraulichen Daten wie Konditionen, Kundennamen oder Personendaten ein, wenn Ihr Unternehmen das für dieses Tool nicht freigegeben hat. Ersetzen Sie solche Angaben im Zweifel durch Platzhalter, also „Lieferant A“ oder „Preis X“.
- Prüfen Sie meine Ergebnisse, vor allem bei Zahlen, Normen und rechtlichen Fragen. Ich kann mich irren, und bei aktuellen Marktpreisen oder Lieferzeiten bin ich nicht auf dem neuesten Stand.

Mit welcher Idee möchten Sie anfangen? Am besten gleich mit einem echten Fall aus Ihrem Alltag.
