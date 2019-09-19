#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Sept 2019
# This is program circumference 

import constants

def main():
    # funciton calculates circumference

    # input
    circumference = float(input("What is radius:"))

    # process
    circumference = constants.TAU * circumference

    # output
    print("\nThe circumference is " + str(round(circumference, 2)) + " units.")


if __name__ == "__main__":
    main()
