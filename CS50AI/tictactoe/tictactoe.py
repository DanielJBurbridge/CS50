"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    count_of_X = 0
    count_of_O = 0

    for row in board:
        for cell in row:
            if cell == X:
                count_of_X += 1
            elif cell == O:
                count_of_O += 1    
    if count_of_X > count_of_O:
        return O
    
    return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = player(board)
        return new_board
    else:
        raise Exception("Illegal move")
    


def winner(board):
    """
    Return either X or O depending on the winner of the game.
    Returns None if there is no winner
    """
    
    #checking Columns
    if board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    
    #checking Diag's
    elif board[0][0] == board[1][1] == board[2][2]:
        return board[0][0] 
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    #checking Rows
    elif board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    empty_count = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                empty_count += 1
    
    if empty_count == 0:
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
        

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return utility(board)

    if player(board) == X:
        best_move = None
        best_value = -math.inf
        for action in actions(board):
             current_value = minimax(result(board, action))
             if current_value > best_value:
                 best_value = current_value
                 best_move = action
        return best_move
    elif player(board) == O:
        best_move = None
        best_value = math.inf
        for action in actions(board):
            current_value = minimax(result(board, action))
            if current_value < best_value:
                best_value = current_value
                best_move = action
        return best_move



