with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day16.txt") as puzzle_input:
    line = puzzle_input.readline().strip()
    binary = f'{int(line, 16):0>{len(line) * 4}b}' # Convert hex to binary left padded with 0s

##cursor = 0
##version_sum = 0
##while int(binary[cursor:], 2) > 0:
##    version_sum += int(binary[cursor:cursor+3], 2)
##    cursor += 3
##    version_type = int(binary[cursor:cursor+3], 2)
##    cursor += 3
##    # Move cursor past groups
##    if version_type == 4:
##        more_groups = True
##        while more_groups:
##            if binary[cursor] == '0':
##                more_groups = False
##            cursor += 5
##    # Move cursor past operator packets
##    else:
##        if binary[cursor] == '0':
##            cursor += 1
##            cursor += 15
##        else:
##            cursor += 1
##            cursor += 11
##print(version_sum)

def parse_packet(binary, char_index):
    packet_type_ID = int(binary[char_index+3:char_index+6], 2)
    char_index += 6

    # Return literal
    if packet_type_ID == 4:
        more_groups = True
        value = ""
        while more_groups:
            if binary[char_index] == "0":
                more_groups = False
            value += binary[char_index+1:char_index+5]
            char_index += 5
        return int(value, 2), char_index

    sub_packets = []
    if binary[char_index] == "0":
        char_index += 16
        sub_packet_end = char_index + int(binary[char_index - 15:char_index], 2)
        while char_index < sub_packet_end:
            val, char_index = parse_packet(binary, char_index)
            sub_packets.append(val)
    else:
        char_index += 12
        sub_packet_count = int(binary[char_index - 11:char_index], 2)
        for i in range(sub_packet_count):
            val, char_index = parse_packet(binary, char_index)
            sub_packets.append(val)
            
    match packet_type_ID:
        case 0:
            result = sum(sub_packets)
        case 1:
            result = 1
            [result := result * packet for packet in sub_packets]
        case 2:
            result = min(sub_packets)
        case 3:
            result = max(sub_packets)
        case 5:
            result = int(sub_packets[0] > sub_packets[1])
        case 6:
            result = int(sub_packets[0] < sub_packets[1])
        case 7:
            result = int(sub_packets[0] == sub_packets[1])

    return result, char_index

print(parse_packet(binary, 0)[0])
