from copy import deepcopy
from linebot.models import FlexSendMessage
import getContents

mediQuestionflex={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "kilo",
      "hero": {
        "type": "image",
        "url": "https://ae759c2c0c49.ngrok.io/sys_img/oftenAskedQuestion.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
              "type": "postback",
              "label": "服藥方式",
              "data": "recordQuestion=服藥方式"
            }
          },
          {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
              "type": "postback",
              "label": "藥物副作用",
              "data": "recordQuestion=藥物副作用"
            }
          },
          {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
              "type": "postback",
              "label": "藥物交互作用",
              "data": "recordQuestion=藥物交互作用"
            }
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
    },
    {
      "type": "bubble",
      "size": "kilo",
      "hero": {
        "type": "image",
        "url": "https://ae759c2c0c49.ngrok.io/sys_img/oftenAskedQuestion.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
              "type": "postback",
              "label": "藥物保存方式",
              "data": "recordQuestion=藥物保存方式"
            }
          },
          {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
              "type": "postback",
              "label": "其他問題",
              "data": "recordQuestion=其他問題"
            }
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
  ]
}

def mediQuestions():
    mediQuestionflex["contents"][0]["hero"]["url"]=getContents.getPicUrl('mediQuestion_pic_url')
    mediQuestionflex["contents"][1]["hero"]["url"]=getContents.getPicUrl('mediQuestion_pic_url')
    return FlexSendMessage(alt_text="選擇問題類型", contents=mediQuestionflex)

