board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def find_empty():
    """Finds next empty space on sodoku board

       Returns:
        i,j (tuple): coordinates of next empty space 
    """
    for i in range(9):
        for j in range(9):
            if (board[i][j] == 0):
                return i,j

def solve():
    """Solves sodoku puzzle using backtracking

        Returns:
            The solved board
    """   
    cell = find_empty()

    if cell:
        row, col = cell
    else:
        return True

    for test_num in range (1,10):
            
        if (validate(row, col, test_num)):
            board[row][col] = test_num

            if solve():
                return True 

            board[row][col] = 0
                
    return False

def validate(row, col, num):
    """Validates that a number placed in an empty cell of the board
       is not duplicated in a column, a row, or a 3x3 square.

       Args:
            row (list): a list of numbers in a specific row
            col (int): the current column that
            num (int): the number being validated

        Returns:
            True if num obeys the rules of sodoku, false otherwise
    """
    
    #validate row
    for i in board[row]:
        if (num == i):
            return False

    #validate col
    for i in board:
        if (num == i[col]):
            return False

    #validate square
    for i in getIndices(row):
        for j in getIndices(col):
            if (num == board[i][j]):
                return False
    
    #if the move agrees with Sodoku rules return True
    return True

def getIndices(index):
    if (index % 3 == 0):
        return [index+1,index+2]

    elif (index % 3 == 1):
        return [index-1,index+1]

    elif (index % 3 == 2):
        return [index-2,index-1]

solve()
print(board)