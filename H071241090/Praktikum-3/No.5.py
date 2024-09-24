a = int(input("Masukkan populasi awal Serangga A : "))
b = int(input("Masukkan populasi awal Serangga B : "))
hari = int(input("Masukkan jumlah hari : "))

for i in range (1, hari+1) :
    if i%2 == 1 :
        a = int(1.3*a)
        b = int(1.5*b)
    else :
        a = int(0.8*a)
        b = int(0.6*b)
    
    if i%5 == 0:
        a = int(0.9*a)
        b = int(0.9*b)
        print (f"Hari {i}: Predator memakan 10% populasi.")

    print(f"Hari {i}: Serangga A = {a:.0f}, Serangga B = {b:.0f}")