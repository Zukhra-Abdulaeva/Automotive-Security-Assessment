# TC-002 – Message Validation
*Automotive Security Regression Lab*

## 1. Ziel des Testfalls
Dieser Testfall überprüft die Robustheit der ECU gegenüber ungültigen oder manipulierten Nachrichten.

---

## 2. Security Objective
Die ECU muss alle eingehenden Nachrichten validieren und ungültige Requests sicher ablehnen.

---

## 3. Threat Scenario
Ein Angreifer sendet:
- fehlerhafte Nachrichten  
- ungültige Parameter  
- Werte außerhalb definierter Bereiche  
- unerwartete Sequenzen  

**Risiken:**
- Tampering  
- Denial of Service  
- unerwartetes Verhalten  

---

## 4. Preconditions
- ECU läuft in Default Session  
- Test Runner ist initialisiert  

---

## 5. Test Steps
1. Sende Diagnose-Service mit ungültigem Subfunction  
2. Sende Nachricht mit ungültigen Parameterwerten  
3. Sende Nachricht mit falscher Sequenz  
4. Beobachte ECU-Reaktion  

---

## 6. Expected Result
Die ECU muss:
- alle ungültigen Nachrichten ablehnen  
- negative Responses zurückgeben  
- keine Session wechseln  
- keine privilegierten Funktionen aktivieren  

---

## 7. Evidence
Evidence enthält:
- Input Payload  
- Validierungsfehler  
- ECU-Antwort  
- PASS/FAIL  

---

## 8. Regression Criteria
Dieser Testfall ist Teil der Robustness Regression Suite.  
Er muss **immer** PASS sein, da Robustheit ein dauerhaftes Sicherheitsziel ist.

---

## 9. Verknüpfte Requirements
- SR‑002 Nachrichten müssen validiert werden  
- SR‑005 Fixes müssen regressionsgesichert sein  
