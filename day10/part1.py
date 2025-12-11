from traceback import print_tb

from reader import day10

def press_button(lights, button):
    new_lights = ''
    for i in range(len(lights)):
        if i in button:
            if lights[i] == '.':
                new_lights += '#'
            else:
                new_lights += '.'
        else:
            new_lights += lights[i]
    return new_lights

def presses_to_turn_on(lights, buttons, **kwargs):
    start_position = '.' * len(lights)
    positions = {start_position:0}
    to_test = [start_position]
    while to_test:
        position = to_test.pop(0)
        press_number = positions[position]
        for button in buttons:
            pos_after_pressing = press_button(position, button)
            if positions.get(pos_after_pressing) is None:
                to_test.append(pos_after_pressing)
                positions[pos_after_pressing] = press_number+1
        if positions.get(lights) is not None:
            return positions.get(lights)
    return positions

file = 'input.txt'
machines = day10(file)
total_presses = 0
for machine in machines:
    presses = presses_to_turn_on(**machine)
    total_presses += presses
print(total_presses)