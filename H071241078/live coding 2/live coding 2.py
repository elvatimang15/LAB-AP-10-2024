golongan = input("Golongan: ")
daya = int(input("Daya: "))
pemakaian = int(input("Pemakaian: "))

if golongan == "RI":
    if daya == 900:
        tarif = 1352
    elif daya == 1300:
        tarif = 1444.70
    elif daya == 2200:
        tarif = 1444.70
    else:
        print("Data tidak valid")
        exit()
elif golongan == "R2":
    if 3500 <= daya <= 5500:
        tarif = 1699.53
    else:
        print("Data tidak valid")
        exit()
elif golongan == "R3":
    if daya >= 6600:
        tarif = 1699.53
    else:
        print("Data tidak valid")
        exit()
elif golongan == "B2":
    if 6600 <= daya <= 200000:
        tarif = 1444.70
    else:
        print("Data tidak valid")
        exit()
elif golongan == "B3":
    if daya >= 200000:
        tarif = 1114.74
    else:
        print("Data tidak valid")
        exit()
elif golongan == "13":
    if daya >= 200000:
        tarif = 1314.12
    else:
        print("Data tidak valid")
        exit()
elif golongan == "P1":
    if 6600 <= daya <= 200000:
        tarif = 1523.28
    else:
        print("Data tidak valid")
        exit()
else:
    print("Data tidak valid")
    exit()


total_tariff = pemakaian * tarif


print(f"Jumlah tagihan anda sebesar: Rp. {total_tariff:.2f}")