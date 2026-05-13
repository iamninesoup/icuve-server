from flask import Flask, request, jsonify
from flask_cors import CORS
import requests as req
import os

app = Flask(__name__)
CORS(app)

CLAUDE_API_KEY = os.environ.get('CLAUDE_API_KEY', '')
RESEND_API_KEY = os.environ.get('RESEND_API_KEY', '')
SENDER_EMAIL   = 'backstage@icuve.kr'
SENDER_NAME    = 'iCUVE'

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'ok': True, 'message': 'iCUVE 서버 정상 작동 중'})

@app.route('/ai', methods=['POST'])
def ai():
    try:
        data = request.json
        messages = data.get('messages', [])
        if not messages:
            return jsonify({'ok': False, 'error': '메시지 없음'})

        response = req.post(
            'https://api.anthropic.com/v1/messages',
            headers={
                'Content-Type': 'application/json',
                'x-api-key': CLAUDE_API_KEY,
                'anthropic-version': '2023-06-01'
            },
            json={
                'model': 'claude-sonnet-4-6',
                'max_tokens': 1500,
                'messages': messages
            },
            timeout=60
        )
        result = response.json()
        if 'error' in result:
            return jsonify({'ok': False, 'error': result['error']['message']})
        return jsonify({'ok': True, 'content': result['content']})

    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)})

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

        to_formatted = f'{to_name} <{to_email}>' if to_name else to_email

        response = req.post(
            'https://api.resend.com/emails',
            headers={
                'Authorization': f'Bearer {RESEND_API_KEY}',
                'Content-Type': 'application/json'
            },
            json={
                'from': f'{SENDER_NAME} <{SENDER_EMAIL}>',
                'to': [to_formatted],
                'subject': subject,
                'html': html
            },
            timeout=30
        )

        result = response.json()
        if response.status_code in [200, 201]:
            return jsonify({'ok': True, 'id': result.get('id')})
        else:
            return jsonify({'ok': False, 'error': result.get('message', '발송 실패')})

    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False)
