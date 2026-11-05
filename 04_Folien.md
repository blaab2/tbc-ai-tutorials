# Folien: KI im Arbeitsalltag

*Folieninhalte mit Sprechernotizen · [FIRMENNAME] · [DATUM] · [RAUM]*

Dieses Dokument enthält alle Folien für das ca. 3-stündige Tutorial – Folie für Folie, in der Reihenfolge des Ablaufplans. Der Ablauf und die Hintergründe stehen im [Trainer-Leitfaden](01_Trainer-Leitfaden.md).

---

## So baust du daraus PowerPoint- oder Google-Folien

1. **Eine Überschrift „## Folie N – …“ = eine Folie.** Der Titel nach dem Gedankenstrich wird der Folientitel.
2. **Der Folieninhalt** (Stichpunkte) kommt auf die Folie. Bleib bei höchstens fünf Stichpunkten und großer Schrift (mind. 24 pt) – die Leute sollen zuhören und mitmachen, nicht lesen.
3. **Bildvorschläge** stehen in *(Klammern, kursiv)*. Die HTML-Präsentation enthält dazu fertige, animierte Grafiken. Nach `./build.sh` liegen sie als SVG-Dateien unter `html/assets/folien/` und lassen sich in PowerPoint oder Google Präsentationen einfügen (dort ohne Animation). Du kannst auch eigene Fotos, Symbole aus der Firmenvorlage oder lizenzfreie Bilder nehmen. Die Klammertexte selbst kommen nicht auf die Folie.
4. **Die Sprechernotiz** kopierst du in das Notizfeld unter der Folie (in PowerPoint: „Notizen“, in Google Präsentationen: „Vortragsnotizen“). Dann siehst du sie in der Referentenansicht.
5. **Blockwechsel** sind mit einer Zeile wie `⏱ BLOCK 3 · 0:30–1:00` markiert. Am besten setzt du dort eine Abschnittsfolie oder zumindest eine kleine Zeitangabe in die Fußzeile – das hilft dir, im Plan zu bleiben.
6. **Platzhalter** in eckigen Großbuchstaben (z. B. [KI-TOOL], [LINK ZUM TOOL]) ersetzt du vorher durch die echten Angaben.
7. **Tipp:** Du kannst dir die Folien auch vom KI-Assistenten vorbereiten lassen – z. B. „Mach aus diesem Folientext eine Gliederung für eine Präsentation, eine Folie pro Abschnitt.“ Kontrollier das Ergebnis aber, bevor du es zeigst.

**Anhang A** (Backup bei Technikproblemen) und **Anhang B** (Wiederholung für Termin 2 bei der Variante „2 × 90 Minuten“) sind ausgeblendete Zusatzfolien.

**Variante 2 × 90 Minuten:** Termin 1 = Folien 1–16 (Blöcke 1–4, Folie 16 endet mit dem Abschluss von Termin 1). Termin 2 = Anhang B, dann Folien 18–26 (Blöcke 5–7). Die Pausenfolie 17 entfällt bzw. wird zur Abschlussfolie von Termin 1.

---

### Überblick

| Block | Zeit | Folien |
|---|---|---|
| 1 – Was ist KI eigentlich? | 0:00–0:15 | 1–6 |
| 2 – Spielregeln | 0:15–0:30 | 7–9 |
| 3 – Übung 1: Texte schreiben | 0:30–1:00 | 10–11 |
| 4 – Gute Prompts (inkl. Übung 2) | 1:00–1:30 | 12–16 |
| Pause | 1:30–1:40 | 17 |
| 5 – Übung 3: Mit Dokumenten und Tabellen arbeiten | 1:40–2:20 | 18–20 |
| 6 – Übung 4: Deine eigene Aufgabe | 2:20–2:50 | 21–22 |
| 7 – Ergebnisse & Abschluss | 2:50–3:05 | 23–26 |
| Anhang | – | A, B |

---

`⏱ BLOCK 1 · 0:00–0:15 · Was ist KI eigentlich?`

## Folie 1 – KI im Arbeitsalltag

**KI im Arbeitsalltag**
Praktisch ausprobieren – mit deinen eigenen Aufgaben

- [FIRMENNAME] · [DATUM] · [RAUM]
- Trainer: [DEIN NAME]
- WLAN: [WLAN-NAME] · Tool: [KI-TOOL] · [LINK ZUM TOOL]

*(Bild: Laptop auf einem Schreibtisch mit Kaffeetasse, freundlich und alltäglich – keine Roboter, keine leuchtenden Gehirne.)*

**Sprechernotiz:**
Diese Folie läuft schon, während die Leute ankommen. Begrüße alle persönlich an der Tür und bitte sie, den Laptop gleich aufzuklappen, ins WLAN zu gehen und [LINK ZUM TOOL] zu öffnen – die Angaben stehen auf der Folie.
Zum Start: „Schön, dass ihr da seid! Heute gibt es keinen langen Vortrag. Ihr werdet in den nächsten drei Stunden selbst ganz viel ausprobieren – und zwar mit Aufgaben, die ihr wirklich aus eurem Job kennt. Ihr braucht keinerlei Vorwissen. Wer heute zum ersten Mal mit so einem Tool arbeitet, ist hier genau richtig.“
Kurz zu dir: wer du bist und warum du das Thema spannend findest – eine persönliche Anekdote, wo dir KI im Alltag Zeit gespart hat, wirkt besser als jede Statistik.

---

## Folie 2 – Unser Plan für heute

- **Verstehen:** Was ist KI – und was nicht? (15 Min.)
- **Spielregeln:** Welche Daten dürfen rein? (15 Min.)
- **Ausprobieren:** Texte · gute Prompts · Dokumente & Tabellen
- **Deine Aufgabe:** Eine echte Aufgabe aus deinem Alltag im Team lösen
- **Abschluss:** Ergebnisse zeigen, nächste Schritte, Feedback (Dauer insgesamt gut 3 Std.)

*(Grafik: Zeitstrahl mit 7 Stationen, Pause nach ca. 1,5 Std. als Kaffeetasse markiert. Etwa zwei Drittel des Balkens farbig als „selbst machen“ hervorgehoben.)*

**Sprechernotiz:**
„So sieht unser Plan für heute aus. Ihr seht: Der größte Teil ist Selbermachen. Ich erzähle nur kurz was am Anfang und zwischendurch – den Rest macht ihr. Nach etwa anderthalb Stunden gibt es zehn Minuten Pause.“
„Am Ende soll jede und jeder von euch drei bis vier echte Aufgaben mit KI erledigt haben – und genau wissen, welche Daten ihr eingeben dürft und welche nicht.“
Hinweis auf Zweierteams: „Ihr arbeitet heute zu zweit. Setzt euch gern neben jemanden, den ihr noch nicht so gut kennt.“ (Wenn du die Vorab-Umfrage ausgewertet hast, kannst du die Teams vorschlagen: eher Unsichere neben eher Neugierige.)
Organisatorisches: Toiletten, Getränke, Handys leise. Und: „Es gibt heute keine dummen Fragen. Wirklich nicht.“

---

## Folie 3 – Warum wir das machen

- KI-Assistenten sind im Alltag angekommen – auch bei uns
- Sie können lästige Schreib- und Sortierarbeit abnehmen
- Sie machen aber auch Fehler – und man muss wissen, welche
- Ziel heute: **sicher und sinnvoll** nutzen, nicht blind vertrauen
- Du entscheidest, wofür du es einsetzt

*(Bild: Waage – auf der einen Seite „Zeit sparen“, auf der anderen „Kopf einschalten“, im Gleichgewicht.)*

