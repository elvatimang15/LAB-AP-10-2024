golongan = input("masukkan golongan: ")
daya = int(input("masukkan daya: ")) # Convert daya to an integer
pemakaian = int(input("masukkan pemakaian: "))


if golongan == "R1":
    if daya == 900:
        tarif = 1352
    elif daya == 1300:
        tarif = 1444.70
    elif daya == 2200:
        tarif = 1444.70
    else:
        print("data tidak valid.")
        exit()
    
elif golongan == "R2":
    if 3500 <= daya <= 5500:
        tarif = 1699.53
    else:
        print("data tidak valid.")
        exit()
        
elif golongan == "R3":
    if daya >= 6600:
        tarif = 1699.53
    else:
        print("data tidak valid.")
        exit()
        
elif golongan == "B2":
    if 6600 <= daya <= 200000:
        tarif = 1444.70
    else:
        print("data tidak valid.")
        exit()
        
elif golongan == "B3":
    if daya >= 200000:
        tarif = 1144.74
    else:
        print("data tidak valid.")
        exit()
        
elif golongan == "I3":
    if daya >= 200000:
        tarif = 1314.12
    else:
        print("data tidak valid.")
        exit()
        
elif golongan == "P1":
    if 6600 <= daya <= 200000:
        tarif = 1523.28
    else:
        print("data tidak valid.")
        exit()
    
else:
    print("data tidak valid.")
    exit()
    
total_tarif = pemakaian * tarif
print(f"pemakaian: jumlah tagihan anda: {total_tarif:}")