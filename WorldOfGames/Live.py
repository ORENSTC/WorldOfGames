

def welcome():
    name = input("What is your name?")
    print(f"Hello {name} and welcome to the World of Games (Wog). Here you can find many cool games to play.")


def getgamechoice():

    print("""Please choose a game to play:
    1. Memory Game - A sequence of numbers will appear for 1 second and you have to guess it back"
    2. Guess Game - Guess a number and see if you chose like the computer"
    3. Currency Roulette - Try and guess the value of a random amount of USD in ILS""")
    gamechoice = (input("What game would you like to play today?\n"))
    if gamechoice not in ["1", "2", "3"]:
        print("One of the games mentioned, if you will")
        gamechoice = getgamechoice()

    return(gamechoice)


def getdifficulty():
    difficultychoice = (input("Please choose a game difficulty ranging from 1 to 5:\n"))
    if difficultychoice not in ["1", "2", "3", "4", "5"]:
        print("Seriously, how hard do you want your game to be?")
        difficultychoice = getdifficulty()

    return int(difficultychoice)

# def play_games(gamechoice, difficultychoice):

# TODO: add difficulty level as argument
# TODO: add questions: Does the user want to play again? Does the user want to play a different game?