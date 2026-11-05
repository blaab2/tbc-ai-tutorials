# Testlauf: Demo 3 – Wissen über die eigene Firma (Urlaubsbeantragung)

**Herkunft:** [Demo: Typische KI-Schwächen live zeigen – Demo 3](../07_Beispielmaterial/demo_fehler_zeigen.md#demo-3-wissen-über-die-eigene-firma) · Bezug: [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md) (enthält keinen eigenen Abschnitt zu Demo 3; nur der allgemeine Hinweis „Aufgabe braucht Firmenwissen“ in Übung 4) · [Trainer-Leitfaden, Block 1](../01_Trainer-Leitfaden.md)

**Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.**

**Getesteter Prompt** (Platzhalter [FIRMENNAME] durch die fiktive Beispielfirma ersetzt, neuer Chat):

```
Wie funktioniert bei der Nordlicht Technik GmbH die Urlaubsbeantragung, und wer ist bei uns für die Freigabe zuständig?
```

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Sagt klar, dass es keine internen Infos zur Firma hat | ja (erster Satz) | ja (erster Absatz) | ja (erster Absatz, sehr ausführlich) |
| Erfindet Person, Tool oder Frist als firmenspezifisch | nein | nein | nein |
| Allgemeine Hinweise als allgemein gekennzeichnet | ja („In vielen Unternehmen … typischerweise“) | ja („nur als Orientierung, nicht als Aussage über Ihr Unternehmen“) | ja („nur zur Orientierung, nicht Ihre Firmenregel“) |
| Verweist auf richtige Quellen (HR, Führungskraft, Intranet) | ja | ja (zusätzlich Betriebsrat) | ja (zusätzlich Arbeitsvertrag/Betriebsvereinbarung) |
| Bietet an, mit mitgeliefertem Kontext zu arbeiten | ja | ja | ja (Text einfügen/Datei hochladen, Mail an HR) |
| Tritt der in der Demo gezeigte Fehler auf? | **nein** | **nein** | **nein** |
| Länge / Beamer-Tauglichkeit | kurz, gut lesbar | mittel | lang (für 3 Minuten eher zu lang) |

**Ergebnis:** Alle drei Modelle verhalten sich vorbildlich. Der Fehler, den die Demo zeigen will („typische“ Antwort, die wie firmenspezifisch klingt), tritt mit diesem Prompt **nicht** auf.

---

## Gefundene Fehler mit Beleg

- **Keine sachlichen Fehler, keine Halluzinationen.** Keines der Modelle nennt eine konkrete Person, ein konkretes System oder eine konkrete Frist als Regel der Nordlicht Technik GmbH.
- **Grenzfall Opus:** Opus nennt reale Produktnamen („Personio, SAP SuccessFactors, DATEV, ATOSS“) und „meist einige Wochen vorher“. Beides ist ausdrücklich als allgemein gekennzeichnet („Viele Firmen nutzen dafür Programme wie …“, „Was in Unternehmen oft üblich ist (nur zur Orientierung, nicht Ihre Firmenregel)“) – laut Prüfkriterium also in Ordnung. Für die Auswertung trotzdem interessant: Wer nur überfliegt, könnte „Personio“ als Antwort auf „welches System nutzen wir?“ mitnehmen.
- **Keine Zahlen zu prüfen** (keine Rechenaufgabe in dieser Demo).

---

## Didaktische Beurteilung

**Funktioniert die Demo wie gedacht? Teilweise.** Der Kern-Merksatz („Die KI kennt [FIRMENNAME] nicht. Kontext musst du mitliefern.“) kommt an – aber als **positive** Demo: Die KI sagt das selbst. Den „schlechten Fall“ bekommt man mit aktuellen Modellen bei dieser direkten Frage praktisch nicht zu sehen. Das deckt sich mit dem Hinweis im Material („Auch ‚Die KI hat es richtig gemacht‘ ist eine gute Lehre“), passt aber nicht zum Platz der Demo im Ablauf: Im Vorschlag für Block 1 steht sie als „Etwas, das schiefgeht“ (0:12–0:15) gleichwertig neben Demo 1.

**Gründe, warum der Fehler nicht auftritt:**
1. Die Frage nennt den Firmennamen ausdrücklich und fragt nach „bei uns“ – das signalisiert dem Modell klar, dass interne Infos gemeint sind.
2. Die Frage ist eine **Wissensfrage**. Modelle sind bei solchen Fragen inzwischen darauf trainiert, Wissenslücken zu benennen.

**Wichtiger Hinweis für den echten Einsatz mit [FIRMENNAME]:** Ist das [KI-TOOL] mit Firmendaten verbunden (z. B. ein Assistent mit Zugriff auf Intranet, SharePoint, Mails oder ein hinterlegtes Firmenhandbuch), kann es die Frage **richtig** beantworten. Dann kippt die Demo komplett. Das Material erwähnt diesen Fall bisher nicht – nur die Websuche bei Demo 2. Vorher unbedingt testen, und die Lehre ggf. umdrehen: „Hier hat die KI nachgeschlagen – woher? Quelle zeigen lassen. Und: Das geht nur, weil jemand ihr diese Daten gegeben hat.“

**Zeit:** 3 Minuten reichen für Prompt und Antwort mit Haiku/Sonnet. Die Antwort von Opus ist für den Beamer lang; gut wäre, nur den ersten Absatz und die Kennzeichnung „nur zur Orientierung“ hervorzuheben.

**Alternativer Prompt mit höherer Chance auf den Fehler (Hypothese, vor dem Einsatz testen):** Statt einer Wissensfrage eine **Schreibaufgabe** stellen, bei der die KI „liefern“ will:

```
Schreib eine kurze Anleitung für neue Mitarbeitende der Nordlicht Technik GmbH: Wie beantragen sie Urlaub, bis wann, und wer gibt frei?
```

Bei solchen Aufträgen füllen Modelle die Lücke eher mit plausiblen Details (konkrete Fristen, „über das HR-Portal“, „Ihre Teamleitung gibt frei“) – manchmal mit Platzhaltern, manchmal ohne Kennzeichnung. Auch das Ergebnis mit Platzhaltern ist eine gute Lehre: „Seht ihr die eckigen Klammern? Genau das müsst ihr mitliefern.“

---

## Lehren für die Auswertung

- **Positive Lehre zeigen:** „Die KI sagt selbst: Ich kenne eure Firma nicht. Das ist gut – aber verlasst euch nicht darauf, dass sie das immer sagt.“
- **Kennzeichnung lesen lernen:** Alle Modelle mischen ehrliche Absage und allgemeine Hinweise. Live zeigen, wo „in vielen Unternehmen“ oder „nur zur Orientierung“ steht. Wer diese Wörter überliest, hält die allgemeine Antwort für die Firmenregel.
- **Reale Produktnamen sind kein Firmenwissen:** Opus nennt Personio, SAP SuccessFactors usw. als Beispiele. Gute Frage an die Gruppe: „Wisst ihr jetzt, welches System *wir* nutzen?“ – Nein.
- **Überleitung zur Daten-Ampel funktioniert sehr gut,** weil alle drei Modelle von sich aus anbieten: „Fügen Sie die Richtlinie hier ein.“ Anschlussfrage: „Darf ich unsere Urlaubsrichtlinie hier einfügen? Was sagt die Ampel?“
- **Screenshot-Backup ist hier wichtiger als bei anderen Demos,** weil der Fehler live kaum auftritt. Ohne Screenshot eines schlechten Falls lieber die Schreibaufgabe-Variante oder Demo 1 als „Fehler-Demo“ nehmen.

---

## Gesprächsprotokolle

### Modell: Claude Haiku

**Nutzer 1**

Wie funktioniert bei der Nordlicht Technik GmbH die Urlaubsbeantragung, und wer ist bei uns für die Freigabe zuständig?

**Assistent 1**

Zu den internen Abläufen der Nordlicht Technik GmbH habe ich keine Informationen. Ich kann Ihre Frage deshalb nicht verbindlich beantworten, und Namen von Freigabeverantwortlichen würde ich nur raten.

In vielen Unternehmen läuft die Urlaubsbeantragung typischerweise so ab:

1. Sie beantragen Urlaub über ein Formular, ein HR-Tool oder einen Kalender (je nach Unternehmen).
2. Ihre direkte Führungskraft (Teamleitung oder Abteilungsleitung) prüft und genehmigt den Antrag.
3. Bei größeren Abwesenheiten oder bestimmten Konstellationen kann zusätzlich die Personalabteilung (HR) einbezogen werden.
4. Die Genehmigung wird dokumentiert, und Ihr Resturlaub wird angepasst.

Für Ihren Fall empfehle ich:
- Die Richtlinie zu Urlaub bzw. Abwesenheiten im Intranet oder in Ihrem Arbeitsvertrag nachzulesen.
- Bei Unklarheiten die Personalabteilung oder Ihre Führungskraft zu fragen, wer konkret freigibt und über welches System beantragt wird.

Wenn Sie mir sagen, welche Regeln oder Formulare Ihnen bekannt sind, kann ich Ihnen helfen, daraus eine Anfrage an die Personalabteilung zu formulieren.

---

### Modell: Claude Sonnet

**Nutzer 1**

Wie funktioniert bei der Nordlicht Technik GmbH die Urlaubsbeantragung, und wer ist bei uns für die Freigabe zuständig?

**Assistent 1**

Dazu kann ich Ihnen leider keine verlässliche Auskunft geben. Die internen Abläufe der Nordlicht Technik GmbH kenne ich nicht, und es liegen mir keine Unterlagen wie Urlaubsrichtlinie, Handbuch oder Intranet-Seiten Ihres Unternehmens vor. Ich möchte nichts erfinden, was dann falsch ist.

So kommen Sie schnell zur richtigen Auskunft:

- **Personalabteilung / HR:** Sie kann Ihnen den offiziellen Ablauf und die Zuständigkeiten nennen.
- **Direkte Führungskraft:** In vielen Unternehmen genehmigt sie den Urlaub. Ob das bei Ihnen so ist, weiß ich nicht.
- **Intranet, Mitarbeiterhandbuch oder Personalsoftware:** Dort finden Sie oft Formulare, Fristen und Vertretungsregeln.
- **Betriebsrat (falls vorhanden):** Er kann zu Regeln wie Urlaubssperren oder Fristen Auskunft geben.

Allgemein läuft es in vielen Firmen so ab (nur als Orientierung, nicht als Aussage über Ihr Unternehmen):
1. Urlaubsantrag über ein Formular oder Tool einreichen, mit Zeitraum und ggf. Vertretung.
2. Die Führungskraft prüft ihn, etwa auf Teamplanung und Überschneidungen.
3. Sie genehmigt oder lehnt ab, danach erfolgt eine Rückmeldung und die Eintragung in den Kalender oder die Zeiterfassung.

Wenn Sie mir die Urlaubsrichtlinie oder den Text aus dem Intranet hier einfügen, fasse ich Ihnen den Ablauf gern übersichtlich zusammen oder formuliere einen Antrag.

---

### Modell: Claude Opus

**Nutzer 1**

Wie funktioniert bei der Nordlicht Technik GmbH die Urlaubsbeantragung, und wer ist bei uns für die Freigabe zuständig?

**Assistent 1**

Darauf kann ich Ihnen leider keine verlässliche Antwort geben. Ich habe keinen Zugriff auf die internen Unterlagen der Nordlicht Technik GmbH, also weder auf Ihr Intranet noch auf Ihr Personalhandbuch, Ihre Betriebsvereinbarungen oder Ihr HR-System. Wie die Urlaubsbeantragung bei Ihnen genau läuft und wer sie freigibt, weiß ich deshalb nicht. Raten möchte ich hier nicht, denn eine erfundene Antwort, die plausibel klingt, könnte Sie auf den falschen Weg schicken.

**So finden Sie die richtige Antwort schnell:**

1. **Intranet oder Mitarbeiterportal:** Suchen Sie nach „Urlaub“, „Abwesenheit“, „Urlaubsantrag“ oder „Personalhandbuch“.
2. **HR- oder Zeiterfassungssystem:** Viele Firmen nutzen dafür Programme wie Personio, SAP SuccessFactors, DATEV, ATOSS oder ein eigenes Self-Service-Portal. Dort steht oft auch gleich, wer den Antrag genehmigt.
3. **Ihre direkte Führungskraft:** In den meisten Unternehmen gibt die direkte Vorgesetzte oder der direkte Vorgesetzte den Urlaub frei. Ob das bei Ihnen auch so ist, sollten Sie aber kurz nachfragen.
4. **Personalabteilung (HR):** HR kann Ihnen den offiziellen Ablauf nennen und die Ansprechperson für die Freigabe.
5. **Arbeitsvertrag oder Betriebsvereinbarung:** Dort stehen manchmal Regeln zu Fristen, Urlaubssperren oder Vertretung.

**Was in Unternehmen oft üblich ist (nur zur Orientierung, nicht Ihre Firmenregel):**
- Sie stellen den Antrag schriftlich oder digital, meist einige Wochen vorher.
- Sie sprechen die Vertretung im Team ab.
- Die direkte Führungskraft gibt den Antrag frei, danach wird er in der Zeiterfassung oder im HR-System eingetragen.
- Für längere Urlaube oder Zeiten mit viel Betrieb gelten manchmal eigene Fristen.

Wenn Sie mir den Text aus Ihrem Personalhandbuch oder Intranet hier einfügen oder die Datei hochladen, fasse ich Ihnen den Ablauf gern verständlich zusammen. Ich kann Ihnen auch eine kurze E-Mail an HR oder Ihre Führungskraft formulieren, in der Sie nach dem Ablauf fragen.