**Sprechernotiz:**
„Viele von euch haben so ein Tool schon mal ausprobiert, manche nutzen es regelmäßig, andere noch nie. Alles okay.“
Kurze Handabfrage: „Wer hat schon mal einen KI-Chat benutzt? Wer nutzt es regelmäßig? Wer hat es noch nie ausprobiert?“ – nicht kommentieren, nur zur Orientierung.
„Damit eines klar ist: Es geht heute nicht darum, jemanden zu ersetzen. KI ist ein Werkzeug – wie damals die Tabellenkalkulation. Wer sie gut bedienen kann, spart sich lästige Arbeit und hat mehr Zeit für das, was wirklich Fachwissen braucht. Aber man muss wissen, wo die Grenzen sind. Genau darum geht es heute.“
Optional, ein Satz: „Übrigens verlangt die europäische KI-Verordnung (EU AI Act) in Artikel 4 seit Februar 2025, dass Unternehmen, die KI einsetzen, Maßnahmen für ausreichende KI-Kompetenz ihrer Beschäftigten ergreifen. Diese Schulung ist ein Baustein dafür – aber vor allem soll sie euch im Alltag helfen.“

---

## Folie 4 – Wie funktioniert ein Sprachmodell?

**Autovervollständigung auf Steroiden**

- Ein **Sprachmodell** hat aus riesigen Textmengen gelernt, wie Sprache funktioniert
- Es sagt Stück für Stück vorher, welcher Text am wahrscheinlichsten passt
- Dadurch kann es erstaunlich gut schreiben, zusammenfassen, übersetzen
- Es „weiß“ nichts im menschlichen Sinn – es erzeugt plausiblen Text
- **Es kennt [FIRMENNAME] nicht** – nur das, was du ihm gibst

*(Grafik: links ein Smartphone mit Wortvorschlägen über der Tastatur – „Ich komme heute etwas …“ → „später“ / „früher“ / „spät“. Rechts derselbe Gedanke riesig: ein ganzer Absatz, der Wort für Wort entsteht. Pfeil dazwischen: „gleiches Prinzip, viel, viel größer“.)*

**Sprechernotiz:**
„Kennt ihr die Wortvorschläge auf dem Handy? Ihr tippt ‚Ich komme heute etwas …‘ und das Handy schlägt ‚später‘ vor. Ein Sprachmodell – so nennt man die Technik hinter dem KI-Assistenten – funktioniert im Kern ähnlich: Es sagt vorher, welches Textstück als Nächstes am wahrscheinlichsten passt. Nur hat es dafür aus unvorstellbar vielen Texten gelernt, und es berücksichtigt den ganzen bisherigen Zusammenhang – eure Frage, die bisherige Unterhaltung, hochgeladene Dokumente.“
„Danach wurde es zusätzlich darauf trainiert, hilfreich auf Anweisungen zu antworten. Deshalb kann es nicht nur Sätze vervollständigen, sondern Mails schreiben, Texte zusammenfassen, übersetzen oder Tabellen aufräumen.“
„Wichtig: Es schlägt nicht in einer Datenbank nach, ob etwas stimmt. Es erzeugt Text, der *plausibel* klingt. Meistens ist plausibel auch richtig – aber nicht immer. Und: Es kennt unsere Firma nicht. Es weiß nichts über unsere Kunden, Produkte oder Abläufe – außer ihr schreibt es ihm hinein.“
Falls jemand fragt, ob das Tool im Internet sucht: „Manche Tools können zusätzlich im Internet suchen oder Dateien lesen. Dann arbeitet die KI mit diesen Inhalten – aber das Grundprinzip bleibt dasselbe, und auch dann kann sie danebenliegen. Wer das macht, Modell oder Tool, zeige ich auf der nächsten Folie.“
Nicht in technische Details abschweifen. Wenn die Analogie sitzt, reicht das völlig.

---

## Folie 4b – Motor und Auto: Modell vs. Werkzeug

**Das Modell ist der Motor – das Tool ist das Auto**

- **Motor = Sprachmodell:** erzeugt Text – sonst nichts
- **Auto = [KI-TOOL]:** Chatfenster, Datei-Upload, Websuche, Rechnen, Firmen-Einstellungen
- **Der Motor hat kein Gedächtnis:** Jede Nachricht beginnt für ihn bei null
- Das Tool schickt bei jeder Nachricht **den ganzen Chat** noch einmal mit
- **Neuer Chat = leeres Blatt** – wichtigen Kontext neu mitgeben

*(Grafik: Links ein Auto im Querschnitt. In der Mitte der Motor, beschriftet „Sprachmodell“. Drumherum beschriftete Teile des Autos: Lenkrad = Eingabefeld, Kofferraum = hochgeladene Dateien, Navi = Websuche, Handschuhfach = Rechner/Werkzeuge. Rechts ein kleiner Ablauf in drei Schritten: Bei jeder neuen Nachricht wandert der komplette Stapel aus Fragen und Antworten in den Motor – und der Stapel wird jedes Mal etwas dicker.)*

**Sprechernotiz:**
„Wenn wir ‚die KI‘ sagen, meinen wir eigentlich zwei Dinge. Das kann man sich vorstellen wie bei einem Auto.“
„Der **Motor** ist das Sprachmodell von eben: Es bekommt Text und erzeugt Text. Mehr nicht. Es kann von sich aus nicht im Internet nachschauen, keine Dateien öffnen und nichts abspeichern.“
„Das **Auto** drumherum ist das Programm, das ihr gleich im Browser öffnet: [KI-TOOL]. Das Auto baut das Chatfenster, nimmt eure Dateien entgegen, sucht – falls eingeschaltet – im Internet, benutzt einen Taschenrechner und hält sich an die Einstellungen unserer Firmenlizenz. Das Ergebnis reicht es dann an den Motor weiter.“
„Derselbe Motor kann in ganz verschiedenen Autos stecken: in einem Chatprogramm im Browser, in Copilot in Word und Outlook oder in Werkzeugen für Programmierer wie Claude Code oder GitHub Copilot. Die lesen dann sogar selbst Dateien und führen Befehle aus. Deshalb kann sich dasselbe Modell in zwei Tools ganz unterschiedlich anfühlen. Und wenn ihr gleich im Tool ein anderes Modell auswählt, tauscht ihr den Motor – das Auto bleibt dasselbe.“
**Kernpunkt – zustandslos:** „Jetzt kommt das Überraschende: Der Motor hat **kein Gedächtnis**. Zwischen zwei Nachrichten merkt er sich gar nichts. Dass sich das trotzdem wie ein Gespräch anfühlt, macht das Auto: Bei jeder neuen Nachricht schickt das Tool den **kompletten bisherigen Chat** noch einmal mit – eure Fragen, seine Antworten, die hochgeladenen Dateien. Das Modell liest jedes Mal alles von vorn und schreibt dann weiter.“
Bild dazu: „Stellt euch eine Aushilfe vor, die jeden Morgen kommt und sich an nichts von gestern erinnert. Damit sie weitermachen kann, legt ihr ihr jedes Mal die ganze Akte auf den Tisch. Genau das macht das Tool – bei jeder einzelnen Nachricht.“
Was das für euch heißt (kurz, nur ansprechen):
- **Neuer Chat = leeres Blatt.** Was ihr in einem anderen Chat erklärt habt, weiß er dort nicht. Für ein neues Thema bewusst einen neuen Chat starten und den nötigen Kontext wieder mitgeben.
- **Sehr lange Chats:** Irgendwann wird die Akte zu dick. Dann kürzt das Tool oder fasst ältere Teile zusammen, und Details vom Anfang gehen unter. Lieber einen neuen Chat mit kurzer Zusammenfassung beginnen.
- **„Aber mein Tool kennt doch meinen Namen!“** Manche Tools haben eine Erinnerungs- oder Projektfunktion. Auch das ist das Auto: Es speichert Notizen und legt sie unbemerkt mit in die Akte. Der Motor selbst lernt während eures Chats nichts dazu.
Brücke zu Block 2: „Und was mit euren Eingaben passiert – ob sie gespeichert werden, wie lange, ob sie zum Training künftiger Modelle verwendet werden dürfen – das entscheidet nicht der Motor, sondern das Auto und unser Vertrag mit dem Anbieter. Dazu gleich mehr bei den Spielregeln.“
Maximal 2–3 Minuten. Die Fahrzeugbeispiele (Copilot, Claude Code) nur nennen, nicht erklären – es sei denn, die Gruppe ist neugierig.

---

## Folie 5 – Was KI gut kann – und was nicht

