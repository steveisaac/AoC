from collections import Counter

with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day9.txt") as input:
    heightmap = [[int(digit) for digit in row.strip()] for row in input]
    
risk_sum = 0
low_points = []
for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        low = True
        val = heightmap[y][x]
        if x > 0 and low:
            low = val < heightmap[y][x-1]
        if x < len(heightmap[0]) - 1 and low:
            low = val < heightmap[y][x+1]
        if y > 0 and low:
            low = val < heightmap[y-1][x]
        if y < len(heightmap) - 1 and low:
            low = val < heightmap[y+1][x]
        if low:
            low_points.append((y,x))

basin_sizes = []
for start in low_points:
    search = {start}
    searched = set()
    while len(search) > 0:
        new_search = set()
##        print(search)
##        print(searched)
        for point in search:
            searched.add(point)
            y, x = point
            val = heightmap[y][x]
            
            if x > 0 and (y, x-1) not in searched and heightmap[y][x-1] < 9:
                new_search.add((y, x-1))
            if x < len(heightmap[0]) - 1 and (y, x+1) not in searched and heightmap[y][x+1] < 9:
                new_search.add((y, x+1))
            if y > 0 and (y-1, x) not in searched and heightmap[y-1][x] < 9:
                new_search.add((y-1, x))
            if y < len(heightmap) - 1 and (y+1, x) not in searched and heightmap[y+1][x] < 9:
                new_search.add((y+1, x))
        search = new_search
    basin_sizes.append(len(searched))

##    break
prd = 1
[prd := prd * el for el in sorted(basin_sizes,reverse=True)[:3]]
print(prd)
