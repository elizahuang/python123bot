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
        "type": "text",
        "text": "patientName: symptom",
        "size": "lg",
        "margin": "none",
        "wrap": False,
        "weight": "bold"
      }
    ],
    "spacing": "sm",
    "paddingAll": "13px"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "text",
        "text": "123",
        "wrap": True,
        "size": "md",
        "flex": 5
      }
    ]
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
      symptom=mediDate["symptom"]
      name=mediDate["userName"]
      dayStart=mediDate["dayStart"]
      dayStart=dayStart[5:]
      weekDayStart=getContents.getWeekDay(mediDate["weekDayStart"])
      dayEnd=mediDate["dayEnd"]
      dayEnd=dayEnd[5:]
      weekDayEnd=getContents.getWeekDay(mediDate["weekDayEnd"])
      print(type(dayStart))  
    ###put the string in config, replace character when read xxxx??
      dateToPickFlex["body"]["contents"][0]["text"]=name+"："+symptom
      msg='慢性處方箋領藥日:\n'+dayStart+weekDayStart+"~"+dayEnd+weekDayEnd#+"\n請攜帶健保卡前來藥局領取慢箋藥品！\n屆時也會再通知您喔！"  
      flex=deepcopy(dateToPickFlex)
      dateToPickFlex["hero"]["url"]=getContents.getPicUrl('mediDateResult_pic_url')
      dateToPickFlex["footer"]["contents"][0]["text"]=msg
      searchResults.append(FlexSendMessage(alt_text="領藥時間查詢結果", contents=dateToPickFlex))
    return  searchResults

def replyNoNeedToPick():
    msg=getContents.getTextContents('msg_contents','no_medi_to_pick')
    dateToPickFlex["hero"]["url"]=getContents.getPicUrl('mediDateResult_pic_url')
    dateToPickFlex["body"]["contents"][0]["contents"][0]["text"]=msg
    return  FlexSendMessage(alt_text="領藥時間查詢結果", contents=dateToPickFlex)
