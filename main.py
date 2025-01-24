import re

"""
4 players. Each player has a confirmed hand and an unconfirmed hand.
The confirmed hand consists of cards we literally saw go into the player.
the unconfirmed hand are the cards that were NOT revealed, but went into the player.

There is no confirmed or unconfirmed in the pile. Everything in pile is unconfirmed.
In further comments, there's also an "active pile", which are cards that were played
in that round. These cards could be revealed, and if so will be appended into confirmed
hands, but if not, they get added into the pile, which is unconfirmed.

The only exception to the above statement is where Player 1 (you) plays. In that case,
the card will ALWAYS be confirmed.
"""
# Global variables
player_hands = {
    1: {"Confirmed": [], "Unconfirmed": []},
    2: {"Confirmed": [], "Unconfirmed": []},
    3: {"Confirmed": [], "Unconfirmed": []},
    4: {"Confirmed": [], "Unconfirmed": []}
}
round_num = 1

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

def print_hands():
    return f"""
    ====== Player 1 ======
    Confirmed  : {player_hands[1]["Confirmed"]}
    Unconfirmed: {player_hands[1]["Unconfirmed"]}

    ====== Player 2 ======
    Confirmed  : {player_hands[2]["Confirmed"]}
    Unconfirmed: {player_hands[2]["Unconfirmed"]}

    ====== Player 3 ======
    Confirmed  : {player_hands[3]["Confirmed"]}
    Unconfirmed: {player_hands[3]["Unconfirmed"]}

    ====== Player 4 ======
    Confirmed  : {player_hands[4]["Confirmed"]}
    Unconfirmed: {player_hands[4]["Unconfirmed"]}
    """

def cycle_player(player, bs):
    # Cycles through the players and rounds
    global round_num
    round_num += 1
    if bs != 0:
        return bs
    elif player == 4:
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
        bs_caller = 0
        pile = []
        confirmed_pile = []
        current_card = round_count()
        cards_played = []
        print(f"Round {round_num} - Card: {current_card} - Player: {current_player}")
        # Asks for the number of cards played by the current player
        if current_player != 1:
            card_amount = str(input(f"Enter '{current_card}'s played: "))

            # Adds played cards to the active pile
            for card in range(int(card_amount)):
                cards_played.append(current_card)
                if current_card in player_hands[current_player]["Unconfirmed"]:
                    player_hands[current_player]["Unconfirmed"].remove(current_card)
                elif current_card in player_hands[current_player]["Confirmed"]:
                    player_hands[current_player]["Confirmed"].remove(current_card)

        else: # If its your turn
            player_cards = card_log(str(input("Enter cards revealed: ")))
            for card in player_cards:
                cards_played.append(card)
            player_hands[1]["Confirmed"].clear()
            player_hands[1]["Unconfirmed"].clear()

        bs_called = str(input("Was BS called? (y/n): ")).lower()
        if bs_called == "y":
            # Active hand is now revealed
            caller = int(input("Enter BS caller: "))
            correct = str(input("Was the call correct? (y/n): ")).lower()
            if correct == "y":
                bs_caller = caller
                # Appends active pile to confirmed, inactive pile to unconfirmed
                cards_played = card_log(str(input("Enter cards revealed: ")))
                player_hands[current_player]["Confirmed"].extend(cards_played)
                player_hands[current_player]["Confirmed"].extend(confirmed_pile)
                player_hands[current_player]["Unconfirmed"].extend(pile)
            else:
                # Appends the active pile to the caller's hands
                player_hands[caller]["Confirmed"].extend(cards_played)
                player_hands[caller]["Confirmed"].extend(confirmed_pile)
                player_hands[caller]["Unconfirmed"].extend(pile)

        else:
            # BS not called, adds played cards (active pile) to the pile
            if current_player != 1:
                pile.extend(cards_played)
            else: # You played these cards
                confirmed_pile.extend(cards_played)
        current_player = cycle_player(current_player, bs_caller) # Cycles to the next player
        print(print_hands())


main()