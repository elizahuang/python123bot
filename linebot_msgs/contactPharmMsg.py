import os,urllib.parse,requests,json
from linebot.models import FlexSendMessage,TextSendMessage
from getContents import getPicUrl,getTextContents,config
from settings import backendUrl
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

#send pharmacy info without undo button
def contactPharmMsg(user_lineId):
      infoObjs=[]
      #user_lineId='321'
      path=urllib.parse.urljoin('phInfo/',user_lineId)
      phInfo=requests.get(urllib.parse.urljoin(backendUrl,path)).content
      phInfo=json.loads(phInfo)
      if (len(phInfo)!=0):
        for singlePharm in phInfo:
          infoObjs.append(singlePharmMsg(singlePharm))
        return infoObjs
      else: 
        return TextSendMessage(text='很抱歉，查無藥局資訊')
def singlePharmMsg(singlePharm):
    print(singlePharm)
    pharmName=singlePharm['phName']
    pharmNumber=singlePharm['phTel']
    pharmAddress=singlePharm['phAdd']
    pharmLineId=singlePharm['LineID']

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


contactPharmFlexWithUndo={
  "type": "bubble",
  "size": "kilo",
  "hero": {
    "type": "image",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://4955723e3c74.ngrok.io/sys_img/contactPharm.png"
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
            "type": "text",
            "text": "按錯了 重新發送領藥提醒",
            "align": "center"
          }
        ],
        "action": {
          "type": "postback",
          "label": "action",
          "data": "resendReminderFlex"
        }
      },
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

def sendcontactPharmWithUndo(jsonData):
  flex=deepcopy(contactPharmFlexWithUndo)
  path=urllib.parse.urljoin(config.get('server_urls','backend_url'),"postPh/")
  print("pharName")
  print(jsonData)
  search=jsonData["pharName"]#'小光藥局'
  print(urllib.parse.urljoin(path,search))
  data=requests.get(urllib.parse.urljoin(path,search)).content
  data=json.loads(data)
  data=data[0]
  print(data)
  
  phName=jsonData["pharName"]#data["phName"]
  phTel=data["phTel"]
  phAdd=data["phAdd"]

  flex["body"]["contents"][0]["text"]=phName
  flex["body"]["contents"][1]["contents"][0]["contents"][0]["text"]=phTel
  flex["body"]["contents"][1]["contents"][0]["contents"][1]["text"]=phAdd
  
  dataToSend={
    "type":"resendReminderFlex",
    "data":""
  }
  dataToSend["data"]=jsonData
  dataToSend=json.dumps(dataToSend)
  flex["footer"]["contents"][0]["action"]["data"]=dataToSend
  flex["hero"]["url"]=getPicUrl('contactPharm_pic_url')
  return FlexSendMessage(alt_text='聯繫藥局詢問',contents=flex)
