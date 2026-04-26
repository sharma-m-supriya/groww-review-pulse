import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="Weekly Review Pulse", layout="centered")

# ---------------- UI STYLING ---------------- #
st.markdown("""
<style>

/* Background */
body {
    background-color: #F7F9FB;
}

/* Container width */
.block-container {
    padding-top: 2rem;
    max-width: 1100px;
}

/* Title */
.title {
    font-size: 36px;
    font-weight: 700;
    color: #1F2937;
    text-align: center;
    margin-bottom: 30px;
}

/* Section title */
.section-title {
    font-size: 20px;
    font-weight: 600;
    color: #374151;
    margin-top: 30px;
    margin-bottom: 15px;
}

/* Card */
.card {
    background: #FFFFFF;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #E5E7EB;
    text-align: center;
}

/* Card value */
.card-value {
    font-size: 24px;
    font-weight: 600;
    color: #111827;
}

/* Card label */
.card-label {
    font-size: 14px;
    color: #6B7280;
}

/* Quote */
.quote {
    background: #FFFFFF;
    padding: 16px;
    border-radius: 10px;
    border-left: 4px solid #00D09C;
    margin-bottom: 10px;
    color: #374151;
}

/* Action */
.action {
    background: #ECFDF5;
    padding: 16px;
    border-radius: 10px;
    border: 1px solid #D1FAE5;
    margin-bottom: 10px;
    color: #065F46;
}

/* Email */
.email {
    background: #111827;
    color: #F9FAFB;
    padding: 18px;
    border-radius: 10px;
    font-family: monospace;
    font-size: 13px;
    white-space: pre-wrap;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown('<div class="title">Weekly Review Pulse</div>', unsafe_allow_html=True)

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

# ---------------- ACTIONS ---------------- #
actions = [
    "Improve application stability and reduce crashes during login and usage",
    "Streamline KYC verification and reduce rejection rates",
    "Improve reliability of payments and withdrawals"
]

# ---------------- WEEKLY NOTE ---------------- #
note = f"""
Weekly Review Pulse

Top Themes:
1. {top_themes.index[0]}
2. {top_themes.index[1]}
3. {top_themes.index[2]}

User Feedback:
- {quotes[0]}
- {quotes[1]}
- {quotes[2]}

Recommended Actions:
- {actions[0]}
- {actions[1]}
- {actions[2]}
"""

# ---------------- EMAIL ---------------- #
email = f"""Subject: Weekly Review Pulse

Hi,

Here is this week's summary:

{note}

This is based on recent app store reviews.

Thanks
"""

# ---------------- DISPLAY ---------------- #

# Top Themes
st.markdown('<div class="section-title">Top Themes</div>', unsafe_allow_html=True)
cols = st.columns(3)

for i, theme in enumerate(top_themes.index):
    with cols[i]:
        st.markdown(f"""
        <div class="card">
            <div class="card-value">{top_themes[theme]}</div>
            <div class="card-label">{theme}</div>
        </div>
        """, unsafe_allow_html=True)

# Quotes
st.markdown('<div class="section-title">User Feedback</div>', unsafe_allow_html=True)
for q in quotes:
    st.markdown(f'<div class="quote">"{q}"</div>', unsafe_allow_html=True)

# Actions
st.markdown('<div class="section-title">Recommended Actions</div>', unsafe_allow_html=True)
for a in actions:
    st.markdown(f'<div class="action">{a}</div>', unsafe_allow_html=True)

# Email
st.markdown('<div class="section-title">Email Draft</div>', unsafe_allow_html=True)
st.markdown(f'<div class="email">{email}</div>', unsafe_allow_html=True)
