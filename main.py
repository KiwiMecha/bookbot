def get_book_text(book):
	with open(book) as read_book:
        	return read_book.read()

from stats import (num_words, char_count, sorted_num)

def main():
    output = get_book_text("books/frankenstein.txt")
    print(f"{num_words(output)} words found in the document")
    print(char_count(output))

main()
