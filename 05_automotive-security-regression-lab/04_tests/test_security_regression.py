import pytest
from src.security_lab.test_runner import TestRunner

@pytest.fixture
def runner():
    """
    Initialisiert den TestRunner für alle Testfälle.
    """
    return TestRunner()


# ---------------------------------------------------------
# TC-001 Diagnostic Authorization
# ---------------------------------------------------------
def test_tc001_diagnostic_authorization(runner):
    evidence = runner.run_tc001()

    assert evidence.data["result"] == "PASS", (
        f"TC-001 failed:\n{evidence.to_json()}"
    )


# ---------------------------------------------------------
# TC-002 Message Validation
# ---------------------------------------------------------
def test_tc002_message_validation(runner):
    evidence = runner.run_tc002()

    assert evidence.data["result"] == "PASS", (
        f"TC-002 failed:\n{evidence.to_json()}"
    )


# ---------------------------------------------------------
# TC-003 Regression Workflow
# ---------------------------------------------------------
def test_tc003_regression_workflow(runner):
    evidence = runner.run_tc003()

    assert evidence.data["result"] == "PASS", (
        f"TC-003 failed:\n{evidence.to_json()}"
    )
