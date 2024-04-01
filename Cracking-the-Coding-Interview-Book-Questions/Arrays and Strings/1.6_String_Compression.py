# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

# Time Complexity = O(n), Space Complexity = O(n), n = len(original)
def compression(original):
    compressed = ""
    countConsecutive = 0
    for i in range(len(original)):
        countConsecutive += 1

        if (i+1 >= len(original)) or (original[i] != original[i+1]):
            compressed += original[i] + str(countConsecutive)
            countConsecutive = 0

    # length check
    if len(compressed) > len(original):
        return original

    return compressed

original = "aabcccccaaa"
print(compression(original))
