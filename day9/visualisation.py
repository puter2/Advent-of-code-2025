from reader import day9
from part2 import find_valid_borders, find_outside

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
valid_tiles = find_valid_borders(red_tiles)
place_on_map(valid_tiles, '#')
print()
display()
outside = find_outside(valid_tiles)
print(outside)
place_on_map(outside, 'O')
display()