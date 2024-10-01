def maksimum(daftar_angka):
    terbesar = daftar_angka[0]
    for angka in daftar_angka:
        if angka > terbesar:
            terbesar = angka

    return terbesar
    
print(maksimum([1, 2, 3, 4, 5, 6, 7, 9, 9, 10]))