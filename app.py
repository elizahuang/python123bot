from flask import Flask, request, abort
from linebot import(LineBotApi, WebhookHandler)
from linebot.exceptions import(InvalidSignatureError)
from linebot.models import (MessageEvent,FollowEvent,PostbackEvent, TextMessage, ImageMessage, TextSendMessage, ImageSendMessage, FlexSendMessage)
import configparser, json, codecs, emoji, requests, os,re,math
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from pathlib import Path
from urls import urls
from tests import flexMsgTest
from linebot_msgs.followMsg import getFollowMsg,askForPersonInfo
from linebot_msgs.instructionMsg import *
from linebot_msgs.pharmacyInfoMsg import *
from linebot_msgs.otherFunctionsMsg import *
from linebot_msgs.mediQuestionMsg import *
from linebot_msgs.contactPharmMsg import *
from linebot_msgs.mediToGrabMsg import *
from linebot_msgs.mediReminderMsg import mediReminderMsg
from linebot_msgs.mediReminderMsg import *
from settings import line_bot_api,handler, headers, backendUrl


app=Flask(__name__)
app.register_blueprint(urls) #urls of the projects were in urls.py
app.register_blueprint(mediReminderMsg)
config=configparser.ConfigParser()
config.read_file(codecs.open("config.ini", "r", "utf8"))


db = SQLAlchemy(app)
db.init_app(app)
###db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://b82f545f02c5ab:39ec4e6f@us-cdbr-east-05.cleardb.net/heroku_fac4d5e662f3db1"

'''Initialize channel access token and channel secret
is_heroku=os.environ.get("IS_HEROKU",None)
if is_heroku:
    channel_access_token=os.environ.get("CHANNEL_ACCESS_TOKEN",None)
    channel_secret=os.environ.get("CHANNEL_SECRET",None)
else:
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    channel_access_token=os.getenv("CHANNEL_ACCESS_TOKEN",None)
    channel_secret=os.getenv("CHANNEL_SECRET",None)


line_bot_api=LineBotApi(channel_access_token)
handler=WebhookHandler(channel_secret)
headers = {'Authorization' : 'Bearer {botToken}'.format(botToken=channel_access_token)}'''


'''response for endpoint of line channel'''
@app.route("/callback", methods=['POST'])
def callback():
    #get X-Line-Signature header value
    signature=request.headers['X-Line-Signature']  
    #get request body as text
    body=request.get_data(as_text=True)  
    app.logger.info("Request body: "+body)
    print(request)
    #print(request.headers)
    print(body)
    #line_bot_api.broadcast(TextSendMessage(text='broadcast_test'),True)
    '''handle webhook body'''
    try: 
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(FollowEvent)
def follow(event):
    '''savePatientInfo()  firstname, lastname, card number, id number, chatbot number'''
    userId=event.source.user_id ## 紀錄userId到DB
    print(userId)
    '''
    #getPatientInfo();  firstname, lastname, gender, chatbot number
    #getPharmInfo();  Pharmacy name, Pharmacist name'''

    line_bot_api.reply_message(event.reply_token,getFollowMsg())

    #line_bot_api.push_message(event.source.user_id,TextSendMessage(followMsg))
    #line_bot_api.push_message(event.source.user_id,TextSendMessage(config.get('followMsg','instruc'))) 
    #getUserLineInfo.get_save_userInfo(event.source.user_id,channel_access_token);    
    #line_bot_api.broadcast(SendMessage(text='broadcast_test'),True)
    #followMsg=config.get('followMsg','greeting_msg')+ emoji.emojize(":grinning_face_with_big_eyes:")+"\n"+config.get('followMsg','instruc')   


