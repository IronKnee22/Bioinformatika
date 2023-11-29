import numpy as np
from hmmlearn import hmm
import nacitani_trenovacich_dat
import nacitani_testovacich_dat


# Seznam učících sekvencí DNA
# training_data_dna = ['ATGCGTACG', "CGATCGATG", "ATATATATG"]
training_data_dna = nacitani_trenovacich_dat.dna_list
# Seznam učících sekvencí non-DNA
# training_data_non_dna = ["GCGCGCGCG", "AGAGAGAGA", "TATATATAT"]
training_data_non_dna = nacitani_trenovacich_dat.non_dna_list

# Příprava dat pro model
training_data = [list(seq)
                 for seq in training_data_dna + training_data_non_dna]
training_labels = [1] * len(training_data_dna) + \
    [0] * len(training_data_non_dna)

# Konvertování sekvencí na číselné hodnoty (např., A=0, C=1, G=2, T=3)
alphabet = {'a': 0, 'c': 1, 'g': 2, 't': 3}
training_data_numeric = np.concatenate(
    [[alphabet[base] for base in seq] for seq in training_data])

# Přizpůsobení tvaru dat pro CategoricalHMM
lengths = [len(seq) for seq in training_data]

# Trénování HMM
model = hmm.CategoricalHMM(n_components=6, n_iter=200)
model.fit(training_data_numeric.reshape(-1, 1), lengths=lengths)

# Funkce pro predikci


def predict_sequence(sequence):
    sequence_numeric = np.array([alphabet[base]
                                for base in sequence]).reshape(-1, 1)
    predicted_labels = model.predict(sequence_numeric)
    return "DNA" if np.sum(predicted_labels) > len(predicted_labels) / 2 else "non-DNA"


# Testování modelu s polem testovacích sekvencí
# test_sequences = ["ATGCGTACG", "GCCGCCGCCGCC"]
test_sequences = nacitani_testovacich_dat.testovaci_data

for i, test_sequence in enumerate(test_sequences, start=1):
    result = predict_sequence(test_sequence)
    print(f"Result for sequence {i}: {result}")
