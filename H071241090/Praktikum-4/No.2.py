def game_harta_karun() :
    
    langkah = 0
    total_langkah = 0
    bahaya = False

    while True :
        total_langkah += langkah
        
        try:
            langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai : "))
        except ValueError:
            print ("Input tidak valid. Masukkan bilangan bulat.")

        if langkah < 0 :
            print("Langkah tidak boleh negatif.")
            continue

        if langkah > 20 :
            bahaya = True
            continue
        
        if langkah == 0 :
            print (f"Total jarak : {total_langkah} ")

            if total_langkah >= 50 :
            
                if bahaya == True :
                    print ("Tidak aman untuk menggali harta karun. Coba lagi!")
                    return
                elif bahaya == False :
                    if bahaya:
                        print ("Tidak aman untuk menggali harta karun. Coba lagi!")
                        return
                    elif total_langkah == 50 :
                        print ("Aman! Kamu tepat menemukan harta karun dan menang!")
                        return
                    else : 
                        print ("Tidak menemukan harta karun. Coba lagi!")
                        return
                
            elif total_langkah < 50:
                print ("Tidak menemukan harta karun. Coba lagi!")
                return

game_harta_karun()