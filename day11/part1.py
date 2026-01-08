from reader import day11

file = 'testinput.txt'
data = day11(file)

started_paths = [['you']]
finished_paths = []
while started_paths:
    curr_path = started_paths.pop(0)
    last_machine = curr_path[-1]
    for next_machine in data[last_machine]:
        new_path = curr_path.copy() + [next_machine]
        if next_machine == 'out':
            finished_paths.append(new_path)
        else:
            started_paths.append(new_path)

print(finished_paths)
print(len(finished_paths))

def find_backwards_neghborhoods(neighbors_list):
    backwards = { key : [] for key in neighbors_list}
    for key in neighbors_list:
        for vert in neighbors_list[key]:
            backwards[vert].append(key)

    return backwards

def find_all_paths_linear(neighbors_list, start, end):
    processed_vertices = []
    waiting_to_be_processed = [start]
