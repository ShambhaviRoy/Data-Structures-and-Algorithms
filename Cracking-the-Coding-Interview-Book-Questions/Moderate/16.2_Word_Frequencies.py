# Word Frequencies: Design a method to find the frequency of occurrences of any given word in a
# book. What if we were running this algorithm multiple times?


def setup_dictionary(book):
    book_dict = {}
    for word in book:
        if word not in book_dict:
            book_dict[word] = 1
        else:
            book_dict[word] += 1
    return book_dict


def find_word_frequency(book_dict, word):
    if word.lower() in book_dict:
        return book_dict[word]
    else:
        return 0
    

book = ["Hello", "How", "are", "you?"]
book = [b.lower() for b in book]
book_dict = setup_dictionary(book)
print(find_word_frequency(book_dict, "hello"))