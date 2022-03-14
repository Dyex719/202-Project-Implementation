import random
import sys

def gen_grid(n, num_values):
    # randomly populate num_values in the grid with range 1 to n
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(num_values):
        row = random.randint(0, n - 1)
        col = random.randint(0, n - 1)
        while grid[row][col] != 0:
            row = random.randint(0, n - 1)
            col = random.randint(0, n - 1)
        grid[row][col] = random.randint(1, n)
    return grid

def get_worst_case_constraints(n, num_values):
    hor_constraints = [['>' for _ in range(n-1)] for _ in range(n)]
    ver_constraints = [['v' for _ in range(n)] for _ in range(n-1)]
    hor_constraints[-1][-1] = '<'
    return hor_constraints, ver_constraints

def gen_horizontal_constraints(n, num_values):
    hor_constraints = [['0' for _ in range(n-1)] for _ in range(n)]
    for i in range(num_values):
        row = random.randint(0, n - 1)
        col = random.randint(0, n - 2)
        while hor_constraints[row][col] != '0':
            row = random.randint(0, n - 1)
            col = random.randint(0, n - 2)
        hor_constraints[row][col] = random.choice(['<', '>'])
    return hor_constraints

def gen_vertical_constraints(n, num_values):
    ver_constraints = [['0' for _ in range(n)] for _ in range(n-1)]
    for i in range(num_values):
        row = random.randint(0, n - 2)
        col = random.randint(0, n - 1)
        while ver_constraints[row][col] != '0':
            row = random.randint(0, n - 2)
            col = random.randint(0, n - 1)
        ver_constraints[row][col] = random.choice(['^', 'v'])
    return ver_constraints

def write_to_file(grid, hor_constraints, ver_constraints, filename):
    with open(filename, 'w') as f:
        for row in grid:
            for val in row:
                f.write(str(val) + ' ')
            f.write('\n')
        f.write('\n')
        for row in hor_constraints:
            for val in row:
                f.write(str(val) + ' ')
            f.write('\n')
        f.write('\n')
        for row in ver_constraints:
            for val in row:
                f.write(str(val) + ' ')
            f.write('\n')
        f.write('\n')
    
def main(n, num_values1, num_values2, num_values3, filename):
    # first argument is the size of the grid
    n = int(sys.argv[1])
    num_values1 = int(sys.argv[2])
    num_values2 = int(sys.argv[3])
    num_values3 = int(sys.argv[4])
    filename = sys.argv[5]
    print(n, num_values1, num_values2, num_values3, filename)
    grid = gen_grid(n, num_values1)
    hor_constraints = gen_horizontal_constraints(n, num_values2)
    ver_constraints = gen_vertical_constraints(n, num_values3)
    write_to_file(grid, hor_constraints, ver_constraints, filename)

def main2(n, num_values1, num_values2, num_values3, filename):
    print(n, num_values1, num_values2, num_values3, filename)
    grid = gen_grid(n, num_values1)
    hor_constraints, ver_constraints = get_worst_case_constraints(n, num_values1)
    write_to_file(grid, hor_constraints, ver_constraints, filename)

# increment n by 5, num_values is constant of 5, filename version should update
if __name__ == '__main__':
    for i in range(3, 20):
        main(i, 0, 3, 3, 'inputw_' + str(i) + '.txt')
        main2(i, 3, 3, 3, 'inputw_' + str(i) + '.txt')