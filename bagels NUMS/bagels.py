import random as r

from utils.exceptions import AccessError, ActionError

class BagelsGame:
    _alphabet = "1234567890"
    _current_guess = None
    _answer = None
    _active_game = False

    def __init__(self, number_of_digits: int, number_of_guesses: int):
        self.set_number_of_digits(number_of_digits)
        self.set_number_of_guesses(number_of_guesses)

    def greeting(self) -> str:
        return f"""Hey! I thought up a {self._number_of_digits}-digit number. 
        You have {self._number_of_guesses} guesses to get the number. Otherwise, 
i'll kill whole world. So, please, pull yourself together :)
I know about your silly mind so i'll give you some clues during our pretty game:
When i say:         That means:
    Pico             One digit is correct but in the wrong position.
    Fermi            One digit is correct and in the right position.
    Bagels           No correct digits in your guess >:c.

The clues will be represented in the alphabet order, so the position of a clue means nothing.
So, lets start the game!"""

    def start_game(self):
        """Start of the game"""
        if not self._active_game:
            self._active_game = True
            self._current_guess = 1
            self._answer = self._create_word()
        else:
            raise ActionError("Game already started.")

    def end_game(self):
        """End of the game"""
        if self._active_game:
            self._active_game = False
        else:
            raise ActionError("Game already ended.")

    def user_guess(self, guess: str):
        # checking whether the input is valid
        if len(guess) == self._number_of_digits and guess.isdecimal():

            # case of the user win
            if guess == self._answer:
                self.end_game()
                return f"Congrats! You guessed the number \"{self._answer}\" within {self._current_guess} guesses!"

            # case of the user lose
            elif guess != self._answer and self._current_guess == self._number_of_guesses:
                self.end_game()
                return f"Oops. Seems like you failed the world. The right number was \"{self._answer}\"."

            self._current_guess += 1
            clues = []

            # filling up the clues array
            for i in range(self._number_of_digits):
                if guess[i] == self._answer[i]:
                    clues.append("Fermi")
                elif guess[i] in self._answer:
                    clues.append("Pico")

            # case of no clues (no correct digits in the guess)
            if len(clues) == 0:
                clues.append("Bagels")
            else:
                # sorting clues to disable the user to detect the position of the correct letter
                clues.sort()

            clue = " ".join(clues)

        # formatting the wrong input message
        else:
            clue = "Wrong input!\n"

            # case of the wrong length
            if len(guess) != self._number_of_digits:
                clue += f'You need to write {self._number_of_digits} digits!\n'

            # case of the wrong letters usage
            if not guess.isdecimal():
                clue += "You should use only digits.\n"

        return clue

    def get_current_guess(self) -> int:
        if self._active_game:
            return self._current_guess
        else:
            raise AccessError("Can't access because game not started.")

    def get_game_state(self) -> int:
        return self._active_game

    def set_number_of_digits(self, number_of_digits: int) -> None:
        if (10 >= number_of_digits >= 1) and not self._active_game:
            self._number_of_digits = number_of_digits
        elif not (10 >= number_of_digits >= 1):
            raise ValueError('Wrong number of digits is given. '
                             'Following number should be more than 0 and less than 11.')
        elif self._active_game:
            raise AccessError("Can't change number of digits while game is started.")

    def set_number_of_guesses(self, number_of_guesses: int) -> None:
        if number_of_guesses > 0 and not self._active_game:
            self._number_of_guesses = number_of_guesses
        elif number_of_guesses < 0:
            raise ValueError(('Wrong number of guesses is given. '
                             'Following number should be more than 0.'))
        elif self._active_game:
            raise AccessError("Can't change number of guesses while game is started.")

    def _create_word(self) -> str:
        """creation of the secret word"""
        # randomizing the alphabet
        temp_shuffled_alphabet = list(self._alphabet)
        r.shuffle(temp_shuffled_alphabet)

        # taking first N letters from shuffled alphabet, so repetitive letters  are avoided
        word = "".join(temp_shuffled_alphabet[:self._number_of_digits])
        return word


def main():
    game = BagelsGame(3, 3)
    print(game.greeting())
    game.start_game()
    while game.get_game_state():
        print(game.user_guess(input(f"Guess #{game.get_current_guess()}\n>")))


if __name__ == "__main__":
    main()
