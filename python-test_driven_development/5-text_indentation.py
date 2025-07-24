#!/usr/bin/python3
"""
5-text_indentation module
Defines a function that prints a text with two new lines
after each of these characters: '.', '?' and ':'
"""


def text_indentation(text):
    """
    Prints text with two new lines after each occurrence of '.', '?' or ':'.
    Arguments:
        text (str): The input text to process.
    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove leading/trailing spaces (but preserve newlines)
    text = text.strip(' ')
    # Collapse any spaces immediately before punctuation
    for punct in ".?:":
        while " " + punct in text:
            text = text.replace(" " + punct, punct)

    i = 0
    length = len(text)
    result = ""

    while i < length:
        ch = text[i]
        result += ch
        if ch in ".?:":
            # after punctuation, add two newlines
            result += "\n\n"
            # skip any spaces immediately following the punctuation
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1

    # Print result without adding any extra newline at the end
    print(result, end="")
