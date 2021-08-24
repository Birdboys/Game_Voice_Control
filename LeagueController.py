import os
import ctypes
from win32 import win32api, win32gui
import time
import speech_recognition as sr
import re


class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)
w = WindowMgr()

w.find_window_wildcard("League* of Legends (TM)*")    # Game window is named 'Minecraft 1.13.1' for example.
w.set_foreground()
#Variables

words = ["1", "2", "3", "4", "5", "6", "recall", "shop"]
keys = [0x10, 0x11, 0x12, 0x13, 0x20, 0x21, 0x30, 0x19]

#stuff-----------------------------------------------------------
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
   _fields_ = [("wVk", ctypes.c_ushort),
               ("wScan", ctypes.c_ushort),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
   _fields_ = [("uMsg", ctypes.c_ulong),
               ("wParamL", ctypes.c_short),
               ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
   _fields_ = [("dx", ctypes.c_long),
               ("dy", ctypes.c_long),
               ("mouseData", ctypes.c_ulong),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
   _fields_ = [("ki", KeyBdInput),
               ("mi", MouseInput),
               ("hi", HardwareInput)]


class Input(ctypes.Structure):
   _fields_ = [("type", ctypes.c_ulong),
("ii", Input_I)]

def press_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008 | 0x0002

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def team():
    press_key(0x1C) #enter
    release_key(0x1C)
    time.sleep(.15)
    press_key(0x19) #p
    release_key(0x19)
    press_key(0x18) #o
    release_key(0x18)
    press_key(0x22) #g
    release_key(0x22)
    press_key(0x22) #g
    release_key(0x22)
    press_key(0x17) #i
    release_key(0x17)
    press_key(0x12) #e
    release_key(0x12)
    press_key(0x1F) #s
    release_key(0x1F)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x14) #t
    release_key(0x14)
    press_key(0x12) #e
    release_key(0x12)
    press_key(0x1E) #a
    release_key(0x1E)
    press_key(0x32) #m
    release_key(0x32)
    press_key(0x33) #,
    release_key(0x33)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x22) #g
    release_key(0x22)
    press_key(0x13) #r
    release_key(0x13)
    press_key(0x12) #e
    release_key(0x12)
    press_key(0x1E) #a
    release_key(0x1E)
    press_key(0x14) #t
    release_key(0x14)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x19) #p
    release_key(0x19)
    press_key(0x26) #l
    release_key(0x26)
    press_key(0x1E) #a
    release_key(0x1E)
    press_key(0x15) #y
    release_key(0x15)
    
    press_key(0x1C) #enter
    release_key(0x1C)

def top_lane():
    press_key(0x1C) #enter
    release_key(0x1C)
    time.sleep(.15)
    press_key(0x18) #o
    release_key(0x18)
    press_key(0x16) #u
    release_key(0x16)
    press_key(0x13) #r
    release_key(0x13)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x14) #t
    release_key(0x14)
    press_key(0x18) #o
    release_key(0x18)
    press_key(0x19) #p
    release_key(0x19)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x26) #l
    release_key(0x26)
    press_key(0x1E) #a
    release_key(0x1E)
    press_key(0x31) #n
    release_key(0x31)
    press_key(0x12) #e
    release_key(0x12)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x17) #i
    release_key(0x17)
    press_key(0x1F) #s
    release_key(0x1F)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x22) #g
    release_key(0x22)
    press_key(0x18) #o
    release_key(0x18)
    press_key(0x17) #i
    release_key(0x17)
    press_key(0x31) #n
    release_key(0x31)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x1F) #s
    release_key(0x1F)
    press_key(0x14) #t
    release_key(0x14)
    press_key(0x17) #i
    release_key(0x17)
    press_key(0x31) #n
    release_key(0x31)
    press_key(0x25) #k
    release_key(0x25)
    press_key(0x15) #y
    release_key(0x15)
    
    press_key(0x2A) #shift
    press_key(0x01) #!
    release_key(0x01)
    release_key(0x2A)

    press_key(0x1C) #enter
    release_key(0x1C)
    
