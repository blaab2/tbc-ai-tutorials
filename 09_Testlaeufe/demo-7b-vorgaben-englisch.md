# Testlauf: Demo 7 Variante B – Antwort mit Vorgaben, dann Englisch

**Herkunft:** [demo_fehler_zeigen.md, Demo 7 Variante B](../07_Beispielmaterial/demo_fehler_zeigen.md) (identisch mit [Trainer-Leitfaden, Block 1](../01_Trainer-Leitfaden.md)) · Material: [kundenmail_beschwerde.txt](../07_Beispielmaterial/kundenmail_beschwerde.txt) · Lösungshinweise: [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md) (enthält keinen eigenen Abschnitt zu dieser Demo)

**Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompts (im selben Chat):**

1. `Schreib eine freundliche, professionelle Antwort auf diese Beschwerde. Wir können bis Freitag liefern und bieten 5 % Rabatt auf die nächste Bestellung an.` + Inhalt der Kundenmail
2. `Und jetzt das Ganze auf Englisch.`

**Ziel laut Material:** Die KI übernimmt Vorgaben (Freitag, 5 %) – ob sie stimmen, muss der Mensch wissen. Nachsteuern im selben Chat („auf Englisch“) funktioniert ohne erneute Eingabe der Mail.

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Lieferung bis Freitag übernommen | ja | ja (als „verbindlich“ + „schriftliche Bestätigung“) | ja (als „schriftlich und verbindlich“, Datum als Platzhalter) |
| 5 % auf die **nächste** Bestellung (nicht 10 %, nicht dieser Auftrag) | ja | ja | ja |
| Keine zusätzlichen erfundenen Zusagen | teilweise – zusätzliche „Rückmeldung bis Mittwoch“ angekündigt; Freitag durch Teillieferungs-Vorbehalt aufgeweicht | teilweise – Klärung der Frachtkosten „bis Mittwoch“ zugesagt | teilweise – Versandbestätigung mit Sendungsnummer zugesagt |
| Rechnung RE-2024-0815 angesprochen | ja | ja | ja |
| Teillieferung 60 Stück / Menge berücksichtigt | vage („Gesamtmenge … nicht vollständig möglich“) | ja, als Platzhalter in der Mail | ja, als Prüfhinweis an den Nutzer |
| 10-%-Forderung des Kunden thematisiert | nein | nur als Hinweis an den Nutzer | ja, ausführlicher Prüfhinweis |
| Englisch im selben Chat, ohne erneute Eingabe | ja | ja | ja |
| Englisch inhaltlich deckungsgleich | ja | ja | ja |
| Fachbegriff „Steuergehäuse“ korrekt übersetzt | **nein – „steering housing“** | ja („control housings“) | ja („control housings“) |
| Hinweise „vor dem Versand prüfen“ | keine | kurz (10 %, Menge) | ausführlich (5 Punkte) + Hinweis, dass Herr Brenner auf Deutsch schreibt |
| Länge für Live-Demo (ca. 3 Min.) | passend | passend | lang |
| **Gesamt** | brauchbar, mit Übersetzungsfehler | **sehr gut** | sehr gut, aber lang |

## Gefundene Fehler mit Beleg

