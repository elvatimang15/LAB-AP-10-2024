sahamkemarin = int(input("Masukkan harga saham kemarin: "))
sahamtoday = int(input("Masukka harga saham hari ini: "))

persentase_saham = ((sahamtoday - sahamkemarin) / sahamkemarin) * 100 

jangka = round(persentase_saham, 2)

beli = (persentase_saham > 5) * 1
jual = (persentase_saham < -3) * 1
tahan = (persentase_saham >= -3) * (persentase_saham <= 5) * 1

rekomendasi = "Beli" * beli + "Jual" * jual + "Tahan" * tahan

print(f"Perubahan persentase harga saham: {jangka}%")
print(f"Rekomendasi investasi: {rekomendasi}")