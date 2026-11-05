# Testlauf: Übung 1 / Weiter D – Eigene Mail verbessern (fiktives Beispiel)

**Herkunft:** [Uebung_1_Texte_schreiben.md, Aufgabe D](../06_Uebungen/Uebung_1_Texte_schreiben.md) · Abgleich mit [Trainer-Lösungshinweise, Übung 1](../06_Uebungen/Trainer-Loesungshinweise.md) · Daten-Ampel: [03_Daten-Ampel.md](../03_Daten-Ampel.md)

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Testmail:** Für den Test wurde eine erfundene Kollegenmail verwendet (Nachfrage nach Messeunterlagen für die „Industrietage“, Platzhalter [KOLLEGIN], [DATUM], [DURCHWAHL], [MEIN NAME]). Diese Mail gibt es im Material bisher **nicht** – siehe „Probleme im Material“.

**Prompt (Turn 1):** Startprompt aus dem Übungsblatt + Testmail. **Turn 2:** „Das klingt zu steif, so rede ich nicht. Schreib es lockerer.“

**Ziel laut Material:** Klare, freundliche, kurze Version der Mail, alle Platzhalter erhalten, danach genau 3 Stichpunkte zu den Änderungen; auf die Rückmeldung hin wird der Stil lockerer, ohne Inhalt zu verlieren. Daten-Ampel: nur Platzhalter, keine vertraulichen Daten.

**Soll (objektiv prüfbar):** Reihenfolge Mail → genau 3 Stichpunkte · Platzhalter [KOLLEGIN], [DATUM], [DURCHWAHL], [MEIN NAME] unverändert · Inhalt erhalten: Produktdatenblätter neue Gehäuse, Fotos vom Stand letztes Jahr, Frist [DATUM], Druckerei/Flyer, Rückrufangebot · Grammatik „wegen den Unterlagen“ korrigiert oder umgangen · Turn 2 spürbar lockerer, Du-Form bleibt, keine neuen Fakten · keine echten Namen/Nummern eingesetzt.

## Bewertung

Wortzahl Mailtext (ohne Anrede/Gruß/Betreff, per python3 gezählt): Original 82 Wörter.

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Reihenfolge: erst Mail, dann genau 3 Stichpunkte | ja | ja | ja (Stichpunkte recht lang, je 2–4 Sätze) |
| Alle 4 Platzhalter unverändert (T1 und T2) | ja | ja | ja |
| Datenblätter + Fotos erhalten | ja | ja (als Liste) | ja (als Liste) |
| Frist [DATUM] + Druckerei/Flyer erhalten | ja | ja | teilweise – T1: „bald“ und „sonst wird es eng“ gestrichen, Dringlichkeit nur noch über Betreff/Frist |
| Rückrufangebot erhalten | ja | ja, aber verallgemeinert („Bei Fragen erreichst du mich kurz …“) | ja |
| Grammatik „wegen den“ behoben | ja (umformuliert: „zu den Unterlagen“) | ja (umformuliert) | ja (umformuliert), **erklärt** aber eine Korrektur „wegen der Unterlagen“, die im Text gar nicht vorkommt |
| Kürzer als Original (T1) | ja (56 W.) | ja (49 W.) | ja (66 W.) |
| Unverlangte Zusätze | keine | Betreff ergänzt | Betreff mit Frist ergänzt |
| T2 spürbar lockerer, Du-Form | ja („Hi“, „LG“, „wird's“) | ja („Hi“, „Schaffst du es“, „wird's echt eng“) | ja („Hi“, „Wär super“, „ruf einfach kurz durch“) |
| T2 freundlich geblieben | eher nein – „Wo bleiben die denn?“ klingt vorwurfsvoll | ja („kurze Erinnerung“ leicht mahnend) | ja, am freundlichsten |
| T2 keine neuen Fakten | ja | weitgehend – „Die Druckerei wartet schon darauf“ verschärft „braucht das bald“ | weitgehend – „wartet schon“ ebenfalls verschärft |
| T2 sprachlich sauber | nein – erster Satz ist ein unvollständiger Satzanfang („wegen der Unterlagen …: Wo bleiben die denn?“) | ja | kleine Holprigkeit: „Die Druckerei wartet schon für die Flyer“ |
| Keine echten Namen/Nummern | ja | ja | ja |

**Gesamturteil:** Alle drei Modelle erfüllen die harten Kriterien (Reihenfolge, Platzhalter, Kerninhalt, Du-Form). Unterschiede liegen im Stil und in Details: Haiku kürzt am stärksten nah am Original, wird in Turn 2 aber unfreundlich und grammatisch holprig. Sonnet und Opus strukturieren mit Liste und Betreff um. Opus hält den Ton am freundlichsten, glättet in Turn 1 aber die Dringlichkeit weg und beschreibt eine Korrektur, die so nicht im Text steht.

