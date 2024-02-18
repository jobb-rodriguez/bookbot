def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_number_of_character_appearance(text):
    characters = {}
    for word in text:
        lowered_word = word.lower()
        for char in lowered_word:
            if(char not in characters):
                characters[char] = 1
            characters[char] += 1
    return characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = get_number_of_words(text)
    number_of_character_appearance = get_number_of_character_appearance(text)
    print(number_of_words)
    print(number_of_character_appearance)
    # print(text)

main()
