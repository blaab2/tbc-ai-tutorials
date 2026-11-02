# Trainer-Leitfaden: „KI im Arbeitsalltag“

> Präsenz-Tutorial, ca. 3 Stunden (alternativ 2 × 90 Minuten)
> Für: Kolleginnen und Kollegen bei [FIRMENNAME] – keine Vorkenntnisse nötig
> Termin: [DATUM] · Raum: [RAUM] · Werkzeug: [KI-TOOL] ([LINK ZUM TOOL])

Dieser Leitfaden ist für dich als Trainerin oder Trainer. Er führt dich von der Vorbereitung über den Ablauf jedes Blocks bis zur Nachbereitung. Du musst kein KI-Profi sein – du solltest aber jede Übung vorher einmal selbst durchgespielt haben.

**Übersicht aller Materialien:** [README.md](README.md)

---

## Inhalt

1. [Zielbild und Zielgruppe](#1-zielbild-und-zielgruppe)
2. [Vorbereitung: Zeitplan als Checkliste](#2-vorbereitung-zeitplan-als-checkliste)
3. [Ablauf Block für Block](#3-ablauf-block-für-block)
4. [Variante: 2 × 90 Minuten](#4-variante-2--90-minuten)
5. [Moderationstipps für gemischte Gruppen](#5-moderationstipps-für-gemischte-gruppen)
6. [Troubleshooting](#6-troubleshooting)
7. [FAQ: Antworten auf schwierige Fragen](#7-faq-antworten-auf-schwierige-fragen)
8. [Materialliste](#8-materialliste)

---

## 1. Zielbild und Zielgruppe

### Zielbild

Am Ende des Tutorials hat **jede Person**:

- **3–4 echte Aufgaben** aus dem eigenen Arbeitsalltag selbst mit dem KI-Assistenten erledigt – nicht nur zugeschaut.
- verstanden, **was ein Sprachmodell ist** und was nicht: Es sagt wahrscheinlichen Text voraus, ist dabei sehr fähig, kann aber überzeugend falsch liegen und kennt unsere Firma nicht.
- die **Daten-Ampel** verinnerlicht: Was darf ich eingeben (grün), was nur mit Vorsicht (gelb), was nie (rot)?
- gelernt, **gute Prompts** zu schreiben (Prompt = die Anweisung oder Frage, die man der KI gibt) – mit dem **Prompt-Baukasten** aus Rolle, Kontext, Aufgabe, Format und Beispiel – und Ergebnisse durch Nachsteuern zu verbessern.
- eine Idee, **wo sie oder er morgen weitermacht** – und wen sie oder er fragen kann.

Kurz gesagt: **Selbstvertrauen + Urteilsvermögen.** Niemand soll mit „Das ist Zauberei“ oder „Das ist Quatsch“ rausgehen, sondern mit „Das ist ein nützliches Werkzeug, und ich weiß, wann ich ihm nicht trauen darf.“

### Zielgruppe

- Kolleginnen und Kollegen aus allen Bereichen (Vertrieb, Einkauf, Verwaltung, Qualität, Technik, Service …).
- Die meisten sind **keine Softwareentwickler**. Es wird nicht programmiert, keine Schnittstellen, keine Fachsprache.
- Alle bringen ihren **eigenen Laptop** mit und arbeiten im **Browser** mit [KI-TOOL].
- Vorwissen sehr unterschiedlich: von „noch nie benutzt“ bis „nutze ich privat täglich“. Rechne mit beiden Extremen in einem Raum.
- Ideale Gruppengröße: **8–16 Personen**. Ab etwa 16 Personen lohnt sich eine zweite Person als Co-Trainer oder Helfer, die in den Übungen mit herumgeht.

### Didaktische Grundsätze

- **70 % selbst machen, 30 % zuhören.** Wenn du merkst, dass du länger als 10 Minuten am Stück redest: Stopp, Übung.
- **Zweierteams:** Setze Unsichere bewusst mit Neugierigen zusammen. Eine Person tippt, die andere liest mit und schlägt vor – nach jeder Teilaufgabe wird getauscht.
- **Fehler bewusst zeigen.** Eine KI, die live danebenliegt, ist der beste Lerneffekt des Tages. Nicht verstecken, sondern feiern.
- **Echte Aufgaben vor Spielbeispielen.** Das fiktive Beispielmaterial (Firma „Nordlicht Technik GmbH“) ist zum sicheren Üben da. Ziel ist aber Block 6: die eigene Aufgabe.
- **Keine Übertreibung, keine Panikmache.** Realistisch und ermutigend.

---

## 2. Vorbereitung: Zeitplan als Checkliste

Druck dir diese Checkliste aus oder kopiere sie in dein Aufgaben-Tool.

### 4 Wochen vorher

- [ ] **Werkzeug klären:** Welches [KI-TOOL] nutzen wir (z. B. Claude, ChatGPT oder Microsoft Copilot – je nach Firmenlizenz)? Gibt es eine **Firmenlizenz**? Für wie viele Personen?
- [ ] **Zugänge klären mit [ANSPRECHPARTNER IT]:** Wie melden sich die Teilnehmenden an (Firmenkonto, Einladungslink oder die zentrale Firmenanmeldung, auch „Single Sign-on“ genannt)? Bis wann sind die Zugänge eingerichtet? Gibt es Einschränkungen (z. B. Datei-Upload deaktiviert, bestimmte Dateitypen gesperrt)?
- [ ] **Daten-Ampel abstimmen:** Die Vorlage [03_Daten-Ampel.md](03_Daten-Ampel.md) mit [ANSPRECHPARTNER IT] und [DATENSCHUTZBEAUFTRAGTE/R] durchgehen, an die Firmenregeln anpassen und **freigeben lassen**. Ohne Freigabe nicht als verbindliche Regel präsentieren.
- [ ] Fragen an IT/Datenschutz mitnehmen: Werden Eingaben bei unserer Lizenz zum Training des Modells genutzt? Wo werden Daten verarbeitet? Wie lange werden Chats gespeichert? Dürfen private Konten dienstlich genutzt werden? Hat unser Zugang Verbindungen zu anderen Systemen (z. B. E-Mail, Laufwerke)? Gibt es eine Regel, ob KI-Texte gekennzeichnet werden müssen? Die Antworten brauchst du für Block 2 und die [FAQ](#7-faq-antworten-auf-schwierige-fragen).
- [ ] **Termin und Raum** festlegen: [DATUM], [RAUM], 3 Stunden plus 30 Minuten Puffer für Aufbau. Alternativ zwei Termine à 90 Minuten (siehe [Abschnitt 4](#4-variante-2--90-minuten)).
- [ ] Wenn möglich **Co-Trainer oder Helfer** gewinnen (ab ca. 16 Teilnehmenden dringend empfohlen).
- [ ] Mit der Führungskraft bzw. Geschäftsleitung klären: Wird das Tutorial als Arbeitszeit gewertet? Gibt es eine offizielle Botschaft („Wir wollen, dass ihr das ausprobiert“)? Ein kurzer Satz der Leitung zu Beginn wirkt Wunder.

> **Hinweis EU AI Act:** Seit Februar 2025 verlangt Art. 4 der EU-KI-Verordnung (AI Act) von Unternehmen, die KI-Systeme einsetzen, Maßnahmen zu ergreifen, damit ihre Mitarbeitenden, die mit KI arbeiten, über ausreichende KI-Kompetenz verfügen. Dieses Tutorial kann ein Baustein dafür sein. Ob und wie es dokumentiert werden soll (z. B. Teilnehmerliste), klärst du mit der Personalabteilung bzw. [DATENSCHUTZBEAUFTRAGTE/R] – keine eigenen juristischen Aussagen dazu machen.

### 2 Wochen vorher

- [ ] **Einladung verschicken** mit der Vorlage aus [02_Einladung_und_Vorbereitung.md](02_Einladung_und_Vorbereitung.md).
- [ ] **Vorab-Umfrage** mitschicken (ebenfalls in 02). Die wichtigste Frage: *„Welche wiederkehrende, lästige Aufgabe würdest du gern schneller erledigen?“* Diese Antworten sind das Material für Block 6.
- [ ] **Einrichtungsanleitung** mitschicken: Bitte vorab einloggen und einmal „Hallo“ schreiben. Wer das vorher geschafft hat, spart dir am Tag 10 Minuten Login-Chaos.
- [ ] Die Folien aus [04_Folien.md](04_Folien.md) in euer Präsentationsprogramm übertragen und mit Firmenvorlage gestalten.

### 1 Woche vorher

- [ ] **Umfrage auswerten:**
  - Wie viele haben schon Erfahrung? → Zweierteams vorplanen (Unsichere + Neugierige).
  - Welche Aufgaben wurden genannt? → In Gruppen clustern (z. B. „E-Mails“, „Protokolle“, „Tabellen“, „Texte für Kunden“). Pro Cluster einen passenden Beispielprompt vorbereiten.
  - Gibt es Aufgaben, die gegen die Daten-Ampel verstoßen würden (z. B. „Personalakten zusammenfassen“)? → Für Block 6 eine anonymisierte Ersatzvariante überlegen und in Block 2 genau so ein Beispiel ansprechen.
- [ ] **Beispielmaterial anpassen:** Wenn die Gruppe z. B. stark aus dem Einkauf kommt, die Lieferantenliste in den Vordergrund stellen; bei Vertrieb die Kundenmail. Das Material liegt in [07_Beispielmaterial/](07_Beispielmaterial/).
- [ ] **Alle Übungen einmal komplett selbst durchspielen** – mit genau dem [KI-TOOL] und dem Konto-Typ, den die Teilnehmenden haben werden:
  - [Übung 1: Texte schreiben](06_Uebungen/Uebung_1_Texte_schreiben.md)
  - [Übung 2: Gute Prompts](06_Uebungen/Uebung_2_Gute_Prompts.md)
  - [Übung 3: Dokumente und Tabellen](06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md) – **besonders prüfen, ob der Upload von .txt, .csv und .md funktioniert**
  - [Übung 4: Eigene Aufgabe](06_Uebungen/Uebung_4_Eigene_Aufgabe.md)
  - Abgleichen mit den [Trainer-Lösungshinweisen](06_Uebungen/Trainer-Loesungshinweise.md)
- [ ] **Demo-Prompts testen** aus [demo_fehler_zeigen.md](07_Beispielmaterial/demo_fehler_zeigen.md). Wichtig: Die Ergebnisse variieren von Mal zu Mal und von Version zu Version. Notiere, welche Prompts bei *eurem* Tool gerade zuverlässig einen Fehler zeigen.
- [ ] **Screenshots machen** von: einer gelungenen Demo, einer schiefgegangenen Demo, dem Login-Bildschirm, dem Upload-Symbol. Das ist dein Backup, falls live nichts funktioniert.
- [ ] **Raum checken:** Beamer und Anschluss (HDMI/USB-C-Adapter), stabiles WLAN für alle Teilnehmenden gleichzeitig, **genügend Steckdosen bzw. Mehrfachsteckdosen** (Laptops laufen 3 Stunden!), Tische so stellen, dass Zweierteams nebeneinandersitzen können, Flipchart oder Whiteboard.
- [ ] **Gastzugang / WLAN-Zugangsdaten** für den Raum besorgen, falls Laptops nicht automatisch im Firmennetz sind.

### 1 Tag vorher

- [ ] **Erinnerungs-Mail** verschicken (Vorlage in [02_Einladung_und_Vorbereitung.md](02_Einladung_und_Vorbereitung.md)): Laptop + Ladekabel mitbringen, Login vorher testen, eigene Aufgabe im Kopf haben.
- [ ] **Ausdrucke** bereitlegen (je Teilnehmende/r ein Exemplar, plus 3 Reserve):
  - [ ] [Spickzettel](05_Spickzettel.md)
  - [ ] [Daten-Ampel](03_Daten-Ampel.md) (gern farbig, ggf. zusätzlich als Plakat A3)
  - [ ] Übungsblätter 1–4 aus [06_Uebungen/](06_Uebungen/)
  - [ ] Feedbackbogen aus [08_Nachbereitung.md](08_Nachbereitung.md)
  - [ ] Für dich: diesen Leitfaden und die [Trainer-Lösungshinweise](06_Uebungen/Trainer-Loesungshinweise.md)
- [ ] Beispielmaterial an einem Ort ablegen, an dem alle es herunterladen können (z. B. gemeinsamer Ordner, Intranet, USB-Sticks als Backup). Link notieren: [LINK ZU DEN MATERIALIEN].
- [ ] Zweierteams vorläufig festlegen (Namensliste), aber flexibel bleiben.
- [ ] **Zwei bis drei geteilte Reserve-Logins** bei IT anfragen bzw. bereithalten, falls einzelne Zugänge nicht funktionieren.
- [ ] Demo-Prompts noch einmal kurz testen – die Antworten können sich seit letzter Woche geändert haben.

### Am Tag selbst

- [ ] **30 Minuten vor Beginn** im Raum sein.
- [ ] Beamer anschließen, Bildschirmauflösung prüfen, Schrift im Browser **groß** stellen (Strg + Plus), damit man den Chat auch in der letzten Reihe lesen kann.
- [ ] Im [KI-TOOL] eingeloggt sein, einen **neuen, leeren Chat** offen haben. Alte private Chats in der Seitenleiste ggf. ausblenden oder mit einem Demo-Konto arbeiten.
- [ ] Benachrichtigungen (E-Mail, Chat) auf deinem Laptop **ausschalten**.
- [ ] WLAN mit zwei, drei Geräten gleichzeitig testen.
- [ ] Ausdrucke auf die Plätze legen. Daten-Ampel-Plakat aufhängen.
- [ ] Auf Flipchart vorbereiten: WLAN-Zugang, [LINK ZUM TOOL], [LINK ZU DEN MATERIALIEN], Ablaufplan mit Uhrzeiten.
- [ ] Getränke/Snacks für die Pause organisiert?
- [ ] Ankommende direkt bitten: „Laptop auf, einloggen, einmal ‚Hallo‘ schreiben.“ Wer Probleme hat, gleich zu dir oder zum Helfer.

---

## 3. Ablauf Block für Block

### Ablauf auf einen Blick

| Zeit | Block | Inhalt | Modus |
|---|---|---|---|
| 0:00–0:15 | 1 | Was ist KI eigentlich? | Zuhören + Demo |
| 0:15–0:30 | 2 | Spielregeln (Daten-Ampel) | Zuhören + kurze Aktivierung |
| 0:30–1:00 | 3 | Übung 1: Texte schreiben | Selbst machen |
| 1:00–1:30 | 4 | Gute Prompts + Übung 2 | Kurzinput + selbst machen |
| 1:30–1:40 | – | Pause | – |
| 1:40–2:20 | 5 | Übung 3: Mit Dokumenten und Tabellen arbeiten | Selbst machen |
| 2:20–2:50 | 6 | Übung 4: Deine eigene Aufgabe | Selbst machen (Zweierteams) |
| 2:50–3:05 | 7 | Ergebnisse & Abschluss | Austausch + Feedback |

Die Zeiten sind relativ zum Start (0:00 = Beginn). Trag dir die echten Uhrzeiten in eine Kopie dieser Tabelle ein.

> **Grundregel für Zeitprobleme:** Kürze lieber bei deinem Input (Blöcke 1, 2, 4) als bei den Übungen. Block 6 (eigene Aufgabe) ist der wichtigste Block des Tages – den schützt du.

---

### Block 1 – „Was ist KI eigentlich?“ (0:00–0:15)

**Ziel des Blocks:** Die Teilnehmenden haben ein einfaches, realistisches Bild davon, wie ein Sprachmodell funktioniert – und haben einmal gesehen, wie gut es sein kann und wie es schiefgehen kann.

**Material:** Folien zu Block 1 (Folien 1–6) in [04_Folien.md](04_Folien.md), [demo_fehler_zeigen.md](07_Beispielmaterial/demo_fehler_zeigen.md), deine Backup-Screenshots.

#### Ablauf

**0:00–0:04 · Begrüßung und Einstieg**

- Kurz vorstellen: wer du bist, warum du das machst.
- Ablauf zeigen (Flipchart oder Folie) und das Ziel nennen: *„Wenn ihr heute rausgeht, habt ihr 3–4 Aufgaben selbst mit KI erledigt – mindestens eine davon aus eurem eigenen Arbeitsalltag. Ihr werdet die meiste Zeit selbst tippen, nicht mir zuhören.“*
- Kurze Stimmungsabfrage per Handzeichen:
  - *„Wer hat so einen KI-Assistenten schon mal benutzt?“*
  - *„Wer nutzt ihn regelmäßig?“*
  - *„Wer ist eher skeptisch?“* – Und dann: *„Sehr gut, Skepsis ist heute ausdrücklich erwünscht.“*
- Organisatorisches: Pause um ca. 1:30, Toiletten, Getränke, Handys leise.

**0:04–0:09 · Was ist ein Sprachmodell?**

Kernbotschaften (Stichpunkte für dich):

1. Ein **Sprachmodell** ist ein Computerprogramm, das mit riesigen Mengen Text trainiert wurde. Es **sagt voraus, welcher Text wahrscheinlich als Nächstes kommt** – Wort für Wort.
2. Das klingt simpel, ist aber **erstaunlich fähig**: schreiben, umformulieren, übersetzen, zusammenfassen, strukturieren, Ideen liefern.
3. Es **kann überzeugend falsch liegen.** Wenn es etwas nicht weiß, erfindet es oft eine plausibel klingende Antwort. Das nennt man **Halluzination**.
4. Es **kennt unsere Firma nicht.** Es weiß nichts über unsere Kunden, Produkte, Preise oder internen Abläufe – außer dem, was du ihm im Chat gibst.

Formulierungsvorschläge:

- *„Stellt euch einen extrem belesenen Praktikanten vor: hat unglaublich viel gelesen, schreibt schnell und gut, ist nie genervt – aber war noch nie bei uns im Haus und gibt ungern zu, wenn er etwas nicht weiß.“*
- *„Die KI ‚weiß‘ nichts im menschlichen Sinn. Sie erzeugt Text, der wahrscheinlich passt. Meistens ist wahrscheinlich auch richtig. Aber eben nicht immer.“*
- *„Ihr seid die Fachleute. Die KI ist das Werkzeug.“*

**0:09–0:15 · Live-Demo: einmal beeindruckend, einmal schiefgehend**

*Was du zeigst* (am Beamer, Schrift groß):

1. **Etwas Beeindruckendes** (ca. 2 Minuten), zum Beispiel:
   - Die [Kundenmail](07_Beispielmaterial/kundenmail_beschwerde.txt) einfügen und schreiben: *„Schreib eine freundliche, professionelle Antwort auf diese Beschwerde. Wir können bis Freitag liefern und bieten 5 % Rabatt auf die nächste Bestellung an.“*
   - Dann: *„Und jetzt das Ganze auf Englisch.“* – Zeigt: Die KI merkt sich, was vorher im Chat stand, und Nachsteuern ist ganz einfach.
   - Alternativen: die Stichwort-Mail aus Folie 6 (Demo 7, Variante C) oder die Zusammenfassung der Kundenmail (Demo 7, Grundvariante) in [demo_fehler_zeigen.md](07_Beispielmaterial/demo_fehler_zeigen.md). Nimm die Variante, die bei deinem Test am besten funktioniert hat.
2. **Etwas, das schiefgeht** (ca. 2 Minuten): Einen der vorher getesteten Prompts aus [demo_fehler_zeigen.md](07_Beispielmaterial/demo_fehler_zeigen.md) verwenden, z. B.:
   - nach Firmenwissen fragen (Demo 3; z. B. *„Wer ist der Geschäftsführer der Nordlicht Technik GmbH und welche Produkte hat sie?“* – die Firma ist fiktiv, die KI erfindet vielleicht trotzdem etwas),
   - nach Quellen mit genauen Fundstellen fragen (Demo 1),
   - Buchstaben zählen oder eine längere Rechnung lösen lassen (Demo 4),
   - nach sehr aktuellen Ereignissen fragen (Demo 2).
3. **Auflösen** (ca. 2 Minuten): *„Was ist hier passiert? Die Antwort klang genauso selbstsicher wie die erste. Genau deshalb prüfen wir. Das schauen wir uns gleich bei den Spielregeln genauer an.“*

> **Wichtig:** Die KI antwortet nicht jedes Mal gleich. Es kann sein, dass sie den „Fehler-Prompt“ live plötzlich richtig beantwortet. Dann sagst du: *„Interessant – heute hat sie Glück gehabt. Letzte Woche kam das hier raus:“* und zeigst den Screenshot. Auch das ist eine Lektion: Man kann sich nicht darauf verlassen, dass eine Antwort beim nächsten Mal gleich ausfällt.

**Was die Teilnehmenden tun:** Zuschauen, Fragen stellen. Wer schon eingeloggt ist, darf parallel mittippen – aber nicht müssen.

**Zeitpuffer-Tipps:**
- Wenn es knapp wird: Stimmungsabfrage auf eine Frage kürzen, nur eine Demo-Hälfte (die Fehler-Demo ist wichtiger als die Wow-Demo, denn die Wow-Momente kommen in den Übungen von selbst).
- Wenn Login-Probleme den Start verzögern: Block 1 trotzdem pünktlich starten, der Helfer kümmert sich parallel um Logins.

---

### Block 2 – „Spielregeln“ (0:15–0:30)

**Ziel des Blocks:** Alle wissen, welche Daten sie eingeben dürfen, dass die Verantwortung beim Menschen bleibt und wann sie Ergebnisse gegenprüfen müssen.

**Material:** Folien zu Block 2 (Folien 7–9) in [04_Folien.md](04_Folien.md), Ausdruck/Plakat [03_Daten-Ampel.md](03_Daten-Ampel.md) (abgestimmte Fassung!).

#### Ablauf

**0:15–0:24 · Die Daten-Ampel**

*Was du sagst:*

- *„Bevor wir loslegen, die wichtigste Folie des Tages. Alles, was ihr in den Chat eintippt oder hochladet, verlässt euren Laptop und wird auf Servern des Anbieters verarbeitet. Deshalb gibt es klare Regeln.“*
- Die drei Farben durchgehen (Inhalte aus der abgestimmten [Daten-Ampel](03_Daten-Ampel.md) übernehmen):

| Farbe | Bedeutung | Beispiele |
|---|---|---|
| 🟢 **Grün** | Unbedenklich, darfst du eingeben | Öffentlich verfügbare Infos, allgemeine Fragen, eigene Texte ohne Namen und Interna, Formulierungshilfen, fiktive Beispiele |
| 🟡 **Gelb** | Nur mit Firmenzugang, nach Prüfung und möglichst anonymisiert – im Zweifel vorher nachfragen | Interne, aber nicht vertrauliche Dokumente (z. B. Richtlinien, Besprechungsnotizen mit ersetzten Namen), Kundenmails ohne Namen, Adressen und Auftragsnummern |
| 🔴 **Rot** | Niemals eingeben | Personenbezogene Daten von Kunden oder Mitarbeitenden, Gesundheitsdaten, Passwörter und Zugangsdaten, vertrauliche Verträge, Konstruktionsdaten und Geschäftsgeheimnisse, ggf. exportkontrollierte Informationen |

- **Der Trick für Gelb – Anonymisieren:** *„Ersetzt ‚Herr Müller von der Firma XY‘ durch ‚[KUNDE]‘. Die KI braucht den Namen nicht, um eine gute Antwort zu schreiben.“*
- **Firmenlizenz vs. privates Gratis-Konto:** *„Wir nutzen heute [KI-TOOL] über die Firmenlizenz. Bei privaten Gratis-Konten können die Bedingungen anders sein – zum Beispiel, ob eure Eingaben zum Weitertrainieren des Modells genutzt werden. Deshalb: Dienstliches nur im Firmenzugang.“* (Genaue Regeln für eure Lizenz vorher mit IT klären, siehe Vorbereitung.)
- *„Im Zweifel: rot. Und im Zweifel fragt ihr [ANSPRECHPARTNER IT] oder [DATENSCHUTZBEAUFTRAGTE/R].“*

> **Wichtig:** Keine Rechtsberatung geben. Wenn jemand eine Detailfrage zur DSGVO stellt, die du nicht sicher beantworten kannst: *„Gute Frage, die nehme ich mit und kläre sie mit [DATENSCHUTZBEAUFTRAGTE/R].“* Schreib sie auf den Flipchart „Offene Fragen“.

**Kurze Aktivierung (ca. 3 Minuten) – „Welche Farbe?“:** Lies die folgenden Beispiele vor (bei Zeitdruck nur 4–5 davon), die Gruppe zeigt per Handzeichen oder farbigen Karten grün/gelb/rot. Beispiele:

1. *„Formuliere meine Abwesenheitsnotiz freundlicher.“* → Grün
2. *„Fasse dieses öffentliche Datenblatt eines Lieferanten zusammen.“* → Grün
3. *„Hier ist ein internes Protokoll unserer Teambesprechung, mach daraus eine Aufgabenliste.“* → Gelb (nur im Firmenzugang, Namen vorher durch Rollen ersetzen, keine vertraulichen Inhalte)
4. *„Hier ist die Krankmeldung von Kollegin X, schreib ihr eine Genesungsmail.“* → Rot (Gesundheitsdaten)
5. *„Ich kopiere dir die Kundenliste mit Adressen und Umsätzen, sortier mal.“* → Rot (personenbezogene Daten, Geschäftszahlen)
6. *„Hier sind die Zugangsdaten zu unserem Server, warum klappt der Login nicht?“* → Rot (Zugangsdaten)
7. *„Hier ist die Konstruktionszeichnung unseres neuen Produkts, finde Schwachstellen.“* → Rot (Geschäftsgeheimnis)

Bei Uneinigkeit kurz diskutieren lassen – das ist gut so.

**0:24–0:30 · Verantwortung und Gegenprüfen**

*Was du sagst:*

- **Die Verantwortung bleibt beim Menschen.** *„Was ihr rausschickt, habt ihr geschrieben – auch wenn die KI den Entwurf gemacht hat. Die KI ist der Entwurfsschreiber, ihr seid die Unterschrift.“*
- **Wann gegenprüfen?** Faustregel:
  - **Immer prüfen:** Zahlen, Daten, Namen, Fakten, Zitate, Quellen, rechtliche oder technische Aussagen, alles, was an Kunden oder nach außen geht.
  - **Kurz drüberlesen reicht:** Formulierungsvorschläge, Ideensammlungen, Gliederungen, interne Entwürfe, die ihr ohnehin überarbeitet.
  - Je wichtiger und je weiter weg vom eigenen Fachwissen, desto gründlicher prüfen.
- *„Wenn ihr ein Ergebnis nicht selbst beurteilen könnt, ist die KI für diese Aufgabe das falsche Werkzeug – oder ihr braucht jemanden, der es prüft.“*

**Was die Teilnehmenden tun:** Zuhören, Ampel-Aktivierung mitmachen, Fragen stellen. Daten-Ampel-Ausdruck liegt vor ihnen.

**Zeitpuffer-Tipps:**
- Aktivierung auf 3–4 Beispiele kürzen.
- **Nicht kürzen:** die Rot-Kategorie und den Satz „Die Verantwortung bleibt beim Menschen“.
- Lange Datenschutz-Diskussionen auf das Flipchart „Offene Fragen“ parken und in Block 7 oder per Follow-up-Mail beantworten.

---

### Block 3 – „Übung 1: Texte schreiben“ (0:30–1:00)

**Ziel des Blocks:** Alle haben selbst eine E-Mail mit KI entworfen bzw. verbessert, den Ton geändert, übersetzt und gekürzt. Erstes Erfolgserlebnis.

**Material:** Übungsblatt [Uebung_1_Texte_schreiben.md](06_Uebungen/Uebung_1_Texte_schreiben.md), [kundenmail_beschwerde.txt](07_Beispielmaterial/kundenmail_beschwerde.txt), [Trainer-Lösungshinweise](06_Uebungen/Trainer-Loesungshinweise.md), Folien zu Block 3 (Folien 10–11) in [04_Folien.md](04_Folien.md).

#### Ablauf

**0:30–0:35 · Einführung (max. 5 Minuten)**

- Zweierteams bilden (vorgeplant, siehe Umfrage). *„Eine Person tippt, die andere liest mit und gibt Tipps. Nach jeder Aufgabe wird getauscht.“*
- Einmal am Beamer zeigen: neuen Chat öffnen, Text einfügen, Prompt schreiben, abschicken, nachbessern.
- Hinweis: *„Ihr könnt nichts kaputt machen. Wenn eine Antwort Mist ist, schreibt einfach dazu, was euch nicht gefällt.“*

**0:35–0:55 · Übung (ca. 20 Minuten)**

Die Teilnehmenden bearbeiten das Übungsblatt in drei Stufen:

- **Basis (ca. 10 Min.) – Aufgaben A und B:** Antwort auf die verärgerte Kundenmail wegen Lieferverzug entwerfen lassen (A), dann den Ton ändern – förmlicher, herzlicher – und auf maximal 5 Sätze kürzen (B).
- **Weiter (ca. 8 Min.) – Aufgaben C und D:** die Antwort ins Englische übersetzen und zurück prüfen, ob Fachbegriffe und Inhalt stimmen (C); eine eigene, echte E-Mail verbessern lassen – nur, wenn sie nach der Daten-Ampel grün ist oder vorher anonymisiert wurde (D).
- **Für Schnelle – Aufgaben E bis G:** Betreffzeilen, Perspektivwechsel, interne Kurznachricht.

Sag deutlich: *„Basis ist das Ziel. Alles darüber ist Zugabe.“* In 20 Minuten schaffen die meisten Teams A, B und eine der Aufgaben C oder D.

*Was du tust:* Herumgehen. Typische Fragen und Stolpersteine findest du in den [Trainer-Lösungshinweisen](06_Uebungen/Trainer-Loesungshinweise.md). Achte besonders auf:

- Teams, die nach der ersten Antwort aufhören → *„Gefällt euch das schon zu 100 %? Was würdet ihr ändern? Schreibt’s der KI.“*
- Teams, die erfundene Details übernehmen (z. B. ein Lieferdatum, das nirgendwo stand) → perfekter Moment für: *„Woher kommt dieses Datum?“*
- Teams, die echte Kundendaten einfügen wollen → freundlich an die Ampel erinnern.

**0:55–1:00 · Kurze Auswertung (5 Minuten)**

- *„Was hat euch überrascht?“* – 2–3 Stimmen sammeln.
- *„Hat die KI irgendwo etwas dazuerfunden?“* – Fast immer meldet sich jemand. Das ist der Brückenschlag zu Block 4: *„Je mehr Kontext ihr gebt, desto weniger muss sie raten.“*

**Zeitpuffer-Tipps:**
- Nur die Basis (A und B) verlangen, C und D als freiwillige Zugabe nennen.
- Auswertung auf eine Frage kürzen.
- Wenn die Gruppe sehr schnell ist: Aufgaben E bis G aktiv anbieten, Auswertung etwas ausdehnen.

---

### Block 4 – „Gute Prompts“ (1:00–1:30)

**Ziel des Blocks:** Die Teilnehmenden kennen die fünf Bausteine des Prompt-Baukastens und wissen, dass Nachsteuern und Verbessern (auch „iterieren“ genannt) normal und erwünscht ist. Sie wenden das in Übung 2 an.

**Material:** Folien zu Block 4 (Folien 12–16) in [04_Folien.md](04_Folien.md), Übungsblatt [Uebung_2_Gute_Prompts.md](06_Uebungen/Uebung_2_Gute_Prompts.md), [Spickzettel](05_Spickzettel.md), [notizen_besprechung.txt](07_Beispielmaterial/notizen_besprechung.txt), [Trainer-Lösungshinweise](06_Uebungen/Trainer-Loesungshinweise.md).

#### Ablauf

**1:00–1:12 · Input: Was macht einen guten Prompt aus? (ca. 12 Minuten)**

**Der Prompt-Baukasten (Folie 13)** – fünf Bausteine, genau so auch auf dem [Spickzettel](05_Spickzettel.md) und in Übung 2. Merkhilfe: *Wer? · Worum? · Was? · Wie? · Wie genau?*

1. **Rolle – Wer soll die KI sein?** *„Du bist eine erfahrene Kundenbetreuerin in einem technischen Mittelstandsunternehmen.“*
2. **Kontext – Worum geht es, für wen?** Hintergrund, Empfänger, Situation. *„Die KI kennt unsere Firma nicht – erzählt ihr das Nötige.“* (Das ist der wichtigste Baustein.)
3. **Aufgabe – Was genau soll herauskommen?** Eine Mail, eine Liste, drei Varianten …
4. **Format – Wie soll das Ergebnis aussehen?** Tabelle, Stichpunkte, max. 5 Sätze, Betreffzeile, Du oder Sie …
5. **Beispiel – Wie sieht „gut“ aus?** Ein Muster mitgeben, z. B. eine frühere, gelungene Mail (ohne rote Daten).

Dazu kommt – kein eigener Baustein, aber genauso wichtig – das **Nachsteuern** (Folie 15): *„kürzer“*, *„förmlicher“*, *„ohne Fachbegriffe“*, und der Joker *„Stell mir erst ein paar Fragen, bevor du loslegst.“*

**Schwach vs. stark nebeneinander (Folie 14)** – live am Beamer zeigen, beide nacheinander jeweils in einem **neuen Chat** abschicken. Auf der Folie steht das Beispiel einer Mail an einen Lieferanten:

> ❌ **Schwacher Prompt:** *„Schreib eine Mail an den Lieferanten wegen der Lieferung.“*
>
> ✅ **Starker Prompt:** Rolle Einkäuferin, Kontext (Lieferung zum zweiten Mal verschoben, wird bis zum 15. gebraucht), Aufgabe (verbindlichen Liefertermin bis Freitag erbitten), Format (max. 120 Wörter, freundlich, aber bestimmt, Betreffzeile, Sie-Form), Beispiel für den Ton. Den vollständigen Text findest du auf Folie 14.

**Alternative für die Live-Demo** – wenn deine Gruppe viel mit Besprechungen zu tun hat, nimm stattdessen die [Besprechungsnotizen](07_Beispielmaterial/notizen_besprechung.txt):

> ❌ **Schwacher Prompt:** *„Schreib ein Protokoll.“*
>
> ✅ **Starker Prompt:** *„Du bist Assistenz der Teamleitung. Unten stehen meine ungeordneten Notizen aus der Teambesprechung von heute. Mach daraus ein kurzes Ergebnisprotokoll für das Team. Format: 1. Beschlüsse als Stichpunkte, 2. eine Tabelle mit den Spalten Aufgabe | Verantwortlich | Termin, 3. offene Fragen. Erfinde nichts dazu – wenn ein Verantwortlicher oder Termin fehlt, schreib ‚offen‘. [Notizen einfügen]“*

Lass die Gruppe vergleichen: *„Welches Ergebnis würdet ihr eher verwenden? Wo hat die KI beim schwachen Prompt geraten oder etwas erfunden?“*

*Formulierungsvorschläge:*

- *„Ein Prompt ist wie ein Arbeitsauftrag an eine neue Kollegin. Je klarer der Auftrag, desto besser das Ergebnis.“*
- *„Ihr müsst keinen perfekten Prompt schreiben. Die erste Antwort ist ein Entwurf – danach redet ihr mit der KI wie mit einem Menschen weiter.“*
- *„Mein Lieblingstrick: ‚Stell mir erst ein paar Fragen, bevor du loslegst.‘ Dann denkt die KI für euch mit, was fehlt.“*

> **Hinweis:** Es gibt keine „Zauberformeln“. Prompts, die im Internet als Geheimtipps kursieren, sind meist nicht nötig. Klarheit schlägt Tricks.

**1:12–1:30 · Übung 2 (ca. 18 Minuten)**

Die Teilnehmenden arbeiten das Übungsblatt [Uebung_2_Gute_Prompts.md](06_Uebungen/Uebung_2_Gute_Prompts.md) in ihren Zweierteams durch (Beispielauftrag: Einarbeitungsplan für einen neuen Kollegen im Lager):

- **Basis (ca. 8 Min.) – A und B:** Minimal-Prompt gegen Baukasten-Prompt, Ergebnisse vergleichen.
- **Weiter (ca. 5 Min.) – C oder D:** „Stell mir zuerst 3 Fragen“ bzw. Schritt für Schritt nachschärfen.
- **Weiter (ca. 5 Min.) – E:** eigenen wiederverwendbaren Prompt bauen. Bitte nicht auslassen – das ist die Brücke zu Block 6.
- **Für Schnelle – F und G.**

*Was du tust:* Herumgehen. Gute Prompts, die du siehst, merken – die kannst du in Block 7 oder in der Follow-up-Mail als Beispiel nehmen (mit Erlaubnis).

Zwei Minuten vor der Pause ankündigen: *„Noch zwei Minuten, dann Pause. Lasst eure Chats offen.“*

**Zeitpuffer-Tipps:**
- Input auf 8 Minuten kürzen: nur schwach vs. stark zeigen und für die Bausteine auf den Spickzettel verweisen.
- In der Übung nur A, B und E verlangen.
- Wenn die Übung nicht fertig wird: kein Problem, die Bausteine werden in Übung 3 und 4 sowieso wieder gebraucht.
- **Pause nicht verschieben.** Nach 90 Minuten brauchen alle eine Pause.

---

### Pause (1:30–1:40)

- 10 Minuten. Pünktlich wieder anfangen.
- Nutze die Pause, um Teams mit Login- oder Upload-Problemen zu helfen und den Upload für Block 5 bei dir am Beamer vorzubereiten.
- Lockerer Gesprächsanlass: Viele erzählen in der Pause, wofür sie die KI gern nutzen würden. Hör zu – das ist Gold für Block 6.

---

### Block 5 – „Übung 3: Mit Dokumenten und Tabellen arbeiten“ (1:40–2:20)

**Ziel des Blocks:** Die Teilnehmenden können Dateien hochladen und mit Inhalten arbeiten: zusammenfassen, Kernpunkte finden, zwei Versionen vergleichen, Notizen in eine Tabelle bringen, Checklisten erzeugen. Sie erleben, dass auch hier gegenprüfen nötig ist.

**Material:** Übungsblatt [Uebung_3_Dokumente_und_Tabellen.md](06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md), Folien zu Block 5 (Folien 18–20) in [04_Folien.md](04_Folien.md), Beispielmaterial:
- [pruefbericht_lang.md](07_Beispielmaterial/pruefbericht_lang.md) – langer Prüfbericht zum Zusammenfassen
- [richtlinie_reisekosten_v1.md](07_Beispielmaterial/richtlinie_reisekosten_v1.md) und [richtlinie_reisekosten_v2.md](07_Beispielmaterial/richtlinie_reisekosten_v2.md) – zwei Versionen zum Vergleichen
- [lieferantenliste_unsortiert.csv](07_Beispielmaterial/lieferantenliste_unsortiert.csv) – unordentliche Tabelle zum Aufräumen
- [notizen_besprechung.txt](07_Beispielmaterial/notizen_besprechung.txt) – Notizen in Tabelle/Checkliste umwandeln

#### Ablauf

**1:40–1:45 · Einführung und Demo (ca. 5 Minuten)**

- Kurze Erinnerung an die Daten-Ampel: *„Beim Hochladen gilt genau dasselbe wie beim Eintippen. Eine Datei ist nur ein sehr langer Text.“*
- Am Beamer zeigen: Upload über das **Büroklammer- bzw. Upload-Symbol** im Chatfenster (je nach Tool unterschiedlich platziert), Datei auswählen, Prompt dazuschreiben.
- Alternative zeigen, falls Upload nicht geht: Text aus der Datei kopieren und in den Chat einfügen.
- Hinweis zur Länge: *„Sehr lange Dokumente kann die KI nicht immer vollständig im Blick behalten. Bei wichtigen Details lieber gezielt nachfragen: ‚Zitiere mir die Stelle, an der das steht.‘“*

**1:45–2:12 · Übung 3 (ca. 27 Minuten)**

Das Übungsblatt hat **vier Stationen (A–D)**, jede mit Basis, Weiter, einem **Prüfschritt (Pflicht!)** und Aufgaben für Schnelle. Die Teams wählen frei – **nicht alles muss gemacht werden**. Empfehlung wie auf dem Blatt: erst **eine Station gründlich** (Basis + Weiter + Prüfschritt), danach eine zweite, wenn Zeit bleibt. Idealerweise ist eine davon eine Text- und eine eine Tabellenaufgabe.

- **Station A – Langen Bericht zusammenfassen:** Den Prüfbericht in genau 5 Sätzen für die Geschäftsführung zusammenfassen lassen. Dann gezielt nachfragen, z. B. *„Welche Risiken oder offenen Punkte nennt der Bericht, die noch nicht gelöst sind? Als Tabelle: Risiko | Wie schlimm | Abschnitt.“* – und drei Aussagen im Original prüfen. Die versteckten Stolpersteine (Schlitzbreite 0,13 mm bei ±0,10 mm „i. O.“, Schutzglas-Lieferzeit, fehlender Kaufpreis) stehen in den Lösungshinweisen.
- **Station B – Zwei Versionen vergleichen:** Beide Reisekostenrichtlinien hochladen: *„Welche inhaltlichen Unterschiede gibt es zwischen Version 1 und 2? Als Tabelle: Thema | alt | neu.“* Die vollständige Liste der Unterschiede steht in den [Trainer-Lösungshinweisen](06_Uebungen/Trainer-Loesungshinweise.md). Lass die Teams zählen, ob die KI alle Unterschiede gefunden hat. **Empfohlen, wenn du nur eine Station vorgeben willst** – größter Aha-Effekt.
- **Station C – Notizen → Protokoll und Aufgabenliste:** Aus den Besprechungsnotizen ein Protokoll, eine Aufgabentabelle und eine Checkliste für das nächste Treffen erzeugen.
- **Station D – Tabelle bereinigen:** Die Lieferantenliste vereinheitlichen lassen (Datumsformate, Schreibweisen), Dubletten und fehlende Werte markieren.

*Was du tust:* Herumgehen. Achte auf:

- **Vergleichsaufgabe:** KI findet oft nicht alle Unterschiede oder erfindet einen. Genau das ist die Lektion: *„Für einen ersten Überblick super – aber wenn es darauf ankommt, prüft ihr gegen das Original.“*
- **Tabellen:** KI kann Dubletten übersehen oder beim Vereinheitlichen Werte verändern. Stichproben machen lassen: *„Prüft drei Zeilen gegen das Original.“*
- **Zählen und Rechnen:** Wenn jemand Summen bilden lässt – nachrechnen lassen.
- Teams, die das Ergebnis zurück in Excel bringen wollen: Tipp *„Gib mir das Ergebnis als CSV mit Semikolon als Trennzeichen“* bzw. die Tabelle kopieren und einfügen. Ob das Tool direkt eine Datei zum Herunterladen erzeugen kann, hängt vom Werkzeug ab.

**2:12–2:20 · Kurze Auswertung (ca. 8 Minuten)**

- *„Wer hat beim Vergleich alle Unterschiede gefunden? Wer hat einen Fehler entdeckt?“*
- Überleitung zu Block 6: *„Jetzt habt ihr alle Werkzeuge. Als Nächstes geht’s an eure eigene Aufgabe.“*

**Zeitpuffer-Tipps:**
- Demo auf 3 Minuten kürzen.
- Alle Teams machen nur **eine** Station (Empfehlung: Station B, Versionsvergleich).
- Auswertung auf 2–3 Minuten kürzen und direkt in Block 6 überleiten.

---

### Block 6 – „Übung 4: Deine eigene Aufgabe“ (2:20–2:50)

**Ziel des Blocks:** Jede Person hat eine echte, eigene Aufgabe aus dem Arbeitsalltag mit KI bearbeitet – unter Beachtung der Daten-Ampel. **Das ist der wichtigste Block des Tages.**

**Material:** Übungsblatt [Uebung_4_Eigene_Aufgabe.md](06_Uebungen/Uebung_4_Eigene_Aufgabe.md) (Vorgehen in 5 Schritten, Ideenliste nach Rollen, Bewertungsraster), Folien zu Block 6 (Folien 21–22) in [04_Folien.md](04_Folien.md), [Spickzettel](05_Spickzettel.md), [Daten-Ampel](03_Daten-Ampel.md), deine Auswertung der Vorab-Umfrage mit vorbereiteten Beispielprompts je Aufgaben-Cluster.

#### Ablauf

**2:20–2:23 · Einführung (ca. 3 Minuten)**

- *„Erinnert euch an die lästige Aufgabe, die ihr in der Umfrage genannt habt. Die nehmt ihr euch jetzt vor.“*
- **Ampel-Check zuerst:** *„Bevor ihr loslegt: Welche Farbe hat eure Aufgabe? Bei Gelb anonymisiert ihr, bei Rot nehmt ihr eine Ersatzaufgabe oder baut ein ausgedachtes Beispiel mit gleicher Struktur.“*
- Wer keine Aufgabe hat: „Ideenliste nach Rollen“ auf dem Übungsblatt oder eine der Umfrage-Aufgaben aus dem Cluster der Kollegen übernehmen.
- Arbeitsweise: Zweierteams, **erst die eine Person, dann die andere** (je ca. 12 Minuten) – oder gemeinsam an der spannenderen Aufgabe. Die zweite Person ist Sparringspartner: Sie fragt nach, schlägt Bausteine vor und achtet auf die Ampel.
- Die letzten 3 Minuten (ab 2:47) bereiten die Teams ihre 2-Minuten-Vorstellung vor (siehe Übungsblatt).

**2:23–2:50 · Arbeitsphase (ca. 27 Minuten)**

*Was du tust:* **Herumgehen, herumgehen, herumgehen.** Jedes Team mindestens einmal besuchen. Nützliche Fragen:

- *„Was willst du am Ende in der Hand haben?“* (hilft, das Ziel zu klären)
- *„Was müsste eine neue Kollegin wissen, um das zu erledigen? Hast du das der KI gesagt?“*
- *„Hast du schon ‚Stell mir erst Fragen‘ probiert?“*
- *„Würdest du das so rausschicken? Was müsstest du noch prüfen?“*
- Bei Ampel-Verstößen: ruhig und unaufgeregt gegensteuern, gemeinsam anonymisieren.

**Merk dir 2–3 schöne Ergebnisse** für Block 7 und frag die Personen schon jetzt: *„Magst du das gleich kurz zeigen?“* So vermeidest du betretenes Schweigen.

Fünf Minuten vor Ende ankündigen: *„Noch fünf Minuten. Wer noch nicht dran war, ist jetzt dran.“*

**Zeitpuffer-Tipps:**
- Diesen Block **nicht kürzen**, wenn irgend möglich. Lieber Block 7 straffen.
- Wenn du insgesamt sehr knapp bist: Teams arbeiten gemeinsam an **einer** Aufgabe statt zwei nacheinander.
- Wenn die Aufgabe einer Person nicht KI-geeignet ist (z. B. braucht Zugriff auf interne Systeme): ehrlich sagen und gemeinsam einen Teil finden, der passt – z. B. die Vorlage, die E-Mail drumherum, die Checkliste.

---

### Block 7 – „Ergebnisse & Abschluss“ (2:50–3:05)

**Ziel des Blocks:** Erfolge sichtbar machen, Gelerntes festigen, klären, wie es weitergeht, Feedback einsammeln.

**Material:** Folien zu Block 7 (Folien 23–26) in [04_Folien.md](04_Folien.md), Feedbackbogen aus [08_Nachbereitung.md](08_Nachbereitung.md), Flipchart „Offene Fragen“.

#### Ablauf

**2:50–2:58 · Ergebnisse zeigen (ca. 8 Minuten)**

- 2–3 Personen (vorher gefragt!) zeigen kurz am Beamer oder vom eigenen Laptop: *Welche Aufgabe? Welcher Prompt? Was kam raus? Was musstest du korrigieren?* Je max. 2–3 Minuten.
- Du würdigst und ergänzt: *„Achtet darauf, was sie gemacht hat: Kontext gegeben, Format vorgegeben, zweimal nachgebessert. Genau so.“*
- Achtung: Beim Zeigen am Beamer nur grüne Inhalte.

**2:58–3:02 · Hilfe und nächste Schritte (ca. 4 Minuten)**

- **Die drei Kernbotschaften zum Mitnehmen:**
  1. *Daten-Ampel beachten – im Zweifel rot.*
  2. *Ihr bleibt verantwortlich – wichtige Inhalte immer prüfen.*
  3. *Kontext geben und nachbessern – die erste Antwort ist ein Entwurf.*
- **Wo gibt’s Hilfe?**
  - Spickzettel ([05_Spickzettel.md](05_Spickzettel.md)) an den Monitor kleben.
  - Fragen zu Zugang/Technik: [ANSPRECHPARTNER IT].
  - Fragen zu Daten/Datenschutz: [DATENSCHUTZBEAUFTRAGTE/R].
  - Austausch und Tipps untereinander: [TIPPS-KANAL].
- **Hausaufgabe (freiwillig):** *„Probiert diese Woche drei echte Aufgaben mit der KI aus – Daten-Ampel beachten – und notiert kurz, was geklappt hat. Postet euren besten Prompt im [TIPPS-KANAL].“* (Gleicher Wortlaut wie in der Follow-up-Mail, siehe [08_Nachbereitung.md](08_Nachbereitung.md).)
- **Folgetermin** ankündigen: kurzes Treffen in 2–4 Wochen zum Erfahrungsaustausch (Details in [08_Nachbereitung.md](08_Nachbereitung.md)).
- Offene Fragen vom Flipchart: kurz beantworten oder zusagen, dass die Antwort mit der Follow-up-Mail kommt.

**3:02–3:05 · Feedback (ca. 3 Minuten)**

- Feedbackbogen aus [08_Nachbereitung.md](08_Nachbereitung.md) ausfüllen lassen (Papier oder Online-Umfrage).
- Optional Blitzlicht: *„Ein Wort: Wie geht ihr raus?“*
- Danke sagen, verabschieden.

**Zeitpuffer-Tipps:**
- Nur 1–2 Ergebnisse zeigen statt 3.
- Feedbackbogen zum Mitnehmen bzw. als Online-Link mit der Follow-up-Mail.
- **Nicht weglassen:** die drei Kernbotschaften und die Info, wo es Hilfe gibt.

---

## 4. Variante: 2 × 90 Minuten

Wenn drei Stunden am Stück schwer zu organisieren sind, teilst du das Tutorial auf zwei Termine. Ideal: **Abstand von 1–7 Tagen**, damit die Teilnehmenden zwischendurch selbst ausprobieren können.

### Termin 1 (90 Minuten) – Grundlagen

| Zeit | Inhalt |
|---|---|
| 0:00–0:15 | Block 1 „Was ist KI eigentlich?“ |
| 0:15–0:30 | Block 2 „Spielregeln“ |
| 0:30–1:00 | Block 3 „Übung 1: Texte schreiben“ |
| 1:00–1:30 | Block 4 „Gute Prompts“ inkl. Übung 2 |

- In den letzten Minuten von Block 4 eine **Mini-Hausaufgabe** geben: *„Nutzt die KI bis zum nächsten Mal für eine echte (grüne!) Aufgabe. Und bringt eure lästige Aufgabe für Übung 4 mit.“*
- Die eigentliche Abschlussrunde fällt hier weg; zwei Minuten für Fragen am Ende einplanen (notfalls bei Übung 2 kürzen).

### Termin 2 (90 Minuten) – Anwendung

| Zeit | Inhalt |
|---|---|
| 0:00–0:10 | Kurze Wiederholung: Daten-Ampel, Prompt-Baukasten, Erfahrungen mit der Hausaufgabe (Folie: Anhang B in [04_Folien.md](04_Folien.md)) |
| 0:10–0:50 | Block 5 „Übung 3: Mit Dokumenten und Tabellen arbeiten“ |
| 0:50–1:20 | Block 6 „Übung 4: Deine eigene Aufgabe“ |
| 1:20–1:30 | Block 7 „Ergebnisse & Abschluss“ (verkürzt auf 10 Minuten) |

**Tipps für die Wiederholung (10 Minuten):**

- *„Wer hat seit dem letzten Mal etwas ausprobiert? Was hat geklappt, was nicht?“* – 2–3 Stimmen.
- Daten-Ampel mit zwei, drei schnellen „Welche Farbe?“-Beispielen auffrischen.
- Die fünf Bausteine des Prompt-Baukastens vom [Spickzettel](05_Spickzettel.md) mit der Merkhilfe wiederholen: *Wer? · Worum? · Was? · Wie? · Wie genau?* – plus: nachsteuern.

**Hinweis:** Da Block 7 auf 10 Minuten verkürzt ist, nur 1–2 Ergebnisse zeigen und den Feedbackbogen ggf. als Online-Link nachschicken.

---

## 5. Moderationstipps für gemischte Gruppen

### Die Skeptikerin / der Skeptiker

*„Das ist doch alles Hype.“ – „Da kommt eh nur Quatsch raus.“*

- **Ernst nehmen, nicht überzeugen wollen.** Skepsis ist berechtigt und passt zur Botschaft des Tages („prüfen!“).
- Formulierung: *„Da hast du in Teilen recht – wir haben ja gerade gesehen, wie sie danebenliegt. Lass uns herausfinden, wofür sie bei dir trotzdem nützlich ist – und wofür nicht.“*
- Gib ihr/ihm eine Rolle: *„Du bist heute unser Fehlerdetektiv. Wenn du was findest, zeig’s uns.“*
- Nicht in Grundsatzdiskussionen verstricken. Max. 2 Minuten, dann: *„Lass uns das in der Pause weiter besprechen.“*

### Die Überfliegerin / der Überflieger

*Ist mit jeder Übung nach 5 Minuten fertig.*

- **Bonusaufgaben** auf den Übungsblättern anbieten.
- Als **Co-Helfer** einsetzen: *„Magst du mal bei Team 3 schauen? Die hängen beim Upload.“* (Achtung: freundlich, nicht als Strafarbeit.)
- Anspruchsvollere Herausforderung: *„Bring die KI dazu, dir zuerst Rückfragen zu stellen und dann eine Vorlage zu bauen, die du jede Woche wiederverwenden kannst.“*

### Die Unsicheren

*Trauen sich nicht zu tippen, haben Angst, etwas falsch zu machen.*

- **Zweierteam mit einer geduldigen, neugierigen Person.**
- Früh kleine Erfolgserlebnisse sichern: Bei Übung 1 zuerst vorbeigehen.
- Formulierung: *„Du kannst hier wirklich nichts kaputt machen. Schreib einfach so, als würdest du einer Kollegin eine Nachricht schicken.“*
- Nicht vor der Gruppe vorführen oder bloßstellen. Beim Zeigen von Ergebnissen nur Freiwillige.
- Tippen lassen, nicht für sie tippen. Höchstens diktieren.

### „Ich hab das schon alles gemacht“

*Nutzt KI privat täglich und fühlt sich unterfordert.*

- **Wertschätzen und einbinden:** *„Super, dann bist du heute unser Praxisexperte. Was ist dein bester Tipp?“* (Einmal, kurz – nicht die Show übernehmen lassen.)
- Auf die Unterschiede hinweisen, die oft neu sind: **Daten-Ampel, Firmenlizenz vs. privates Konto, Verantwortung für Ergebnisse.** Gerade erfahrene Nutzer haben oft Gewohnheiten, die dienstlich nicht passen.
- Anspruchsvollere Varianten anbieten: Versionsvergleich ohne Hilfe auf Vollständigkeit prüfen, wiederverwendbare Prompt-Vorlagen für das Team erstellen.
- Als Kandidat für den [TIPPS-KANAL] oder eine Fortgeschrittenen-Session gewinnen (Ideen in [08_Nachbereitung.md](08_Nachbereitung.md)).

### Allgemeine Tipps

- **Namen verwenden**, Namensschilder bereitlegen.
- **Fehler normalisieren:** Wenn bei dir etwas schiefgeht, lach drüber und nutze es als Beispiel.
- **„Offene Fragen“-Flipchart** als Parkplatz für Themen, die den Ablauf sprengen.
- **Nicht zu viel erklären.** Wenn eine Frage nur eine Person betrifft, beantworte sie beim Herumgehen.
- **Ruhe bewahren bei Technikproblemen** – deine Gelassenheit überträgt sich auf die Gruppe.
- **Keine Bewertung der Arbeitsweise einzelner Abteilungen** („Das macht ihr ja noch total umständlich“). Es geht ums Ausprobieren, nicht um Kritik.

---

## 6. Troubleshooting

| Problem | Sofortmaßnahme | Wenn das nicht hilft |
|---|---|---|
| **Kein Login / Zugang funktioniert nicht** | Browser wechseln, privates Fenster probieren, Pop-up-Blocker prüfen, ggf. Cache leeren. Prüfen, ob die richtige (Firmen-)Mailadresse verwendet wird. | Person setzt sich zum Teampartner und arbeitet mit dessen Laptop mit (Zweierteams sind dafür ideal). Reserve-Login nutzen, falls mit IT vereinbart. [ANSPRECHPARTNER IT] per Telefon/Chat informieren. |
| **Mehrere Logins gehen nicht** | Ruhig bleiben, Block 1/2 laufen ohne Login. Helfer kümmert sich parallel. | Größere Teams (3–4 Personen) an funktionierenden Laptops bilden, Reserve-Logins verteilen. **Niemals private Gratis-Konten als Ersatz empfehlen.** |
| **WLAN ist weg oder sehr langsam** | Router/Access-Point prüfen, Gastnetz probieren, einige Teilnehmende aus dem WLAN nehmen (ein Laptop pro Team reicht). | Mobilen Hotspot nur nach Firmenregeln nutzen. Sonst: **Beamer-Demo** – du arbeitest vorn, die Gruppe diktiert dir Prompts und bewertet die Antworten. Wenn auch dein Zugang ausfällt: vorbereitete **Screenshots** zeigen und die Übungen als „Prompt auf Papier schreiben, gemeinsam besprechen“ durchführen. |
| **Upload geht nicht** | Prüfen: Wird das richtige Symbol (Büroklammer/Upload) genutzt? Ist der Dateityp unterstützt? Datei evtl. umbenennen oder in ein anderes Format speichern. | **Text kopieren und in den Chat einfügen** – funktioniert fast immer. Bei der CSV-Datei: Datei mit einem Texteditor öffnen und den Inhalt einfügen. Falls Upload bei eurer Lizenz grundsätzlich gesperrt ist, weißt du das aus der Vorbereitung und planst von Anfang an mit Einfügen. |
| **KI verweigert eine Antwort** | Nachfragen, warum. Oft hilft mehr Kontext: *„Das ist eine fiktive Übungsmail für eine interne Schulung.“* | Als Lernmoment nutzen: Die Tools haben Schutzmechanismen, die manchmal übervorsichtig sind. Umformulieren oder Aufgabe wechseln. |
| **KI antwortet seltsam / falsch / in falscher Sprache** | Neuen Chat starten (alte Gesprächsverläufe können die Antwort beeinflussen). Prompt präzisieren. | Positiv nutzen: *„Seht ihr, genau deshalb prüfen wir.“* Bei Bedarf Screenshot machen für Block 7. |
| **Antworten sind sehr langsam / Tool überlastet** | Kurz warten, Seite neu laden, Gruppe beruhigen. | Pause vorziehen. Antworten gemeinsam lesen statt jede Person einzeln abschicken lassen. |
| **Antwort ist abgeschnitten** | *„Bitte mach weiter“* bzw. *„Schreib den Rest“* eingeben. | Aufgabe in kleinere Teile zerlegen. |
| **Gruppe ist zu schnell** | Bonusaufgaben der Übungsblätter, Block 6 früher starten und verlängern, mehr Ergebnisse in Block 7 zeigen. | Zusätzliche Mini-Challenge: *„Baut euch einen Prompt, den ihr jede Woche wiederverwenden könnt, und speichert ihn.“* |
| **Gruppe ist zu langsam** | Input kürzen (Block 1, 2, 4), pro Übung nur die Kernaufgaben, Auswertungen kürzen. | Block 5 auf eine Aufgabe reduzieren. **Block 6 schützen.** Notfalls Feedback per Online-Link nachreichen. |
| **Laptop-Akku leer** | Mehrfachsteckdose bereithalten. | Beim Teampartner mitarbeiten. |
| **Beamer funktioniert nicht** | Adapter prüfen, anderer Anschluss, Bildschirm duplizieren (Windows: Windows-Taste + P). | Ohne Beamer: Teilnehmende arbeiten selbst, du gehst herum. Demos an einem Laptop für kleine Gruppen zeigen. |

---

## 7. FAQ: Antworten auf schwierige Fragen

Diese Antworten sind Formulierungsvorschläge. Sei ehrlich – auch „Das weiß ich nicht, ich kläre das“ ist eine gute Antwort. Juristische Fragen gibst du an [DATENSCHUTZBEAUFTRAGTE/R] bzw. die zuständigen Stellen weiter; du gibst keine Rechtsberatung.

### „Nimmt mir die KI den Job weg?“

> *„Ehrlich gesagt: Niemand kann genau vorhersagen, wie sich Arbeit in den nächsten Jahren verändert. Was man heute sieht: KI übernimmt vor allem einzelne Aufgaben – Entwürfe schreiben, zusammenfassen, umformulieren –, nicht ganze Berufe. Euer Fachwissen, eure Kontakte, euer Urteilsvermögen und die Verantwortung bleiben bei euch. Gerade deshalb ist es sinnvoll, das Werkzeug zu kennen: Wer es gut einsetzt, hat mehr Zeit für die Teile der Arbeit, die wirklich Erfahrung brauchen. Und genau deswegen machen wir dieses Tutorial.“*

Keine Versprechungen machen („Hier wird niemand ersetzt“), die du nicht halten kannst – das ist Sache der Geschäftsleitung. Wenn die Frage drängend wird, ehrlich sagen, dass du sie weitergibst.

### „Was passiert mit meinen Daten?“

> *„Alles, was du eintippst oder hochlädst, wird an die Server des Anbieters geschickt und dort verarbeitet. Was danach damit passiert – wie lange es gespeichert wird, ob es zum Weitertrainieren genutzt wird –, hängt vom Anbieter und vom Vertrag ab. Für unsere Firmenlizenz gilt: [HIER DIE MIT IT/DATENSCHUTZ GEKLÄRTE ANTWORT EINTRAGEN]. Deshalb haben wir die Daten-Ampel: Was rot ist, kommt gar nicht erst rein.“*

Wenn du die Antwort für eure Lizenz nicht sicher weißt: nicht raten. *„Das kläre ich mit [ANSPRECHPARTNER IT] und schicke die Antwort mit der Follow-up-Mail.“*

### „Darf ich das privat oder mit meinem Gratis-Konto nutzen?“

> *„Privat für private Dinge: Das ist deine Sache – die Daten-Ampel ist aber auch privat ein guter Kompass. Für dienstliche Inhalte gilt: Bitte nur den Firmenzugang nutzen. Bei privaten Gratis-Konten können andere Bedingungen gelten, zum Beispiel ob deine Eingaben zum Training genutzt werden, und die Firma hat dafür keinen Vertrag mit dem Anbieter. [GGF. FIRMENREGEL EINTRAGEN, Z. B. ‚Dienstliche Nutzung privater Konten ist nicht erlaubt.‘]“*

### „Wie erkenne ich falsche Antworten?“

> *„Leider oft gar nicht auf den ersten Blick – falsche Antworten klingen genauso überzeugend wie richtige. Deshalb ein paar Faustregeln:*
> - *Zahlen, Daten, Namen, Zitate und Quellen immer selbst prüfen.*
> - *Bei Dokumenten fragen: ‚Wo genau steht das?‘ und im Original nachsehen.*
> - *Misstrauisch werden, wenn die Antwort sehr konkret ist, obwohl du keine konkreten Infos gegeben hast.*
> - *Nachfragen: ‚Bist du sicher? Was davon könnte falsch sein?‘ – das hilft manchmal, ersetzt aber nicht die eigene Prüfung.*
> - *Und vor allem: Nutze KI vor allem für Themen, bei denen du selbst beurteilen kannst, ob das Ergebnis stimmt.“*

### „Wer haftet, wenn die KI einen Fehler macht?“

> *„Rechtlich im Detail kann ich das nicht beantworten – das ist keine Frage für ein Tutorial, sondern für die Rechtsabteilung bzw. die Geschäftsleitung. Praktisch ist die Regel für uns aber klar: Was du verschickst oder entscheidest, verantwortest du – genauso, als hättest du es ohne KI gemacht. Die KI ist ein Werkzeug wie eine Rechtschreibprüfung oder ein Taschenrechner. ‚Das hat die KI geschrieben‘ ist keine Ausrede.“*

### „Wie sieht es mit Stromverbrauch und Umwelt aus?“

> *„Berechtigte Frage. Das Trainieren und Betreiben großer KI-Modelle braucht viel Rechenleistung und damit Energie und Kühlung in Rechenzentren. Wie viel genau eine einzelne Anfrage verbraucht, lässt sich schwer pauschal sagen – Schätzungen gehen auseinander und hängen stark von Modell und Rechenzentrum ab. Ein pragmatischer Umgang: KI dort einsetzen, wo sie echten Nutzen bringt, und nicht für Spielereien zwanzigmal neu generieren lassen. Wenn dich das Thema interessiert, lohnt es sich, aktuelle unabhängige Quellen dazu zu lesen.“*

Keine konkreten Zahlen nennen, die du nicht belegen kannst.

### „Wem gehören die Ergebnisse? Wie ist das mit dem Urheberrecht?“

> *„Das ist rechtlich ein komplexes und teils noch offenes Feld, und ich bin kein Jurist. Ein paar Punkte, die man trotzdem sagen kann: Die Nutzungsbedingungen der Anbieter regeln, wie man die Ergebnisse verwenden darf – für unsere Lizenz klärt das [ANSPRECHPARTNER IT]. Rein von KI erzeugte Texte sind nach verbreiteter Auffassung oft nicht in gleicher Weise urheberrechtlich geschützt wie menschliche Werke. Und die KI kann theoretisch Formulierungen erzeugen, die bestehenden Texten ähneln. Für Alltags-E-Mails und interne Dokumente ist das in der Praxis selten ein Problem. Bei Texten für Veröffentlichungen, Werbung oder Verträge: bitte vorher mit den zuständigen Stellen sprechen.“*

### „Warum gibt sie jedes Mal eine andere Antwort?“

> *„Weil das Sprachmodell nicht stur immer das eine wahrscheinlichste Wort nimmt, sondern ein bisschen Zufall eingebaut ist. Dadurch klingen die Texte natürlicher und abwechslungsreicher. Der Nachteil: Dieselbe Frage kann unterschiedliche Antworten bringen – manchmal besser, manchmal schlechter, manchmal sogar inhaltlich anders. Für euch heißt das: Wenn euch eine Antwort nicht gefällt, einfach neu generieren lassen oder nachbessern. Und: Ein richtiges Ergebnis heute garantiert nicht, dass es morgen wieder richtig ist. Auch das ist ein Grund, wichtige Inhalte zu prüfen.“*

### Weitere Fragen, die häufig kommen

**„Kennt die KI aktuelle Ereignisse / das Internet?“**
> *„Das Modell wurde mit Texten bis zu einem bestimmten Zeitpunkt trainiert. Manche Tools können zusätzlich im Internet suchen, andere nicht – das hängt vom Werkzeug und von den Einstellungen ab. Wenn es um Aktuelles geht, immer prüfen, ob die KI wirklich gesucht hat und welche Quellen sie nennt.“*

**„Kann die KI auf unsere Systeme, Laufwerke oder E-Mails zugreifen?“**
> *„Das hängt vom Werkzeug und von den Einstellungen ab – manche KI-Assistenten lassen sich mit anderen Programmen verbinden. In den Übungen heute sieht sie nur, was du in den Chat schreibst oder hochlädst. Für unseren Zugang gilt: [HIER DIE MIT IT/DATENSCHUTZ GEKLÄRTE ANTWORT EINTRAGEN].“*

**„Muss ich angeben, dass ein Text mit KI erstellt wurde?“**
> *„Dafür gibt es bei uns [FIRMENREGEL EINTRAGEN / noch keine feste Regel]. Für interne Entwürfe meist nicht nötig. Bei Texten nach außen oder bei Veröffentlichungen: bitte mit [ANSPRECHPARTNER IT] bzw. der Kommunikationsabteilung abklären.“*

**„Ist das jetzt Pflicht?“**
> *„Die Nutzung ist ein Angebot. Unternehmen, die KI einsetzen, müssen allerdings seit Februar 2025 nach der EU-KI-Verordnung Maßnahmen ergreifen, damit Mitarbeitende, die mit KI arbeiten, über ausreichende KI-Kompetenz verfügen – dazu trägt dieses Tutorial bei.“* (Nur sagen, wenn mit Personalabteilung/Leitung so abgestimmt.)

---

## 8. Materialliste

Alle Dateien liegen im Tutorial-Ordner. Übersicht und Index: [README.md](README.md).

### Für dich (Trainer)

| Datei | Inhalt | Wann |
|---|---|---|
| [README.md](README.md) | Übersicht und Index aller Materialien | Einstieg |
| [01_Trainer-Leitfaden.md](01_Trainer-Leitfaden.md) | Dieser Leitfaden | Vorbereitung + am Tag |
| [04_Folien.md](04_Folien.md) | Folieninhalte Folie für Folie mit Sprechernotizen | Vorbereitung (in Präsentationsprogramm übertragen) + am Tag |
| [06_Uebungen/Trainer-Loesungshinweise.md](06_Uebungen/Trainer-Loesungshinweise.md) | Musterlösungen, Beispielprompts, typische Stolpersteine zu allen Übungen | Vorbereitung + beim Herumgehen |
| [07_Beispielmaterial/demo_fehler_zeigen.md](07_Beispielmaterial/demo_fehler_zeigen.md) | Demo-Prompts für typische KI-Schwächen (vorher testen, Screenshots als Backup) | Block 1 |

### Vorher verschicken

| Datei | Inhalt | Wann |
|---|---|---|
| [02_Einladung_und_Vorbereitung.md](02_Einladung_und_Vorbereitung.md) | Einladungs-Mail, Erinnerungs-Mail, Einrichtungsanleitung, Vorab-Umfrage | 2 Wochen / 1 Tag vorher |
| [03_Daten-Ampel.md](03_Daten-Ampel.md) | Datenregeln grün/gelb/rot – **Vorlage, mit IT/Datenschutz abstimmen** | 4 Wochen vorher abstimmen, in Block 2 verteilen |

### Ausdrucke für Teilnehmende

| Datei | Inhalt | Block |
|---|---|---|
| [03_Daten-Ampel.md](03_Daten-Ampel.md) | Daten-Ampel (abgestimmte Fassung) | 2 |
| [05_Spickzettel.md](05_Spickzettel.md) | Einseitiger Spickzettel | 2 (am Ende von Folie 9 austeilen), begleitet alle Übungen, zum Mitnehmen |
| [06_Uebungen/Uebung_1_Texte_schreiben.md](06_Uebungen/Uebung_1_Texte_schreiben.md) | Übungsblatt 1 | 3 |
| [06_Uebungen/Uebung_2_Gute_Prompts.md](06_Uebungen/Uebung_2_Gute_Prompts.md) | Übungsblatt 2 | 4 |
| [06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md](06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md) | Übungsblatt 3 | 5 |
| [06_Uebungen/Uebung_4_Eigene_Aufgabe.md](06_Uebungen/Uebung_4_Eigene_Aufgabe.md) | Übungsblatt 4 | 6 |
| [08_Nachbereitung.md](08_Nachbereitung.md) (Feedbackbogen) | Feedbackbogen | 7 |

### Beispielmaterial zum Herunterladen (fiktive Firma „Nordlicht Technik GmbH“)

| Datei | Inhalt | Block |
|---|---|---|
| [07_Beispielmaterial/kundenmail_beschwerde.txt](07_Beispielmaterial/kundenmail_beschwerde.txt) | Verärgerte Kundenmail wegen Lieferverzug | 1 (Demo), 3 |
| [07_Beispielmaterial/notizen_besprechung.txt](07_Beispielmaterial/notizen_besprechung.txt) | Chaotische Besprechungsnotizen mit versteckten Aufgaben und Terminen | 4, 5 |
| [07_Beispielmaterial/lieferantenliste_unsortiert.csv](07_Beispielmaterial/lieferantenliste_unsortiert.csv) | Unordentliche Lieferantentabelle (Semikolon-getrennt) | 5 |
| [07_Beispielmaterial/pruefbericht_lang.md](07_Beispielmaterial/pruefbericht_lang.md) | Langer technischer Prüfbericht zum Zusammenfassen | 5 |
| [07_Beispielmaterial/richtlinie_reisekosten_v1.md](07_Beispielmaterial/richtlinie_reisekosten_v1.md) | Reisekostenrichtlinie, Version 1 | 5 |
| [07_Beispielmaterial/richtlinie_reisekosten_v2.md](07_Beispielmaterial/richtlinie_reisekosten_v2.md) | Reisekostenrichtlinie, Version 2 (genau 7 inhaltliche Unterschiede zu v1) | 5 |
| [07_Beispielmaterial/demo_fehler_zeigen.md](07_Beispielmaterial/demo_fehler_zeigen.md) | Demo-Prompts für KI-Schwächen (nur für dich) | 1 |

### Nachbereitung

| Datei | Inhalt | Wann |
|---|---|---|
| [08_Nachbereitung.md](08_Nachbereitung.md) | Feedbackbogen, Follow-up-Mail, Tipps-Kanal-Idee, Folgetermin nach 2–4 Wochen, Ideen für Fortgeschrittenen-Session | Direkt danach bis 4 Wochen danach |

### Sonstiges, das du brauchst

- Laptop mit Zugang zu [KI-TOOL], Ladekabel, Adapter für Beamer
- Mehrfachsteckdosen (mind. eine pro zwei Tische)
- Flipchart/Whiteboard + Stifte (Ablauf, WLAN-Daten, Links, „Offene Fragen“)
- Namensschilder
- Optional: farbige Karten grün/gelb/rot für die Ampel-Aktivierung
- Backup: Screenshots der Demos, Beispielmaterial auf USB-Stick, 2–3 Reserve-Logins (mit IT abgestimmt)

---

*Viel Erfolg! Und denk dran: Du musst nicht alles wissen. „Gute Frage – lass es uns zusammen ausprobieren“ ist oft die beste Antwort des Tages.*
