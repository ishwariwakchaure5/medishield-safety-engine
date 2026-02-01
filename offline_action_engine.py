from severity_engine import estimate_severity

def decide_action_offline(prompt, category):

    severity = estimate_severity(prompt)

    # ✅ Match dataset convention:
    # Severity->Action mapping

    if severity == 5:
        return "Block", severity

    if severity == 4:
        return "Warn", severity

    if severity == 3:
        return "Warn", severity

    if severity == 2:
        return "Safe", severity

    return "Safe", severity
