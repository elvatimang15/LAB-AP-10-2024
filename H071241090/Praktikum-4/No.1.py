import random

def tarik_kartu() :
    return random.randint(1,11)

def blackjack() :
    print ("Welcome to Blackjack!")

    pemain = tarik_kartu()
    dealer = tarik_kartu()

    print (f"Kartu anda sekarang adalah : {pemain}")

    while pemain <= 21:
        ambil_kartu = input("Apakah masih akan mengambil kartu? (y/n) : ")

        if ambil_kartu == "y":
            pemain += tarik_kartu()
            print (f"Kartu anda sekarang adalah : {pemain}")

            if pemain > 21:
                print("Anda kalah! Kartu anda melebihi 21")
                return
            
        elif ambil_kartu == "n":
            break

        else :
            print ("Inputan tidak valid. Masukkan y/n")
            continue

    if pemain <= 21 :
        print (f"Kartu dealer sekarang adalah : {dealer}") 

        while dealer <= 17 :
            dealer += tarik_kartu()
            print (f"Kartu dealer sekarang adalah : {dealer}") 

        if dealer > 21 :
            print ("Anda Menang! Dealer melebihi 21")
            return
    
    if pemain > dealer :
        print ("Anda Menang!")
    elif pemain == dealer :
        print ("Permainan Seri!")
    elif pemain < dealer :
        print ("Dealer Menang!")
        
blackjack()
