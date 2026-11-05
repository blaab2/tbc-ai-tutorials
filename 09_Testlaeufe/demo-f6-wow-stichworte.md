# Testlauf: Folie 6 / Demo 7 Variante C – Mail aus Stichworten, lockerer, Englisch

**Herkunft:** [Folie 6 – Live-Demo: Wow – und Hoppla](../04_Folien.md) (Sprechernotiz „Teil 1 – Wow“) und [demo_fehler_zeigen.md, Variante C](../07_Beispielmaterial/demo_fehler_zeigen.md)

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompts (alle im selben Chat):**

1. `Mail an Kunden: Lieferung verschiebt sich um 1 Woche, Grund Materialengpass, wir bieten kostenlosen Expressversand an.`
2. `Jetzt bitte etwas lockerer.`
3. `Und jetzt auf Englisch.`

**Ziel laut Material:** Wow-Moment – aus drei Stichworten entsteht in Sekunden eine höfliche, versandfähige Kundenmail; Nachsteuern im selben Chat funktioniert ohne Neuanfang.

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Höfliche, versandfähige Mail (V1) | ja | ja | ja (sehr ausführlich) |
| „1 Woche“ in allen Versionen exakt erhalten | nein – V2/V3 „etwa eine Woche“ / „about a week“ | ja (V1–V3) | nein – schon V1 „etwa eine Woche“, V3 „about a week“ |
| Grund Materialengpass erhalten | ja, aber ausgeschmückt („bei unserem Lieferanten“) | ja | ja, leicht verengt („Engpass bei einem benötigten Material“) |
| Kostenloser Expressversand erhalten | ja, aber als Opt-in („melden Sie sich bei Interesse“) | ja | ja, automatisch („Sie müssen dafür nichts tun“) |
| Keine erfundenen Details / nur Platzhalter | teilweise – Lieferant erfunden; Platzhalter [Ihr Name], [Firma], [Vorname] | ja – plus Hinweis, Bestellnr. und Datum zu ergänzen | teilweise – „trotz sorgfältiger Planung“ erfunden; Bestellnr./Datum sauber als Platzhalter |
| V2 merklich lockerer, noch professionell | ja | ja, kleiner Stilbruch („Hallo zusammen“ an einen Kunden) | ja (eher leicht lockerer) |
| V3 = Englisch der lockeren Version, deckungsgleich | ja (übernimmt auch „about“) | ja | ja (übernimmt auch „about“) |
| Chatverlauf genutzt, kein Neuanfang | ja | ja | ja |
| Länge für Live-Demo (2 Min.) | kurz, ideal | kurz, ideal | lang, Vorlesen kostet Zeit |
| **Gesamt** | gut, mit Faktendrift | **am besten** | gut, mit Faktendrift und Ausschmückung |

## Gefundene Fehler mit Beleg

1. **Faktendrift „1 Woche“ → „etwa eine Woche“** (Haiku V2/V3, Opus V1–V3). Vorgabe im Prompt: „verschiebt sich um 1 Woche“. Haiku V2: „verschiebt sich leider um *etwa* eine Woche“, V3: „pushed back by *about* a week“. Opus V1: „um *etwa* eine Woche verzögert“, V3: „*about* a week later“. Die Zusage wird ungefragt aufgeweicht – im Kundenkontakt kein harmloser Unterschied.
2. **Erfundener Lieferant** (Haiku V1–V3): „Materialengpass *bei unserem Lieferanten*“ / „short on materials *from our supplier*“. Im Prompt steht nur „Materialengpass“; ob ein Lieferant schuld ist, weiß die KI nicht.
3. **Erfundene Begründung** (Opus V1): „auf den wir *trotz sorgfältiger Planung* keinen Einfluss hatten“ – nicht vorgegeben. Ebenso „Engpass bei *einem* benötigten Material“ (V1–V3), eine Verengung gegenüber der Vorgabe.
4. **Ablauf des Expressversands ergänzt – je Modell unterschiedlich.** Der Prompt sagt nur „wir bieten kostenlosen Expressversand an“. Haiku macht daraus ein Opt-in („Bitte melden Sie sich bei Interesse kurz bei uns“), Opus einen Automatismus („versenden wir … sobald die Ware verfügbar ist. Sie müssen dafür nichts weiter tun“). Beides ist plausibel, aber eine Entscheidung, die der Absender treffen muss.
5. **Kleiner Stilbruch** (Sonnet V2): „Hallo zusammen“ in einer Mail an einen einzelnen Kunden mit „Sie“-Anrede.
6. Kleinigkeit (Haiku V1): „leider muss *ich* Ihnen mitteilen“ und danach „*wir* bieten“ – Ich/Wir-Wechsel.

