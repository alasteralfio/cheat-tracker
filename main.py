import re

"""
4 players. Each player has a confirmed hand and an unconfirmed hand.
The confirmed hand consists of cards we literally saw go into the player.
the unconfirmed hand are the cards that were NOT revealed, but went into the player.

There is no confirmed or unconfirmed in the pile. Everything in pile is unconfirmed.
In further comments, there's also an "active pile", which are cards that were played
in that round. These cards could be revealed, and if so will be appended into confirmed
hands, but if not, they get added into the pile, which is unconfirmed.
"""
# Global variables
player_hands = {
    1: {"Confirmed": [], "Unconfirmed": []},
    2: {"Confirmed": [], "Unconfirmed": []},
    3: {"Confirmed": [], "Unconfirmed": []},
    4: {"Confirmed": [], "Unconfirmed": []}
}
round_num = 1
pile = []

def card_log(card_sequence):
    # Converts string card_sequence into a list of valid cards
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "Invalid"]
    card_return = []
    card_list = re.findall(r'10|[A-Za-z]|[2-9]', card_sequence)
    for card in card_list:
        card = card.upper()
        if card in cards:
            card_return.append(card)
    card_return.sort(key=lambda x: cards.index(x))
    return card_return

def cycle_player(player):
    # Cycles through the players and rounds
    round_num += 1
    if player == 4:
        return 1
    else:
        return player + 1

def round_count():
    # Returns the current card in play
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    return cards[(round_num - 1) % 13]

def main():
    game_running = True

    # Current player is asked only once as the program calculates the current players afterwards
    current_player = int(input("Enter starting player: "))
    
    while game_running:
        current_card = round_count()
        cards_played = []
        print(f"Round {round_num} - {current_card}")
        # Asks for the number of cards played by the current player
        card_amount = str(input(f"Enter '{current_card}'s played: "))

        # Adds played cards to the active pile
        for card in range(int(card_amount)):
            cards_played.append(current_card)

        bs_called = str(input("Was BS called? (y/n): ")).lower()
        if bs_called == "y":
            # Active hand is now revealed
            caller = int(input("Enter BS caller: "))
            correct = str(input("Was the call correct? (y/n): ")).lower()
            if correct == "y":
                # Appends active pile to confirmed, inactive pile to unconfirmed
                player_hands[current_player]["Confirmed"].extend(cards_played)
                player_hands[current_player]["Unconfirmed"].extend(pile)
            else:
                # Appends the active pile to the caller's hands
                cards_played = card_log(str(input("Enter cards revealed: ")))
                player_hands[caller]["Confirmed"].extend(cards_played)
                player_hands[caller]["Unconfirmed"].extend(pile)

        else:
            # BS not called, adds played cards (active pile) to the pile
            pile.extend(cards_played)
            current_player = cycle_player(current_player) # Cycles to the next player
        print(player_hands)


main()