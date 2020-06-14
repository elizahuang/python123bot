import os, configparser,codecs,requests
from dotenv import load_dotenv
from pathlib import Path
import json

config=configparser.ConfigParser()
config.read_file(codecs.open("config.ini", "r", "utf8"))

def getServerUrl():
    is_heroku=os.environ.get("IS_HEROKU",None)
    if is_heroku:
        return config.get('server_urls','heroku_server_path')
    else:
        return config.get('server_urls','local_server_path')
        
def getPicUrl(picPath):
    is_heroku=os.environ.get("IS_HEROKU",None)
    if is_heroku:
        return os.path.join(config.get('server_urls','heroku_server_path'),config.get('paths',picPath))
    else:
        return os.path.join(config.get('server_urls','local_server_path'),config.get('paths',picPath))

def getTextContents(group, index):
    return config.get(group,index)
    
def get_userInfo(current_user_id,channel_access_token):
    userInfoUrl='https://api.line.me/v2/bot/profile/{userId}'.format(userId=current_user_id)
    headers = {'Authorization' : 'Bearer {botToken}'.format(botToken=channel_access_token)}
    userInfo=requests.get(userInfoUrl,headers=headers).content #the result turn out to be a byte object 
    userInfo=userInfo.decode('ASCII') #convert the byte object into string`,the result will be a string dictionary
    userInfo=json.loads(userInfo) #convert the string dictionary into python dict
    '''
    userId=userInfo['userId']
    line_displayName=userInfo['displayName']
    linePersonPic=requests.get(userInfo['pictureUrl']).content
    userLanguage=userInfo['language']
    '''
    return userInfo
    #print(userId)
    #print(line_displayName)
    #with open('myPic.png', 'wb+') as fd:
     #fd.write(linePersonPic)
    #print(userLanguage)
    #print('save the above contents into database')
    '''save the above contents into database'''

def getWeekDay(intDay):
    weekday=""
    if(intDay==1 or intDay=='1'):
        weekday="（一）"
    elif(intDay==2 or intDay=='2'):
        weekday="（二）"
    elif(intDay==3 or intDay=='3'):
        weekday="（三）"
    elif(intDay==4 or intDay=='4'):
        weekday="（四）"
    elif(intDay==5 or intDay=='5'):
        weekday="（五）"
    elif(intDay==6 or intDay=='6'):
        weekday="（六）"
    elif(intDay==0 or intDay=='0' or intDay==7 or intDay=='7'):
        weekday="（日）"
    return weekday