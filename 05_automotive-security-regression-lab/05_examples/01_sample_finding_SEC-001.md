# SEC-001 – Invalid Message Handling Vulnerability
*Automotive Security Regression Lab – Beispiel-Finding*

---

## 1. Summary
Die simulierte ECU akzeptierte zuvor ungültige Nachrichten mit negativen Werten.  
Dies führte zu unerwartetem Verhalten und stellte ein Robustheitsproblem dar.

---

## 2. Affected Component
- `ECUSimulator.validate_message()`

---

## 3. Severity
**Medium**  
Ungültige Nachrichten können zu unerwartetem Verhalten führen, jedoch nicht zu privilegierten Aktionen.

---

## 4. Description
Die ECU validierte eingehende Nachrichten nicht korrekt.  
Negative Werte wurden nicht abgelehnt, obwohl sie außerhalb des zulässigen Bereichs liegen.

Beispiel:
```json
{"value": -1}
Erwartetes Verhalten:

Ablehnung der Nachricht

Tatsächliches Verhalten:

Nachricht wurde akzeptiert

---

## 5. Root Cause
Die ursprüngliche Implementierung prüfte nur den oberen Grenzwert, nicht jedoch den unteren.

Fehlerhafte Logik:

python
if payload["value"] > 100:
    return {"response": "OutOfRange"}

---

## 6. Fix
Die Validierungslogik wurde korrigiert:

python
if not (0 <= payload["value"] <= 100):
    return {"response": "OutOfRange"}

---

7. Retest
Nach dem Fix wurde der ursprüngliche Angriff erneut ausgeführt.

Ergebnis:

ECU lehnt negative Werte korrekt ab

Verhalten entspricht dem Security Requirement SR‑002

---

## 8. Regression Test
Der Regression Test TC‑003 stellt sicher, dass der Fix dauerhaft wirkt.

Ergebnis:

PASS

Keine Regression festgestellt

Evidence bestätigt konsistentes Verhalten

---

## 9. Evidence
Evidence wird automatisch durch test_runner.py erzeugt und enthält:

Input: {"value": -1}

Output: {"response": "OutOfRange"}

Expected: ECU should reject invalid values after fix

Actual: Fix validated, ECU rejects invalid values

Result: PASS

---

## 10. Status
Closed – Fix validated and regression-secured

---
