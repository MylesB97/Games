from dice import Dice
from high_low import HighLow
from hangman_final import HangMan

dice_game = Dice()
hl_game = HighLow()
hm_game = HangMan()


def menu():
    print("Hello and Welcome players")
    print("Press 1 for Dice Rolling Game")
    print("Press 2 for Higher or Lower")
    print("Press 3 for Hangman")
    print("Press 4 for Exit")
    choice = input("Which Game would you like to play?\n")

    if choice == "1":
        dice_game.start()
        menu()
    elif choice == "2":
        hl_game.start()
        menu()
    elif choice == "3":
        hm_game.start()
        menu()
    elif choice == "4":
        print("Thanks for playing!")
        exit(0)
    else:
        print("Please enter a valid choice")
        menu()


if __name__ == '__main__':
    menu()
