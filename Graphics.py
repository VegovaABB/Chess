# importing required library
import pygame
import time

def see_board(fen):

    usable_fen=""


    #pretvori fen v uporabno obliko "brez / in namesto stevilk"

    for i in fen:
        if i.isalpha() == True:
            usable_fen += i
        if i.isnumeric() == True:
            for j in range(int(i)):
                usable_fen += "0"


    # aktiviraj pygame

    pygame.init()

    X = 720
    Y = 720
    x = 720/8

    #visina, sirina displaya
    scrn = pygame.display.set_mode((X, Y))

    # ime display windowa
    pygame.display.set_caption('image')

    # naredi surface po katerem lahko rises
    background = pygame.image.load(".\\board.png").convert()

    pieces = {

    "Q": pygame.transform.scale(pygame.image.load(".\\white\\Q.png").convert_alpha(), (85, 85)), 
    "K": pygame.transform.scale(pygame.image.load(".\\white\\K.png").convert_alpha(), (85, 85)),
    "B": pygame.transform.scale(pygame.image.load(".\\white\\B.png").convert_alpha(), (85, 85)),
    "N": pygame.transform.scale(pygame.image.load(".\\white\\N.png").convert_alpha(), (85, 85)),
    "R": pygame.transform.scale(pygame.image.load(".\\white\\R.png").convert_alpha(), (85, 85)),
    "P": pygame.transform.scale(pygame.image.load(".\\white\\P.png").convert_alpha(), (85, 85)),


    "q": pygame.transform.scale(pygame.image.load(".\\black\\Q.png").convert_alpha(), (85, 85)),
    "k": pygame.transform.scale(pygame.image.load(".\\black\\K.png").convert_alpha(), (85, 85)),
    "b": pygame.transform.scale(pygame.image.load(".\\black\\B.png").convert_alpha(), (85, 85)),
    "n": pygame.transform.scale(pygame.image.load(".\\black\\N.png").convert_alpha(), (85, 85)),
    "r": pygame.transform.scale(pygame.image.load(".\\black\\R.png").convert_alpha(), (85, 85)),
    "p": pygame.transform.scale(pygame.image.load(".\\black\\P.png").convert_alpha(), (85, 85))

    }



    scrn.blit(background, (0, 0))

    for i in range(64):
        if usable_fen[i] != "0":
            scrn.blit(pieces[usable_fen[i]], (((63-i)%8)*x, ((63-i)//8)*x))



    pygame.display.flip()
    time.sleep(1)


