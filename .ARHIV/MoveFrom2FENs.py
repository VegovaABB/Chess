squares = {
        "1": "a8",
        "2": "b8",
        "3": "c8",
        "4": "d8",
        "5": "e8",
        "6": "f8",
        "7": "g8",
        "8": "h8",

        "9": "a7",
        "10": "b7",
        "11": "c7",
        "12": "d7",
        "13": "e7",
        "14": "f7",
        "15": "g7",
        "16": "h7",

        "17": "a6",
        "18": "b6",
        "19": "c6",
        "20": "d6",
        "21": "e6",
        "22": "f6",
        "23": "g6",
        "24": "h6",

        "25": "a5",
        "26": "b5",
        "27": "c5",
        "28": "d5",
        "29": "e5",
        "30": "f5",
        "31": "g5",
        "32": "h5",

        "33": "a4",
        "34": "b4",
        "35": "c4",
        "36": "d4",
        "37": "e4",
        "38": "f4",
        "39": "g4",
        "40": "h4",

        "41": "a3", 
        "42": "b3", 
        "43": "c3", 
        "44": "d3", 
        "45": "e3", 
        "46": "f3", 
        "47": "g3", 
        "48": "h3", 

        "49": "a2", 
        "50": "b2", 
        "51": "c2", 
        "52": "d2", 
        "53": "e2", 
        "54": "f2", 
        "55": "g2", 
        "56": "h2", 

        "57": "a1",
        "58": "b1",
        "59": "c1",
        "60": "d1",
        "61": "e1",
        "62": "f1",
        "63": "g1",
        "64": "h1",

    }

def get_move(prej, potem_x):


    temp1 = ""
    temp2 = ""

    for i in prej:
        if i != "/":
            temp1 += i
    
    for i in potem_x:
        if i != "/":
            temp2 += i

    prej = temp1
    potem_x = temp2

    print(prej, potem_x)

    move=""
    


    for i in range(64):
        if prej[i] != "0" and potem_x[i]=="0":
            move = squares[str(i+1)]+move
        if (prej[i] == "0" and potem_x[i]!="0") or (prej[i].islower() == True and potem_x[i]=="w") or (prej[i].isupper() == True and potem_x[i]=="b"):
            move += squares[str(i+1)]
    return(move)

#print(get_move("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/8", "bbbbbbbb/bbbbbbbb/8/8/5w2/8/wwwww1ww/8"))