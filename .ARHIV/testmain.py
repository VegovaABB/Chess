import FEnotation
import coords
import stockfish_wrapper
import stockfish_wrapper2
import CheckCoords
import socket
import time
import random
import pogled
import MoveFrom2FENs

prev = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

while True:

    x = input("Naprej? (y/n)  ")

    output = ""
    zeros = 0

    if x == "y":
        BnW = pogled.get_fen_from_pic()
        counter = 0
        temp = ""
        for i in prev:
            if i.isalpha() != True and i != "/" and i != "0":
                for j in range(int(i)):
                    temp +="0"
            else: 
                temp += i

        prev = temp        
        temp = ""
        for i in BnW:
            if i.isalpha() != True and i != "/" and i != "0":
                for j in range(int(i)):
                    temp +="0"
            else: 
                temp += i
        BnW=temp
        

        print(MoveFrom2FENs.get_move(prev, BnW))
        prev = FEnotation.get_fen(prev, BnW)


    