## Gefundene Fehler mit Beleg

1. **Opus, Turn 1 – Änderungserklärung passt nicht zum Text.** Stichpunkt 2: „Die Grammatik habe ich korrigiert: ‚wegen der Unterlagen‘ statt ‚wegen den Unterlagen‘.“ Die verbesserte Mail enthält das Wort „wegen“ gar nicht („ich warte noch auf die Unterlagen …“). Der Fehler ist also durch Umformulieren verschwunden, nicht durch die genannte Korrektur. Kleiner Fehler, aber ein gutes Beispiel: Auch die Selbstbeschreibung der KI muss man gegenlesen.
2. **Opus, Turn 1 – Dringlichkeit verloren.** Original: „Die Druckerei braucht das ja bald … sonst wird es echt eng mit den Flyern.“ Opus: „Die Druckerei braucht sie für die Flyer.“ Opus begründet das bewusst („kann leicht nach Druck klingen“). Das ist eine inhaltliche Änderung, die die Absenderin vielleicht nicht will.
3. **Sonnet, Turn 1 – widersprüchliche Erklärung.** Stichpunkt 3: „Das Telefonangebot gilt jetzt allgemein bei Fragen und nur für den Fall, dass etwas unklar ist.“ Gemeint ist offenbar „allgemein bei Fragen statt nur für den Fall …“. Dazu kommt das schiefe „Bei Fragen erreichst du mich kurz unter [DURCHWAHL]“: „kurz“ steht an der falschen Stelle.
4. **Haiku, Turn 2 – Ton und Satzbau.** „wegen der Unterlagen für die Industrietage, die du mir schicken wolltest (…): Wo bleiben die denn?“ Das ist ein unvollständiger Satz, und „Wo bleiben die denn?“ klingt nach Vorwurf. Die Vorgabe „freundlich“ aus Turn 1 geht verloren.
5. **Sonnet und Opus, Turn 2 – leichte Faktenverschiebung.** „Die Druckerei wartet schon darauf / wartet schon für die Flyer“: Im Original braucht die Druckerei die Unterlagen „bald“, von „wartet schon“ steht dort nichts. Das ist keine Halluzination im engeren Sinn, aber eine Zuspitzung, die man vor dem Absenden prüfen sollte.
6. **Unverlangte Betreffzeile (Sonnet, Opus).** Der Prompt verlangt keinen Betreff. Opus schreibt zusätzlich die Frist in den Betreff („bitte bis [DATUM]“). Das ist nicht falsch und oft nützlich, sollte aber bewusst übernommen werden.

Keine Platzhalter wurden ersetzt oder erfunden, keine echten Namen oder Nummern eingesetzt. Dass die Messe in Turn 2 bei Haiku und Opus nur noch „Industrietage“ heißt, ist unkritisch.

## Lehren für die Auswertung

- **Die Übung funktioniert:** Alle Modelle liefern in Turn 1 eine brauchbare, kürzere Mail (49–66 statt 82 Wörter) und halten die Platzhalter. Die Platzhalter-Anweisung im Prompt wirkt zuverlässig. Das kann man im Plenum zeigen: So einfach lässt sich die Daten-Ampel praktisch umsetzen.
- **„Verbessern“ heißt auch „verändern“:** Jedes Modell hat Inhalte umgedeutet. Opus hat die Dringlichkeit gestrichen, Sonnet das Rückrufangebot verallgemeinert, Sonnet und Opus haben in Turn 2 „wartet schon“ hinzugefügt. Gute Frage ans Plenum: „Steht in eurer verbesserten Mail noch alles, was ihr sagen wolltet, und nichts, was ihr nicht sagen wolltet?“
- **Die Erklärung der KI ist kein Beweis:** Opus beschreibt eine Grammatikkorrektur, die im Text nicht vorkommt. Sonnet erklärt sich widersprüchlich. Die Stichpunkte gegen den Text halten.
- **„Lockerer“ kann kippen:** Haikus „Wo bleiben die denn?“ ist locker, aber nicht mehr freundlich. Wer nachsteuert, sollte die alten Vorgaben mitnennen, z. B. „lockerer, aber weiterhin freundlich und ohne neue Inhalte“.
- **Der eigene Stil ist der Maßstab:** Die drei lockeren Versionen klingen sehr verschieden. Es gibt keine richtige Lösung, sondern die, die zur Person passt. Das passt zum Merksatz „Was rausgeht, verantwortest du.“
- **Unverlangte Extras (Betreff, Liste):** Diese Zusätze erkennen und bewusst entscheiden, ob man sie übernimmt.

