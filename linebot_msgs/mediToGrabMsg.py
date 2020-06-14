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


def replyDateSearch(pickMediDate):
    searchResults=[]
    '''get patient name, gender, and date to pick up medi'''
    for mediDate in pickMediDate:
      flex=deepcopy(dateToPickFlex)
      name=mediDate["userName"]
      dayStart=mediDate["dayStart"]
      weekDayStart=getContents.getWeekDay(mediDate["weekDayStart"])
      dayEnd=mediDate["dayEnd"]
      weekDayEnd=getContents.getWeekDay(mediDate["weekDayEnd"])  
    ###put the string in config, replace character when read xxxx??
      msg='領藥人： '+name+'\n您下次的慢箋領藥時間:\n'+dayStart+weekDayStart+"~"+dayEnd+weekDayEnd+"，請攜帶健保卡前來藥局領取慢箋藥品！\n屆時也會再通知您喔！"  
      flex=deepcopy(dateToPickFlex)
      dateToPickFlex["hero"]["url"]=getContents.getPicUrl('mediDate_pic_url')
      dateToPickFlex["body"]["contents"][0]["contents"][0]["text"]=msg
      searchResults.append(FlexSendMessage(alt_text="領藥時間查詢結果", contents=dateToPickFlex))
    return  searchResults

def replyNoNeedToPick():
    msg=getContents.getTextContents('msg_contents','no_medi_to_pick')
    dateToPickFlex["hero"]["url"]=getContents.getPicUrl('mediDate_pic_url')
    dateToPickFlex["body"]["contents"][0]["contents"][0]["text"]=msg
    return  FlexSendMessage(alt_text="領藥時間查詢結果", contents=dateToPickFlex)
