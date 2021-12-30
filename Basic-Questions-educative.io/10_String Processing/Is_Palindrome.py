# A palindrome is a word, number, phrase, or any other sequence of characters that reads the same forward as it does backward.

s = "Malayalam"

s = ''.join([i for i in s if i.isalnum()]).replace(" ", "").lower()
print (s == s[::-1])

def is_palindrome(s):
    s_rev = ""
    for ch in reversed(s):
        s_rev += ch
    return (s == s_rev)

print(is_palindrome(s))