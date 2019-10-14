

def queensAttacktheKing(queens, king):

    king_row = king[0]
    king_col = king[1]

    result = []

    for i in [-1,0,1]:
        for j in [-1,0,1]:
            for k in range(1,8,1):
                current_row = king_row + i*k
                current_col = king_col + j*k

                pos = [current_row,current_col]

                if pos in queens:
                    result.append(pos)
                    break

    return result



if __name__ == "__main__":
    queens =  [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
    king = [0,0]

    print (queensAttacktheKing(queens,king))
