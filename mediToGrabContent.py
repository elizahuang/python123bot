import json
#imgUrl: /sys_img/pharInfo.png
def replyDateSearch():
    '''reply when to pick up medicine from user search'''
    content={
  "type": "bubble",
  "size": "micro",
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
    '''get patient name, gender, and date to pick up medi'''
    name='梅艷芳'
    gender='female'
    dateToGrab='5/4(一) ~ 5/13(三)'
    if gender=='male':
        name+='先生: \n'
    else: name+='女士: \n'
    
    ###put the string in config, replace character when read xxxx??
    msg=name+'您的下次的慢箋領藥時間:\n'+dateToGrab+"，請攜帶健保卡前來藥局領取慢箋藥品！屆時也會再通知您喔！"  
    '''
    content is a dict, call values through the keys is the dict.
    the 2 contents are list, should be called through integer indices(index). 
    '''
    content["body"]["contents"][0]["contents"][0]["text"]=msg
    return content
