grid = []
with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day25.txt") as puzzle_input:
    for line in puzzle_input:
        grid += [list(line.strip())]

height = len(grid)
width = len(grid[0])

iterations = 0

changed = True
while changed:
    iterations += 1
##    for i in grid:
##        print("".join(i))
##    print()
    changed = False
    newgrid = [[None for i in range(width)] for j in range(height)]
    for row_index in range(height):
        for col_index in range(width - 1):
            if newgrid[row_index][col_index]:
                continue
            if grid[row_index][col_index] == '>' and grid[row_index][col_index + 1] == '.':
                newgrid[row_index][col_index], newgrid[row_index][col_index + 1] = '.', '>'
                changed = True
            else:
                newgrid[row_index][col_index] = grid[row_index][col_index]
        if newgrid[row_index][-1]:
            continue
        if grid[row_index][-1]  == '>' and grid[row_index][0] == '.':
                newgrid[row_index][-1], newgrid[row_index][0] = '.', '>'
                changed = True
        else:
            newgrid[row_index][-1] = grid[row_index][-1]
    grid = newgrid
    
    newgrid = [[None for i in range(width)] for j in range(height)]
    for col_index in range(width):
        for row_index in range(height - 1):
            if newgrid[row_index][col_index]:
                continue
            if grid[row_index][col_index] == 'v' and grid[row_index+1][col_index] == '.':
                newgrid[row_index][col_index], newgrid[row_index+1][col_index] = '.', 'v'
                changed = True
            else:
                newgrid[row_index][col_index] = grid[row_index][col_index]
        if newgrid[-1][col_index]:
            continue
        if grid[-1][col_index]  == 'v' and grid[0][col_index] == '.':
                newgrid[-1][col_index], newgrid[0][col_index] = '.', 'v'
                changed = True
        else:
            newgrid[-1][col_index] = grid[-1][col_index]

    grid = newgrid

print(iterations)