Keine Zahlen zum Nachrechnen außer der „1 Woche“; kein Modell nennt ein konkretes Datum, eine Auftragsnummer oder einen Kundennamen – das bleibt bei allen ein Platzhalter oder fehlt.

## Lehren für die Auswertung

- **Der Wow-Moment funktioniert zuverlässig.** Alle drei Modelle liefern in einem Schritt eine brauchbare Mail, setzen „lockerer“ und „Englisch“ ohne Wiederholung des Inhalts um – der Chatverlauf wird erkennbar genutzt. Sonnet und Haiku sind dabei kurz genug für die geplanten 2 Minuten.
- **Bonus-Lehre direkt aus dem Wow-Teil:** Auch eine gute Mail muss gegengelesen werden. Zwei von drei Modellen haben aus „1 Woche“ ein „etwa eine Woche“ gemacht, eines hat einen Lieferanten als Schuldigen erfunden. Damit lässt sich elegant zu „Hoppla“ überleiten: „Klingt super – aber steht da noch, was wir vorgegeben haben?“
- **Die KI füllt Lücken.** Wie der Kunde den Expressversand bekommt (automatisch oder auf Nachfrage), stand nicht im Prompt – jedes Modell hat es anders entschieden. Gute Frage an die Runde: „Wer entscheidet das eigentlich – ihr oder die KI?“
- **Platzhalter sind ein Qualitätsmerkmal.** Opus und Sonnet weisen auf Bestellnummer und Liefertermin hin, statt sie zu erfinden. Das ist gut – und zeigt, was ein Mensch noch ergänzen muss.
- **Gleicher Prompt, unterschiedliche Ergebnisse** – passt zur Folienbotschaft „Ergebnisse können bei euch anders aussehen“.
- Für die Live-Demo: Bei langen Antworten (Opus-Stil) nicht alles vorlesen, sondern nur Betreff, Anrede und den Satz mit „Woche“ zeigen.

## Probleme im Material / Verbesserungsvorschlag

- Die Sprechernotiz zu Teil 1 (Folie 6, [04_Folien.md](../04_Folien.md)) zeigt nur die Geschwindigkeit, nicht das Gegenlesen. Vorschlag: am Ende von „Teil 1 – Wow“ ergänzen: *„Kurz gegenlesen lassen: Steht noch ‚1 Woche‘ drin – oder ‚etwa eine Woche‘? Hat die KI etwas dazuerfunden (z. B. einen Lieferanten)? Wie bekommt der Kunde den Expressversand?“*
- In [demo_fehler_zeigen.md, Variante C](../07_Beispielmaterial/demo_fehler_zeigen.md) fehlt (anders als bei Variante A) ein Absatz „Was du zeigen willst“. Vorschlag: *„Was du zeigen willst: Tempo und Nachsteuern im selben Chat. Danach prüfen: Sind alle drei Fakten (1 Woche, Materialengpass, kostenloser Express) noch exakt drin? In Tests wurde ‚1 Woche‘ öfter zu ‚etwa eine Woche‘ und ein Lieferant als Ursache dazugedichtet.“*

---

## Gesprächsprotokoll: Haiku

### Nutzer 1
Mail an Kunden: Lieferung verschiebt sich um 1 Woche, Grund Materialengpass, wir bieten kostenlosen Expressversand an.