| 👍 Kann sie gut | 👎 Da musst du aufpassen |
|---|---|
| Entwürfe schreiben, umformulieren, kürzen | Fakten, Zahlen, Quellen – manchmal erfunden |
| Übersetzen und Ton anpassen | Aktuelle Ereignisse |
| Lange Texte zusammenfassen | Zählen und genaues Rechnen |
| Notizen und Tabellen ordnen | Alles über [FIRMENNAME] |
| Ideen sammeln, Fragen stellen | Klingt immer sicher – auch wenn's falsch ist |

*(Grafik: Zweispaltige Tabelle, links grün mit Daumen hoch, rechts orange mit Warndreieck.)*

**Sprechernotiz:**
„Links seht ihr, wofür sich KI im Büroalltag richtig lohnt: alles rund um Sprache und Struktur. Rechts die typischen Schwachstellen.“
Fachbegriff erklären: „Wenn eine KI etwas erfindet und das überzeugend darstellt, nennt man das **Halluzination**. Zum Beispiel ein Buch, das es nicht gibt, ein Paragraf, der anders lautet, oder eine Statistik aus dem Nichts. Das ist kein ‚Lügen‘ – das Modell erzeugt einfach plausiblen Text, auch wenn es die Antwort eigentlich nicht kennt.“
„Das Tückische ist die letzte Zeile: Die KI klingt immer gleich selbstbewusst. Ob sie richtig oder falsch liegt, seht ihr am Ton nicht.“
„Faustregel: Die KI ist wie eine sehr schnelle, sehr belesene neue Kollegin, die am ersten Tag da ist. Sie formuliert super, aber sie kennt unsere Firma nicht und hat manchmal falsche Erinnerungen. Ihre Arbeit würdet ihr auch gegenlesen.“

---

## Folie 6 – Live-Demo: Wow – und Hoppla

- **Wow:** Aus drei Stichworten wird eine fertige Mail – auf Deutsch und Englisch
- **Hoppla:** Wir fragen etwas, das die KI nicht wissen kann
- Achte darauf: Wie sicher klingt die Antwort?
- Ergebnisse können bei euch anders aussehen – das ist normal

*(Folie bewusst leer halten, nur Überschrift „Live-Demo“ – dann zum Browser wechseln. Backup: Screenshots der vorab getesteten Demo als ausgeblendete Folien dahinter.)*

**Sprechernotiz:**
Wechsle zum Browser mit [KI-TOOL]. Die Demo-Prompts findest du in [demo_fehler_zeigen.md](07_Beispielmaterial/demo_fehler_zeigen.md). **Teste sie am Vortag mit genau dem Tool und Konto, das du im Kurs nutzt, und mach Screenshots als Backup** – die Antworten variieren von Mal zu Mal und je nach Tool.
**Teil 1 – Wow (ca. 2 Min.):** Lass dir aus ein paar Stichworten eine höfliche Mail schreiben (z. B. „Mail an Kunden: Lieferung verschiebt sich um 1 Woche, Grund Materialengpass, wir bieten kostenlosen Expressversand an“). Dann: „Jetzt bitte etwas lockerer.“ Dann: „Und jetzt auf Englisch.“ Lass die Leute die Geschwindigkeit sehen. Dann kurz gegenlesen lassen: Steht noch „1 Woche“ drin – oder „etwa eine Woche“? Hat die KI etwas dazuerfunden (z. B. einen Lieferanten als Ursache)? Wie bekommt der Kunde den Expressversand – automatisch oder auf Nachfrage? Bei langen Antworten nur Betreff, Anrede und den Satz mit der Woche zeigen.
**Teil 2 – Hoppla (ca. 3 Min.):** Nimm ein bis zwei Beispiele aus der Demo-Datei, z. B. eine Frage nach Fachliteratur mit genauen Quellenangaben, eine Zählaufgabe oder eine Frage zu [FIRMENNAME]. Frag laut in die Runde: „Klingt das überzeugend? Würdet ihr das so weitergeben?“ Dann zeigen, wo es falsch oder erfunden ist.
Falls die KI wider Erwarten alles richtig macht: „Diesmal hat's geklappt – beim Test gestern nicht.“ und den Screenshot zeigen. Das ist sogar eine gute Botschaft: Man weiß vorher nicht, wann es schiefgeht.
Überleitung: „Und genau deshalb brauchen wir ein paar Spielregeln.“

---

`⏱ BLOCK 2 · 0:15–0:30 · Spielregeln`

## Folie 7 – Die Daten-Ampel

- 🟢 **Grün – bedenkenlos:** öffentliche Infos, eigene Formulierungen, allgemeine Fragen, anonymisierte Texte
- 🟡 **Gelb – nur mit Firmenzugang, nach Prüfung und möglichst anonymisiert:** interne Dokumente, Entwürfe, Richtlinien – vorher Namen und Kundendaten entfernen
- 🔴 **Rot – niemals eingeben:** personenbezogene Daten (Kunden, Mitarbeitende), Gesundheitsdaten, Passwörter/Zugangsdaten, vertrauliche Verträge, Konstruktionsdaten/Geschäftsgeheimnisse, ggf. exportkontrollierte Infos
- **Im Zweifel: nicht eingeben, nachfragen.**

*(Grafik: Große Verkehrsampel, neben jedem Licht zwei, drei kleine Symbole – grün: Zeitungsartikel, Sprechblase; gelb: Dokument mit geschwärztem Namen; rot: Schloss, Ausweis, Bauplan, Herz/Gesundheit.)*

**Sprechernotiz:**
„Das ist die wichtigste Folie heute. Wenn ihr nur eine Sache mitnehmt, dann diese.“
Erkläre die drei Farben mit je einem Alltagsbeispiel:
- Grün: „Formulier mir eine Absage für eine Messe-Einladung“ oder „Erklär mir, was eine Pivot-Tabelle ist.“
- Gelb: Ein interner Ablaufplan ohne Namen, ein Entwurf einer Richtlinie – nur im Firmen-Tool und nachdem ihr Namen, Kundennummern usw. entfernt habt.
- Rot: „Die Krankmeldung von Kollege X“, „Die Kundenliste mit Adressen“, „Der Vertrag mit Lieferant Y“, „Die Konstruktionszeichnung“, „Mein Passwort“.
„Personenbezogene Daten – also alles, womit man eine echte Person erkennen kann – sind nach der DSGVO besonders geschützt. Deshalb sind die bei uns rot.“
Ganz wichtig: „Diese Ampel ist mit [ANSPRECHPARTNER IT] und [DATENSCHUTZBEAUFTRAGTE/R] abgestimmt.“ (Diesen Satz nur sagen, wenn das stimmt!) „Die ausführliche Fassung findet ihr in der Daten-Ampel.“ (Verweis auf [Daten-Ampel](03_Daten-Ampel.md).) **Vor dem Termin unbedingt prüfen, dass die Vorlage tatsächlich freigegeben ist, und die Folie an die finale Fassung anpassen.**
Mini-Quiz (2–3 Min., per Handzeichen): „Grün, gelb oder rot?“ – die Speisekarte der Kantine (grün) · ein Angebot an einen Kunden mit dessen Namen und Preisen (rot) · das interne Protokoll ohne Namen (gelb) · die Fehlermeldung eines Programms, ohne Zugangsdaten (grün/gelb).

---

## Folie 8 – Firmenlizenz oder Privatkonto?

- **Für Firmendaten nur:** [KI-TOOL] mit Firmenlizenz über [LINK ZUM TOOL]
- **Private Gratis-Konten sind für Firmendaten tabu**
- Grund: Was mit deinen Eingaben passiert (z. B. ob sie zum Training genutzt werden), regeln Lizenz und Einstellungen – das kann sich deutlich unterscheiden
- Auch im Firmen-Tool gilt: Rot bleibt rot
- Fragen dazu: [ANSPRECHPARTNER IT] · [DATENSCHUTZBEAUFTRAGTE/R]

*(Grafik: Zwei Türen – eine mit Firmenlogo „Firmenlizenz“ (offen, gelber und grüner Bereich dahinter), eine mit „Privat / Gratis“ (für Firmendaten durchgestrichen).)*

