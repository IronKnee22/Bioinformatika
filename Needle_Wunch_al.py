import numpy as np


def create_scoring_matrix(match, mismatch, gap):
    scoring_matrix = {}
    bases = ['A', 'T', 'C', 'G']
    for base1 in bases:
        for base2 in bases:
            if base1 == base2:
                scoring_matrix[(base1, base2)] = match
            else:
                scoring_matrix[(base1, base2)] = mismatch
    return scoring_matrix

# Needleman-Wunch algoritmus pro pairwise alignment


def needleman_wunsch(seq1, seq2, scoring_matrix, gap_penalty):
    n = len(seq1)
    m = len(seq2)

    # Inicializace matice pro dynamické programování
    dp = np.zeros((n + 1, m + 1))

    # Inicializace první řádku a prvního sloupce
    for i in range(1, n + 1):
        dp[i][0] = dp[i-1][0] + gap_penalty
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j-1] + gap_penalty

    # Výpočet hodnot v matici
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match_score = dp[i-1][j-1] + scoring_matrix[(seq1[i-1], seq2[j-1])]
            delete_score = dp[i-1][j] + gap_penalty
            insert_score = dp[i][j-1] + gap_penalty
            dp[i][j] = max(match_score, delete_score, insert_score)

    # Rekonstrukce alignmentu
    align1 = []
    align2 = []
    i = n
    j = m
    while i > 0 or j > 0:
        if i > 0 and dp[i][j] == dp[i-1][j] + gap_penalty:
            align1.append(seq1[i-1])
            align2.append('-')
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j-1] + gap_penalty:
            align1.append('-')
            align2.append(seq2[j-1])
            j -= 1
        else:
            align1.append(seq1[i-1])
            align2.append(seq2[j-1])
            i -= 1
            j -= 1

    alignment1 = ''.join(align1[::-1])
    alignment2 = ''.join(align2[::-1])

    return alignment1, alignment2


# Vstupní sekvence
seq1 = "ATGCT"
seq2 = "AGCT"

# Nastavení parametrů
match_score = 1
mismatch_score = -1
gap_penalty = -2

# Vytvoření skórovací tabulky
scoring_matrix = create_scoring_matrix(
    match_score, mismatch_score, gap_penalty)

# Spuštění Needleman-Wunch algoritmu
alignment1, alignment2 = needleman_wunsch(
    seq1, seq2, scoring_matrix, gap_penalty)

# Výstup
print("Optimální alignment:")
print(alignment1)
print(alignment2)
