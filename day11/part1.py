from reader import day11

file = 'input.txt'
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
