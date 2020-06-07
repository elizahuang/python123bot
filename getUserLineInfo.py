import requests, configparser, codecs, json

config=configparser.ConfigParser();
config.read_file(codecs.open("config.ini", "r", "utf8"))

def get_save_userInfo(current_user_id,channel_access_token):
    userInfoUrl='https://api.line.me/v2/bot/profile/{userId}'.format(userId=current_user_id)
    headers = {'Authorization' : 'Bearer {botToken}'.format(botToken=channel_access_token)}
    userInfo=requests.get(userInfoUrl,headers=headers).content #the result turn out to be a byte object 
    userInfo=userInfo.decode('ASCII') #convert the byte object into string`,the result will be a string dictionary
    userInfo=json.loads(userInfo) #convert the string dictionary into python dict
   
    userId=userInfo['userId']
    line_displayName=userInfo['displayName']
    linePersonPic=requests.get(userInfo['pictureUrl']).content
    userLanguage=userInfo['language']
    print(userId)
    print(line_displayName)
    with open('myPic.png', 'wb+') as fd:
     fd.write(linePersonPic)
    print(userLanguage)

    print('save the above contents into database')
    '''save the above contents into database'''

#userid='U36ae4132a3e2709192e0b635596435b3'
#get_save_userInfo(userid)