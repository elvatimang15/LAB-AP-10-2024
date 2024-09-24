Golongan = str(input("Golongan: "))
Daya = int(input("Daya (VA): "))
Pemakaian = int(input("Pemakaian: "))

tarif = 0

if Golongan == "R1":
    if Daya <= 900:
        tarif = 1352
    elif 900 < Daya <= 1300:  
        tarif = 1,444.70
    else: 
        tarif = 1,444.70
elif Golongan == "R2":
    if 3500 <= Daya <= 5500:
        tarif = 1699.53
elif Golongan == "R3":
    if Daya >= 6600:
        tarif = 1699.53
elif Golongan == "B2":
    if 6600 <= Daya <= 200000:
        tarif = 1444.70
elif Golongan == "B3":
    if Daya >= 200000:
        tarif = 1114.74
elif Golongan == "I3":
    if Daya >= 200000:
        tarif = 1314.72
elif Golongan == "P1":
    if 6600 <= Daya <= 200000:
        tarif = 1523.28
else:
    print("Data tidak valid")

Tagihan = 0 
if tarif > 0:
    Tagihan = tarif * Pemakaian

print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {Tagihan}") 