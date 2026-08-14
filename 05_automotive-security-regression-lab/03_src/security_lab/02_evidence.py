import json
from datetime import datetime

class Evidence:
    """
    Standardisiertes Evidence-Modell für Security-Tests.
    """

    def __init__(self, test_id):
        self.data = {
            "test_id": test_id,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "input": None,
            "output": None,
            "expected": None,
            "actual": None,
            "result": None,
            "notes": None,
            "finding_id": None
        }

    def set_input(self, input_data):
        self.data["input"] = input_data

    def set_output(self, output_data):
        self.data["output"] = output_data

    def set_expected(self, expected):
        self.data["expected"] = expected

    def set_actual(self, actual):
        self.data["actual"] = actual

    def set_result(self, result):
        self.data["result"] = result

    def set_notes(self, notes):
        self.data["notes"] = notes

    def link_finding(self, finding_id):
        self.data["finding_id"] = finding_id

    def to_json(self):
        return json.dumps(self.data, indent=4)
