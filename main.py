import FEnotation #Ugotovi kera figura je kje na podlagi prejsnjega FEN-a in ali so polja prazna, imajo črne ali bele figure
import coords #Ti mu das polje, on ti da koordinate kamor mora robot
import stockfish_wrapper #Z njim lahko uporabljamo stockfish - da nam poteze (zahvale zhelyabuzhsky-ju)
import CheckCoords #Pove nam če je polje praznio, kako visoka je figura na njem ali pa spremeni FEN na podlagi poteze
import socket #Za socket komunikacijo
import time #Za funkcije čakanja
import pogled #S kamero pogleda ploščo in nam pove ali so polja prazna, oz. katere barve je figura na njih
import Graphics #GUI za pokazat FEN
import RokeActions, threading

HOST = "192.168.125.123" #IP od računalnika za namene socket komunikacije
PORT = 65432 #Št. porta za namene socket komunikacije 

roke = RokeActions.Roke()
rokeThread = threading.Thread(target=roke.rokeVnSekud, args=[5,])


prev = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR" #FEN začetne pozicije 
#prev = "1K2k2r/pppppppp/1q6/8/8/8/8/8"

def send_coords(c_socket, coords:list): #Roki pošlje koordinate po socketu (sprejme socket ki ga želi na clientu in pa seznam koordinat)
    c_socket.sendall(str(coords[0]).encode()) #Pošlje prvo koordinato
    time.sleep(0.1) #Delay da ni prehitro
    c_socket.sendall(str(coords[1]).encode())
    time.sleep(0.1)
    c_socket.sendall(str(coords[2]).encode())
    time.sleep(0.1)

    c_socket.sendall(str(coords[3]).encode())
    time.sleep(0.1)
    c_socket.sendall(str(coords[4]).encode())
    time.sleep(0.1)
    c_socket.sendall(str(coords[5]).encode())
    time.sleep(0.1)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

server_socket.listen(5)
print(f'Server listening on {HOST}:{PORT}')
GotMove = False #Bool če ima potezo
cords = []
konec=["E", "0", "0", "0", "0", "0"] #Te koordinate pošljemo če se igra konča

while True:
    
    client_socket, addr = server_socket.accept() #Odpre socket
    
    while True:
        
        # dobimo podatke od roke
        data = client_socket.recv(1024).decode('utf-8') # 1MB max
        if not data:
            break
        if data == "move": #Če po socketu prejmemo move, roki vrnemo potezo
            seznam_koordinat = [] #Sprazne seznam koordinat
            while roke.getStatus() != True:
                    pass

            BnW = pogled.get_fen_from_pic() #iz slike vidi ali so polja prazna, ali imajo črne ali bele igure    
            print(1)
            prev = FEnotation.get_fen(prev, BnW) #Na podlagi tega ali so polja prazna in barv figur na njih nam pove katera figura je kje

            Graphics.see_board(prev) #Poaže igro z GUI
            #poteza za stockfish
            print(prev)
            stock = stockfish_wrapper.get_move(prev + " b qk QK") 
            move, temp = stock[0],  stock[1]

            print(move, CheckCoords.kera_figura(prev, move[:2]))

            

            if CheckCoords.kera_figura(prev, move[:2]) == "k" and move[2:] == "g8": 
                
                seznam_koordinat.append(coords.get_coords(move[:2]))
                seznam_koordinat[0].append(CheckCoords.Piece_height(prev, move[:2]))
                seznam_koordinat.append(coords.get_coords(move[2:]))
                seznam_koordinat[1].append(CheckCoords.Piece_height(prev, move[2:]))

                seznam_koordinat.append(coords.get_coords("h8"))
                seznam_koordinat[2].append(CheckCoords.Piece_height(prev, "h8"))
                seznam_koordinat.append(coords.get_coords("f8"))
                seznam_koordinat[3].append(CheckCoords.Piece_height(prev, "h8"))
                
                print("castle")

            elif CheckCoords.kera_figura(prev, move[:2]) == "k" and move[2:] == "c8":
                seznam_koordinat.append(coords.get_coords(move[:2]))
                seznam_koordinat[0].append(CheckCoords.Piece_height(prev, move[:2]))
                seznam_koordinat.append(coords.get_coords(move[2:]))
                seznam_koordinat[1].append(CheckCoords.Piece_height(prev, move[2:]))

                seznam_koordinat.append(coords.get_coords("a8"))
                seznam_koordinat[2].append(CheckCoords.Piece_height(prev, "a8"))
                seznam_koordinat.append(coords.get_coords("d8"))
                seznam_koordinat[3].append(CheckCoords.Piece_height(prev, "a8"))

                print("castle")

            elif CheckCoords.check_square(prev, move[2:])!=True: #Če na cilju še ni figure oz. če roka ne rabi "jesti"
                seznam_koordinat.append(coords.get_coords(move[:2]))
                seznam_koordinat[0].append(CheckCoords.Piece_height(prev, move[:2]))
                seznam_koordinat.append(coords.get_coords(move[2:]))
                seznam_koordinat[1].append(CheckCoords.Piece_height(prev, move[2:]))

            else:
                seznam_koordinat.append(coords.get_coords(move[2:]))                     # dobimo prve koordinate (ta kmet bo pojeden)    [(x, y, 0)]
                seznam_koordinat[0].append(CheckCoords.Piece_height(prev, move[2:]))     # dobimo višino za prejšnjo potezo [(x, y, Z)]
                seznam_koordinat.append((0, 650, 0))                                     # nesemo kmeta na (0, 650, 0)
                
                seznam_koordinat.append(coords.get_coords(move[:2]))                     # dobimo koordinate kje je kmet, ki je pojedel
                seznam_koordinat[2].append(CheckCoords.Piece_height(prev, move[:2]))     # dobimo višino za prejšnjo potezo
                seznam_koordinat.append(coords.get_coords(move[2:]))                     # dobimo kam rabi ta kmet it
                seznam_koordinat[3].append(CheckCoords.Piece_height(prev, move[2:]))     # in kako visoko ga odpozimo  
            #! sez.clear()          # napaka hall of fame

            print(seznam_koordinat)
            prev = temp
            Graphics.see_board(prev)
            GotMove = True
            cords.clear()
            time.sleep(0.3)
            for i in range (0, 2): #Na coords da 1. del poteze
                cords.append(str(seznam_koordinat[0][0]))
                cords.append(str(seznam_koordinat[0][1]))
                cords.append(str(seznam_koordinat[0][2]))
                seznam_koordinat.pop(0)
        
        if data == "move2" and len(seznam_koordinat)!=0: #Move2 -> roka pričakuje 2. del poteze, če seznam koordinat ni prazen ga dodamo na cords
            cords.clear()
            for i in range (0, 2):
                cords.append(str(seznam_koordinat[0][0]))
                cords.append(str(seznam_koordinat[0][1]))
                cords.append(str(seznam_koordinat[0][2]))
                seznam_koordinat.pop(0)

        elif data == "move2" and len(seznam_koordinat)==0: #Če je seznam koordinat prazen pomeni da roka ne bo jedla in mu damo koordinate ki nakazujejo konec poteze
            cords.clear()
            for i in konec:
                cords.append(i)   

        send_coords(client_socket, cords)