from stats import count_words
import sys

def main():
    book_path = sys.argv[1]
    file_contents = read_text(book_path)
    word_count = count_words(file_contents)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    letter_count = count_chars(file_contents)
    for letter in letter_count:
        print(f"{letter}: {letter_count[letter]}")
    print("--- End report ---")

def read_text(file_loc):
    with open(file_loc) as f:
        return f.read()

def count_chars(text):
    lowered_string = text.lower()
    dictionary = {}
    for letter in set(lowered_string):
        if (letter != '\n') and (letter != ' ') and (letter != '.') and (letter != '#') and (letter != '-') and (letter != '"') and (letter != '!'):
            dictionary[letter] = lowered_string.count(letter)
    return dictionary

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()