## Probleme im Material

- **Keine fiktive Ersatzmail vorhanden:** Das Übungsblatt sagt „Im Zweifel: weglassen oder eine erfundene Beispielmail nehmen“. Im Ordner `07_Beispielmaterial` gibt es aber keine solche Mail. Wer keine harmlose eigene Mail hat (oder unsicher ist), muss in der knappen Zeit (ca. 8 Min. für C und D zusammen) selbst eine erfinden. Diese Testmail eignet sich dafür und passt thematisch zu `notizen_besprechung.txt` („Messe Hannover / Industrietage“).
- **Lösungshinweise zu Aufgabe D fehlen fast ganz:** In den [Trainer-Lösungshinweisen](../06_Uebungen/Trainer-Loesungshinweise.md) steht zu D nur der Stolperstein „Echte Daten in Aufgabe D“. Unter „Woran du ein gutes Ergebnis erkennst“ fehlen Kriterien für D (Platzhalter erhalten, Inhalt vollständig, nichts dazuerfunden, Erklärung stimmt mit Text überein, Turn 2 lockerer, aber freundlich).
- **Nachsteuer-Prompt ohne Leitplanken:** Der Beispielsatz „Schreib es lockerer.“ führt bei einem Modell zu unfreundlichem Ton. Ein Zusatz wie „aber weiterhin freundlich, ohne neue Inhalte“ wäre die bessere Vorlage, oder man nutzt den kurzen Satz bewusst als Lernmoment.
- **Zeit:** D ist allein in 3–4 Minuten machbar, wenn eine Mail bereitliegt. Mit Daten-Ampel-Check und eigener Mailsuche wird es knapp.

## Korrekturvorschlag

1. Neue Datei `07_Beispielmaterial/kollegenmail_unterlagen.txt` mit dieser Testmail anlegen (Text siehe Protokolle unten, Nutzer 1). In `06_Uebungen/Uebung_1_Texte_schreiben.md` unter „Was du brauchst“ ergänzen: „Optional: eine kurze, harmlose Mail aus deinem eigenen Postfach (siehe Aufgabe D) – oder die fiktive Ersatzmail [kollegenmail_unterlagen.txt](../07_Beispielmaterial/kollegenmail_unterlagen.txt)“. In Aufgabe D nach der Checkliste: „Keine passende Mail? Nimm die Ersatzmail `kollegenmail_unterlagen.txt`.“
2. In `06_Uebungen/Uebung_1_Texte_schreiben.md`, Aufgabe D, „Prüfe:“ ergänzen: „Steht noch alles drin, was du sagen wolltest – und nichts, was du nicht gesagt hast? Stimmen die 3 Stichpunkte mit dem Text überein?“ Den Beispielsatz erweitern zu: „Das klingt zu steif, so rede ich nicht. Schreib es lockerer, aber weiterhin freundlich und ohne neue Inhalte.“
3. In `06_Uebungen/Trainer-Loesungshinweise.md`, Abschnitt Übung 1 „Woran du ein gutes Ergebnis erkennst“, einen Punkt für D ergänzen: „Eigene Mail (Aufgabe D): Platzhalter unverändert, kein Inhalt verloren oder dazugekommen (z. B. ‚Druckerei wartet schon‘), die 3 Stichpunkte beschreiben, was wirklich geändert wurde; die lockere Version bleibt freundlich. Modelle ergänzen oft unverlangt einen Betreff.“ Unter „Typische Stolpersteine“: „‚Lockerer‘ kippt manchmal ins Vorwurfsvolle (z. B. ‚Wo bleiben die denn?‘).“

---

## Gesprächsprotokoll: Haiku

### Nutzer 1
Verbessere die folgende E-Mail. Sie soll klar, freundlich und kurz sein.
Behalte alle Platzhalter in eckigen Klammern bei.
Zeige mir zuerst die verbesserte Version und erkläre danach in 3 Stichpunkten, was du geändert hast.

Hallo [KOLLEGIN],

ich wollte mal nachfragen wegen den Unterlagen für die Messe Industrietage, die du mir schicken wolltest. Also die Produktdatenblätter für die neuen Gehäuse und die Fotos vom Stand letztes Jahr. Die Druckerei braucht das ja bald und ich hab bis jetzt noch nichts bekommen, oder hab ich da was übersehen? Kannst du mir das bitte bis [DATUM] schicken, sonst wird es echt eng mit den Flyern. Falls du nicht weißt welche Unterlagen ich genau meine, ruf mich einfach kurz an unter [DURCHWAHL].

