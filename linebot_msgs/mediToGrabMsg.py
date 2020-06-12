from copy import deepcopy
from linebot.models import FlexSendMessage
import getContents

dateToPickFlex={
  "type": "bubble",
  "size": "kilo",
  "hero": {
    "type": "image",
    "url": "https://python123bot.herokuapp.com/sys_img/dateForMedi.png",
    "size": "full",
    "aspectMode": "cover",
    "aspectRatio": "320:213"
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


def replyDateSearch(userId):
    searchResults=[]
    '''get patient name, gender, and date to pick up medi'''
    
    name='123'
    gender="female"
    dateToGrab='5/4(一) ~ 5/13(三)'
        
    ###put the string in config, replace character when read xxxx??
    msg=name+'您下次的慢箋領藥時間:\n'+dateToGrab+"，請攜帶健保卡前來藥局領取慢箋藥品！屆時也會再通知您喔！"  
    
    #when there is no results
    flex=deepcopy(dateToPickFlex)
    msg=getContents.getTextContents('msg_contents','no_medi_to_pick')
    dateToPickFlex["hero"]["url"]=getContents.getPicUrl('mediDate_pic_url')
    dateToPickFlex["body"]["contents"][0]["contents"][0]["text"]=msg
    searchResults.append(FlexSendMessage(alt_text="領藥時間查詢結果", contents=dateToPickFlex))
    return  searchResults
