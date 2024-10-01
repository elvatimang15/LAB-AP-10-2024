def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")
    
    try:
        angka_pertama = float(input("Angka pertama: "))
    except ValueError as e:
        # jika inputnya bukan angka 
        print("Input tidak valid: tidak bisa mengonversi string ke float. {e}")
        return
    
    try:
        angka_kedua = float(input("Angka kedua: "))
    except ValueError as e:
        # jika inputnya bukan angka
        print("Input tidak valid: tidak bisa mengonversi string ke float. {e}")
        return
    
    operasi = input("Operasi (+, -, *, /): ")
    
    if operasi == "+":
        hasil = angka_pertama + angka_kedua
    elif operasi == "-":
        hasil = angka_pertama - angka_kedua
    elif operasi == "*":
        hasil = angka_pertama * angka_kedua
    elif operasi == "/":
        if angka_kedua == 0:
            print("Pembagian dengan nol tidak diperbolehkan.")
            return
        hasil = angka_pertama / angka_kedua
    else:
        # jika yg di input bukan simbol di atas
        print("Operasi tidak valid.")
        return

    print(f"Hasil: {hasil}")

kalkulator()
