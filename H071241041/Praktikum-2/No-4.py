penggunaan_data = float(input("Masukkan penggunaan data (GB): "))
waktu_penggunaan = input("Mayoritas penggunaan di peak hours/off-peak? (peak/off-peak): ").lower()
jenis_pengguna = input("Jenis pengguna (personal/bisnis): ").lower()

if penggunaan_data < 10 and waktu_penggunaan == "off-peak" and jenis_pengguna == "personal":
    print("Paket A cocok untuk Anda")
elif 10 <= penggunaan_data <= 50 and waktu_penggunaan == "peak" and jenis_pengguna == "personal":
    print("Paket B cocok untuk Anda")
elif penggunaan_data > 50 and waktu_penggunaan == "peak" and (jenis_pengguna == "personal" or jenis_pengguna == "bisnis"):
    print("Paket C cocok untuk Anda")
elif penggunaan_data > 50 and waktu_penggunaan == "off-peak" and jenis_pengguna == "bisnis":
    print("Paket D cocok untuk Anda")
else:
    print("Tidak ada paket yang cocok.")
