from .ecu_simulator import ECUSimulator
from .evidence import Evidence

class TestRunner:
    """
    Führt Security-Testfälle aus und erzeugt Evidence.
    """

    def __init__(self):
        self.ecu = ECUSimulator()

    # ---------------------------------------------------------
    # TC-001 Diagnostic Authorization
    # ---------------------------------------------------------
    def run_tc001(self):
        evidence = Evidence("TC-001")

        input_data = {"service": 0x10, "subfunction": 0x03}
        evidence.set_input(input_data)

        output = self.ecu.request_session_control(0x03)
        evidence.set_output(output)

        expected = "ECU should deny unauthorized diagnostic session"
        evidence.set_expected(expected)

        actual = (
            "ECU denied session as expected"
            if output.get("reason") == "SecurityAccessDenied"
            else "Unexpected behavior"
        )
        evidence.set_actual(actual)

        result = "PASS" if actual == "ECU denied session as expected" else "FAIL"
        evidence.set_result(result)

        return evidence

    # ---------------------------------------------------------
    # TC-002 Message Validation
    # ---------------------------------------------------------
    def run_tc002(self):
        evidence = Evidence("TC-002")

        input_data = {"value": 999}  # invalid
        evidence.set_input(input_data)

        output = self.ecu.validate_message(input_data)
        evidence.set_output(output)

        expected = "ECU should reject out-of-range values"
        evidence.set_expected(expected)

        actual = (
            "ECU rejected invalid message"
            if output.get("response") == "OutOfRange"
            else "Unexpected behavior"
        )
        evidence.set_actual(actual)

        result = "PASS" if actual == "ECU rejected invalid message" else "FAIL"
        evidence.set_result(result)

        return evidence

    # ---------------------------------------------------------
    # TC-003 Regression Workflow
    # ---------------------------------------------------------
    def run_tc003(self):
        evidence = Evidence("TC-003")
        evidence.link_finding("SEC-001")

        input_data = {"value": -1}  # original bug
        evidence.set_input(input_data)

        output = self.ecu.validate_message(input_data)
        evidence.set_output(output)

        expected = "ECU should reject invalid values after fix"
        evidence.set_expected(expected)

        actual = (
            "Fix validated, ECU rejects invalid values"
            if output.get("response") == "OutOfRange"
            else "Regression detected"
        )
        evidence.set_actual(actual)

        result = "PASS" if actual.startswith("Fix validated") else "FAIL"
        evidence.set_result(result)

        return evidence
