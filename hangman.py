import random
import string
import words


def hangman():
    # accessing the word from word list and choosing a random one
    word = random.choice(words.words_list).upper()
    # a list for keeping track of what letters the user has guessed and using it for displaying the guessed letters
    guessed = []
    lives = 6

    # this is the first line and all the letters will be blank so the user can see how many letters are in the word
    for letter in word:
        print("_", end=' ')
    print()

    while lives > 0:
        user_letter = input(">").upper()

        # in case that the user input is not a letter (could be symbols or numbers and...)
        if user_letter not in string.ascii_letters:
            print("wrong input")
        elif user_letter not in word:
            lives -= 1
        elif user_letter in word and user_letter in guessed:
            print("you've already guessed that!")
        for letter in word:
            if letter == user_letter:
                guessed.append(letter)

        # this is the displaying part, and it shows the letter or _ based on what is guessed and what is not
        for i in word:
            if i in set(guessed):
                print(i, end=' ')
            else:
                print("_", end=' ')
        print()
        print()

        # won or lost
        if lives == 0:
            print(f"you lost\nThe word was \033[1;34;40m{word.upper()}", end='')

        if len(set(word)) == len(set(guessed)):
            print(f"you won!\nThe word was \033[1;34;40m{word.upper()}", end='')
            break


hangman()
