usia = int(input("Masukka usia: "))
status= input("Apakah anda Anggota (ya/tidak): ")

if usia < 5:
    harga = int('gratis')
elif 5 <= usia <= 12:
    harga = 50000
elif 13 <= usia <= 59:
    harga = 100000
else:
    herga = 70000

harga = harga * 0.8 if status == 'ya' else harga
print(f"Harga tiket: Rp. {int(harga)}")