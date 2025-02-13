#prva stvilka gre po crkah druga pa po stevilkah

def get_coords(x): #Vrne koordinate polja

    start_coords = (50, 50) #Prilagodi po potrebi

    coords_dic = {

    "a1" : (start_coords[0]*1, start_coords[1]*1),
    "a2" : (start_coords[0]*2, start_coords[1]*1),
    "a3" : (start_coords[0]*3, start_coords[1]*1),
    "a4" : (start_coords[0]*4, start_coords[1]*1),
    "a5" : (start_coords[0]*5, start_coords[1]*1),
    "a6" : (start_coords[0]*6, start_coords[1]*1),
    "a7" : (start_coords[0]*7, start_coords[1]*1),
    "a8" : (start_coords[0]*8, start_coords[1]*1),

    "b1" : (start_coords[0]*1, start_coords[1]*2),
    "b2" : (start_coords[0]*2, start_coords[1]*2),
    "b3" : (start_coords[0]*3, start_coords[1]*2),
    "b4" : (start_coords[0]*4, start_coords[1]*2),
    "b5" : (start_coords[0]*5, start_coords[1]*2),
    "b6" : (start_coords[0]*6, start_coords[1]*2),
    "b7" : (start_coords[0]*7, start_coords[1]*2),
    "b8" : (start_coords[0]*8, start_coords[1]*2),

    "c1" : (start_coords[0]*1, start_coords[1]*3),
    "c2" : (start_coords[0]*2, start_coords[1]*3),
    "c3" : (start_coords[0]*3, start_coords[1]*3),
    "c4" : (start_coords[0]*4, start_coords[1]*3),
    "c5" : (start_coords[0]*5, start_coords[1]*3),
    "c6" : (start_coords[0]*6, start_coords[1]*3),
    "c7" : (start_coords[0]*7, start_coords[1]*3),
    "c8" : (start_coords[0]*8, start_coords[1]*3),

    "d1" : (start_coords[0]*1, start_coords[1]*4),
    "d2" : (start_coords[0]*2, start_coords[1]*4),
    "d3" : (start_coords[0]*3, start_coords[1]*4),
    "d4" : (start_coords[0]*4, start_coords[1]*4),
    "d5" : (start_coords[0]*5, start_coords[1]*4),
    "d6" : (start_coords[0]*6, start_coords[1]*4),
    "d7" : (start_coords[0]*7, start_coords[1]*4),
    "d8" : (start_coords[0]*8, start_coords[1]*4),

    "e1" : (start_coords[0]*1, start_coords[1]*5),
    "e2" : (start_coords[0]*2, start_coords[1]*5),
    "e3" : (start_coords[0]*3, start_coords[1]*5),
    "e4" : (start_coords[0]*4, start_coords[1]*5),
    "e5" : (start_coords[0]*5, start_coords[1]*5),
    "e6" : (start_coords[0]*6, start_coords[1]*5),
    "e7" : (start_coords[0]*7, start_coords[1]*5),
    "e8" : (start_coords[0]*8, start_coords[1]*5),

    "f1" : (start_coords[0]*1, start_coords[1]*6),
    "f2" : (start_coords[0]*2, start_coords[1]*6),
    "f3" : (start_coords[0]*3, start_coords[1]*6),
    "f4" : (start_coords[0]*4, start_coords[1]*6),
    "f5" : (start_coords[0]*5, start_coords[1]*6),
    "f6" : (start_coords[0]*6, start_coords[1]*6),
    "f7" : (start_coords[0]*7, start_coords[1]*6),
    "f8" : (start_coords[0]*8, start_coords[1]*6),

    "g1" : (start_coords[0]*1, start_coords[1]*7),
    "g2" : (start_coords[0]*2, start_coords[1]*7),
    "g3" : (start_coords[0]*3, start_coords[1]*7),
    "g4" : (start_coords[0]*4, start_coords[1]*7),
    "g5" : (start_coords[0]*5, start_coords[1]*7),
    "g6" : (start_coords[0]*6, start_coords[1]*7),
    "g7" : (start_coords[0]*7, start_coords[1]*7),
    "g8" : (start_coords[0]*8, start_coords[1]*7),

    "h1" : (start_coords[0]*1, start_coords[1]*8),
    "h2" : (start_coords[0]*2, start_coords[1]*8),
    "h3" : (start_coords[0]*3, start_coords[1]*8),
    "h4" : (start_coords[0]*4, start_coords[1]*8),
    "h5" : (start_coords[0]*5, start_coords[1]*8),
    "h6" : (start_coords[0]*6, start_coords[1]*8),
    "h7" : (start_coords[0]*7, start_coords[1]*8),
    "h8" : (start_coords[0]*8, start_coords[1]*8),

    }

    return [coords_dic[x][1]-50, coords_dic[x][0]-50]

#465/8