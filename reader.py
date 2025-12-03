def day2(path):
    result = []
    with open(path) as file:
        line = file.readline()
        ranges = line.split(',')
        for r in ranges:
            start, end = r.split('-')[0], r.split('-')[1]
            result.append((int(start), int(end)))
    return result

if __name__=='__main__':
    day2('day2/testinput.txt')