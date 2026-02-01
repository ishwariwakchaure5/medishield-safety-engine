def estimate_severity(prompt):

    p = prompt.lower()

    # ---------------- SEVERITY 5 ----------------
    if any(k in p for k in [
        "how many pills",
        "cause death",
        "lethal dose",
        "kill myself",
        "overdose",
        "suicide",
        "bleeding heavily",
        "not breathing",
        "heart attack",
        "stroke emergency"
    ]):
        return 5

    # ---------------- SEVERITY 4 ----------------
    if any(k in p for k in [
        "dosage",
        "dose mg",
        "take how many",
        "inject",
        "sleeping pills",
        "double my medicine",
        "self treat",
        "home remedy fracture",
        "cancer",
        "brain tumor"
    ]):
        return 4

    # ---------------- SEVERITY 3 ----------------
    if any(k in p for k in [
        "headache",
        "dizziness",
        "vomiting",
        "fever",
        "pain",
        "symptoms"
    ]):
        return 3

    # ---------------- DEFAULT ----------------
    return 2
