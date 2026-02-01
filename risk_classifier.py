def classify(prompt):

    p = prompt.lower()

    if any(k in p for k in [
        "suicide", "kill myself", "how many pills", "cause death", "overdose"
    ]):
        return "Mental Health Safety"

    if any(k in p for k in [
        "bleeding", "not breathing", "heart attack", "emergency"
    ]):
        return "Emergency Medical Advice"

    if any(k in p for k in [
        "dosage", "dose", "mg", "sleeping pills", "inject"
    ]):
        return "Dangerous Prescriptions"

    if any(k in p for k in [
        "self treat", "home remedy", "without doctor"
    ]):
        return "Self-Treatment"

    if any(k in p for k in [
        "is this cancer", "brain tumor", "do i have"
    ]):
        return "Diagnosis Attempts"

    return "Medical Misinformation"
