print("Welcome to Hangman: Your Worst Nightmare")
word = input("Player 1, please choose a wonderful word: ")
guesses = ''
turns = 12
while turns > 0:
    guess = input("Player 2, Guess a character: ")
    guesses += guess
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You won")
        break
    if guess not in word:
        turns -= 1
        print("Wrong")
        print(f"You have {turns} more guesses")
    if turns == 0:
        print("You Lose... time for the eternal slumber")