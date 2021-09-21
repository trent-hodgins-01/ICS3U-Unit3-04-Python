# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 09/21/2021
# This is the Positive/ Negative/ 0
# The user enters in a number and the program tells the user if it's a positive, negative, or 0


def main():
    # this function checks to see what sign the integer is

    # input
    number = int(input("Enter in a number to see its sign (integer): "))
    print("")

    # process and output
    if number < 0:
        print("-")
    elif number > 0:
        print("+")
    else:
        print("0")

    print("\nDone")


if __name__ == "__main__":
    main()
