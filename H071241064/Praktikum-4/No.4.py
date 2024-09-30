def kalkulator():
    print("Selamat datang di kalkulator sederhana!")
    
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError as e:
        print(f"Input tidak valid. {e}")
        return  

    operasi = input("Operasi (+, -, *, /): ")

    if operasi == '+':
        hasil = angka1 + angka2
        print(f"Hasil: {hasil}")
    elif operasi == '-':
        hasil = angka1 - angka2
        print(f"Hasil: {hasil}")
    elif operasi == '*':
        hasil = angka1 * angka2
        print(f"Hasil: {hasil}")
    elif operasi == '/':
        if angka2 == 0:
            print("Pembagian dengan nol tidak diperbolehkan")
        else:
            hasil = angka1 / angka2
            print(f"Hasil: {hasil}")
    else:
        print("Operasi tidak valid. Harap pilih +, -, *, atau /.")

# Menjalankan kalkulator
if __name__ == "__main__":
    kalkulator()
