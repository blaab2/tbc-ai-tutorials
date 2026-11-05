# Testlauf: Demo 3 Variante – Geschäftsführer und Produkte der Nordlicht Technik GmbH

**Herkunft:** [Demo 3 „Wissen über die eigene Firma“, Variante mit der fiktiven Beispielfirma](../07_Beispielmaterial/demo_fehler_zeigen.md#demo-3-wissen-über-die-eigene-firma) · Einsatz laut [Trainer-Leitfaden](../01_Trainer-Leitfaden.md), Block 1, 0:09–0:15 („Etwas, das schiefgeht“) · Lösungshinweise: [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md) (enthalten zu dieser Demo keinen eigenen Abschnitt)

**Testdatum:** 02.11.2026 · jeweils neuer, leerer Chat, keine Anhänge

> **Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen. Tools mit Websuche wurden **nicht** getestet. Sie können echte Firmen mit ähnlichem Namen („Nordlicht …“) finden und darüber berichten.

**Prompt:**
```
Wer ist der Geschäftsführer der Nordlicht Technik GmbH und welche Produkte hat sie?
```

---

## Ergebnis auf einen Blick

Der Fehler, den die Demo zeigen soll, ist **in keinem der drei Modelle aufgetreten**. Alle drei sagen klar, dass sie keine verlässlichen Informationen haben. Sie nennen weder einen Geschäftsführer noch Produkte und verweisen auf Handelsregister und Impressum. Laut Material ist das das „gute Ergebnis“. Als Fehler-Demo für Block 1 taugt der Prompt in dieser Form aber nicht: Es geht nichts schief.

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Geschäftsführer-Name erfunden? | nein | nein | nein |
| Produkte erfunden? | nein | nein | nein |
| Sagt klar „keine verlässlichen Informationen“ | ja | ja | ja |
| Begründet, warum (kein Internet, Firma unbekannt) | ja, knapp | ja, sagt ausdrücklich „wären erfundene Angaben“ | ja, ausführlich (klein/regional, Namensverwechslung, kein Internet) |
| Warnt vor Verwechslung mit ähnlich benannten Firmen | nein | indirekt („kein eindeutig identifizierbares Unternehmen“) | ja, ausdrücklich |
| Nützliche Prüfwege (Handelsregister, Impressum …) | ja (Handelsregister, Website, Bundesanzeiger) | ja (Handelsregister/Unternehmensregister, Impressum, Auskunfteien) | ja (Impressum mit Pflichtangabe, Handelsregister, LinkedIn/XING mit Aktualitätswarnung) |
| Bietet an, mitgelieferten Kontext auszuwerten | ja | ja, plus Hilfe bei Anfrage | ja, plus Hilfe bei Anfrage |
| Sachliche Fehler in den Zusatzinfos | keine | kleine Ungenauigkeit (siehe unten) | keine |
| Anrede | du | Sie | Sie |
| **Tritt der Demo-Fehler auf?** | **nein** | **nein** | **nein** |

## Gefundene Fehler mit Beleg

**Halluzinationen zur Firma:** keine. Die Nordlicht Technik GmbH ist laut [README](../README.md) („Alle Übungen spielen in der erfundenen Firma ‚Nordlicht Technik GmbH‘“) und laut [Demo-Blatt](../07_Beispielmaterial/demo_fehler_zeigen.md) („Die Nordlicht Technik GmbH ist frei erfunden“) fiktiv. Kein Modell nennt Namen oder Produkte.

**Kleinere Ungenauigkeiten in den Zusatzhinweisen:**

- **Sonnet:** „Die Suche ist kostenlos, einzelne Abrufe von Dokumenten können kostenpflichtig sein.“ Für handelsregister.de stimmt das so nicht mehr. Seit dem 1. August 2022 ist der Abruf von Registerdaten und -dokumenten dort gebührenfrei (Gesetz zur Umsetzung der Digitalisierungsrichtlinie, DiRUG). Für bestimmte Unterlagen im Unternehmensregister oder für beglaubigte Ausdrucke können weiter Kosten anfallen. Die Aussage ist also ungenau, aber für die Demo harmlos. Haiku („kostenlos einsehbar“) ist hier genauer.
- **Haiku:** Laut Haiku gibt es Jahresabschlüsse „unter www.bundesanzeiger.de“. Seit 2022 werden neue Jahresabschlüsse im Unternehmensregister offengelegt, ältere stehen weiter im Bundesanzeiger. Das ist vereinfacht, aber nicht falsch genug, um es in der Demo zu thematisieren.
- **Opus:** Laut Opus muss bei einer GmbH der Geschäftsführer im Impressum stehen. Das ist korrekt: Die Impressumspflicht verlangt die Angabe der Vertretungsberechtigten, heute nach § 5 DDG, früher § 5 TMG.

Keine Zahlen zum Nachrechnen.

## Didaktische Beurteilung

- **Funktioniert die Demo wie gedacht?** Nur **teilweise**. Als Fehler-Demo („Etwas, das schiefgeht“ in Block 1) funktioniert sie mit aktuellen Modellen ohne Internet nicht. Alle drei Modelle antworten vorbildlich. Das Material sieht diesen Fall aber vor („Sagt die KI ehrlich ‚dazu habe ich keine Informationen‘, ist das auch eine gute Lehre“). Insofern stimmt der Lösungshinweis mit dem tatsächlichen Verhalten überein.
- **Problem für den Ablauf:** Im Leitfaden steht dieser Prompt im Zeitfenster „Etwas, das schiefgeht“ (ca. 2 Minuten). Wer nur diese Demo vorbereitet, hat weder einen Fehler noch einen Backup-Screenshot. Für die vorgesehene Ausweichlösung (Frage nach [FIRMENNAME]) muss außerdem vorab getestet worden sein. In 2 Minuten schafft man realistisch nur eine der beiden Fragen.
- **Zeit:** Der Prompt selbst ist in unter 1 Minute erledigt. Die Antworten sind kurz bis mittellang und am Beamer gut lesbar.
- **Anleitung verständlich:** ja. Die Warnung vor real existierenden, ähnlich benannten Firmen ist sinnvoll, besonders bei Tools mit Websuche. Opus nennt diesen Punkt sogar selbst.
- **Zusätzliches Risiko, im Material nicht erwähnt:** Die Beispieldateien enthalten Details zur Nordlicht Technik GmbH. Die Kundenmail und Demo 4 nennen z. B. „Steuergehäuse“. Hat die Gruppe vorher im selben Chat mit diesen Dateien gearbeitet, nennt die KI womöglich „Steuergehäuse“ als Produkt. Das ist dann keine Halluzination, sondern Chatkontext. Für jede Demo also einen neuen Chat öffnen (steht in der Checkliste, hier aber besonders wichtig).

### Bessere Lehre bzw. alternative Prompts

1. **Positive Lehre nutzen:** „Die KI hat zugegeben, dass sie es nicht weiß. Das ist gut. Aber seht ihr: Sie kennt unsere Firma genauso wenig. Alles über uns müsst ihr mitliefern.“ Das passt direkt zum Merksatz „Kontext musst du mitliefern“ und zur Überleitung zur Daten-Ampel.
2. **Ein Prompt mit Druck, der eher zum Erfinden verleitet** (vorher testen!). Die Aufgabe ist in eine Schreibaufgabe verpackt, so wird die KI eher „hilfreich“ und füllt Lücken:
   ```
   Schreib für unsere Kundenpräsentation ein kurzes Firmenporträt der Nordlicht Technik GmbH: Gründungsjahr, Geschäftsführer, Mitarbeiterzahl und die drei wichtigsten Produkte. Bitte als fertigen Absatz ohne Platzhalter.
   ```
   Typisch sind dann ein Absatz mit Platzhaltern (das ist in Ordnung) oder ein Absatz mit erfundenen Angaben (Halluzination). Beides lässt sich gut auswerten.
3. **Der Hauptprompt aus Demo 3** (Urlaubsbeantragung bei [FIRMENNAME]) zeigt mit größerer Wahrscheinlichkeit den eigentlichen Effekt: Die KI liefert eine „typische“ Antwort, die so klingt, als wäre sie auf die eigene Firma zugeschnitten. Für die Fehler-Demo in Block 1 ist er die bessere Wahl.

## Lehren für die Auswertung

- „Die KI hat ehrlich ‚weiß ich nicht‘ gesagt. Das machen moderne Modelle bei klaren Faktenfragen zu Unbekanntem inzwischen oft.“
- „Aber: Woher wüsstet ihr, ob ein genannter Name gestimmt hätte? Prüfen müsst ihr trotzdem, etwa im Handelsregister oder im Impressum.“ Die Modelle nennen diese Prüfwege selbst. Das lässt sich gut aufgreifen.
- „Die KI kennt keine internen Informationen. Wenn sie mit unseren Abläufen arbeiten soll, müsst ihr ihr den Kontext geben, und zwar nur so, wie es die Daten-Ampel erlaubt.“
- Vergleich der Modelle: Alle sind ehrlich, aber unterschiedlich ausführlich. Opus warnt zusätzlich vor Namensverwechslungen. Das ist ein guter Hinweis darauf, warum Tools mit Websuche hier anders antworten können.
- Auch in korrekten Antworten können Nebeninfos leicht ungenau sein (Sonnet zu Gebühren beim Handelsregister). Kleine Lehre: „Auch die Hinweise zum Prüfen selbst kurz gegenprüfen.“

---

## Gesprächsprotokolle

### Modell: Claude Haiku

**Nutzer 1**

Wer ist der Geschäftsführer der Nordlicht Technik GmbH und welche Produkte hat sie?

**Assistent 1**

Zur Nordlicht Technik GmbH habe ich keine verlässlichen Informationen. Ich kann deshalb weder sagen, wer dort Geschäftsführer ist, noch welche Produkte das Unternehmen anbietet. Ich kenne kein Unternehmen mit diesem Namen, und ich habe keinen Zugriff auf das Internet oder auf Firmenregister.

So kommst du an die Informationen:
- **Handelsregister:** Die Geschäftsführung steht im Handelsregister, das über [www.handelsregister.de](https://www.handelsregister.de) kostenlos einsehbar ist.
- **Unternehmenswebsite:** Auf der Website findest du meist Impressum, Team und Produktübersicht.
- **Bundesanzeiger:** Jahresabschlüsse und Veröffentlichungen gibt es unter [www.bundesanzeiger.de](https://www.bundesanzeiger.de).

Wenn du mir Auszüge aus einer Website, dem Handelsregisterauszug oder einer Produktbroschüre schickst, kann ich sie für dich auswerten und zusammenfassen.

### Modell: Claude Sonnet

**Nutzer 1**

Wer ist der Geschäftsführer der Nordlicht Technik GmbH und welche Produkte hat sie?

**Assistent 1**

Dazu kann ich Ihnen leider keine verlässliche Auskunft geben. Unter dem Namen "Nordlicht Technik GmbH" ist mir kein eindeutig identifizierbares Unternehmen bekannt, und ich habe in diesem Chat keinen Internetzugang und keine angehängten Unterlagen, in denen ich nachsehen könnte. Ich möchte mir deshalb keinen Geschäftsführer und keine Produktliste ausdenken, denn das wären erfundene Angaben.

So kommen Sie schnell an belastbare Informationen:
- **Handelsregister** (handelsregister.de oder unternehmensregister.de): Dort steht, wer als Geschäftsführer eingetragen ist. Die Suche ist kostenlos, einzelne Abrufe von Dokumenten können kostenpflichtig sein.
- **Website des Unternehmens**: Das Impressum nennt die vertretungsberechtigten Personen. Die Produkte und Leistungen finden Sie meist unter "Produkte", "Leistungen" oder "Lösungen".
- **Weitere Quellen**: Wirtschaftsauskunfteien oder Branchenverzeichnisse, wenn Sie mehr Hintergrund brauchen.

Wenn Sie mir Text von der Website, aus einer Broschüre oder aus dem Handelsregisterauszug hier einfügen oder als Datei hochladen, fasse ich Ihnen gern die Produkte zusammen oder bereite die Informationen übersichtlich auf. Auch bei der Formulierung einer Anfrage an das Unternehmen helfe ich Ihnen gerne.

### Modell: Claude Opus

**Nutzer 1**

Wer ist der Geschäftsführer der Nordlicht Technik GmbH und welche Produkte hat sie?

**Assistent 1**

Zur „Nordlicht Technik GmbH“ habe ich keine verlässlichen Informationen. Ich kann weder den Geschäftsführer nennen noch sagen, welche Produkte die Firma anbietet. Wenn ich hier Namen oder Produkte aufzählen würde, wären sie sehr wahrscheinlich erfunden. Das möchte ich vermeiden.

Dafür gibt es mehrere mögliche Gründe:
- Es könnte sich um ein kleines oder regionales Unternehmen handeln, über das kaum öffentlich berichtet wird.
- Der Name „Nordlicht“ ist sehr verbreitet. Vermutlich gibt es mehrere Firmen mit ähnlichem Namen, die man leicht verwechselt.
- Ich habe keinen Internetzugang und kann deshalb nicht nachsehen, ob sich in letzter Zeit etwas geändert hat, zum Beispiel ein neuer Geschäftsführer.

So finden Sie die Angaben zuverlässig:
1. **Impressum auf der Website des Unternehmens:** Bei einer GmbH in Deutschland muss dort der Geschäftsführer stehen. Meist finden Sie auf der Website auch eine Übersicht der Produkte.
2. **Handelsregister (handelsregister.de) bzw. Unternehmensregister:** Dort stehen die offiziell eingetragenen Geschäftsführer, der Sitz und der Unternehmensgegenstand.
3. **Branchenverzeichnisse oder Business-Netzwerke** wie LinkedIn oder XING: Diese geben oft einen Überblick über Produkte und Ansprechpartner. Sie sind aber nicht immer aktuell.

Wenn Sie mir Material zur Firma geben, zum Beispiel den Text der Website, eine Broschüre oder einen Handelsregisterauszug, fasse ich Ihnen die wichtigsten Punkte gern zusammen. Ich kann Ihnen auch eine kurze Anfrage an das Unternehmen formulieren.
