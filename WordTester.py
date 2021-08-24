import speech_recognition as sr
r = sr.Recognizer()
r.pause_threshold = 0.1
r.phrase_threshold = 0.3
r.non_speaking_duration = 0.1
for x in range(0, len(sr.Microphone.list_microphone_names())):
    if "Yeti Stereo Microph" in sr.Microphone.list_microphone_names()[x]:
        mic = sr.Microphone(device_index=x)
        break
    
while(True):
    with mic as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            pass