@handler.add(MessageEvent ,message=[TextMessage,ImageMessage])
def echo(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        #print(event.message)
        #messageId=event.message.id
        #print(messageId)       
        #print(event.message.type)
        if event.message.type=="image":
            url='https://api-data.line.me/v2/bot/message/{imageMessageId}/content'.format(imageMessageId=event.message.id)
            headers = {'Authorization' : 'Bearer {botToken}'.format(botToken=channel_access_token)}
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

        else:
            if event.message.text=="撥打電話":
                '''call function to get pharmacy number'''
                pharmNumber='\n0900-000-000'
                replyMsg=config.get('msg_contents','dial_instruc') 
                replyMsg+=pharmNumber 
                line_bot_api.reply_message(event.reply_token,TextSendMessage(replyMsg))
            elif event.message.text=="用藥問題":
                '''call function to get pharmacy number'''
                line_bot_api.reply_message(event.reply_token,mediQuestions())
            
            elif (event.message.text=="藥局資訊"):
                path=urllib.parse.urljoin('phInfo/','123o')#event.source.user_id
                phInfo=requests.get(urllib.parse.urljoin(backendUrl,path)).content
                #print(phInfo)
                phInfo=json.loads(phInfo)
                print((phInfo))
                print(len(phInfo))
                print(len(phInfo))
                print(len(phInfo))
                if (len(phInfo)!=0):
                    line_bot_api.reply_message(event.reply_token,setAndGetPharmacyFlex(phInfo))
                else:
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='您尚未綁定藥局，請進行資料填寫。'))
            elif event.message.text=="領藥日查詢":
                path=urllib.parse.urljoin('checkTime/','321')#event.source.user_id
                pickMediDate=requests.get(urllib.parse.urljoin(backendUrl,path)).content
                pickMediDate=json.loads(pickMediDate)
                print('test0')
                if (len(pickMediDate)!=0):
                    pickMediDate=replyDateSearch(pickMediDate)
                    #print('test1')
                    #print(len(pickMediDate))
                    msgLen=math.floor(len(pickMediDate)/5)+1
                    if(len(pickMediDate)/5>math.floor(len(pickMediDate)/5)):
                        msgLen=math.floor(len(pickMediDate)/5)+1
                    else: 
                        msgLen=math.floor(len(pickMediDate)/5)
                    #print(msgLen)
                    #print('test2')
                    if msgLen==1:
                        line_bot_api.reply_message(event.reply_token,pickMediDate)
                    elif msgLen==2:
                        sendmsg=pickMediDate[0:5]
                        line_bot_api.reply_message(event.reply_token,sendmsg)
                        pickMediDate.pop(0)
                        pickMediDate.pop(0)
                        pickMediDate.pop(0)
                        pickMediDate.pop(0)
                        pickMediDate.pop(0)
                        line_bot_api.push_message(event.source.user_id,pickMediDate)
                    elif msgLen==3:
                        sendmsg=pickMediDate[0:5]
                        line_bot_api.reply_message(event.reply_token,sendmsg)
                        pickMediDate.pop(0)
                        pickMediDate.pop(0)
                        pickMediDate.pop(0)
                        pickMediDate.pop(0)
                        pickMediDate.pop(0)
                        line_bot_api.push_message(event.source.user_id,pickMediDate)
                        pickMediDate.pop(0)
                        pickMediDate.pop(0)
                        pickMediDate.pop(0)
                        pickMediDate.pop(0)
                        pickMediDate.pop(0)
                        line_bot_api.push_message(event.source.user_id,pickMediDate)
                else:
                    replyMsg=replyNoNeedToPick()
                    line_bot_api.reply_message(event.reply_token,replyMsg)
                #content=mediToGrabContent.replyDateSearch()
                
            elif event.message.text=="其他功能":
                line_bot_api.reply_message(event.reply_token,sendOtherFuncMsg())
            elif event.message.text=="立即前往":
                '''get fb url'''
                fb_url='https://www.facebook.com/'
                requests.get(fb_url).content
            elif event.message.text=="有問題，聯絡藥局":
                line_bot_api.reply_message(event.reply_token,contactPharmMsg())
            elif event.message.text=="跳過教學":
                line_bot_api.reply_message(event.reply_token,replyNotNeedInstruc())
            elif event.message.text=="好的！顯示使用說明":
                line_bot_api.reply_message(event.reply_token,replyNeedInstruc())
            
            '''     
            else:    
                pretty_note = '♫♪♬'
                
                #print(event.message)
                #texttype=type(event.message.text)
                #print(type(event.message.text))
                
                pretty_note+=(event.message.text)
                replyMsg=TextSendMessage(text=pretty_note)
                line_bot_api.reply_message(event.reply_token, replyMsg)
                line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Hello World!'))
            '''
            if event.message.text=="資料已填":
                line_bot_api.reply_message(event.reply_token,sendInstrucMsg())
            #if event.message.text=="test":
                #msg=sendMediRemind('樂森藥局', '@tsx6095n', 'eeeeee', '11', 'female', '2020-06-12', '2020-06-21')
                #line_bot_api.reply_message(event.reply_token,TextSendMessage(text='testReply',quick_reply=QuickReply(contents=testReply)))

       
