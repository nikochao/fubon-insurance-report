from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import*

import main

app = Flask(__name__)

line_bot_api = LineBotApi('7fmxuM5SubOVtJNhKxjuGKgjIkNfk6HRLmPGTZRzEdEVRUnyYN84tG7J/qfkLmupzljtR4MNi0FgCbZIltrOVCe6uVfI21NL/IyTreMSM3Nn2+GtLAALxZtyydDXZ7M63DJEKW4osr0P34QIbJE0MwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('deec9998ffe57bf957ce3f836130979a')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text=="保險進度":
        main.search()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="已寄電子郵件"))


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
