# Attack Surface & Threat Model
*Automotive Security Regression Lab*

Dieses Dokument beschreibt die Angriffsflächen und das Threat Model der simulierten ECU im Automotive Security Regression Lab.  
Es bildet die Grundlage für die Security-Testfälle und die Regression-Tests.

---

# 1. Ziel des Threat Models

Das Threat Model dient dazu:

- sicherheitsrelevante Angriffsflächen der ECU zu identifizieren  
- mögliche Angriffsszenarien zu beschreiben  
- Security Requirements abzuleiten  
- Testfälle strukturiert zu begründen  
- Regression Tests auf reale Risiken auszurichten  

Da die ECU simuliert ist, basiert das Threat Model auf **typischen Automotive-Security-Risiken**, ohne reale Fahrzeugdaten oder OEM-spezifische Implementierungen.

---

# 2. Systemübersicht

Die simulierte ECU stellt folgende Funktionen bereit:

- Diagnosezugriff (UDS‑ähnliche Logik)
- Session Management (Default / Extended / Programming)
- Message Validation (Eingabevalidierung)
- Security Access (vereinfacht simuliert)

Diese Funktionen bilden die Angriffsfläche für Security-Tests.

---

# 3. Angriffsflächen

## 3.1 Diagnosekommunikation
Die ECU akzeptiert Diagnoseanfragen (simuliert):

- Service Requests  
- Subfunctions  
- Session Control  

**Risiko:**  
Manipulierte oder unautorisierte Diagnosezugriffe können sicherheitskritische Funktionen aktivieren.

---

## 3.2 Session Management
Die ECU wechselt zwischen Sessions:

- Default Session  
- Extended Session  
- Programming Session  

**Risiko:**  
Unberechtigter Wechsel in eine privilegierte Session kann sicherheitsrelevante Operationen ermöglichen.

---

## 3.3 Message Validation
Die ECU prüft eingehende Nachrichten:

- Format  
- Wertebereiche  
- Sequenzen  

**Risiko:**  
Fehlerhafte oder manipulierte Nachrichten können zu unerwartetem Verhalten führen.

---

## 3.4 Security Access (simuliert)
Die ECU besitzt eine vereinfachte Security-Access-Logik.

**Risiko:**  
Fehlerhafte Implementierungen können unautorisierten Zugriff ermöglichen.

---

# 4. Bedrohungsanalyse (STRIDE)

| Kategorie | Beispielbedrohung | Relevanz |
|----------|-------------------|----------|
| **S – Spoofing** | Unautorisierter Diagnosezugriff | Hoch |
| **T – Tampering** | Manipulierte Nachrichten | Hoch |
| **R – Repudiation** | Fehlende Evidence | Mittel |
| **I – Information Disclosure** | Leaks über Diagnoseantworten | Niedrig |
| **D – Denial of Service** | Flooding / ungültige Requests | Mittel |
| **E – Elevation of Privilege** | Unberechtigter Sessionwechsel | Hoch |

---

# 5. Angriffsszenarien

## Szenario 1: Unautorisierter Diagnosezugriff
Ein Angreifer sendet Diagnoseanfragen ohne gültige Autorisierung.

**Ziel:**  
Privilegierte Funktionen aktivieren.

**Testfall:**  
TC‑001 Diagnostic Authorization

---

## Szenario 2: Manipulierte Nachrichten
Ein Angreifer sendet ungültige oder fehlerhafte Nachrichten.

**Ziel:**  
Robustheitsschwächen ausnutzen.

**Testfall:**  
TC‑002 Message Validation

---

## Szenario 3: Regression nach Fix
Ein zuvor gefundener Fehler wird behoben, aber könnte erneut auftreten.

**Ziel:**  
Sicherstellen, dass Fixes dauerhaft wirken.

**Testfall:**  
TC‑003 Regression Workflow

---

# 6. Security Requirements

| ID | Requirement | Begründung |
|----|-------------|------------|
| **SR‑001** | Diagnosezugriff muss autorisiert sein | Schutz vor Spoofing |
| **SR‑002** | Nachrichten müssen validiert werden | Schutz vor Tampering |
| **SR‑003** | Sessionwechsel muss kontrolliert sein | Schutz vor Privilege Escalation |
| **SR‑004** | Evidence muss erzeugt werden | Nachvollziehbarkeit |
| **SR‑005** | Fixes müssen regressionsgesichert sein | Langfristige Sicherheit |

---

# 7. Verbindung zu Testfällen

| Testfall | Abgedeckte Risiken | Angriffsfläche |
|----------|--------------------|----------------|
| **TC‑001** | Spoofing, Privilege Escalation | Diagnosezugriff |
| **TC‑002** | Tampering, DoS | Message Validation |
| **TC‑003** | Regression, Repudiation | alle relevanten Flächen |

---

# 8. Zusammenfassung

Dieses Threat Model bildet die Grundlage für die Security-Testfälle und Regression-Tests im Automotive Security Regression Lab.  
Es zeigt typische Automotive-Security-Risiken, ohne reale Fahrzeugdaten zu verwenden, und ermöglicht reproduzierbare, automatisierte Security-Tests.
