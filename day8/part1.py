from reader import day8

def calculate_distance(point1, point2):
    result = 0
    for i in range(3):
        result += (point1[i] - point2[i])**2
    return result**0.5

file='input.txt'

boxes = day8(file)

distances = []

for i in range(len(boxes)-1):
    for j in range(i+1, len(boxes)):
        distances.append(
            (calculate_distance(boxes[i], boxes[j]),
             (i, j)
             ))
distances = sorted(distances, key= lambda a:a[0])

# making connections
number_of_connections = 1000
circuits = [{i} for i in range(len(boxes))]
connection_num = 0
while connection_num < number_of_connections:
    box1, box2 = distances.pop(0)[1]
    # check if those two boxes were in any group
    box1_location = -1
    box2_location = -1
    for i in range(len(circuits)):
        if box1_location==-1 and box1 in circuits[i]:
            box1_location = i
        if box2_location==-1 and box2 in circuits[i]:
            box2_location = i
        if box1_location != -1 and box2_location != -1:
            break
    # connect circuits
    if box1_location==box2_location:
        #boxes are already in the same circuit no need to connect
        connection_num+=1
        continue
    else:
        new_circuit = circuits[box1_location].union(circuits[box2_location])
        if box1_location < box2_location:
            circuits.pop(box2_location)
            circuits.pop(box1_location)
        else:
            circuits.pop(box1_location)
            circuits.pop(box2_location)
        circuits.append(new_circuit)
    connection_num+=1

sorted_circuits = sorted(circuits, key=lambda a: len(a), reverse=True)

result = 1
for i in range(3):
    result *= len(sorted_circuits[i])
print(result)