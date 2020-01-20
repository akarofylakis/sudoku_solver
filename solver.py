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
        for j in range(len(b[0]))
            if b[i][j] == 0:
                return (j, i)


