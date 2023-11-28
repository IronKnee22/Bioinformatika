with open('sources/train_seqs.txt', 'r') as file:
    lines = file.readlines()

start_non = []
end_non = []
start_dna = []
end_dna = []

for line in lines:

    parts = line.strip().split('\t')

    if len(parts) >= 3:
        start_non.append(int(parts[0]))
        end_non.append(int(parts[1]))
        coordinates = parts[2].strip().split(' ')
        coordinates = [coord.strip('[],') for coord in coordinates]
        for i in range(0, len(coordinates), 2):

            start_dna.append(int(coordinates[i]))
            end_dna.append(int(coordinates[i + 1]))

# print("start_non:", start_non)
# print("end_non:", end_non)
# print("start_dna:", start_dna)
# print("end_dna:", end_dna)


with open('sources/sequenceOfEcoliStrainM54.txt', 'r') as file:
    file_contents = file.read()

non_dna_list = []
dna_list = []

for start, end in zip(start_non, end_non):
    vysek = file_contents[start - 1:end - 1]
    vysek = vysek.replace('\n', '')
    i = start-1
    non_dna = ""
    dna = ""

    for j in range(len(vysek)):
        i += 1
        if any(start_dna_elem - 1 <= i <= end_dna_elem - 1 for start_dna_elem, end_dna_elem in zip(start_dna, end_dna)):
            if non_dna:
                non_dna_list.append(non_dna.strip())
                non_dna = ""
            dna += vysek[j]
        else:
            if dna:
                dna_list.append(dna.strip())
                dna = ""
            non_dna += vysek[j]

    if non_dna:
        non_dna_list.append(non_dna.strip())
    if dna:
        dna_list.append(dna.strip())

# Výsledek
# print("non_dna_list:", non_dna_list)
# print("dna_list:", dna_list)
