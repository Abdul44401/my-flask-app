from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return '''
        <html>
            <head>
                <title>Fleet Dashboard</title>
                <style>
                    body { margin: 0; background: #f4f4f4; }
                    iframe { display: block; border: none; width: 100vw; height: 100vh; }
                </style>
            </head>
            <body>
                <iframe title="Fleet Management" src="https://app.powerbi.com/reportEmbed?reportId=38a7f1b4-4c67-40b3-81de-58bd322e606e&autoAuth=true&ctid=80f93bfb-0dec-4cbf-8835-279bd4f13ab7" allowFullScreen="true"></iframe>
            </body>
        </html>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
