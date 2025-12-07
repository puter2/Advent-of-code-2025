from functools import reduce

from reader import day6

file = 'input.txt'

homework = day6(file)
number_of_tasks = len(homework[0])
number_of_operands = len(homework)-1
operands = homework[-1]

results = []
for col in range(number_of_tasks):
    tmp_list = []
    for row in range(number_of_operands):
        tmp_list.append(int(homework[row][col]))
    if operands[col] == '+':
        res = reduce(lambda a, b: a+b, tmp_list)
    else:
        res = reduce(lambda a, b: a*b, tmp_list)
    results.append(res)

print(sum(results))
