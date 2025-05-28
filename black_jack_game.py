import random
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []
    for suit in suits:
        for value in values:
            deck.append((suit, value))

    random.shuffle(deck)
    return deck

def calculate_score(hand):
    score = 0
    aces = 0
    
    for card in hand:
        value = card[1]
        if value in ['J', 'Q', 'K']:
            score += 10
        elif value == 'A':
            aces += 1
        else:
            score += int(value)
    
    for _ in range(aces):
        if score + 11 <= 21:
            score += 11
        else:
            score += 1
            
    return score

def print_hand(name, hand, hide_dealer=False):
    if hide_dealer and name == "Dealer":
        print(f"{name}'s hand: {hand[0]}, Hidden Card")
    else:
        print(f"{name}'s hand:", end=" ")
        for card in hand:
            print(f"{card[1]} of {card[0]}", end=", ")
        print(f"Score: {calculate_score(hand)}")

def play_game():
    deck = create_deck()
    player_hand = []
    dealer_hand = []
    
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    
    while True:
        print("\n" + "="*20)
        print_hand("Dealer", dealer_hand, hide_dealer=True)
        print_hand("Player", player_hand)
        
        player_score = calculate_score(player_hand)
        if player_score > 21:
            print("Bust! You lose!")
            return
        if player_score == 21:
            print("Blackjack! You win!")
            print(""".------..------..------..------..------..------..------..------..------.
                    |B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
                    | :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
                    | ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
                    | '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
                    `------'`------'`------'`------'`------'`------'`------'`------'`------'
                """)
            return
        
        choice = input("Do you want to hit (h) or stand (s)? ").lower()
        if choice == 'h':
            player_hand.append(deck.pop())
        elif choice == 's':
            break
    
    print("\nDealer's turn:")
    print_hand("Dealer", dealer_hand)
    
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print_hand("Dealer", dealer_hand)
    
    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)
    
    print("\nFinal scores:")
    print(f"Your score: {player_score}")
    print(f"Dealer's score: {dealer_score}")
    
    if dealer_score > 21:
        print("Dealer busts! You win!")
    elif dealer_score > player_score:
        print("Dealer wins!")
    elif player_score > dealer_score:
        print("You win!")
    else:
        print("It's a tie!")

while True:
    play_game()
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        break

print("Thanks for playing!")