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
    first_value_index = find_index_of_max(bank,0, len(bank)-1)
    second_value_index = find_index_of_max(bank,first_value_index+1, len(bank))
    joltages.append(int(bank[first_value_index]+bank[second_value_index]))
print(joltages)
print(sum(joltages))