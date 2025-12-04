from reader import day4

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
            new_x = pos_y+dir_y
            new_y = pos_x+dir_x
            spot = diagram[new_x][new_y]
            if spot=='@' and new_x>=0 and new_y>=0:
                neighbors+=1
        except IndexError:
            continue
    return neighbors

file = 'input.txt'

valid_boxes = 0
diagram = day4(file)
for y in range(len(diagram)):
    for x in range(len(diagram[y])):
        if diagram[y][x]=='@' and how_many_neighbors(diagram, x, y) < 4:
            valid_boxes+=1


print(valid_boxes)
