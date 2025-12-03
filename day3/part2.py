from functools import reduce

from reader import day3

def find_index_of_max(sequence, start, end):
    max_val = int(sequence[start])
    pos = start
    for i in range(start, end):
        if int(sequence[i])>max_val:
            max_val = int(sequence[i])
            pos = i
    return pos


banks = day3('input.txt')
joltages = []
for bank in banks:
    indices = []
    for battery_number in range(12,0,-1):
        last_finished_at_index = indices[-1] if len(indices)>0 else -1
        indices.append(find_index_of_max(bank, last_finished_at_index+1, len(bank) - battery_number+1))
    combination = ''
    print(indices)
    for index in indices:
        combination += bank[index]
    joltages.append(int(combination))
print(joltages)
print(sum(joltages))

