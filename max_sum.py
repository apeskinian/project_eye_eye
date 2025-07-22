"""
- Matthew Aitken
- 2i Testing Coding Challenge
- 22nd July 2025

- Task:
    Given an array of strings, each made up of a combination of letters and
    digits, write the functionality to find and return the largest sum of
    digits within a string.

    Considering a variety of different input arrays, state any assumptions or
    design choices you had to make.

    Notes:
    - Each digit should be considered its own 1-digit number i.e. in the third
    string below 36 is evaluated as 3 and 6 separately.
    - The input arrays can vary in length; however, they will not be larger
    than 10 strings.
    - Strings can vary in length; however, they will not be larger than 12
    characters.

    Example:
    Input - ["dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw"]
    Sums - 11, 4, 10, 13
    Output - 13
"""
import re


def sum_of_list(list):
    """
    Filters out given list of strings and returns a list of the sums of single
    numbers found in each string.

    **Assumptions**
    That the input array is always a valid array.
    """
    # create new blank list to return
    new_list = []
    # iterate through list and append sum of each filtered list to `new_list``
    for item in list:
        just_numbers = ''.join(re.findall(r'\d', item))
        sum_of_numbers = 0
        for char in just_numbers:
            sum_of_numbers += int(char)
        new_list.append(sum_of_numbers)
    # return list of sums
    return new_list


def find_largest(list):
    """
    Returns the largest from a given list of numbers.
    """
    largest = max(list)

    return largest


def main():
    """
    Main entry point of program.
    """
    # send list to get the sums
    sums = (sum_of_list(["dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw"]))
    # deduce largest from new sums list
    output = find_largest(sums)

    print(output)
    # return largest sum from input list
    return output


if __name__ == "__main__":
    main()
