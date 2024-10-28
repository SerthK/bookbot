def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_book_wordcount(text)
    
    print(f"{count} words were found in the document.")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_book_wordcount(text):
        return len(text.split())

main()