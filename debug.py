import Graphics
import RokeActions
import cv2
import pogled
import FEnotation
import time
import mediapipe
import threading
cap = cv2.VideoCapture(1)

roke = RokeActions.Roke(cap)

rokeThread = threading.Thread(target=roke.rokeVnSekud, args=[5,]).start()

prev="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
player_move=True
while player_move:
    prevprev=prev
    while roke.getStatus() != False: # dokler roke ne pridejo v kader
        pass
    print("rokice")    
    while roke.getStatus() != True: # dokler roke ne grejo iz kAdra
        pass
    print("ni rokic :(")
    time.sleep(0.5)
    BnW = pogled.get_fen_from_pic(cap) #iz slike vidi ali so polja prazna, ali imajo črne ali bele igure
    print(BnW)
    prev = FEnotation.get_fen(prevprev, BnW) #Na podlagi tega ali so polja prazna in barv figur na njih nam pove katera figura je kje
    print("Prev:", prev)
    if prev!='':
        prevprev=prev
        Graphics.see_board(prev)
