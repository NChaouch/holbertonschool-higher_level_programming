#!/usr/bin/python3
"""
Function prints  a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with two new lines after each '.', '?', and ':'.

    Args:
        text: The text to be processed(str).

    Raises:
        TypeError: If `text` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = []
    space_ignore = False

    for punc in text:
        if punc in ['.', '?', ':']:
            result.append(punc)
            result.append("\n\n")
            space_ignore = True
        elif punc == " " and space_ignore:
            continue
        else:
            result.append(punc)
            space_ignore = False

    print("".join(result))
