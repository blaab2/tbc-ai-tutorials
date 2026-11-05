# Testlauf: Demo 6 – Unterschiedliche Antworten auf dieselbe Frage (Produktname)

**Herkunft:** [Demo: Typische KI-Schwächen live zeigen – Demo 6](../07_Beispielmaterial/demo_fehler_zeigen.md#demo-6-unterschiedliche-antworten-auf-dieselbe-frage) (Hauptprompt, ohne die Fakten-Zusatzvariante DIN 476) · Lösungshinweise: [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md) (enthalten **keinen** Abschnitt zu Demo 6)

> **Hinweis:** Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Testaufbau:** Jedes Modell hat den Prompt **einmal** in einem neuen Chat erhalten. Ein echter Wiederholungslauf desselben Modells (zweiter Chat bzw. „Antwort neu erzeugen“) liegt nicht vor. Der Vergleich unten ist daher ein Vergleich **zwischen drei Modellen**, nicht zwischen zwei Läufen desselben Modells – genau das, was die Demo eigentlich zeigen will, ist damit nur näherungsweise belegt.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Genau ein Name | ja („Armora“) | ja („TerraGuard“) | ja („TerraShield“) |
| Genau ein Satz Begründung | ja | ja (langer Satz) | ja (langer Satz) |
| Begründung inhaltlich passend (robust, außen) | ja | ja | ja |
| Sachlich korrekt | weitgehend (Latein-Herleitung ungenau, s. u.) | ja | ja |
| Name unterscheidet sich von den anderen | ja | ja, aber sehr ähnlich zu Opus | ja, aber sehr ähnlich zu Sonnet |
| Demo-Effekt „andere Antwort“ sichtbar | – (nur ein Lauf) | – (nur ein Lauf) | – (nur ein Lauf) |

**Gesamt:** Das Format wird von allen drei Modellen sauber eingehalten. Die drei Namen sind verschieden – das objektive Kriterium „die Namen unterscheiden sich“ ist modellübergreifend erfüllt. Auffällig: Sonnet und Opus landen beim **gleichen Baumuster** („Terra“ + englisches Schutzwort, fast identische Begründung). Die Varianz ist also eher „Variation über ein Thema“ als „völlig neue Idee“.

---

## Gefundene Fehler mit Beleg

1. **Haiku – ungenaue Wortherleitung.** Haiku schreibt: *„Der Name leitet sich vom lateinischen ‚arma‘ (Rüstung, Schutz) ab“*. Lateinisch *arma* bedeutet in erster Linie „Waffen, Kriegsgerät“ (umfasst zwar auch Schutzwaffen wie Schild/Rüstung, aber „Schutz“ ist keine Grundbedeutung); „Rüstung“ wäre eher *armatura*. Kein grober Fehler, aber ein schönes Beispiel dafür, dass auch kreative Antworten kleine, selbstbewusst formulierte Sachbehauptungen enthalten. Quelle: allgemeines Lateinwörterbuch (z. B. Stowasser/PONS: *arma, -orum* = „Waffen, Gerät“).
2. **Keine erfundenen Fakten bei Sonnet und Opus.** „Terra“ = Erde, „Guard“ = Wache/Schutz, „Shield“ = Schild – korrekt.
3. **Nicht geprüft (und von keinem Modell erwähnt):** Ob „Armora“, „TerraGuard“ oder „TerraShield“ als Marke bereits belegt ist. Ohne Internetzugang kann das Modell das nicht wissen – und es weist auch nicht darauf hin. Für die Praxis wichtig: Namensvorschläge vor Verwendung markenrechtlich prüfen.
4. **Keine Rechenwerte vorhanden** – es gab nichts nachzurechnen.

---

## Lehren für die Auswertung

- **Die Demo funktioniert grundsätzlich**, der Effekt ist aber schwächer als erhofft: Namen unterscheiden sich, ähneln sich aber oft (zwei von drei Modellen: „Terra…“). Bei demselben Modell zweimal hintereinander ist es durchaus möglich, dass derselbe oder ein fast gleicher Name erscheint. Darum **vorher mit dem echten [KI-TOOL] zweimal testen** und ggf. einen Screenshot zweier verschiedener Antworten als Backup bereithalten.
- **Gute Pointe für Teilnehmende:** „Die KI ist kreativ – aber berechenbarer, als man denkt.“ Wenn zwei Läufe ähnliche Namen liefern, ist das selbst eine Lehre: Für echte Vielfalt lieber **in einem Prompt 10 unterschiedliche Vorschläge** anfordern (ggf. mit Vorgabe „unterschiedliche Stilrichtungen: deutsch, lateinisch, technisch, verspielt“), statt nur auf Zufall zu hoffen.
- **Auch kreative Antworten enthalten Behauptungen** (Haikus „arma = Rüstung, Schutz“). Brücke zur Fakten-Zusatzvariante (DIN 476): Begründungen ebenfalls kurz prüfen.
- **Praxisbezug:** Kein Modell hat auf Markenrecht oder bestehende Produktnamen hingewiesen – das bleibt Aufgabe des Menschen.
- **Zeit:** Zweimal fragen und vergleichen dauert real 1–2 Minuten – passt gut in Block 2.

### Alternativer, robusterer Prompt (Vorschlag)

Für einen sicher sichtbaren Effekt in einem Chat:
```
Schlage mir 5 sehr unterschiedliche Namen für eine neue Produktlinie von robusten Steuergehäusen für den Außeneinsatz vor – je einen deutschen, einen lateinischen, einen englischen, einen verspielten und einen sachlich-technischen. Je ein Satz Begründung.
```
Danach den Originalprompt zweimal stellen und zeigen: Einzelanfragen liefern oft Varianten desselben Musters, gezielte Vielfalt bekommt man durch die Anweisung.

---

## Gesprächsprotokolle

### Modell: Claude Haiku

**Nutzer 1**

Schlage mir einen Namen für eine neue Produktlinie von robusten Steuergehäusen für den Außeneinsatz vor. Nur einen Namen, mit einem Satz Begründung.

**Assistent 1**

**Armora**

Der Name leitet sich vom lateinischen „arma“ (Rüstung, Schutz) ab und vermittelt sofort, dass die Gehäuse zuverlässig gegen Wind, Regen und Witterung schützen.

### Modell: Claude Sonnet

**Nutzer 1**

Schlage mir einen Namen für eine neue Produktlinie von robusten Steuergehäusen für den Außeneinsatz vor. Nur einen Namen, mit einem Satz Begründung.

**Assistent 1**

**TerraGuard**

Der Name verbindet „Terra" (Erde, Außenbereich) mit „Guard" (Schutz) und vermittelt damit auf einen Blick, dass die Gehäuse die empfindliche Steuerungstechnik zuverlässig gegen Wetter, Staub und raue Einsatzbedingungen abschirmen.

### Modell: Claude Opus

**Nutzer 1**

Schlage mir einen Namen für eine neue Produktlinie von robusten Steuergehäusen für den Außeneinsatz vor. Nur einen Namen, mit einem Satz Begründung.

**Assistent 1**

**TerraShield**

Der Name verbindet „Terra“ (Erde, Gelände, Außeneinsatz) mit „Shield“ (Schutzschild) und sagt damit sofort, dass die Gehäuse die Steuerungstechnik zuverlässig vor Wetter, Staub und rauen Umgebungsbedingungen schützen.

---

Zurück zur [Demo-Sammlung](../07_Beispielmaterial/demo_fehler_zeigen.md) · [Trainer-Lösungshinweise](../06_Uebungen/Trainer-Loesungshinweise.md)
