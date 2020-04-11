from flask import Flask, request, abort
from linebot import(LineBotApi, WebhookHandler)
from linebot.exceptions import(InvalidSignatureError)
from linebot.models import * 
import configparser, json, codecs, emoji

app=Flask(__name__)
config=configparser.ConfigParser()
config.readfp(codecs.open("config.ini", "r", "utf8"))
#config.read('config.ini')

#Channel Access Token
line_bot_api=LineBotApi(config.get('line-bot','channel_access_token'))
#Channel Secret
handler=WebhookHandler(config.get('line-bot','channel_secret'))


#監聽來自 /callback的Post request  #伺服器設置來接收line發送過來資訊的位置
@app.route("/callback", methods=['POST'])
def callback():
    #get X-Line-Signature header value
    signature=request.headers['X-Line-Signature']
    #get request body as text
    body=request.get_data(as_text=True)
    app.logger.info("Request body: "+body)
    print(request)
    print(request.headers)
    
    #print(body)
    #handle webhook body
    #line_bot_api.broadcast(TextSendMessage(text='broadcast_test'),True)
    try: 
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

#處理訊息
@handler.add(FollowEvent)
def follow(event):
    #line_bot_api.broadcast(SendMessage(text='broadcast_test'),True)
    followMsg=config.get('followMsg','greeting_msg')+ emoji.emojize(":grinning_face_with_big_eyes:")+"\n"+config.get('followMsg','instruc')
    #print(type(config.get('msgWords','follow_msg')))
    line_bot_api.reply_message(event.reply_token,TextSendMessage(followMsg));
    #StickerSendMessage(package_id=1, sticker_id=2)

@handler.add(MessageEvent ,message=TextMessage)
def echo(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        pretty_note = '♫♪♬'
        #texttype=type(event.message.text)
        #print(type(event.message.text))
        pretty_note+=(event.message.text)
        message=TextSendMessage(text=pretty_note)
        line_bot_api.reply_message(event.reply_token, message)
        line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Hello World!'))

import os 
if __name__=="__main__":
    port=int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)
    app.run()


####testing heroku git