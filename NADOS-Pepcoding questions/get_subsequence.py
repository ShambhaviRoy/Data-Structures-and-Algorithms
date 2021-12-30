# Get subsequences of a given string
# For a string, subsequence is a part derived from a given string which is obtained by deleting some or no elements of the given string without changing the order of the remaining elements.
# Example: 'abc' --> ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']

def getSS(s):
    # base case
    if len(s) == 0:
        return ['']

    ch = s[0]
    ros = s[1:len(s)]
    
    mres = getSS(ros)
    print(mres)

    answer = []

    for sub in mres:
        answer.append(sub)
    
    for ss in mres:
        answer.append(ch + ss)
    return answer

    
if __name__ == "__main__":
    s = input() 
    ans = getSS(s)
    print("["+', '.join(ans) + "]")