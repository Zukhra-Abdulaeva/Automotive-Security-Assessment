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
│   ├── architecture.md        → Systemarchitektur & Testflow
│   ├── methodology.md         → Security-Testmethodik
│   └── evidence-format.md     → Standardisiertes Evidence-Format
│
├── threat_model/
│   └── attack_surface.md      → Angriffsflächen & Threat Model
│
├── test_cases/
│   ├── TC-001-diagnostic-authorization.md
│   ├── TC-002-message-validation.md
│   └── TC-003-regression-workflow.md
│
├── src/
│   └── security_lab/
│       ├── __init__.py
│       ├── ecu_simulator.py   → simulierte ECU
│       ├── evidence.py        → Evidence-Datenmodell
│       └── test_runner.py     → Testframework
│
├── tests/
│   └── test_security_regression.py  → pytest Regression Tests
│
├── examples/
│   ├── run_demo.py               → Demo-Skript
│   └── sample_finding_SEC-001.md → Beispiel-Finding
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

Fix-Validierung

Regression Testing

Damit demonstriert es genau die Fähigkeiten, die Automotive-Security-Teams (OEMs, Tier‑1, Engineering-Dienstleister) suchen.
