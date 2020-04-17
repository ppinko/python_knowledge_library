#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 10:32:18 2019

@author: lx
"""

"""
My first interactive game - cross and circle
"""

import sys
from recursion import test

board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def update_board(a, b, c, current_board):
    """ Update board """
    current_board[a][b] = c
    return current_board

#test(update_board(0, 0, 'x', board) == [['x', '-', '-'], ['-', '-', '-'], 
#     ['-', '-', '-']])
#test(update_board(1, 2, 'o', board) == [['x', '-', '-'], ['-', '-', 'o'], 
#     ['-', '-', '-']])
#test(update_board(2, 0, 'x', board) == [['x', '-', '-'], ['-', '-', 'o'], 
#     ['x', '-', '-']])
#print(board)
    
def check_win(current_board, symbol):
    """ Check if someone wins """
    for i in range(3):
        if current_board[i].count(symbol) == 3:
            return True
        if current_board[0][i] == current_board[1][i] == current_board[2][i]  == symbol:
            return True
    if current_board[0][0] == current_board[1][1] == current_board[2][2] == symbol:
            return True
    if current_board[0][2] == current_board[1][1] == current_board[2][0] == symbol:
            return True  
    return False

#test(check_win([['x', '-', '-'], ['-', '-', '-'], 
#                ['-', '-', '-']], 'x') == False)
#test(check_win([['x', 'x', 'x'], ['-', '-', '-'], 
#                ['-', '-', '-']], 'x') == True)
#test(check_win([['x', '-', '-'], ['x', '-', '-'], 
#                ['x', '-', '-']], 'x') == True)
#test(check_win([['x', '-', '-'], ['-', 'x', '-'], 
#                ['-', '-', 'x']], 'x') == True)
    
def printed_board(current_board):
    """ Show current board """
    print(current_board[0][0], current_board[1][0], current_board[2][0])
    print(current_board[0][1], current_board[1][1], current_board[2][1])
    print(current_board[0][2], current_board[1][2], current_board[2][2])
    
def check_move(x, y, possible_moves):
    """ Check possibility of the movement """
    move = (x-1, y-1)
    if move in possible_moves:
        return True
    else:
        return False
        
#possibles = [(0,0), (0,1), (1,1), (1,0)]
#test(check_move(1,1, possibles) == [(0,1), (1,1), (1,0)])      
  
        
def two_player_game():
    """ Interactive game for two players """
    symbol = 'x'
    possible_moves = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    current_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    n = 1
    print("Welcome in the game!\nHave a nice game!\n")
    printed_board(current_board)
    while n <= 9:
        x = int(input('Choose a column: '))
        y = int(input('Choose a row: '))
        z = (x-1, y-1)
        if check_move(x, y, possible_moves) == False:
            print('Invalid move')
            continue
        possible_moves.remove(z)
        print('\n')
        updated_board = update_board(x-1, y-1, symbol, current_board)
        current_board = updated_board[:]
        printed_board(current_board)
        if n >= 3:
            if check_win(updated_board, symbol) == True:
                return print('WINNER')
        n += 1
        if symbol == 'x':
            symbol = 'o'
        else:
            symbol = 'x'
    return print('END OF THE GAME' + '\n' + 'NO WINNER')

""" Initilizing the game """
two_player_game() # START OF THE GAME