import numpy as np

from game_abc import AbstractGameState, AbstractGameAction

class ttt_register_move (AbstractGameAction):
    
    def __init__ (self, x, y, move):
        
        self.x = x
        self.y = y
        self.move = move

    def __repr__(self):

        return " x:{0} y:{1} m:{2}".format(self.x, self.y, self.move)


class ttt_game_state (AbstractGameState):
    
    X = 1
    O = -1
    

    def __init__ (self, state, next_to_move = 1):

        self.ttt_board = state
        self.board_size = state.shape[0]

        self.next_to_move = next_to_move


    @property
    def game_result(self):

        sum_row = np.sum(self.ttt_board, 0)
        sum_col = np.sum(self.ttt_board, 1)
        sum_dia_left = self.ttt_board.trace()
        sum_dia_right = self.ttt_board[::-1].trace()

        
        player_one_wins = any(sum_row == self.board_size)
        player_one_wins += any(sum_col == self.board_size)
        player_one_wins += (sum_dia_left == self.board_size)
        player_one_wins += (sum_dia_right == self.board_size)

        if player_one_wins:
            return self.x

        player_two_wins = any(sum_row == -self.board_size)
        player_two_wins += any(sum_col == -self.board_size)
        player_two_wins += (sum_dia_left == -self.board_size)
        player_two_wins += (sum_dia_right == -self.board_size)

        if player_two_wins:
            return self.o

        
        if np.all(self.ttt_board != 0):
            return 0

        return none


    def is_game_over(self):
        return self.game_result is not None

    def is_legal_move(self, move):

        if move.move != self.next_to_move:
            return False

        # check if inside the board on x-axis
        x_in_range = (0 <= move.x < self.board_size)
        if not x_in_range:
            return False

        # check if inside the board on y-axis
        y_in_range = (0 <= move.y < self.board_size)
        if not y_in_range:
            return False

        # finally check if board field not occupied yet
        return self.ttt_board[move.x, move.y] == 0


    def move (self, move):

        if not self.is_legal_move(move):
            raise ValueError ( " Move Not Legal ")

        new_board = np.copy(self.board)
        new_board[move.x, move.y] = move.value

        next_to_move = ttt_game_state.O if self.next_to_move==ttt_game_state.X else ttt_game_state.X
        
        return(new_board, next_to_move)

    def get_legal_actions(self):

        empty_xy = np.where(self.ttt_board == 0)
        
        for xy in list(zip(empty_xy[0],empty_xy[1])):
            legal_actions = [ttt_register_move (xy[0], xy[1], self.next_to_move)]

        return legal_actions
        






