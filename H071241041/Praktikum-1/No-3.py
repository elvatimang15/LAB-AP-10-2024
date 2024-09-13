x = int(input("masukkan detik: "))
jam = x // 3600
sisa_detik = x % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print(f"{jam:02}:{menit:02}:{detik:02}")

print(f"Waktu dalam format jam:menit:detik adalah: {jam:02}:{menit:02}:{detik:02}")