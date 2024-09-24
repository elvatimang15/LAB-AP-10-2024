total_harga = int(input("Masukkan total harga: "))
uangdiberikan = int(input("Masukkan uang yang diberikan: "))
uangkasir = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
kembalian = uangdiberikan - total_harga
for k in uangkasir:  
    lembar = kembalian // k  
    if kembalian >= k:  
         kembalian %= k 
         print(f"{lembar} lembar {k}")