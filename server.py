from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)

# ── 고정값 ──
GMAIL_USER = 'icuvenews@gmail.com'
GMAIL_PASS = 'wdui gjgj dziu qltt'
SENDER_NAME = 'iCUVE'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'ok': True, 'message': 'iCUVE 서버 정상 작동 중'})

@app.route('/send', methods=['POST'])
def send():
    try:
        data = request.json
        to_email = data.get('to_email', '').strip()
        to_name  = data.get('to_name', '').strip()
        subject  = data.get('subject', '').strip()
        html     = data.get('html', '')

        if not to_email or not subject:
            return jsonify({'ok': False, 'error': '수신자 또는 제목 누락'})

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From']    = f'{SENDER_NAME} <{GMAIL_USER}>'
        msg['To']      = f'{to_name} <{to_email}>' if to_name else to_email

        msg.attach(MIMEText(html, 'html', 'utf-8'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PASS)
            server.sendmail(GMAIL_USER, to_email, msg.as_string())

        return jsonify({'ok': True})

    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False)
