from flask import Flask, request, abort

from linebot import(LineBotApi, WebhookHandler)

from linebot.exceptions import(InvalidSignatureError)

from linebot.models import * 

app=Flask(__name__)

#Channel Access Token
line_bot_api=LineBotApi('wFIIYURbi0u7+WZTgmX+lmzyyiVicagWMOkLNBliRW+Hb9ycfdXx0jg7fEydw32TdFF74qprleXwNEX/w7HhMl7QbkMV3vEGeHrY49kRs9okUW9gz14HQTaOUqku5vBit2DYWxzgZpuQ6FyxCg8erAdB04t89/1O/w1cDnyilFU=')
#Channel Secret
handler=WebhookHandler('3194fbf9c0e027b0aec2ac2abb390f29')

#監聽來自 /callback的Post request
@app.route("/callback", methods=['POST'])
def callback():
    #get X-Line-Signature header value
    signature=request.headers['X-Line-Signature']
    #get request body as text
    body=request.get_data(as_text=True)
    app.logger.info("Request body: "+body)
    #handle webhook body
    try: 
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

#處理訊息
@handler.add(MessageEvent ,message=TextMessage)
def handle_message(event):
    message=TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os 
if __name__=="__main__":
    port=int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)