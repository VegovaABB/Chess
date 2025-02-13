squares = {
        "a8": "1", "a7": "9" , "a6": "17", "a5": "25", "a4": "33", "a3": "41", "a2": "49", "a1": "57", 
        "b8": "2", "b7": "10", "b6": "18", "b5": "26", "b4": "34", "b3": "42", "b2": "50", "b1": "58", 
        "c8": "3", "c7": "11", "c6": "19", "c5": "27", "c4": "35", "c3": "43", "c2": "51", "c1": "59", 
        "d8": "4", "d7": "12", "d6": "20", "d5": "28", "d4": "36", "d3": "44", "d2": "52", "d1": "60", 
        "e8": "5", "e7": "13", "e6": "21", "e5": "29", "e4": "37", "e3": "45", "e2": "53", "e1": "61", 
        "f8": "6", "f7": "14", "f6": "22", "f5": "30", "f4": "38", "f3": "46", "f2": "54", "f1": "62", 
        "g8": "7", "g7": "15", "g6": "23", "g5": "31", "g4": "39", "g3": "47", "g2": "55", "g1": "63", 
        "h8": "8", "h7": "16", "h6": "24", "h5": "32", "h4": "40", "h3": "48", "h2": "56", "h1": "64",     
    } #Ta dict nam ko mu damo polje povee njegovo mesto v arrayu povecano za 1. Zakaj povecano za 1? \_(*-*)_/

def check_square(fen, square): #Pričakuje FEN ki ima notri števila namesto ničel (!!)

    temp1 = ""

    for i in fen: #Iz FEN-a odstrani ničle
        if i.isalpha() == True:
            temp1+=i
        elif i.isnumeric()== True:
            for i in range(int(i)):
                temp1+="0"

    return temp1[int(squares[square])-1]!="0" #-1 ker se zacne pri 0 ns dictionary pa zacne pri 1


def Piece_height(fen, square): #Pričakuje FEN z števili namesto ničel

    temp1 = ""
    
    for i in fen:
        if i.isalpha() == True:
            temp1+=i
        elif i.isnumeric()== True:
            for i in range(int(i)):
                temp1+="0"

    if temp1[int(squares[square])-1].lower() == "q" or temp1[int(squares[square])-1].lower() == "k": #Za kralja in kraljico se spusti 120mm
        return "120"
    elif temp1[int(squares[square])-1].lower() == "b" or temp1[int(squares[square])-1].lower() == "n" or temp1[int(squares[square])-1].lower() == "r": #Za konja, trdnjavo in tekača se susti 140mm

        return "140"
    
    else: #Za vse ostale se spusti 164mm

        return "164"

def change_fen(move, fen): #Pričakuje FEN z števili namesto ničel
    start = move[:2]
    end = move[2:]
    temp1 = ""
    for i in fen: #Doda ničle
        if i.isalpha() == True:
            temp1+=i
        elif i.isnumeric()== True:
            for i in range(int(i)):
                temp1+="0"

    fen = temp1[:64]

    fen = list(fen)
    fen[(int(squares[end])-1)] = fen[(int(squares[start])-1)] #Na končno mesto da figuro iz začetka
    fen[(int(squares[start])-1)] = "0" #Začetno mesto nastavi na prazno polje

    out = ""
    counter = 1
    for i in fen: #Doda /
        out += i
        if counter == 8:
            counter = 0
            out += "/"
        counter += 1
    
    out = out[:71]
    zeros = 0

    finalout = ""

    for i in out: #Iz zaporedja ničel da v FEN številke
        if i != "0":
            if zeros != 0:
                finalout += str(zeros)
            zeros = 0
            finalout+=i
        else:
            zeros += 1

    return finalout

#print(change_fen("e2e4", "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"))

def kera_figura(fen, square): #Pričakuje FEN ki ima notri števila namesto ničel (!!)

    temp1 = ""

    for i in fen: #Iz FEN-a odstrani ničle
        if i.isalpha() == True:
            temp1+=i
        elif i.isnumeric()== True:
            for i in range(int(i)):
                temp1+="0"

    return temp1[int(squares[square])-1] #-1 ker se zacne pri 0 ns dictionary pa zacne pri 1

    