### Assistent 1
Betreff: Verschiebung Ihrer Lieferung um eine Woche

Sehr geehrte Damen und Herren,

leider muss ich Ihnen mitteilen, dass sich die Lieferung Ihrer Bestellung um eine Woche verschiebt. Grund dafür ist ein Materialengpass bei unserem Lieferanten, auf den wir leider keinen Einfluss haben.

Um die Unannehmlichkeiten für Sie so gering wie möglich zu halten, bieten wir Ihnen kostenlosen Expressversand an. Bitte melden Sie sich bei Interesse kurz bei uns, dann veranlassen wir den Versand umgehend.

Wir bitten um Ihr Verständnis für die Verzögerung und danken Ihnen für Ihre Geduld.

Mit freundlichen Grüßen
[Ihr Name]
[Firma]

### Nutzer 2
Jetzt bitte etwas lockerer.

### Assistent 2
Betreff: Kleine Verzögerung bei Ihrer Lieferung

Hallo [Vorname],

kurze Info vorab: Ihre Lieferung verschiebt sich leider um etwa eine Woche. Der Grund ist ein Materialengpass bei unserem Lieferanten, da können wir gerade leider nichts dran drehen.

Als kleinen Ausgleich schicken wir Ihnen die Bestellung per Express, und das kostet Sie nichts. Sagen Sie einfach kurz Bescheid, dann kümmern wir uns darum.

Danke für Ihr Verständnis und viele Grüße
[Ihr Name]
[Firma]

### Nutzer 3
Und jetzt auf Englisch.

### Assistent 3
Subject: Slight delay in your delivery

Hi [First name],

Quick heads-up: your delivery is going to be pushed back by about a week. We're short on materials from our supplier, and unfortunately we can't do much about that right now.

To make up for it, we'll ship your order express at no cost to you. Just let us know and we'll take care of it.

Thanks for your patience, and best regards,
[Your name]
[Company]

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1
Mail an Kunden: Lieferung verschiebt sich um 1 Woche, Grund Materialengpass, wir bieten kostenlosen Expressversand an.

### Assistent 1
Hier ein Entwurf:

**Betreff:** Ihre Bestellung: Lieferung verschiebt sich um eine Woche

Sehr geehrte Damen und Herren,

leider müssen wir Ihnen mitteilen, dass sich die Lieferung Ihrer Bestellung um eine Woche verschiebt. Der Grund ist ein aktueller Materialengpass, auf den wir leider keinen Einfluss hatten.

Wir bedauern die Unannehmlichkeiten sehr. Als Entschädigung bieten wir Ihnen den Versand per Express selbstverständlich kostenlos an, damit Sie Ihre Ware so schnell wie möglich erhalten.

Falls Sie Fragen haben oder Ihre Bestellung anpassen möchten, melden Sie sich gerne bei uns.

Vielen Dank für Ihr Verständnis und Ihre Geduld.

Mit freundlichen Grüßen
[Name]
[Firma]

Hinweis: Ergänzen Sie gern Bestell- oder Kundennummer sowie das neue voraussichtliche Lieferdatum, damit die Mail für Ihre Kunden noch konkreter wird.

### Nutzer 2
Jetzt bitte etwas lockerer.

### Assistent 2
Gerne, hier eine lockerere Version:

**Betreff:** Kleine Verzögerung bei Ihrer Bestellung

Hallo zusammen,

kurze Info von uns: Ihre Lieferung kommt eine Woche später als geplant. Der Grund: Uns fehlt aktuell Material, und das ist leider nicht ganz unter unserer Kontrolle.

Damit Sie nicht länger warten müssen als nötig, schicken wir Ihr Paket dafür kostenlos per Express. Das geht aufs Haus!

Wenn Sie Fragen haben oder etwas ändern möchten, schreiben Sie uns einfach.

Danke für Ihre Geduld, wir wissen das zu schätzen!

Viele Grüße
[Name]
[Firma]

### Nutzer 3
Und jetzt auf Englisch.

