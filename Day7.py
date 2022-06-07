from statistics import mean
with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day7.txt") as input:
    crabs = [int(f) for f in input.readline().split(",")]


middle = int(mean(crabs))
movements_l = [abs(crab-middle) * (abs(crab-middle) + 1) * 0.5 for crab in crabs]
middle += 1
movements_u = [abs(crab-middle) * (abs(crab-middle) + 1) * 0.5 for crab in crabs]
print(min(sum(movements_l),sum(movements_u)))
