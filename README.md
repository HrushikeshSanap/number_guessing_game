
# Number Guessing Game

This is a simple Number Guessing Game built in Python, where players try to guess a randomly generated number within a range. The game has three difficulty levels, each with a different number of attempts. The game logic is separated into two modules: `logic.py`, which handles the core logic, and `main.py`, which serves as the entry point for the game.

## Features

- **Three Difficulty Levels**:
  - **Easy**: 13 attempts
  - **Intermediate**: 10 attempts
  - **Hard**: 7 attempts
- **Hints**: The game provides feedback on whether a guess is "too high" or "too low," with additional hints on proximity to the secret number.

## Files

- `logic.py`: Contains the `game_logic` class with methods for checking guesses and managing attempts based on difficulty level.
- `main.py`: Main script to run the game, which interacts with the player, accepts inputs, and utilizes the `game_logic` class from `logic.py`.

## Requirements

- Python 3.x

## How to Play

1. Run the `main.py` file:
   ```bash
   python main.py
   ```

2. Select a difficulty level when prompted:
   ```
   Choose your level:
   Easy | Intermediate | Hard
   ```

3. Guess a number between 1 and 50 within the allowed attempts for the selected difficulty.

4. The game will give hints to help you narrow down the number:
   - "too high" or "too low"
   - "a bit high" or "a bit low" if the guess is close

5. If you guess the number correctly, you win! Otherwise, you can try again until you run out of attempts.

## Example

```plaintext
Hi. Welcome to Number Guessing Game. 
The number is between 1 to 50. 
So Let's begin...

Choose your level: 
Easy	|	Intermediate	|	Hard
Intermediate

You have 10 Guesses

Your Guess no 1 is 25
Your guess was too low
...
Congratulations!!! Your Guess was right.
```

## Code Structure

- `game_logic(level, secret_number)`: Initializes the game with the selected difficulty level and a randomly generated secret number.
- `level_checker(level)`: Returns the number of attempts based on the chosen level.
- `number_checker(guess)`: Compares the player's guess to the secret number, giving hints and returning `True` if the guess is correct.

Enjoy the game and good luck!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
