class game_logic():
    def __init__(self, level, secret_number):
        self.level = level
        self.secret_number = secret_number

    def level_checker (self, level):
        if self.level == 'easy':
            print("\nYou have 13 Guesses\n")
            return 13
        elif self.level == 'intermediate':
            print("\nYou have 10 Guesses\n")
            return 10
        elif self.level == 'hard':
            print("\nYou have 7 Guesses\n")
            return 7

    def number_checker (self, guess):
        if guess == self.secret_number:
            print("Congratulations!!! Your Guess was right.")
            return True
        elif guess > self.secret_number and abs(guess - self.secret_number) > 5:
            print ("Your guess was too high")
            return False
        elif guess > self.secret_number and abs(guess - self.secret_number) < 5:
            print("your Guess was a bit high")
            return False
        elif guess < self.secret_number and abs(guess - self.secret_number) > 5:
            print("Your guess was too low")
            return False
        elif guess < self.secret_number and abs(guess - self.secret_number) < 5:
            print("Your guess was  a bit low")
            return False
            

        


