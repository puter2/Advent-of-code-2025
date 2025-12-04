from reader import day4, day4_alt

def how_many_neighbors(diagram, pos_x, pos_y):
    directions = [
        (1,0),
        (0,1),
        (-1,0),
        (0,-1),
        (1,1),
        (-1,-1),
        (-1,1),
        (1,-1)
    ]
    neighbors = 0
    for dir_x, dir_y in directions:
        try:
            new_x = pos_x+dir_x
            new_y = pos_y+dir_y
            if (new_x, new_y) in diagram:
                neighbors+=1
        except IndexError:
            continue
    return neighbors

file = 'input.txt'

removed_boxes = 0
diagram = day4_alt(file)
did_remove_box = True
#set solution
it = 0
while did_remove_box:
    did_remove_box=False
    it+=1
    new_set = set()
    # print(f'iteracja: {it}')
    for box in diagram:
        new_set.add(box)
        if how_many_neighbors(diagram, *box) < 4:
            # print(f'usuwam {box}')
            new_set.remove(box)
            removed_boxes+=1
            did_remove_box=True
    diagram = new_set.copy()

print(diagram)
print(removed_boxes)