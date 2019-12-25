
def generate(numRows):
    if numRows == 0: return []
    if numRows == 1: return [[1]]
    if numRows == 2: return [[1],[1,1]]

    result = [[1],[1,1]]
    for i in range(3, numRows+1):
        previousRow = result[-1]
        currentRow = [1]*i
        for index in range(1,i-1):
            currentRow[index] = previousRow[index-1]+previousRow[index]
        result.append(currentRow)
    
    return result

print(generate(5))