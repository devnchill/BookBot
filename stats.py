import string


def get_num_words(file_contents):
    no_of_words = len(file_contents.split())
    return no_of_words


def count_char(file_contents):
    file_contents = file_contents.lower()
    d = dict.fromkeys(string.ascii_lowercase, 0)
    for char in file_contents:
        if char in d:
            d[char] += 1
        else:
            d[char] = 0
    return d
