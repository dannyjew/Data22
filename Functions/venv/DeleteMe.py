user_inputted_word = input("Please choose a word for the oponent to guess...")
wrong_counter = 1
underscores = "_________________________________________"
hidden_word = underscores[0:len(user_inputted_word)]
print(hidden_word)

while wrong_counter <= 3:
    guessed_letter = input("Please guess a letter...")
    if guessed_letter in user_inputted_word:
        print("True")
    else:
        wrong_counter += 1


