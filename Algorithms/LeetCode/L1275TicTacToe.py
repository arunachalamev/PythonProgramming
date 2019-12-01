def tictactoe(moves):
    m = len(moves)
    row = [0]*3
    col = [0]*3
    diagonal,offdiagonal = 0,0
    if m %2 ==1:
        Amoves = moves[::2]
        for i,j in Amoves:
            row[i] = row[i] + 1
            col[j] = col[j] + 1
            if i==j: diagonal = diagonal + 1
            if i+j==2 : offdiagonal = offdiagonal + 1

        if row[i]==3 or col[j] == 3 or diagonal ==3 or offdiagonal ==3:
            return "A"
        else:
            if m == 9:
                return "Draw"
            else:
                return "Pending"

    else:
        Bmoves = moves[1::2]
        for i,j in Bmoves:
            row[i] = row[i] + 1
            col[j] = col[j] + 1
            if i==j: diagonal = diagonal + 1
            if i+j==2 : offdiagonal = offdiagonal + 1

        if row[i]==3 or col[j] == 3 or diagonal ==3 or offdiagonal ==3:
            return "B"
        else:
            if m == 9:
                return "Draw"
            else:
                return "Pending"

    return None

print (tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])) #A
print (tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]])) #B
print (tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]])) #Draw
print (tictactoe([[0,0],[1,1]])) #pending
