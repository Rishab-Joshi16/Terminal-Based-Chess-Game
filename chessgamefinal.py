import chess
import colorama

colorama.init()

class ChessGame:
    def __init__(self):
        self.board = chess.Board()

    def play(self):
        while not self.board.is_game_over():
            self.print_board()
            print(colorama.Fore.GREEN + "\nWhite to move\n" if self.board.turn == chess.WHITE else colorama.Fore.GREEN + "\nBlack to move\n")
            move = self.get_player_move()
            self.make_move(move)

        self.print_board()
        self.print_game_result()

    def print_board(self):
        print("\n")
        print(colorama.Fore.WHITE + "    a  b  c  d  e  f  g  h")
        print(colorama.Fore.WHITE + "  -------------------------")
        ranks = range(8)[::-1] # Ranks
        files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # Files
        is_check = self.board.is_check()
        king_square = self.board.king(self.board.turn)
        for rank in ranks:
            print(colorama.Fore.WHITE + str(rank + 1) + " |", end="")
            for i, file in enumerate(files):
                square = chess.square(ord(file) - ord('a'), rank)
                piece = self.board.piece_at(square)
                if (rank + i) % 2 == 0:
                    bg_color = colorama.Back.LIGHTGREEN_EX
                else:
                    bg_color = colorama.Back.LIGHTWHITE_EX

                if piece is not None:
                    piece_color = colorama.Fore.CYAN if piece.color == chess.WHITE else colorama.Fore.MAGENTA
                    if is_check and square == king_square:
                        bg_color = colorama.Back.RED #Set red background for king in check
                    piece_symbol = self.get_unicode_character(piece.piece_type)
                    print(piece_color + bg_color + " " + colorama.Style.BRIGHT + piece_symbol + " " + colorama.Style.RESET_ALL, end="")
                else:
                    print(bg_color + "   " + colorama.Style.RESET_ALL, end="")
            print(colorama.Fore.WHITE + "|" + str(rank + 1))
        print(colorama.Fore.WHITE + "  -------------------------")
        print(colorama.Fore.WHITE + "    a  b  c  d  e  f  g  h")

    def get_unicode_character(self, piece_type):
        unicode_symbols = {
            chess.PAWN: '♟',
            chess.KNIGHT: '♞',
            chess.BISHOP: '♝',
            chess.ROOK: '♜',
            chess.QUEEN: '♛',
            chess.KING: '♚'
        }
        return unicode_symbols.get(piece_type, '')

    def get_player_move(self):
        while True:
            try:
                move_str = input("Enter your move: ")
                move = self.board.parse_san(move_str)
                if move in self.board.legal_moves:
                    return move
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid move format. Try again.")

    def make_move(self, move):
        self.board.push(move)

    def print_game_result(self):
        result = self.board.result()
        if result == "1-0":
            print(colorama.Fore.YELLOW + "White wins!")
        elif result == "0-1":
            print(colorama.Fore.YELLOW + "Black wins!")
        else:
            print(colorama.Fore.YELLOW + "Draw!")

game = ChessGame()
game.play()