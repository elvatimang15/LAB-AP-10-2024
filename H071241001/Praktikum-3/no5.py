A = int(input("Masukkan populasi awal Serangga A: "))
B = int(input("Masukkan populasi awal Serangga B: "))
jumlahari = int(input("Masukkan jumlah hari: "))
for i in range (1, jumlahari + 1):
    if i % 2 == 0:
        A -= int(A * 0.2)
        B -= int(B * 0.4)
    else:
        A += int(A * 0.3)
        B += int(B * 0.5)
    
    if i % 5 == 0:
        A = int(A * 0.9)
        B = int(B * 0.9)
        print(f"Hari {i}: Predator makan 10%")
    
    print(f"Hari {i}: Serangga A = {A}, Serangga B = {B}")