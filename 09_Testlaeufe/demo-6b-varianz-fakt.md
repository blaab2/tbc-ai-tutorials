# Testlauf: Demo 6 Zusatz – Faktenfrage zweimal stellen (DIN 476)

**Herkunft:** [Demo 6 – Zusatzvariante für Fakten](../07_Beispielmaterial/demo_fehler_zeigen.md#demo-6-unterschiedliche-antworten-auf-dieselbe-frage) im Material „Fehler zeigen“. In den [Trainer-Lösungshinweisen](../06_Uebungen/Trainer-Loesungshinweise.md) gibt es dazu keinen eigenen Abschnitt. Die einzige Lösungsangabe steht im Übungsblatt selbst („nach gängiger Darstellung 1922“) und in der Vorbereitungs-Checkliste („DIN-Jahr“).

**Prompt:**
```
In welchem Jahr wurde die Norm DIN 476 (Papierformate) erstmals veröffentlicht?
```

> Getestet mit Claude Haiku, Sonnet und Opus als Stellvertreter für [KI-TOOL] ohne Internetzugang – andere Tools/Versionen können abweichen.

**Einschränkung dieses Testlaufs:** Jedes Modell wurde nur **einmal** gefragt. Der Kern der Demo, also dieselbe Frage zweimal in getrennten Chats zu stellen und die Antworten zu vergleichen, wurde damit pro Modell nicht durchgespielt. Verglichen werden können nur die drei Modelle untereinander. Wenn man sie als „drei Versuche“ liest, waren alle drei Antworten gleich.

---

## Bewertung

| Kriterium | Haiku | Sonnet | Opus |
|---|---|---|---|
| Jahr genannt | 1922 | 1922 | 1922 |
| Stimmt mit 1922 überein | ja | ja | ja |
| Zusatzangaben | Porstmann, Ablösung durch ISO 216 / DIN EN ISO 216 | Porstmann, 1:√2, A0 = 1 m², ISO 216 (1975), Normenausschuss, Hinweis auf Beuth Verlag | genaues Datum 18.08.1922, Normenausschuss, Porstmann, 1:√2, A0 = 1 m², ISO 216 / DIN EN ISO 216 |
| Sachfehler | keiner im Kern, „abgelöst“ ist leicht verkürzt | keiner im Kern, „Beuth Verlag“ veraltet (heute DIN Media) | keiner erkennbar, Tagesdatum muss der Trainer selbst prüfen |
| Unsicherheit / Prüfhinweis | nein | ja (empfiehlt Prüfung, ohne Internetzugang) | nein |
| Abweichung zwischen den Antworten | nein | nein | nein |
| Zeigt die Demo das Warnsignal „widersprüchliche Antworten“? | nein | nein | nein |

**Gesamturteil:** Die Übung funktioniert **nur teilweise** wie gedacht. Die Frage wird von allen Modellen richtig und gleich beantwortet. Der Effekt, den die Demo zeigen soll (widersprüchliche Faktenantworten), tritt bei dieser bekannten, gut dokumentierten Tatsache sehr wahrscheinlich nicht auf.

---

## Gefundene Fehler mit Beleg

Es wurden **keine falschen Kernaussagen** gefunden. Alle drei nennen 1922, wie im Übungsblatt angegeben (Zeile 129: „nach gängiger Darstellung 1922“). Kleinere Punkte:

1. **Opus – genaues Datum „18. August 1922“:** Das Datum wird in gängigen Darstellungen (z. B. in Lexikonartikeln zum Papierformat) genannt und ist plausibel. Es steht aber nicht im Material. Das Modell sagt es ohne jede Einschränkung. Für die Demo ist das ein gutes Beispiel: Je genauer eine Angabe ist, desto wichtiger ist es, sie zu prüfen. Der Trainer sollte das Datum vorab nachschlagen, falls Teilnehmende danach fragen.
2. **Sonnet – „Beuth Verlag“:** Der Normenverlag heißt seit 2024 „DIN Media“. Das zeigt den Wissensstand des Modells, ist aber kein Sachfehler zur Frage.
3. **Sonnet – ISO 216 „(1975)“:** Die erste Ausgabe der ISO 216 stammt von 1975. Das ist korrekt. Die Bezeichnung „Deutscher Normenausschuss (damals noch Normenausschuss der deutschen Industrie)“ ist eine sinnvolle Vereinfachung, denn der Name „Deutscher Normenausschuss“ kam erst 1926.
4. **Haiku – „wurde ... durch ISO 216 bzw. DIN EN ISO 216 abgelöst“:** Das ist verkürzt. Die A-Reihe steht heute in DIN EN ISO 216, aber Teile der DIN 476 (z. B. Teil 2 für die C-Reihe) gibt es weiterhin. Für die Demo ist das unerheblich.

Nachgerechnet (Plausibilität der Zusatzangaben): Ein Blatt A0 mit 841 × 1189 mm hat 0,99995 m² ≈ 1 m², und 1189 / 841 ≈ 1,414 ≈ √2. Die Angaben „A0 = 1 m²“ und „1 : √2“ stimmen also.

---

## Lehren für die Auswertung

- **Die Demo zeigt hier eher das Gegenteil:** Bei einer bekannten Tatsache antworten die Modelle stabil und richtig. Das ist auch eine wichtige Lehre: Abweichungen sind ein Warnsignal, aber **gleiche Antworten beweisen nicht, dass etwas stimmt**. Ein Modell kann auch zweimal denselben Fehler machen.
- **Sicher klingend ist nicht gleich geprüft:** Opus nennt sogar den Tag (18. August 1922), ohne Einschränkung. Frage an die Gruppe: „Würdet ihr das Datum ungeprüft in ein Dokument schreiben?“
- **Gutes Verhalten hervorheben:** Sonnet weist selbst darauf hin, dass es ohne Internetzugang nicht jede Angabe garantieren kann, und empfiehlt eine Prüfung. Daran kann man zeigen, wie eine vorsichtige Antwort aussieht.
- **Zusatzwissen als Fehlerquelle:** Alle Modelle liefern mehr, als gefragt war (Porstmann, ISO 216, Verlag). Gerade in solchen Nebensätzen stecken oft kleine Ungenauigkeiten, hier z. B. der veraltete Verlagsname.
- **Merksatz bleibt gültig:** „Bei Fakten: nicht der KI glauben, sondern prüfen“. Hier gilt er sogar dann, wenn die Antwort richtig ist.

---

## Probleme im Material und Vorschläge

- **Effekt tritt wahrscheinlich nicht auf:** DIN 476 / 1922 ist ein sehr bekannter Fakt. Zwei Antworten werden fast immer übereinstimmen. Wenn der Trainer die Abweichung zeigen will, braucht er eine seltenere Faktenfrage, deren Antwort er vorher selbst sicher geprüft hat. Etwa eine Frage nach einer genauen Zahl oder einem Datum aus dem eigenen Fachgebiet, z. B. zu einer weniger bekannten Norm oder zum Gründungsjahr eines regionalen Unternehmens. Die Frage nach dem **genauen Datum** („An welchem Tag ...?“) erzeugt eher Unterschiede als die Frage nach dem Jahr.
- **Erwartung im Übungsblatt ergänzen:** Im Übungsblatt sollte stehen, dass beide Antworten wahrscheinlich gleich und richtig sind, und welche Lehre der Trainer dann zieht (siehe oben).
- **Lösungshinweise fehlen:** In den Trainer-Lösungshinweisen gibt es keinen Abschnitt zu Demo 6. Ein kurzer Eintrag mit „1922 (18. August 1922)“ und der erwarteten Reaktion wäre hilfreich.

---

## Gesprächsprotokolle

### Haiku

**Nutzer 1**

In welchem Jahr wurde die Norm DIN 476 (Papierformate) erstmals veröffentlicht?

**Assistent 1**

Die Norm DIN 476 wurde im Jahr 1922 erstmals veröffentlicht. Sie geht auf das von Walter Porstmann entwickelte System zurück, das die Grundlage der A-Formate bildet. Die Norm wurde später durch die internationale Norm ISO 216 bzw. DIN EN ISO 216 abgelöst.

### Sonnet

**Nutzer 1**

In welchem Jahr wurde die Norm DIN 476 (Papierformate) erstmals veröffentlicht?

**Assistent 1**

DIN 476 (Papierformate, A-Reihe) wurde erstmals **1922** veröffentlicht. Sie geht auf den Berliner Ingenieur Walter Porstmann zurück, der das Format-System auf Basis des Seitenverhältnisses 1:√2 und der Fläche von 1 m² (A0) entwickelte. Die Norm hieß zunächst DIN 476 und wurde später international als ISO 216 übernommen (1975).

Kurz zur Einordnung: Das System wurde 1922 vom Deutschen Normenausschuss (damals noch "Normenausschuss der deutschen Industrie") als Norm veröffentlicht. Falls Sie das Datum für ein offizielles Dokument oder eine Quellenangabe brauchen, empfehle ich, es kurz im aktuellen Normenverzeichnis (z. B. beim Beuth Verlag) zu prüfen, da ich ohne Internetzugang nicht jede Detailangabe garantieren kann.

### Opus

**Nutzer 1**

In welchem Jahr wurde die Norm DIN 476 (Papierformate) erstmals veröffentlicht?

**Assistent 1**

Die DIN 476 erschien erstmals **1922**, und zwar am 18. August 1922. Herausgeber war der damalige Normenausschuss der Deutschen Industrie, aus dem später das Deutsche Institut für Normung (DIN) wurde.

Die Norm geht vor allem auf den Ingenieur **Walter Porstmann** zurück. Sie legte die bekannten Papierformate der A-Reihe fest (A0, A1, … A4 usw.). Dabei gelten zwei Grundsätze:
- Die Seiten stehen im Verhältnis 1 : √2 zueinander. Halbiert man ein Blatt, bleibt dieses Seitenverhältnis also gleich.
- A0 hat eine Fläche von genau 1 m².

Später wurde das System international übernommen, heute als **ISO 216**. In Deutschland gilt dafür inzwischen die DIN EN ISO 216.

---

[Zurück zum Übungsblatt](../07_Beispielmaterial/demo_fehler_zeigen.md)
