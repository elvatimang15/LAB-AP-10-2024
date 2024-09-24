total_harga = int(input("Masukkan total harga: "))
uang_diberikan = int(input("Masukkan jumlah uang yang diberikan: "))

if uang_diberikan < total_harga:
    print("uang tidak cukup.")
else:
    kembalian = uang_diberikan - total_harga

    pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

    print("Kembalian:", kembalian)

    for uang in pecahan_uang:
        if kembalian >= uang:
            jumlah_lembar = kembalian // uang
            kembalian = kembalian % uang
            print(f"Lembaran {uang}: {jumlah_lembar}")
