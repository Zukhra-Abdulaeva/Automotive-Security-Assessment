# SEC-XXX – [Kurzer Titel des Findings]
*Automotive Security Regression Lab – Security Finding Template*

---

## 1. Summary
Kurze Beschreibung des Problems in 2–3 Sätzen.  
Was ist passiert? Warum ist es relevant?

---

## 2. Affected Component
- [Name der betroffenen Funktion oder Datei]
- Beispiel: `ECUSimulator.validate_message()`

---

## 3. Severity
**Low / Medium / High / Critical**

Begründung:
- Warum ist das Finding wichtig?
- Welche Auswirkungen hätte ein Angriff?

---

## 4. Description
Detaillierte Beschreibung des Fehlers:

- Welche Eingabe führt zum Problem?
- Was ist das erwartete Verhalten?
- Was ist das tatsächliche Verhalten?

Beispiel-Input:
```json
{"value": -1}

---

## 5. Root Cause
Technische Ursache des Fehlers:

Welche Logik war falsch?

Warum konnte der Fehler auftreten?

Beispiel:

python
# Fehlerhafte Logik
if payload["value"] > 100:
    return {"response": "OutOfRange"}
---

## 6. Fix
Beschreibung der Korrektur:

Welche Logik wurde angepasst?

Warum funktioniert der Fix?

Beispiel:

python
# Korrigierte Logik
if not (0 <= payload["value"] <= 100):
    return {"response": "OutOfRange"}

---

## 7. Retest
Ergebnis des erneuten Tests nach dem Fix:

Wurde das ursprüngliche Fehlverhalten beseitigt?

Entspricht das Verhalten jetzt dem Security Requirement?

---

## 8. Regression Test
Welcher Regression Test deckt dieses Finding ab?

TC‑001 / TC‑002 / TC‑003 oder eigener Test

Ergebnis: PASS / FAIL

Evidence bestätigt konsistentes Verhalten

---

## 9. Evidence
Evidence aus dem Test Runner:

Input

Output

Expected

Actual

Result

Beispiel:

json
{
  "input": {"value": -1},
  "output": {"response": "OutOfRange"},
  "expected": "...",
  "actual": "...",
  "result": "PASS"
}

---

## 10. Status
Open / In Progress / Fixed / Retested / Regression-Secured / Closed

Datum
Verantwortlicher Engineer

---
