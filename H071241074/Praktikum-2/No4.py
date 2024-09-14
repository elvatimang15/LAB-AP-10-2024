penggunaan_data = float(input("Masukkan jumlah data yang digunakan (GB): "))
waktu_penggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak)? atau di jam sibuk (peak) (off-peak/peak): ")
jenis_pengguna = input("Apakah Anda pengguna Personal atau Bisnis? (personal/bisnis): ")


if penggunaan_data < 10:
    if waktu_penggunaan == "off-peak" and jenis_pengguna == "personal":
        print("Paket yang sesuai: Paket A")
    else:
        print("Tidak ada paket yang cocok")
elif 10 <= penggunaan_data <= 50:
    if waktu_penggunaan == "peak" and jenis_pengguna == "personal":
        print("Paket yang sesuai: Paket B")
    else:
        print("Tidak ada paket yang cocok")
elif penggunaan_data > 50:
    if jenis_pengguna == "personal" or jenis_pengguna == "bisnis" and waktu_penggunaan == "peak":
        print("Paket yang sesuai: Paket C")
    elif jenis_pengguna == "bisnis" and waktu_penggunaan == "off-peak":
        print("Paket yang sesuai: Paket D")
else:
    print("Tidak ada paket yang cocok")