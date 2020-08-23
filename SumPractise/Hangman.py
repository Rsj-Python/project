
import random

def hangman(word):
    wrong = 0
    stages = [
              "_________      ",
              "|              ",
              "|       |      ",
              "|       0      ",
              "|      /|\     ",
              "|      / \     ",
              "|              "]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False

    print("Welcome to Hangman")
    print('-' * 60)

    while wrong < len(stages):
        char = input("Guess a letter")
        if char in rletters:
            index = rletters.index(char)
            board[index] = char
            rletters[index] = "$"
        else:
            wrong += 1

        print(" ".join(board))
        print("\n".join(stages[0:wrong]))

        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages))
        print("You lose! It was {}.".format(word))

alist = ["welcome","book","apple","banana"]
hangman(random.choice(alist))






















