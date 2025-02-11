import re

def parse_fen(fen):
    board = []
    rows = fen.split()[0].split('/')
    for row in rows:
        board_row = []
        for char in row:
            if char.isdigit():
                board_row.extend(['.'] * int(char))
            else:
                board_row.append(char)
        board.append(board_row)
    return board

def get_piece_moves(piece, board, color):
    moves = []
    directions = {
        'P': [(-1, 0), (-1, -1), (-1, 1)],
        'N': [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)],
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],
        'Q': [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)],
        'K': [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)],
    }
    for row in range(8):
        for col in range(8):
            if board[row][col].upper() == piece:
                for direction in directions[piece]:
                    for i in range(1, 8):
                        r = row + direction[0] * i
                        c = col + direction[1] * i
                        if 0 <= r < 8 and 0 <= c < 8:
                            if board[r][c] == '.':
                                moves.append((row, col, r, c))
                            elif board[r][c].isalpha():
                                if (color == 'w' and board[r][c].islower()) or (color == 'b' and board[r][c].isupper()):
                                    moves.append((row, col, r, c))
                                break
                        else:
                            break
                    if piece in 'PNK':
                        break
    return moves

def chess_notation_to_coordinates(move, fen):
    board = parse_fen(fen)
    piece = move[0]
    if piece.islower() or piece in 'abcdefgh':
        piece = 'P'
        target = move if piece == 'P' else move[1:]
    else:
        target = move[1:]
    color = 'w' if ' ' in fen and fen.split()[1] == 'w' else 'b'
    file_to_col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    row = 8 - int(target[1])
    col = file_to_col[target[0]]
    
    moves = get_piece_moves(piece, board, color)
    for move in moves:
        if move[2] == row and move[3] == col:
            start_square = (move[0], move[1])
            end_square = (row, col)
            return start_square, end_square

    return None

# Example usage
fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
move = "Bf4"
result = chess_notation_to_coordinates(move, fen)
if result:
    start, end = result
    print(f"Start square: {start}, End square: {end}")
else:
    print("Invalid move or move not found.")
