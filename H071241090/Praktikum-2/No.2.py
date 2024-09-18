usia = int(input("Masukkan usia : "))
anggota = input("Apakah anda anggota (ya/tidak) : ")
tiket = ()

if usia < 5: 
    tiket == 0
elif usia <= 12 :
    tiket == 50000
elif 13 <= usia <= 59:
    tiket = 100000
else :
    tiket = 70000

harga = (tiket * 0.8) if anggota == "ya" else tiket 

print (f"Harga tiket : Rp{int(harga)}")



