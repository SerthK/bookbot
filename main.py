def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_book_wordcount(text)
    char_count = get_char_count(text)

    print(f"{count} words were found in the document.\n")
    sorted_char_count = sort_char_count(char_count)
    for char in sorted_char_count:
        print(f"The {char[0]} character was found {char[1]} times.")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_book_wordcount(text):
        return len(text.split())

def get_char_count(text):
    chars = {}
    for character in text:
        if character.lower() in chars:
            chars[character.lower()] += 1
        else:
            chars[character.lower()] = 1
    return chars

def sort_char_count(dict):
    return sorted(filter(lambda x: x[0].isalpha() == True, dict.items()), key=lambda y: y[1], reverse=True)

main()