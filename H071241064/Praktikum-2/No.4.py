# 4

penggunaan_data = float(input("Masukkan jumlah data yang digunakan (GB): "))
waktu_penggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak): ")
jenis_pengguna = input("Apakah anda pengguna personal atau bisnis? (personal/bisnis): ")

if penggunaan_data < 10 and waktu_penggunaan == "off-peak" and jenis_pengguna == "personal":
  print("Paket A")
elif 10 >= penggunaan_data <= 50 and waktu_penggunaan == "peak" and jenis_pengguna == "personal":
  print("Paket B")
elif penggunaan_data > 50 and waktu_penggunaan == "peak" and (jenis_pengguna == "personal" or jenis_pengguna == "bisnis"):
  print("Paket C")
elif penggunaan_data > 50 and waktu_penggunaan == "off-peak" and jenis_pengguna == "bisnis":
  print("Paket D")
else:
  print("Tidak ada paket yang cocok")