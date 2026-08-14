# SEC-002 – Unauthorized Diagnostic Session Elevation
*Automotive Security Regression Lab – Beispiel-Finding*

---

## 1. Summary
Die simulierte ECU erlaubte unter bestimmten Bedingungen einen Wechsel in die Extended Diagnostic Session, obwohl kein gültiger Security Access durchgeführt wurde.  
Dies stellt ein Risiko für unautorisierten Zugriff auf privilegierte Diagnosefunktionen dar.

---

## 2. Affected Component
- `ECUSimulator.request_session_control()`

---

## 3. Severity
**High**  
Ein unautorisierter Sessionwechsel kann sicherheitsrelevante Funktionen freischalten und ist daher kritisch.

---

## 4. Description
Die ECU besitzt eine vereinfachte Session-Control-Logik.  
Ein Angreifer sendet:

```json
{"service": "0x10", "subfunction": "0x03"}

Erwartetes Verhalten:

ECU muss den Wechsel in die Extended Session verweigern, wenn security_unlocked == False.

Tatsächliches Verhalten:

Unter bestimmten Bedingungen akzeptierte die ECU den Sessionwechsel trotzdem.

Dies ermöglicht potenziell unautorisierten Zugriff auf erweiterte Diagnosefunktionen.

---

## 5. Root Cause
Die ursprüngliche Logik prüfte die Security Access Bedingung nicht korrekt:

Fehlerhafte Logik:
if subfunction == 0x03:
    return {"response": 0x50, "session": "extended"}
Die Bedingung if not self.security_unlocked: fehlte.

---

## 6. Fix
Die Session-Control-Logik wurde korrigiert:
if subfunction == 0x03:
    if not self.security_unlocked:
        return {"response": 0x7F, "reason": "SecurityAccessDenied"}
    self.session = "extended"
    return {"response": 0x50, "session": "extended"}

---

## 7. Retest
Nach dem Fix wurde der Angriff erneut ausgeführt.

Ergebnis:

ECU verweigert den Sessionwechsel korrekt

Negative Response: SecurityAccessDenied

Verhalten entspricht dem Security Requirement SR‑001 und SR‑003

---

## 8. Regression Test
Der Regression Test TC‑001 deckt diesen Fall ab.

Ergebnis:

PASS

Kein unautorisierter Sessionwechsel möglich

Fix ist stabil und regressionsgesichert

---

## 9. Evidence
Evidence wird automatisch durch test_runner.py erzeugt und enthält:

Input: {"service": 0x10, "subfunction": 0x03}

Output: {"response": 0x7F, "reason": "SecurityAccessDenied"}

Expected: ECU must deny unauthorized session elevation

Actual: ECU denied session as expected

Result: PASS

---

## 10. Status
Closed – Fix validated and regression-secured

---
