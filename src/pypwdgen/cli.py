#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Password generator"""

from typing import List

from .config import *
from .core import Password, _validate_parameter

PassList = List[Password]


def _generate_password_list(
        given_number: int = PARAMETERS["number"]["DEFAULT"],
        given_length: int = PARAMETERS["length"]["DEFAULT"],
        given_complexity: int = PARAMETERS["complexity"]["DEFAULT"]
) -> PassList:
    """Generate a given number of passwords.

    :param int given_number: the number of passwords to generate
    :param int given_length: the length of passwords to generate
    :param int given_complexity: the complexity of passwords to generate
    :return: the generated passwords
    :rtype: PassList
    :raises ValuError: if any parameter is not valid
    """
    _validate_parameter(given_number, "number")
    password_list = []
    for i in range(given_number):
        password_list.append(Password(given_length, given_complexity))
    return password_list


def _print_passwords(password_list: PassList) -> None:
    """Prints the generated password(s).

    :param Passlist password_list: the list of password to be printed
    """
    for password in password_list:
        print(password)


def _parse_arguments() -> dict:
    """Parse the cli arguments with argparse

    :return: a dictionnary containing the arguments
    :rtype: dict
    """
    import argparse

    parser = argparse.ArgumentParser(prog="pypwdgen", description="Complex password generator")
    parser.add_argument(
        '-l',
        '--length',
        type=int,
        default=PARAMETERS["length"]["DEFAULT"],
        choices=range(PARAMETERS["length"]["MIN"], PARAMETERS["length"]["MAX"] + 1),
        help=f"Password length (default : {PARAMETERS['length']['DEFAULT']})",
    )
    parser.add_argument(
        '-n',
        '--number',
        type=int,
        default=PARAMETERS["number"]["DEFAULT"],
        choices=range(PARAMETERS["number"]["MIN"], PARAMETERS["number"]["MAX"] + 1),
        help=f"Number of passwords (defaut : {PARAMETERS['number']['DEFAULT']})",
    )
    parser.add_argument(
        '-c',
        '--complexity',
        type=int,
        default=PARAMETERS["complexity"]["DEFAULT"],
        choices=range(PARAMETERS["complexity"]["MIN"], PARAMETERS["complexity"]["MAX"] + 1),
        help=f"Minimum number of character classes to use (default : {PARAMETERS['complexity']['DEFAULT']})",
    )
    args = parser.parse_args()
    return {"number": args.number, "length": args.length, "complexity": args.complexity}


def main() -> None:
    """Main function

    Called when the module is run directly.
    """
    args = _parse_arguments()
    password_list = _generate_password_list(args["number"], args["length"], args["complexity"])
    _print_passwords(password_list)


if __name__ == '__main__':
    import sys

    sys.exit(main())
