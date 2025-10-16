#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, operator


operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

cards_list = [n for n in range(1, 11) for _ in range(2)] + [25, 50, 75, 100]

def generate_target_number():
    """
    Generate a random target number for the game.

    :return: int - A random integer between 101 and 999 (inclusive).
    """
    return random.randint(101, 999)


def draw_starting_cards():
    """
    Randomly draw 6 unique cards from the given card list.

    :return: list - A list of 6 randomly selected cards with no duplicates.
    """
    return random.sample(cards_list, 6)


def ask_number(available_numbers):
    """
    Ask the user to select a valid number from the list of available numbers.

    :param available_numbers: list of int - The numbers the user can currently choose from.
    :return: int - A number chosen by the user that exists in the available list.
    """
    print("Choisissez un chiffre parmi les suivants :", ", ".join(str(n) for n in available_numbers))

    valid_nb = False
    nb = None
    while not valid_nb:
        user_number = input().strip()
        if user_number.isdigit():
            nb = int(user_number)
            valid_nb = (nb in available_numbers)
            if not valid_nb:
                print(f"Choisissez un nombre parmi ceux proposés")
        else:
            print(f"Choisissez un nombre parmi ceux proposés")
    return nb


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


def calculator(nb_1, nb_2, operator_symbol):
    """
    Performs a basic arithmetic operation between two numbers based on the provided operator.

    :param nb_1: int or float - The first operand.
    :param nb_2: int or float - The second operand.
    :param operator: str - A string representing the operator. One of '+', '-', '*', '/'.
    :return: The result of applying the operator to the two numbers.
    """
    return operators[operator_symbol](nb_1, nb_2)


if __name__ == '__main__':

    available_numbers = draw_starting_cards()

    operator = ask_operator()
    nb_1 = ask_number(available_numbers)
    available_numbers.remove(nb_1)
    nb_2 = ask_number(available_numbers)
    operation = calculator(nb_1, nb_2, operator)
    print(operation)

