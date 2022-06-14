from collections import Counter
with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day14.txt") as puzzle_input:
    template = puzzle_input.readline().strip()
    puzzle_input.readline()
    rules = dict(line.strip().split(' -> ') for line in puzzle_input)
    
##print(template)
##print(rules)
##
##for i in range(40):
##    new_template = ""
##    for letter_index in range(len(template) - 1):
##        new_template += template[letter_index]
##        new_template += rules[template[letter_index:letter_index+2]]
##    new_template += template[letter_index+1]
##    template = new_template
##
##char_counts = Counter(template).most_common()
##print(char_counts[0][1] - char_counts[-1][1])

last_letter = template[-1]
template = Counter([template[c:c+2] for c in range(len(template) - 1)])
for i in range(40):
    new_template = Counter()
    for pair in template:
        middle = rules[pair]
        count = template[pair]
        new_template.update({pair[0] + middle: count, middle + pair[1]: count})
    template = new_template

letter_count = Counter()
for pair in template:
    letter_count.update({ pair[0]: template[pair]})
letter_count.update((last_letter))
        
print(letter_count.most_common()[0][1] - letter_count.most_common()[-1][1])
