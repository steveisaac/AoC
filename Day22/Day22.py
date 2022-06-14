##steps = []
##with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day22.txt") as puzzle_input:
##        for line in puzzle_input:
##                on = line[1] == "n"
##                cuboid = [[a for a in i.split("=")[1].split("..")] for i in line.strip().split(",")]
##                cuboid = [(int(a), int(b)+1) for a,b in cuboid]
####                cuboid = [(max(min(int(a), 51), -50), max(min(int(b)+1, 51), -50)) for a,b in cuboid]
##                steps.append((on, *cuboid))
####                print(steps[-1])
##
##
##on_cubes = set()
##for on, x_range, y_range, z_range in steps:
##        if on:
##                on_cubes |= {(x, y, z) for x in range(*x_range) for y in range(*y_range) for z in range(*z_range)}
##        else:
##                on_cubes -= {(x, y, z) for x in range(*x_range) for y in range(*y_range) for z in range(*z_range)}
##        print(len(on_cubes))
##
##print()

def overlaps(new_cub, old_cub):
        new_x_min, new_x_max, new_y_min, new_y_max, new_z_min, new_z_max = new_cub
        old_x_min, old_x_max, old_y_min, old_y_max, old_z_min, old_z_max = old_cub
        if new_x_min > old_x_max or new_x_max < old_x_min or new_y_min > old_y_max or new_y_max < old_y_min or new_z_min > old_z_max or new_z_max < old_z_min:
                return False
        return True

def remove_overlap(new_cub, old_cub):
        new_x_min, new_x_max, new_y_min, new_y_max, new_z_min, new_z_max = new_cub
        old_x_min, old_x_max, old_y_min, old_y_max, old_z_min, old_z_max = old_cub
        if new_x_min > old_x_max or new_x_max < old_x_min or new_y_min > old_y_max or new_y_max < old_y_min or new_z_min > old_z_max or new_z_max < old_z_min:
                return [new_cub]
        new_cubes = []
        if new_x_min < old_x_min:
                new_cubes.append((new_x_min, old_x_min-1, new_y_min, new_y_max, new_z_min, new_z_max))
                new_x_min = old_x_min
        if new_x_max > old_x_max:
                new_cubes.append((old_x_max+1, new_x_max, new_y_min, new_y_max, new_z_min, new_z_max))
                new_x_max = old_x_max
        if new_y_min < old_y_min:
                new_cubes.append((new_x_min, new_x_max, new_y_min, old_y_min-1, new_z_min, new_z_max))
                new_y_min = old_y_min
        if new_y_max > old_y_max:
                new_cubes.append((new_x_min, new_x_max, old_y_max+1, new_y_max, new_z_min, new_z_max))
                new_y_max = old_y_max
        if new_z_min < old_z_min:
                new_cubes.append((new_x_min, new_x_max, new_y_min, new_y_max, new_z_min, old_z_min-1))
        if new_z_max > old_z_max:
                new_cubes.append((new_x_min, new_x_max, new_y_min, new_y_max, old_z_max+1, new_z_max))
        return new_cubes

steps = []
with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day22.txt") as puzzle_input:
        for line in puzzle_input:
                on = line[1] == "n"
                cuboid = tuple(int(j) for i in line.strip().split(",") for j in i.split("=")[1].split(".."))
                steps.append((on, cuboid))
                
on_cuboids = []
for on, cuboid in steps:
        if on:
                cuboids_to_add = [cuboid]
                for oc in on_cuboids:
                        temp_cuboids_to_add = []
                        for cuboid in cuboids_to_add:
                                temp_cuboids_to_add += remove_overlap(cuboid, oc)
                        cuboids_to_add = temp_cuboids_to_add
                on_cuboids += cuboids_to_add
        else:
                for i in range(len(on_cuboids)-1,-1,-1):
                        if overlaps(cuboid, on_cuboids[i]):
                                on_cuboids += remove_overlap(on_cuboids.pop(i), cuboid)
                
on_cubes = 0
for c in on_cuboids:
        on_cubes += (abs(c[0] - c[1]) + 1) * (abs(c[2] - c[3]) + 1) * (abs(c[4] - c[5]) + 1)
print(on_cubes)
