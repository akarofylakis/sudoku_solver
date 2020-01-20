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

def print_board(b):
    """
    Prints a given sudoku board

    :type b: List[int]
    :rtype: None
    """
    for i in range(len(b)):

        # Separate for each row
        if i % 3 == 0 and i != 0:
            print('---------------------')

        # Separate for every 3 columns, else just print cell number
        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            if j != 8:
                print(b[i][j], end=' ')
            else:
                print(b[i][j], end='')
        print('')


def find_empty(b):
    """
    Finds empty cell to start testing for solutions. Returns tuple of cell indeces (x, y)

    :type b: List[int]
    :rtype: Tuple(int, int)
    """
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (j, i)

    return None

def valid(b, num, pos):
    """
    Checks whether given solution (num) for cell (pos) is valid or not.  

    :type b: List[int]
    :type num: int
    :type pos: Tuple(int, int)
    :rtype: Boolean
    """
    # Check if row is valid
    for i in range(len(b[0])):
        if pos[1] != i and b[pos[0]][i] == num:
            return False

    # Check if column is valid
    for j in range(len(b)):
        if pos[0] != j and b[j][pos[1]] == num:
            return False

    # Check if box is valid
    box_x = pos[0] // 3
    box_y = pos[1] // 3
    for j in range(box_y*3, box_y*3+3):
        for i in range(box_x*3, box_x*3+3):
            if b[i][j] == num and pos != (j, i):
                return False
    return True


def solve(b):
    """
    Solves the board recursively using backtracking 

    :type b: List[int]
    :rtype: Boolean
    """
    find = find_empty(b)
    if not find:
        return True
    else:
        col, row = find

    for i in range(1,10):
        if valid(b, i, (row, col)):
            b[row][col] = i

            if solve(b):
                return True

            b[row][col] = 0

    return False

print_board(board)
solve(board)
print('')
print_board(board)