**Sprechernotiz:**
„Eine Frage, die immer kommt: Kann ich nicht einfach mein privates Konto nehmen? Für Firmendaten: nein.“
„Bei vielen Anbietern hängt es von der Art des Kontos und den Einstellungen ab, was mit euren Eingaben passiert – zum Beispiel, ob sie gespeichert oder zum Verbessern des Modells verwendet werden dürfen. Für die Firmenlizenz gelten die Bedingungen, die [FIRMENNAME] mit dem Anbieter vereinbart hat. Für euer privates Konto gelten die nicht.“ (Was genau in eurer Lizenz geregelt ist, klärst du vorher mit [ANSPRECHPARTNER IT] – sag nur, was du sicher weißt.)
Formuliere hier nichts Produktspezifisches, was du nicht sicher weißt. Wenn jemand Details wissen will: „Das klären wir mit der IT – ich nehme die Frage mit.“ Schreib dir die Frage auf und beantworte sie in der Follow-up-Mail.
„Und auch mit Firmenlizenz: Rote Daten bleiben draußen. Die Lizenz macht aus Rot nicht Grün.“

---

## Folie 9 – Du bleibst verantwortlich

- Die KI liefert einen **Entwurf** – du entscheidest, was rausgeht
- **Immer gegenprüfen:** Zahlen, Namen, Termine, Quellen, Paragrafen
- **Besonders genau:** alles, was an Kunden, Behörden oder nach außen geht
- Warnzeichen: Klingt sehr sicher, aber du kannst es nicht nachprüfen
- Faustregel: Was du nicht beurteilen kannst, lässt du prüfen

*(Bild: Hand mit Stift, die einen ausgedruckten Text abhakt – Symbol „Vier-Augen-Prinzip: deine zwei Augen zählen“.)*

**Sprechernotiz:**
„Die zweite Spielregel ist ganz einfach: Die Verantwortung für das Ergebnis bleibt bei euch. Wenn ihr eine Mail mit KI schreibt und darin steht ein falscher Liefertermin, dann hat nicht ‚die KI‘ den Fehler gemacht, sondern die Mail kam von euch.“
„Wann müsst ihr besonders gründlich prüfen? Immer wenn es Zahlen, Namen, Termine oder Quellen gibt – und immer, wenn etwas nach außen geht. Bei einem Brainstorming für die Weihnachtsfeier reicht ein kurzer Blick.“
Die drei Warnzeichen aus dem [Spickzettel](05_Spickzettel.md) kurz erwähnen: genaue Zahlen/Quellen/Links, Aussagen über die Firma oder Aktuelles, „klingt sicher, kann ich aber nicht prüfen“.
Teile jetzt den Spickzettel aus (ausgedruckt) – er begleitet die Leute durch alle Übungen.
Überleitung: „Genug Theorie. Jetzt seid ihr dran.“

---

`⏱ BLOCK 3 · 0:30–1:00 · Übung 1: Texte schreiben`

## Folie 10 – Los geht's: Tool öffnen

1. [LINK ZUM TOOL] im Browser öffnen
2. Mit deinem Firmenkonto anmelden
3. Neuen Chat starten
4. Ersten Satz eintippen: „Hallo! Erklär mir in zwei Sätzen, was du kannst.“
5. Klappt's? Daumen hoch 👍 – sonst Hand heben ✋
6. Kurz anschauen: Wo wählst du das **Modell**? (⚡ schnell · ⭐ stark · 🧠 Nachdenken)

*(Screenshot-Platzhalter: Startseite von [KI-TOOL] mit markiertem Eingabefeld und „Neuer Chat“. Screenshot vorab selbst machen – Menüs sehen je nach Tool und Version anders aus.)*

**Sprechernotiz:**
Gib allen zwei bis drei Minuten. Geh sofort herum und schau, wer hängt.
Typische Probleme: Login funktioniert nicht, falscher Browser, Konto noch nicht freigeschaltet, VPN/WLAN. **Kein langes Troubleshooting im Kurs** – wer nicht reinkommt, arbeitet mit dem Teampartner an einem Laptop weiter. Notier dir die Namen und kläre das Problem später mit [ANSPRECHPARTNER IT].
Wenn das WLAN oder der Login für viele ausfällt: Backup-Plan aus **Anhang A** (geteilte Logins, Beamer-Demo, Arbeit zu dritt).
„Ihr seht: Man schreibt einfach ganz normal, wie in einem Chat. Was ihr da eintippt, nennt man übrigens **Prompt** – das ist einfach eure Anweisung oder Frage an die KI. Das Wort werdet ihr heute noch öfter hören.“
Zum Schluss zeigst du am Beamer, wo man das Modell umschaltet (30 Sekunden, nicht mehr): „Für Texte reicht das voreingestellte Modell. Bei Zahlen, Tabellen und langen Dokumenten schaltet ihr auf [STARKES MODELL] bzw. [DENK-MODUS] – das steht auch auf dem Spickzettel und in der [Modellauswahl](05b_Modellauswahl.md).“ Gibt es bei eurer Lizenz nur ein Modell, lässt du Schritt 6 weg.

---

## Folie 11 – Übung 1: Texte schreiben

**Deine Aufgabe (zu zweit, ca. 20 Minuten):**
- Antworte auf eine verärgerte Kundenmail (Lieferverzug)
- Ändere den Ton: förmlicher, lockerer, kürzer
- Übersetze ins Englische – und zurück
- Bonus: Verbessere eine eigene Mail (ohne rote Daten!)

📄 Übungsblatt: **Übung 1 – Texte schreiben** · Material: `kundenmail_beschwerde.txt`

*(Grafik: Briefumschlag mit Pfeilen zu drei Varianten – „förmlich“, „locker“, „EN“. Großer Timer „20 Min.“ in der Ecke.)*

**Sprechernotiz:**
Verweis auf das Übungsblatt [Übung 1 – Texte schreiben](06_Uebungen/Uebung_1_Texte_schreiben.md) und die Beispieldatei [kundenmail_beschwerde.txt](07_Beispielmaterial/kundenmail_beschwerde.txt). Sag, wo die Dateien liegen ([LINK ZU DEN MATERIALIEN] / Ordner / ausgedruckt).
„Die Kundenmail ist erfunden – die Firma Nordlicht Technik GmbH gibt es nicht. Deshalb dürft ihr die komplett reinkopieren. Bei echten Kundenmails müsstet ihr vorher Namen und Kundendaten entfernen – Daten-Ampel!“
„Fangt ruhig ganz einfach an: ‚Schreib eine Antwort auf diese Mail.‘ Und dann schaut, was passiert, wenn ihr nachsteuert. Ihr müsst nicht alle Aufgaben schaffen.“
Stell einen Timer sichtbar ein (20 Min., 0:35–0:55). Geh herum, hör zu, lob gute Ideen laut („Schaut mal, was die beiden hier gemacht haben …“). Sammle zwei, drei gute Beispiele für die Überleitung zu Block 4.
Musterlösungen und typische Stolpersteine: [Trainer-Lösungshinweise](06_Uebungen/Trainer-Loesungshinweise.md).
Fünf Minuten vor Ende kurze Ansage. Zum Abschluss (0:55–1:00, ca. 5 Min.): „Wer hat eine Antwort bekommen, die schon richtig gut war? Wer war unzufrieden?“ – Unzufriedenheit ist die perfekte Überleitung: „Dann schauen wir jetzt, wie man bessere Antworten bekommt.“

---

`⏱ BLOCK 4 · 1:00–1:30 · Gute Prompts`

## Folie 12 – Warum ist die Antwort mal super und mal mau?

- Die KI weiß nur, was in deinem Prompt steht
- Kurzer Prompt = die KI muss raten = Durchschnittsantwort
- Stell dir vor: Du gibst die Aufgabe einer neuen Kollegin am ersten Tag
- Was müsste sie wissen, um es gleich richtig zu machen?

*(Bild: Zwei Sprechblasen – eine winzig („Schreib was über Lieferung“), eine ausführlich. Daneben ein ratloses und ein zufriedenes Gesicht.)*

