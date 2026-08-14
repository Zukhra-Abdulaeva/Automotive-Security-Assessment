Automotive Security Regression Lab
From Security Finding to Reproducible Automotive Security Tests

Dieses Projekt ist ein vollständig simuliertes Automotive‑Security‑Testlabor, das zeigt, wie Security-Findings in automatisierte Regression Tests überführt werden können.
Es ergänzt das Hauptprojekt Automotive-Security-Assessment um einen modernen, reproduzierbaren Security‑Engineering‑Workflow.

## 🚗 Ziele des Projekts
Dieses Lab demonstriert:

Entwicklung reproduzierbarer Automotive-Security-Tests

Automatisierte Testausführung mit pytest

Evidence-Erfassung & Dokumentation

Threat Modeling & Security-Testmethodik

Engineering-Prozess:
Finding → Root Cause → Fix → Retest → Regression Test

Die ECU ist vollständig simuliert, sodass das Projekt öffentlich gezeigt werden kann, ohne reale Fahrzeugdaten oder OEM-sensible Informationen.

---

## 🔐 Was dieses Projekt bietet

### ✔️ Reproduzierbare Penetrationstests  
Jeder Angriff ist als Testfall definiert (`test_cases/`), inklusive Input, Expected Behavior und Evidence.

### ✔️ ECU‑Simulation  
Die Datei `ecu_simulator.py` simuliert sicherheitskritische Diagnosefunktionen (UDS).

### ✔️ Security Test Runner  
`test_runner.py` führt alle Security‑Testfälle automatisiert aus.

### ✔️ Evidence‑Format  
Alle Ergebnisse werden strukturiert dokumentiert (`docs/evidence-format.md`).

### ✔️ Regression Testing  
Fixes werden durch automatisierte Wiederholtests abgesichert (`tests/test_security_regression.py`).

### ✔️ CI/CD‑Integration  
GitHub Actions Workflow (`.github/workflows/security-regression.yml`) führt Security‑Tests bei jedem Commit aus.

---

## 📁 Projektstruktur
automotive-security-regression-lab/
├── README.md
├── pyproject.toml
│
├── docs/
│   ├── 01_architecture.md        → Systemarchitektur & Testflow
│   ├── 02_methodology.md         → Security-Testmethodik
│   └── 03_evidence-format.md     → Standardisiertes Evidence-Format
│
├── 01_threat_model/
│   └── 01_attack_surface.md      → Angriffsflächen & Threat Model
│
├── 02_test_cases/
│   ├── TC-001-diagnostic-authorization.md
│   ├── TC-002-message-validation.md
│   └── TC-003-regression-workflow.md
│
├── 03_src/
│   └── security_lab/
│       ├── __init__.py
│       ├── 01_ecu_simulator.py   → simulierte ECU
│       ├── 02_evidence.py        → Evidence-Datenmodell
│       └── 03_test_runner.py     → Testframework
│
├── 04_tests/
│   └── test_security_regression.py  → pytest Regression Tests
│
├── 05_examples/
│   ├── 00_run_demo.py               → Demo-Skript
│   └── 01_sample_finding_SEC-001.md → Beispiel-Finding
│   └── 02_sample_finding_SEC-002.md → Beispiel-Finding
│
└── .github/
    └── workflows/
        └── security-regression.yml → GitHub Actions CI

---

## 🧪 Security-Testfälle
TC‑001 – Diagnostic Authorization
Zeigt den klassischen Security-Engineering-Prozess:
Security Requirement → Angriffshypothese → Test → Evidence → Regression.

TC‑002 – Message Validation
Robustheitstests & Input Validation gegen fehlerhafte oder manipulierte Nachrichten.

TC‑003 – Regression Workflow
Der vollständige Lifecycle eines Findings:

Finding → Root Cause → Fix → Retest → Regression Test

Dieser Case ist besonders relevant für Automotive-Security-Teams, da er zeigt, wie Findings langfristig abgesichert werden.

---

## 🔧 Technische Komponenten
Simulierte ECU (ecu_simulator.py)
modelliert Diagnosefunktionen

simuliert Message-Validation

ermöglicht reproduzierbare Tests ohne Fahrzeughardware

Evidence-Modell (evidence.py)
standardisiertes Format für Security-Evidence

kompatibel mit Reports & CI

Test Runner (test_runner.py)
führt Security-Testcases aus

erzeugt Evidence

integriert mit pytest

pytest Regression Tests (tests/)
automatisierte Testausführung

reproduzierbare Ergebnisse

Integration in CI/CD

---

## ⚙️ Automatisierung mit GitHub Actions
Die Pipeline security-regression.yml führt bei jedem Commit:

Setup der Python-Umgebung

Ausführung aller Regression Tests

Upload der Evidence-Artefakte

Damit wird jeder Fix automatisch validiert.

## 📄 Beispiel-Finding
Im Ordner examples/ befindet sich ein vollständiges Beispiel-Finding:

SEC‑001

Risikoanalyse

Root Cause

Exploitability

Fix

Retest

Regression Test

Dieses Finding ist vollständig reproduzierbar und automatisiert.

