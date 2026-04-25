import streamlit as st
import re

st.set_page_config(page_title="PhishEye", layout="wide")

# -------- CSS --------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #00ff9f;
}

.stApp {
    background-color: #0e1117;
}

h1, h2, h3 {
    color: #00ff9f;
}

.stTextArea textarea {
    background-color: #1c1f26;
    color: white;
    border: 1px solid #00ff9f;
}

.stTextInput input {
    background-color: #1c1f26;
    color: white;
    border: 1px solid #00ff9f;
}

.stButton>button {
    background-color: #00ff9f;
    color: black;
    border-radius: 6px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("PhishEye")
st.write("Phishing Email Analyzer for Threat Detection")

# -------- INPUT --------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Email Content")

    email_body = st.text_area(
        "Paste email body",
        height=250,
        placeholder="Click here to verify your account..."
    )

with col2:
    st.subheader("Email Metadata")

    sender = st.text_input("Sender Email", placeholder="example@domain.com")
    subject = st.text_input("Subject", placeholder="Urgent: Verify your account")

analyze = st.button("Analyze Email")

# -------- ANALYSIS --------
if analyze and email_body:

    with st.spinner("Analyzing email... detecting phishing indicators..."):

        suspicious_keywords = ["urgent", "verify", "login", "password", "bank", "account", "click", "immediately"]
        keyword_hits = 0
        reasons = []

        for word in suspicious_keywords:
            if word in email_body.lower():
                keyword_hits += 1
                reasons.append(f"Keyword detected: {word}")

        # Links
        links = re.findall(r"https?://\S+", email_body)
        suspicious_links = []

        for link in links:
            if "@" in link or "login" in link or "verify" in link:
                suspicious_links.append(link)
                reasons.append(f"Suspicious link: {link}")

        # Sender
        suspicious_sender = False
        if sender and ("@" not in sender or sender.endswith(".xyz")):
            suspicious_sender = True
            reasons.append("Sender domain looks suspicious")

        # Risk score
        risk_score = keyword_hits * 10 + len(suspicious_links) * 20
        if suspicious_sender:
            risk_score += 20

        risk_score = min(risk_score, 100)

        # Severity
        if risk_score >= 80:
            severity = "HIGH"
            color = "red"
        elif risk_score >= 40:
            severity = "MEDIUM"
            color = "orange"
        else:
            severity = "LOW"
            color = "green"

    # -------- RESULTS --------
    st.subheader("Analysis Results")

    colA, colB, colC = st.columns(3)
    colA.metric("Keyword Flags", keyword_hits)
    colB.metric("Suspicious Links", len(suspicious_links))
    colC.metric("Risk Score", f"{risk_score}/100")

    # Severity Card
    st.markdown(f"""
    <div style="
        padding:20px;
        border-radius:10px;
        border:2px solid {color};
        text-align:center;
        margin-top:20px;
    ">
        <h2 style="color:{color};">Severity: {severity}</h2>
    </div>
    """, unsafe_allow_html=True)

    # Alerts
    if suspicious_links:
        st.warning("Suspicious links detected:")
        for link in suspicious_links:
            st.write(link)

    if suspicious_sender:
        st.error("Sender email looks suspicious")

    if risk_score < 40:
        st.success("No strong phishing indicators detected")

    # -------- EXPLANATION --------
    st.subheader("Why this was flagged")

    if reasons:
        for r in reasons:
            st.write(f"- {r}")
    else:
        st.write("No major phishing indicators detected")

    # -------- REPORT --------
    report = f"""
PhishEye Report

----------------------------
Sender: {sender}
Subject: {subject}

Risk Score: {risk_score}/100
Severity: {severity}

Findings:
"""

    for r in reasons:
        report += f"- {r}\n"

    st.download_button(
        label="Download Report",
        data=report,
        file_name="phishing_report.txt",
        mime="text/plain"
    )

elif analyze:
    st.warning("Please enter email content")