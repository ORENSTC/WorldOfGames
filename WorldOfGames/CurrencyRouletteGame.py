from Live import getdifficulty
import random
import requests

difficultychoice = getdifficulty()

# This function is converting a random amount of USD to ILS, and showing the amount to the user


def get_money_interval():
    api_key = "aa8e277404734d35ab6782758ac8140e"
    url = f"https://openexchangerates.org/api/latest.json?app_id=aa8e277404734d35ab6782758ac8140e"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["rates"]
    available_currencies = ""
    amount = int([random.randint(1, 101)][0])
    for currency in exchange_rate.keys():
        available_currencies += currency + ", "
        available_currencies = available_currencies[:-2]
        from_currency = 'USD'
        to_currency = 'ILS'
        original_amount = amount / exchange_rate[from_currency]
        converted_amount = original_amount * exchange_rate[to_currency]
    # print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
    d = difficultychoice
    t = converted_amount
    money_interval = (t - (5 - d), t + (5 - d))
    print(original_amount)
    print(converted_amount)
    print(money_interval)
    return converted_amount, original_amount, money_interval


def get_guess_from_user(original_amount):
    guess_from_user = float(input(f"""if the original amount is {original_amount} USD, how much will it be after the 
    conversion to ILS?"""))
    return guess_from_user


def play(guess_from_user, money_interval):
    lower_limit_of_money_interval = money_interval[0]
    upper_limit_of_money_interval = money_interval[1]
    if guess_from_user < upper_limit_of_money_interval and guess_from_user > lower_limit_of_money_interval:
        print("Correct")
    else:
        print("Wrong!")


converted_amount, original_amount, money_interval = get_money_interval()
guess_from_user = get_guess_from_user(original_amount)
play(guess_from_user, money_interval)
