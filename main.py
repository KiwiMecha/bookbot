import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book):
	with open(book) as read_book:
        	return read_book.read()

from stats import (num_words, char_count, sorted_num)

def main():
    output = get_book_text("books/frankenstein.txt")
    print(f"Found {num_words(output)} total words")
    sorted_chars = (sorted_num(char_count(output)))
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

main()
