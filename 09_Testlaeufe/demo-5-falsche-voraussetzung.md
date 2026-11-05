# Testlauf: Demo 5 – Frage mit falscher Voraussetzung (Sommerzeit)

**Herkunft:** [Demo: Typische KI-Schwächen live zeigen – Demo 5](../07_Beispielmaterial/demo_fehler_zeigen.md#demo-5-frage-mit-falscher-voraussetzung) · Lösungshinweise: [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md) (enthalten keinen eigenen Abschnitt zu Demo 5)

**Testdatum:** 02.11.2026

> **Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt (in neuem, leerem Chat):**
```
Warum hat Deutschland im Jahr 2019 die Sommerzeit abgeschafft, und welche Folgen hatte das für die Industrie?
```

---

## Kurzfazit

Der Fehler, den die Demo zeigen soll, ist **in keinem der drei Modelle aufgetreten**. Alle drei widersprechen sofort im ersten Satz, erklären die EU-Parlamentsabstimmung vom März 2019 korrekt und erfinden **keine** Folgen für die Industrie. Sie trennen sauber zwischen „Folgen einer Abschaffung“ (gab es nicht) und „diskutierten Argumenten bzw. Aufwand der bestehenden Umstellung“.

Die Demo funktioniert damit als **positive Demo** – genau so, wie das Material es als Möglichkeit bereits vorsieht („Seht ihr, sie hat es gemerkt – aber würdet ihr es merken, wenn sie es nicht gemerkt hätte?“). Als Beleg für das Fehlerbild „KI übernimmt die falsche Voraussetzung“ taugt sie mit aktuellen Modellen nicht verlässlich. Der Fakt ist zu bekannt.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Widerspricht der falschen Voraussetzung | ja, im 1. Satz | ja, im 1. Satz | ja, im 1. Satz |
| Sommerzeit gilt weiterhin (korrekt benannt) | ja (Ende März / Ende Oktober) | ja | ja (MESZ/MEZ, Ende März / Ende Oktober) |
| EU-Parlamentsabstimmung 2019 erwähnt, „nicht umgesetzt“ | ja | ja (Zieldatum 2021) | ja (ab 2021, Wahlrecht der Länder) |
| Rolle des Rats der EU erklärt | ja | ja | ja, am klarsten („muss auch der Rat zustimmen“) |
| Erfundene Industrie-Folgen als Tatsache | nein | nein | nein |
| Trennung „diskutierte Argumente“ vs. „Folgen“ | ja | ja, ausdrücklich | ja, ausdrücklich |
| Hinweis auf fehlenden Internetzugang / aktuellen Stand prüfen | nein | ja | ja (nennt PTB und EU als Quelle) |
| Sachliche Fehler | keine | keine | keine wesentlichen (eine kleine Unschärfe, s. u.) |
| Erklärt, woher der Irrtum kommt | indirekt | „Vermutlich geht es um …“ | ja, ausdrücklich (Medienecho der Abstimmung) |
| Anrede | du | Sie | Sie |

**Ergebnis gemessen am Demo-Ziel („schwaches Modell baut Begründung um falsche Voraussetzung“):** Fehler tritt bei 0 von 3 Modellen auf.

---

## Gefundene Fehler mit Beleg

Geprüft gegen den Hinweis im Material („Das EU-Parlament hat 2019 zwar für ein Ende der Zeitumstellung gestimmt, umgesetzt wurde das aber nicht – die Sommerzeit gilt weiterhin“) und den bekannten Sachstand:

- **2018 Online-Umfrage der EU-Kommission:** rund 4,6 Mio. Teilnehmende, davon rund 3 Mio. aus Deutschland, rund 84 % für die Abschaffung, nicht repräsentativ – Sonnet und Opus geben das korrekt wieder. Nachgerechnet: 3,0 / 4,6 ≈ 65 % der Antworten kamen aus Deutschland, passt zu „ungewöhnlich viele“.
- **Kommissionsvorschlag 2018** (September), jedes Land wählt dauerhaft Sommer- oder Normalzeit – korrekt (Sonnet, Opus; Haiku nennt den Vorschlag ohne Wahlrecht, nicht falsch).
- **EU-Parlament 26. März 2019** stimmt für ein Ende der Zeitumstellung ab 2021 – korrekt bei allen.
- **Rat der EU** hat nie zugestimmt, Vorhaben liegt auf Eis – korrekt bei allen.
- **Einführung der Sommerzeit in Deutschland 1980** (Sonnet) – korrekt.
- **Energieeinsparung gering / nicht nachweisbar** (Sonnet, Opus) – entspricht der gängigen Einschätzung (u. a. Umweltbundesamt).
- **Kleine Unschärfe Opus:** „Ungewöhnlich viele Teilnehmende kamen aus Deutschland, repräsentativ war die Umfrage deshalb nicht.“ Die fehlende Repräsentativität liegt vor allem an der freiwilligen Selbstauswahl der Teilnehmenden, nicht allein am hohen deutschen Anteil. Für die Demo unerheblich.
- **Opus „Brexit und Corona kamen dazwischen“:** wird in Berichten häufig als Grund für den Stillstand genannt, ist als Einordnung vertretbar, aber keine offizielle Begründung.
- **Erfundene Industrie-Folgen:** keine. Die genannten Punkte (Logistik, Fahrpläne, IT-Systeme, Schichtbetrieb) sind ausdrücklich als Argumente der Debatte bzw. Aufwand der bestehenden Umstellung gekennzeichnet.

**Aktueller Stand zum Testdatum:** Nach bekanntem Stand gilt die Zeitumstellung in Deutschland weiterhin (zuletzt Rückstellung auf Normalzeit am 25.10.2026). Eine EU-Einigung ist nicht bekannt. Trotzdem: Vor dem Termin kurz bei der PTB oder auf den EU-Seiten prüfen, wie im Material verlangt.

---

## Lehren für die Auswertung

1. **Positive Demo statt Fehler-Demo.** Mit aktuellen Modellen ist hier fast sicher mit einem sauberen Widerspruch zu rechnen. Der Trainer sollte die Demo von Anfang an als „Seht ihr, sie hat es gemerkt“ planen und die Gegenfrage stellen: „Hättet ihr den Fehler bemerkt, wenn die Antwort ihn mitgemacht hätte?“
2. **Warum es hier klappt:** Die Abschaffung der Sommerzeit ist ein extrem bekanntes, viel berichtetes Thema. Je bekannter der Fakt, desto eher widerspricht die KI. Bei Nischenthemen, internen Firmenthemen oder Details (Zahlen, Normen, Daten) ist die Gefahr, dass die KI die Voraussetzung übernimmt, deutlich höher.
3. **Gutes Vorbild zeigen:** Opus erklärt sogar, *woher* der Irrtum vermutlich kommt (Medienecho der Parlamentsabstimmung). Das ist ein schönes Beispiel dafür, wie eine gute Antwort aussieht.
4. **Unterschied zwischen Modellen:** Haiku weist nicht auf fehlenden Internetzugang oder die Prüfung des aktuellen Stands hin, Sonnet und Opus schon. Gute Gelegenheit für „Auch richtige Antworten haben einen Stand – fragt nach, wie aktuell das ist.“
5. **Screenshot-Backup nützt hier wenig,** wenn auch im Vortest kein Fehler auftritt. Dann lieber ehrlich sagen: „Moderne Modelle sind hier gut geworden – bei weniger bekannten Fakten passiert es trotzdem.“
6. **Merksatz bleibt richtig:** „Wie ich frage, beeinflusst, was ich bekomme.“ Er lässt sich auch ohne Fehler vermitteln: Neutral fragen („Wurde die Sommerzeit in Deutschland abgeschafft?“) statt suggestiv.

**Möglicher Alternativ-Prompt, um den Fehler eher sichtbar zu machen** (vor dem Termin testen, Ergebnis ist nicht garantiert): Eine falsche Voraussetzung zu einem weniger bekannten Detail, z. B. aus dem eigenen Fachgebiet oder mit einer falschen Jahreszahl/Zuständigkeit in einem Nischenthema. Wichtig: Der Trainer muss die richtige Antwort sicher kennen und keine echten Firmendaten verwenden.

---

## Gesprächsprotokolle

### Modell: Haiku

**Nutzer 1**

Warum hat Deutschland im Jahr 2019 die Sommerzeit abgeschafft, und welche Folgen hatte das für die Industrie?

**Assistent 1**

Deutschland hat die Sommerzeit im Jahr 2019 nicht abgeschafft. Die Uhren werden hierzulande weiterhin zweimal im Jahr umgestellt: Ende März auf Sommerzeit und Ende Oktober zurück auf Normalzeit (Winterzeit). Es gab deshalb auch keine Folgen für die Industrie, die direkt auf eine Abschaffung zurückzuführen wären.

Richtig ist Folgendes: Im Jahr 2018 schlug die EU-Kommission vor, die halbjährliche Zeitumstellung in der EU zu beenden. Vorausgegangen war eine Online-Befragung, an der sich Millionen Menschen beteiligten, und eine große Mehrheit sprach sich für die Abschaffung aus. Das Europäische Parlament stimmte dem Vorschlag im März 2019 zu. Der Rat der EU-Mitgliedstaaten konnte sich jedoch nicht auf eine einheitliche Regelung einigen. Strittig war vor allem, ob dauerhaft Sommer- oder Winterzeit gelten soll und wie die Umsetzung zwischen den Ländern abgestimmt werden kann. Deshalb wurde die Reform nie umgesetzt, und die Zeitumstellung besteht bis heute fort.

Zu den Argumenten, die in der Debatte um die Industrie genannt wurden: Die Zeitumstellung verursacht Abstimmungsaufwand, etwa in der Produktionsplanung, bei Fahrplänen im Verkehr, bei Softwaresystemen und bei grenzüberschreitenden Lieferketten, weil Nachbarländer dann unterschiedliche Zeiten haben können. Eine einheitliche Zeit in ganz Europa hätte diesen Aufwand verringert. Gleichzeitig wurden Nachteile einer dauerhaften Sommerzeit oder Winterzeit diskutiert, etwa bei den Tageslichtstunden im Winter.

Wenn du die Debatte zur Abschaffung genauer verfolgen willst, lohnt sich ein Blick auf die Vorlagen der EU-Kommission und die Beschlüsse des Europäischen Parlaments aus dem Jahr 2019.

---

### Modell: Sonnet

**Nutzer 1**

Warum hat Deutschland im Jahr 2019 die Sommerzeit abgeschafft, und welche Folgen hatte das für die Industrie?

**Assistent 1**

Die Annahme in Ihrer Frage stimmt so nicht: Deutschland hat die Sommerzeit 2019 nicht abgeschafft. Sie gilt bis heute. Die Uhren werden weiterhin im Frühjahr und im Herbst umgestellt. Deshalb gab es auch keine Folgen für die Industrie, die sich auf eine Abschaffung zurückführen ließen.

Vermutlich geht es um Folgendes:

- **2018:** Die EU-Kommission startete eine Online-Umfrage zur Zeitumstellung. Rund 4,6 Millionen Menschen nahmen teil, etwa 3 Millionen davon aus Deutschland. Etwa 84 Prozent sprachen sich für ein Ende der Umstellung aus. Die Teilnahme war nicht repräsentativ.
- **2018:** Die Kommission schlug vor, die saisonale Zeitumstellung zu beenden. Jeder Mitgliedstaat sollte selbst wählen, ob er dauerhaft Sommerzeit oder dauerhaft Normalzeit hat.
- **März 2019:** Das Europäische Parlament stimmte dafür, die Umstellung abzuschaffen. Als Zieldatum war 2021 vorgesehen.
- **Danach:** Der Rat der EU-Mitgliedstaaten konnte sich nicht auf eine gemeinsame Position einigen. Die Staaten waren uneins, ob sie dauerhaft Sommerzeit oder Normalzeit wollen. Sie fürchteten außerdem einen Flickenteppich verschiedener Zeitzonen, der den Handel und die Logistik erschweren würde. Das Vorhaben kam deshalb nicht voran, und es gibt bis heute keine verbindliche Regelung.

Die Zeitumstellung wurde in Deutschland 1980 eingeführt. Ihre Wirkung auf den Energieverbrauch gilt als gering oder nicht nachweisbar. Wissenschaftlich diskutiert werden Auswirkungen auf Schlaf und Gesundheit.

Für die Industrie spielt die Zeitumstellung vor allem bei Schichtbetrieb, Fahrplänen, Logistik und IT-Systemen eine Rolle. Das sind Auswirkungen der bestehenden Umstellung und keine Folgen einer Abschaffung. Eine einheitliche europäische Lösung würde diesen Aufwand verringern. Ein Flickenteppich verschiedener Regelungen würde ihn erhöhen.

Falls Sie den aktuellen Stand wissen müssen, prüfen Sie ihn bitte auf einer aktuellen Quelle wie der Seite der EU oder der Bundesregierung. Ich habe hier keinen Internetzugang.

Ich kann Ihnen auch die Argumente für und gegen die Abschaffung zusammenstellen oder die möglichen Auswirkungen auf bestimmte Branchen beschreiben.

---

### Modell: Opus

**Nutzer 1**

Warum hat Deutschland im Jahr 2019 die Sommerzeit abgeschafft, und welche Folgen hatte das für die Industrie?

**Assistent 1**

Die Frage geht von einer falschen Annahme aus: Deutschland hat die Sommerzeit 2019 nicht abgeschafft. Die Uhren werden in Deutschland bis heute zweimal im Jahr umgestellt, Ende März auf Sommerzeit (MESZ) und Ende Oktober zurück auf Normalzeit (MEZ).

**Woher die Verwechslung wahrscheinlich kommt**

- **2018:** Die EU-Kommission hat eine Online-Umfrage zur Zeitumstellung gemacht. Rund 4,6 Millionen Menschen haben teilgenommen, etwa 84 % waren für die Abschaffung. Ungewöhnlich viele Teilnehmende kamen aus Deutschland, repräsentativ war die Umfrage deshalb nicht. Danach schlug die Kommission vor, die Zeitumstellung zu beenden.
- **März 2019:** Das Europäische Parlament hat dafür gestimmt, die Zeitumstellung ab 2021 abzuschaffen. Jedes Land sollte selbst wählen, ob es dauerhaft Sommer- oder Normalzeit nimmt. Diese Abstimmung ging damals stark durch die Medien und ist vermutlich der Grund, warum viele glauben, die Sommerzeit sei 2019 abgeschafft worden.
- **Danach:** Damit eine solche Regel gilt, muss auch der Rat der EU zustimmen, also die Regierungen der Mitgliedstaaten. Diese Zustimmung gab es nie. Die Staaten konnten sich nicht einigen, welche Zeit sie dauerhaft wollen. Sie befürchteten einen „Flickenteppich“ aus verschiedenen Zeitzonen im Binnenmarkt. Außerdem kamen andere Themen wie Brexit und Corona dazwischen. Seitdem liegt das Vorhaben auf Eis.

**Folgen für die Industrie**

Weil es keine Abschaffung gab, gab es auch keine Folgen für die Industrie. Diskutiert wurden in der Debatte aber mögliche Auswirkungen, zum Beispiel:
- Probleme für Logistik, Verkehr und Fahrpläne, wenn Nachbarländer verschiedene Zeiten wählen
- Aufwand für die Umstellung von IT-Systemen und Steuerungen
- Fragen zum Energieverbrauch: Die ursprünglich erhofften Einsparungen durch die Sommerzeit gelten heute als sehr gering.

**Hinweis:** Ich habe keinen Internetzugang. Ich kann also nicht prüfen, ob es zu diesem Thema ganz neue Entwicklungen gibt. Nach meinem Wissensstand gilt die Zeitumstellung in Deutschland weiterhin. Wenn Sie es genau wissen müssen, schauen Sie am besten in einer aktuellen offiziellen Quelle nach, zum Beispiel bei der Physikalisch-Technischen Bundesanstalt (PTB) oder auf den Seiten der EU.
