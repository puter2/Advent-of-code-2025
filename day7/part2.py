from reader import day7

file = 'input.txt'

splitters, start, height = day7(file)

# rekurencja
paths = []
def find_paths(start_path:list, next_step:tuple):
    # input()
    next_height = next_step[1]
    print(next_height, next_step)
    if next_step in splitters:
        left = (next_step[0] - 1, next_height + 1)
        right = (next_step[0] + 1, next_height + 1)
        left_path = [*start_path, left]
        right_path = [*start_path, right]
        find_paths(left_path, left)
        find_paths(right_path, right)
    else:
        global height
        if next_height >= height:
            global paths
            paths.append(start_path.copy())
        else:
            next_next_step = (next_step[0], next_height + 1)
            down_path = [*start_path]
            find_paths(down_path, next_next_step)

next_step = (start[0], 1)
find_paths([start], next_step)
for path in paths:
    print(path)
print(len(paths))