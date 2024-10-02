import speech_recognition as sr

wav_num = 1
# 创建一个Recognizer对象
r = sr.Recognizer()
            #启用麦克风
mic = sr.Microphone()
print('say Something...')
with mic as source:
    #降噪
    r.adjust_for_ambient_noise(source,duration=0.2)
    audio = r.listen(source)
with open(f"00{wav_num}.wav", "wb") as f:
# #将麦克风录到的声音保存为wav文件
    f.write(audio.get_wav_data(convert_rate=16000))
    print('save successfull，识别中...')
print('录音结束，识别中...')
# with open("text.txt",'w')as file:
#     file.write(r.recognize_vosk(audio,language="zh-CN"))
print("wo:",r.recognize_google(audio,language="zh-CN"))