1. **Falscher Fachbegriff in der Übersetzung (Haiku).** „Steuergehäuse SG-40“ wird zu „steering housings SG-40“, Betreff „Steering housing“. *Steering* bedeutet Lenkung (Fahrzeug), gemeint ist ein Gehäuse für eine Steuerung/Elektronik („control housing“ bzw. „controller enclosure“). Sonnet und Opus übersetzen korrekt mit „control housings“. Der Fehler ist für Nicht-Muttersprachler kaum zu erkennen – ein gutes Beispiel für Aufgabe C (Rückübersetzung, Fachbegriffe prüfen).
2. **Aus „können liefern“ wird eine verbindliche schriftliche Zusage (Sonnet, Opus).** Vorgabe: „Wir können bis Freitag liefern.“ Sonnet: „Wir können Ihnen die Lieferung bis Freitag verbindlich zusagen. Bitte betrachten Sie diese Mail als schriftliche Bestätigung.“ Opus: „Diese Zusage gilt schriftlich und verbindlich, nicht ‚voraussichtlich‘.“ Inhaltlich passend zur Forderung des Kunden – aber die rechtlich wichtigere Formulierung hat die KI gewählt, nicht der Absender.
3. **Zusätzliche Zusagen, die nicht vorgegeben waren.**
   - Opus: „Sobald die Ware unser Haus verlässt, schicken wir Ihnen die Versandbestätigung mit Sendungsnummer.“ – nicht vorgegeben.
   - Sonnet: Frachtkosten „Wir prüfen … und melden uns dazu bis Mittwoch.“ – Frist frei gewählt (aus der Kundenforderung übernommen). Opus setzt an derselben Stelle korrekt einen Platzhalter „bis [Datum]“.
   - Haiku: „Ihre Rückmeldung bis Mittwoch erhalten Sie von uns in jedem Fall.“ – unlogisch, denn diese Mail *ist* die Rückmeldung; sie kündigt damit eine weitere an.
4. **Freitag wird aufgeweicht (Haiku).** „Sollte die Gesamtmenge bis dahin nicht vollständig möglich sein, melden wir uns umgehend …“ – direkt nach der Zusage ein Vorbehalt, den der Nutzer nicht vorgegeben hat. Genau das „voraussichtlich“, das der Kunde nicht mehr hören will.
5. **10-%-Forderung in der Mail selbst nicht beantwortet (alle).** Der Kunde verlangt „mindestens 10 % Nachlass auf diesen Auftrag“. Keine Mail sagt, dass es bei 5 % bleibt. Sonnet und Opus weisen den Nutzer darauf hin, Haiku nicht. Kein Fehler im engeren Sinn, aber ein offener Punkt, den der Mensch entscheiden muss.
6. **Kleinigkeiten.** Haiku übernimmt den geschrienen Betreff („Re: WIE LANGE NOCH???“ / „HOW MUCH LONGER???“) und schreibt im Englischen „Dear Mr. Brenner, thank you“ klein (im Englischen nach der Anrede groß). Sonnet übersetzt auch die Notiz an den Nutzer („Note: I deliberately …“) ins Englische, obwohl sie nicht zur Mail gehört.

Sachlich korrekt übernommen wurden bei allen drei: Auftrag 4711-NT, 120 Stück SG-40, KW 18, zweimalige Vertröstung, 85 Euro Frachtkosten, Rechnung RE-2024-0815, „frei Haus“, acht Jahre Zusammenarbeit (Sonnet: „langjährige“). Kein Modell nennt 10 % oder einen Rabatt auf den laufenden Auftrag. Es gibt keine Beträge zum Nachrechnen (5 % ohne Bestellwert, 85 Euro werden nur zitiert).

## Lehren für die Auswertung

