import os
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_test_email():
    mail_to = os.environ.get("MAIL_TO")
    mail_pass = os.environ.get("MAIL_PASS")
    
    if not mail_to or not mail_pass:
        print("⚠️ Email credentials (MAIL_TO / MAIL_PASS) are missing in environment variables.")
        return

    timestamp = datetime.datetime.utcnow().isoformat()
    report_content = f"""
    ==================================================
    🚀 AD ASTRA OMNI: SOVEREIGN TEST REPORT
    ==================================================
    📅 Timestamp: {timestamp} UTC
    🌐 Status: SUCCESSFUL CONNECTION TEST
    
    [SYSTEM MESSAGE]:
    This is a verified test transmission from your Apex Sovereign AI Engine. All systems are fully operational, secure, and ready for autonomous operations.
    ==================================================
    """

    try:
        msg = MIMEMultipart()
        msg['From'] = mail_to
        msg['To'] = mail_to
        msg['Subject'] = "🧪 [Ad Astra Omni] Sovereign Test Email Verification"
        
        msg.attach(MIMEText(report_content, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(mail_to, mail_pass)
        server.sendmail(mail_to, mail_to, msg.as_string())
        server.quit()
        print("✅ Test email successfully sent to your inbox!")
    except Exception as e:
        print(f"❌ Failed to send test email: {e} (Note: If using Gmail, ensure you use an App Password).")

if __name__ == "__main__":
    send_test_email()
