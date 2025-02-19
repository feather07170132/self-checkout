import speech_recognition as sr
import time
import threading
import re
import requests

LINE_event_name = 'LLLLLLLLLLLLLL'
LINE_key = 'KKKKKKKKKKKKKKKKKKKKKKKK'

session = requests.Session()

try:

    while True:
        r = sr.Recognizer()
        m = sr.Microphone()
        m.RATE = 44100
        m.CHUNK = 512

        print("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
            if (r.energy_threshold < 2000):
                r.energy_threshold = 2000
            print("Set minimum energy threshold to {}".format(r.energy_threshold))

            print("Say something!")
            audio = r.listen(source)
            print("Got it! Now to recognize it...")

            speechtext = r.recognize_google(audio,language='zh',show_all=True) #Load Google Speech Recognition API
            print(type(speechtext)) #dict
            if len(speechtext) == 0:
                pass
            else:
                speechtext = speechtext['alternative'][0]['transcript']
                speechtext = speechtext.replace(' ', '')
                print("You said: " + speechtext)

                if re.search('\s*開冷氣\s*',speechtext):
                    print('冷氣機已開啟')

                elif re.search('\s*關冷氣\s*',speechtext):
                    print('冷氣機已關閉')

                elif re.search('\s*開電扇\s*',speechtext):
                    print('電風扇已開啟')

                elif re.search('\s*關電扇\s*',speechtext):
                    print('電風扇已關閉')

                elif re.search('\s*開電燈\s*',speechtext):
                    print('電燈已開啟')

                elif re.search('\s*關電燈\s*',speechtext):
                    print('電燈已關閉')

                elif re.search('\s*救命\s*',speechtext):
                    print('救命訊息已發送至手機')
                    LINE_URL='https://maker.ifttt.com/trigger/' + LINE_event_name + '/with/key/' + LINE_key
                    r = session.post(LINE_URL, params={"value1":'有人喊救命',"value2":'來自家裡',"value3":'JACK'})
                    
                elif re.search('\s*結束程式\s*',speechtext):
                    print('結束程式運作')
                    break
                    
except KeyboardInterrupt:
    print("Quit")



