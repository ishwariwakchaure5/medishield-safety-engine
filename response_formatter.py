def format_response(action, ai_response):

    if action == "Block":
        return "❌ Request blocked. Please consult a certified doctor."

    if action == "Redirect":
        return "🚑 This may be an emergency. Seek immediate medical help."

    if action == "Warn":
        return f"⚠️ Medical caution:\n{ai_response}"

    return ai_response
