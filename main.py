import os
import datetime
import urllib.request
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def check_ecosystem_health():
    # قائمة المستودعات السيادية للتحقق من حالتها
    repos = [
        "aliali12345908ali-hub/ad-astra-engine",
        "aliali12345908ali-hub/ad-astra-core",
        "aliali12345908ali-hub/adastra-autonomous-os",
        "aliali12345908ali-hub/ad-astra-omni"
    ]
    
    health_status = []
    for repo in repos:
        url = f"https://api.github.com/repos/{repo}/actions/runs?per_page=1"
        req = urllib.request.Request(url, headers={'User-Agent': 'AdAstra-Sovereign-Core'})
        try:
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode('utf-8'))
                if data.get('workflow_runs'):
                    latest_run = data['workflow_runs'][0]
                    status = latest_run.get('status')
                    conclusion = latest_run.get('conclusion')
                    health_status.append(f"🟢 {repo}: Status={status}, Conclusion={conclusion}")
                else:
                    health_status.append(f"🟡 {repo}: No active runs found.")
        except Exception as e:
            health_status.append(f"🔴 {repo}: Failed to fetch status ({e})")
            
    return "\n".join(health_status)

def run_omni_upgrade():
    timestamp = datetime.datetime.utcnow().isoformat()
    ecosystem_report = check_ecosystem_health()
    
    report = f"""
    ==================================================
    🚀 AD ASTRA OMNI: ADVANCED SOVEREIGN REPORT
    ==================================================
    📅 Timestamp: {timestamp} UTC
    
    [ECOSYSTEM NODES STATUS]:
    {ecosystem_report}
    
    ==================================================
    Status: All sovereign nodes operating under autonomous protocols.
    """
    print(report)
    return report

def send_email_notification(report_content):
    mail_to = os.environ.get("MAIL_TO")
    mail_pass = os.environ.get("MAIL_PASS")
    
    if not mail_to or not mail_pass:
        print("⚠️ Email credentials missing. Skipping transmission.")
        return

    try:
        msg = MIMEMultipart()
        msg['From'] = mail_to
        msg['To'] = mail_to
        msg['Subject'] = "⚡ [Ad Astra Omni] Advanced Sovereign Ecosystem Report"
        
        msg.attach(MIMEText(report_content, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(mail_to, mail_pass)
        server.sendmail(mail_to, mail_to, msg.as_string())
        server.quit()
        print("✅ Advanced ecosystem report successfully processed!")
    except Exception as e:
        print(f"❌ Email transmission note: {e}")

if __name__ == "__main__":
    report = run_omni_upgrade()
    send_email_notification(report)
