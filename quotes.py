import random

quotes = [
    "I am hungry",
    "*$*#*@",
    "Kill me please",
    "What a pussy"
]

def get_quote():
    return quotes[random.randint(0, len(quotes) - 1)]
