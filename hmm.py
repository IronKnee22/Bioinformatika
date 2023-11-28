import numpy as np
from hmmlearn import hmm

# Seznam učících sekvencí DNA
training_data_dna = ["ATGCGTACG", "CGATCGATG", "ATATATATG"]

# Příprava dat pro model
training_data = [list(seq) for seq in training_data_dna]
training_labels = [1] * len(training_data)

# Konvertování sekvencí na číselné hodnoty (např., A=0, C=1, G=2, T=3)
alphabet = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
training_data_numeric = np.concatenate(
    [[alphabet[base] for base in seq] for seq in training_data])

# Přizpůsobení tvaru dat pro CategoricalHMM
lengths = [len(seq) for seq in training_data]

# Trénování HMM
model = hmm.CategoricalHMM(n_components=2, n_iter=100)
model.fit(training_data_numeric.reshape(-1, 1), lengths=lengths)

# Funkce pro predikci


def predict_sequence(sequence):
    sequence_numeric = np.array([alphabet[base]
                                for base in sequence]).reshape(-1, 1)
    predicted_labels = model.predict(sequence_numeric)
    return "DNA" if np.sum(predicted_labels) > len(predicted_labels) / 2 else "non-DNA"


# Testování modelu
test_sequence_1 = "ATATATATG"
test_sequence_2 = "GCCGCCGCCGCC"

result_1 = predict_sequence(test_sequence_1)
result_2 = predict_sequence(test_sequence_2)

print(f"Result for sequence 1: {result_1}")
print(f"Result for sequence 2: {result_2}")
