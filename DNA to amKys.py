#Prosím poku kód nepůjde zpustit spustě v debbug modu poté bude vše fungovat bez problémů
def rle_decompress(compress_data):
    decompress_data = []   
    count = 0

    for char in compress_data:
        if char.isdigit():
            count = int(char)
        else:
            decompress_data.append(char * count)  # Přidání dekompresovaného znaku do seznamu
            count = 0

    return ''.join(decompress_data)  # Spojení dekompresovaných dat do jednoho řetězce


def trankrispce(DNA):
    trankripce_slovnik = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    mRNA = ''.join(trankripce_slovnik[base] for base in DNA)  # Překlad bází do mRNA

    return mRNA

def translace(ANRm):
    stop_codon = False  
    codon_slovnik = {
        'UUU': 'Fenylalanin', 'UUC': 'Fenylalanin', 'UUA': 'Leucin', 'UUG': 'Leucin',
        'CUU': 'Leucin', 'CUC': 'Leucin', 'CUA': 'Leucin', 'CUG': 'Leucin',
        'AUU': 'Isoleucin', 'AUC': 'Isoleucin', 'AUA': 'Isoleucin', 'AUG': 'Methionin',
        'GUU': 'Valin', 'GUC': 'Valin', 'GUA': 'Valin', 'GUG': 'Valin',
        
        'UCU': 'Serin', 'UCC': 'Serin', 'UCA': 'Serin', 'UCG': 'Serin',
        'CCU': 'Prolin', 'CCC': 'Prolin', 'CCA': 'Prolin', 'CCG': 'Prolin',
        'ACU': 'Threonin', 'ACC': 'Threonin', 'ACA': 'Threonin', 'ACG': 'Threonin',
        'GCU': 'Alanin', 'GCC': 'Alanin', 'GCA': 'Alanin', 'GCG': 'Alanin',

        'UAU': 'Tyrosin', 'UAC': 'Tyrosin', 'UAA': 'Stop', 'UAG': 'Stop',
        'CAU': 'Histidin', 'CAC': 'Histidin', 'CAA': 'Glutamin', 'CAG': 'Glutamin',
        'AAU': 'Asparagin', 'AAC': 'Asparagin', 'AAA': 'Lysin', 'AAG': 'Lysin',
        'GAU': 'Asparagová kyselina', 'GAC': 'Asparagová kyselina', 'GAA': 'Kyselina glutamová', 'GAG': 'Kyselina glutamová',

        'UGU': 'Cystein', 'UGC': 'Cystein', 'UGA': 'Stop', 'UGG': 'Tryptofan',
        'CGU': 'Arginin', 'CGC': 'Arginin', 'CGA': 'Arginin', 'CGG': 'Arginin',
        'AGU': 'Serin', 'AGC': 'Serin', 'AGA': 'Arginin', 'AGG': 'Arginin',
        'GGU': 'Glycin', 'GGC': 'Glycin', 'GGA': 'Glycin', 'GGG': 'Glycin',
    }

    # Inverze řetězce mRNA pro hledání startovního kodónu od konce
    mRNA = ANRm[::-1]
    
    start_index = mRNA.find('AUG')  # Hledání indexu startovního kodónu (AUG)
    if start_index == -1:
        return 'V celém řetězci nebylo ani jeden startovní kodón'  # Pokud není startovní kodón nalezen

    amkys = [] 
    codons = [mRNA[i:i+3] for i in range(start_index, len(mRNA), 3)]  # Rozdělení mRNA na kodony

    for codon in codons:
        if codon in {'UAA', 'UAG', 'UGA'}:
            stop_codon = True  
            break
        elif codon in codon_slovnik:
            amkys.append(codon_slovnik[codon])
        else:
            amkys.append(f'Není ve slovníku: {codon}')

    if stop_codon:
        return ', '.join(amkys)  # Vrácení aminokyselin jako řetězce s oddělovačem
    else:
        return 'Našel jsem startovní kodón, bohužel ani jeden stop kodon'  # Pokud není nalezen stop kodón


def nacteni_souboru(soubor):
    header = "" 
    amKys_list = []

    with open(soubor, 'r') as Fasta:
        for radek in Fasta:
            radek = radek.strip()
            if radek.startswith('>'):
                header = radek
            else:
                DNA = rle_decompress(radek)  # Dekompresce genetických dat
                mRNA = trankrispce(DNA)  # Transkripce do mRNA
                amKys = translace(mRNA)  # Translace mRNA na aminokyseliny
                amKys_list.append(amKys)  # Přidání aminokyselin do seznamu

    return header, ', '.join(amKys_list)  # Vrácení hlavičky aminokyselin jako řetězce s oddělovačem


# Hlavní část kódu
Header, AmKys = nacteni_souboru('c:\\Users\\MarekU\\Desktop\\data_rle.fa')

# Výpis hlavičky a aminokyselin
print(f'Hlavička: {Header}')
print(f'Aminokyseliny: {AmKys}')

#1. Homo sapiens
#2. Poskytnutá data neopsahují stop kodon nejsem schopen odpovědět
#3. Není výhodná
