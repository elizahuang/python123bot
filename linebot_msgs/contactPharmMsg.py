import os
from linebot.models import FlexSendMessage
from getContents import getPicUrl,getTextContents
from copy import deepcopy

contactPharmFlex={
  "type": "bubble",
  "size": "kilo",
  "hero": {
    "type": "image",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://ae759c2c0c49.ngrok.io/sys_img/contactPharm.png"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "藥局名稱",
        "weight": "bold",
        "size": "lg"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "電話：",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "地址：",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
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
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "icon",
            "url": "https://ae759c2c0c49.ngrok.io/sys_img/phoneIcon.png",
            "offsetStart": "68px",
            "position": "relative",
            "offsetTop": "3px"
          },
          {
            "type": "text",
            "text": "撥打電話",
            "align": "center"
          }
        ],
        "action": {
          "type": "message",
          "label": "action",
          "text": "請撥打 藥局名稱："
        }
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "icon",
            "url": "https://ae759c2c0c49.ngrok.io/sys_img/lineIcon.png",
            "offsetStart": "65px",
            "position": "relative",
            "size": "xl",
            "offsetTop": "5px"
          },
          {
            "type": "text",
            "text": "線上諮詢",
            "align": "center"
          }
        ],
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://line.me/R/ti/p/"
        }
      }
    ],
    "flex": 0
  }
}

def contactPharmMsg():
    pharmName="樂森藥局"
    pharmNumber="06-2600000"
    pharmAddress="台南市東區123巷123號"
    pharmLineId='@tsx6095n'

    flex=deepcopy(contactPharmFlex)
    flex["hero"]["url"]=getPicUrl('contactPharm_pic_url')
    flex["body"]["contents"][0]["text"]=pharmName
    flex["body"]["contents"][1]["contents"][0]["contents"][0]["text"]="電話："+pharmNumber
    flex["body"]["contents"][1]["contents"][0]["contents"][1]["text"]="地址："+pharmAddress
    flex["footer"]["contents"][0]["contents"][0]["url"]=getPicUrl('phone_icon_url')
    flex["footer"]["contents"][0]["action"]["text"]="請撥打 "+pharmName+":\n"+pharmNumber
    flex["footer"]["contents"][1]["contents"][0]["url"]=getPicUrl('line_icon_url')
    flex["footer"]["contents"][1]["action"]["uri"]='https://line.me/R/ti/p/{LINE_id}'.format(LINE_id=pharmLineId)

    return FlexSendMessage(alt_text='藥局資訊',contents=flex) 
