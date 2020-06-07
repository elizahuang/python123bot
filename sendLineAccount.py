def sendLineAccount():
    '''抓藥局名稱、
    line帳號圖片
    藥局linebot 帳號代碼'''
    content={
    "type": "bubble",
    "hero": {
        "type": "image",
        "url": "https://python123bot.herokuapp.com/sys_img/greetingPic.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "樂森藥局",
            "weight": "bold",
            "size": "xl"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "uri",
            "label": "聯繫樂森藥局官方帳號",
            "uri": "https://line.me/R/ti/p/@tsx6095n"
            }
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "撥打電話",
            "text": "撥打電話"
            }
        }
        ],
        "flex": 0
    }
    }
    return content