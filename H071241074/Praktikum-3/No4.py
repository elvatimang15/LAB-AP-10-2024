total_harga = int(input("Masukkan total harga: "))
uang_diberikan = int(input("Masukkan uang yang diberikan: "))

pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
kembalian_uang = uang_diberikan - total_harga

for pecahan in pecahan_uang:
    if kembalian_uang >= pecahan:
        jumlah_lembar = kembalian_uang // pecahan
        kembalian_uang %= pecahan
        print(f" {jumlah_lembar} lembar Rp{pecahan: ,}")