**Sprechernotiz:**
„Ihr habt gerade gemerkt: Manchmal kommt sofort was Brauchbares, manchmal ist es zu lang, zu steif oder an der Sache vorbei. Das liegt fast immer am Prompt.“
„Denkt an eine neue Kollegin am ersten Tag. Wenn ihr sagt ‚Schreib mal dem Kunden‘, wird sie zurückfragen: Welcher Kunde? Worum geht's? Wie förmlich? Die KI fragt meistens nicht zurück – sie rät einfach. Und wenn sie rät, kommt Mittelmaß raus.“
„Die gute Nachricht: Es gibt ein paar Bausteine, mit denen eure Prompts sofort besser werden.“

---

## Folie 13 – Der Prompt-Baukasten

| Baustein | Frage | Beispiel |
|---|---|---|
| **1. Rolle** | Wer soll die KI sein? | „Du bist eine erfahrene Kundenbetreuerin …“ |
| **2. Kontext** | Worum geht es, für wen? | „… bei einem technischen Hersteller. Der Kunde wartet seit 2 Wochen.“ |
| **3. Aufgabe** | Was genau soll passieren? | „Schreib eine Antwort-Mail.“ |
| **4. Format** | Wie soll das Ergebnis aussehen? | „Max. 120 Wörter, freundlich, Sie-Form.“ |
| **5. Beispiel** | Gibt es eine Vorlage? | „So klingen unsere Mails: …“ |

**Merkhilfe: Wer? · Worum? · Was? · Wie? · Wie genau?**

*(Grafik: Fünf Bauklötze übereinander, jeder mit einem Baustein beschriftet. Oben drauf ein Häkchen „gute Antwort“.)*

**Sprechernotiz:**
„Das hier ist der Prompt-Baukasten. Fünf Bausteine – ihr findet sie auch oben auf eurem Spickzettel.“
Geh die Bausteine einzeln durch:
- **Rolle:** „Wer soll die KI sein? Eine erfahrene Kundenbetreuerin schreibt anders als ein Jurist.“
- **Kontext:** „Das ist der wichtigste Baustein. Die KI kennt unsere Firma nicht – also erzählt ihr, worum es geht und für wen der Text ist.“
- **Aufgabe:** „Was genau soll rauskommen? Eine Mail, eine Liste, drei Varianten?“
- **Format:** „Länge, Ton, Aufbau. Stichpunkte oder Fließtext? Du oder Sie?“
- **Beispiel:** „Wenn ihr eine alte Mail habt, deren Stil euch gefällt, gebt sie als Beispiel mit – natürlich ohne rote Daten.“
„Merkhilfe: Wer? Worum? Was? Wie? Wie genau? Ihr müsst nicht jedes Mal alle fünf verwenden. Aber je wichtiger das Ergebnis, desto mehr Bausteine lohnen sich.“

---

## Folie 14 – Schlechter vs. guter Prompt

| ❌ Schwach | ✅ Stark |
|---|---|
| „Schreib eine Mail an den Lieferanten wegen der Lieferung.“ | „Du bist Einkäuferin bei einem kleinen technischen Hersteller. **(Rolle)** Unser Lieferant hat die Lieferung von 500 Dichtungsringen zum zweiten Mal um eine Woche verschoben. Wir brauchen sie spätestens am 15. für einen Kundenauftrag. **(Kontext)** Schreib eine E-Mail, in der du um einen verbindlichen Liefertermin bis Freitag bittest. **(Aufgabe)** Höchstens 120 Wörter, freundlich, aber bestimmt, mit Betreffzeile, Sie-Form. **(Format)** Der Ton soll ungefähr so sein: „Wir schätzen die Zusammenarbeit, brauchen jetzt aber Verlässlichkeit.“ **(Beispiel)**“ |
| → Allgemeine, lange Mail, Details erfunden oder Platzhalter | → Passende Mail, fast versandfertig |

*(Layout: Zwei Spalten nebeneinander, links grau/rot, rechts grün. Die Bausteine im starken Prompt farbig markiert – passend zu den Farben der Bauklötze auf Folie 13.)*

**Sprechernotiz:**
„Schauen wir uns das mal live an.“ Wechsle zum Browser und gib **beide** Prompts nacheinander ein – jeweils in einem neuen Chat, damit sich die Antworten nicht beeinflussen.
Lass die Gruppe vergleichen: „Was ist der Unterschied? Welche Mail würdet ihr eher abschicken?“
Typische Beobachtungen beim schwachen Prompt: Die KI liefert eine allgemeine Vorlage mit vielen Platzhaltern wie [Bestellnummer] und stellt Rückfragen – manche Tools erfinden stattdessen Details (Bestellnummer, Datum). Lass zählen: Wie viele Lücken müsste ich noch füllen? Und achte auf Sätze ohne Klammer, die etwas behaupten (z. B. „Fotos haben wir beigefügt“). Beim starken Prompt: konkret, richtige Länge, richtiger Ton. Platzhalter für Name, Firma oder das genaue Datum sind auch hier normal – sie markieren, was nur ihr wissen könnt. Schlecht sind Platzhalter oder Erfindungen bei den eigentlichen Inhalten (Menge, Frist, Anliegen).
„Der starke Prompt hat vielleicht 40 Sekunden länger gedauert. Dafür müsst ihr danach kaum noch nacharbeiten.“
Wichtig: „Die Zahlen und Daten im Beispiel sind erfunden. Bei echten Lieferanten: Namen und vertrauliche Konditionen weglassen oder neutral umschreiben – ‚unser Lieferant‘ reicht der KI völlig.“

---

## Folie 15 – Nachfragen und verbessern

- **Nicht neu anfangen – einfach nachsteuern:**
- „Kürzer, bitte – maximal 3 Sätze.“ · „Weniger förmlich.“
- „Das stimmt nicht: … Bitte überarbeiten.“ · „Gib mir drei Varianten.“
- **Joker:** „Stell mir erst bis zu 3 Fragen, bevor du loslegst.“
- Die erste Antwort ist ein Entwurf – nicht das Endergebnis

*(Grafik: Kreislauf-Pfeil mit drei Stationen „Fragen → Antwort lesen → nachschärfen“. Daneben eine Sprechblase „Stell mir erst Fragen“ als Joker-Karte.)*

**Sprechernotiz:**
„Das Schöne an einem Chat: Ihr müsst nicht beim ersten Versuch perfekt sein. Ihr könnt einfach weiterreden wie mit einem Menschen. Innerhalb eines Chats berücksichtigt die KI, was ihr bisher geschrieben habt – in einem neuen Chat fängt sie wieder bei null an.“
Live zeigen (1–2 Min.): Nimm die Mail aus Folie 14 und schreib „Kürzer und etwas wärmer“. Dann: „Gib mir noch eine Variante, die mit einer Frage beginnt.“ Kurz prüfen: Ist beim Kürzen etwas weggefallen (z. B. „um eine Woche“) oder dazugekommen? In Tests hat die KI einmal „Eine weitere Verschiebung können wir nicht auffangen“ ergänzt. Mit einer Zahl dazu („höchstens 60 Wörter“) wird „kürzer“ genauer.
„Und jetzt mein Lieblingstrick, der Joker: Wenn ihr selbst noch nicht genau wisst, was ihr braucht, schreibt einfach: ‚Ich möchte X. Stell mir zuerst bis zu 3 Fragen, bevor du loslegst.‘ Dann interviewt euch die KI – und ihr merkt oft erst dadurch, was eigentlich wichtig ist.“
Kurzer Hinweis: „Wenn ein Chat sehr lang und durcheinander wird, lieber einen neuen Chat anfangen und das Wichtigste neu reinkopieren.“

---

## Folie 16 – Übung 2: Gute Prompts

**Deine Aufgabe (zu zweit, ca. 18 Minuten):**
- **A + B:** Minimal-Prompt gegen Baukasten-Prompt – Antworten vergleichen
- **C oder D:** Joker „Stell mir zuerst Fragen“ – oder Schritt für Schritt nachsteuern
- **E:** Deinen eigenen Prompt zum Wiederverwenden bauen (bitte nicht auslassen!)
- Für Schnelle: F und G

