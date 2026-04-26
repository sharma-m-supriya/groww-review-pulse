import streamlit as st
import pandas as pd

# ---------------- PAGE ---------------- #
st.set_page_config(page_title="Groww Review Pulse", layout="centered")

st.title("📊 Weekly Review Pulse — Groww")
st.write("Understand what users are saying in the last few weeks")

# ---------------- LOAD DATA ---------------- #
df = pd.read_csv("reviews.csv")

# ---------------- THEME LOGIC ---------------- #
def get_theme(text):
    text = text.lower()

    if "kyc" in text:
        return "KYC"
    elif "login" in text or "crash" in text or "bug" in text:
        return "App Issues"
    elif "payment" in text or "upi" in text:
        return "Payments"
    elif "withdraw" in text:
        return "Withdrawals"
    elif "slow" in text or "loading" in text:
        return "Performance"
    else:
        return "General"

df["theme"] = df["review"].apply(get_theme)

# ---------------- TOP THEMES ---------------- #
top_themes = df["theme"].value_counts().head(3)

# ---------------- QUOTES ---------------- #
quotes = []
for theme in top_themes.index:
    sample = df[df["theme"] == theme]["review"].iloc[0]
    quotes.append(sample)

# ---------------- ACTION IDEAS ---------------- #
actions = [
    "Improve app stability and fix crashes during login and usage",
    "Simplify KYC process and reduce verification failures",
    "Fix payment and withdrawal delays to improve reliability"
]

# ---------------- DISPLAY ---------------- #
st.subheader("🔥 Top Themes")
for i, theme in enumerate(top_themes.index, 1):
    st.write(f"{i}. {theme}")

st.subheader("💬 User Quotes")
for q in quotes:
    st.write(f"- {q}")

st.subheader("🚀 Action Ideas")
for a in actions:
    st.write(f"- {a}")

# ---------------- EMAIL ---------------- #
email = f"""
Subject: Weekly Review Pulse - Groww

Hi,

Here is this week’s summary:

Top Themes:
{top_themes.to_string()}

User Quotes:
- {quotes[0]}
- {quotes[1]}
- {quotes[2]}

Action Ideas:
- {actions[0]}
- {actions[1]}
- {actions[2]}

Thanks
"""

st.subheader("📧 Email Draft")
st.code(email)
