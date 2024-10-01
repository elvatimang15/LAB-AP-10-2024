print("Selamat datang di Kalkulator Sederhana!")
def operasi():
    try:
        pertama = float(input("Angka pertama: "))
        kedua = float(input("Angka kedua: "))
        operasi = input("(+, -, *, /): ")
    
        if operasi == "+":
                hasil = pertama + kedua
        elif operasi == "-":
                hasil = pertama - kedua
        elif operasi == "*":
                hasil = pertama * kedua
        elif operasi == "/":
            if kedua == 0:
                    print("Pembagian dengan nol tidak diperbolehkan")
                    return
            hasil = pertama / kedua
        else:
            print("Operasi tidak valid. Gunakan +, -, *, /.")
            return
        print(f"Hasil: {hasil}")
        
    except ValueError as e:
        print(f"Input tidak valid: could not convert string to float: {e}")
operasi()
    
    
