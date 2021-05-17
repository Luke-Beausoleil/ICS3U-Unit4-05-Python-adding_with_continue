#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program adds inputted numbers using a continue statement


def main():
    # this functoin adds the numbers

    # variables
    loop_counter = 0
    lst = []

    # input
    times_to_add_as_string = input(
          "How many numbers would you like to add together? ")

    # process
    try:
        times_to_add = int(times_to_add_as_string)
        if times_to_add > 0:
            while loop_counter < times_to_add:
                user_input = input("Enter a number you wish to add: ")
                try:
                    number = float(user_input)
                    if number > 0:
                        for loop_counter in range(times_to_add + 1):
                            if loop_counter < number:
                                loop_counter = loop_counter + 1
                                total = sum(lst.append(number))
                            else:
                                continue
                    else:
                        continue
                except (Exception):
                    continue
            print("\nThe sum of the positive numbers is {0}".format(total))
        elif times_to_add < 0:
            print("\nUnable to add that many numbers")
        else:
            print("\nThe sum of zero numbers is 0")
    except (Exception):
        print("\nUnable to add that many numbers")
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
