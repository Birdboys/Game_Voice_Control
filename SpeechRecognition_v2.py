from pynput.keyboard import Key, Controller
from pynput.mouse import Button
from pynput.mouse import Controller as Mouse
import time
import speech_recognition as sr
from playsound import playsound
#Variables

Dva = ["fly", "rocket", "self-destruct", "matrix"]
Orisa = ["gold", "block", "bongo", "yoink"]
Rein = ["advance", "firestrike", "shatter", "shield"]
Hog = ["grab", "juice", "hog"]
Sigma = ["suck", "rock", "lyft"]
Winston = ["jump", "bubble", "rage"]
Ball = ["ball", "shield", "mines"]
Zarya = ["self", "projected", "surge"]
Ashe = ["coach", "dynamite", "bob"]
Bastion = ["century", "null", "tank"]
Doomfist = ["uppercut", "slam", "meteor"]
Echo = ["flight", "beam", "transform"]
Genji = ["dash", "reflect", "blade"]
Hanzo = ["sonar", "storm", "dragon"]
Junkrat = ["mine", "trap", "tire"]
McCree = ["roll", "flash", "high noon"]
Mei = ["ice", "wall", "blizzard"]
Pharah = ["jet", "concussive", "barrage"]
Reaper = ["disappear", "teleport", "blossom"]
Soldier = ["sprint", "heal", "visor"]
Sombra = ["stealth", "teleport", "emp"]
Symmetra = ["baby", "teleporter", "wall"]
Torbjorn = ["baby", "overload", "come"]
Tracer = ["blink", "recall", "pulse"]
Widowmaker = ["grapple", "mine", "sight"]
Ana = ["sleep", "made", "nano"]
Baptiste = ["heal", "lamp", "window"]
Brig = ["whip", "pack", "rally"]
Lucio = ["fade", "amplify", "barrier"]
Mercy = ["angel", "resurrect", "valkyrie"]
Moira = ["disappear", "ball", "coalescence"]
Zenyatta = ["harmony", "discord", "transcendence"]

Dva_Keys = [Key.shift, "e", "q", Button.right, 1, 1, 1, 0]
Orisa = [Key.shift, "e", "q", Button.right, 1, 1, 1, 1]
Rein = [Key.shift, "e", "q", Button.right, 1, 1, 1, 1]
Hog
Sigma
Winston
Ball
Zarya 
Ashe
Bastion
Doomfist
Echo
Genji
Hanzo
Junkrat
McCree
Mei
Pharah
Reaper
Soldier
Sombra
Symmetra
Torbjorn
Tracer
Widowmaker
Ana
Baptiste
Brig
Lucio
Mercy
Moira
Zenyatta


Characters = [Dva, Orisa, Rein, Hog, Sigma, Winston, Ball, Zarya, Ashe, Bastion, Doomfist, Echo,
              Genji, Hanzo, Junkrat, McCree, Mei, Pharah, Reaper, Soldier, Sombra, Symmetra, Torbjorn,
              Tracer, Widowmaker, Ana, Baptiste, Brig, Lucio, Mercy, Moira, Zenyatta]

#Setting up speech recognition                             
keyboard = Controller()
mouse = Mouse()



#Function definitions

def abilities(char_words, keys):

    keyboard = Controller()
    mouse = Mouse()


    r = sr.Recognizer()
    r.pause_threshold = 0
    r.phrase_threshold = 0.3
    r.non_speaking_duration = 0
    for x in range(0, len(sr.Microphone.list_microphone_names())):
        if "Yeti" in sr.Microphone.list_microphone_names()[x]:
            mic = sr.Microphone(device_index=x)
            break


    while(True):
        with mic as source:
        
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text = text.lower()

            for y in range(0, len(char_words)):
                if char_words[y] in text:
                    keyboard.press(keys[y])
                    keyboard.release(keys[y])

            if text == "stop":
                return
        except:
            continue

def getCharacter():
    characters = ['diva', 'orisa', 'reinhardt', 'roadhog', 'sigma', 'winston', 'wrecking ball', 'zaria',
                  'ash', 'bastion', 'doomfist', 'echo', 'genji', 'hanzo', 'junkrat', 'mccree', 'mets',
                  'farah', 'reaper', 'soldier', 'sombra', 'symmetra', 'torbjorn', 'tracer', 'widowmaker',
                  'anna', 'baptiste', 'brig', 'lucio', 'mercy', 'moira', 'zenyatta']
    keyboard = Controller()
    mouse = Mouse()


    r = sr.Recognizer()
    r.pause_threshold = 0.05
    r.phrase_threshold = 0.3
    r.non_speaking_duration = 0.05
    for x in range(0, len(sr.Microphone.list_microphone_names())):
        if "Yeti" in sr.Microphone.list_microphone_names()[x]:
            mic = sr.Microphone(device_index=x)
            break

    while(True):
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio).lower()

            for y in range(0, len(characters)):
                if text == characters[y]:
                    return y
        except:
            pass

def startUp():
    print("Say the name of the character you wan't to play")
    character_names = ["D.Va", "Orisa", "Reinhardt", "Roadhog", "Sigma", "Winston", "Wrecking Ball", "Zarya", "Ashe",
                       "Bastion", "Doomfist", "Echo", "Genji", "Hanzo", "Junkrat", "McCree", "Mei", "Pharah", "Reaper",
                       "Soldier", "Sombra", "Symmetra", "Torbjorn", "Tracer", "Widowmaker", "Ana", "Baptiste", "Brigitte",
                       "Lucio", "Mercy", "Moira", "Zenyatta"]
    while(True):
        num = getCharacter()
        if num < 0 or num >= 32:
            print("Invalid character, try again")
        else:
            audio = "C:\\Users\\colby\\OneDrive\\Desktop\\Code_Stuff\\Overwatch Voice Control\\Voice_Lines\\" + character_names[num] + ".wav"
            playsound(audio)
            print("Hero selected. Have fun!")
            return num
    

#Getting character keywords

while(True):
    playsound("C:\\Users\\colby\\OneDrive\\Desktop\\Code_Stuff\\Overwatch Voice Control\\Voice_Lines\\Select.wav")
    char_num = startUp()
    char_words = Characters[char_num]
    print(char_words)
    keys = [Key.shift, "e", "q"]
    abilities(char_words, keys)

    

#keyboard.press('e')
#keyboard.release('e')

