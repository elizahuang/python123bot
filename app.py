from flask import Flask, request, abort, send_file
from linebot import(LineBotApi, WebhookHandler)
from linebot.exceptions import(InvalidSignatureError)
from linebot.models import (MessageEvent,FollowEvent, TextMessage, ImageMessage, TextSendMessage, ImageSendMessage)
import configparser, json, codecs, emoji, requests, os
import flexMsgTest, setRichMenu

app=Flask(__name__)
config=configparser.ConfigParser()
config.read_file(codecs.open("config.ini", "r", "utf8"))
#config.read_file('config.ini')

'''Channel Access Token'''
line_bot_api=LineBotApi(config.get('line-bot','channel_access_token'))
'''Channel Secret'''
handler=WebhookHandler(config.get('line-bot','channel_secret'))

@app.route("/greetingPic",methods=['GET','POST'])#
def returnGreetingPic():
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    greetingPicPath=fileDir+"/greetingPic.png"
    return send_file(greetingPicPath, mimetype='image/png')   

@app.route('/<get_sys_img>/<pic_path>',methods=['GET','POST'])#
def returnPic():
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    targetPath=fileDir+config.get('paths',get_sys_img)+config.get('paths',pic_path)
    #greetingPicPath=fileDir+"/greetingPic.png"
    #greetingPicPath=fileDir+targetPath
    return send_file(greetingPicPath, mimetype='image/png')   

'''監聽來自 /callback的Post request  伺服器設置來接收line發送過來資訊的位置'''
@app.route("/callback", methods=['POST'])
def callback():
    '''get X-Line-Signature header value'''
    signature=request.headers['X-Line-Signature']
    '''get request body as text'''
    body=request.get_data(as_text=True)
    app.logger.info("Request body: "+body)
    #print(request)
    #print(request.headers)
    #print(body)
    #line_bot_api.broadcast(TextSendMessage(text='broadcast_test'),True)
    '''handle webhook body'''
    try: 
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

'''處理訊息'''
@handler.add(FollowEvent)
def follow(event):
    '''savePatientInfo()  firstname, lastname, gender , card number, id number, chatbot number'''
   
    userId=event.source.user_id ## 紀錄userId到DB
    print(userId)

    '''
    #getPatientInfo();  firstname, lastname, gender, chatbot number
    #getPharmInfo();  Pharmacy name, Pharmacist name'''
    
    lastName="汪";
    gender="male"
    if gender=="male":
        title="先生"
    else: title="小姐"

    pharmacyName="亮亮藥局"
    pharmacistName="王藥師"
    
    #greetImgUrl=config.get('urls','heroku_server_path')+config.get('urls','greeting_pic_url')
    greetImgUrl=config.get('urls','heroku_server_path')+config.get('paths','get_sys_img')+config.get('paths','greeting_pic_url')
    followMsg=lastName+title+"您好，\n我是"+pharmacyName+"的"+pharmacistName+"。\n"+config.get('followMsg','greeting_msg')
    
    line_bot_api.reply_message(event.reply_token,ImageSendMessage(
        type="image",
        original_content_url=greetImgUrl,
        preview_image_url=greetImgUrl
    ))
    line_bot_api.push_message(event.source.user_id,TextSendMessage(followMsg))
    line_bot_api.push_message(event.source.user_id,TextSendMessage(config.get('followMsg','instruc')))    
    
    #line_bot_api.broadcast(SendMessage(text='broadcast_test'),True)
    #followMsg=config.get('followMsg','greeting_msg')+ emoji.emojize(":grinning_face_with_big_eyes:")+"\n"+config.get('followMsg','instruc')
    #print(type(config.get('msgWords','follow_msg')))
    #line_bot_api.reply_message(event.reply_token,TextSendMessage(followMsg));
    #StickerSendMessage(package_id=1, sticker_id=2)    

@handler.add(MessageEvent ,message=[TextMessage,ImageMessage])#||ImageMessage
def echo(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        #print(event.message)
        #messageId=event.message.id
        #print(messageId)       
        #print(event.message.type)
        if event.message.type=="image":
            url='https://api-data.line.me/v2/bot/message/{imageMessageId}/content'.format(imageMessageId=event.message.id)
            headers = {'Authorization' : 'Bearer {botToken}'.format(botToken=config.get('line-bot','channel_access_token'))}
            bytesPic=requests.get(url,headers=headers).content
            
            with open("test.png", 'wb+') as fd:
                fd.write(bytesPic)
            
            #save picbytes into file. Then open file and convert bytes in to image. 
            """
            with open('testWriteBytes', 'wb+') as fd:
                fd.write(message_content)
            with open('testWriteBytes', 'rb')as rd:
                data=rd.read()
            with open('test.png', 'wb+') as fd:
                fd.write(data)
            """

            #Failed. Use line api to retreive message_content. 
            '''
            message_content = line_bot_api.get_message_content(event.message.id)
            with open('test.png', 'wb+') as fd:
                        fd.write(message_content)
            '''                
        else:
            if event.message.text=="flexBubble":
                content=flexMsgTest.returnBubble()
                replyMsg=FlexSendMessage(alt_text="flex test failed.",contents =content)
                line_bot_api.reply_message(event.reply_token,replyMsg)
            elif event.message.text=="flexCarousel":
                content=flexMsgTest.returnCarousel()
                replyMsg=FlexSendMessage(alt_text="flex test failed.",contents =content)
                line_bot_api.reply_message(event.reply_token,replyMsg)    
            else:    
                pretty_note = '♫♪♬'
                
                #print(event.message)
                #texttype=type(event.message.text)
                #print(type(event.message.text))
                
                pretty_note+=(event.message.text)
                replyMsg=TextSendMessage(text=pretty_note)
                line_bot_api.reply_message(event.reply_token, replyMsg)
                line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Hello World!'))

            
if __name__=="__main__":
    #app.debug=True
    port=int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)
    app.run()


