import os, configparser,codecs
from linebot.models import (TextSendMessage, ImageSendMessage, FlexSendMessage,MessageAction,QuickReply,QuickReplyButton)
from getContents import getPicUrl,getTextContents

config=configparser.ConfigParser()
config.read_file(codecs.open("config.ini", "r", "utf8"))


def sendInstrucMsg():   
    msgObjs=[]
    msgObjs.append(TextSendMessage(text=config.get('instrucMsg','auth_complete')))
    greetImgUrl=getPicUrl('greeting_pic_url')
    msgObjs.append(ImageSendMessage(
        type="image",
        original_content_url=greetImgUrl,
        preview_image_url=greetImgUrl
    ))
    msgObjs.append(TextSendMessage(
        text=config.get('instrucMsg','instruc'),
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(
                        label="跳過教學",
                        text="跳過教學")
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="好的！顯示使用說明",
                        text="好的！顯示使用說明")
                )
            ]
        )))
    return msgObjs

def replyNotNeedInstruc():
    return TextSendMessage(text=getTextContents('instrucMsg','no_need_instruc_reply'))

def replyNeedInstruc():
    msgObjs=[]
    # append an introduction picture
    msgObjs.append(TextSendMessage(text=getTextContents('instrucMsg','need_instruc_reply')))    
    return msgObjs
