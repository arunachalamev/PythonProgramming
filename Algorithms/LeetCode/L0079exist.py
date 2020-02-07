

def exist(board, word):
    m,n = len(board), len(board[0])
    def search(i,j,word):
        nonlocal m,n
        if len(word) == 0:
            return True
        if i<0 or i==m or j <0 or j==n or board[i][j] !=word[0]:
            return False
        board[i][j] = '#'
        for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            if search (i+di, j+dj , word[1:]):
                return True
        board[i][j] = word[0]
        return False

    for i,row in enumerate(board):
        for j,_ in enumerate(row):
                if search(i,j,word):
                    return True
    return False


print (exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], 'ABCCEDX'))