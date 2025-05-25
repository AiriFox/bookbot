import sys
from stats import get_num_words
from stats import get_char_count
from stats import get_sorted_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:

    def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

    def main():
        book_text = get_book_text(sys.argv[1])
        book_title = sys.argv[1]
        word_count = get_num_words(book_text)
        char_count = get_char_count(book_text)
        sorted_count = get_sorted_chars(char_count)
        print(f"""============ BOOKBOT ============
Analyzing {book_title}...
----------- Word Count ----------
Found {word_count} total words!
--------- Character Count -------""")
        for char, count in sorted_count:
            print(f"{char}: {count}")

main()