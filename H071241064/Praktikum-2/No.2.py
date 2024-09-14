# 2

# Input usia dan status keanggotaan
usia = int(input("Masukkan usia: "))
status_keanggotaan = input("Apakah Anda anggota? (ya/tidak): ")

# Kategori Usia
if usia < 5:
    harga_tiket = 0
elif 5 <= usia <= 12:
    harga_tiket = 50000
elif 13 <= usia <= 59:
    harga_tiket = 100000
else:
    harga_tiket = 70000

# Diskon Keanggotaan
harga = harga_tiket - (harga_tiket * 20 /100) if status_keanggotaan == "ya" else harga_tiket

print(f"Harga tiket: Rp. {harga}")