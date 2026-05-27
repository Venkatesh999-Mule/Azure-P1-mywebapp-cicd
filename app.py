from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>My Azure App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #0078d4, #00bcf2);
                color: white;
                text-align: center;
            }
            .card {
                background: rgba(255,255,255,0.15);
                padding: 40px 60px;
                border-radius: 16px;
                backdrop-filter: blur(10px);
            }
            h1 { font-size: 2.5rem; margin-bottom: 10px; }
            p  { font-size: 1.2rem; opacity: 0.9; }
            .badge {
                display: inline-block;
                margin-top: 20px;
                padding: 8px 20px;
                background: #00bcf2;
                border-radius: 20px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Hello from Azure!</h1>
            <p>This app is deployed using:</p>
            <p>
                <span class="badge">Azure Pipelines</span>
                <span class="badge">Docker</span>
                <span class="badge">App Service</span>
            </p>
            <p style="margin-top:20px; opacity:0.7;">CI/CD Pipeline is working perfectly ✅</p>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'App is running!'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
