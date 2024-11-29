baris = int(input("Masukkan jumlah baris: "))
input_ganjil = baris % 2 != 0
max_width = (baris if input_ganjil else baris - 1) * 2 - 1
space = ""

for i in range(1, baris // 2 + 1):
    print((space, "*" * (2 * i - 1)).center(max_width))

if input_ganjil:
    print((space, "*" * baris).center(max_width))

for i in range(baris // 2, 0, -1):
    print((space, "*" * (2 * i - 1)).center(max_width))