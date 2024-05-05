# Permutations without Dups: Write a method to compute all permutations of a string of unique
# characters.


def get_permutations(s):
    permutations = []
    if len(s) <= 1:
        permutations.append(s[-1])
        return permutations
     
    
    char = s[0]
    remaining = s[1:]
    print(char, remaining)

    words = get_permutations(remaining)
    print(words)
    
    for word in words:
        for i in range(len(word)+1):
            new_word = insert_char_at(word, char, i)
            permutations.append(new_word)
    
    return permutations


def insert_char_at(word, char, i):
    start = word[:i]
    end = word[i:]
    new_word = start + char + end
    return new_word


s = 'abc'
print(get_permutations(s))