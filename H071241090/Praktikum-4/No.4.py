def kalkulator_sederhana() :
    
    print ("Selamat datang di Kalkulator Sederhana!")

    hasil = 0

    try:
        x = int(input("Angka Pertama: "))
        y = int(input("Angka Kedua: "))
        operasi = (input("Operasi (+, -, *, /): "))
        if operasi == "+" :
            hasil = x+y
        elif operasi == "-" :
            hasil = x-y
        elif operasi == "*" :
            hasil = x*y
        elif operasi == "/" :
            if y == 0 :
                print ("Pembagian dengan 0 tidak dibolehkan")
                return
            else :
                hasil = x//y
        else :
            print ("Operasi tidak Valid. Gunakan +, -, *, /")
            return

        print (f"Hasil : {hasil}")
    except ValueError as e :
        print (f"Input tidak valid : could not convert string to float {e}")        
        return
        
kalkulator_sederhana()