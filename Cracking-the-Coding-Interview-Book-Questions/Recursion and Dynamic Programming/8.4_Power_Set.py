# Power Set: Write a method to return all subsets of a set.

# s = ['a', 'b', 'c']
# P(['a']) = [[], ['a']]
# P(['a', 'b']) = [[], ['a'], ['b'], ['ab']]

def get_subsets(s, index):
    all_subsets = []
    if(len(s) == index):
        all_subsets.append([])
    else:
        all_subsets = get_subsets(s, index+1)
        item = s[index]
        more_subsets = []
        for subset in all_subsets:
            new_subset = []
            new_subset.extend(subset)
            new_subset.append(item)
            more_subsets.append(new_subset)
        all_subsets.extend(more_subsets)
        print(f'all_subsets = {all_subsets}')
    return all_subsets


def get_subsets2(s):
    # generate binary numbers from 0 to 2^len(s)
    all_subsets = []
    for num in range(0, 2**len(s)):
        subsets = convert_int_to_set(num, s)
        all_subsets.append(subsets)
    return all_subsets

def convert_int_to_set(num, s):
    set = []
    k = num
    index = 0
    while k>0:
        if (k & 1) == 1:
            set.append(s[index])
            index += 1
        k = k >> 1
    return set


    

s = ['a', 'b', 'c']
print(get_subsets(s, 0))
