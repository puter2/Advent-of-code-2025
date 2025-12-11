from reader import day10

def press_button(joltage, button):
    new_joltage = [j for j in joltage]
    for i in button:
        new_joltage[i] += 1
    return tuple(new_joltage)

def presses_to_configure(joltage, buttons, **kwargs):
    start_position = tuple([0 for i in range(len(joltage))])
    positions = {start_position:0}
    to_test = [start_position]
    while to_test:
        position = to_test.pop(0)
        press_number = positions[position]
        for button in buttons:
            joltage_after_pressing = press_button(position, button)
            if positions.get(joltage_after_pressing) is None:
                for i in range(len(joltage)):
                    if joltage_after_pressing[i]>joltage[i]:
                        continue
                to_test.append(joltage_after_pressing)
                positions[joltage_after_pressing] = press_number+1
        if positions.get(joltage) is not None:
            return positions.get(joltage)
    return positions

file = 'input.txt'
machines = day10(file)
total_presses = 0
# print(press_button([0,0,0], (1,2)))
for i, machine in enumerate(machines):
    presses = presses_to_configure(**machine)
    print(f'{presses} to configure this machine {i}')
    total_presses += presses
print(total_presses)