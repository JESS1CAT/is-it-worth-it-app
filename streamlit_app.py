import streamlit as st

# Display a message based on hours required
def display_message(hours_required):
    if 0 < hours_required <= 0.25:
        return "A steal! This is barely a coffee break. ☕"
    elif 0.25 < hours_required <= 1:
        return "That’s like one Zoom meeting. Treat yourself."
    elif 1 < hours_required <= 3:
        return "This is treat-yourself territory. Joy-per-hour must be high."
    elif 3 < hours_required <= 6:
        return "Getting into serious time-trade territory now. If it’s not useful or meaningful, it’s just clutter in disguise."
    elif 6 < hours_required <= 10:
        return "That’s a full day of work. You better really want it."
    elif 10 < hours_required <= 20:
        return "Multiple shifts… hope it’s worth the fatigue. Something else might have to wait."
    elif 20 < hours_required <= 30:
        return "That’s a big chunk of your week. If it doesn’t serve your future, it may be a passing fantasy."
    elif 30 < hours_required <= 38:
        return "You're skimming full-week energy. Is this solving a problem or scratching an itch?"
    elif 38 < hours_required <= 45:
        return "A full-time work week. This better upgrade your quality of life, not just your aesthetic."
    elif 45 < hours_required <= 80:
        return "Double shifts. Double takes. Double check your ‘why.’"
    elif 80 < hours_required <= 200:
        return "That’s a month of labor. Is it transformational—or just expensive?"
    elif 200 < hours_required <= 1_000:
        return "A saga-level spend. If it’s not sacred, it’s excessive. Legacy or liability?"
    elif 1_000 < hours_required <= 10_000:
        return "This should come with an oath, a velvet box, or a security deposit."
    elif 10_000 < hours_required <= 100_000:
        return "This better be passed down in your will, featured in a documentary, or orbiting Earth. 🚀"
    else:
        return "🚫 Over 100,000 hours? Even eternity clocks out eventually. Unless you’re buying the moon, take a breath
