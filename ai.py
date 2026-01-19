from game import TicTacToe
import math

def minimax(game, player, alpha=-math.inf, beta=math.inf, depth=0):
    if game.is_winner('O'):  # AI wins
        return 10 - depth
    if game.is_winner('X'):  # Human wins
        return depth - 10
    if game.is_full():
        return 0

    if player == 'O':  # Maximizing (AI)
        max_eval = -math.inf
        for move in game.available_moves():
            game.make_move(move, 'O')
            eval_score = minimax(game, 'X', alpha, beta, depth + 1)
            game.board[move] = ' '
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval
    else:  # Minimizing (Human)
        min_eval = math.inf
        for move in game.available_moves():
            game.make_move(move, 'X')
            eval_score = minimax(game, 'O', alpha, beta, depth + 1)
            game.board[move] = ' '
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval

def best_move(game):
    best_score = -math.inf
    move = None
    for possible_move in game.available_moves():
        game.make_move(possible_move, 'O')
        score = minimax(game, 'X')
        game.board[possible_move] = ' '
        if score > best_score:
            best_score = score
            move = possible_move
    return move
