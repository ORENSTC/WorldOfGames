from Live import getdifficulty
import random


def guessgame():
    difficultychoice = getdifficulty()
    difficultychoice = int(difficultychoice)
    secret_number = random.randint(1, difficultychoice)
    get_guess_from_user = input("Guess what number the computer came up with: ")
    get_guess_from_user = int(get_guess_from_user)
    if secret_number == get_guess_from_user:
        print("True")
    else:
        print("False")


guessgame()
