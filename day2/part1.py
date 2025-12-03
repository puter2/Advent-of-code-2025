import reader

input_file = 'input.txt'

ranges = reader.day2(input_file)

invalid_ids = []
for start, end in ranges:
    for i in range(start, end+1):
        if len(str(i)) % 2 != 0:
            continue
        else:
            number = str(i)
            length = len(number)
            first_half = number[:length//2]
            second_half = number[length//2:]
            if first_half==second_half:
                invalid_ids.append(i)

print(sum(invalid_ids))