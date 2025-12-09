from reader import day9

def calculate_area(point1, point2):
    width = abs(point1[0] - point2[0]) + 1
    height = abs(point1[1] - point2[1]) + 1
    return width * height

file = 'input.txt'

red_tiles = day9(file)

areas = {}
for i in range(len(red_tiles)):
    for j in range(i+1,len(red_tiles)):
        tile1 = red_tiles[i]
        tile2 = red_tiles[j]
        areas[tile1,tile2] = calculate_area(tile1, tile2)

print(max(areas.values()))