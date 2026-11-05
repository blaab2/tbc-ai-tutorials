# Testlauf: Demo 4A – Große Zahlen multiplizieren ohne Rechenweg

**Herkunft:** Demo 4, Prompt A aus [demo_fehler_zeigen.md](../07_Beispielmaterial/demo_fehler_zeigen.md#demo-4-rechnen-und-zählen) (Einsatz in Block 1). Zugehörige Lösungshinweise: [Trainer-Loesungshinweise.md](../06_Uebungen/Trainer-Loesungshinweise.md) – dort gibt es **keinen eigenen Abschnitt** zu dieser Demo; die Lösung steht nur im Demo-Blatt selbst.

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Prompt:**
```
Was ist 48.763 × 9.217? Antworte nur mit der Zahl, ohne Rechenweg.
```

**Richtige Lösung:** 48.763 × 9.217 = **449.448.571** (mit `python3` nachgerechnet: `48763*9217 = 449448571`).

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Ziffernfolge korrekt (449448571) | ja | ja | ja |
| Als ganze Zahl im deutschen Format lesbar | **nein** – „449,448571“ liest sich als Dezimalzahl ≈ 449 | ja – 449.448.571 | ja – 449.448.571 |
| Nur die Zahl, ohne Rechenweg | ja | ja | ja |
| Gezeigter Fehler (falsche Ziffern) tritt auf | nein | nein | nein |
| Für die Demo brauchbar | ja, aber anders als geplant (Formatfehler) | nur als „richtig – trotzdem prüfen“ | nur als „richtig – trotzdem prüfen“ |

---

## Gefundene Fehler mit Beleg

1. **Haiku – Trennzeichen falsch, Größenordnung dadurch falsch.** Antwort: `449,448571`. Die Ziffern stimmen alle, aber im Deutschen ist das Komma das Dezimalzeichen. Gelesen ergibt das 449,448571 – also rund 449 statt rund 449 Millionen (Faktor 1.000.000 daneben). Es ist auch kein gültiges englisches Format (das wäre `449,448,571`).
   Auffällig: `48.763 × 9.217` mit Punkt als *Dezimalzeichen* gelesen (englische Schreibweise) ergibt genau `449.448571` (per `python3` geprüft). Haiku hat also vermutlich die Tausenderpunkte im Prompt als Dezimalpunkte verstanden und das Ergebnis dann mit deutschem Komma ausgegeben. Das ist eine echte Mehrdeutigkeit im Prompt, kein Ziffernfehler.
2. **Sonnet und Opus:** kein Fehler. Beide liefern exakt `449.448.571`.
3. **Erfundenes:** keins. Alle drei halten sich an „nur die Zahl“.

**Tritt der Demo-Fehler auf?** Nein – der eigentlich gezeigte Fehler (falsche Ziffern durch „Schätzen“) kam in keinem Modell vor. Die Multiplikation 5-stellig × 4-stellig ist für aktuelle Modelle offenbar zu leicht.

---

## Lehren für die Auswertung

- **„Richtig – aber woher wisst ihr das?“** Bei zwei von drei Modellen ist das die einzige mögliche Botschaft. Das Demo-Blatt sieht das vor („Auch ‚Die KI hat es richtig gemacht‘ ist eine gute Lehre“). Den Taschenrechner live daneben halten.
- **Der Haiku-Fall ist eigentlich die stärkere Lehre:** Eine Antwort kann aus den richtigen Ziffern bestehen und trotzdem um den Faktor eine Million danebenliegen – nur wegen Punkt und Komma. Das passiert im Alltag ständig (Excel-Import, englische Tools, CSV-Dateien). Merksatz-Ergänzung: „Nicht nur die Ziffern prüfen – auch Komma, Punkt und Einheit.“
- **Mehrdeutige Prompts:** „48.763“ ist im Deutschen 48 Tausend, im Englischen 48 Komma 763. Wer Zahlen an eine KI gibt, sollte eindeutig schreiben (z. B. `48763` ohne Trennzeichen).
- **Nicht verallgemeinern:** Dass das Ergebnis hier stimmt, heißt nicht, dass KI zuverlässig rechnet. Bei längeren Zahlen, Summen über viele Zeilen oder Prozentrechnung in Texten kommen Fehler weiterhin vor (vgl. Kontrollwert in Übung 3 der [Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md)).
- **Zeit:** Die Demo dauert unter einer Minute und passt gut in Block 1.

---

## Probleme im Material und Vorschläge

- **Der Fehler ist schlecht reproduzierbar.** Empfehlung: zusätzlich einen schwereren Prompt vorbereiten, z. B.
  ```
  Was ist 8437291 × 6958743? Antworte nur mit der Zahl, ohne Rechenweg.
  ```
  Richtige Lösung: **58.712.939.685.213** (per `python3` geprüft). Vorher im eigenen [KI-TOOL] testen – auch hier kann das Modell richtig liegen oder ein Rechenwerkzeug nutzen.
- **Satz in Zeile 91 von demo_fehler_zeigen.md passt nicht zum Prompt:** „Dann zeigst du: ‚Mit Rechenweg ist es richtig …‘“ – der Prompt verlangt aber ausdrücklich *ohne* Rechenweg, und die Modelle lagen auch ohne Rechenweg richtig. Vorschlag: „Dann zeigst du: ‚Diesmal stimmt es – aber prüfen müsst ihr wichtige Zahlen trotzdem.‘“
- **Punkt/Komma-Hinweis fehlt.** Vorschlag für die Lösungszeile: „(Richtige Lösung: **449.448.571** … Achtung: Manche Tools lesen die Punkte als Dezimalzeichen und antworten z. B. „449,448571“ – Ziffern richtig, Größenordnung falsch. Auch das ist eine gute Lehre.)“
- **Trainer-Loesungshinweise.md** enthält keinen Abschnitt zu den Block-1-Demos. Das ist vertretbar, weil die Lösung im Demo-Blatt steht – ggf. dort einen Verweis ergänzen.

---

## Gesprächsprotokolle

### Modell: Claude Haiku

**Nutzer 1:**
```
Was ist 48.763 × 9.217? Antworte nur mit der Zahl, ohne Rechenweg.
```

**Assistent 1:**
```
449,448571
```

### Modell: Claude Sonnet

**Nutzer 1:**
```
Was ist 48.763 × 9.217? Antworte nur mit der Zahl, ohne Rechenweg.
```

**Assistent 1:**
```
449.448.571
```

### Modell: Claude Opus

**Nutzer 1:**
```
Was ist 48.763 × 9.217? Antworte nur mit der Zahl, ohne Rechenweg.
```

**Assistent 1:**
```
449.448.571
```

---

Zurück zum Demo-Blatt: [demo_fehler_zeigen.md](../07_Beispielmaterial/demo_fehler_zeigen.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md)
