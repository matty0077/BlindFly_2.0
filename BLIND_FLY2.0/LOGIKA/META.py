import time
import threading
import pygame

##SOUNDFX PATH VARIABLE
FXPATH="/home/pi/Desktop/BLIND_FLY2.0/LOGIKA/FX/"
    
#////////////////////////////////soundfx
def soundplay(folder, fx, vol):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(vol)#put above?
    pygame.mixer.music.load(FXPATH + folder +'/' + fx + ".wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy==True:
        continue
    ##EX
    ###soundplay("misc","xdie",1.0)
    ##the volume goes from 0.0 lowest to 1.0 max

######################SHUTDOWN MACHINE
def ShutDown():
    import os
    soundplay("meta","shut_off",.7)
    time.sleep(1)
    os.system("sudo shutdown now -P")
