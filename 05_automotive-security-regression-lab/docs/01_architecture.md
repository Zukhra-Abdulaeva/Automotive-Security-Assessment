flowchart TD

    %% ============================
    %% SECTION: SYSTEM OVERVIEW
    %% ============================

    subgraph ECU["Simulierte ECU (ecu_simulator.py)"]
        ECU_Auth["Diagnostic Authorization Logic"]
        ECU_Validation["Message Validation Logic"]
    end

    subgraph Framework["Security Lab Framework (src/security_lab)"]
        TR["test_runner.py"]
        EV["evidence.py"]
    end

    subgraph TestCases["Security Test Cases (test_cases/)"]
        TC1["TC-001 Diagnostic Authorization"]
        TC2["TC-002 Message Validation"]
        TC3["TC-003 Regression Workflow"]
    end

    subgraph Pytest["Automated Tests (tests/)"]
        PT["pytest Regression Tests"]
    end

    subgraph CI["GitHub Actions (security-regression.yml)"]
        CI_Run["Automated Test Execution"]
        CI_Artifacts["Evidence Upload"]
    end

    subgraph Docs["Documentation (docs/)"]
        Arch["architecture.md"]
        Method["methodology.md"]
        EvidenceFmt["evidence-format.md"]
    end

    subgraph Examples["Examples (examples/)"]
        Demo["run_demo.py"]
        Finding["sample_finding_SEC-001.md"]
    end

    %% ============================
    %% SECTION: DATA FLOW
    %% ============================

    TC1 --> TR
    TC2 --> TR
    TC3 --> TR

    TR --> ECU
    TR --> EV

    PT --> TR
    PT --> EV

    CI_Run --> PT
    PT --> CI_Artifacts

    Finding --> TC3
    EvidenceFmt --> EV
    Method --> TC1
    Method --> TC2
    Method --> TC3