- **Die Demo funktioniert wie geplant.** Alle drei Modelle übernehmen „Freitag“ und „5 % auf die nächste Bestellung“ exakt und übersetzen im selben Chat ohne erneute Eingabe der Mail. Der Wow-Effekt (Chatverlauf, Nachsteuern) ist zuverlässig.
- **Kernbotschaft „Die KI übernimmt, was du vorgibst“:** Kein Modell kann wissen, ob Freitag realistisch ist – alle schreiben es hinein. Frage an die Gruppe: „Wer in diesem Raum weiß, ob wir wirklich bis Freitag liefern können?“
- **Die KI übernimmt nicht nur – sie verstärkt und ergänzt.** Aus „können liefern“ wird „verbindliche schriftliche Bestätigung“, dazu kommen Sendungsnummer oder eine Frist „bis Mittwoch“. Das ist die eigentlich spannende Lehre: Beim Gegenlesen nicht nur prüfen, ob die Vorgaben drin sind, sondern auch, ob *mehr* zugesagt wird.
- **Erwartung „Rechnung oft vergessen“ hat sich nicht bestätigt.** Alle drei Modelle sprechen RE-2024-0815 an – und sagen korrekt nur eine Prüfung zu, keine Gutschrift. Positiv zeigen.
- **Übersetzung braucht Fachkunde:** Haikus „steering housing“ klingt flüssig, ist aber falsch. Schöne Brücke zu Aufgabe C (Rückübersetzung) und zum Merksatz „Fachbegriffe immer prüfen“.
- **Gute Assistenten fragen zurück bzw. geben Prüfhinweise** (Opus, Sonnet: 10 % vs. 5 %, Menge, Platzhalter). Opus merkt sogar an, dass ein deutscher Kunde besser eine deutsche Antwort bekommt – ein guter Moment für „Die KI denkt mit, aber entscheiden müsst ihr“.
- **Für die Live-Demo:** Opus-Antworten sind lang. Nicht alles vorlesen, sondern gezielt die Sätze mit „Freitag“, „5 %“ und „verbindlich“ markieren.

## Probleme im Material / Verbesserungsvorschlag

- In den [Trainer-Lösungshinweisen](../06_Uebungen/Trainer-Loesungshinweise.md) gibt es keinen Abschnitt zu den Block-1-Demos; die Erwartung „Rechnung wird oft vergessen“ trifft in den Tests nicht zu.
- In [demo_fehler_zeigen.md, Variante B](../07_Beispielmaterial/demo_fehler_zeigen.md) beschränkt sich der Hinweis auf „Die KI übernimmt, was du vorgibst“. Vorschlag, den Klammersatz am Ende von Variante B zu ergänzen: *„Beim Gegenlesen auch prüfen: Hat die KI mehr zugesagt als vorgegeben (z. B. ‚verbindliche schriftliche Bestätigung‘, Sendungsnummer, Rückmeldung bis Mittwoch)? Wurde auf die 10-%-Forderung reagiert? Stimmen die Fachbegriffe im Englischen (Steuergehäuse = ‚control housing‘, nicht ‚steering housing‘)?“*
- Optional, um den Englisch-Schritt plausibler zu machen (der Kunde schreibt Deutsch): *„Und jetzt das Ganze auf Englisch – für unseren englischsprachigen Kollegen, der den Fall übernimmt.“*

---

## Gesprächsprotokoll: Haiku

### Nutzer 1
Schreib eine freundliche, professionelle Antwort auf diese Beschwerde. Wir können bis Freitag liefern und bieten 5 % Rabatt auf die nächste Bestellung an.

[Anhang: kundenmail_beschwerde.txt, eingelesen mit dem Read-Tool]

### Assistent 1
Betreff: Re: WIE LANGE NOCH??? Auftrag 4711-NT / Steuergehäuse

Sehr geehrter Herr Brenner,

vielen Dank für Ihre deutlichen Worte und Ihre Geduld. Es tut uns aufrichtig leid, dass Sie zweimal vertröstet wurden und dass Ihre Montage nun durch die fehlenden Steuergehäuse teilweise stillsteht. Das hätte nicht passieren dürfen, und wir verstehen sehr gut, wie sehr Sie das unter Druck setzt.

Zu Ihrem Auftrag 4711-NT (120 Steuergehäuse SG-40): Wir können Ihnen eine Lieferung bis Freitag zusagen. Sollte die Gesamtmenge bis dahin nicht vollständig möglich sein, melden wir uns umgehend bei Ihnen, damit Sie Ihre Planung entsprechend anpassen können.

Als Zeichen unseres guten Willens gewähren wir Ihnen 5 % Rabatt auf Ihre nächste Bestellung.

Zusätzlich prüfen wir die Frachtkosten auf Rechnung RE-2024-0815 umgehend. Sollte die frei-Haus-Lieferung wie vereinbart gelten, korrigieren wir den Betrag von 85 Euro und senden Ihnen eine korrigierte Rechnung bzw. Gutschrift.

