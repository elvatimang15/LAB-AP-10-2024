total = int(input("Masukkan total harga : "))
uang = int(input("Masukkan uang yang diberikan : "))
kembalian = uang - total

pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
lembar = [0] * len(pecahan)

for i in range(len(pecahan)):
    while kembalian >= pecahan[i]:
        lembar[i] += 1
        kembalian -= pecahan[i]

for i in range(len(pecahan)):
    if lembar[i] > 0:
        print(f"{lembar[i]} lembar Rp.{pecahan[i]}")
#loop ini berfungsi utk tidak print lembar yang 0