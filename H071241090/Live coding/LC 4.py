# No 2
def tukar_huruf() :
    kata = input("String 1 : ")

    print (kata.swapcase())

tukar_huruf()

# No 3
def hitung_frekuensi_huruf(teks) :
    teks.lower()
    frekuensi = {}

    for char in teks:
        if 'a' <= char <= 'z' :
            if char in frekuensi :
                frekuensi[char] += 1
            else :
                frekuensi[char] = 1
    urut = dict(sorted(frekuensi.items()))

    return urut

string = input("Masukkan string : ")
hasil = hitung_frekuensi_huruf(string)

for char, jumlah in hasil.items():
    print(f'{char} : {jumlah}')