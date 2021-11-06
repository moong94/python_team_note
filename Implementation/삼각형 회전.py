def make_temp(grid):
    temp = [[] for _ in range(len(grid))]

    for i in range(len(grid)):
        temp[i] = ["-"] * (2 * i + 1)
    return temp

def rotate(grid, temp):
    for i in range(len(grid[-1])):
        for j in range(len(grid) - (i + 1) // 2):
            temp[len(grid) - j - 1][len(grid[-(j + 1)]) - i - 1] = grid[(i + 1) // 2 + j ][i]
    return temp

def list_to_str(grid):
    for i in range(len(grid)):
        grid[i] = "".join(grid[i])
        
def solution(grid, clockwise):
    for i in range(len(grid)):
        grid[i] = list(grid[i])
    
    temp = make_temp(grid)
    
    new_grid = rotate(grid, temp)
    
    if not clockwise:
        temp = make_temp(grid)
        new_grid = rotate(new_grid, temp)
    
    list_to_str(new_grid)
    return new_grid