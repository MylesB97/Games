import random


class HighLow():
    def __init__(self):
        self.comp_guess = random.randint(1,100)
        self.guesses = 1
        self.user_guess = 0
        self.userint = self.user_guess

    def validate(self, message):
        while True:
            try:
                self.userint = int(input(message))
                if 1 <= self.userint <= 100:
                    return self.userint
                else:
                    print("You must enter a valid number")
            except ValueError:
                print("You must enter a valid number")
                # Reference: http://easypythondocs.com/validation.html

    def start(self):
        self.user_guess = self.validate("Pick a number between 1 & 100?\n")

        while self.comp_guess != self.user_guess:
            if self.user_guess > self.comp_guess:
                print("Too High!\n")
                self.user_guess = self.validate(">")
                self.guesses += 1
            else:
                print("Too Low!\n")
                self.user_guess = self.validate(">")
                self.guesses += 1
        else:
            print(f"Congratulations, it took you {self.guesses} guesses")
