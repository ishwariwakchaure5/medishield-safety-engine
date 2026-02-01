from severity_engine import estimate_severity

def decide_action(prompt, category):

    severity = estimate_severity(prompt)

    if severity == 5:
        return "Block", severity

    if category == "Mental Health Safety":
        return "Redirect", severity

    if category == "Emergency Medical Advice":
        return "Redirect", severity

    if category == "Dangerous Prescriptions":
        return "Block", severity

    if severity >= 4:
        return "Warn", severity

    return "Safe", severity
