# Soal 4
Penggunaan_data = float(input("Masukkan jumlah data yang digunakan (GB): "))
Waktu_penggunaan = input("Apakah mayoritas penggunaan diluar jam sibuk (off-peak) atau di jam sibuk (peak)?: ")
Jenis_pengguna = input("Apakah anda pengguna Personal atau Bisnis? : ")

if Penggunaan_data < 10 and Waktu_penggunaan == "off-peak" and Jenis_pengguna == "personal":
  print("Paket A")
elif 10 >= Penggunaan_data <= 50 and Waktu_penggunaan == "peak" and Jenis_pengguna == "personal":
  print("Paket B")
elif Penggunaan_data > 50 and Waktu_penggunaan == "peak" and (Jenis_pengguna == "personal" and Jenis_pengguna == "bisnis"):
  print("Paket C")
elif Penggunaan_data > 50 and Waktu_penggunaan == "off-peak" and Jenis_pengguna == "bisnis":
  print("Paket D")
else:
  print("Tidak ada paket yang cocok")
