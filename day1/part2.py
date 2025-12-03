from math import floor


def turn_left(position, number):
    return (position - number) % 100

def turn_right(position, number):
    return (position + number) % 100

instructions = {
    'L' : turn_left,
    'R' : turn_right
}

input_file='input.txt'
position = 50
code = 0

print(f'dial at {position}')
with open(input_file) as file:
    for line in file.readlines():
        direction = line[0]
        number = int(line[1:].strip())
        code += floor(number/100)
        number = number % 100
        new_position = instructions[direction](position, number)
        if new_position == 0 or (new_position > position != 0 and direction == 'L') or (new_position < position != 0 and direction == 'R'):
            code+=1
            print(f'crossed 0, current code: {code}')
        position=new_position
        print(f'dial at {position}')

print(f'the code is {code}')