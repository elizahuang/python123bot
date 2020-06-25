import os
from linebot.models import (TextSendMessage, ImageSendMessage, FlexSendMessage,MessageAction,QuickReply,QuickReplyButton)
from getContents import getPicUrl,getTextContents
from copy import deepcopy

pharmacyInfoFlex={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "kilo",
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
            "offsetStart": "65px",
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
      "size": "kilo",
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
            "offsetTop": "3px",
            "offsetStart": "64px",
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
      "size": "kilo",
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
            "offsetTop": "3px",
            "offsetStart": "72px",
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

def setAndGetPharmacyFlex(phInfo):
    # get phgarmacy info from db
    phInfoList=[]
    showList=[]
    for info in phInfo:
      if (not(info["phName"] in showList)):
        showList.append(info["phName"])
        phInfoList.append(setSinglePharmFlex(info))
    return phInfoList
def setSinglePharmFlex(singleInfo):  
    flex=deepcopy(pharmacyInfoFlex)
    pharmPicUrl=getPicUrl('pharminfo_pic_url')
    pharmFBPicUrl=getPicUrl('pharminfo_pic_url')
    pharmLinePicUrl=getPicUrl('pharminfo_pic_url')
    
    pharmFBUrl=singleInfo["WebURL"]
    pharmName=singleInfo['phName']
    pharmNumber=singleInfo['phTel']
    pharmAddress=singleInfo['phAdd']
    pharmLineId=singleInfo['LineID']
    
    flex["contents"][0]["hero"]["url"]=pharmPicUrl
    flex["contents"][0]["body"]["contents"][0]["text"]=pharmName
    flex["contents"][0]["body"]["contents"][1]["contents"][0]["text"]="電話："+pharmNumber
    flex["contents"][0]["body"]["contents"][2]["contents"][0]["contents"][0]["text"]="地址："+pharmAddress
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
        flex["contents"][2]["footer"]["action"]["uri"]=pharmFBUrl
    
    if(pharmLineId==None):
        del flex["contents"][1]
    else:
        flex["contents"][1]["hero"]["url"]=pharmLinePicUrl
        flex["contents"][1]["body"]["contents"][0]["text"]=pharmName+"Line客服"
        flex["contents"][1]["body"]["contents"][1]["contents"][0]["text"]="ID: "+pharmLineId
        flex["contents"][1]["footer"]["contents"][0]["url"]=getPicUrl('line_icon_url')
        flex["contents"][1]["footer"]["action"]["uri"]='https://line.me/R/ti/p/{LINE_id}'.format(LINE_id=pharmLineId)

    return FlexSendMessage(alt_text='藥局聯繫資訊',contents=flex) 