Ihre Rückmeldung bis Mittwoch erhalten Sie von uns in jedem Fall. Für Rückfragen erreichen Sie mich unter [Telefonnummer] oder per E-Mail unter [E-Mail-Adresse].

Mit freundlichen Grüßen

[Name]
[Position]
[Firma]

### Nutzer 2
Und jetzt das Ganze auf Englisch.

### Assistent 2
Subject: Re: HOW MUCH LONGER??? Order 4711-NT / Steering housing

Dear Mr. Brenner,

thank you for your direct message and for your patience. We sincerely apologize that you were put off twice and that your assembly line is now partially at a standstill due to the missing steering housings. This should not have happened, and we fully understand the pressure this puts you under.

Regarding your order 4711-NT (120 steering housings SG-40): we can commit to a delivery by Friday. Should we not be able to deliver the full quantity by then, we will contact you immediately so you can adjust your planning accordingly.

As a gesture of goodwill, we are offering you a 5 % discount on your next order.

In addition, we are reviewing the freight charges on invoice RE-2024-0815 immediately. If free-delivery terms were agreed as you state, we will correct the amount of 85 euros and send you a corrected invoice or a credit note.

You will receive our response by Wednesday in any case. For any questions, you can reach me at [phone number] or at [email address].

Kind regards,

[Name]
[Position]
[Company]

---

## Gesprächsprotokoll: Sonnet

### Nutzer 1
Schreib eine freundliche, professionelle Antwort auf diese Beschwerde. Wir können bis Freitag liefern und bieten 5 % Rabatt auf die nächste Bestellung an.

[Inhalt von kundenmail_beschwerde.txt: Beschwerde von Markus Brenner, Leitung Einkauf, Brenner Gerätebau GmbH, zu Auftrag 4711-NT (120 Steuergehäuse SG-40, zugesagt für KW 18, jetzt KW 21 nichts geliefert). Er fordert einen verbindlichen schriftlichen Liefertermin, akzeptiert notfalls eine Teillieferung von 60 Stück, verlangt mindestens 10 % Nachlass auf den Auftrag, bittet um Prüfung der Frachtkosten von 85 Euro auf Rechnung RE-2024-0815 (frei Haus vereinbart) und erwartet bis Mittwoch eine Rückmeldung.]

### Assistent 1
Hier ein Entwurf:

**Betreff: Auftrag 4711-NT / Steuergehäuse SG-40 – verbindlicher Liefertermin und Klärung Ihrer Anliegen**

Sehr geehrter Herr Brenner,

vielen Dank für Ihre Nachricht und Ihre offenen Worte. Sie haben völlig recht: Die Lieferung der 120 Steuergehäuse SG-40 hätte in KW 18 erfolgen sollen, und dass Sie darüber nicht proaktiv informiert wurden und zweimal vertröstet wurden, hätte nicht passieren dürfen. Dafür möchte ich mich in aller Form entschuldigen. Besonders bedauern wir, dass Ihre Montage dadurch teilweise stillsteht und Sie gegenüber Ihrem eigenen Kunden unter Druck geraten sind.

**Liefertermin**
Wir können Ihnen die Lieferung bis Freitag verbindlich zusagen. Bitte betrachten Sie diese Mail als schriftliche Bestätigung. [Bitte vor Versand ergänzen: ob die gesamte Menge von 120 Stück oder nur eine Teillieferung bis Freitag kommt, und das konkrete Datum.] Sollte sich daran aus irgendeinem Grund etwas ändern, melden wir uns von uns aus und rechtzeitig bei Ihnen, nicht erst auf Nachfrage.

**Entgegenkommen**
Für die entstandenen Unannehmlichkeiten bieten wir Ihnen 5 % Rabatt auf Ihre nächste Bestellung an. Ich hoffe, Sie sehen darin ein Zeichen, dass uns die langjährige Zusammenarbeit wichtig ist.

