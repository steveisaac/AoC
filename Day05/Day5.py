with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day5.txt") as input:
    lines = []
    for l in input:
        start, _, end = l.split()
        
        lines.append(start.split(",") + end.split(","))
lines = [[int(val) for val in line] for line in lines]

### filter for cardinal lines
##lines = [line for line in lines if line[0] == line[2] or line[1] == line[3]]

point_dict = {}
for line in lines:
    if line[0] == line[2]:
        x_range = [line[0] for i in range(abs(line[1]-line[3]) + 1)]
    else:
        draw_direction = 1 if line[0] < line[2] else -1
        x_range = range(line[0], line[2] + draw_direction, draw_direction)

    if line[1] == line[3]:
        y_range = [line[1] for i in range(abs(line[0]-line[2]) + 1)]
    else:
        draw_direction = 1 if line[1] < line[3] else -1
        y_range = range(line[1], line[3] + draw_direction, draw_direction)
        
    for point in zip(x_range, y_range):
        if point in point_dict:
            point_dict[point] += 1
        else:
            point_dict[point] = 1

points = [point for point, count in point_dict.items() if count > 1]
print(len(points))
