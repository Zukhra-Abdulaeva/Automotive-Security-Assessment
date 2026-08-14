# TC-003 – Regression Workflow
*Automotive Security Regression Lab*

## 1. Ziel des Testfalls
Dieser Testfall bildet den vollständigen Security-Engineering-Lifecycle ab:

**Finding → Root Cause → Fix → Retest → Regression Test**

Er zeigt, wie ein Security-Finding dauerhaft abgesichert wird.

---

## 2. Security Objective
Ein behobener Security-Fehler darf nie wieder auftreten.  
Regression Tests müssen sicherstellen, dass Fixes langfristig wirken.

---

## 3. Threat Scenario
Ein zuvor gefundener Fehler könnte durch Codeänderungen oder neue Funktionen unbeabsichtigt wieder auftreten.

**Risiken:**
- Regression  
- erneute Exploitability  
- fehlende Absicherung von Fixes  

---

## 4. Preconditions
- Ein Finding existiert (z. B. SEC‑001)  
- Fix wurde implementiert  
- Retest war erfolgreich  
- Regression Test ist definiert  

---

## 5. Test Steps
1. Reproduziere ursprünglichen Angriff  
2. Führe Fix-Validierung durch  
3. Führe Regression Test aus  
4. Vergleiche Evidence mit früheren Ergebnissen  

---

## 6. Expected Result
- ursprünglicher Fehler tritt nicht mehr auf  
- ECU verhält sich gemäß Fix  
- Regression Test zeigt PASS  
- Evidence bestätigt konsistentes Verhalten  

---

## 7. Evidence
Evidence enthält:
- ursprüngliches Fehlverhalten  
- Fix-Verhalten  
- Retest-Verhalten  
- Regression-Verhalten  
- PASS/FAIL  

---

## 8. Regression Criteria
Dieser Testfall ist **kritisch**:  
Er muss **immer** PASS sein, da er die langfristige Sicherheit eines behobenen Fehlers garantiert.

---

## 9. Verknüpfte Requirements
- SR‑004 Evidence muss erzeugt werden  
- SR‑005 Fixes müssen regressionsgesichert sein  
