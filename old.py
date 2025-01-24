import re

def card_log(card_sequence):
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "Invalid"]
    card_return = []
    card_list = re.findall(r'10|[A-Za-z]|[2-9]', card_sequence)
    for card in card_list:
        card = card.upper()
        if card in cards:
            card_return.append(card)
    card_return.sort(key=lambda x: cards.index(x))

    return card_return

def print_players(players):
    for player in players:
        print(player, ":", players[player])

def play_game():
    game_running = True
    players = {"player_1": [], "player_2": [], "player_3": [], "player_4": []}
    while game_running:
        choice = str(input("Enter cards played:"))
        if choice == "0":
            print(players)
            game_running = False
        else:
            print(card_log(choice))
            card_player = str(input("Enter player:"))
            if card_player == "1":
                players["player_1"].extend(card_log(choice))
            elif card_player == "2":
                players["player_2"].extend(card_log(choice))
            elif card_player == "3":
                players["player_3"].extend(card_log(choice))
            elif card_player == "4":
                players["player_4"].extend(card_log(choice))
            print_players(players)



if __name__ == "__main__":
    play_game()