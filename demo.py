from game import TicTacToe
from ai import best_move
import random

def ai_vs_ai(num_games=100):
    ai_wins, draws, losses = 0, 0, 0
    for _ in range(num_games):
        game = TicTacToe()
        while not game.is_full():
            move = best_move(game)
            game.make_move(move, 'O')
            if game.is_winner('O'):
                ai_wins += 1
                break
            if game.is_full():
                draws += 1
                break
        print(f"AI vs AI: Wins {ai_wins}, Draws {draws}, Losses {losses}")

if __name__ == "__main__":
    ai_vs_ai()
