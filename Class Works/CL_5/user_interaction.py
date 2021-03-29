from Player import Player
import json


def main():
    editing = True
    players = []
    while editing:
        player_name = input("Enter player name: ")
        player_last_name = input("Enter player name: ")
        new_player = Player(player_name, player_last_name)
        value = input("Enter player result: ")
        if value.isdigit():
            new_player.set_score(int(value))
        players.append(new_player)
        age = 0
        while not new_player.set_age(age):
            age = int(input("Enter age: "))
        if input('Enter "+" if you add new player: ') != '+':
            editing = False
    print(*players)
    with open("players.json", "w") as f:
        json.dump([p.get_dict_repr() for p in players], f, indent=4)


if __name__ == '__main__':
    main()
