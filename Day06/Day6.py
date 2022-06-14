with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day6.txt") as input:
    fish = [int(f) for f in input.readline().split(",")]

##def breed(fish):
##    for f in fish:
##        if f == 0:
##            yield 6
##            yield 8
##        else:
##            yield f - 1
##
####print(list(fish))
##for i in range(256):
##    print(i)
##    fish = breed(fish)
####
##print(len(list(fish)))


from collections import Counter
fish_counts = Counter(fish)
for i in range(256):
    fish_counts[0], fish_counts[1], fish_counts[2], fish_counts[3], fish_counts[4], fish_counts[5], fish_counts[6], fish_counts[7], fish_counts[8] = fish_counts[1], fish_counts[2], fish_counts[3], fish_counts[4], fish_counts[5], fish_counts[6], fish_counts[7] + fish_counts[0], fish_counts[8], fish_counts[0]

print(sum([fish_counts[i] for i in fish_counts]))
