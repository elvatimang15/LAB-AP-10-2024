import random

def hit_card():
    return random.randint(1, 11)

def blackjack():
    print("Welcome to Blackjack!")

    player_cards = [hit_card()]
    dealer_cards = [hit_card()]

    print(f"Kartu anda sekarang adalah: {sum(player_cards)}")

    while True:
        choice = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        
        if choice == "y":
            player_cards.append(hit_card())
            total_player = sum(player_cards)
            print(f"Kartu anda sekarang adalah: {total_player}")

            if total_player > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return
        elif choice == "n":
            break
        else:
            print("Input tidak valid, harap masukkan 'y' atau 'n'.")

    
    print(f"Kartu dealer adalah: {dealer_cards[0]}")
    total_dealer = sum(dealer_cards)
    print(f"Kartu dealer sekarang adalah: {total_dealer}")

    while total_dealer < 17:
        dealer_cards.append(hit_card())
        total_dealer = sum(dealer_cards)
        print(f"Kartu dealer sekarang adalah: {total_dealer}")

    if total_dealer > 21:
        print("Anda menang, kartu dealer melebihi 21.")
        return

    total_player = sum(player_cards)
    if total_player > total_dealer:
        print("Anda menang!")
    elif total_player == total_dealer:
        print("Seri!")
    else:
        print("Dealer menang!")

blackjack()
