from reader import day10
from solver import solve

#different approach, use linear programming,
#we want to minimize sum of button presses,
#button presses are limited by joltege
#example:
#buttons: (3) (1,3) (2) (2,3) (0,2) (0,1) joltage: {3,5,4,7}
#then constraints are as follows
# x5 + x6 = 3
# x2 + x6 = 5
# x3 + x4 + x5 = 4
# x1 + x2 + x4 = 7
file = 'input.txt'
machines = day10(file)
total_presses = 0
# print(press_button([0,0,0], (1,2)))
for i, machine in enumerate(machines):
    presses = solve(**machine)
    print(f'{presses} to configure this machine {i}')
    total_presses += presses
print(total_presses)