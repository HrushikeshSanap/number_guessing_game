import random
import logic

def main():
    print("Hi. Welcome to Number Guessing Game. \nThe number is between 1 to 50. \nYou will get 7 guesses to indentify the secret number. \nSo Let's begin...")
    level = input("Choose your level: \nEasy\t|\tIntermediate\t|\tHard\n")
    secret_number = random.randint(1, 50)
    print(secret_number)
    game_start = logic.game_logic(level, secret_number )

    total_guesses = game_start.level_checker(level)
    guess_count = 1

    while guess_count <= total_guesses:
        guess = int(input(f"Your Guess no {guess_count} is  "))
        win = game_start.number_checker(guess)
        if win:
            break
        else:
            guess_count += 1
            continue
    else:
        print("Better luck next time!!!")
    

if __name__ == '__main__':
    main()