Danke dir und viele Grüße
[MEIN NAME]

### Assistent 1
Hallo [KOLLEGIN],

kurze Nachfrage zu den Unterlagen für die Messe Industrietage: Ich hätte gern die Produktdatenblätter der neuen Gehäuse und die Fotos vom Stand letztes Jahr bis [DATUM]. Die Druckerei braucht sie bald, und ohne die Unterlagen wird es bei den Flyern knapp.

Falls unklar ist, welche Unterlagen genau gemeint sind, ruf mich gern kurz an unter [DURCHWAHL].

Danke dir und viele Grüße
[MEIN NAME]

**Was ich geändert habe:**
- Den Einstieg gekürzt und die Frage „hab ich da was übersehen?“ entfernt, damit der Ton sachlich bleibt.
- Die Dringlichkeit in einem Satz zusammengefasst: Frist [DATUM] und Grund (Druckerei, Flyer).
- Das Rückruf-Angebot knapper formuliert, Platzhalter unverändert.

### Nutzer 2
Das klingt zu steif, so rede ich nicht. Schreib es lockerer.

### Assistent 2
Hi [KOLLEGIN],

wegen der Unterlagen für die Industrietage, die du mir schicken wolltest (Produktdatenblätter der neuen Gehäuse und die Fotos vom Stand letztes Jahr): Wo bleiben die denn? Die Druckerei braucht sie bald und ich hab noch nichts bekommen. Kannst du sie mir bis [DATUM] schicken? Sonst wird's bei den Flyern echt eng.

Wenn was unklar ist, ruf mich einfach kurz an: [DURCHWAHL].

Danke dir und LG
[MEIN NAME]

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1
Verbessere die folgende E-Mail. Sie soll klar, freundlich und kurz sein.
Behalte alle Platzhalter in eckigen Klammern bei.
Zeige mir zuerst die verbesserte Version und erkläre danach in
3 Stichpunkten, was du geändert hast.

Hallo [KOLLEGIN],

ich wollte mal nachfragen wegen den Unterlagen für die Messe Industrietage, die du mir schicken wolltest. Also die Produktdatenblätter für die neuen Gehäuse und die Fotos vom Stand letztes Jahr. Die Druckerei braucht das ja bald und ich hab bis jetzt noch nichts bekommen, oder hab ich da was übersehen? Kannst du mir das bitte bis [DATUM] schicken, sonst wird es echt eng mit den Flyern. Falls du nicht weißt welche Unterlagen ich genau meine, ruf mich einfach kurz an unter [DURCHWAHL].

Danke dir und viele Grüße
[MEIN NAME]

### Assistent 1
**Verbesserte Version:**

Betreff: Unterlagen für die Messe Industrietage

Hallo [KOLLEGIN],

für die Flyer zur Messe Industrietage warte ich noch auf deine Unterlagen:

- Produktdatenblätter für die neuen Gehäuse
- Fotos vom Stand des letzten Jahres

Könntest du mir beides bis [DATUM] schicken? Die Druckerei braucht sie bald, und sonst wird die Zeit knapp.

Bei Fragen erreichst du mich kurz unter [DURCHWAHL].

Danke dir und viele Grüße
[MEIN NAME]

**Was ich geändert habe:**

- **Klarer aufgebaut:** Die zwei benötigten Unterlagen stehen jetzt als Liste da, und die Bitte samt Frist steht in einem eigenen Satz. Ich habe auch einen Betreff ergänzt.
- **Kürzer:** Ich habe die Wendungen "ich wollte mal nachfragen" und "oder hab ich da was übersehen?" gestrichen. Der Hinweis auf die Druckerei und die Flyer ist jetzt ein einziger Satz.
- **Freundlich, aber direkter:** Die Bitte ist als höfliche Frage formuliert ("Könntest du ..."). Das Telefonangebot gilt jetzt allgemein bei Fragen und nur für den Fall, dass etwas unklar ist. Alle Platzhalter sind unverändert.

### Nutzer 2
Das klingt zu steif, so rede ich nicht. Schreib es lockerer.

### Assistent 2
Klar, hier eine lockerere Version:

Betreff: Unterlagen für die Industrietage

Hi [KOLLEGIN],

kurze Erinnerung: Mir fehlen für die Flyer zur Messe Industrietage noch zwei Sachen von dir:

- die Produktdatenblätter für die neuen Gehäuse
- die Fotos vom Stand letztes Jahr

