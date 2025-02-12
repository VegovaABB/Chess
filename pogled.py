import cv2
import math
import numpy as np

def get_fen_from_pic():
    # Setup camera 
    cap = cv2.VideoCapture(0) #! adjust 
    

    x = 23
    y = 50
    counter = 1
    modra = 3

    kernel = np.ones((5, 5), np.uint8)

    # While loop 
    
        
        
    ret, frame = cap.read() 
    frame = frame[0:480, 170:520]
    #cv2.imshow("", frame)
    #cv2.waitKey(0)

    fen = ""
    yellow_mask = cv2.inRange(frame, lowerb=np.array([91, 188, 210]), upperb=np.array([166, 247, 235]))
    yellow_mask = cv2.dilate(yellow_mask, kernel, iterations = 2)
    yellow_mask = cv2.cvtColor(yellow_mask, cv2.COLOR_GRAY2BGR)


    #   rgb(24, 108, 56)

    green_mask = cv2.inRange(frame, lowerb=np.array([50, 100, 20]), upperb=np.array([130, 190, 50]))
    green_mask = cv2.dilate(green_mask, kernel, iterations = 2)
    green_mask = cv2.cvtColor(green_mask, cv2.COLOR_GRAY2BGR)

    #cv2.imshow("", yellow_mask)
    #cv2.waitKey(0)

    fen_array = ["0" for x in range(64)]
    for coord in range(64):         #?coord je index 
            
        for i in range(15):    
            b1 = yellow_mask[y+i, x+i, 0]
            g1 = yellow_mask[y+i, x+i, 1]
            r1 = yellow_mask[y+i, x+i, 2]

            b2 = green_mask[y+i, x+i, 0]
            g2 = green_mask[y+i, x+i, 1]
            r2 = green_mask[y+i, x+i, 2]

            if  b1 == 255 and r1 == 255 and g1 == 255:
                fen = "w"

                fen_array[coord] = "w"

            elif b2 == 255 and r2 == 255 and g2 == 255:
                fen = "b"

                fen_array[coord] = "b"

        # rišemo krogce
            cv2.circle(frame, (x+i, y+i), 2, [0, modra, 255], 2)
        x += 41
        if counter % 8==0:
            counter = 0
            x = 23
            y += 52
            
        counter += 1
        modra += 3
    
    #cv2.imshow("", frame)
    #cv2.waitKey(0)

    #? print(fen_array)
    #! epska koda za dt v 2d array (tokrat celo pravilno)
    final = []
    for i in range(8):
        _ = []
        for j in range(8):
            _.append(fen_array[i*8 + j])
        final.append(_)
    print(final)

    np_final = np.array(final, str)
    np_final = np.rot90(np_final, k=3)

    fen = ""
    zeros = 0
    output = ""

    for i in np_final:
        for j in i:
            fen+=j
        fen +="/"

    for i in fen:
        if i.isalpha() != True and i != "/" and i != "0":
            for j in range(int(i)):
                output +="0"
        else: 
            output += i
            
    return output

print(get_fen_from_pic())

  
