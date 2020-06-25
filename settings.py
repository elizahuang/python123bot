from linebot import(LineBotApi, WebhookHandler)
import os
from pathlib import Path
from dotenv import load_dotenv
from getContents import getTextContents

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify


'''Initialize channel access token and channel secret'''
is_heroku=os.environ.get("IS_HEROKU",None)
if is_heroku:
    channel_access_token=os.environ.get("CHANNEL_ACCESS_TOKEN",None)
    channel_secret=os.environ.get("CHANNEL_SECRET",None)
    db_url=os.environ.get("DB_URL",None)
else:
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    channel_access_token=os.getenv("CHANNEL_ACCESS_TOKEN",None)
    channel_secret=os.getenv("CHANNEL_SECRET",None)
    db_url=os.getenv("DB_URL",None)

line_bot_api=LineBotApi(channel_access_token)
handler=WebhookHandler(channel_secret)
headers = {'Authorization' : 'Bearer {botToken}'.format(botToken=channel_access_token)}
headers_to_db={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
backendUrl=getTextContents('server_urls','backend_url')

