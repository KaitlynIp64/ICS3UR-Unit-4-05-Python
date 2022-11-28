#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Nov 2022
# This program adds the user's numbers except negatives


def main():
    # this function adds user numbers except negative numbers
    while True:
        # main function
        try:
            total_numbers = []
            # input
            amount_num = int(input("Input the amount of numbers you want to add: "))
            print()
            # process
            for addition in range(amount_num):
                amount_num = int(input("Enter a number: "))
                if amount_num < 0:
                    continue
                total_numbers.append(amount_num)
            # output
            print()
            print("The sum of all positive numbers is: ", sum(total_numbers))
        except ValueError:
            print("That is not a valid input.")
            continue
        # break out of loop
        else:
            break

    print("\nDone.")


if __name__ == "__main__":
    main()
