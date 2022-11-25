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
            number = int(input("Input the amount of numbers you want to add: "))
            print()

            # process
            for addition in range(number):
                numbers = int(input("Enter a number: "))

                if numbers < 0:
                    continue

                total_numbers.append(numbers)

            # output
            print()
            print("The sum of all positive numbers is: ", sum(total_numbers))

        except ValueError:
            print("Invalid Input")
            continue

        # break out of loop
        else:
            break


if __name__ == "__main__":
    main()
