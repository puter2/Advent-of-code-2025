from reader import day5

file = 'input.txt'
ranges, available_ingredient_IDs = day5(file)

fresh = 0
for id in available_ingredient_IDs:
    for start, end in ranges:
        if start <= id <= end:
            fresh+=1
            break

print(fresh)