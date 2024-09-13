# soal 1
saham_kemarin = float(input("harga saham kemarin : "))
saham_sekarang = float(105.0)

persentase = ((saham_sekarang - saham_kemarin)/saham_kemarin)*100

beli = persentase>5
tahan = 5>=persentase>=-3
jual = persentase<=-3

Rekomendasi_invest = "Beli"*beli + "Tahan"*tahan + "Jual"*jual

print(f"Perubahan persentase harga saham : {persentase:.2f}%")
print(f"rekomendasi investasi : {Rekomendasi_invest}")