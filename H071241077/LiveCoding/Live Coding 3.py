golongan = (input("masukkan golongannya : "))
daya = float(input("masukkan berapa dayanya (VA) : "))
pemakaian = float(input("masukkan pemakaian pengguna (kWh): "))

# Inisialisasi variabel untuk menyimpan tarif
tarif = 0

# Conditional Statements
if golongan == "R1":
    if daya <= 900:
        tarif = 1352
    elif daya <= 1300:
        tarif = 1444.70
    else:
        tarif = 1444.70

elif golongan == "R2":
    if 3500 <= daya <= 5500:
        tarif = 1699.53

elif golongan == "R3":
    if daya >= 6600:
        tarif = 1699.53

elif golongan == "B2":
    if 6600 <= daya <= 200000:
        tarif = 1444.70

elif golongan == "B3":
    if daya > 200000:
        tarif = 1114.74

elif golongan == "I3":
    if daya >= 200000:
        tarif = 1314.12

elif golongan == "P1":
    if 6600 <= daya <= 200000:
        tarif = 1523.28

else:
    print("Data golongan tidak valid")

# total tagihan
if tarif != 0:
    total_tagihan = tarif * pemakaian
    print(f"Pemakaian = {pemakaian}")
    print(f"Jumlah tagihan Anda sebesar: Rp. {total_tagihan:.2f}")
else:
    print("Data tidak valid")