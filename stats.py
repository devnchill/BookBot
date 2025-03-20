import string
from operator import itemgetter
from typing import Dict, List


def total_words(file_contents: str) -> int:
    """
    Counts the total number of words in the given file content.

    Args:
        file_contents (str): The content of the book file as a string.

    Returns:
        int: The total word count.
    """
    no_of_words = len(file_contents.split())
    return no_of_words


def chars_frequency(file_contents: str) -> Dict[str, int]:
    """
    Counts the frequency of each lowercase alphabet character in the file content.

    Args:
        file_contents (str): The content of the book file as a string.

    Returns:
        Dict[str, int]: A dictionary mapping each lowercase letter to its frequency.
    """
    file_contents = file_contents.lower()

    # Initialize dictionary with lowercase alphabets and count set to 0
    d = dict.fromkeys(string.ascii_lowercase, 0)

    # Iterate through each character and count only alphabetical ones
    for char in file_contents:
        if char in d:
            d[char] += 1
    return d


def sort_dict(char_dict: Dict[str, int]) -> List[Dict[str, int]]:
    """
    Sorts the character frequency dictionary by the count in descending order.

    Args:
        char_dict (Dict[str, int]): Dictionary with character frequencies.

    Returns:
        List[Dict[str, int]]: A list of dictionaries with "alphabet" and "count" keys, sorted by count.
    """
    char_list = [
        {"alphabet": char, "count": count} for char, count in char_dict.items()
    ]

    # Sort the list by frequency in descending order
    char_list.sort(key=itemgetter("count"), reverse=True)
    return char_list