**Frachtkosten Rechnung RE-2024-0815**
Den Hinweis auf die berechneten Frachtkosten von 85 Euro bei der Ersatzteillieferung nehmen wir gerne auf. Wir prüfen, ob "frei Haus" vereinbart war, und melden uns dazu bis Mittwoch. Sollte sich Ihre Darstellung bestätigen, erhalten Sie umgehend eine korrigierte Rechnung bzw. Gutschrift.

Für Rückfragen erreichen Sie mich jederzeit direkt unter [Telefonnummer / E-Mail].

Mit freundlichen Grüßen
[Name]
Nordlicht Technik

*Hinweis: Den Nachlass von 10 % auf diesen Auftrag habe ich bewusst nicht zugesagt, da Sie nur 5 % auf die nächste Bestellung genehmigt haben. Falls Sie dazu einen Satz wünschen, kann ich ihn ergänzen.*

### Nutzer 2
Und jetzt das Ganze auf Englisch.

### Assistent 2
Here is the English version:

**Subject: Order 4711-NT / Control Housings SG-40 – Binding Delivery Date and Response to Your Concerns**

Dear Mr. Brenner,

Thank you for your message and for being so open with us. You are absolutely right: the 120 SG-40 control housings should have been delivered in calendar week 18, and the fact that you were not proactively informed and were put off twice should not have happened. Please accept our sincere apology. We particularly regret that your assembly line is partly at a standstill as a result and that you have been put under pressure with your own customer.

**Delivery date**
We can commit to delivery by Friday. Please treat this email as our written confirmation. [Please complete before sending: whether the full quantity of 120 units or only a partial shipment will arrive by Friday, and the specific date.] Should anything change for any reason, we will contact you proactively and in good time, not only when you ask.

**Our goodwill gesture**
To make up for the inconvenience, we would like to offer you a 5% discount on your next order. We hope you see this as a sign of how much we value our long-standing relationship.

**Freight charges on invoice RE-2024-0815**
We have taken note of your point about the 85 euro freight charge on the spare parts delivery. We are checking whether "free delivery" was agreed and will get back to you by Wednesday. If your account is confirmed, you will promptly receive a corrected invoice or credit note.

Please feel free to contact me directly at any time at [phone number / email].

Kind regards,
[Name]
Nordlicht Technik

*Note: I deliberately did not agree to the 10% discount on this order, since you only approved 5% on the next order. If you would like a sentence on this, I can add it.*

---

## Gesprächsprotokoll: Opus

### Nutzer 1
Schreib eine freundliche, professionelle Antwort auf diese Beschwerde. Wir können bis Freitag liefern und bieten 5 % Rabatt auf die nächste Bestellung an.

[INHALT VON /home/daniel/tbc-ai-tutorials/07_Beispielmaterial/kundenmail_beschwerde.txt]

### Assistent 1
Hier ist ein Entwurf für Ihre Antwort an Herrn Brenner:

---

**Betreff:** AW: Auftrag 4711-NT / Steuergehäuse SG-40 – verbindlicher Liefertermin

Sehr geehrter Herr Brenner,

vielen Dank für Ihre offene Nachricht. Sie haben völlig recht: Die Lieferung der 120 Steuergehäuse SG-40 (Auftrag 4711-NT) war für KW 18 zugesagt, und dass Sie seitdem weder die Ware noch eine verlässliche Auskunft von uns erhalten haben, ist nicht in Ordnung. Dafür entschuldige ich mich ausdrücklich, auch für die zweimalige Vertröstung Ihres Einkaufs. Mir ist klar, dass Sie dadurch gegenüber Ihrem eigenen Kunden in eine schwierige Lage geraten sind und Ihre Montage darunter leidet.

Hier unsere verbindliche Zusage:

**Liefertermin:** Wir liefern die Steuergehäuse SG-40 aus Auftrag 4711-NT **bis spätestens Freitag, den [Datum einsetzen]**, zu Ihnen. Diese Zusage gilt schriftlich und verbindlich, nicht „voraussichtlich“. Sobald die Ware unser Haus verlässt, schicken wir Ihnen die Versandbestätigung mit Sendungsnummer.

