class ECUSimulator:
    """
    Simulierte ECU für das Automotive Security Regression Lab.
    Enthält vereinfachte Diagnose- und Validierungslogik.
    Keine echte CAN-/UDS-Kommunikation.
    """

    def __init__(self):
        self.session = "default"
        self.security_unlocked = False

    # ---------------------------------------------------------
    # Diagnose: Session Control (simuliert)
    # ---------------------------------------------------------
    def request_session_control(self, subfunction):
        """
        Simuliert UDS Service 0x10 (Session Control).
        """
        if subfunction == 0x01:
            self.session = "default"
            return {"response": 0x50, "session": "default"}

        if subfunction == 0x03:
            if not self.security_unlocked:
                return {"response": 0x7F, "reason": "SecurityAccessDenied"}
            self.session = "extended"
            return {"response": 0x50, "session": "extended"}

        return {"response": 0x7F, "reason": "InvalidSubFunction"}

    # ---------------------------------------------------------
    # Security Access (simuliert)
    # ---------------------------------------------------------
    def request_security_access(self, seed):
        """
        Simulierte Security-Access-Logik.
        """
        if seed == "valid_seed":
            self.security_unlocked = True
            return {"response": "SecurityUnlocked"}
        return {"response": "SecurityDenied"}

    # ---------------------------------------------------------
    # Message Validation (Robustness)
    # ---------------------------------------------------------
    def validate_message(self, payload):
        """
        Validiert eingehende Nachrichten.
        """
        if not isinstance(payload, dict):
            return {"response": "InvalidFormat"}

        if "value" not in payload:
            return {"response": "MissingField"}

        if not (0 <= payload["value"] <= 100):
            return {"response": "OutOfRange"}

        return {"response": "Valid"}
