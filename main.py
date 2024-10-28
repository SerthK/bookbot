def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_book_wordcount(text)
    char_count = get_char_count(text)

    print(f"{count} words were found in the document.")
    print(char_count)

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

main()