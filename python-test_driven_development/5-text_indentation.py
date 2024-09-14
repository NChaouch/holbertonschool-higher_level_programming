#!/usr/bin/python3

"""
This contains the tex_indentation function
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

    punc = {'.', '?', ':'}
    text = text.strip()  # remove white spaces at the start and end of str

    ct = 0
    leng = len(text)
    while ct < leng:
        print(text[ct], end="")

        if text[ct] in punc:
            print("\n")
            ct += 1
            while ct < leng and text[ct] == " ":
                ct += 1
            continue

        ct += 1
