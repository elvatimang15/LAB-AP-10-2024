harga_saham_kemarin = float(input("Masukkan harga saham kemarin: "))
harga_saham_hari_ini = 105.0

perubahan_persen = ((harga_saham_hari_ini - harga_saham_kemarin) / harga_saham_kemarin) * 100
jual = (perubahan_persen > 5) * 1
beli = (perubahan_persen < -3) * 1
tahan = (perubahan_persen <= 5) and (perubahan_persen >= -3) * 1

rekomendasi = jual * 'jual' + beli * 'beli' + tahan * 'tahan'
print(f"Perubahan persentase harga: {perubahan_persen:.2f}%")
print(f"Rekomendasi: {rekomendasi}")