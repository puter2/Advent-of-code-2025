import reader

def consists_of_repeated_subsequences(sequence, seq_length):
    if len(sequence)%seq_length!=0:
        return False
    subsequence = sequence[:seq_length]
    for start in range(seq_length, len(sequence)-seq_length+1, seq_length):
        if subsequence!=sequence[start:start+seq_length]:
            return False
    return True

input_file = 'input.txt'

ranges = reader.day2(input_file)

invalid_ids = []
for start, end in ranges:
    for id in range(start, end+1):
        id_length = len(str(id))
        for test_len in range(id_length//2, 0, -1):
            if consists_of_repeated_subsequences(str(id), test_len):
                invalid_ids.append(id)
                break


print(sum(invalid_ids))