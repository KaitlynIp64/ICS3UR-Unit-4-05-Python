#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Nov 2022
# This program adds the user's numbers except negatives


def main():
    # this is a number guessing game
    loop_counter = 0
    answer = 0

    # input
    loop_number = input("Enter the amount of integers you want to add: ")

    # process
    try:
        int_loops = int(loop_number)
        while loop_counter < int_loops:
            user_string = input("Enter an integer: ")
            int_user = int(user_string)
            if int_user > 0:
                answer = answer + int_user
            else:
                loop_counter = loop_counter + 1
                continue
            loop_counter = loop_counter + 1
        print("The sum of all positive integers is: {0}.".format(answer))
    except ValueError:
        print("That is not a valid input.")
    # output

    print("\nDone.")


if __name__ == "__main__":
    main()
