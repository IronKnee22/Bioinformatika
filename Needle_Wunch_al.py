import numpy 


def vytvoreni_tabulky(shoda, neshoda):
    tabulka = {}
    bases = ['A', 'T', 'C', 'G']
    for base1 in bases:
        for base2 in bases:
            if base1 == base2:
                tabulka[(base1, base2)] = shoda
            else:
                tabulka[(base1, base2)] = neshoda
    return tabulka



def needleman_wunsch(seq1, seq2, skore_tabulky, mezera):
    x = len(seq1)
    y = len(seq2)

    tabulka = numpy.zeros((x + 1, y + 1))

    # Inicializace první řádku a prvního sloupce
    for i in range(1, x + 1):
        tabulka[i][0] = tabulka[i-1][0] + mezera
    for j in range(1, y + 1):
        tabulka[0][j] = tabulka[0][j-1] + mezera

    # Výpočet hodnot v matici
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            shoda = tabulka[i-1][j-1] + skore_tabulky[(seq1[i-1], seq2[j-1])]
            zleva = tabulka[i-1][j] + mezera
            zeShora = tabulka[i][j-1] + mezera
            tabulka[i][j] = max(shoda, zleva, zeShora)

    # Rekonstrukce alignmentu
    pomocna1 = []
    pomocna2 = []
  
    while x > 0 or y > 0:
        if tabulka[x][y] == tabulka[x-1][y] + mezera:
            pomocna1.append(seq1[x-1])
            pomocna2.append('-')
            x -= 1
        elif tabulka[x][y] == tabulka[x][y-1] + mezera:
            pomocna1.append('-')
            pomocna2.append(seq2[y-1])
            y -= 1
        else:
            pomocna1.append(seq1[x-1])
            pomocna2.append(seq2[y-1])
            x -= 1
            y -= 1

    Vzor = ''.join(pomocna1[::-1])
    Zarovnano = ''.join(pomocna2[::-1])

    return Vzor, Zarovnano


# Vstupní sekvence
seq1 = "ATGCT"
seq2 = "AGCT"

# Nastavení parametrů
shoda_skore = 1
neschodujici_skore = -1
mezera_skore = -2

# Vytvoření skórovací tabulky
tabulka = vytvoreni_tabulky(
    shoda_skore, neschodujici_skore)

# Spuštění Needleman-Wunch algoritmu
Vzor, Zarovnano = needleman_wunsch(
    seq1, seq2, tabulka, mezera_skore)

# Výstup
print("Optimální zarovnani:")
print(Vzor)
print(Zarovnano)
