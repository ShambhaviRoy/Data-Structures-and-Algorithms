# Given a list of strings, return a list of 2 strings having the maximum Jaccard Index
# For any 2 strings, find Jaccard Index between lists of ngrams of both strings of length upto the length of the smaller string
# Jaccard index = Intersection / Union

# Example: Input strings 'abc' and 'abcd'
# 'abc' --> ['a', 'b', 'c', 'ab', 'bc', 'ac', 'abc']
# 'abcd' --> ['a', 'b', 'c', 'd', 'ab', 'bc', 'ac', 'ad', 'bd', 'abc', 'bcd']


def solution(words):
    jaccard = 0
    ans  = []
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            word1 = words[i]
            word2 = words[j]

            if word1 == '' or word2 == '':
                break
            else:
                result = calc_jaccard(word1, word2)
                if result > jaccard:
                    jaccard = result
                    ans = [word1, word2]
    return ans


def calc_jaccard(word1, word2):
    # method to calculate jaccard index of 2 strings
    jaccard = 0

    max_length = 0
    if len(word1) < len(word2):
        max_length = len(word1)
    else:
        max_length = len(word2)

    list1 = create_ngrams_list(word1, max_length)
    list2 = create_ngrams_list(word2, max_length)

    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    jaccard = float(intersection) / union

    return jaccard


def create_ngrams_list(word, max_length):
    # method to create ngrams list of a word
    ngrams_list = []
    n = len(word)

    for i in range(1, n):
        for j in range(n-i+1):
            ngram = word[j: j+i]
            if ngram != '':
                if ngram not in ngrams_list and len(ngram) <= max_length:
                    ngrams_list.append(ngram)

    return ngrams_list






if __name__ == '__main__':
    print('Enter length of words list:')
    n = int(input())

    words = []

    for _ in range(n):
        word = input()
        words.append(word)

    ans = solution(words)
    print(ans)