📄 Übungsblatt: **Übung 2 – Gute Prompts** · Spickzettel liegt bereit

*(Grafik: Die fünf Bauklötze aus Folie 13 klein in der Ecke, dazu Timer „18 Min.“)*

**Sprechernotiz:**
Verweis auf [Übung 2 – Gute Prompts](06_Uebungen/Uebung_2_Gute_Prompts.md). Timer auf ca. 18 Minuten (1:12–1:30); für den Input auf den Folien 12–15 hast du also nur ca. 12 Minuten. Tipp aus dem Übungsblatt: Für A und B zwei getrennte Chats nehmen (oder Person 1 macht A, Person 2 macht B) und die Ergebnisse nebeneinanderlegen. Achte darauf, dass alle bis Aufgabe E kommen – der eigene Prompt ist das, was nach dem Kurs bleibt.
„Ihr habt gesehen, wie viel die Bausteine bringen. Jetzt probiert ihr es selbst. Vergleicht immer: Was kam beim schwachen Prompt raus, was beim starken?“
Geh herum. Achte besonders darauf, ob jemand echte Kundendaten oder Namen eingibt – freundlich darauf hinweisen, ohne die Person bloßzustellen.
Musterlösungen: [Trainer-Lösungshinweise](06_Uebungen/Trainer-Loesungshinweise.md).
In den letzten 2 Minuten: „Wer hat einen Prompt, auf den er stolz ist? Lies ihn mal vor.“ – ein Beispiel reicht.
**Variante 2 × 90 Min.:** Hier endet Termin 1. Kurze Abschlussrunde: „Was war heute neu für euch?“ Hausaufgabe: „Probiert bis zum nächsten Termin ein- bis zweimal den Prompt-Baukasten bei einer echten Aufgabe aus – Daten-Ampel beachten. Und überlegt euch eine lästige Aufgabe, die ihr beim nächsten Mal mitbringt.“

---

`⏱ PAUSE · 1:30–1:40`

## Folie 17 – Pause

**10 Minuten Pause**
Weiter geht's um [UHRZEIT]

- Kurz die Beine vertreten, Kaffee holen
- Laptops dürfen offen bleiben
- Fragen? Komm gern zu mir

*(Bild: Kaffeetasse. Optional ein großer Countdown-Timer.)*

**Sprechernotiz:**
Trag die konkrete Uhrzeit ein, zu der es weitergeht – das wirkt besser als „in 10 Minuten“.
Nutze die Pause, um bei denen nachzuhaken, die im ersten Teil Probleme hatten (Login, Unsicherheit). Bereite für Block 5 den Upload der Beispieldateien vor und prüf, dass die Dateien auf allen Wegen erreichbar sind.
Pünktlich wieder anfangen – Block 6 braucht seine Zeit.

---

`⏱ BLOCK 5 · 1:40–2:20 · Übung 3: Mit Dokumenten und Tabellen arbeiten`

## Folie 18 – Die KI liest für dich mit

- **Datei hochladen:** über das Büroklammer- oder Upload-Symbol – oder Text reinkopieren
- **Zusammenfassen:** „Fasse in 5 Stichpunkten für die Geschäftsführung zusammen.“
- **Kernpunkte finden:** „Welche Fristen, Risiken und Aufgaben stehen drin?“
- **Vergleichen:** „Was hat sich zwischen Version 1 und 2 geändert?“
- ⚠️ **Vorher Daten-Ampel:** Was hochgeladen wird, ist eingegeben!

*(Grafik: Dokumentenstapel → Trichter → drei saubere Stichpunkte. Kleines Ampel-Symbol in der Ecke.)*

**Sprechernotiz:**
„Bisher haben wir mit kurzen Texten gearbeitet. Jetzt wird's richtig nützlich: lange Dokumente.“
**Zeit im Blick:** Für die Folien 18 und 19 zusammen hast du nur ca. 5 Minuten (1:40–1:45), damit für Übung 3 rund 27 Minuten (1:45–2:12) und für die Auswertung ca. 8 Minuten (2:12–2:20) bleiben – so steht es auch im Übungsblatt.
Live-Demo (ca. 3–4 Min.): Lade [pruefbericht_lang.md](07_Beispielmaterial/pruefbericht_lang.md) hoch (oder kopiere den Text rein) und frag: „Fasse den Bericht in 5 Stichpunkten zusammen. Nenne danach die 3 wichtigsten Risiken oder Fristen.“ Je nach Tool sieht das Upload-Symbol anders aus – zeig, wo es in eurem [KI-TOOL] ist.
Dann eine Kontrollfrage, die zeigt, dass man prüfen muss: „Auf welcher Seite / in welchem Abschnitt steht das?“ – und im Original nachsehen. Wichtig: Eine Aussage tatsächlich im Original aufschlagen, z. B. „alle Maße in Toleranz“ gegen Abschnitt 4, Zeile Schlitzbreite (0,13 mm bei ±0,10 mm). Oder prüfen, ob die 30 % Schlusszahlung und die Schulungslücke genannt sind. Bei einer Textdatei gibt es keine Seiten: Sagt die KI das ehrlich, ist das gut. Erfindet sie Seitenzahlen, ist das der Fehler. Kommt kein Fehler, nachschieben: „Rechne jede Zeile der Messwerttabelle in Abschnitt 4 nach.“ „Zusammenfassungen sind meistens gut. Aber manchmal lässt die KI etwas Wichtiges weg oder vermischt Details. Bei wichtigen Dokumenten: stichprobenartig im Original prüfen.“
Daten-Ampel noch einmal ganz deutlich: „Hochladen ist genau dasselbe wie Eintippen. Ein Vertrag mit Kundennamen ist rot – egal, ob ihr ihn abtippt oder als PDF hochladet.“

---

## Folie 19 – Ordnung in Notizen und Tabellen

- **Notizen → Protokoll:** Entscheidungen · Aufgaben (wer, was, bis wann) · offene Fragen
- **Chaos-Tabelle → aufgeräumt:** einheitliche Datumsformate und Schreibweisen
- **Dubletten und Lücken** markieren lassen
- **Checkliste erzeugen:** „Mach daraus eine Checkliste zum Abhaken.“
- Immer: „Zeig mir, was du geändert hast.“

*(Grafik: Links ein Zettel mit krakeligen Notizen und eine schiefe Tabelle, rechts eine saubere Tabelle mit Spalten „Wer – Was – Bis wann“. Pfeil dazwischen.)*

**Sprechernotiz:**
„Kennt ihr das? Nach einer Besprechung habt ihr wilde Notizen und keiner weiß mehr, wer was bis wann machen sollte. Oder eine Tabelle, in der jeder das Datum anders schreibt.“
Nur erwähnen, nicht vorführen (das machen die Teams selbst in Station C) – z. B. mit [notizen_besprechung.txt](07_Beispielmaterial/notizen_besprechung.txt): „Mach aus diesen Notizen ein Protokoll mit: Entscheidungen, Aufgaben (wer, was, bis wann), offene Fragen.“ Darin sind Termine und Aufgaben versteckt, die die KI herausholen soll.
Hinweis zu Tabellen: „Bei Tabellen ist die KI gut im Aufräumen von Schreibweisen und Formaten. Beim Zählen und Rechnen ist sie unzuverlässiger – erinnert euch an die Demo am Anfang. Lasst euch immer zeigen, was geändert wurde, und prüft Stichproben. Summen und Statistiken rechnet ihr lieber in der Tabellenkalkulation nach.“
„Und dann gleich der nächste Schritt: ‚Mach daraus eine Checkliste.‘ So wird aus einem Dokument direkt etwas, mit dem ihr arbeiten könnt.“

---

## Folie 20 – Übung 3: Dokumente und Tabellen

**Deine Aufgabe (zu zweit, ca. 27 Minuten) – wähle 1 bis 2 Stationen:**
- **A** Langen Prüfbericht zusammenfassen und Kernpunkte finden
- **B** Zwei Versionen der Reisekostenrichtlinie vergleichen
- **C** Besprechungsnotizen → Protokoll und Aufgabenliste (Bonus: Checkliste)
- **D** Unordentliche Lieferantenliste bereinigen
- Jede Station endet mit einem **Prüfschritt** – nicht weglassen!

