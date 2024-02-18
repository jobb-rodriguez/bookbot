def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_chars_count(text):
    characters = {}
    for word in text:
        lowered_word = word.lower()
        for char in lowered_word:
            if(char not in characters):
                characters[char] = 1
            characters[char] += 1
    return characters
def sort_on(dict):
    return dict["count"]

def print_report(path, word_count, chars_count):
    print(f"-- -Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()
    
    cleaned_chars_count = []
    for char, count in chars_count.items():
        cleaned_chars_count.append({"name": char, "count": count})
    cleaned_chars_count.sort(reverse=True, key=sort_on)
    
    for char in cleaned_chars_count:
       print("The '{}' character was found {} times".format(char["name"], char["count"]))
    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    chars_count = get_chars_count(text)

    print(word_count)
    print(chars_count)
    print_report(book_path, word_count, chars_count)

main()
