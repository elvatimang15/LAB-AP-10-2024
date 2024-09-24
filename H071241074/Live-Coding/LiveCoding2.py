golongan = str(input("Golongan: "))
daya = int(input("Daya: "))
pemakaian = int(input("Pemakaian: "))

if golongan == "R1":
    if daya == 900:
        tarif = 1352
    elif daya == 1.300 or daya == 2.200:
        tarif = 1444.70
    else:
        print("Data tidak valid")
       

if golongan == "R2":
    if 3500 <= daya <= 5500:
        tarif = 1699.53
    else:
        print("Data tidak valid")
      

if golongan == "R3":
    if daya >= 6600:
        tarif = 1699.53
    else:
        print("Data tidak valid")
       

elif golongan == "B2":
    if 6600 <= daya <= 200000:
        tarif = 1444.70
    else:
        print("Data tidak valid")
        

elif golongan == "B3" and daya <= 200000:
        tarif = 1114.74
   
elif golongan == "I3" and daya >= 200000:
        tarif = 1314.12

elif golongan == "PI" and daya >= 200000:
        tarif = 1523.28

else:
        print("Data tidak valid")

total_tagihan = pemakaian * tarif

print (f"Jumlah tagihan anda sebesar : Rp. {total_tagihan: ,}")
       

