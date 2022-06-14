from itertools import islice
cmds = []
with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day24.txt") as puzzle_input:
        for line in puzzle_input:
                cmds.append(line.strip().split())

##for i in range(18):
##    for cmd in cmds[i::18]:
##        print(cmd)
##    print()

##def check_simplification(candidate, cmds = cmds):
##        candidate_iter = (int(digit) for digit in str(candidate))
##        wxyz = { var: 0 for var in "wxyz"}
##        for cmd in cmds:
##                if cmd[0] == "inp":
##                        wxyz[cmd[1]] = next(candidate_iter)
##                        print(wxyz["z"])
##                else:
##                        if (arg := wxyz.get(cmd[2])) == None:
##                                arg = int(cmd[2])
##                        match cmd[0]:
##                                case "add":
##                                        wxyz[cmd[1]] += arg
##                                case "mul":
##                                        wxyz[cmd[1]] *= arg
##                                case "div":
##                                        wxyz[cmd[1]] //= arg
##                                case "mod":
##                                        wxyz[cmd[1]] %= arg
##                                case "eql":
##                                        wxyz[cmd[1]] = int(wxyz[cmd[1]] == arg)
##        print(wxyz["z"], test_candidate(candidate))
##        return wxyz["z"] == test_candidate(candidate)
        

def ingest_digit(w, a, b, c, z):
        x = (z % 26) + a != w
        z //= b
        if x:
                z = z*26 + w + c # RHS >= 1

        return z


##w5 == w4 - 2
##w8 == w7 - 4
##w10 == w9 - 8
##w11 == w6 + 6
##w12 == w3 + 7
##w13 == w2 + 8
##w14 == w1 - 6

def test_candidate(candidate):
        A = iter([14, 13, 15, 13, -2, 10, 13, -15, 11, -9, -9, -7, -4, -6])
        B = iter([1, 1, 1, 1, 26, 1, 1, 26, 1, 26, 26, 26, 26, 26])
        C = iter([0, 12, 14, 0, 3, 15, 11, 12, 1, 12, 3, 10, 14, 12])
        z = 0
        candidate = (int(digit) for digit in str(candidate))
        for digit in candidate:
##              print(i, digit)
                z = ingest_digit(digit, next(A), next(B), next(C), z)
                print(z)
                print()
##        return z == 0
        return z
        


def calc_max_input():
        A = [14, 13, 15, 13, -2, 10, 13, -15, 11, -9, -9, -7, -4, -6]
        # if A greater than 9, x will always be true as w ranges from 1-9
        # x_always_true = [a > 9 for a in A]
        x_always_true = [True, True, True, True, False, True, True, False, True, False, False, False, False, False]
        B = [1, 1, 1, 1, 26, 1, 1, 26, 1, 26, 26, 26, 26, 26]
        C = [0, 12, 14, 0, 3, 15, 11, 12, 1, 12, 3, 10, 14, 12]
        ABC = list(zip(A,B,C))
        # w + c has maximum of 24
        # implies we can never end up with z = 0 when processing a digit if x = 1
        
        # for first x = True (1st digit), z = w + c
        # z_1 = w_1 + c_1 = w_1
        # z_2 = 26(w_1) + w_2 + c_2 = 26(w_1) + w_2 + 12
        # z_3 = 26(z_2) + w_3 + c_3 = 26^2(w_1) + 26(w_2) + 26(12) + (w_3) + 14
        # z_4 = 26(z_3) + w_4 + c_4 = 26^3(w_1) + 26^2(w_2) + 26(w_3) +  26^2(12) + 26(14) + w_4
        # (z_4 % 26) + a_5 = w_4 - 2

        # we must divide by 26 1 more time than we multiply by 26 to get to 0
        # x is true 7 times, however the first time x is true z == 0, so we multiply by 26 6 times
        # we divide by 26 7 times, therefore there we must have x = false whereever possible

        z_list = [0]
        current_digit = 0
        candidate = ""
        go_back = False
        print_count = 0
        while True:
                print_count += 1
                if x_always_true[current_digit]:
                        if len(candidate) == current_digit:
                                candidate += '9'
                                z_list.append(ingest_digit(9, *ABC[current_digit], z_list[current_digit]))
                                current_digit += 1

                        elif candidate[current_digit] == '1':
                                candidate = candidate[:-1]
                                current_digit -= 1
                                z_list.pop()
                                go_back = True
                        else:
                                digit_candidate = int(candidate[-1]) - 1
                                candidate = f"{candidate[:-1]}{digit_candidate}"
                                z_list[current_digit + 1] = ingest_digit(digit_candidate, *ABC[current_digit], z_list[current_digit])
                                current_digit += 1
                                go_back = False
                else:
                        if go_back:
                                candidate = candidate[:-1]
                                current_digit -= 1
                                z_list.pop()
                        if len(candidate) == current_digit:
                                digit_candidate = (z_list[current_digit] % 26) + A[current_digit]
                                if 1 <= digit_candidate <= 9:
                                        candidate += str(digit_candidate)
                                        z_list.append(ingest_digit(digit_candidate, *ABC[current_digit], z_list[current_digit]))
                                        current_digit += 1
                                else:
                                        current_digit -= 1
                                        go_back = True
                if len(candidate) == 14:
                        return candidate
                                
def calc_min_input():
        A = [14, 13, 15, 13, -2, 10, 13, -15, 11, -9, -9, -7, -4, -6]
        x_always_true = [True, True, True, True, False, True, True, False, True, False, False, False, False, False]
        B = [1, 1, 1, 1, 26, 1, 1, 26, 1, 26, 26, 26, 26, 26]
        C = [0, 12, 14, 0, 3, 15, 11, 12, 1, 12, 3, 10, 14, 12]
        ABC = list(zip(A,B,C))

        z_list = [0]
        current_digit = 0
        candidate = ""
        go_back = False
        print_count = 0
        while True:
                print_count += 1
                if x_always_true[current_digit]:
                        if len(candidate) == current_digit:
                                candidate += '1'
                                z_list.append(ingest_digit(1, *ABC[current_digit], z_list[current_digit]))
                                current_digit += 1

                        elif candidate[current_digit] == '9':
                                candidate = candidate[:-1]
                                current_digit -= 1
                                z_list.pop()
                                go_back = True
                        else:
                                digit_candidate = int(candidate[-1]) + 1
                                candidate = f"{candidate[:-1]}{digit_candidate}"
                                z_list[current_digit + 1] = ingest_digit(digit_candidate, *ABC[current_digit], z_list[current_digit])
                                current_digit += 1
                                go_back = False
                else:
                        if go_back:
                                candidate = candidate[:-1]
                                current_digit -= 1
                                z_list.pop()
                        if len(candidate) == current_digit:
                                digit_candidate = (z_list[current_digit] % 26) + A[current_digit]
                                if 1 <= digit_candidate <= 9:
                                        candidate += str(digit_candidate)
                                        z_list.append(ingest_digit(digit_candidate, *ABC[current_digit], z_list[current_digit]))
                                        current_digit += 1
                                else:
                                        current_digit -= 1
                                        go_back = True
                if len(candidate) == 14:
                        return candidate
##                if print_count % 1000 == 0:
##                        print(candidate, current_digit, print_count)



print(calc_max_input())
print(calc_min_input())
