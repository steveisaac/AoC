from collections import Counter
grid = []
with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day15.txt") as puzzle_input:
    for line in puzzle_input:
        grid.append([int(i) for i in line.strip()])

    grid = [[el + i + j if el + i + j < 10 else (el + i + j) % 9 for i in range(5) for el in row] for j in range(5) for row in grid]

##[print(row) for row in grid]

max_x = len(grid[0]) - 1
max_y = len(grid) - 1

searching = True
visited = {(0,0)}
explore_candidates = {0: [(0,0)]}
final_risk = None

while searching:
    risk = min(explore_candidates)
    candidates = explore_candidates.pop(risk)
    for candidate in candidates:
        x, y = candidate
        if x < max_x:
            new_candidate = (x+1, y)
            if new_candidate not in visited:
                visited.add(new_candidate)
                new_risk = risk + grid[y][x+1]
                if new_candidate == (max_x, max_y):
                    searching = False
                    final_risk = new_risk
                    break
                if new_risk in explore_candidates:
                    explore_candidates[new_risk].append(new_candidate)
                else:
                    explore_candidates[new_risk] = [new_candidate]
        if x > 0:
            new_candidate = (x-1, y)
            if new_candidate not in visited:
                visited.add(new_candidate)
                new_risk = risk + grid[y][x-1]
                if new_risk in explore_candidates:
                    explore_candidates[new_risk].append(new_candidate)
                else:
                    explore_candidates[new_risk] = [new_candidate]
        if y < max_y:
            new_candidate = (x, y+1)
            if new_candidate not in visited:
                visited.add(new_candidate)
                new_risk = risk + grid[y+1][x]
                if new_candidate == (max_x, max_y):
                    searching = False
                    final_risk = new_risk
                    break
                if new_risk in explore_candidates:
                    explore_candidates[new_risk].append(new_candidate)
                else:
                    explore_candidates[new_risk] = [new_candidate]
        if y > 0:
            new_candidate = (x, y-1)
            if new_candidate not in visited:
                visited.add(new_candidate)
                new_risk = risk + grid[y-1][x]
                if new_risk in explore_candidates:
                    explore_candidates[new_risk].append(new_candidate)
                else:
                    explore_candidates[new_risk] = [new_candidate]

print(final_risk)
