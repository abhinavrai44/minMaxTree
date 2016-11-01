#!/bin/python
import random
import copy

def check_win(player, board):
    flag = 0
    for i in range(3):
        if (board[i][0]==player and board[i][1]==player and board[i][2]==player):
            flag = 1
        elif(board[0][i]==player and board[1][i]==player and board[2][i]==player):
            flag = 1
    if(board[0][0]==player and board[1][1]==player and board[2][2]==player):
        flag = 1
    elif(board[0][2]==player and board[1][1]==player and board[2][0]==player):
        flag = 1
    if (flag == 1):
        return True
    else:
        return False

def check_lose(rival, board):
    for i in range(3):
        if (board[i][0]==rival and board[i][1]==rival and board[i][2]==rival):
            return True
        elif(board[0][i]==rival and board[1][i]==rival and board[2][i]==rival):
            return True
    if(board[0][0]==rival and board[1][1]==rival and board[2][2]==rival):
        return True
    elif(board[0][2]==rival and board[1][1]==rival and board[2][0]==rival):
        return True
    else:
        return False
    
def check_draw(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j] == '_'):
                return False
    return True

def moves(board):
    move = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] == '_'):
                move.append([i, j])
    return move        

def max_prune(player, rival, board, depth, alpha, beta):
    max_val = float("-inf")
    
    if (check_win(rival, board) == True):
        # print board
        return (-1 * (10 + (9 - depth)))
    # elif (check_lose(rival, board) == True):
    #     return (10 + depth)
    elif (check_draw(board) == True):
        return (0)
    actions = moves(board)
    # print actions
    board_t = copy.deepcopy(board)
        
    for action in actions:
        board_temp = copy.deepcopy(board_t)
        board_temp[action[0]][action[1]] = player
        
        # print "MOVES : ", board_temp, depth, action, actions
        
        val = min_prune(player, rival, board_temp, depth + 1, alpha, beta)
        
        if val > beta:
            return val
        print "Max : ", action, " ", board_temp," ", val ," ", depth
        if (val > max_val):
            max_val = val
            best_action = action
            print "MAX Best: ",best_action, " ",max_val ," ", depth
            # print board
            
        alpha = max(alpha, max_val)
    if depth == 1:
        return best_action
    else:
        return max_val

    
    
def min_prune(player, rival, board, depth, alpha, beta):
    min_val = float("inf")
    
    if (check_win(player, board) == True):
        # print board
        return (10 + (9 - depth))
    # elif (check_lose(player, board) == True):
    #     return (-10 - depth)
    elif (check_draw(board) == True):
        return (0)
    
    for action in moves(board):
        board_temp =  copy.deepcopy(board)
        board_temp[action[0]][action[1]] = rival
        
        val = max_prune(player, rival, board_temp, depth + 1, alpha, beta)
        print "Min : ", action, " ", val ," ", depth
        if val < alpha:
            return val
        
        if (val < min_val):
            min_val = val
            best_action = action
            print "MIN Best", action, " ", val ," ", depth
            
        beta = min(beta, min_val)
    return min_val
    
    

# Complete the function below to print 2 integers separated by a single space which will be your next move 
def nextMove(player,board):
    w = 3
    h = 3
    maze = [[0 for x in range(w)] for y in range(h)] 
    for i in range(3):
        for j in range(3):
            maze[i][j] = board[i][j]
            
    if player == 'X':
        rival = 'O'
    else:
        rival = 'X'
    alpha = float("-inf")
    beta = float("inf")
    depth = 1
    move = max_prune(player, rival, maze, depth, alpha, beta)
    print move[0], move[1]

    

#If player is X, I'm the first player.
#If player is O, I'm the second player.
player = raw_input()

#Read the board now. The board is a 3x3 array filled with X, O or _.
board = []
for i in xrange(0, 3):
    board.append(raw_input())

nextMove(player,board);  