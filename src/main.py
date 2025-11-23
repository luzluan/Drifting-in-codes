from engine import create_player, show_status, lose_oxygen


def main():
    player = create_player()
    print("Player Initialized:")
    print(player)

    lose_oxygen(player)
    show_status(player)


if __name__ == "__main__":
    main()

