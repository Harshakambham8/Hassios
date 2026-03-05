def parse_intent(text):
    text = text.lower()

    if "log" in text and "hour" in text:
        parts = text.split()
        try:
            hours = float([p for p in parts if p.replace('.', '', 1).isdigit()][0])
        except:
            return None

        return {
            "intent": "log_work",
            "project": "general",
            "hours": hours
        }

    return None
