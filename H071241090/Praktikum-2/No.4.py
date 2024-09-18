data = int(input("Masukkan jumlah data yang digunakan (GB) : "))
jam = input("Apakah mayoritas penggunaan di luar jam sibuk (off peak) atau di jam sibuk (peak)? ")
penggunaan = input("Apakah anda pengguna Personal atau Bisnis? ")

if data < 10 and jam == "off peak" and penggunaan == "personal":
    paket = "A"
elif 10 <= data <= 50 and jam == "peak" and penggunaan == "personal":
    paket = "B"
elif data > 50 and jam == "peak" and penggunaan == "personal":
    paket = "C"
elif data > 50 and jam == "peak" and penggunaan == "bisnis":
    paket = "C"
elif data > 50 and jam == "off peak" and penggunaan == "bisnis":
    paket = "D"
else:
    paket = "Tidak ada paket yang cocok"

# Output hasil
print(f"Paket yang cocok untuk anda adalah : Paket {paket}")
