from stats import count_char, get_num_words


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    file_content = get_book_text("./books/frankenstein.txt")
    print(f"{get_num_words(file_content)} words found in the document")
    print(f"{count_char(file_content)}")


main()
