from collections import Counter

with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day8.txt") as input:
    output_sum = 0
    for line in input:
        line = line.split()
        sample = line[:10]
        
        seg_counts = Counter((seg for digit in sample for seg in digit))
        f = seg_counts.most_common()[0][0]
        b = seg_counts.most_common()[5][0]
        e = seg_counts.most_common()[6][0]
        for digit in sample:
            if len(digit) == 2:
                if digit[0] == f:
                    c = digit[1]
                else:
                    c = digit[0]

        output = line[11:]
        power = 3
        for d in output:
            #0123457689
            if len(d) in [2,3,4,7]:
                if len(d) == 2:
                    digit = 1
                elif len(d) == 3:
                    digit = 7
                elif len(d) == 4:
                    digit = 4
                else:
                    digit = 8
            elif len(d) == 5:
                #023569
                if f not in d:
                    digit = 2
                #03569
                elif b not in d:
                    digit = 3
                #0569
                else:
                    digit = 5
            #06
            elif e not in d:
                digit = 9
            elif c in d:
                digit = 0
            else:
                digit = 6
            output_sum += digit * pow(10, power)
            power -= 1
##        print(output_sum)
            
print(output_sum)

