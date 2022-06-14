from collections import Counter

with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day10.txt") as input:
    lines = [line.strip() for line in input]

##openers = ("(", "{", "[", "<")
##closers = { "(": ")", "{": "}", "[": "]", "<": ">"}
##points = { ")": 3, "]": 57, "}": 1197, ">": 25137}
##score = 0
##for line in lines:
##    char_stack = []
##    for char in line:
##        if char in openers:
##            char_stack += char
##        else:
##            if char != closers[char_stack.pop()]:
##                score += points[char]
##print(score)

openers = ("(", "{", "[", "<")
closers = { "(": ")", "{": "}", "[": "]", "<": ">"}
points = { ")": 1, "]": 2, "}": 3, ">": 4}
scores = []
for line in lines:
    corrupt = False
    char_stack = []
    for char in line:
        if char in openers:
            char_stack += char
        else:
            if char != closers[char_stack.pop()]:
                corrupt = True
                break
    if corrupt:
        continue
    score = 0
    for i in range(len(char_stack)):
        score *= 5
        score += points[closers[char_stack.pop()]]
    scores.append(score)
scores.sort()        
print(scores[len(scores) // 2])
