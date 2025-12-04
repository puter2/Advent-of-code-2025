def day2(path):
    result = []
    with open(path) as file:
        line = file.readline()
        ranges = line.split(',')
        for r in ranges:
            start, end = r.split('-')[0], r.split('-')[1]
            result.append((int(start), int(end)))
    return result

def day3(path):
    banks = []
    with open(path) as file:
        for line in file.readlines():
            banks.append(line.strip())
    return banks

def day4(path):
    diagram = []
    with open(path) as file:
        for line in file.readlines():
            row=[]
            for c in line.strip():
                row.append(c)
            diagram.append(row)
    return diagram

if __name__=='__main__':
    print(day4('day4/testinput.txt'))