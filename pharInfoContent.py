#imgUrl: 
#imgUrl: 
def returnPharmInfo():
    content={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://python123bot.herokuapp.com/sys_img/pharmInfo.png",
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
            "text": "亮亮藥局",
            "weight": "bold",
            "size": "md",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "size": "xs",
                "margin": "md",
                "flex": 0,
                "text": "電話：0900-000-000"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "地址：台南市東區xxx路xxx號",
                "wrap": True,
                "size": "xs",
                "flex": 5
              }
            ]
          }
        ],
        "spacing": "xs",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "撥打電話",
            "align": "center"
          }
        ],
        "action": {
          "type": "message",
          "label": "action",
          "text": "撥打電話"
        }
      },
      "styles": {
        "body": {
          "separator": True
        },
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://python123bot.herokuapp.com/sys_img/fbInfo.png",
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
            "text": "亮亮藥局fb粉專",
            "weight": "bold",
            "size": "md",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "地址：台南市東區xxx路xxx號",
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
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "立即前往",
            "align": "center"
          }
        ],
        "action": {
          "type": "message",
          "label": "action",
          "text": "立即前往"
        }
      },
      "styles": {
        "body": {
          "separator": True
        },
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip12.jpg",
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
            "text": "Tata",
            "weight": "bold",
            "size": "sm"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
              },
              {
                "type": "text",
                "text": "4.0",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
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
                    "text": "東京旅行",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    }
  ]
}
    return content