Schaffst du es, mir die bis [DATUM] zu schicken? Die Druckerei wartet schon darauf, und sonst wird's echt eng.

Wenn unklar ist, was genau ich meine, ruf mich einfach kurz an: [DURCHWAHL].

Danke dir und liebe Grüße
[MEIN NAME]

Ich habe "Hallo" durch "Hi" ersetzt, "Könntest du" durch "Schaffst du es" und "wird die Zeit knapp" durch "wird's echt eng". Außerdem klingt der Anruf-Satz jetzt eher wie gesprochen. Alle Platzhalter sind weiterhin drin. Wenn dir "liebe Grüße" zu persönlich ist, nimm einfach "Viele Grüße".

---

## Gesprächsprotokoll: Opus

### Nutzer 1
Verbessere die folgende E-Mail. Sie soll klar, freundlich und kurz sein.
Behalte alle Platzhalter in eckigen Klammern bei.
Zeige mir zuerst die verbesserte Version und erkläre danach in
3 Stichpunkten, was du geändert hast.

Hallo [KOLLEGIN],

ich wollte mal nachfragen wegen den Unterlagen für die Messe Industrietage, die du mir schicken wolltest. Also die Produktdatenblätter für die neuen Gehäuse und die Fotos vom Stand letztes Jahr. Die Druckerei braucht das ja bald und ich hab bis jetzt noch nichts bekommen, oder hab ich da was übersehen? Kannst du mir das bitte bis [DATUM] schicken, sonst wird es echt eng mit den Flyern. Falls du nicht weißt welche Unterlagen ich genau meine, ruf mich einfach kurz an unter [DURCHWAHL].

Danke dir und viele Grüße
[MEIN NAME]

### Assistent 1
**Betreff:** Unterlagen für die Industrietage – bitte bis [DATUM]

Hallo [KOLLEGIN],

ich warte noch auf die Unterlagen für die Messe Industrietage:

- die Produktdatenblätter für die neuen Gehäuse
- die Fotos von unserem Stand im letzten Jahr

Die Druckerei braucht sie für die Flyer. Könntest du sie mir bitte bis [DATUM] schicken? Falls du sie schon geschickt hast und ich sie übersehen habe, sag mir bitte kurz Bescheid.

Wenn noch etwas unklar ist, ruf mich gern unter [DURCHWAHL] an.

Danke dir und viele Grüße
[MEIN NAME]

**Was ich geändert habe:**
- **Klarer aufgebaut:** Das Anliegen steht jetzt im ersten Satz. Die zwei Unterlagen stehen als Liste darunter, damit man auf einen Blick sieht, was fehlt. Dazu kommt ein Betreff mit der Frist.
- **Kürzer:** Füllwörter wie „mal“, „also“, „ja“ und „echt“ sind raus. Die Grammatik habe ich korrigiert: „wegen der Unterlagen“ statt „wegen den Unterlagen“.
- **Freundlicher:** Der Satz „sonst wird es echt eng“ kann leicht nach Druck klingen. Jetzt steht dort einfach, wofür die Druckerei die Unterlagen braucht. Die Frage, ob du etwas übersehen hast, ist eine freundliche Bitte um Rückmeldung. So fühlt sich niemand beschuldigt. Alle Platzhalter sind geblieben.

### Nutzer 2
Das klingt zu steif, so rede ich nicht. Schreib es lockerer.

### Assistent 2
Klar, hier eine lockerere Version:

**Betreff:** Kurze Frage zu den Industrietage-Unterlagen

Hi [KOLLEGIN],

kurze Frage: Hast du die Unterlagen für die Industrietage schon rausgeschickt? Bei mir ist bis jetzt nichts angekommen, aber vielleicht hab ich's auch einfach übersehen.

Es geht um:
- die Produktdatenblätter für die neuen Gehäuse
- die Fotos von unserem Stand letztes Jahr

Die Druckerei wartet schon für die Flyer. Wär super, wenn du mir das bis [DATUM] schicken könntest.

Falls was unklar ist, ruf einfach kurz durch: [DURCHWAHL].

Danke dir und liebe Grüße
[MEIN NAME]

**Was anders ist:** Die Anrede ist jetzt „Hi“ statt „Hallo“. Ich habe Formen aus der gesprochenen Sprache genommen, zum Beispiel „hab ich's“, „wär super“ und „ruf einfach kurz durch“. Die Bitte klingt jetzt mehr nach einer Frage unter Kollegen als nach einer Aufforderung. Die Liste ist geblieben, damit sofort klar ist, welche Unterlagen fehlen. Wenn es noch lockerer sein soll, kann ich die Liste auch weglassen und alles in einen Satz packen.
