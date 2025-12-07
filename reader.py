import re


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

def day4_alt(path):
    diagram = set()
    with open(path) as file:
        y=-1
        for line in file.readlines():
            y+=1
            x=0
            for c in line.strip():
               if c=='@':
                   diagram.add((x,y))
               x+=1
    return diagram

def day5(path):
    ranges = []
    available = []
    with open(path) as file:
        MODE = "RANGES"
        for line in file.readlines():
            if MODE == "RANGES":
                if line == '\n':
                    MODE = "AVAILABLE IDS"
                    continue
                start = line.split('-')[0]
                end = line.split('-')[1].strip()
                ranges.append((int(start), int(end)))
            else:
                available.append(int(line.strip()))
    return ranges, available

def day6(path):
    data = []
    with open(path) as file:
        for line in file.readlines():
            #delete multiple spaces
            formatted_line = re.sub(r'\s+',' ', line).strip()
            data.append(formatted_line.split())
    return data

def day6_part2(path):
    with open(path) as file:
        data = file.read(-1)
    return data

def day7(path):
    splitters = set()
    start = ()
    with open(path) as file:
        for line_num, line in enumerate(file.readlines()):
            for char_num, char in enumerate(line):
                if char=='S':
                    start = (char_num, line_num)
                elif char=='^':
                    splitters.add((char_num, line_num))
        height = line_num

    return splitters, start, height



if __name__=='__main__':
    print(day7('day7/testinput.txt'))