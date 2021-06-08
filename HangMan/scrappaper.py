def reveal_letter(letter_picked, word_to_guess, hidden_word):
    counter = 0
    hidden_word_list = list(hidden_word)

    for letter in word_to_guess:
        if letter == letter_picked:
            hidden_word_list[counter] = letter_picked
        counter += 1
    return ''.join(hidden_word_list)

print(reveal_letter("h","hello","_____"))




