saham_kemarin = float(input("Masukkan harga saham kemarin : "))
saham_hari_ini = 105.0

perubahan_persen = ((saham_hari_ini-saham_kemarin)/saham_kemarin ) *100

beli = (perubahan_persen > 5) * 1
tahan = (-3 <= perubahan_persen <= 5 ) * 1
jual = (perubahan_persen < -3) * 1

rekomendasi_investasi = beli * "Beli" + tahan * "Tahan" + jual * "jual"

print (f"Perubahan persentase harga saham : {perubahan_persen : .2f}%")
print ("Rekomendasi Investasi :", rekomendasi_investasi)