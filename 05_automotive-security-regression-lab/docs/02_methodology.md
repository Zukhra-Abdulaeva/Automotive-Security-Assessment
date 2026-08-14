# Security Testing Methodology
*Automotive Security Regression Lab*

Dieses Dokument beschreibt die Security-Testmethodik, die im Automotive Security Regression Lab verwendet wird.  
Sie basiert auf etablierten Automotive-Security-Standards und kombiniert klassische Testverfahren mit modernen, reproduzierbaren Regression-Workflows.

---

## 1. Ziele der Methodik

Die Methodik verfolgt folgende Ziele:

- Identifikation sicherheitsrelevanter Schwachstellen
- Reproduzierbare Security-Tests
- Automatisierte Validierung von Fixes
- Dokumentation von Evidence
- Integration in CI/CD-Pipelines
- Abbildung eines vollständigen Security-Engineering-Lifecycles

---

## 2. Grundlagen

Die Methodik orientiert sich an:

- ISO/SAE 21434 (Road Vehicles – Cybersecurity Engineering)
- Automotive SPICE for Cybersecurity
- Best Practices aus OEM- und Tier‑1-Security-Teams
- Security Testing & Robustness Testing
- Threat Modeling (STRIDE, Attack Surface Analysis)

---

## 3. Testarten

### 3.1 Functional Security Tests
Prüfen sicherheitsrelevante Anforderungen wie:
- Diagnose-Autorisierung
- Zugriffskontrolle
- Kommunikationsvalidierung

### 3.2 Robustness & Input Validation Tests
Prüfen:
- fehlerhafte Nachrichten
- ungültige Parameter
- Grenzwerte
- unerwartete Sequenzen

### 3.3 Regression Tests
Werden nach einem Fix automatisiert ausgeführt:
- Validieren, dass der Fix wirkt
- Stellen sicher, dass keine neuen Schwachstellen entstehen
- Laufen automatisch über GitHub Actions

---

## 4. Testworkflow

Der Security-Testworkflow besteht aus:

1. **Requirement / Security Objective**  
   Definition der erwarteten Sicherheitsfunktion.

2. **Threat Model / Angriffshypothese**  
   Beschreibung möglicher Angriffe.

3. **Test Case Definition**  
   Strukturierter Testfall mit:
   - Preconditions  
   - Steps  
   - Expected Result  

4. **Execution**  
   Ausführung über das Python-Testframework.

5. **Evidence Collection**  
   Automatische Erzeugung von Evidence-Daten.

6. **Finding Creation**  
   Dokumentation eines reproduzierbaren Findings.

7. **Fix & Retest**  
   Validierung der Korrektur.

8. **Regression Test**  
   Automatisierte Absicherung über CI/CD.

---

## 5. Testfallstruktur

Ein Testfall folgt diesem Format:

- **ID**: TC-XXX  
- **Name**  
- **Security Objective**  
- **Threat Scenario**  
- **Test Steps**  
- **Expected Result**  
- **Evidence**  
- **Regression Criteria**

---

## 6. Automatisierung

### 6.1 Test Runner
Der Test Runner:
- führt Testcases aus  
- interagiert mit der simulierten ECU  
- erzeugt Evidence  

### 6.2 pytest
pytest übernimmt:
- Testausführung  
- Assertions  
- Integration in CI  

### 6.3 GitHub Actions
GitHub Actions:
- führt alle Regression Tests bei jedem Commit aus  
- speichert Evidence-Artefakte  

---

## 7. Vorteile der Methodik

- reproduzierbare Security-Tests  
- klare Dokumentation  
- automatisierte Regression  
- realistische Automotive-Security-Szenarien  
- sicher & öffentlich nutzbar (simulierte ECU)

---

## 8. Bezug zu den Testfällen

| Testfall | Fokus | Methode |
|---------|--------|---------|
| TC‑001 | Diagnostic Authorization | Functional Security Test |
| TC‑002 | Message Validation | Robustness Testing |
| TC‑003 | Regression Workflow | Full Security Lifecycle |

---

## 9. Zusammenfassung

Diese Methodik bildet einen vollständigen Automotive-Security-Engineering-Prozess ab und zeigt, wie Security-Findings reproduzierbar, automatisiert und langfristig abgesichert werden können.
