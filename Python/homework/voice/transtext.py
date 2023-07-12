from aip import AipSpeech

APP_ID = "34143930"
API_KEY = "a4SmaFS2XEIzOrtld8Cg77N2"
SECRET_KEY = "ohuIuLdeqdFSH2jvMELAlhlnKgtH1yem"  # 接口账号密钥

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def listen():
    with open("homework/voice/recording.wav", "rb") as f:  # 将上传至百度语音的服务，返回识别后的文本结果并输出。
        audio_data = f.read()

    results = client.asr(
        audio_data,
        "wav",
        16000,
        {
            "dev_pid": 1537,  # 这里的results是一个字典，文本内容在Key名字为result对应的值，
        },
    )
    if "result" in results:
        print(
            "你说：: " + results["result"][0]
        )  # results['result']这个是输出Key名字为result对应的值，也就是我们要的文本
        return results["result"][0]
    else:
        print("出现错误，错误代码：", results["err_no"])  # 不存在result就返回错误代码err_no


listen()  # 运行listen函数，将录音转成文字
