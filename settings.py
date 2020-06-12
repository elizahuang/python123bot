from linebot import(LineBotApi, WebhookHandler)
import os
from pathlib import Path
from dotenv import load_dotenv

'''Initialize channel access token and channel secret'''
is_heroku=os.environ.get("IS_HEROKU",None)
if is_heroku:
    channel_access_token=os.environ.get("CHANNEL_ACCESS_TOKEN",None)
    channel_secret=os.environ.get("CHANNEL_SECRET",None)
else:
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    channel_access_token=os.getenv("CHANNEL_ACCESS_TOKEN",None)
    channel_secret=os.getenv("CHANNEL_SECRET",None)


line_bot_api=LineBotApi(channel_access_token)
handler=WebhookHandler(channel_secret)
headers = {'Authorization' : 'Bearer {botToken}'.format(botToken=channel_access_token)}