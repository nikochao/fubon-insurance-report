# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('7fmxuM5SubOVtJNhKxjuGKgjIkNfk6HRLmPGTZRzEdEVRUnyYN84tG7J/qfkLmupzljtR4MNi0FgCbZIltrOVCe6uVfI21NL/IyTreMSM3Nn2+GtLAALxZtyydDXZ7M63DJEKW4osr0P34QIbJE0MwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('deec9998ffe57bf957ce3f836130979a')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()