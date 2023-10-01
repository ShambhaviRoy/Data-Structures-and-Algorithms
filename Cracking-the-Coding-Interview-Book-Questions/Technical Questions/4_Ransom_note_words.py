# Example: A ransom note can be formed by cutting words out of a magazine to form a new
# sentence. How would you figure out if a ransom note (represented as a string) can be formed
# from a given magazine (string)?

# Approach:
# Check whether each word in ransom note occurs in magazine. That means each word in ransom note should be in magazine. 
# So check each word in ransome note and it's frequency in the magazine

# Time complexity = O(len(ransom note))
# Space complexity = O(len(magazine))


def create_dict(st):
    map = {}
    word_list = st.split(" ")
    for s in word_list:
        if s not in map:
            map[s] = 1
        else:
            map[s] += 1
    return map



def find_ransom_note_words(ransom_note, magazine):
    rn_map = create_dict(ransom_note)
    mag_map = create_dict(magazine)

    flag = False

    for rn_word, rn_freq in rn_map.items():
        if mag_map[rn_word] >= rn_freq:
            flag = True
        else:
            flag = False
        
    return flag



# Sample input
ransom_note = "the quick fox"
magazine = "the quick fox jumps over the lazy dog"
print(find_ransom_note_words(ransom_note, magazine))