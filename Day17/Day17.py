from math import ceil
with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day17.txt") as puzzle_input:
    line = puzzle_input.readline().strip()
    binary = f'{int(line, 16):0>{len(line) * 4}b}' # Convert hex to binary left padded with 0s

#target area: x=240..292, y=-90..-57

def model_y(v):
    s = 0
    while s > -90:
        s += v
        v -= 1
        yield s
        
def model_x(v):
    if v > 0:
        s = 0
        while s < 292 and v > 0:
            s += v
            v -= 1
            yield s
##            
##print(list(model_y(89)))
##print(list(model_x(22)))

def find_all_xys(min_x, max_x, min_y, max_y):
    # make assumptions about signs of targets cos cba
    smallest_x = int((2*min_x) ** 0.5)
    largest_y = abs(min_y) - 1
    print(smallest_x, max_x + 1, min_y, largest_y + 1)
    return sum(check_xy(x, y, min_x, max_x, min_y, max_y) for x in range(smallest_x, max_x + 1) for y in range(min_y, largest_y + 1))
    
    

def check_xy(v_x, v_y, min_x, max_x, min_y, max_y):
    s_x, s_y = 0, 0
    while s_x <= max_x and (v_x > 0 or s_x >= min_x) and s_y > min_y:
        s_x += v_x
        if v_x > 0:
            v_x -= 1
        
        s_y += v_y
        v_y -= 1
        if min_x <= s_x <= max_x and min_y <= s_y <= max_y:
            return True
    return False


print(find_all_xys(240, 292, -90,-57))
print(find_all_xys(20, 30, -10,-5))
