"""
Demo-Skript für das Automotive Security Regression Lab.
Führt alle drei Security-Testfälle aus und zeigt Evidence im Terminal.
"""

from src.security_lab.test_runner import TestRunner

def print_evidence(evidence):
    print("=" * 60)
    print(f"Test ID: {evidence.data['test_id']}")
    print(f"Result : {evidence.data['result']}")
    print("Evidence:")
    print(evidence.to_json())
    print("=" * 60)
    print()

def main():
    runner = TestRunner()

    print("\nRunning Automotive Security Regression Lab Demo...\n")

    # TC-001
    ev1 = runner.run_tc001()
    print_evidence(ev1)

    # TC-002
    ev2 = runner.run_tc002()
    print_evidence(ev2)

    # TC-003
    ev3 = runner.run_tc003()
    print_evidence(ev3)

    print("Demo completed.\n")

if __name__ == "__main__":
    main()
