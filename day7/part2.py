from reader import day7

def advance_until_next_splitter(splitters, node, height):
    while node not in splitters and node[1] < height:
        node = (node[0], node[1] + 1)
    return node

file = 'input.txt'

splitters, start, height = day7(file)

'''
idea:
label each splitter with number of paths to the bottom from that splitter starting from bottom
splitters at the bottom will have only two paths
each higher splitter must check, if there's a next splitter below to the left and to the right,
if there is a splitter to the below-left then add it's number of paths to current splitter label, otherwise add 1
similarly with below-right
use the same rule with start node
label on the start node is the total number of paths
'''

number_of_paths = {
    start : 0,
}

splitters_sorted = sorted({*splitters, start}, key = lambda a: a[1], reverse=True)

for splitter in splitters_sorted:
    curr_height = splitter[1]
    left = (splitter[0] - 1, curr_height + 1)
    right = (splitter[0] + 1, curr_height + 1)
    left = advance_until_next_splitter(splitters, left, height)
    right = advance_until_next_splitter(splitters, right, height)
    number_of_paths[splitter] = 0
    number_of_paths[splitter] += 1 if left[1]>=height else number_of_paths[left]
    number_of_paths[splitter] += 1 if right[1] >= height else number_of_paths[right]

print(number_of_paths[start])