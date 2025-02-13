import pygame
import chess
import stockfish_wrapper

class ChessBoard:
    def __init__(self, fen, color):
        self.move = True
        pygame.init()
        self.color = " "+color
        self.fen = fen
        self.usable_fen = self.fen_to_usable(self.fen)
        self.selected_piece = None
        self.previous_fen = self.fen
        self.running = True

        # Pygame setup
        self.X, self.Y = 720, 720
        self.square_size = self.X // 8
        self.screen = pygame.display.set_mode((self.X, self.Y))
        pygame.display.set_caption("Chess Game")

        # Load assets
        self.background = pygame.image.load("./board.png").convert()
        self.pieces = self.load_pieces()

    def update_fen(self, novfen):
        self.fen = novfen
        self.usable_fen=self.fen_to_usable(self.fen)
        self.previous_fen=self.fen
        self.draw_board()

    
    def update_move(self, bul):
        self.move = bul
    
    def retfen(self):
        return self.previous_fen
        #return self.usable_to_fen(self.fen)

    def load_pieces(self):
        pieces = {
            "Q": pygame.transform.scale(pygame.image.load("./white/Q.png").convert_alpha(), (self.square_size, self.square_size)),
            "K": pygame.transform.scale(pygame.image.load("./white/K.png").convert_alpha(), (self.square_size, self.square_size)),
            "B": pygame.transform.scale(pygame.image.load("./white/B.png").convert_alpha(), (self.square_size, self.square_size)),
            "N": pygame.transform.scale(pygame.image.load("./white/N.png").convert_alpha(), (self.square_size, self.square_size)),
            "R": pygame.transform.scale(pygame.image.load("./white/R.png").convert_alpha(), (self.square_size, self.square_size)),
            "P": pygame.transform.scale(pygame.image.load("./white/P.png").convert_alpha(), (self.square_size, self.square_size)),
            "q": pygame.transform.scale(pygame.image.load("./black/Q.png").convert_alpha(), (self.square_size, self.square_size)),
            "k": pygame.transform.scale(pygame.image.load("./black/K.png").convert_alpha(), (self.square_size, self.square_size)),
            "b": pygame.transform.scale(pygame.image.load("./black/B.png").convert_alpha(), (self.square_size, self.square_size)),
            "n": pygame.transform.scale(pygame.image.load("./black/N.png").convert_alpha(), (self.square_size, self.square_size)),
            "r": pygame.transform.scale(pygame.image.load("./black/R.png").convert_alpha(), (self.square_size, self.square_size)),
            "p": pygame.transform.scale(pygame.image.load("./black/P.png").convert_alpha(), (self.square_size, self.square_size)),
        }
        return pieces

    def fen_to_usable(self, fen):
        """Convert FEN string to a usable form."""
        usable = ""
        for char in fen:
            if char.isalpha():
                usable += char
            elif char.isnumeric():
                usable += "0" * int(char)
            elif char ==  " ":
                break
        return usable

    def usable_to_fen(self, usable):
        """Convert usable board string back to FEN format."""
        fen = ""
        empty_count = 0
        for i, char in enumerate(usable):
            if char == "0":
                empty_count += 1
            else:
                if empty_count > 0:
                    fen += str(empty_count)
                    empty_count = 0
                fen += char
            if (i + 1) % 8 == 0:
                if empty_count > 0:
                    fen += str(empty_count)
                    empty_count = 0
                if i < 63:
                    fen += "/"
        return fen

    def is_move_legal(self, prev_fen, new_fen):
        """Validate moves using python-chess."""
        board = chess.Board(prev_fen)
        uci_move = self.get_uci(prev_fen, new_fen)
        if not uci_move:
            return False
        move = chess.Move.from_uci(uci_move)
        return move in board.legal_moves

    def get_uci(self, prev_fen, new_fen):
        """Generate UCI from FEN comparison."""
        prev_usable = self.fen_to_usable(prev_fen)
        new_usable = self.fen_to_usable(new_fen)
        old_square, new_square = None, None

        for i in range(64):
            if prev_usable[i] != new_usable[i]:
                if new_usable[i] == "0":
                    old_square = i
                elif new_usable[i] != "0":
                    new_square = i

        if old_square is not None and new_square is not None:
            return f"{chr(old_square % 8 + 97)}{8 - old_square // 8}{chr(new_square % 8 + 97)}{8 - new_square // 8}"
        return None

    def draw_board(self):
        """Draw the chessboard and pieces."""
        self.screen.blit(self.background, (0, 0))
        for i in range(64):
            if self.usable_fen[i] != "0":
                self.screen.blit(self.pieces[self.usable_fen[i]], ((i % 8) * self.square_size, (i // 8) * self.square_size))
        pygame.display.flip()
    

    def run(self):
        """Start the game loop."""
        while self.running and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN and self.move:
                    if event.button == 1:  # Left mouse button
                        x, y = event.pos
                        col, row = x // self.square_size, y // self.square_size
                        index = row * 8 + col
                        if self.usable_fen[index] != "0":
                            self.selected_piece = (index, self.usable_fen[index])  # Store the piece and its position
                            self.usable_fen = self.usable_fen[:index] + "0" + self.usable_fen[index + 1:]

                elif event.type == pygame.MOUSEBUTTONUP and self.move:
                    if event.button == 1 and self.selected_piece:
                        x, y = event.pos
                        col, row = x // self.square_size, y // self.square_size
                        index = row * 8 + col

                        new_usable_fen = self.usable_fen[:index] + self.selected_piece[1] + self.usable_fen[index + 1:]
                        new_fen = self.usable_to_fen(new_usable_fen)


                        if self.is_move_legal(self.previous_fen, new_fen):
                            self.usable_fen = new_usable_fen
                            self.previous_fen = new_fen
                            self.running = False
                            self.move=False

                        else:
                            # Revert move if illegal
                            self.usable_fen = self.fen_to_usable(self.previous_fen)

                        self.selected_piece = None

            # Redraw the board
            self.draw_board()

            if self.selected_piece:
                x, y = pygame.mouse.get_pos()
                self.draw_board()  # Draw without the selected piece
                self.screen.blit(self.pieces[self.selected_piece[1]], (x - self.square_size // 2, y - self.square_size // 2))
                pygame.display.flip()

    def quit():
        pygame.quit()
