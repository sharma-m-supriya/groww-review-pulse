# Groww Weekly Review Pulse

This is a simple Streamlit app that converts recent user reviews into a weekly summary.
It helps understand what users are saying and what needs to be improved.

---

## What this app does

* Reads recent app reviews from a CSV file
* Groups them into themes (max 5)
* Shows:

  * Top 3 themes
  * 3 user quotes
  * 3 action ideas
* Generates a short weekly note
* Creates a draft email with the summary

---

## Project Structure

```
groww-review-pulse/
│
├── app.py
├── reviews.csv
├── requirements.txt
├── README.md
└── .streamlit/
    └── config.toml
```

---

## How to run

1. Clone the repo

```
git clone https://github.com/your-username/groww-review-pulse.git
cd groww-review-pulse
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the app

```
streamlit run app.py
```

---

## Input format (reviews.csv)

The CSV file should have this format:

```
date,rating,title,review
```

Example:

```
2026-03-01,2,Login issue,App keeps crashing during login
```

---

## How to re-run for a new week

1. Replace the `reviews.csv` file with new reviews (last 8–12 weeks)
2. Keep the same column format
3. Save the file
4. Restart the app

The app will automatically generate a new weekly summary.

---

## Theme legend

The app groups reviews into these themes:

* **App Issues** → crashes, login problems, bugs
* **KYC** → verification failures, delays
* **Payments** → UPI issues, SIP failures
* **Withdrawals** → delays in getting money
* **Performance** → slow loading, lag

(Max 5 themes as required)

---

## Notes / Limitations

* Uses simple keyword-based grouping
* Works only on the provided CSV data
* No personal data (PII) is used

---

## Deployment

You can deploy this using Streamlit Community Cloud by connecting your GitHub repo and selecting `app.py`.

---

## Author

Supriya Sharma
