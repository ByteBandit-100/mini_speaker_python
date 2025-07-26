# author = github :: ByteBandit-100
# name = Mohit
# In this program i use SAPI Win32com.client

import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print("Enter the word/sentence you want to hear from me (q for quit) : ")
    s = input()
    if s.lower() == 'q':
        break
    speaker.Speak(s)

