# Permutations with Duplicates: Write a method to compute all permutations of a string whose
# characters are not necessarily unique. The list of permutations should not have duplicates.


def get_all_permutations(s):
    count_dict = get_freq_dict(s)
    result = []
    get_permutations(count_dict, '', len(s), result)
    return result

def get_freq_dict(s):
    count_dict = {}
    for char in s:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    return count_dict


def get_permutations(count_dict, prefix, remaining_len, result):
    if remaining_len == 0:
        result.append(prefix)
        return
    
    for char, count in count_dict.items():
        if(count > 0):
            count_dict[char] = count-1
            get_permutations(count_dict, prefix+char, remaining_len-1, result)
            count_dict[char] = count
        


s = 'abbc'
print(get_all_permutations(s))