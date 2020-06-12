import os, configparser,codecs
from linebot.models import (TextSendMessage, ImageSendMessage, FlexSendMessage,PostbackAction,QuickReply,QuickReplyButton)
from getContents import getPicUrl

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
