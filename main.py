from stats import chars_frequency, total_words, sort_dict
import sys


def get_book_text(path_to_file: str) -> str:
    """
    Reads the content of a file and returns it as a string.

    Args:
        path_to_file (str): The path to the book file.

    Returns:
        str: The content of the file.
    """
    with open(path_to_file, "r") as f:
        file_contents = f.read()
        return file_contents


def main():
    """
    Main function that executes the book analysis:
    - Reads the book file path from command-line arguments.
    - Validates the argument count.
    - Analyzes the book content for word and character frequency.
    - Displays the results.
    """

    # Ensure the script is run with a file path argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Extract file path from the command-line argument
    path_to_file = sys.argv[1]

    # Read and analyze the book content
    content = get_book_text(path_to_file)
    words = total_words(content)
    char_dict = chars_frequency(content)
    arr = sort_dict(char_dict)

    # Display the results
    print("\n============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")

    print("----------- Word Count ----------")
    print(f"Found {words} total words")

    print("--------- Character Count -------")
    for item in arr:
        # Only display single alphabetical characters
        if item["alphabet"].isalpha() and len(item["alphabet"]) == 1:
            print(f"{item['alphabet']}: {item['count']}")

    print("============= END ===============")


# Standard Python entry point to run the script
if __name__ == "__main__":
    main()
