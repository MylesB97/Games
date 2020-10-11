import random
from collections import defaultdict


class HangMan(object):
    def __init__(self, *args, **kwargs):
        self.lives = 10
        self.guessed = []
        self.hm_dict = defaultdict(list)
        self.guess = ""
        self.word = ""
        self.answer = ""
        self.correct_guess = []

    def end_game(self):
        # breaks loop if lives run out
        if self.lives == 0:
            print("You Lose!")
            print("The word was %s" % self.word)

        # breaks loop if you guess correctly
        if self.correct_guess == self.answer:
            print("You Win!")
            print("The word was %s" % self.word)

    # validates words by trying to make them an integer and if it can't returns the word
    def validate(self, message):
        while True:
            val = input(message)
            try:
                val = int(val)
                print("Please enter a valid guess")
            except ValueError:
                return val

    # Loads words from english dictionary and creates list of words
    def load_words(self):
        with open('words_alpha.txt') as word_file:
            self.valid_words = set(word_file.read().split())

        return self.valid_words

    # Checks to see if Player 1 inputs a valid word
    def real_word(self, message):
        while True:
            self.words = self.load_words()
            if message in self.words:
                return message
            else:
                print("Word is not available")

    # 1 Player option
    def one_player(self):
        self.hm_words = self.load_words()

        # Creates a python dict where the key is the word length
        for hm_word in self.hm_words:
            self.hm_dict[len(hm_word)].append(hm_word)
        # prompts user for the length of the word and pulls words of that length from dict
        x = self.hm_dict.get(int(input("How Long Do You want your word to be?\n")))
        # selects random word from the list
        self.word = random.choice(x)
        self.answer = list(self.word.lower())
        self.correct_guess = list(len(self.word) * "_")

        while True:
            print(" \n \n")
            # breaks loop if lives run out
            if self.lives == 0:
                print("You Lose!")
                print("The word was %s" % self.word)
                break

            # breaks loop if you guess correctly
            if self.correct_guess == self.answer:
                print("You Win!")
                print("The word was %s" % self.word)
                break

            # shows the correct guesses and how many lives you have left
            print(" ".join(self.correct_guess))
            print("You have %d lives remaining" % self.lives)
            self.guess = self.validate("What is your guess?\n")

            # check to see if previously guessed
            if self.guess not in self.guessed:
                self.guessed.append(self.guess)
                # check to see if guess is incorrect
                if self.guess not in self.answer:
                    self.lives = self.lives - 1
                # if guess is correct put guess in right place
                else:
                    for i in range(0, len(self.answer)):
                        if self.guess == self.answer[i]:
                            self.correct_guess[i] = self.guess
            else:
                print("You already said that!")

    def two_player(self):
        # Checks to see if word player one uses is in the dictionary
        self.word = self.real_word(input("Player 1, What is your word?\n"))
        self.answer = list(self.word.lower())
        self.correct_guess = list(len(self.word) * "_")

        while True:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            # breaks loop if lives run out
            if self.lives == 0:
                print("You Lose!")
                print("The word was %s" % self.word)
                break

            # breaks loop if you guess correctly
            if self.correct_guess == self.answer:
                print("You Win!")
                print("The word was %s" % self.word)
                break

            # shows the correct guesses and how many lives you have left
            print(" ".join(self.correct_guess))
            print("You have %d lives remaining" % self.lives)
            self.guess = self.validate("Player 2, what is your guess?\n")

            # check to see if previously guessed
            if self.guess not in self.guessed:
                self.guessed.append(self.guess)
                # check to see if guess is incorrect
                if self.guess not in self.answer:
                    self.lives = self.lives - 1
                # if guess is correct put guess in right place
                else:
                    for i in range(0, len(self.answer)):
                        if self.guess == self.answer[i]:
                            self.correct_guess[i] = self.guess
            else:
                print("You already said that!")

    def start(self):
        mode = input("How many players are there \"1\" or \"2\"?\n").lower()
        if "1" in mode:
            self.one_player()
        elif "2" in mode:
            self.two_player()
        else:
            quit()
