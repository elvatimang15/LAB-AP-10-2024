import random

def kartuacak():
    return random.randint(1, 11)

def hitungkalkulasikartu(cards):
    return sum(cards)

def blackjack():
    print("Welcome to Blackjack")
    
    # Inisialisasi kartu pemain dan dealer
    pemain_kartu = [kartuacak()]
    dealer_kartu = [kartuacak()]
    
    # Loop pemain untuk mengambil kartu atau berhenti
    while True:
        print(f"Kartu anda sekarang adalah: {', '.join(str(kartu) for kartu in pemain_kartu)}")
        print(f"Kartu dealer sekarang adalah {dealer_kartu[0]} (kartu tertutup)")
        
        # Jika total kartu pemain lebih dari 21, pemain kalah
        if hitungkalkulasikartu(pemain_kartu) > 21:
            print("Anda kalah, kartu anda melebihi 21.")
            return
        
        # Pemain memutuskan untuk mengambil kartu tambahan atau berhenti
        aksi = input("Apakah masih akan mengambil kartu? (y/n):  ").lower()
        if aksi == 'y':
            pemain_kartu.append(kartuacak())
        elif aksi == 'n':
            break
        else:
            print("Input tidak valid. Harap masukkan 'y' atau 'n'.")

    # Dealer akan terus mengambil kartu hingga total kartu mencapai 17 atau lebih
    while hitungkalkulasikartu(dealer_kartu) < 17:
        dealer_kartu.append(kartuacak())
    
    pemain_skor = hitungkalkulasikartu(pemain_kartu)
    dealer_skor = hitungkalkulasikartu(dealer_kartu)
    
    # Menampilkan hasil kartu dealer setelah mengambil kartu
    print(f"Kartu dealer sekarang adalah: {', '.join(str(kartu) for kartu in dealer_kartu)} (Total: {dealer_skor})")
    
    # Hasil akhir permainan
    if dealer_skor > 21:
        print("Anda menang, dealer melebihi 21.")
    elif pemain_skor > 21:
        print("Anda kalah, kartu anda melebihi 21.")
    elif pemain_skor > dealer_skor:
        print("Anda menang!")
    elif dealer_skor > pemain_skor:
        print("Dealer menang!")
    else:
        print("Seri!")

# Jalankan permainan Blackjack
blackjack()