## 🧩 Warum dieses Projekt wichtig ist
Das Regression Lab zeigt einen modernen Automotive-Security-Workflow:

White‑Box Analyse

Threat Modeling

Security Testing

Evidence-Erfassung

In Automotive‑ und IoT‑Systemen reicht es nicht, eine Schwachstelle einmal zu finden.  
Ein Angriff ist erst dann wirklich wertvoll, wenn er:

- reproduzierbar ist  
- validiert werden kann  
- nach einem Fix erneut getestet wird  
- und langfristig abgesichert ist  

Genau dafür wurde dieses Lab entwickelt.

Es verbindet klassische Automotive‑Engineering‑Erfahrung (ECUs, Diagnose, Bussysteme)  
mit moderner Cybersecurity (Penetration Testing, Threat Modeling, Regression).

---

## 🚀 Demo ausführen

```bash
python examples/run_demo.py

---

## 🚀 📄 Workplace‑Simulation – Automotive Security Regression Lab

Beschreibung des Diagramms
1. Simulierte ECU
Enthält Diagnose‑Autorisierung

Enthält Message‑Validation

Keine echten Fahrzeugdaten → sicher & öffentlich

2. Security Lab Framework
test_runner.py führt Testcases aus

evidence.py erzeugt standardisierte Evidence

3. Security Test Cases
TC‑001: Diagnostic Authorization

TC‑002: Message Validation

TC‑003: Finding → Fix → Retest → Regression

4. pytest Regression Tests
automatisierte Testausführung

reproduzierbare Ergebnisse

5. GitHub Actions
führt alle Regression Tests bei jedem Commit aus

speichert Evidence als Artefakte

6. Dokumentation
Architektur

Methodik

Evidence‑Format

7. Beispiele
Demo‑Skript

Beispiel‑Finding (SEC‑001)

Fix-Validierung

Regression Testing

Damit demonstriert es genau die Fähigkeiten, die Automotive-Security-Teams (OEMs, Tier‑1, Engineering-Dienstleister) suchen.

## 🚗🔐 Rolle im Automotive‑Security‑Team

1. Security Engineer
Entwickelt Angriffsszenarien

Leitet Threat Modeling

Führt Penetrationstests durch

Identifiziert Root Causes

Entwickelt reproduzierbare Security‑Testfälle

Validiert Fixes

Erstellt Findings & Evidence

Nutzen: Du bringst Struktur, Methodik und technische Tiefe in den Security‑Prozess.

2. Software Tester (Security‑Fokus)
Führt automatisierte Security‑Regression aus

Bewertet Testergebnisse

Meldet Abweichungen

Arbeitet eng mit Security Engineer zusammen

Nutzen: Stellt sicher, dass Fixes dauerhaft wirken.

3. Embedded Developer
Implementiert Fixes

Verbessert Security‑Mechanismen

Optimiert Diagnose‑ und Kommunikationslogik

Nutzen: Schließt die Lücke zwischen Security‑Analyse und Software‑Entwicklung.

4. System Architect
Definiert Trust Boundaries

Bewertet Kommunikationspfade

Entscheidet über Security‑Design

Nutzen: Sorgt dafür, dass Security nicht nur im Code, sondern im Systemdesign verankert ist.

5. Quality Engineer
Integriert Security‑Tests in CI/CD

Bewertet Stabilität und Reproduzierbarkeit

Dokumentiert Compliance (z. B. ISO/SAE 21434)

Nutzen: Macht Security zu einem kontinuierlichen Qualitätsprozess.

## 🛠️ 2. Tools & Infrastruktur
Technische Basis
Python (Test Runner, ECU‑Simulation)

pytest (Regression Testing)

GitHub Actions (CI/CD Security Pipeline)

Evidence‑Format (JSON‑basiert)

Threat Modeling (STRIDE, Attack Trees, TARA)

Automotive‑Spezifische Tools
CANoe / CANalyzer

python‑can

Wireshark

Scapy

Binwalk / Firmware‑Mod‑Kit

🔁 3. Ablaufdiagramm – End‑to‑End Security Workflow
Dieses Diagramm zeigt, wie dein Projekt in einem echten Workplace eingesetzt wird:
                ┌──────────────────────────┐
                │ 1. Scope Definition      │
                │ attack_surface.md        │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │ 2. Architekturverständnis │
                │ architecture.md           │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │ 3. Threat Modeling        │
                │ TARA, STRIDE, AttackTree  │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │ 4. Angriffsszenario       │
                │ test_cases/TC-001...      │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │ 5. Penetrationstest       │
                │ test_runner.py            │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │ 6. Evidence               │
                │ evidence-format.md        │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │ 7. Root Cause Analysis    │
                │ sample_finding_SEC-001.md │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │ 8. Fix Implementation     │
                │ ecu_simulator.py          │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │ 9. Retest                 │
                │ test_runner.py            │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │ 10. Regression Testing    │
                │ tests/test_security_reg.. │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │ 11. CI/CD Automation      │
                │ security-regression.yml   │
                └──────────────────────────┘

