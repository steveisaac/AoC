from numpy import array

def flash(y, x, cavern):
    flash_count = 1
    for check_y, check_x in get_adjacent(y, x, len(cavern), len(cavern[0])):
        if cavern[check_y][check_x] < 9:
            cavern[check_y][check_x] += 1
        elif cavern[check_y][check_x] == 9:
            cavern[check_y][check_x] = 11
            flash_count += flash(check_y, check_x, cavern)
    return flash_count

def get_adjacent(y, x, rows, cols):
    if y > 0:
        if x > 0:
            yield (y-1, x-1)
        yield (y-1, x)
        if x < cols - 1:
            yield (y-1, x+1)
    if x > 0:
        yield (y, x-1)
    if x < cols - 1:
        yield (y, x+1)
    if y < rows - 1:
        if x > 0:
            yield (y+1, x-1)
        yield (y+1, x)
        if x < cols - 1:
            yield (y+1, x+1)

with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day11.txt") as input:
    cavern = [[int(octo) + 1 for octo in row.strip()] for row in input]

##flash_count = 0
##
##print(cavern)
##for step in range(100):
##    for y in range(len(cavern)):
##        for x in range(len(cavern[0])):
##            if cavern[y][x] == 10:
##                flash_count += flash(y, x, cavern)
##    cavern = [[int(octo) + 1 if octo < 10 else 1 for octo in row] for row in cavern]
##print(flash_count)
##



print(cavern)
step = 0
octo_count = len(cavern) * len(cavern[0])
while True:
    step += 1
    flash_count = 0
    for y in range(len(cavern)):
        for x in range(len(cavern[0])):
            if cavern[y][x] == 10:
                flash_count += flash(y, x, cavern)
    if flash_count == octo_count:
        print(step)
        break
    cavern = [[int(octo) + 1 if octo < 10 else 1 for octo in row] for row in cavern]


