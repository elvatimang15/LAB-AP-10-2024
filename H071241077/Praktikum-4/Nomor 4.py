print("Selamat datang di Kalkulator Sederhana!")

try:
    Angka1 = float(input("Masukkan angka pertama: "))
    Angka2 = float(input("Masukkan angka kedua: "))
    
    operator = str(input("Operasi (+, -, *, /): "))
    
    if operator == "+":
        print("Hasil: ", Angka1 + Angka2)
    elif operator == "-":
        print("Hasil: ", Angka1 - Angka2)
    elif operator == "*":
        print("Hasil: ", Angka1 * Angka2)
    elif operator == "/":
        try:
            print("Hasil: ", Angka1 / Angka2)
        except ZeroDivisionError:
            print("Pembagian dengan 0 tidak diperbolehkan")
    else:
        print("Operasi tidak valid. Gunakan +, -, *, atau /.")        
    
except ValueError as a:
    print(f"Input tidak valid: {a}")
