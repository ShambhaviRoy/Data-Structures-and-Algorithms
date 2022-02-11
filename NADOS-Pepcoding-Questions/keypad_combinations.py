# Given a string of numbers, print all keypad combinations possible
# https://nados.io/question/print-kpc

# Given a string of numbers, get all keypad combinations possible in a list
# https://nados.io/question/get-kpc



mapping = {'0': '.;', '1': 'abc', '2': 'def', '3': 'ghi', '4': 'jkl', '5': 'mno', '6':'pqrs', '7':'tu', '8':'vwx', '9': 'yz'}


def printKPC(ques, ans_so_far):
    # only printing each keypad combination

    if len(ques) == 0:
        print(ans_so_far)
        return

    num0 = ques[0]
    rem = ques[1:len(ques)]

    for ch in mapping[num0]:
        printKPC(rem, ch+ans_so_far)



def getKPC(ques):
    # saving each keypad combination in a list and returning it

    if len(ques) == 0:
        return ['']

    num0 = ques[0]
    rem = ques[1:len(ques)]

    codefornum0 = mapping[num0]
    remres = getKPC(rem)
    ans_so_far = []

    for ch in codefornum0:
        for rch in remres:
            ans_so_far.append(ch + rch)

    return ans_so_far

    
    
if __name__ == "__main__":
    s = input() 
    printKPC(s, '')
    ans = getKPC(s)
    print(ans)
    