from stats import chars_frequency, total_words, sort_dict
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    content = get_book_text(path_to_file)
    words = total_words(content)
    char_dict = chars_frequency(content)
    arr = sort_dict(char_dict)

    print("\n============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in arr:
        if item["alphabet"].isalpha() and len(item["alphabet"]) == 1:
            print(f"{item['alphabet']}: {item['count']}")

    print("============= END ===============")


main()
