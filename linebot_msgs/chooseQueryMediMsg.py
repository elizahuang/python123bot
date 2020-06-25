from copy import deepcopy
from linebot.models import FlexSendMessage
from getContents import *

postChoiceCarousel={
  "type": "carousel",
  "contents": [
      #add bubbles
  ]
}

queryMedTimeBubble={
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
            #add patient name text and symptom buttons
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

queryBubbleName={
        "type": "text",
        "text": "patient name",
        "align": "center",
        "size": "lg",
        "weight": "bold"
      }

queryMedTimeButton= {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
              "type": "postback",
              "label": "xxxxxxxxxxxxxxxxxxxx",
              "data": "recordQuestion=其他問題"
            }
          }

postBackData={
    "type":"choosePost",
    "posts":[]
}

def getMediQueryCarousel(allQueryData):
    queryMedTimeCarousel=deepcopy(postChoiceCarousel)
    nameList=[] #list that save patient names iof this lineid
    sortedPostsFromName=[] 
    toAppendBubbleList=[] #bubbles to be append to the carousel
    toAppendNameText=[] #dicts
    for data in allQueryData:
        if(not(data["userName"]in nameList)):
            nameList.append(data["userName"])
            singleMedTimeBubble=deepcopy(queryMedTimeBubble) #make enough amount of  empty bubbles in the carousel 
            singleMedTimeBubble["hero"]["url"]=getPicUrl('mediDate_pic_url')
            toAppendBubbleList.append(singleMedTimeBubble)
            singleBubbleNameText=deepcopy(queryBubbleName)
            singleBubbleNameText["text"]=data["userName"]
            toAppendNameText.append(singleBubbleNameText)

    for name in nameList :
      sortedPost=[]
      for data in allQueryData:
        if (data["userName"]==name):
            sortedPost.append(data)
      sortedPostsFromName.append(sortedPost)

    
    for index in range(len(nameList)):
        symptomList=[]
        allSymptomDataSorted=[]
        for post in sortedPostsFromName[index]:
          if(not(post["symptom"] in symptomList)):
            symptomList.append(post["symptom"])
        for symptom in symptomList:
          singleSymptomData=[]
          for data in sortedPostsFromName[index]:
            if (symptom==data["symptom"]):
              singleSymptomData.append(data)
          allSymptomDataSorted.append(singleSymptomData)
        dataAppendToBody=[]
        dataAppendToBody.append(toAppendNameText[index])
        for i in range(len(symptomList)):
          button=deepcopy(queryMedTimeButton)
          button["action"]["label"]=symptomList[i]
          postData=deepcopy(postBackData)
          postData["posts"]=allSymptomDataSorted[i]
          button["action"]["data"]=json.dumps(postData)
          dataAppendToBody.append(button)
        toAppendBubbleList[index]["body"]["contents"]=dataAppendToBody
    queryMedTimeCarousel["contents"]=toAppendBubbleList
    #print('flex\nflex\nflex\nflex\n')
    #print(json.dumps(queryMedTimeCarousel, indent=4, sort_keys=False))    

    return FlexSendMessage(alt_text='請選擇想查詢的藥單',contents=queryMedTimeCarousel)

