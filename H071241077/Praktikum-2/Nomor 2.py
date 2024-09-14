# Soal 2
Usia_pengunjung = int(input("Masukkan usia : "))
Anggota = input("Apakah anda anggota (ya/tidak) : ")

if Usia_pengunjung < 5:
    harga_dasar = 0
elif Usia_pengunjung <= 12:
    harga_dasar = 50000
elif Usia_pengunjung <= 59:
    harga_dasar = 100000
else: 
    harga_dasar = 70000

harga_akhir = harga_dasar - (harga_dasar * 20/100) if Anggota == "ya" else harga_dasar

print(f"harga tiket = Rp.{harga_akhir}")