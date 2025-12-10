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
    outside.add((start_x, start_y))
    to_check = set()
    for x, y in directions:
        new_x, new_y = start_x + x, start_y + y
        if (
                (new_x, new_y) not in borders and
                (new_x,new_y) not in outside and
                min_y < new_y < max_y and
                min_x < new_x < max_x
        ):
            to_check.add((new_x, new_y))

    while to_check:
        print(len(outside), len(to_check))
        point = to_check.pop()
        outside.add(point)
        for x, y in directions:
            new_x, new_y = point[0] + x, point[1] + y
            if (
                    (new_x, new_y) not in borders and
                    (new_x, new_y) not in outside and
                    min_y < new_y < max_y and
                    min_x < new_x < max_x
            ):
                to_check.add((new_x, new_y))

def find_outside(borders:set):
    #bounds
    min_height = min(borders, key=lambda a: a[1])[1]
    min_width = min(borders, key=lambda a: a[0])[0]
    max_width = max(borders, key=lambda a: a[0])[0]
    max_height = max(borders, key=lambda a: a[1])[1]
    print(max_height, max_width, min_height, min_width)
    starting_point = (min_width-1, min_height-1)
    outside = set()
    fill_outside(outside, borders, starting_point[0], starting_point[1], min_height-2, max_height+2, min_width-2, max_width+2)
    return outside

def find_inside(borders:set):
    # bounds
    min_height = min(borders, key=lambda a: a[1])[1]
    min_width = min(borders, key=lambda a: a[0])[0]
    max_height = max(borders, key=lambda a: a[1])[1]
    point_inside = find_first_point_inside(borders, min_width, min_height, max_height)
    inside = {point_inside}
    fill_inside(inside, borders, point_inside)
    return inside

def fill_inside(inside:set, borders:set, start):
    to_check = set()
    start_x, start_y = start
    for x, y in directions:
        new_x, new_y = start_x + x, start_y + y
        if (new_x, new_y) not in borders:
            to_check.add((new_x, new_y))
    while to_check:
        print(len(to_check), len(inside))
        point = to_check.pop()
        inside.add(point)
        for x, y in directions:
            new_x, new_y = point[0] + x, point[1] + y
            if (
                    (new_x, new_y) not in borders and
                    (new_x, new_y) not in inside
            ):
                to_check.add((new_x, new_y))

def find_first_point_inside(borders, left_border, bottom_border, top_border):
    #idea: go top to bottom, when you find singular wall, then next point must be inside, if double wall, abandon
    current_x = left_border
    while True:
        current_x = current_x + 1
        for y in range(bottom_border - 1 , top_border + 1):
            if (current_x, y) in borders:
                if (current_x, y + 1) not in borders:
                    return (current_x, y+1)
                else:
                    break



def is_rectangle_outside(outside, corner1, corner2):
    x1, y1 = corner1
    x2, y2 = corner2
    for i in range(min(x1,x2), max(x1,x2)):
        if (i, y1) in outside or (i, y2) in outside:
            return False
    for i in range(min(y1,y2), max(y1,y2)):
        if (x1, i) in outside or (x2, i) in outside:
            return False
    return True

def is_rectangle_inside(inside, corner1, corner2):
    x1, y1 = corner1
    x2, y2 = corner2
    for i in range(min(x1, x2), max(x1, x2)):
        if (i, y1) not in inside or (i, y2) not in inside:
            return False
    for i in range(min(y1, y2), max(y1, y2)):
        if (x1, i) not in inside or (x2, i) not in inside:
            return False
    return True

directions2 = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
#new idea, find outside BORDER
def find_outside_border(border, corners):
    min_x = min(border, key=lambda a: a[0])[0]
    corners_on_left_border = []
    for (x, y) in corners:
        if x == min_x:
            corners_on_left_border.append((x,y))
    min_y = min(corners_on_left_border, key=lambda a: a[1])[1]
    leftmost_top_corner = (min_x-1, min_y-1)
    outside_border = {leftmost_top_corner}
    to_check = set()
    for x1,y1 in directions2:
        new_point = (leftmost_top_corner[0] + x1, leftmost_top_corner[1] + y1)
        if new_point not in border:
            for x2, y2 in directions2:
                adjacent_point = (new_point[0] + x2, new_point[1] + y2)
                if adjacent_point in border:
                    to_check.add(new_point)
                    break
    while to_check:
        point = to_check.pop()
        outside_border.add(point)
        for x1, y1 in directions2:
            new_point = (point[0] + x1, point[1] + y1)
            if new_point not in border and new_point not in outside_border:
                for x2, y2 in directions2:
                    adjacent_point = (new_point[0] + x2, new_point[1] + y2)
                    if adjacent_point in border:
                        to_check.add(new_point)
                        break
    return outside_border

def does_rectangle_stay_inside(outside_borders, corner1, corner2):
    x1, y1 = corner1
    x2, y2 = corner2
    for i in range(min(x1, x2), max(x1, x2)):
        if (i, y1) in outside_borders or (i, y2) in outside_borders:
            return False
    for i in range(min(y1, y2), max(y1, y2)):
        if (x1, i) in outside_borders or (x2, i) in outside_borders:
            return False
    return True


if __name__ == '__main__':
    file = 'input.txt'

    red_tiles = day9(file)
    borders = find_valid_borders(red_tiles)
    # outside = find_outside(borders)
    # inside = find_inside(borders)
    # valid = inside.union(borders)
    outside_borders = find_outside_border(borders, red_tiles)

    areas = {}
    for i in range(len(red_tiles)):
        print(f'checking {red_tiles[i]} connections')
        for j in range(i+1,len(red_tiles)):
            tile1 = red_tiles[i]
            tile2 = red_tiles[j]
            # if is_rectangle_inside(valid, tile1, tile2):
            #     areas[tile1,tile2] = calculate_area(tile1, tile2)
            if does_rectangle_stay_inside(outside_borders, tile1, tile2):
                areas[tile1, tile2] = calculate_area(tile1, tile2)



    print(max(areas.values()))

# idea, check which corners are valid