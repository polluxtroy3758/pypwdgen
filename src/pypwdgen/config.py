#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contants used by pypwdgen"""

from string import ascii_lowercase, ascii_uppercase, digits

LOWERCASE = ascii_lowercase  #: Lowercase latin letters to build full set of characters
UPPERCASE = ascii_uppercase  #: Uppercase latin letters to build full set of characters
DIGITS = digits  #: Digits to build full set of characters
PUNCTUATION = ".,;:!?&-_@=+*/%<>#"  #: Punctuation marks to build full set of characters

#: Full set of characters that can be used in generated passwords
ALL_CHARACTERS = f"{LOWERCASE}{UPPERCASE}{DIGITS}{PUNCTUATION}"

#: Valid ranges and default parameters for password generation
PARAMETERS = {
        "length": {"MIN": 9, "MAX": 50, "DEFAULT": 9},
        "complexity": {"MIN": 3, "MAX": 4, "DEFAULT": 3},
        "number": {"MIN": 1, "MAX": 100, "DEFAULT": 1},
    }
