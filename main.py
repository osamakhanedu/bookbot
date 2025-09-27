import sys
from stats import count_words, count_characters, sort_dict


def get_book_text(file_path):
    with open(file_path) as f: 
        file_content = f.read()
    
    return file_content



def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Sort characters by count (descending) then alphabetically
    sorted_chars = sort_dict(char_count);

    for key in sorted_chars: 
        print(f"{key}: {sorted_chars[key]}")


    print("============= END ===============")

# Entry point for the script how it work? 
if __name__ == "__main__":
    main()