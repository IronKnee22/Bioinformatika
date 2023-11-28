with open('sources/test_seqs.txt', 'r') as file:
    lines = file.readlines()

start_zbytecne = []
end_zbytecne = []
start_dulezite = []
end_dulezite = []

for line in lines:

    parts = line.strip().split('\t')

    if len(parts) >= 3:
        start_zbytecne.append(int(parts[0]))
        end_zbytecne.append(int(parts[1]))
        coordinates = parts[2].strip().split(' ')
        coordinates = [coord.strip('[],') for coord in coordinates]
        for i in range(0, len(coordinates), 2):

            start_dulezite.append(int(coordinates[i]))
            end_dulezite.append(int(coordinates[i + 1]))

# print("start_zbytecne:", start_zbytecne)
# print("end_zbytecne:", end_zbytecne)
# print("start_dulezite:", start_dulezite)
# print("end_dulezite:", end_dulezite)


with open('sources/sequenceOfEcoliStrainM54.txt', 'r') as file:
    file_contents = file.read()

non_dna_list = []
testovaci_data = []

for start, end in zip(start_zbytecne, end_zbytecne):
    vysek = file_contents[start - 1:end - 1]
    vysek = vysek.replace('\n', '')
    i = start-1

    non_dna = ""
    dna = ""

    for j in range(len(vysek)):
        i += 1
        if any(start_dna_elem - 1 <= i <= end_dna_elem - 1 for start_dna_elem, end_dna_elem in zip(start_dulezite, end_dulezite)):
            if non_dna:
                non_dna_list.append(non_dna.strip())
                non_dna = ""
            dna += vysek[j]
        else:
            if dna:
                testovaci_data.append(dna.strip())
                dna = ""
            non_dna += vysek[j]

    if non_dna:
        non_dna_list.append(non_dna.strip())
    if dna:
        testovaci_data.append(dna.strip())

# Výsledek
# print("non_dna_list:", non_dna_list)
# print("dna_list:", testovaci_data)
