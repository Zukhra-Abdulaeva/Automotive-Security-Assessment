# TC-001 – Diagnostic Authorization
*Automotive Security Regression Lab*

## 1. Ziel des Testfalls
Dieser Testfall überprüft, ob die simulierte ECU unautorisierte Diagnoseanfragen korrekt ablehnt.  
Er bildet einen typischen Automotive-Security-Fall ab, bei dem privilegierte Diagnosefunktionen geschützt werden müssen.

---

## 2. Security Objective
Die ECU darf nur autorisierte Diagnosezugriffe akzeptieren.  
Unberechtigte Requests müssen zuverlässig abgelehnt werden.

---

## 3. Threat Scenario
Ein Angreifer sendet Diagnoseanfragen ohne gültige Autorisierung, um privilegierte Sessions zu aktivieren.

**Risiken:**
- Spoofing  
- Privilege Escalation  
- Manipulation sicherheitskritischer Funktionen  

---

## 4. Preconditions
- ECU befindet sich in der Default Session  
- Keine gültige Security Access Challenge wurde durchgeführt  
- Test Runner ist initialisiert  

---

## 5. Test Steps
1. Sende Diagnose-Service `0x10` (Session Control)  
2. Fordere Wechsel in eine privilegierte Session an  
3. Beobachte ECU-Reaktion  

---

## 6. Expected Result
Die ECU muss den Request ablehnen und eine negative Antwort zurückgeben.

Beispiel:
- Response: `0x7F`  
- Reason: `SecurityAccessDenied`  

---

## 7. Evidence
Evidence wird automatisch durch `evidence.py` erzeugt und enthält:
- Eingaben  
- ECU-Ausgaben  
- erwartetes Verhalten  
- tatsächliches Verhalten  
- PASS/FAIL  

---

## 8. Regression Criteria
Dieser Testfall ist Teil der Regression Suite.  
Er muss **immer** PASS sein, da ein Fix an der Autorisierungslogik niemals rückgängig werden darf.

---

## 9. Verknüpfte Requirements
- SR‑001 Diagnosezugriff muss autorisiert sein  
- SR‑003 Sessionwechsel muss kontrolliert sein  