📄 Übungsblatt: **Übung 3 – Dokumente und Tabellen** · Material im Ordner `07_Beispielmaterial`

*(Grafik: Vier kleine Kacheln A–D mit Dateisymbolen: Bericht, zwei Dokumente mit „≠“, Notizzettel mit Häkchenliste, Tabelle. Timer „27 Min.“)*

**Sprechernotiz:**
Verweis auf [Übung 3 – Dokumente und Tabellen](06_Uebungen/Uebung_3_Dokumente_und_Tabellen.md). Beispieldateien:
- [pruefbericht_lang.md](07_Beispielmaterial/pruefbericht_lang.md)
- [richtlinie_reisekosten_v1.md](07_Beispielmaterial/richtlinie_reisekosten_v1.md) und [richtlinie_reisekosten_v2.md](07_Beispielmaterial/richtlinie_reisekosten_v2.md)
- [notizen_besprechung.txt](07_Beispielmaterial/notizen_besprechung.txt)
- [lieferantenliste_unsortiert.csv](07_Beispielmaterial/lieferantenliste_unsortiert.csv)
„Sucht euch eine Station aus, die am ehesten zu eurem Job passt, und macht sie gründlich – wer fertig ist, nimmt eine zweite. Wer viel mit Zahlen und Listen arbeitet, nimmt die Lieferantenliste. Wer viel liest, den Bericht oder die Richtlinie. Und: Der Prüfschritt am Ende jeder Station ist Pflicht.“
Tipp für den Richtlinien-Vergleich: „Die beiden Versionen haben mehrere inhaltliche Unterschiede. Zählt mal nach, ob die KI alle findet!“ (Es sind genau **7** – die Versionsnummer im Kopf zählt nicht mit.) – die vollständige Liste der Unterschiede steht in den [Trainer-Lösungshinweisen](06_Uebungen/Trainer-Loesungshinweise.md). Ein schönes Aha-Erlebnis, wenn die KI einen Unterschied übersieht oder einen erfindet.
Falls der Upload bei jemandem nicht klappt: Datei öffnen, Inhalt kopieren, in den Chat einfügen – funktioniert genauso.
Auswertung (ca. 8 Min., 2:12–2:20): „Was hat geklappt? Habt ihr eine Antwort gefunden, bei der die KI danebenlag?“ – ein, zwei Beispiele einsammeln. Dann Überleitung: „Jetzt kommt der wichtigste Teil: eure eigene Aufgabe.“

---

`⏱ BLOCK 6 · 2:20–2:50 · Übung 4: Deine eigene Aufgabe`

## Folie 21 – Jetzt wird's persönlich

- Welche Aufgabe nervt dich regelmäßig? (Die aus der Vorab-Umfrage!)
- Ideen: Standard-Mails · Protokolle · Texte kürzen · Listen sortieren · Anleitungen schreiben
- **Erst prüfen:** Welche Daten brauchst du? Welche Ampelfarbe?
- Rote Daten durch Platzhalter ersetzen: „Kunde A“, „[Betrag]“
- Ziel: ein Ergebnis, das du nächste Woche wirklich nutzt

*(Bild: Werkzeugkasten mit der Aufschrift „Dein Alltag“, darin die fünf Bauklötze aus dem Prompt-Baukasten.)*

**Sprechernotiz:**
„In der Einladung habe ich euch gebeten, euch eine lästige Aufgabe aus eurem Alltag zu überlegen. Jetzt ist es so weit.“
„Wer keine Idee hat: Schaut auf die Liste auf der Folie oder ins Übungsblatt – da stehen Vorschläge. Oder fragt die KI: ‚Ich arbeite als [TÄTIGKEIT] in einem Unternehmen der Branche [BRANCHE]. Welche meiner typischen Aufgaben könntest du mir erleichtern? Gib mir 10 Ideen, die ohne vertrauliche Daten funktionieren.‘ Prüft bei jeder Idee: Welche Ampelfarbe hätten die Daten?“
Ganz wichtig, bevor es losgeht: „Echte Aufgaben heißt oft echte Daten. Bitte schaut vorher auf die Daten-Ampel. Ersetzt Namen durch ‚Kunde A‘ oder ‚Kollegin B‘, Beträge durch Platzhalter. Die KI braucht die echten Namen fast nie, um euch zu helfen.“
Wenn die Vorab-Umfrage ausgewertet ist: Nenne zwei, drei typische Aufgaben aus der Gruppe (anonym), um Ideen anzustoßen.

---

## Folie 22 – Übung 4: Deine eigene Aufgabe

**Zu zweit, ca. 27 Minuten (2:23–2:50):**
1. Eine Person erzählt ihre Aufgabe – die andere fragt nach
2. Gemeinsam prüfen: Ampel okay? Platzhalter nötig?
3. Prompt mit dem Baukasten bauen – nachsteuern
4. Ergebnis sichern: Prompt und Antwort speichern
5. Halbzeit nach ca. 12 Minuten: Rollen tauschen

📄 Übungsblatt: **Übung 4 – Eigene Aufgabe**

*(Grafik: Zwei Personen an einem Laptop, Sprechblasen; darunter kleiner Zeitstrahl mit „Halbzeit – tauschen“. Timer „27 Min.“)*

**Sprechernotiz:**
Verweis auf [Übung 4 – Eigene Aufgabe](06_Uebungen/Uebung_4_Eigene_Aufgabe.md).
„Ihr arbeitet zu zweit. Erst ist die eine Person dran, nach etwa zwölf Minuten tauscht ihr. Die zweite Person ist sozusagen der Coach: Sie fragt nach, achtet auf die Daten-Ampel und schlägt Bausteine vor.“
„Speichert euch am Ende den Prompt, der am besten funktioniert hat – zum Beispiel in einer Notiz-Datei. Den könnt ihr nächste Woche einfach wiederverwenden.“
Jetzt ist deine Hauptrolle: herumgehen, zuhören, helfen. Gib keine fertigen Prompts vor, sondern stell Fragen: „Was weiß die KI noch nicht über deine Aufgabe?“, „Wie soll das Ergebnis aussehen?“, „Hast du den Joker schon probiert?“
Merk dir zwei, drei Teams mit guten oder interessanten Ergebnissen (auch interessante Fehlschläge!) und frag sie, ob sie gleich kurz zeigen würden.
Halbzeit-Ansage nach ca. 12 Minuten: „Rollen tauschen!“ Wenn ein Team lieber gemeinsam an der spannenderen der beiden Aufgaben weiterarbeiten möchte, ist das auch in Ordnung (so steht es auch im Übungsblatt).
In den letzten 3 Minuten: „Bereitet kurz vor, was ihr gleich in zwei Minuten zeigen würdet.“

---

`⏱ BLOCK 7 · 2:50–3:05 · Ergebnisse & Abschluss`

## Folie 23 – Zeigt her!

- 2–3 Teams zeigen ihr Ergebnis (je ca. 2–3 Minuten)
- Was war die Aufgabe?
- Wie sah der Prompt aus – was hat geholfen?
- Was hat (noch) nicht geklappt?

*(Bild: Bühne mit Scheinwerfer oder einfach ein großes „Eure Ergebnisse“ mit Applaus-Symbol.)*

**Sprechernotiz:**
Hol die vorher gefragten Teams nach vorne bzw. lass sie ihren Bildschirm am Beamer zeigen. **Vorher kurz checken, dass auf dem Bildschirm keine roten Daten sichtbar sind.**
Stell jedem Team die drei Fragen von der Folie. Lob konkret: „Super, dass du der KI erst den Kontext gegeben hast“ oder „Schöner Fehlschlag – genau dafür ist Gegenprüfen da.“
„Ihr seht: Die Aufgaben sind ganz unterschiedlich, aber das Vorgehen ist immer gleich – Daten prüfen, Bausteine nutzen, nachsteuern, Ergebnis prüfen.“
Zeitlimit beachten: ca. 8 Minuten für diese Folie (2:50–2:58), damit noch Zeit für Abschluss (2:58–3:02) und Feedback (3:02–3:05) bleibt.

