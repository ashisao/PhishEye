# PhishEye

PhishEye is a phishing email analysis tool that detects suspicious emails using content analysis, link inspection, and sender validation. It simulates real-world email threat detection used in SOC (Security Operations Center) environments.

## Features

- Email content analysis for phishing indicators  
- Detection of suspicious keywords (urgent, verify, login, etc.)  
- Extraction and inspection of links from email body  
- Identification of suspicious sender domains  
- Risk scoring system (0–100)  
- Severity classification (Low, Medium, High)  
- Explanation of detected threats  
- Downloadable phishing analysis report  
- Interactive dashboard using Streamlit  

## Tech Stack

- Python  
- Streamlit  
- Regex  

## How it Works

1. User inputs email content, sender, and subject  
2. System scans for phishing-related keywords  
3. Links are extracted and analyzed for suspicious patterns  
4. Sender email is validated for anomalies  
5. Risk score and severity are calculated  
6. Results are displayed with explanation  
7. A downloadable report is generated  

## Live Demo

https://your-phisheye-link.streamlit.app

## Use Case

PhishEye simulates phishing detection workflows used by SOC analysts to identify malicious emails, extract indicators of compromise (IOCs), and assess risk in real time.
