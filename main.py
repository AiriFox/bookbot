from stats import get_num_words
from stats import get_char_count
from stats import get_sorted_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(book_text)
    char_count = get_char_count(book_text)
    sorted_count = get_sorted_chars(char_count)
    print(f"""============ BOOKBOT ============
Analyzing book...
----------- Word Count ----------
Found {word_count} total words!
--------- Character Count -------
{sorted_count}""")

main()