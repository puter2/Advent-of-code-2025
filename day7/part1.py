from reader import day7

file = 'input.txt'

splitters, start, height = day7(file)

active_beams = {start}
used_splitters = set()

while True:
    # print(active_beams)
    new_beams = set()
    for beam in active_beams:
        new_beam = (beam[0], beam[1]+1)
        if new_beam in splitters:
            used_splitters.add(new_beam)
            new_beam1 = (beam[0]-1, beam[1] + 1)
            new_beam2 = (beam[0]+1, beam[1] + 1)
            new_beams.add(new_beam1)
            new_beams.add(new_beam2)
        else:
            new_beams.add(new_beam)
    active_beams = new_beams
    if new_beam[1]>=height:
        break

print(len(used_splitters))