from reader import day9
from part2 import find_valid_borders, find_outside, find_first_point_inside, find_inside

def display():
    global floor_map
    for line in floor_map:
        print(''.join(line))

def place_on_map(coords_list, symbol):
    global floor_map
    for y, x in coords_list:
        floor_map[x][y] = symbol


file = 'testinput.txt'
red_tiles = day9(file)
width, height = 15, 10
floor_map = [['.' for i in range(width)] for j in range(height)]
place_on_map(red_tiles, '#')
display()
valid_borders = find_valid_borders(red_tiles)
place_on_map(valid_borders, '#')
print()
display()
# outside = find_outside(valid_borders)
# print(outside)
# place_on_map(outside, 'O')
# display()
print(point_inside:=find_first_point_inside(valid_borders, 0, 0 , 11))
place_on_map({point_inside}, 'O')
display()
print(inside:=find_inside(valid_borders))
place_on_map(inside, 'O')
display()
valid_spots = inside.union(valid_borders)
place_on_map(valid_spots, 'X')
display()