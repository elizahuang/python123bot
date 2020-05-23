# haven't debug 
import requests, configparser, os, codecs, json

menuId="123"
config=configparser.ConfigParser()
config.read_file(codecs.open("config.ini", "r", "utf8"))

def createRichMenu():
    pwd=config.get('line-bot','channel_access_token')
    url='https://api.line.me/v2/bot/richmenu'
    headers={
        "authorization":'Bearer '+pwd,
        "content-type":"application/json"
    }
    #fileDir = os.path.dirname(os.path.realpath('__file__'))
    #f=open(fileDir+"/json_files/createRichMenu.json","r",encoding="utf-8")
    #body=json.load(f)
    body={
        "size": {
        "width": 1257,
        "height": 424
        },
        "selected": True,
        "name": "Nice richmenu",
        "chatBarText": "點此開啟服務選單",
        "areas":[
            {
                "bounds":{
                    "x":0,
                    "y":0,
                    "width":419,
                    "height":424
                },
                "action":{
                    "type":"message",
                    "label":"pharmacyInfo",
                    "text":"藥局資訊"
                }
            },
            {
                "bounds":{
                    "x":419,
                    "y":0,
                    "width":419,
                    "height":424
                },
                "action":{
                    "type":"message",
                    "label":"dateToPickDrug",
                    "text":"領藥日查詢"
                }
            },
            {
                "bounds":{
                    "x":838,
                    "y":0,
                    "width":419,
                    "height":424
                },
                "action":{
                    "type":"message",
                    "label":"askAboutDrug",
                    "text":"用藥問題"
                }
            }            
        ]
    }
    menuId=requests.post(url, headers=headers, json=body).json()['richMenuId']
    #f.close()    
    return menuId

def uploadRichMenuImg():
    print(menuId)
    pwd=config.get('line-bot','channel_access_token')
    url='https://api.line.me/v2/bot/richmenu/{targetMenuId}/content'.format(targetMenuId=menuId)
    headers={
        "authorization":'Bearer '+pwd,
        'ontent-Type': 'image\png'
    }
    
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    
    #with open(fileDir+'\\sys_img\\richMenuPic.png', 'rb')as rd:
    #            data=rd.read()
    files = {'media': open(fileDir+'\\sys_img\\richMenuPic.png', 'rb')}
    response=requests.post(url, headers=headers,files=files)
    print(response)

def linkMenuToAllUser():
    print(menuId)
    pwd=config.get('line-bot','channel_access_token')
    url='https://api.line.me/v2/bot/user/all/richmenu/{targetMenuId}'.format(targetMenuId=menuId)
    headers={
        "authorization":'Bearer '+pwd,
        "content-type":"application/json"
    }
    response=requests.post(url,headers=headers)
    print(response)


menuId=createRichMenu()
uploadRichMenuImg()
linkMenuToAllUser()
