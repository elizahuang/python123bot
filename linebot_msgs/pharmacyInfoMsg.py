import os
from linebot.models import (TextSendMessage, ImageSendMessage, FlexSendMessage,MessageAction,QuickReply,QuickReplyButton)
from getContents import getPicUrl,getTextContents
from copy import deepcopy

pharmacyInfoFlex={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://ae759c2c0c49.ngrok.io/sys_img/pharmInfo.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "藥局名稱",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "電話：",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
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
                    "text": "地址：",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "icon",
            "size": "lg",
            "url": "https://ae759c2c0c49.ngrok.io/sys_img/phoneIcon.png",
            "position": "relative",
            "offsetStart": "22px",
            "offsetTop": "3px"
          },
          {
            "type": "text",
            "text": " 撥打電話",
            "gravity": "center",
            "weight": "regular",
            "align": "center"
          }
        ],
        "action": {
          "type": "message",
          "label": "action",
          "text": "請撥打 藥局名稱：\\n"
        }
      },
      "styles": {
        "body": {
          "separator": True
        },
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://ae759c2c0c49.ngrok.io/sys_img/lineInfo.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "藥局名稱Line客服",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "ID：",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "icon",
            "size": "lg",
            "position": "relative",
            "offsetTop": "6px",
            "offsetStart": "25px",
            "url": "https://ae759c2c0c49.ngrok.io/sys_img/lineIcon.png"
          },
          {
            "type": "text",
            "text": "加入好友",
            "gravity": "center",
            "weight": "regular",
            "align": "center"
          }
        ],
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://line.me/R/ti/p/@tsx6095n"
        }
      },
      "styles": {
        "body": {
          "separator": True
        },
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://ae759c2c0c49.ngrok.io/sys_img/fbInfo.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "藥局名稱FB粉專",
            "weight": "bold",
            "size": "sm"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://ae759c2c0c49.ngrok.io/sys_img/searchIcon.png"
              },
              {
                "type": "text",
                "text": "藥局名稱",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "icon",
            "size": "lg",
            "position": "relative",
            "offsetTop": "4px",
            "offsetStart": "25px",
            "url": "https://ae759c2c0c49.ngrok.io/sys_img/linkIcon.png"
          },
          {
            "type": "text",
            "text": "立即前往",
            "gravity": "center",
            "weight": "regular",
            "align": "center"
          }
        ],
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "http://www.facebook.com/"
        }
      },
      "styles": {
        "body": {
          "separator": False
        },
        "footer": {
          "separator": True
        }
      }
    }
  ]
}

def setAndGetPharmacyFlex():
    # get phgarmacy info from db
    flex=deepcopy(pharmacyInfoFlex)
    pharmPicUrl=getPicUrl('pharminfo_pic_url')
    pharmFBPicUrl=getPicUrl('fbinfo_pic_url')
    pharmLinePicUrl=getPicUrl('lineinfo_pic_url')
    #pharmFBUrl=None
    pharmFBUrl="https://www.facebook.com"
    pharmName="樂森藥局"
    pharmNumber="06-2600000"
    pharmAddress="台南市東區123巷123號"
    pharmLineId='@tsx6095n'

    flex["contents"][0]["hero"]["url"]=pharmPicUrl
    flex["contents"][0]["body"]["contents"][0]["text"]=pharmName
    flex["contents"][0]["body"]["contents"][1]["contents"][0]["text"]="電話："+pharmNumber
    flex["contents"][0]["body"]["contents"][2]["contents"][0]["text"]="地址："+pharmAddress
    flex["contents"][0]["footer"]["contents"][0]["url"]=getPicUrl('phone_icon_url')
    flex["contents"][0]["footer"]["action"]["text"]="請撥打 藥局名稱： "+pharmNumber

    if(pharmFBUrl==None):
        del flex["contents"][2]
    else:
        flex["contents"][2]["hero"]["url"]=pharmFBPicUrl
        flex["contents"][2]["body"]["contents"][0]["text"]=pharmName+"FB粉專"
        flex["contents"][2]["body"]["contents"][1]["contents"][0]["url"]=getPicUrl('search_icon_url')
        flex["contents"][2]["body"]["contents"][1]["contents"][1]["text"]=pharmName
        flex["contents"][2]["footer"]["contents"][0]["url"]=getPicUrl('link_icon_url')
        flex["contents"][2]["footer"]["action"]["url"]=pharmFBUrl
    
    if(pharmLineId==None):
        del flex["contents"][1]
    else:
        flex["contents"][1]["hero"]["url"]=pharmLinePicUrl
        flex["contents"][1]["body"]["contents"][0]["text"]=pharmName+"Line客服"
        flex["contents"][1]["body"]["contents"][1]["contents"][0]["text"]="ID: "+pharmLineId
        flex["contents"][1]["footer"]["contents"][0]["url"]=getPicUrl('line_icon_url')
        print(os.path.join('https://line.me/R/ti/p/',pharmLineId))
        flex["contents"][1]["footer"]["action"]["uri"]='https://line.me/R/ti/p/{LINE_id}'.format(LINE_id=pharmLineId)

    return FlexSendMessage(alt_text='Flex send failed',contents=flex) 
