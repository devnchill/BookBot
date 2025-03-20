import string
from operator import itemgetter


def total_words(file_contents):
    no_of_words = len(file_contents.split())
    return no_of_words


def chars_frequency(file_contents):
    file_contents = file_contents.lower()
    d = dict.fromkeys(string.ascii_lowercase, 0)
    for char in file_contents:
        if char in d:
            d[char] += 1
        else:
            d[char] = 0
    return d


def sort_dict(dict):
    char_list = []
    for char, count in dict.items():
        char_list.append({"alphabet": char, "count": count})
    char_list.sort(key=itemgetter("count"), reverse=True)
    return char_list
