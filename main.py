import sys
from stats import get_num_words, get_num_chars, get_sorted_chars


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return
    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    content = get_book_text(book_path)
    print("----------- Word Count ----------")
    word_count = get_num_words(content)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_dict = get_num_chars(content)
    sorted_chars = get_sorted_chars(char_dict)
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")


main()