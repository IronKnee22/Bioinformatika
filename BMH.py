def vytvoreni_tabulky(heslo):
    tabulka = {}

    for i in range(len(heslo)):
        tabulka[heslo[i]] = len(heslo) - i - 1

    return tabulka


def boyer_moore_horspool(text, heslo):
    tabulka_hesla = vytvoreni_tabulky(heslo)
    
    start_index = 0
    while start_index <= len(text) - len(heslo):
        end_index = len(heslo) - 1
        while end_index >= 0 and heslo[end_index] == text[start_index + end_index]:
            end_index = end_index - 1

        if end_index < 0:
            print(f"Heslo jsem našel v textu na indexu {start_index}, a končí na indexu {start_index + len(heslo) - 1}")
            break
        else:
            a = tabulka_hesla.get(text[start_index + len(heslo)-1], len(heslo))
            start_index += a
    else:
        print("Hledané heslo v textu není")



text =   "dfaedfgcedffesvesdrfskfksdjsfjsdafjsdafksds"
heslo  = "fksdjsf"
boyer_moore_horspool(text,heslo)