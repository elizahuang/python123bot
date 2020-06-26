import os, configparser,codecs, requests,urllib
from linebot.models import (TextSendMessage, ImageSendMessage, FlexSendMessage,PostbackAction,QuickReply,QuickReplyButton)
from getContents import getPicUrl,getServerUrl
from copy import deepcopy
from settings import headers_to_db

config=configparser.ConfigParser()
config.read_file(codecs.open("config.ini", "r", "utf8"))

quickReply_hello={
    "type": "text", 
    "text": "",
    "quickReply": { 
    "items": [
      {
        "type": "action", 
        "action": {
          "type": "uri",
          "label": "你好",
          "uri":"https://www.google.com"
        }
      }
    ]
    }
}

def getFollowMsg():
    greetImgUrl=getPicUrl('greeting_pic_url')
    msgObjs=[]
    msgObjs.append(ImageSendMessage(
        type="image",
        original_content_url=greetImgUrl,
        preview_image_url=greetImgUrl
    ))
    msgObjs.append(TextSendMessage(
        text=config.get('followMsg','greeting_msg'),
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=PostbackAction(
                        label="你好!",
                        data="enterPersonInfo")
                )
            ]
        )
    ))
    #quickReply_hello["text"]=config.get('followMsg','greeting_msg')
    #print(quickReply_hello)
    #msgObjs.append(TextSendMessage(text=quickReply_hello))
    #print(msgObjs)
    return msgObjs


askForInfoMsg={
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Brown Cafe",
        "wrap": True,
        "weight": "regular",
        "size": "md"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "輸入資料",
          "uri": "https://www.google.com"
        },
        "gravity": "center",
        "color": "#45566d",
        "position": "relative"
      }
    ],
    "flex": 0,
    "borderColor": "#ffffff"
  }
}

def askForPersonInfo():
    askForInfoMsg["body"]["contents"][0]["text"]=config.get('followMsg','ask_for_info')
    return FlexSendMessage(alt_text="開始填寫資料",contents=askForInfoMsg)

checkAccountStatusMsg={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "帳號審核中",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "感謝您使用「享藥健康」！\n正在審核您的帳號，請耐心等候。\n我們會於審核通過時，通知您。",
            "wrap": True
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "postback",
          "label": "查看審核狀態",
          "data": "checkCheckStatus"
        }
      }
    ],
    "flex": 0
  }
}

def returnInCheck():
  #flex["hero"]["url"]=
  flex=deepcopy(checkAccountStatusMsg)
  return FlexSendMessage(alt_text="帳號審核中，請耐心等候",contents=flex)


showPendingMsg={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "審核中帳戶",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
            #add single pendings
        ]
      }
    ]
  }
}

showSinglePending= {
            "type": "text",
            "text": "姓名：patientName",
            "wrap": True
          }


def showCheckStatus(line_id):
  dataObj={"line_id":""}
  dataObj["line_id"]=line_id
  print(dataObj)
  print('test1')
  pendingResults=requests.post(urllib.parse.urljoin(getServerUrl(),'/getLinePending'),headers=headers_to_db,json=dataObj).json()
  #pendingResults=json.loads(pendingResults)
  print('test2')
  print(pendingResults)
  contents=[]
  for singlePending in pendingResults:
    item=deepcopy(showSinglePending)
    item["text"]="姓名："+singlePending["name"]
    contents.append(item)
  flex=deepcopy(showPendingMsg)
  flex["body"]["contents"][1]["contents"]=contents
  return FlexSendMessage(alt_text="您的帳號審核狀態",contents=flex)