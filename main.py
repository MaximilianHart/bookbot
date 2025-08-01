import sys
from stats import get_num_words, get_letters, sort_dict

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    get_num_words(sys.argv[1])
    get_letters(sys.argv[1])
    sort_dict()
    print("============= END ===============")


main()
