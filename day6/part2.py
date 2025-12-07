from functools import reduce

from reader import day6_part2
import re

file = 'input.txt'

homework = day6_part2(file).strip()
# find all operators
last_line_index = homework.rfind('\n')
operators = homework[last_line_index+1:]
operators = re.sub(r'\s+', ' ', operators).split()

# find all operands
numbers = homework[:last_line_index]
lines = numbers.split('\n')
lengths = [len(l) for l in lines]
max_size = max(lengths)
operands = []
tmp_list = []
for char_number in range(max_size):
    number = ''
    for row in lines:
        try:
            read_char=row[char_number]
        except IndexError:
            continue
        number+=read_char
    number = number.replace(' ','')
    if number:
        # case: column is not empty
        tmp_list.append(int(number.strip()))
    else:
        # case: column was all spaces
        operands.append(tmp_list)
        tmp_list = []

operands.append(tmp_list)
results = []
for col_num in range(len(operators)):
    res = 0
    if operators[col_num] == '+':
        res = reduce(lambda a, b: a+b, operands[col_num])
    else:
        res = reduce(lambda a, b: a*b, operands[col_num])
    results.append(res)
print(sum(results))