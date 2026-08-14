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
