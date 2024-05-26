# Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
# each other.

from collections import defaultdict

def group_anagrams(words):
    word_map = defaultdict(list)
    ans = []
    
    for word in words:
        sorted_word = sort_word(word)
        word_map[sorted_word].append(word)

    ans = [value for value in word_map.values()]
    return ans


def sort_word(word):
    word_list = sorted(word)
    return ''.join(word_list)

words = ['state', 'angel', 'acre', 'race', 'glean', 'care', 'taste']
print(group_anagrams(words))