### Assistent 3
Sure, here's the English version, keeping the relaxed tone:

**Subject:** Small delay with your order

Hi there,

Quick heads-up: your delivery will arrive one week later than planned. The reason is a current material shortage, which is unfortunately not entirely in our hands.

To make up for it, we're shipping your order via express, free of charge. It's on us!

If you have any questions or want to change anything, just drop us a line.

Thanks for your patience, we really appreciate it!

Best regards,
[Name]
[Company]

---

## Gesprächsprotokoll: Opus

### Nutzer 1
Mail an Kunden: Lieferung verschiebt sich um 1 Woche, Grund Materialengpass, wir bieten kostenlosen Expressversand an.

### Assistent 1
Hier ist ein Entwurf für die Kundenmail:

---

**Betreff:** Ihre Bestellung [Bestellnummer]: neuer Liefertermin

Sehr geehrte/r Frau/Herr [Name],

vielen Dank für Ihre Bestellung und Ihr Vertrauen in uns.

Leider müssen wir Ihnen mitteilen, dass sich die Lieferung Ihrer Bestellung um etwa eine Woche verzögert. Grund dafür ist ein Engpass bei einem benötigten Material, auf den wir trotz sorgfältiger Planung keinen Einfluss hatten. Der neue voraussichtliche Liefertermin ist der [Datum].

Wir bitten Sie, die Unannehmlichkeiten zu entschuldigen. Als kleinen Ausgleich versenden wir Ihre Bestellung kostenlos per Expressversand, sobald die Ware verfügbar ist. Sie müssen dafür nichts weiter tun.

Wenn Sie Fragen haben oder der neue Termin für Sie ein Problem ist, melden Sie sich gerne jederzeit bei uns. Wir finden gemeinsam eine Lösung.

Vielen Dank für Ihr Verständnis.

Mit freundlichen Grüßen

[Ihr Name]
[Position]
[Firma]
[Telefon / E-Mail]

---

Setzen Sie vor dem Versand noch die Platzhalter in eckigen Klammern ein. Soll ich die Mail kürzer fassen oder den Ton anpassen?

### Nutzer 2
Jetzt bitte etwas lockerer.

### Assistent 2
Gerne, hier eine lockerere Version:

---

**Betreff:** Kleine Verzögerung bei Ihrer Bestellung [Bestellnummer]

Hallo Frau/Herr [Name],

leider haben wir keine so gute Nachricht: Ihre Bestellung kommt etwa eine Woche später als geplant. Bei einem Material, das wir dafür brauchen, gibt es gerade einen Engpass, und darauf haben wir leider keinen Einfluss.

Neuer voraussichtlicher Liefertermin: **[Datum]**

Das tut uns wirklich leid! Als Dankeschön für Ihre Geduld schicken wir Ihnen die Ware kostenlos per Express, sobald sie da ist. Sie müssen dafür nichts tun.

Haben Sie Fragen, oder passt der neue Termin gar nicht? Melden Sie sich einfach bei uns, wir finden bestimmt eine Lösung.

Danke für Ihr Verständnis und viele Grüße

[Ihr Name]
[Firma]
[Telefon / E-Mail]

---

Falls Sie Ihre Kunden duzen, kann ich die Mail auch gerne auf „Du“ umschreiben.

### Nutzer 3
Und jetzt auf Englisch.

### Assistent 3
Here's the relaxed version in English:

---

**Subject:** Quick update on your order [order number]

Hi [Name],

We're afraid we have some not-so-great news: your order will arrive about a week later than planned. There's currently a shortage of one of the materials we need, and unfortunately it's out of our hands.

New estimated delivery date: **[date]**

We're really sorry about this! To thank you for your patience, we'll ship your order by express delivery free of charge as soon as it's ready. There's nothing you need to do.

Got any questions, or does the new date not work for you? Just get in touch and we'll find a solution together.

Thanks so much for your understanding!

Best regards,

[Your name]
[Company]
[Phone / email]

---

Remember to fill in the placeholders in square brackets before sending. Would you like a more formal English version as well?
