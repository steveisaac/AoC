import numpy

##with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day20.txt") as puzzle_input:
##        pixelmap = [1 if c == "#" else 0 for c in puzzle_input.readline().strip()]
##        puzzle_input.readline()
##        for line in puzzle_input:
##                image.append([1 if c == "#" else 0 for c in line.strip()])




##def g1():
##        while True:
##                yield 6
##                yield 4
##                yield 2
##                yield 0
##                yield 8
##
##                
##def g2():
##        while True:
##                yield 5
##                yield 3
##                yield 1
##                yield 9
##                yield 7
##
##pos1 = 4
##pos2 = 8
##score1 = 0
##score2 = 0
##d1 = g1()
##d2 = g2()
##rolls = 0
##while True:
##        rolls += 3
##        pos1 += next(d1)
##        if pos1 > 10:
##                pos1 -= 10
##        score1 += pos1
##        if score1 >= 1000:
##                break
##        rolls += 3
##        pos2 += next(d2)
##        if pos2 > 10:
##                pos2 -= 10
##        score2 +=pos2
##        if score2 >= 1000:
##                break
##
##print(rolls)
##print(score1,score2)



p1wins, p2wins = 0, 0

player_ones_turn = True

rolls = ((3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1))
states = {(0, 0, 6, 7):1}

while len(states) > 0:
        next_states = {}
        for k in states:
                occurrences = states[k]
                score_one, score_two, pos_one, pos_two = k
                if score_one > 20:
                        p1wins += occurrences
                        continue
                if score_two > 20:
                        p2wins += occurrences
                        continue
                for roll, n in rolls:
                        if player_ones_turn:
                                if (score_one + 1 + ((pos_one + roll) % 10), score_two, (pos_one + roll) % 10, pos_two) in next_states:
                                        next_states[(score_one + 1 + ((pos_one + roll) % 10), score_two, (pos_one + roll) % 10, pos_two)] += n * occurrences
                                else:
                                        next_states[(score_one + 1 + ((pos_one + roll) % 10), score_two, (pos_one + roll) % 10, pos_two)] = n * occurrences
                        else:
                                if (score_one, score_two + 1 + ((pos_two + roll) % 10), pos_one, (pos_two + roll) % 10) in next_states:
                                        next_states[(score_one, score_two + 1 + ((pos_two + roll) % 10), pos_one, (pos_two + roll) % 10)] += n * occurrences
                                else:
                                        next_states[(score_one, score_two + 1 + ((pos_two + roll) % 10), pos_one, (pos_two + roll) % 10)] = n * occurrences
        player_ones_turn = not player_ones_turn
        states = next_states
##        print(states)
##        break
                        
print(p1wins, p2wins)

