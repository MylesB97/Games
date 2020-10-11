import random


class Dice():
    def __init__(self):
        self.comp_guess = random.randint(1, 6)
        self.guesses = 1
        self.user_guess = 0
        self.userint = self.user_guess

    def validate(self, message):
        while True:
            try:
                self.userint = int(input(message))
                if 1 <= self.userint <= 6:
                    return self.userint
                else:
                    print("You must enter a valid number")
            except ValueError:
                print("You must enter a valid number")

    def start(self):
        self.user_guess = self.validate("Pick a number between 1 & 6?\n")

        while self.user_guess != self.comp_guess:
            if self.user_guess > self.comp_guess:
                self.guesses += 1
                print("Try Again")
                self.user_guess = self.validate("> ")
            else:
                self.guesses += 1
                print("Try Again")
                self.user_guess = self.validate("> ")
        else:
            print("Congratulations it took you %d guesses" % self.guesses)
