from Live import getdifficulty
from time import sleep
import random
import os
generate_sequence = None
numbers_from_user = None

difficultychoice = getdifficulty()


# generate random numbers, as many as the difficulty, and show them to the user
def generate(difficultychoice):
    generate_sequence = random.sample(range(1, 101), difficultychoice)
    print(generate_sequence)
    sleep(0.7)
    os.system("cls")
    return(generate_sequence)


# Have the user input the numbers shown, and make sure they work within the game. then make a list out of them
def get_list_from_user(difficultychoice):
    list_of_numbers_from_user = []
    for x in range(0, difficultychoice):
        numbers_from_user = input("What numbers did you see? One at a time, please")
        numbers_from_user = int(numbers_from_user)
        list_of_numbers_from_user.append(numbers_from_user)
    return(list_of_numbers_from_user)


def is_list_equal(generate_sequence, list_of_numbers_from_user):
    if list_of_numbers_from_user == generate_sequence:
        print("Correct!")
    else:
        print("Wrong!")


generate_sequence = generate(difficultychoice)
list_of_numbers_from_user = get_list_from_user(difficultychoice)
is_list_equal(generate_sequence, list_of_numbers_from_user)
