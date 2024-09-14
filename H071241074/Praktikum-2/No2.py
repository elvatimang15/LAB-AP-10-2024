usia = int(input("Masukkan usia: "))
anggota = input("Apakah Anda anggota? (ya/tidak): ")

if usia < 5:
        harga = 0
elif 5 <= usia <= 12:
        harga = 50000
elif 13 <= usia <= 59:
        harga = 100000
elif usia >= 60:
        harga = 70000
else:
        harga = 0

harga_akhir = harga * 0.8 if anggota == 'ya' else harga

print(f"Harga tiket: Rp{harga_akhir:.0f}")