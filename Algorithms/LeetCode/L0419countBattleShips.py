

def countBattleships(board):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X':
                flag = 1
                if j>0 and board[i][j-1] == 'X': flag = 0
                if i>0 and board[i-1][j] == 'X': flag = 0
                total += flag
    return total

print (countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))
