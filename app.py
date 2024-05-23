from flask import Flask, request
import user_agents

app = Flask(__name__)

@app.route('/')
def index():
    user_agent_str = request.headers.get('User-Agent')
    user_agent = user_agents.parse(user_agent_str)

    browser = user_agent.browser.family
    browser_version = user_agent.browser.version_string
    os = user_agent.os.family
    os_version = user_agent.os.version_string
    device = user_agent.device.family

    return f'''
        <html>
            <body>
                <h1>Connection Information</h1>
                <p><strong>Browser:</strong> {browser} {browser_version}</p>
                <p><strong>Operating System:</strong> {os} {os_version}</p>
                <p><strong>Device:</strong> {device}</p>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

