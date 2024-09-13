harga_kemarin = float(input("Masukkan harga saham kemarin: "))
harga_hari_ini = 105.0

perubahan_persen = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

rekomendasi = ("Beli" * (perubahan_persen > 5) +
               "Tahan" * (-3 <= perubahan_persen <= 5) +
               "Jual" * (perubahan_persen < -3))

print(f"Perubahan persentase: {perubahan_persen:.2f}%")
print(f"Rekomendasi investasi: {rekomendasi}")
