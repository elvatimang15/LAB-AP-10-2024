jumlah_data = float(input("Masukkan jumlah data yang digunakan (GB): "))
offorpeak = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? ")
PerBis = (input("Apakah Anda pengguna Personal atau Bisnis? "))

if jumlah_data < 10:
    if offorpeak == "off-peak":
        if PerBis == "personal":
            paket = "Paket A"
        else:
            paket = "Tidak ada paket yang cocok"
    else:
        paket = "Tidak ada paket yang cocok"
elif 10 <= jumlah_data <= 50:
    if offorpeak == "peak":
        if PerBis == "personal":
            paket = "Paket B"
        else:
            paket = "Tidak ada paket yang cocok"
    else:
        paket = "Tidak ada paket yang cocok"
else:
    if offorpeak == "peak":
        if PerBis == "personal":
            paket = "Paket C"
        elif PerBis == "bisnis":
            paket = "Paket C"
        else:
            paket = "Tidak ada paket yang cocok"
    elif offorpeak == "off-peak":
        if PerBis == "bisnis":
            paket = "Paket D"
        else:
            paket = "Tidak ada paket yang cocok"
    else:
        paket = "Tidak ada paket yang cocok"

print(f"Paket yang sesuai: {paket}")