def sendQuestion(type,user_lineid):
    questionObj={
        "Type": 1,
        "LineID": ""
    }
    dataObj=deepcopy(questionObj)
    dataObj["Type"]=type
    dataObj["LineID"]=user_lineid
    path=urllib.parse.urljoin(backendUrl,'problem/')
    requests.post(path,data=dataObj)   


@handler.add(PostbackEvent)
def postbackReply(event):
    user_lineid='123o'
    if event.postback.data=="enterPersonInfo":
            line_bot_api.reply_message(event.reply_token,askForPersonInfo())
    elif event.postback.data=="recordQuestion=服藥方式":
        sendQuestion(1, user_lineid)
        line_bot_api.reply_message(event.reply_token,contactPharmMsg(user_lineid))
    elif event.postback.data=="recordQuestion=藥物副作用":
        sendQuestion(2, user_lineid)
        line_bot_api.reply_message(event.reply_token,contactPharmMsg(user_lineid))
    elif event.postback.data=="recordQuestion=藥物交互作用":
        sendQuestion(3, user_lineid)
        line_bot_api.reply_message(event.reply_token,contactPharmMsg(user_lineid))
    elif event.postback.data=="recordQuestion=藥物保存方式":
        sendQuestion(4, user_lineid)
        line_bot_api.reply_message(event.reply_token,contactPharmMsg(user_lineid))    
    elif event.postback.data=="recordQuestion=其他問題":
        sendQuestion(5, user_lineid)
        line_bot_api.reply_message(event.reply_token,contactPharmMsg(user_lineid))
    elif re.search("^patientId=",event.postback.data):
        line_bot_api.reply_message(event.reply_token,sendRemindConfirmMsg(event.postback.data))
    if isinstance(json.loads(event.postback.data),dict):
        received_data=json.loads(event.postback.data)
        print(received_data)
        if(received_data["type"]=='confirmPickMed'):
            line_bot_api.reply_message(event.reply_token,sendRemindConfirmMsg(received_data["data"]))
            url=urllib.parse.urljoin(backendUrl,'/notify/')
            #print(requests.get(urllib.parse.urljoin(url,received_data["data"]["postNumber"])))
            print(requests.get(urllib.parse.urljoin(url,"1"))) #???
            print('confirm pick med achieved.')
        elif(received_data["type"]=="ask_when_send_reminder"):
            line_bot_api.reply_message(event.reply_token,sendcontactPharmWithUndo(received_data["data"]))
        elif(received_data["type"]=="resendReminderFlex"):
            requests.post(urllib.parse.urljoin(getContents.getServerUrl(),"sendReminder"),data=received_data["data"])
    
    #print(event.postback.data)
        

   


if __name__=="__main__":
    #app.debug=True
    port=int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)
    app.run()

import views


