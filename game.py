class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winning_player = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print()

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def is_winner(self, player):
        win_states = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        return any(all(self.board[i] == player for i in combo) for combo in win_states)

    def is_full(self):
        return ' ' not in self.board

    def make_move(self, position, player):
        self.board[position] = player

    def reset(self):
        self.board = [' ' for _ in range(9)]
