def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def num_words(file_contents):
    no_of_words = len(file_contents.split())
    return no_of_words


def main():
    file_content = get_book_text("./books/frankenstein.txt")
    # print(file_content)
    print(f"{num_words(file_content)} words found in the document")


main()
