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
        letter = line[0]
        number = int(line[1:].strip())
        position = instructions[letter](position, number)
        if position == 0:
            code+=1
        print(f'dial at {position}')

print(f'the code is {code}')