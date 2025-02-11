import socket
from stockfish import Stockfish


#! ENGINE INITIALIZATION
STOCKFISH_PATH = "stockfish\\stockfish-windows-x86-64-avx2.exe" #MORE BIT RELATIVEN !!!!!!!!!!!!!!!!!!!!

stockfish = Stockfish(path=STOCKFISH_PATH, depth=18, parameters={"Threads": 7, "Minimum Thinking Time": 8, "Skill Level": 20}) # 18 is the depth of the engine
stockfish.update_engine_parameters({"Hash": 4056})





def get_move(fen:str):

    stockfish.set_fen_position(fen) #stockfish nastavi figure na mesta zapisana v FEN notaciji. Na koncu dobi črko w ali b ki mu pove ali naj dela potezo iz perspektive črnega ali belega igralca

    move = stockfish.get_best_move()   #stockfish najde najboljšo potezo             
    stockfish.make_moves_from_current_position([move])  #potezo doda v notacijo FEN
    #print(stockfish.get_board_visual(fen))

    return move, stockfish.get_fen_position()   # stockfish nam vrne potezo, ki naj jo naredimo in pa FEN