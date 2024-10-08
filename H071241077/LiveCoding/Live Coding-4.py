# Soal 2
kata = input("Masukkan kata: ")
kata_baru = kata.swapcase()
print(kata_baru)

# Soal 3
def hitung_frekuensi_huruf(teks):

    teks = teks.lower()

    frekuensi = {}

    for huruf in teks:
        if 'a' <= huruf <= 'z':
            if huruf in frekuensi:
                frekuensi[huruf] +=1
            else:
                frekuensi[huruf] = 1

    frekuensi_terurut = dict(sorted(frekuensi.items()))

    return frekuensi_terurut

input_teks = (input("Masukkan kalimat: "))
hasil = hitung_frekuensi_huruf(input_teks)

for huruf, jumlah in hasil.items():
    print(f'{huruf}: {jumlah}')