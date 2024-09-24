print("Tebak angka antara 1 sampai 100. Kamu punya 5 kali percobaan.")

angka_awal = int(input("Masukkan angka untuk memulai: "))

angka_rahasia = (angka_awal * 3 + 2) % 100 + 1  

percobaan = 0

while percobaan < 5:
    tebakan = int(input("Masukkan tebakan (atau 0 untuk keluar): "))
    
    if tebakan == 0:
        print("Permainan dihentikan.")
        break
    
    percobaan += 1
    
    if tebakan == angka_rahasia:
        print("Selamat! Tebakanmu benar.")
        break
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Angka terlalu kecil.")
        
    if percobaan == 5:
        print(f"Kesempatan habis, angka yang benar adalah {angka_rahasia}.")
