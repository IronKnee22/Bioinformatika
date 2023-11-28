with open('sources/train_seqs.txt', 'r') as file:
    lines = file.readlines()

start_non = []
end_non = []
start_dna = []
end_dna = []

for line in lines:
    # Rozdělení řádku podle mezer a odstranění speciálních znaků
    parts = line.strip().split('\t')

    # Pokud máme alespoň čtyři části, rozdělíme další podle '[' a ']'
    if len(parts) >= 3:
        start_non.append(int(parts[0]))
        end_non.append(int(parts[1]))
        coordinates = parts[2].strip().split(' ')
        coordinates = [coord.strip('[],') for coord in coordinates]
        for i in range(0, len(coordinates), 2):

            start_dna.append(int(coordinates[i]))
            end_dna.append(int(coordinates[i + 1]))

print("start_non:", start_non)
print("end_non:", end_non)
print("start_dna:", start_dna)
print("end_dna:", end_dna)
