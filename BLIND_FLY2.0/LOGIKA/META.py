import time
import threading
import pygame
'''#speech
import cgi,os,cgitb,sys
cgitb.enable()
import subprocess
ENG='sudo espeak "{0}"'#scottish en-sc
ACCENT=ENG'''

FXPATH="/home/pi/Desktop/BLIND_FLY2.0/LOGIKA/FX/"
#//////////////////////threader
def Threader(action):
    THREAD=threading.Thread(target=action)
    #Thread.daemon=True
    THREAD.start()
    #THREAD.join()#optional?
    
#////////////////////////////////soundfx
def soundplay(folder, fx, vol):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(vol)#put above?
    pygame.mixer.music.load(FXPATH + folder +'/' + fx + ".wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy==True:
        continue

######################SHUTDOWN MACHINE
def ShutDown():
    import os
    soundplay("meta","shut_off",.7)
    time.sleep(1)
    os.system("sudo shutdown now -P")


#soundplay("misc","xdie",1.0)
#time.sleep(1)
#soundplay("misc","xdie",.2)

'''#/////////////////////////speak message
def say(something):
    try:
        os.system(ACCENT.format(something))
    except Exception as e:#-vaf,-vhi
        print(e)'''
