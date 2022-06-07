with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day13.txt") as puzzle_input:
    read_dots = True
    dots = set()
    commands = []
    for line in puzzle_input:
        line = line.strip()
        if read_dots:
            if line == '':
                read_dots = False
                continue
            dots.add(tuple(map(int, line.split(','))))
        else:
            command, val = line.split('=')
            commands.append((command[-1], int(val)))
##print(dots)
print(len(dots))
print(commands)

for axis, val in commands:
    if axis == 'x':
        dots = {(x, y) if x < val else (2*val - x, y) for x, y in dots}
    
    elif axis == 'y':
        dots = {(x, y) if y < val else (x, 2*val - y) for x, y in dots}

max_x = max((x for x, y in dots))
max_y = max((y for x, y in dots))
for y in range(max_y + 1):
    print(''.join(['#' if (x,y) in dots else ' ' for x in range(max_x + 1)]))
