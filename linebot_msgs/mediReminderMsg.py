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
    "url": "https://ae759c2c0c49.ngrok.io/sys_img/pickMediReminder.png",
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
          "label": "知道了。確定會去領喔！",
          "data": "patientId=",
          "displayText": "知道了。確定會去領喔！"
        }
      },
      {
        "type": "button",
        "style": "secondary",
        "color": "#ffffff",
        "action": {
          "type": "message",
          "label": "有問題，聯絡藥局",
          "text": "有問題，聯絡藥局"
        }
      }
    ]
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
        print(data)
        flex=deepcopy(mediRemindFlex)
        '''
        pharName=
        patientName=
        gender=
        if gender=='male':
            title='先生'
        else:
            title='小姐'
        pickDate1=
        pickDate2=
        patientId=
        user_lineid=
        pharmLineId=     
        
        flex["body"]["contents"][0]["text"]=pharName+"提醒您：\n"+patientName+title+"您的慢箋領藥時間快到了！\n請於"+pickDate1+"~"+pickDate2+"，攜帶健保卡，前來領取慢箋藥品！"
        flex["footer"]["contents"][0]["action"]["data"]="patientId={id}".format(id=patientId)
        flex["footer"]["contents"][1]["action"]["uri"]='https://line.me/R/ti/p/{LINE_id}'.format(LINE_id=pharmLineId)
        flex["footer"]["contents"][1]["action"]["uri"]=urllib.parse.urljoin('https://line.me/R/ti/p/', pharmLineId)
        '''
        status_code = Response(status=200)
        flex["hero"]["url"]=getContents.getPicUrl('pick_medi_reminder_url')
        line_bot_api.push_message('U36ae4132a3e2709192e0b635596435b3',FlexSendMessage(alt_text='慢箋領藥時間提醒',contents=flex))
    except:
        status_code = Response(status=500)
    
    return status_code



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

def sendRemindConfirmMsg(postPatientIdParam):
    msgObjs=[]
    msgObjs.append(TextSendMessage(text=getContents.getTextContents('msg_contents','reply_pickmedi_confirmed')))
    #get patient pick med info with patient id

    #requests.post('{postParam}'.format(postParam=postPatientIdParam))
    patientName="eeeee"
    pickDate1="5/4(一)"
    pickDate2="5/13(三)"
    flex=deepcopy(mediConfirmFlex)
    flex["hero"]["url"]=getContents.getPicUrl('pick_medi_confirm_url')
    flex["body"]["contents"][0]["contents"][0]["text"]=patientName+" 您好，已確認您的預約慢性處方箋領藥日:\n"+pickDate1+"~"+pickDate2
    msgObjs.append(FlexSendMessage(alt_text='慢箋領藥時間確認',contents=flex))
    return msgObjs

