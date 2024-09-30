import random

def draw_card(): #kartu undian
    """Mengambil kartu secara acak dengan nilai 1-11."""
    return random.randint(1, 11) #[11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,]

def calculate_total(cards):
    """Menghitung total nilai dari kartu."""
    return sum(cards)

def play_blackjack():
    print("Welcome to Blackjack!")
    
    # Inisialisasi kartu pemain dan dealer
    player_cards = [draw_card()] 
    dealer_cards = [draw_card()]
    
    print(f"Kartu anda sekarang adalah: {player_cards[0]}")
    
    # Giliran pemain
    while True:
        choice = input("Apakah masih akan mengambil kartu? (y/n) ").strip().lower()
        
        if choice == 'y':
            new_card = draw_card()
            player_cards.append(new_card)
            total_player = calculate_total(player_cards)
            print(f"Kartu anda sekarang adalah: {total_player}")
            
            if total_player > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return
        elif choice == 'n':
            break
        else:
            print("Pilihan tidak valid, silakan masukkan 'y' atau 'n'.")
            continue

    # Giliran dealer
    total_dealer = calculate_total(dealer_cards)
    print(f"Kartu dealer adalah: {dealer_cards[0]}")
    
    while total_dealer < 17:
        new_card = draw_card()
        dealer_cards.append(new_card)
        total_dealer = calculate_total(dealer_cards)
        print(f"Kartu dealer sekarang adalah: {total_dealer}")

    # Menentukan hasil
    print(f"Kartu anda: {total_player}, Kartu dealer: {total_dealer}")
    
    if total_dealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif total_player > total_dealer:
        print("Anda menang!")
    elif total_player < total_dealer:
        print("Dealer menang!")
    else:
        print("Seri!")

# Mulai permainan
play_blackjack()