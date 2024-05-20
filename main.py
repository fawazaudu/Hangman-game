from random import choice

def read_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file.readlines()]
        return words
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []




def run_game():
    words = read_words_from_file('words.txt')

    if not words:
        print("No words found in the file. Using default list.")
        words = ['jungle', 'choice', 'plastic', 'biscuit', 'brisket', 'tomato']

        # Prompt players to enter their names
    player1 = input('Player 1, enter your name: ')
    player2 = input('Player 2, enter your name: ')

    # Initialize scores for both players
    player_scores = {player1: 0, player2: 0}



    print("Welcome to hangman:)\nThe goal of this game is to guess random words by typing in letters\nThe first player to 3 correct guesses is the winner")

    while True:
        for player in [player1, player2]:
            guessed: str = ''
            print(f"\n{player}, it's your turn.")
            tries=5
            word = choice(words)
        # The game
            while tries > 0:
                blanks: int = 0

                print('Word: ', end='')
                for char in word:
                    if char in guessed:
                        print(char, end='')
                    else:
                        print('_', end='')
                        blanks += 1

                print()  # Add a blank line

            # If there are no blanks left, that means the user won the game!
                if blanks == 0:
                    print(f'Congratulations, {player}! You got it!')
                    player_scores[player] += 1
                    break

            # Get user input
            # Get user input
                guess = input('Enter a letter: ')

            # Validate the user input
                if len(guess) != 1 or not guess.isalpha():
                    print('Please enter a single alphabetical character.')
                    continue

            # Check that the user isn't just guessing the same letter again
                if guess in guessed:
                    print(f'You already used: "{guess}". Please try with another letter!')
                    continue

            # Add the guess to the guessed string
                guessed += guess

            # Check that the guess is in the word
                if guess not in word:
                    tries -= 1
                    print(f'Sorry, that was wrong... ({tries} tries remaining)')

                # Game-over if tries reaches 0
                if tries == 0:
                    print('No more tries remaining... You lose.')
                    print(f'The word was: {word}')
                    break


        for player, score in player_scores.items():
            if score >= 3:
                print(f'\nCongratulations, {player}! You are the winner!')
                return


if __name__ == '__main__':
    run_game()