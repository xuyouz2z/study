import requests
import json

TURING_KEY = "myzbaoucgx17pjlwge5fh4awt0vpnpgd"  # 这里输入你的机器人Apikey
URL = "http://openapi.tuling123.com/openapi/api/v2"
HEADERS = {"Content-Type": "application/json;charset=UTF-8"}


def robot(text=""):
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {"text": ""},
            "selfInfo": {"location": {"city": "广州", "street": "大学城"}},  # 这里输入你的城市
        },
        "userInfo": {
            "apiKey": "myzbaoucgx17pjlwge5fh4awt0vpnpgd",  # 这里输入你的机器人Apikey
            "userId": "123",
        },
    }

    data["perception"]["inputText"]["text"] = text
    response = requests.request("post", URL, json=data, headers=HEADERS)
    response_dict = json.loads(response.text)

    result = response_dict["results"][0]["values"]["text"]  # 把机器人回复的文字储存在result里
    print("the AI said: " + result)
    return result


robot("你好吗？")  # 运行robot函数，与机器人聊天
