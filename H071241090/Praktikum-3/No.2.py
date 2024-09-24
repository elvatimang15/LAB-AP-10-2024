import random

print("Tebak angka 1 - 100") 

x = random.randint(1, 100)

for i in range (5) :  
    tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))
    
    if tebakan == 0:
        print("Permainan selesai")
        break  

    if tebakan < x:
        print("Angka terlalu kecil")
    elif tebakan > x:
        print("Angka terlalu besar")
   
    else:
     print("Selamat, Anda menebak angka yang benar!")
     break 

if tebakan != x :
   print (f"Sayang sekali, angka yang benar adalah : {x}")