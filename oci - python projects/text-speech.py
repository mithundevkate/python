from gtts import gTTS
import playsound
import os

x = ['sunny', 'sagar', 'akhil']

with open("C:\\Users\\mdevkate\\Desktop\\hindi.txt", "r", encoding="utf-8") as ins:
    array = []
    for line in ins:
        array.append(line)
tts = 'tts'
for i in range(0,len(array)):
    tts = gTTS(text= array[i], lang = 'hi')
    file1 = str("hello" + str(i) + ".mp3")
    tts.save(file1)
    playsound.playsound(file1,True)
    os.remove(file1)
