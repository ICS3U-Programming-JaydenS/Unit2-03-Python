#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: March 4, 2025
# This programs calculates the cost of a pizza.

import constants


def main():
    # Asks for user input for the diameter of pizza.
    pizza_diameter = int(input("Please enter the diameter of your Pizza! (in)"))
    # Calculates subtotal, tax and total.
    subtotal = (
        (pizza_diameter * constants.INGRED_COST)
        + constants.LABOUR_COST
        + constants.RENTAL_COST
    )
    tax = constants.HST * subtotal
    total = subtotal + tax
    # displays total rounded 2 decimals.
    print("The Cost of your Pizza is ${:.2f}".format(total))


if __name__ == "__main__":
    main()