def bottom_lane():
    press_key(0x1C) #enter
    release_key(0x1C)
    time.sleep(.15)
    press_key(0x18) #o
    release_key(0x18)
    press_key(0x16) #u
    release_key(0x16)
    press_key(0x13) #r
    release_key(0x13)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x30) #b
    release_key(0x30)
    press_key(0x18) #o
    release_key(0x18)
    press_key(0x14) #t
    release_key(0x14)
    press_key(0x14) #t
    release_key(0x14)
    press_key(0x18) #o
    release_key(0x18)
    press_key(0x32) #m
    release_key(0x32)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x26) #l
    release_key(0x26)
    press_key(0x1E) #a
    release_key(0x1E)
    press_key(0x31) #n
    release_key(0x31)
    press_key(0x12) #e
    release_key(0x12)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x17) #i
    release_key(0x17)
    press_key(0x1F) #s
    release_key(0x1F)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x22) #g
    release_key(0x22)
    press_key(0x18) #o
    release_key(0x18)
    press_key(0x17) #i
    release_key(0x17)
    press_key(0x31) #n
    release_key(0x31)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x1F) #s
    release_key(0x1F)
    press_key(0x14) #t
    release_key(0x14)
    press_key(0x17) #i
    release_key(0x17)
    press_key(0x31) #n
    release_key(0x31)
    press_key(0x25) #k
    release_key(0x25)
    press_key(0x15) #y
    release_key(0x15)
    
    press_key(0x2A) #shift
    press_key(0x01) #!
    release_key(0x01)
    release_key(0x2A)

    press_key(0x1C) #enter
    release_key(0x1C)

def mid_lane():
    press_key(0x1C) #enter
    release_key(0x1C)
    time.sleep(.15)
    press_key(0x18) #o
    release_key(0x18)
    press_key(0x16) #u
    release_key(0x16)
    press_key(0x13) #r
    release_key(0x13)
    press_key(0x39) #space
    release_key(0x39)

    
    press_key(0x32) #m
    release_key(0x32)
    press_key(0x17) #i
    release_key(0x17)
    press_key(0x20) #d
    release_key(0x20)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x26) #l
    release_key(0x26)
    press_key(0x1E) #a
    release_key(0x1E)
    press_key(0x31) #n
    release_key(0x31)
    press_key(0x12) #e
    release_key(0x12)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x17) #i
    release_key(0x17)
    press_key(0x1F) #s
    release_key(0x1F)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x22) #g
    release_key(0x22)
    press_key(0x18) #o
    release_key(0x18)
    press_key(0x17) #i
    release_key(0x17)
    press_key(0x31) #n
    release_key(0x31)
    press_key(0x39) #space
    release_key(0x39)

    press_key(0x1F) #s
    release_key(0x1F)
    press_key(0x14) #t
    release_key(0x14)
    press_key(0x17) #i
    release_key(0x17)
    press_key(0x31) #n
    release_key(0x31)
    press_key(0x25) #k
    release_key(0x25)
    press_key(0x15) #y
    release_key(0x15)
    
    press_key(0x2A) #shift
    press_key(0x01) #!
    release_key(0x01)
    release_key(0x2A)

    press_key(0x1C) #enter
    release_key(0x1C)

def jg_lane():
    press_key(0x1C) #enter
    release_key(0x1C)
    time.sleep(.15)
    press_key(0x24) #j
    release_key(0x24)
    press_key(0x22) #g
    release_key(0x22)
    press_key(0x39) #space
    release_key(0x39)

    
    press_key(0x22) #g
    release_key(0x22)
    press_key(0x1E) #a
    release_key(0x1E)
    press_key(0x19) #p
    release_key(0x19)
   
    press_key(0x2A) #shift
    press_key(0x01) #!
    release_key(0x01)
    release_key(0x2A)
    press_key(0x1C) #enter
    release_key(0x1C)


#--------------------------------------------------------------------


r = sr.Recognizer()
r.pause_threshold = 0.1
r.phrase_threshold = 0.3
r.non_speaking_duration = 0.1
for x in range(0, len(sr.Microphone.list_microphone_names())):
    if "Yeti" in sr.Microphone.list_microphone_names()[x]:
        mic = sr.Microphone(device_index=x)
        break


while(True):
    with mic as source:
    

        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text = text.lower()
            text = " " + text + " "
            for y in range(0, len(words)):
                if words[y] in text:
                    press_key(keys[y])
                    release_key(keys[y])
            if "team" in text:
                team()
            if "bottom" in text or "bot" in text:
                bottom_lane()
            if "Med" in text or "middle" in text:
                mid_lane()
            if "top" in text:
                top_lane()
            if "jungle" in text:
                jg_lane()    
    

           
        except:
            continue



    

#keyboard.press('e') qwerfdp
#keyboard.release('e')

