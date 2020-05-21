from flask import Flask, request, abort
from linebot import(LineBotApi, WebhookHandler)
from linebot.exceptions import(InvalidSignatureError)
from linebot.models import *  #need revise
import configparser, json, codecs, emoji
import flexMsgTest
import requests

app=Flask(__name__)
config=configparser.ConfigParser()
#config.readfp(codecs.open("config.ini", "r", "utf8"))
config.read_file(codecs.open("config.ini", "r", "utf8"))
#config.read('config.ini')

#Channel Access Token
line_bot_api=LineBotApi(config.get('line-bot','channel_access_token'))
#Channel Secret
handler=WebhookHandler(config.get('line-bot','channel_secret'))


#監聽來自 /callback的Post request  #伺服器設置來接收line發送過來資訊的位置
@app.route("/callback", methods=['GET','POST'])
def callback():
    #get X-Line-Signature header value
    signature=request.headers['X-Line-Signature']
    #get request body as text
    body=request.get_data(as_text=True)
    app.logger.info("Request body: "+body)
    #print(request)
    #print(request.headers)
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
    userId=event.source.user_id ## 紀錄userId到DB
    print(userId)

@handler.add(MessageEvent ,message=[TextMessage,ImageMessage])#||ImageMessage
def echo(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        #print(event.message)
        messageId=event.message.id
        print(messageId)       
        print(event.message.type)
        if event.message.type=="image":
            url='https://api-data.line.me/v2/bot/message/%s/content'%(messageId)
            botToken=config.get('line-bot','channel_access_token')
            headers = {'Authorization' : 'Bearer %s'%(botToken)}
            bytesPic=requests.get(url,headers=headers).content
            
            with open("test.png", 'wb+') as fd:
                fd.write(bytesPic)
                
        else:
            if event.message.text=="flexBubble":
                content=flexMsgTest.returnBubble()
                #replyMsg=FlexSendMessage(contents =get_or_new_from_json_dict_with_types(content))
                replyMsg=FlexSendMessage(alt_text="flex test failed.",contents =content)
                line_bot_api.reply_message(event.reply_token,replyMsg)
            elif event.message.text=="flexCarousel":
                content=flexMsgTest.returnCarousel()
                replyMsg=FlexSendMessage(alt_text="flex test failed.",contents =content)
                line_bot_api.reply_message(event.reply_token,replyMsg)    
            else:    
                pretty_note = '♫♪♬'
                '''
                print(event.message)
                texttype=type(event.message.text)
                print(type(event.message.text))
                '''
                pretty_note+=(event.message.text)
                replyMsg=TextSendMessage(text=pretty_note)
                line_bot_api.reply_message(event.reply_token, replyMsg)
                line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Hello World!'))


            '''
            message_content = line_bot_api.get_message_content(event.message.id)
            with open('test.png', 'wb+') as fd:
                        fd.write(message_content)
            '''
            
import os 
if __name__=="__main__":
    port=int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)
    app.run()


####testing heroku git