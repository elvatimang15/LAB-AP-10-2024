import random

angka_tersembunyi = random.randint(1, 100)
percobaan = 0
maksimal_percobaan = 5

teks = [
    "Ini adalah permainan tebak angka",
    "Masukkan angka antara 1 hingga 100",
    "Maksimal tebakan hanya 5 kali",
]

for i in teks:
    print(i)

while percobaan < maksimal_percobaan:
    tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))
    if tebakan == 0:
        print("Permainan dihentikan.")
        break
    percobaan += 1
    if tebakan == angka_tersembunyi:
        print("Selamat! Anda menebak angka dengan benar.")
        break
    elif tebakan > angka_tersembunyi:
        print("Angka terlalu besar.")
    else:
        print("Angka terlalu kecil.")
else:
    print(f"Maaf, anda sudah mencapai maksimal percobaan. Angka tersembunyi yang benar adalah {angka_tersembunyi}")