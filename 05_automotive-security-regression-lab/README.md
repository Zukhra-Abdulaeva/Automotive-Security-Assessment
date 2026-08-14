Automotive Security Regression Lab
From Security Finding to Reproducible Automotive Security Tests

Dieses Projekt ist ein vollständig simuliertes Automotive‑Security‑Testlabor, das zeigt, wie Security-Findings in automatisierte Regression Tests überführt werden können.
Es ergänzt das Hauptprojekt Automotive-Security-Assessment um einen modernen, reproduzierbaren Security‑Engineering‑Workflow.

🎯 Ziele des Projekts
Dieses Lab demonstriert:

Entwicklung reproduzierbarer Automotive-Security-Tests

Automatisierte Testausführung mit pytest

Evidence-Erfassung & Dokumentation

Threat Modeling & Security-Testmethodik

Engineering-Prozess:
Finding → Root Cause → Fix → Retest → Regression Test

Die ECU ist vollständig simuliert, sodass das Projekt öffentlich gezeigt werden kann, ohne reale Fahrzeugdaten oder OEM-sensible Informationen.

📁 Projektstruktur
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

Security-Testfälle
TC‑001 – Diagnostic Authorization
Zeigt den klassischen Security-Engineering-Prozess:
Security Requirement → Angriffshypothese → Test → Evidence → Regression.

TC‑002 – Message Validation
Robustheitstests & Input Validation gegen fehlerhafte oder manipulierte Nachrichten.

TC‑003 – Regression Workflow
Der vollständige Lifecycle eines Findings:

Finding → Root Cause → Fix → Retest → Regression Test

Dieser Case ist besonders relevant für Automotive-Security-Teams, da er zeigt, wie Findings langfristig abgesichert werden.

🔧 Technische Komponenten
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

⚙️ Automatisierung mit GitHub Actions
Die Pipeline security-regression.yml führt bei jedem Commit:

Setup der Python-Umgebung

Ausführung aller Regression Tests

Upload der Evidence-Artefakte

Damit wird jeder Fix automatisch validiert.

📄 Beispiel-Finding
Im Ordner examples/ befindet sich ein vollständiges Beispiel-Finding:

SEC‑001

Risikoanalyse

Root Cause

Exploitability

Fix

Retest

Regression Test

Dieses Finding ist vollständig reproduzierbar und automatisiert.

🧩 Warum dieses Projekt wichtig ist
Das Regression Lab zeigt einen modernen Automotive-Security-Workflow:

White‑Box Analyse

Threat Modeling

Security Testing

Evidence-Erfassung

eschreibung des Diagramms (für dein README oder architecture.md)
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
