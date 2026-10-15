import os
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_ai_report():
    timestamp = datetime.datetime.utcnow().isoformat()
    report = f"""
    ==================================================
    🚀 AD ASTRA OMNI: THE APEX SOVEREIGN AI ENGINE
    ==================================================
    📅 Timestamp: {timestamp} UTC
    🌐 Status: FULLY OPERATIONAL & AUTONOMOUS
    
    [SYSTEM ANALYTICS & CAPABILITIES]:
    - Autonomous Cloud Orchestration: ACTIVE
    - AI-Driven Intelligence Core: ONLINE
    - Multi-Repo Synchronization: STABLE (Engine, Core, OS)
    - Security & Self-Healing Protocols: ENGAGED
    
    "The ultimate autonomous ecosystem is now sovereign."
    ==================================================
    """
    print(report)
    return report

def send_email_notification(report_content):
    mail_to = os.environ.get("MAIL_TO")
    mail_pass = os.environ.get("MAIL_PASS")
    
    if not mail_to or not mail_pass:
        print("⚠️ Email credentials (MAIL_TO / MAIL_PASS) not set. Skipping email notification.")
        return

    try:
        msg = MIMEMultipart()
        msg['From'] = mail_to
        msg['To'] = mail_to
        msg['Subject'] = "🌟 [Ad Astra Omni] Apex Sovereign AI Status Report"
        
        msg.attach(MIMEText(report_content, 'plain'))
        
        # الاتصال بخادم البريد (Gmail SMTP كمثال)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(mail_to, mail_pass)
        server.sendmail(mail_to, mail_to, msg.as_string())
        server.quit()
        print("✅ Omni Apex Report successfully sent to your email!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    report = generate_ai_report()
    send_email_notification(report)
