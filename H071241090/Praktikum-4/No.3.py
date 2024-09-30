def teka_teki():
    langkah = 0

    try:
        angka = int(input("Masukkan angka : "))
    except ValueError :
        print ("Input tidak Valid")
        return

    while angka != 1 :
        
        if angka % 2 == 0 :
            angka = angka // 2
        else :
            angka = (angka*3) + 1
            
        langkah += 1

        print (float(angka))
    
    print (f"Jumlah langkah : {langkah}")

teka_teki()