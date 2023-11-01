"""
This module contains various utility functions for string manipulation and analysis.

Author: Bruyère Gabriel
Date: 20/10/2023
"""


def nearest_value(values: set[int], one: int) -> int:
    """
    Find nearest value in the set 'values' to the integer 'one'.

    Args:
        values (set[int]): A set of integers.
        one (int): The target integer.

    Returns:
        int: The nearest value from the set to 'one'.
    """
    closest_value = None

    min_distance = float("inf")

    for value in values:
        distance = abs(value - one)
        if distance < min_distance or (
            distance == min_distance and value < closest_value
        ):
            closest_value = value
            min_distance = distance

    return closest_value


def first_word(text: str) -> str:
    """
    Extract the first word from a given text.

    Args:
        text (str): The input text.

    Returns:
        str: The first word from the input text.
    """
    words = text.split()
    if words:

        return words[0]
    return ""


def split_pairs(text: str):
    """
    Split the input text into pairs of characters.

    Args:
        text (str): The input text.

    Yields:
        str: Pairs of characters from the input text.
    """
    if len(text) % 2 == 1:
        
        text += "_"
    for i in range(0, len(text), 2):
        yield text[i : i + 2]


def correct_sentence(text: str) -> str:
    """
    Correct a sentence by ensuring it starts with a capital letter and ends with a period.

    Args:
        text (str): The input sentence.

    Returns:
        str: The corrected sentence.
    """
    if not text[0].isupper():
        text = text[0].upper() + text[1:]
    if not text.endswith("."):
        text += "."
    return text


def beginning_zeros(a: str) -> int:
    """
    Count the number of leading zeros in a string.

    Args:
        a (str): The input string.

    Returns:
        int: The count of leading zeros.
    """
    count = 0
    for digit in a:
        if digit == "0":
            count += 1
        else:
            break
    return count


def between_markers(text: str, start: str, end: str) -> str:
    """
    Extract a substring between two markers within the input text.

    Args:
        text (str): The input text.
        start (str): The starting marker.
        end (str): The ending marker.

    Returns:
        str: The substring between the markers (excluding the markers themselves).
    """
    start_index = text.find(start)
    end_index = text.rfind(end)
    if start_index != -1 and end_index != -1:
        return text[start_index + 1 : end_index]
    return ""


def checkio(data: list[int]):
    """
    Find and return a list of non-unique elements in the input list 'data'.

    Args:
        data (list[int]): A list of integers.

    Returns:
        list[int]: A list of non-unique elements.
    """
    element_count = {}
    non_unique_elements = []
    for element in data:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    for element in data:
        if element_count[element] > 1:
            non_unique_elements.append(element)
    return non_unique_elements


def backward_string_by_word(text: str) -> str:
    """
    Reverse words in the input text while keeping the word order.

    Args:
        text (str): The input text.

    Returns:
        str: The reversed text.
    """
    words = text.split(" ")
    reversed_words = [word[::-1] for word in words]
    reversed_text = " ".join(reversed_words)
    return reversed_text
