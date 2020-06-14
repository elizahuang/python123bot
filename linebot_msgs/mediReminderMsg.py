from copy import deepcopy
from linebot.models import FlexSendMessage,TextSendMessage
import getContents
import requests,urllib.parse,json
from flask import Blueprint,request,Response
from settings import line_bot_api

mediReminderMsg = Blueprint('mediReminderMsg', __name__,)
mediRemindFlex={
  "type": "bubble",
  "size": "kilo",
  "hero": {
    "type": "image",
    "url": "https://4790063d1f56.ngrok.io/sys_img/pickMediReminder.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "contents": [
      {
        "type": "text",
        "text": "亮亮藥局提醒您： \n柯文華先生，您的慢箋領藥時間快到了！ 請於5/4(一) ~ 5/13(三)，攜帶健保卡前來藥局領取慢箋藥品！",
        "wrap": True,
        "size": "md",
        "weight": "regular"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "color": "#45566d",
        "action": {
          "type": "postback",
          "label": "知道了，確定會去領",
          "data": "hello"
        }
      },
      {
        "type": "button",
        "style": "secondary",
        "color": "#ffffff",
        "action": {
          "type": "postback",
          "label": "有問題，聯絡藥局",
          "data": "copyAllRecievedData"
        }
      }
    ]
  }
}

confirmData={
  "type":"confirmPickMed",
  "data":{
  "postNumber":"",
  "patientName":"",
  "pickDate1":"",
  "pickDate2":"",
  "user_lineid":""
  }
}

'''
quickReply_askQuestion=QuickReply(
    items = [
        QuickReplyButton(action = MessageAction(label = "是，確定要聯絡藥局", text = "是，確定要聯絡藥局")),
        QuickReplyButton(action = MessageAction(label = "取消，無須聯絡藥局", text = "取消，無須聯絡藥局"),)
    ]
)'''


def sendMediRemind(pharName, pharmLineId, patientName, patientId, gender, pickDate1, pickDate2):
    flex=deepcopy(mediRemindFlex)
    flex["hero"]["url"]=getContents.getPicUrl('pick_medi_reminder_url')
    flex["body"]["contents"][0]["text"]=pharName+"提醒您：\n"+patientName+gender+"您的慢箋領藥時間快到了！請於"+pickDate1+"~"+pickDate2+"，攜帶健保卡，前來領取慢箋藥品！"
    flex["footer"]["contents"][0]["action"]["data"]="patientId={id}".format(id=patientId)
    #flex["footer"]["contents"][1]["action"]["uri"]='https://line.me/R/ti/p/{LINE_id}'.format(LINE_id=pharmLineId)
    #flex["footer"]["contents"][1]["action"]["uri"]=urllib.parse.urljoin('https://line.me/R/ti/p/', pharmLineId)
    return FlexSendMessage(alt_text='慢箋領藥時間提醒',contents=flex)

@mediReminderMsg.route('/sendReminder',methods=['POST'])
def sendMediRemind():
    try:
        data=dict(request.form)
        flex=deepcopy(mediRemindFlex)
        
        postNumber=data['postNumber']#data['']
        pharName=data['pharName']#'213'#data['pharName']
        patientName=data['patientName']#'123'#data['patientName']
        gender='male'#data['gender']
        pickDate1=data['pickDate1']#'123'#data['pickdate1']
        pickDate2=data['pickDate2']#'123'#data['pickdate2']
        weekday1=data['weekday1']
        weekday2=data['weekday2']
        user_lineid=data['user_lineid']#'123'#data['user_lineid']
        
        confirmData2=deepcopy(confirmData)
        confirmData2["data"]["postNumber"]=postNumber
        confirmData2["data"]["patientName"]=patientName
        confirmData2["data"]["pickDate1"]=pickDate1
        confirmData2["data"]["pickDate2"]=pickDate2
        confirmData2["data"]["weekday1"]=weekday1  #tell亮亮
        confirmData2["data"]["weekday2"]=weekday2
        confirmData2["data"]["user_lineid"]=user_lineid
        confirmData2=json.dumps(confirmData2)
        print("confirmData2:")
        print(confirmData2)


        if gender=='male':
            title='先生'
        else:
            title='小姐'

        #藥單編號
        #if(data['pharLineId']==None):
        #  del flex
        #pharmLineId=data['pharLineId'] 
        
        flex["body"]["contents"][0]["text"]=pharName+"提醒您：\n"+patientName+title+"您的慢箋領藥時間快到了！\n請於"+pickDate1+getContents.getWeekDay(weekday1)+"~"+pickDate2+getContents.getWeekDay(weekday2)+"，攜帶健保卡，前來領取慢箋藥品！"
        flex["footer"]["contents"][0]["action"]["data"]=confirmData2


        stringFormData={
          "type":"ask_when_send_reminder",
          "data":""
        }
        
        stringFormData["data"]=data
        stringFormData=json.dumps(stringFormData)
        flex["footer"]["contents"][1]["action"]["data"]=stringFormData
        flex["hero"]["url"]=getContents.getPicUrl('pick_medi_reminder_url')
                
        line_bot_api.push_message(user_lineid,FlexSendMessage(alt_text='慢箋領藥時間提醒',contents=flex))
        status_code = Response(status=200)
        
    except:
        return 'err', 500
        #status_code = Response(status=500)
    #status_code
    return 'ok', 200




mediConfirmFlex={
  "type": "bubble",
  "size": "kilo",
  "hero": {
    "type": "image",
    "size": "full",
    "aspectMode": "cover",
    "aspectRatio": "320:213",
    "url": "https://82f0de3bfecd.ngrok.io/sys_img/pickMediConfirm.png"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "baseline",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "123",
            "wrap": True,
            "size": "xs",
            "flex": 5
          }
        ]
      }
    ],
    "spacing": "sm",
    "paddingAll": "13px"
  },
  "styles": {
    "body": {
      "separator": True
    },
    "footer": {
      "separator": True
    }
  }
}

def sendRemindConfirmMsg(postConfirmParam):
    msgObjs=[]
    msgObjs.append(TextSendMessage(text=getContents.getTextContents('msg_contents','reply_pickmedi_confirmed')))
    #get patient pick med info with patient id

    #requests.post('{postParam}'.format(postParam=postPatientIdParam))
    patientName=postConfirmParam["patientName"]
    pickDate1=postConfirmParam["pickDate1"]
    pickDate2=postConfirmParam["pickDate2"]
    weekday1=postConfirmParam["weekday1"]
    weekday2=postConfirmParam["weekday2"]
    flex=deepcopy(mediConfirmFlex)
    flex["hero"]["url"]=getContents.getPicUrl('pick_medi_confirm_url')
    flex["body"]["contents"][0]["contents"][0]["text"]=patientName+" 您好，\n已確認您的預約慢性處方箋領藥日:"+pickDate1+getContents.getWeekDay(weekday1)+"~"+pickDate2+getContents.getWeekDay(weekday2)
    msgObjs.append(FlexSendMessage(alt_text='慢箋領藥時間確認',contents=flex))
    return msgObjs

