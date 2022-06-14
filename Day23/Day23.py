##steps = []
rows = []
char_to_digit = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day23.txt") as puzzle_input:
        puzzle_input.readline()
        puzzle_input.readline()
        for line in puzzle_input:
                if line[3] != '#':
                        rows.append([char_to_digit[c] for c in line.strip() if c != '#'])
        rooms = [[j[i] for j in rows] for i in range(4)]

print(rooms)
open_spaces = [(-1, i) for i in [0,1,3,5,7,9,10]]
corridor = [None for i in range(11)]
# for i in range(4):
#         for j in range(3,-1,-1):
#                 if rooms[i][j] == pow(10,i):
#                         rooms[i].pop(j)
#                 else:
#                         break
print(rooms)

# unfinished = False
# while unfinished:


# s = sum(sum(i) for i in rooms)
