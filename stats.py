def count_words(text):
    words = text.split(" ")
    return len(words)


def count_characters(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char.isalpha():
            if char in char_count:
                
                char_count[char] += 1
            else:
                    char_count[char] = 1

    return char_count


# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def sort_dict(char_dict):
    return dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))