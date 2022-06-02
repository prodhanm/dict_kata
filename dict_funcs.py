import sys

gaming_console = {
    "XBox" : 499.00,
    "Playstation 5" : 450.00,
    "Switch" : 299.00,
    "Quest" : 150.00
}

def price_update(gaming_console):
    try:
        increase = 1.11
        for game, price in gaming_console.items():
            gaming_console[game] = round(price*increase, 2)
        print(gaming_console)
    except Exception:
        print(f"The {sys.exc_info()[0]} exception occured.")

price_update(gaming_console)

try:
    for game, price in gaming_console.items():
        print(f"The {game} with another controller is ${price}.")
except Exception:
    print("The variable must be inserted in this statement.")

