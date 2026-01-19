from game import TicTacToe
from ai import best_move

def play_game():
    game = TicTacToe()
    print("Welcome to Tic-Tac-Toe! You are X, AI is O. AI goes first.")
    game.print_board()

    # AI first move
    move = best_move(game)
    game.make_move(move, 'O')
    print("AI plays:", move // 3 + 1, move % 3 + 1)
    game.print_board()

    while not game.is_full() and not game.is_winner('X') and not game.is_winner('O'):
        try:
            pos = int(input("Your move (1-9): ")) - 1
            if pos not in game.available_moves():
                print("Invalid move!")
                continue
            game.make_move(pos, 'X')
            game.print_board()
            if game.is_winner('X'):
                print("You win!")
                break
            if game.is_full():
                break

            # AI move
            move = best_move(game)
            game.make_move(move, 'O')
            print("AI plays:", move // 3 + 1, move % 3 + 1)
            game.print_board()
            if game.is_winner('O'):
                print("AI wins! (Unbeatable)")
                break
        except ValueError:
            print("Enter number 1-9")

    print("Game over.")

if __name__ == "__main__":
    play_game()
