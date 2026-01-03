from scipy.optimize import linprog
from reader import day10
path = 'testinput.txt'

def solve(joltage, buttons, **kwargs):
    to_minimize = [1 for i in range(len(buttons))]
    left_hand_side = []
    for current, limit in enumerate(joltage):
        tmp = []
        for index, button in enumerate(buttons):
            if current in button:
                tmp += [1]
            else:
                tmp += [0]
        left_hand_side.append(tmp)
    right_hand_side = list(joltage)
    solution = linprog(c=to_minimize, A_eq=left_hand_side, b_eq=right_hand_side, method='highs', integrality=1)
    return solution.get('fun')


if __name__=='__main__':
    data = day10(path)
    print(data[0])
    # to_minimize = [1 for i in range(len(data[0]['buttons']))]
    # left_hand_side = []
    # for current, limit in enumerate(data[0]['joltage']):
    #     tmp = []
    #     for index, button in enumerate(data[0]['buttons']):
    #         if current in button:
    #             tmp += [1]
    #         else:
    #             tmp += [0]
    #     left_hand_side.append(tmp)
    # print(to_minimize)
    # print(left_hand_side)
    # right_hand_side = list(data[0]['joltage'])
    # print(right_hand_side)
    # solution = linprog(c=to_minimize,A_eq=left_hand_side, b_eq=right_hand_side, method='highs', integrality=1)
    # print(solution.get('fun'))
    for d in data:
        print(solve(**d))