from functools import reduce

from reader import day5

def find_superset(element, sets):
    for start, end in sets:
        if start <= element <= end:
            return start, end
    return -1,-1

def delete_completely_overlapping_sets(new_set, sets: set):
    sets_to_be_removed=set()
    for start, end in sets:
        if new_set[0]<=start and end<=new_set[1]:
            sets_to_be_removed.add((start,end))
    return sets.difference(sets_to_be_removed)


file = 'input.txt'
ranges, available_ingredient_IDs = day5(file)
fresh_ranges = set()
for start, end in ranges:
    #determine if start and end are in any range taken so far
    superset_start = find_superset(start, fresh_ranges)
    superset_end = find_superset(end, fresh_ranges)

    if superset_start == (-1,-1) and superset_end == (-1,-1):
        #case 1 completely new range
        new_range = (start, end)
        fresh_ranges = delete_completely_overlapping_sets(new_range, fresh_ranges)
        fresh_ranges.add((start, end))
    elif superset_start == (-1,-1):
        #case 2 new range overlaps with existing range from right side
        new_range = (start, superset_end[1])
        fresh_ranges.remove(superset_end)
        fresh_ranges = delete_completely_overlapping_sets(new_range, fresh_ranges)
        fresh_ranges.add(new_range)
    elif superset_end == (-1,-1):
        #case 3 new range overlaps with existing range from left side
        new_range = (superset_start[0], end)
        fresh_ranges.remove(superset_start)
        fresh_ranges = delete_completely_overlapping_sets(new_range, fresh_ranges)
        fresh_ranges.add(new_range)
    else:
        #case 4 new range overlaps with existing ranges from both sides
        if superset_start==superset_end:
            #case 4.1 new range is a subset
            continue
        new_range = (superset_start[0], superset_end[1])
        fresh_ranges.remove(superset_start)
        fresh_ranges.remove(superset_end)
        fresh_ranges = delete_completely_overlapping_sets(new_range, fresh_ranges)
        fresh_ranges.add(new_range)

print(fresh_ranges)
fresh_products = 0
for start, end in fresh_ranges:
    fresh_products+= end - start + 1
print(fresh_products)