inputdetik = int(input("Masukkan jumlah detik: "))
jam = inputdetik // 3600
sisa_detik= inputdetik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60
print(f"{jam:02d}:{menit:02d}:{detik:02d}")