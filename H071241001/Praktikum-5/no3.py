pertama = input("Masukkan String pertama: ")
kedua = input("Masukkan String kedua: ")

penghapusan = 0

karakter = set(pertama) | set(kedua)

for x in karakter:
    count1 = pertama.count(x)
    count2 = kedua.count(x)
    penghapusan += abs(count1 - count2)
    
print(f"Jumlah minimum penghapusan untuk membuat anagram: {penghapusan}")