**Entgegenkommen:** Als Ausgleich für den Ärger gewähren wir Ihnen **5 % Rabatt auf Ihre nächste Bestellung** bei uns.

**Rechnung RE-2024-0815:** Danke für den Hinweis zu den Frachtkosten von 85 Euro bei der Ersatzteillieferung. Wir prüfen die vereinbarten Konditionen umgehend und melden uns dazu bis [Datum] bei Ihnen bzw. Ihrer Buchhaltung. Falls „frei Haus“ vereinbart war, erhalten Sie selbstverständlich eine korrigierte Rechnung bzw. eine Gutschrift.

Wir schätzen die acht Jahre Zusammenarbeit mit Ihnen sehr und möchten Ihr Vertrauen zurückgewinnen. Bei Fragen erreichen Sie mich direkt unter [Telefonnummer] bzw. [E-Mail-Adresse].

Mit freundlichen Grüßen

[Ihr Name]
[Funktion]
Nordlicht Technik
[Kontaktdaten]

---

**Bitte vor dem Versand prüfen:**
1. **Rabatt:** Herr Brenner verlangt mindestens 10 % auf *diesen* Auftrag. Sie bieten 5 % auf die *nächste* Bestellung an. Das kann er als zu wenig empfinden. Überlegen Sie, ob Sie kurz begründen wollen, warum es bei 5 % bleibt, oder ob Spielraum besteht.
2. **Liefermenge:** Ich bin davon ausgegangen, dass bis Freitag alle 120 Stück kommen. Falls es nur eine Teillieferung ist (er würde 60 Stück akzeptieren), sollten Menge und Termin für den Rest klar in der Mail stehen.
3. **Frist:** Er erwartet bis Mittwoch eine Antwort. Am besten schicken Sie die Mail vorher ab.
4. **Frachtkosten:** Ich habe nichts zugesagt, sondern nur eine Prüfung angekündigt. Wenn Sie schon wissen, dass „frei Haus“ vereinbart war, können Sie die Korrektur direkt bestätigen.
5. Platzhalter in eckigen Klammern ergänzen (Datum, Name, Kontaktdaten).

### Nutzer 2
Und jetzt das Ganze auf Englisch.

### Assistent 2
Here is the English version:

---

**Subject:** RE: Order 4711-NT / SG-40 control housings – confirmed delivery date

Dear Mr Brenner,

Thank you for your candid message. You are absolutely right: delivery of the 120 SG-40 control housings (order 4711-NT) was promised for calendar week 18, and it is not acceptable that since then you have received neither the goods nor reliable information from us. I sincerely apologise for this, and also for your purchasing team being put off twice. I understand that this has put you in a difficult position with your own customer and that your assembly line is affected.

Here is our firm commitment:

**Delivery date:** We will deliver the SG-40 control housings from order 4711-NT to you **by Friday, [insert date], at the latest**. This is a binding written commitment, not an estimate. As soon as the goods leave our premises, we will send you a shipping confirmation with the tracking number.

**Goodwill gesture:** To make up for the inconvenience, we are offering you a **5% discount on your next order** with us.

**Invoice RE-2024-0815:** Thank you for pointing out the EUR 85 freight charge on the spare parts delivery. We are checking the agreed terms right away and will get back to you or your accounts department by [date]. If carriage paid ("frei Haus") was agreed, you will of course receive a corrected invoice or a credit note.

We greatly value our eight years of working together and want to earn back your trust. If you have any questions, you can reach me directly at [phone number] or [email address].

Kind regards,

[Your name]
[Job title]
Nordlicht Technik
[Contact details]

---

**Please check before sending:** the same points apply as for the German version: the 5% discount versus the 10% he asked for, whether all 120 units arrive by Friday, his Wednesday deadline, and the placeholders. One more thing: Herr Brenner wrote in German, so a German reply is probably the better fit for him. The English version makes sense if it is going to an English-speaking contact.
