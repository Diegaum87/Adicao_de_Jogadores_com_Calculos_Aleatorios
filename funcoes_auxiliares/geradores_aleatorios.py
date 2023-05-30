from random import randint, choice
from string import ascii_lowercase


def gerador_de_numero():
    numero = randint(1,10)
    return f' O número gerado foi {numero}'

def gerador_de_letra():
    return choice(ascii_lowercase)