---

## Folie 24 – Was nehme ich mit?

- **KI = sehr gute Textmaschine**, kein Lexikon und kein Firmenwissen
- **Daten-Ampel:** Rot bleibt draußen – im Zweifel nachfragen
- **Prompt-Baukasten:** Rolle · Kontext · Aufgabe · Format · Beispiel
- **Nachsteuern** statt neu anfangen – und der Joker „Stell mir erst Fragen“
- **Du bist verantwortlich:** Immer gegenlesen, vor allem Zahlen und Namen

*(Grafik: Fünf Symbole in einer Reihe – Sprechblase, Ampel, Bauklötze, Kreislauf-Pfeil, Häkchen mit Lupe. Dieselben Symbole wie auf den jeweiligen Folien vorher.)*

**Sprechernotiz:**
„Lasst uns zum Schluss die fünf wichtigsten Punkte zusammenfassen.“ Geh die Punkte zügig durch – sie sind alle schon bekannt, deshalb reicht ein Satz pro Punkt.
„Alles davon steht auf eurem Spickzettel. Hängt ihn euch neben den Bildschirm.“
Kurze Runde, wenn Zeit ist (max. 1 Minute): „Sagt in einem Wort: Wofür werdet ihr die KI nächste Woche als Erstes nutzen?“ – Antworten einfach in den Raum rufen lassen.

---

## Folie 25 – Nächste Schritte & Hilfe

- **Diese Woche:** Drei echte Aufgaben mit KI ausprobieren – Spickzettel nutzen, Daten-Ampel beachten
- **Tipps teilen:** [TIPPS-KANAL] – gute Prompts und Fragen posten
- **Folgetermin:** [DATUM FOLGETERMIN] – Erfahrungen austauschen, offene Fragen
- **Technik & Login:** [ANSPRECHPARTNER IT]
- **Datenschutz:** [DATENSCHUTZBEAUFTRAGTE/R] · Daten-Ampel: [LINK ZU DEN MATERIALIEN]

*(Grafik: Wegweiser mit drei Schildern „Ausprobieren“, „Austauschen“, „Nachfragen“. Darunter Kontaktkacheln mit Foto/Name der Ansprechpersonen, falls gewünscht.)*

**Sprechernotiz:**
„Das Wichtigste ist jetzt: dranbleiben. Wer das Tool in den nächsten Tagen nicht anfasst, hat in zwei Wochen das meiste wieder vergessen. Nehmt euch für diese Woche drei echte Aufgaben vor – die erste am besten gleich die von heute. Und postet euren besten Prompt im [TIPPS-KANAL].“
„Im [TIPPS-KANAL] könnt ihr gute Prompts teilen und Fragen stellen. Keine Angst vor ‚dummen‘ Fragen – wenn ihr euch etwas fragt, fragen es sich andere auch.“
„In etwa zwei bis vier Wochen treffen wir uns noch einmal kurz: Was hat funktioniert, was nicht? Den Termin bekommt ihr mit der Follow-up-Mail.“
Ansprechpartner nennen und sagen, wofür sie zuständig sind. Die Follow-up-Mail mit allen Materialien schickst du am selben oder nächsten Tag (Vorlage in der [Nachbereitung](08_Nachbereitung.md)).

---

## Folie 26 – Danke! Dein Feedback, bitte

**Danke fürs Mitmachen!**

- Feedbackbogen: ca. 3 Minuten – jetzt gleich, anonym
- [LINK/QR-CODE ZUM FEEDBACK]
- Was war hilfreich? Was soll beim nächsten Mal anders sein?
- Fragen? Ich bin noch kurz da.

*(Bild: Großer QR-Code zum Feedbackbogen, daneben ein freundliches „Danke“. Optional ein Gruppenfoto-Hinweis, falls gewünscht und alle einverstanden sind.)*

**Sprechernotiz:**
„Vielen Dank, dass ihr so engagiert mitgemacht habt! Eine letzte Bitte: Füllt den Feedbackbogen aus – jetzt gleich, das dauert nur ein paar Minuten und ist anonym. Ich will das Training verbessern, und dafür brauche ich ehrliche Rückmeldungen. Auch Kritik.“
Feedbackbogen-Vorlage: [Nachbereitung](08_Nachbereitung.md). Wenn ihr Papier nutzt: Bögen jetzt austeilen und an der Tür einsammeln.
Gib bewusst die ca. 3 Minuten Zeit (3:02–3:05), bevor alle gehen – danach kommt erfahrungsgemäß kaum noch Feedback.
Bleib noch ein paar Minuten für Einzelfragen da. Notier offene Fragen für die Follow-up-Mail.

---

## Anhang A – Backup: Wenn die Technik streikt *(ausgeblendete Folie)*

- **WLAN weg / Login klappt nicht:** zu zweit oder zu dritt an einem funktionierenden Laptop
- **Geteilte Logins:** vorbereitete Test-Zugänge von [ANSPRECHPARTNER IT]
- **Tool komplett aus:** Beamer-Demo – Gruppe diktiert die Prompts, du tippst
- **Gar nichts geht:** Screenshots der Übungen besprechen, Prompts auf Papier formulieren
- Ruhig bleiben – Prompts schreiben üben geht auch offline

*(Keine Grafik nötig – reine Arbeitsfolie für dich.)*

**Sprechernotiz:**
Diese Folie ist ausgeblendet und nur für dich. Zeig sie, wenn du die Gruppe auf einen Plan B einschwören musst.
**Vorbereitung am Vortag:** Kläre mit [ANSPRECHPARTNER IT], ob es Ersatz-Zugänge gibt und ob gemeinsame Konten mit den Lizenzbedingungen vereinbar sind. Mach Screenshots aller Demos und je einer Beispiellösung pro Übung (siehe [Trainer-Lösungshinweise](06_Uebungen/Trainer-Loesungshinweise.md)). Halte einen mobilen Hotspot bereit, falls erlaubt.
Bei der Beamer-Demo: Lass die Gruppe den Prompt gemeinsam mit dem Baukasten formulieren – das ist sogar eine gute Übung für Block 4. Die Papier-Variante: Jedes Team schreibt einen Prompt mit allen fünf Bausteinen auf, ihr vergleicht und diskutiert, und du probierst die besten später aus und schickst die Ergebnisse mit der Follow-up-Mail.

---

## Anhang B – Wiederholung für Termin 2 *(nur bei der Variante 2 × 90 Minuten)*

**Was wissen wir noch?** (ca. 10 Minuten)

- Sprachmodell: Autovervollständigung auf Steroiden – plausibel ≠ richtig, ohne Gedächtnis (Motor vs. Auto)
- Daten-Ampel: grün · gelb · rot – im Zweifel nachfragen
- Prompt-Baukasten: Rolle · Kontext · Aufgabe · Format · Beispiel
- Nachsteuern und der Joker „Stell mir erst Fragen“
- Eure Erfahrungen seit dem letzten Mal?

*(Grafik: Die Symbole aus Folie 24 als Erinnerung, dazu ein Fragezeichen „Was ist euch seitdem passiert?“)*

**Sprechernotiz:**
Starte Termin 2 mit dieser Folie statt mit Folie 1. Ablauf: kurze Begrüßung, dann eine Mini-Abfrage: „Wer hat seit dem letzten Mal etwas ausprobiert? Was hat geklappt, was nicht?“ Zwei, drei Erfahrungen reichen.
Die Daten-Ampel kurz mit einer Quizfrage wiederholen, den Prompt-Baukasten mit einem Beispiel aus der Runde.
Danach direkt mit Folie 18 (Block 5) weitermachen. Die Zeiten verschieben sich entsprechend: 0:00–0:10 Wiederholung, 0:10–0:50 Block 5, 0:50–1:20 Block 6, 1:20–1:30 Block 7 (verkürzt auf 10 Min.: nur 1–2 Ergebnisse zeigen, Feedbackbogen notfalls als Link nachschicken) – Details im [Trainer-Leitfaden](01_Trainer-Leitfaden.md).
Login vorher noch einmal prüfen lassen, falls seit dem letzten Termin Passwörter abgelaufen sind.
