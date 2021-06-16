#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Functions and classes specific for password generation."""

from random import sample
from secrets import choice

from .config import *


class Password:
    """Complex password generated from given length and complexity."""

    def __init__(
            self,
            given_length: int = PARAMETERS["length"]["DEFAULT"],
            given_complexity: int = PARAMETERS["complexity"]["DEFAULT"]
    ) -> None:
        """Generate a password from given length and complexity.

        :param int given_length: length of the generated password
        :param int given_complexity: MINIMAL complexity of the generated password
        """
        for param_name, param in {"length": given_length, "complexity": given_complexity}.items():
            _validate_parameter(param, param_name)

        self._given_length = given_length
        self._given_complexity = given_complexity

        self._characters = sample(ALL_CHARACTERS, len(ALL_CHARACTERS))

        self._complexity = -1
        self._password = self._generate_password()

        # Delete characters as they are not meant to be stored
        del self._characters

    def __str__(self):
        return self._password

    def __repr__(self):
        return f"Password: {self._password}\tComplexity: {self._complexity}"

    @property
    def password(self) -> str:
        """Generated password.

        :return: the generated password
        :rtype: str
        """
        return self._password

    @property
    def complexity(self) -> int:
        """Complexity score.

        :return: the complexity score of the generated password
        :rtype: int
        """
        return self._complexity

    def _generate_password(self) -> str:
        """Generate a password following the given parameters.

        :return: a valid password
        :rtype: str
        """
        password = ""
        while True:
            password += choice(self._characters)
            if len(password) == self._given_length:
                complexity = _calculate_complexity(password)
                if complexity >= self._given_complexity:
                    self._complexity = complexity
                    return password
                else:
                    password = ""


def _validate_parameter(param: int, param_name: str) -> None:
    """Checks if the given parameters are in a valid range.

    :param int param: the value of the parameter to validate
    :param str param_name: the name of the parameter to validate
    :raises KeyError: if the parameter name does not exists
    :raises ValueError: if the parameter is not in correct predefined range
    """
    if param_name not in PARAMETERS.keys():
        raise KeyError(f"The '{param_name}' parameter does not exists."
                       f"Accepted parameter names are: {PARAMETERS.keys()}")

    if param < PARAMETERS[param_name]["MIN"] or param > PARAMETERS[param_name]["MAX"]:
        raise ValueError(f"The given {param_name} can't be less than {PARAMETERS[param_name]['MIN']} "
                         f"or greater than {PARAMETERS[param_name]['MAX']}.\n"
                         f"Given length: {param}")


def _calculate_complexity(password: str) -> int:
    """Calculate a 'complexity score' based on the numbers of different character classes in the password.

    Presence of the characters types a tested :

        - LOWERCASE
        - UPPERCASE
        - DIGITS
        - PUNCTUATION

    For each character class, checks the presence of at least one character in the password, and store the result as
    a boolean.

    The complexity score is the sum of these booleans (True = 1 and False = 0).

    :param str password: the password from which to calculate the complexity
    :return: the complexity score
    :rtype: int
    """
    score = []
    for char_class in (LOWERCASE, UPPERCASE, DIGITS, PUNCTUATION):
        score.append(any(char in password for char in char_class))
    return sum(score)
