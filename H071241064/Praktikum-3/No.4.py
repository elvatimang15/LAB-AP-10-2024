pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

total_harga = int(input("Masukkan total harga: "))
uang_diberikan = int(input("Masukkan jumlah uang yang diberikan: "))
    
kembalian = uang_diberikan - total_harga
    
if kembalian < 0:
    print("Uang yang diberikan tidak cukup.")
else:
    print(f"Kembalian: {kembalian}")
        
for pecahan_uang in pecahan:
    jumlah_lembar = kembalian // pecahan_uang
    if jumlah_lembar > 0:
        print(f"{jumlah_lembar} lembar Rp {pecahan_uang}")
        kembalian %= pecahan_uang