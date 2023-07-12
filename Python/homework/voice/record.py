import speech_recognition as sr  # pyaudio SpeechRecognition模块


def rec(rate=16000):  # 从系统麦克风拾取音频数据，采样率为 16000
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("请开始说话...")
        audio = r.listen(source)

    with open(
        "homework/voice/recording.wav", "wb"
    ) as f:  # 把采集到的音频数据以 wav 格式保存在当前目录下的recording.wav 文件
        f.write(audio.get_wav_data())
    return 1


rec()  # 运行rec函数，录制音频
