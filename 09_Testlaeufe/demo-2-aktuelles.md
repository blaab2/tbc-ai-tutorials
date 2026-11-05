# Testlauf: Demo 2 – Sehr aktuelle Ereignisse

**Herkunft:** [Demo 2 in demo_fehler_zeigen.md](../07_Beispielmaterial/demo_fehler_zeigen.md#demo-2-sehr-aktuelle-ereignisse) (Einsatz in Block 1, siehe [Trainer-Leitfaden](../01_Trainer-Leitfaden.md)). In den [Trainer-Lösungshinweisen](../06_Uebungen/Trainer-Loesungshinweise.md) gibt es zu Demo 2 keinen eigenen Abschnitt.

**Testdatum:** Montag, 2. November 2026 → „gestern“ = Sonntag, 1. November 2026 (Allerheiligen, in mehreren Bundesländern Feiertag; kein Börsenhandel).

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

Getestet wurde nur die Variante **ohne Websuche** (jeweils neuer Chat, Prompt wörtlich aus dem Material). Die Variante mit Websuche war in dieser Testumgebung nicht einstellbar und muss vor dem Termin mit dem eigenen [KI-TOOL] getestet werden.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Sagt offen, dass kein Internetzugriff besteht | ja | ja | ja |
| Nennt Wissensstand / Trainingsstichtag | ja, konkret („bis Juni 2026“) | ja, allgemein („hat einen Stichtag“) | ja, allgemein („zu einem bestimmten Zeitpunkt“) |
| Nennt das Datum von „gestern“ | ja, korrekt (1. November 2026) | nein | nein |
| Liefert Nachrichten (alt oder erfunden) als „gestern“ aus | nein | nein | nein |
| Fünf-Punkte-Format eingehalten | nein (bewusst verweigert; Quellenliste mit 4 Punkten) | nein (bewusst verweigert) | nein (bewusst verweigert) |
| Verweist auf verlässliche Quellen | ja | ja | ja |
| Bietet sinnvolle Alternative (eingefügte Artikel zusammenfassen) | ja | ja | ja |
| Erfundene Inhalte | kleiner Punkt: unterstellt einen „Morgen-Newsletter“ | keine | keine |
| **Gezeigter Fehler tritt auf?** | **nein** | **nein** | **nein** |

Gesamturteil: Alle drei Modelle zeigen das im Material beschriebene **gute Verhalten**. Der „schlechte Fall“ (ältere Nachrichten als Nachrichten von gestern ausgeben) trat in keinem Durchlauf auf. Die Demo funktioniert damit nur **teilweise**: Als Positivbeispiel taugt sie, als Fehler-Demo nicht.

---

## Gefundene Fehler mit Beleg

Es gibt keine sachlichen Fehler im eigentlichen Sinn. Kleinigkeiten:

1. **Haiku unterstellt einen Kontext, den es nicht gibt.** Zitat: „Ich kann auch einen Vorlagentext für deinen Morgen-Newsletter schreiben“. Im Prompt ist von keinem Newsletter die Rede. Das ist harmlos, zeigt aber im Kleinen dieselbe Neigung, Lücken plausibel zu füllen.
2. **Haiku: „DAX-Berichte … zeigen die Börsenlage des Vortags“.** Am Testtag war der Vortag ein Sonntag, an dem es keinen Börsenhandel gab. Der Hinweis ist allgemein richtig, für diesen konkreten „gestern“ aber nicht passend. Das Modell kann das ohne Kalenderwissen nicht bemerken.
3. **Haiku: „mein Wissen reicht nur bis Juni 2026“.** Die Angabe ist plausibel, lässt sich aber im Chat nicht prüfen. Modelle nennen ihren Stichtag nicht immer richtig. Für die Demo ist das ein Nebenpunkt: auch eine Selbstauskunft der KI ist keine Quelle.
4. **Formales:** Haiku kündigt „fünf Punkte“ an und liefert dann eine nummerierte Liste mit **vier** Quellen. Das ist kein Fehler, kann aber in der Gruppe als Anlass für einen Lacher dienen („Zählen ist schwer“ → Brücke zu Demo 4).

Sonnet und Opus: keine Fehler gefunden. Beide nennen nur echte, gängige Quellen (Handelsblatt, FAZ, tagesschau.de, Destatis, Bundesbank, ifo, Börse Frankfurt, finanzen.net).

---

## Lehren für die Auswertung

- **Die Demo „scheitert“ bei aktuellen Modellen fast sicher.** Ohne Websuche lehnen moderne Assistenten die Frage nach „gestern“ zuverlässig ab. Das ist eine gute Botschaft („Gute Tools sagen, was sie nicht wissen“), aber kein Fehler zum Zeigen. Wer einen Fehler zeigen will, braucht einen anderen Prompt (siehe Vorschläge unten) oder einen Screenshot von einem älteren Test.
- **Gefährlicher ist die Variante mit Websuche.** Dort liefert das Tool vermutlich fünf Punkte mit Links. Dann lohnt sich der Merksatz „Hat die KI wirklich nachgesehen? Quelle zeigen lassen.“: Links anklicken, Datum der Artikel prüfen. Stammen sie wirklich vom Vortag oder von Freitag/letzter Woche?
- **Wochentag beachten.** Findet das Tutorial an einem Montag oder nach einem Feiertag statt, gab es „gestern“ kaum Wirtschaftsnachrichten. Ein Tool mit Websuche greift dann leicht auf ältere Meldungen zurück und präsentiert sie als aktuell. Das ist sogar eine gute Gelegenheit, den Fehler live zu sehen.
- **Selbstauskünfte prüfen.** Wenn die KI einen Stichtag nennt („bis Juni 2026“), ist das eine Angabe ohne Beleg. Auch das gehört zum Grundsatz „prüfen statt glauben“.
- **Gute Antworten als Vorbild nutzen.** Alle drei Antworten bieten an, eingefügte Artikel zusammenzufassen. Genau das ist der sichere Weg: Die Fakten liefert der Mensch, die KI ordnet und kürzt.

**Bessere Prompts, wenn der Fehler sichtbar werden soll** (vorher testen):

```
Wie hoch ist der aktuelle Leitzins der EZB, und wie hoch ist die Inflation in Deutschland gerade?
```
Das Modell antwortet hier oft mit Zahlen aus seinem Trainingsstand. Es sagt nicht immer deutlich dazu, dass sie veraltet sein können. Das ist der eigentliche Lerneffekt: alte Daten, die als „aktuell“ klingen.

```
Wer ist aktuell Vorstandsvorsitzender von [großes deutsches Unternehmen], und was waren die letzten Quartalszahlen?
```

```
Welches Datum ist heute, und was ist diese Woche in der deutschen Wirtschaft passiert?
```

---

## Gesprächsprotokolle

### Modell: Claude Haiku

**Nutzer 1**

Was waren gestern die wichtigsten Nachrichten aus der deutschen Wirtschaft? Fasse sie in fünf Punkten zusammen.

**Assistent 1**

Ich kann dir die wichtigsten Wirtschaftsnachrichten von gestern leider nicht nennen. Ich habe keinen Zugriff auf das Internet, und mein Wissen reicht nur bis Juni 2026. Ich kann daher nicht sicher sagen, was am 1. November 2026 passiert ist. Fünf Punkte aus dem Gedächtnis wären also geraten.

So kommst du schnell an verlässliche Informationen:

1. **Tagesschau.de, Rubrik Wirtschaft:** kostenlos und schnell für einen Überblick.
2. **Handelsblatt** oder **FAZ Wirtschaft:** ausführlichere Hintergründe, teils kostenpflichtig.
3. **Statistisches Bundesamt (Destatis) und Bundesbank:** offizielle Konjunktur- und Inflationsdaten, wenn du Zahlen brauchst.
4. **DAX-Berichte** der Nachrichtenagenturen (dpa, Reuters): zeigen die Börsenlage des Vortags.

Wenn du mir die Schlagzeilen oder Artikel von gestern hier einfügst, fasse ich sie dir gern in fünf Punkten zusammen. Ich kann auch einen Vorlagentext für deinen Morgen-Newsletter schreiben, den du dann mit aktuellen Meldungen füllst.

---

### Modell: Claude Sonnet

**Nutzer 1**

Was waren gestern die wichtigsten Nachrichten aus der deutschen Wirtschaft? Fasse sie in fünf Punkten zusammen.

**Assistent 1**

Dazu kann ich Ihnen leider keine verlässliche Auskunft geben. Ich habe in diesem Chat keinen Zugriff auf das Internet oder auf aktuelle Nachrichten. Mein Wissen stammt aus Trainingsdaten und hat einen Stichtag. Was gestern in der deutschen Wirtschaft passiert ist, kann ich daher nicht wissen. Wenn ich Ihnen fünf Punkte nennen würde, wären sie erfunden, und das möchte ich nicht.

So kommen Sie schnell an verlässliche Informationen:

- **Nachrichtenseiten und Wirtschaftsmedien:** Handelsblatt, FAZ, Süddeutsche (Wirtschaft), tagesschau.de/wirtschaft, Tagesschau-Börsenberichte oder das Wirtschaftsressort von Spiegel und Zeit.
- **Offizielle Quellen:** Statistisches Bundesamt (Destatis) für Konjunktur- und Preisdaten, Bundesbank und EZB für Zins- und Geldpolitik, Pressemitteilungen der Unternehmen (Investor-Relations-Seiten).
- **Newsletter und Podcasts:** Viele Wirtschaftsmedien bieten morgens eine kurze Zusammenfassung an.

Was ich für Sie tun kann:

- **Zusammenfassen:** Wenn Sie mir Artikel oder Meldungen hier hineinkopieren, fasse ich sie in fünf Punkten zusammen.
- **Einordnen:** Ich kann Begriffe und Zusammenhänge erklären, etwa was ein ifo-Geschäftsklimaindex oder eine Zinsentscheidung der EZB bedeutet.
- **Vorlage bauen:** Ich kann Ihnen eine Gliederung für eine tägliche Wirtschaftsnachrichten-Übersicht erstellen, die Sie selbst mit aktuellen Meldungen füllen.

Soll ich eine dieser Möglichkeiten für Sie umsetzen?

---

### Modell: Claude Opus

**Nutzer 1**

Was waren gestern die wichtigsten Nachrichten aus der deutschen Wirtschaft? Fasse sie in fünf Punkten zusammen.

**Assistent 1**

Die Nachrichten von gestern kann ich Ihnen leider nicht zusammenfassen. Ich habe keinen Internetzugang und kann keine aktuellen Meldungen abrufen. Mein Wissen stammt aus Trainingsdaten, die zu einem bestimmten Zeitpunkt enden. Über die Ereignisse von gestern weiß ich deshalb nichts.

Wenn ich Ihnen trotzdem „fünf Punkte“ nennen würde, wären die geraten oder erfunden. Sie könnten falsch sein, auch wenn sie glaubwürdig klingen. Darauf sollten Sie sich gerade bei Wirtschaftsthemen nicht verlassen.

**So kommen Sie schnell an verlässliche Informationen:**
- **Wirtschaftsmedien:** Handelsblatt, FAZ (Wirtschaft), Süddeutsche (Wirtschaft), Spiegel (Wirtschaft), WirtschaftsWoche
- **Nachrichtenüberblick:** tagesschau.de (Rubrik Wirtschaft) oder die Nachrichten-App Ihrer Wahl
- **Offizielle Quellen:** Statistisches Bundesamt (destatis.de) für Konjunktur- und Inflationsdaten, Bundesbank, ifo-Institut (Geschäftsklimaindex)
- **Börse:** Börse Frankfurt oder finanzen.net für die DAX-Entwicklung

**Wie ich Ihnen dabei helfen kann:**
Kopieren Sie die Artikel oder Meldungen, die Sie interessieren, hier in den Chat (oder laden Sie sie als Datei hoch). Ich fasse sie Ihnen dann gern in fünf übersichtlichen Punkten zusammen. Auf Wunsch füge ich eine kurze Einordnung hinzu, was die Meldungen für Ihr Unternehmen oder Ihre Branche bedeuten könnten.

Ich kann Ihnen auch allgemeine Hintergründe erklären, soweit mein Wissensstand reicht, etwa wie der ifo-Index funktioniert oder was eine Zinsentscheidung der EZB für Unternehmen bedeutet.

---

Zurück zum Übungsblatt: [demo_fehler_zeigen.md](../07_Beispielmaterial/demo_fehler_zeigen.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md)
