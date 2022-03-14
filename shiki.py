from functools import wraps
from time import time
import os

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        # write time taken to file
        with open('time.txt', 'a') as x:
            x.write(f'{file} took {te-ts} seconds\n')
        # print('func:%r args:[%r, %r] took: %2.4f sec' % \
        #   (f.__name__, args, kw, te-ts))
        return result
    return wrap

# Reads from the input file to get the futoshiki puzzle and constraints
def get_matrix(filename):
    with open(filename, 'r') as file:
        for i in range(num_cells):
            str_row = file.readline().strip().split()
            int_row = [int(num) for num in str_row]
            matrix.append(int_row)
        file.readline()

        for i in range(num_cells):
            row = file.readline().strip().split()
            row_constraints.append(row)
        file.readline()

        for i in range(num_cells-1):
            row = file.readline().strip().split()
            col_constraints.append(row)

# Check if value exists in row
def check_row(val, row):
    for col in range(num_cells):
        if matrix[row][col] == val:
            return False
    return True

# Check if value exists in column
def check_col(val, col):
    for row in range(num_cells):
        if matrix[row][col] == val:
            return False
    return True


# Checks for a certain position whether the value passes the constraints
def passes_constraint(val, row_num, col_num):
    if col_num > 0:
        if matrix[row_num][col_num - 1] != 0:
            if (row_constraints[row_num][col_num - 1] == '>' and matrix[row_num][col_num - 1] < val):
                return False
            elif (row_constraints[row_num][col_num - 1] == '<' and  matrix[row_num][col_num - 1] > val):
                return False

    if col_num < num_cells - 1:
        if matrix[row_num][col_num + 1] != 0:
            if (row_constraints[row_num][col_num] == '>' and matrix[row_num][col_num + 1] < val):
                return False
            elif (row_constraints[row_num][col_num] == '<' and  matrix[row_num][col_num + 1] > val):
                return False

    if row_num > 0:
        if (col_constraints[row_num - 1][col_num] == 'v' and matrix[row_num - 1][col_num] != 0 and
        matrix[row_num - 1][col_num] < val):
            return False
        if (col_constraints[row_num - 1][col_num] == '^' and matrix[row_num - 1][col_num] != 0 and
        matrix[row_num - 1][col_num] > val):
            return False

    if row_num < num_cells - 1:
        if (col_constraints[row_num][col_num] == 'v' and matrix[row_num + 1][col_num] != 0 and
        val < matrix[row_num + 1][col_num]):
            return False
        if (col_constraints[row_num][col_num] == '^' and matrix[row_num + 1][col_num] != 0 and
        val > matrix[row_num + 1][col_num]):
            return False
            
    return True

# Gets the next empty cell in the matrix
def get_blank_cell():
    for row in range(num_cells):
        for col in range(num_cells):
            if not matrix[row][col]:
                return (row, col)
    return False

# main function that solves the puzzle
@timing
def solve_puzzle():
    if not backtrack():
        return False
    return matrix

# Visits empty cells, places values and backtracks if it cannout progress further
def backtrack():
    cell = get_blank_cell()
    # print(cell)
    if not cell:
        return True
    for num in range(1, num_cells + 1):
        if (check_row(num, cell[0]) and check_col(num, cell[1]) and
        passes_constraint(num, cell[0], cell[1])):
            matrix[cell[0]][cell[1]] = num
            if backtrack():
                return True
            matrix[cell[0]][cell[1]] = 0

    return False

# main function
# if __name__ == "__main__":
#     input_file = "input.txt"
#     num_cells = 5
#     matrix = []
#     row_constraints = []
#     col_constraints = []
#     get_matrix(input_file)
#     res = solve_puzzle()

#     if res:
#         print(matrix)
#     else:
#         print("No solution formed")

# read all files that start with input and solve them
for file in os.listdir():
    if file.startswith("inputw"):
        print(file)
        input_file = file
        num_cells = int(file.split('.')[0].split('_')[1])
        matrix = []
        row_constraints = []
        col_constraints = []
        get_matrix(input_file)
        print(matrix)
        res = solve_puzzle()

        if res:
            print(matrix)
        else:
            print("No solution formed")
