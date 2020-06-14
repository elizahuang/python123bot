from copy import deepcopy
from linebot.models import FlexSendMessage
import getContents
otherFuncFlex={
  "type": "bubble",
  "size": "kilo",
  "hero": {
    "type": "image",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://ae759c2c0c49.ngrok.io/sys_img/otherFuncPic.png"
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
          "type": "uri",
          "label": "聊天機器人使用說明",
          "uri": "https://linecorp.com"
        }
      }
    ],
    "flex": 0
  }
}
def sendOtherFuncMsg():
    flex=deepcopy(otherFuncFlex)
    flex["hero"]["url"]=getContents.getPicUrl('other_func_pic_url')
    #flex["footer"]["contents"][0]["uri"]=
    return FlexSendMessage(alt_text="其他功能", contents=flex)