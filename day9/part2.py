from reader import day9

def calculate_area(point1, point2):
    width = abs(point1[0] - point2[0]) + 1
    height = abs(point1[1] - point2[1]) + 1
    return width * height

def add_inbetweens(valid_tiles, point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2:
        # add horizontal line
        for i in range(y1, y2, 1 if y2 > y1 else -1):
            valid_tiles.add((x1, i))
    else:
        # add vertical line
        for i in range(x1, x2, 1 if x2 > x1 else -1):
            valid_tiles.add((i, y1))

def find_valid_borders(all_tiles):
    valid_tiles = set()
    first_tile = all_tiles[-1]
    for tile in all_tiles:
        next_tile = tile
        add_inbetweens(valid_tiles, first_tile, next_tile)
        valid_tiles.add(first_tile)
        valid_tiles.add(next_tile)
        first_tile = next_tile
    return valid_tiles

directions = [(1,0), (-1,0), (0,1), (0,-1)]

def fill_outside(outside, borders, start_x, start_y, min_y, max_y, min_x, max_x):
    if (start_x, start_y) in outside:
        return
    outside.add((start_x, start_y))
    for x, y in directions:
        new_x, new_y = start_x + x, start_y + y
        if (new_x, new_y) not in borders and (new_x, new_y) not in outside and min_y< new_y <max_y and min_x< new_x <max_x:
            fill_outside(outside, borders, new_x, new_y, min_y, max_y, min_x, max_x)



def find_outside(borders:set):
    #bounds
    min_height = min(borders, key=lambda a: a[1])[1]
    min_width = min(borders, key=lambda a: a[0])[0]
    max_width = max(borders, key=lambda a: a[0])[0]
    max_height = max(borders, key=lambda a: a[1])[1]
    starting_point = (min_width-1, min_height-1)
    outside = set()
    fill_outside(outside, borders, starting_point[0], starting_point[1], min_height-2, max_height+2, min_width-2, max_width+2)
    return outside

def is_rectangle_inside(outside, corner1, corner2):
    x1, y1 = corner1
    x2, y2 = corner2
    for i in range(min(x1,x2), max(x1,x2)):
        if (i, y1) in outside or (i, y2) in outside:
            return False
    for i in range(min(y1,y2), max(y1,y2)):
        if (x1, i) in outside or (x2, i) in outside:
            return False
    return True


file = 'input.txt'

red_tiles = day9(file)
borders = find_valid_borders(red_tiles)
outside = find_outside(borders)

areas = {}
for i in range(len(red_tiles)):
    for j in range(i+1,len(red_tiles)):
        tile1 = red_tiles[i]
        tile2 = red_tiles[j]
        if is_rectangle_inside(outside, tile1, tile2):
            areas[tile1,tile2] = calculate_area(tile1, tile2)



print(max(areas.values()))

# idea, check which corners are valid