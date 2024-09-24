populasi_a = int(input("Masukkan populasi awal Serangga A: "))
populasi_b = int(input("Masukkan populasi awal Serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))


for hari in range(1, jumlah_hari + 1):
    if hari % 2 != 0:
        populasi_a = populasi_a * 1.3  
        populasi_b = populasi_b * 1.5
    else:
        populasi_a = populasi_a * 0.8  
        populasi_b = populasi_b * 0.6

    if hari % 5 == 0:
        print(f"Hari {hari}: Predator memakan 10% populasi.")
        populasi_a = populasi_a * 0.9  
        populasi_b = populasi_b * 0.9
    
    if populasi_a < 1:
        populasi_a = 0

    if populasi_b < 1:
        populasi_b = 0

    populasi_a_akhir = f"{populasi_a:.0f}" if populasi_a > 0 else 'telah habis'
    populasi_b_akhir = f"{populasi_b:.0f}" if populasi_b > 0 else 'telah habis'

    print(f"Hari {hari}: {'Serangga A =' if populasi_a > 0 else 'Serangga A'} {populasi_a_akhir}, {'Serangga B =' if populasi_b > 0 else 'Serangga B'} {populasi_b_akhir}")
