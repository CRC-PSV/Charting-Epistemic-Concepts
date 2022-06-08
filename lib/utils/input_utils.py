"""Util functions to manage command line inputs"""
from typing import Sequence


def read_validate_input(prompt: str, values: Sequence[str], success_msg: str = None, error_msg: str = None, to_lower: bool = True):
    """Prompts for an input based on a list of accepted values. Loops until a valid value is entered.

    Args:
        prompt: Prompt message to display, directly passed to input().
        values: A list (or list-like object) of accepted input values.
        success_msg: Message to print after a valid input is entered. Leaving it as None will not print anything, passing an empty string will print a blank line.
        error_msg: Message to print after an invalid input is entered. Leaving it as None will not print anything, passing an empty string will print a blank line.
        to_lower: Whether to call .lower() on the input before comparing it to values.

    Returns:
        The first valid value entered. Will be transformed to lowercase if to_lower is set to True.
    """

    while True:
        s = input(prompt).lower() if to_lower else input(prompt)
        if s in values:
            if success_msg is not None:
                print(success_msg)
            return s
        else:
            if error_msg is not None:
                print(error_msg)


def read_y_n_input(prompt: str = 'Continue? (y/n): ') -> bool:
    """Asks for a y/n input and wait for a valid input

    Accepts 'y', 'n', 'yes', 'no', case insensitive.

    Args:
        prompt: The prompt message to display

    Returns:
        The boolean corresponding to the input value
    """

    s = read_validate_input(prompt, ['y', 'n', 'yes', 'no'])

    return s[0] == 'y'


