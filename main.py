def main():
    book_path = 'books/frankenstein.txt'
    file_contents = read_text(book_path)
    word_count = count_words(file_contents)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    letter_count = count_chars(file_contents)
    for letter in letter_count:
        print(f"The '{letter}' character was found {letter_count[letter]} times")
    print("--- End report ---")

def read_text(file_loc):
    with open(file_loc) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    lowered_string = text.lower()
    dictionary = {}
    for letter in set(lowered_string):
        if (letter != '\n') and (letter != ' ') and (letter != '.') and (letter != '#') and (letter != '-') and (letter != '"') and (letter != '!'):
            dictionary[letter] = lowered_string.count(letter)
    return dictionary

main()