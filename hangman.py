# Matthew Sperry

import random
import re



words = ['like', 'funny', 'secrets', 'kibble', 'lionize', 'taxi', 'antidisestablishmentarianism',
'pie', 'keyboard', 'great']

# Draw gallows and person being hanged
gallows6 = '_____\n     |\n     |\n     |\n  ______'
gallows5 = '_____\n  O  |\n     |\n     |\n  ______'
gallows4 = '_____\n  O  |\n  |  |\n     |\n  ______'
gallows3 = '_____\n  O  |\n  |\ |\n     |\n  ______'
gallows2 = '_____\n  O  |\n /|\ |\n     |\n  ______'
gallows1 = '_____\n  O  |\n /|\ |\n /   |\n  ______'
gallows0 = '_____\n  O  |\n /|\ |\n / \ |\n  ______'
gallows = [gallows0, gallows1, gallows2, gallows3, gallows4, gallows5, gallows6]

# game loop
play = 'Y'

while play == 'Y':
    wrongGuess = 6
    correctGuess = 0
    wGuessedLetters = []
    cGuessedLetters = []
    # Select 1 of 10 random words from a list to be used in a hang man game
    secretWord = random.choice(words)

    # Show how many letter are in the word
    guessWord = '_' * len(secretWord)
    print(f'Guess the word: {guessWord}')
    while secretWord != guessWord:
        # loop ending messages
        if wrongGuess == 0:
            print("You took too many guesses!")
            print(f'the word was {secretWord}')
            break
        # guessed letter
        guess = input('Guess a letter: ').lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in wGuessedLetters or guess in cGuessedLetters:
                print(f'You already guessed {guess}')

            elif guess not in wGuessedLetters and guess not in cGuessedLetters and guess not in secretWord:
                # If not in word decrease guess amount
                wrongGuess -= 1
                print(f'\n{guess} is not in the word, you have {wrongGuess} guesses left')
                wGuessedLetters.append(guess)
                print(f'incorrect guesses: {wGuessedLetters}')
                print(guessWord)

            elif guess not in wGuessedLetters and guess not in cGuessedLetters and guess in secretWord:
                cGuessedLetters.append(guess)
                correctGuess += 1
                print(f'\n{guess} is in the word! You have {wrongGuess} guesses left')

                # Show the letter in correct position if correctly guessed
                # Find all indices of "guess"
                indices_object = re.finditer(pattern=guess, string=secretWord)
                pos = [index.start() for index in indices_object] # gets indices of letter

                # pos = guessWord.find(guess)
                for i in range(len(pos)):
                    guessWord = guessWord[:pos[i]] + guess + guessWord[(pos[i] + 1):]
                print(guessWord)
            # Display # of guesses (correct/incorrect)
            print(gallows[wrongGuess])
            print(f'\nYou have correctly guessed {correctGuess} letters and incorrectly guessed {len(wGuessedLetters)} letters')
            if secretWord == guessWord:
                print(f'\nCorrect! You used {6 - wrongGuess} Guesses') # display "Correct!" 
                print(f'\n\nThe word was {secretWord}') # show # of guesses it took
        else:
            print('Invalid guess, must be a single letter')
    # Ask if the user wants to play again
    play = input('Would you like to play again?(y/n) ').upper()
# if no display thanks for playing
print('Thanks for Playing!')

