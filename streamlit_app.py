import streamlit as st

# Display a message based on hours required
def display_message(hours_required):
    if hours_required <= 0.5:
        return "A steal! This is barely a coffee break. ☕"
    elif hours_required <= 1:
        return "That’s like one Zoom meeting. Treat yourself."
    elif hours_required <= 2:
        return "Two hours of work? Think about it… but not too hard."
    elif hours_required <= 4:
        return "Half a workday. Do you love it or just like it?"
    elif hours_required <= 6:
        return "Getting into serious time-trade territory now."
    elif hours_required <= 8:
        return "That’s a full day of work. You better really want it."
    elif hours_required <= 12:
        return "Day and a half. Will Future You say ‘thanks’ or ‘yikes’?"
    elif hours_required <= 20:
        return "Multiple shifts… hope it’s worth the fatigue."
    elif hours_required <= 40:
        return "A full work week. You might want to sleep on it."
    elif hours_required <= 100:
        return "Serious lifestyle choice. Is this a one-time joy or a financial drain?"
    elif hours_required <= 1_000:
        return "That’s a month of work. Is this a laptop or a regrettable vacation?"
    elif hours_required <= 10_000:
        return "This is a long-term investment. Hope it earns interest in your soul."
    elif hours_required <= 100_000:
        return "This is generational labor. Your descendants better inherit it."
    else:
        return "🚫 Over 100,000 hours? Even eternity clocks out eventually..."

# App title
st.title("💸 Is It Worth It? Calculator")

# Currency selector
currency = st.selectbox("Choose your currency", ["$", "€", "£", "¥", "Other"])
if currency == "Other":
    currency = st.text_input("Enter your custom currency symbol")

# Input fields
item_cost = st.number_input(f"Enter the cost of the item ({currency})", min_value=0.0, format="%.2f")
hourly_wage = st.number_input(f"Enter your hourly wage ({currency})", min_value=0.01, value=15.00, format="%.2f")

# When button is clicked
if st.button("🧠 Calculate"):
    hours_required = item_cost / hourly_wage

    if hours_required > 100_000:
        st.warning(f"⚠️ This would cost you {hours_required:,.2f} hours of work.")
        st.error("🚫 Over 100,000 hours? Even eternity clocks out eventually... Maybe in the next life..")
    else:
        st.success(f"This will cost you approximately {hours_required:,.2f} hour(s) of work.")
        st.info(display_message(hours_required))

