with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day12.txt") as input:
    edges = [[node for node in row.strip().split("-")] for row in input ]

adjacent_nodes = {}
for x, y in edges:
    if x in adjacent_nodes:
        adjacent_nodes[x].append(y)
    else:
        adjacent_nodes[x] = [y]
    
    if y in adjacent_nodes:
        adjacent_nodes[y].append(x)
    else:
        adjacent_nodes[y] = [x]

##curr_paths = [["start"]]
##valid_paths = 0
##while len(curr_paths) > 0:
##    new_paths = []
##    for path in curr_paths:
##        for next_node in adjacent_nodes[path[-1]]:
##            if next_node == 'end':
##                valid_paths += 1
##            elif next_node.isupper() or next_node not in path:
##                new_paths.append(path + [next_node])
##    curr_paths = new_paths
##print(valid_paths)

curr_paths = [['start']]
valid_paths = 0
while len(curr_paths) > 0:
    new_paths = []
    for path in curr_paths:
        for next_node in adjacent_nodes[path[-1]]:
            if next_node == 'end':
                valid_paths += 1
            elif next_node.isupper() or next_node not in path:
                new_paths.append(path + [next_node])
            elif '' not in path and next_node != 'start':
                new_paths.append(path + ['', next_node])
    curr_paths = new_paths
print(valid_paths)
