def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")
    
    try:
        angka1 = float(input("Angka Pertama: "))
        angka2 = float(input("Angka Kedua: "))
        pilihan = input("Operasi (+, -, *, /): ")

        if pilihan == '+':
            hasil = angka1 + angka2
        elif pilihan == '-':
            hasil = angka1 - angka2
        elif pilihan == '*':
            hasil = angka1 * angka2
        elif pilihan == '/':
            if angka2 == 0:
                print("Pembagian dengan nol tidak diperbolehkan.")
                return
            hasil = angka1 / angka2
        else:
            print("Operasi tidak valid. Gunakan +, -, *, atau /.")
            return

        print(f"Hasil:{hasil: .0f}")

    except ValueError as e:
        print(f"Input tidak valid: {e}")

kalkulator()
