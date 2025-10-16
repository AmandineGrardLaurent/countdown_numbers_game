#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# random chiffre à trouver entre 101 et 999
# random de 6 plaques
# total des plaques : ( 1 à 10 )x2 et (25, 50, 75, 100)
# à chaque tour, on choisit 2 chiffres dispos (plaques ou chiffre d'une précédente opé)
# à chaque tour, on choisit une opération entre les 2 chiffres

cards_list = [n for n in range(1, 11) for _ in range(2)] + [25, 50, 75, 100]

def generate_target_number():
    """
    Generate a random target number for the game.
    :return: int - A random integer between 101 and 999 (inclusive).
    """
    return random.randint(101, 999)

def draw_starting_cards(cards_list):
    """
    Randomly draw 6 unique cards from the given card list.
    :param cards_list: The full list of available cards.
    :return: list - A list of 6 randomly selected cards with no duplicates.
    """
    return random.sample(cards_list, 6)

def ask_operator():
    """
     Prompt the user to select a valid mathematical operator.

    :return: str - One of the four valid operators: '+', '-', '*', '/'
    """
    valid_operators = {"+", "-", "*", "/"}

    while True:
        operator = input("Quelle opération souhaitez-vous réaliser ? [ + , - , * , / ]\n").strip()
        if operator in valid_operators:
            return operator
        print("Entrée invalide. Merci de choisir une opération parmi [ + , - , * , / ].")

if __name__ == '__main__':

   ask_operator()