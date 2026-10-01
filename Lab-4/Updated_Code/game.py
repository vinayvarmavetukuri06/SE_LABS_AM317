import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    def __init__(self, length=5):
        self.length = length
        self.target = random.choice([w for w in WORDS if len(w) == length])
        self.history = []

    def _print_history(self):
        print("\nGuess history:")
        for number, (guess, feedback) in enumerate(self.history, start=1):
            print(f"{number}. {guess} -> {' '.join(feedback)}")

    def _print_summary(self, result):
        print("\nFinal Summary")
        print(f"Result: {result}")
        print(f"Accepted guesses: {len(self.history)}")
        print(f"Word length: {self.length}")

        if result == "Won" or result == "Lost":
            print(f"Target word: {self.target}")

    def run(self):
        print(f"Wordle — {self.length} letters, 6 guesses.")

        accepted_guesses = 0

        while accepted_guesses < 6:
            guess = input("> ").strip().lower()

            if guess == "q":
                print("Game quit.")
                self._print_history()
                self._print_summary("Quit")
                return

            if len(guess) != self.length or not guess.isalpha():
                print("Enter a valid word of the required length.")
                continue

            accepted_guesses += 1

            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))

            print(" ".join(feedback))
            self._print_history()

            if guess == self.target:
                print(f"Solved in {accepted_guesses} guesses!")
                self._print_summary("Won")
                return

        print("Game over! Better luck next time.")
        print("The word was:", self.target)
        self._print_summary("Lost")