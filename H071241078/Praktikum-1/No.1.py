harga_saham_kemarin = float(input("Masukkan harga saham kemarin: "))
harga_saham_hari_ini = 105.0

perubahan_persentase = ((harga_saham_hari_ini - harga_saham_kemarin) / harga_saham_kemarin) * 100

Beli = (perubahan_persentase > 5) * 1
Tahan =( -3 <= perubahan_persentase <= 5) * 1
jual = (perubahan_persentase < -3 ) * 1

rekomendasi = Beli * "beli" + Tahan * "tahan" + jual * "jual"

print(f"Perubahan persentase: {perubahan_persentase:.2f}%")
print(f"rekomendasi investasi: {rekomendasi}")
