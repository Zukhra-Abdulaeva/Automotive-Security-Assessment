# Evidence Format
*Automotive Security Regression Lab*

Dieses Dokument definiert das standardisierte Evidence-Format, das im Security Regression Lab verwendet wird.  
Evidence dient der reproduzierbaren Dokumentation von Testergebnissen und ist integraler Bestandteil des Regression-Workflows.

---

## 1. Ziele des Evidence-Formats

- Reproduzierbarkeit von Security-Tests
- Nachvollziehbarkeit von Findings
- Automatisierte Auswertung
- Integration in CI/CD
- Einheitliche Struktur für Reports

---

## 2. Evidence-Datenmodell

Evidence wird als Python-Datenstruktur erzeugt und kann in JSON exportiert werden.

### 2.1 Felder

| Feld | Beschreibung |
|------|--------------|
| `test_id` | ID des Testfalls (z. B. TC‑001) |
| `timestamp` | Zeitpunkt der Testausführung |
| `input` | Eingaben, die an die ECU gesendet wurden |
| `output` | Antworten der ECU |
| `result` | PASS / FAIL |
| `expected` | Erwartetes Verhalten |
| `actual` | Tatsächliches Verhalten |
| `notes` | Zusätzliche Beobachtungen |
| `finding_id` | Verknüpfung zu einem Finding (optional) |

---

## 3. Beispiel-Evidence (JSON)

```json
{
  "test_id": "TC-001",
  "timestamp": "2026-08-14T17:32:10Z",
  "input": {
    "service": "0x10",
    "subfunction": "0x03"
  },
  "output": {
    "response": "0x7F",
    "reason": "SecurityAccessDenied"
  },
  "expected": "ECU should deny unauthorized diagnostic session",
  "actual": "ECU denied session as expected",
  "result": "PASS",
  "notes": "Behavior consistent with security requirement"
}

---

## 4. Evidence-Erzeugung im Framework
Evidence wird automatisch erzeugt durch:

test_runner.py

evidence.py

Der Test Runner sammelt:

Eingaben

ECU-Ausgaben

Assertions

Metadaten

und übergibt sie an das Evidence-Modell.

---

## 5. Evidence in Regression Tests
Evidence wird in Regression Tests verwendet, um:

Fixes zu validieren

Abweichungen zu erkennen

Ergebnisse über CI zu speichern

GitHub Actions lädt Evidence als Artefakt hoch.

---

## 6. Evidence in Findings
Ein Finding enthält:

Evidence des ursprünglichen Fehlers

Evidence des Retests

Evidence des Regression Tests

Damit ist der gesamte Lifecycle dokumentiert.

---

## 7. Zusammenfassung
Das Evidence-Format stellt sicher, dass alle Security-Tests:

nachvollziehbar

reproduzierbar

automatisiert

CI-kompatibel

sind und bildet die Grundlage für professionelle Automotive-Security-Regression.

---
