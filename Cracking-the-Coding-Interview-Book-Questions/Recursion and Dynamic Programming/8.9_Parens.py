# Parens: Implement an algorithm to print all valid (Le., properly opened and closed) combinations
# of n pairs of parentheses.


# Approach 1: Base Case and Build
def get_parens(n):
    if n == 1:
        return {'()'}
    
    all_parens = set()
    paren_set = get_parens(n-1)
    
    # add a () after every ( in paren_set
    for paren in paren_set:
        all_parens.add('()' + paren)

        for i in range(len(paren)):
            if paren[i] == '(':
                new_paren = insert_inside(paren, i)
                all_parens.add(new_paren)

    return all_parens


def insert_inside(paren, left_index):
    new_paren = paren[:left_index+1] + '()' + paren[left_index+1:]
    return new_paren




# Approach 2: Add all open and close parens in a valid pattern, would not create duplicate patterns

def generate_parens(parens_list, open_rem, closed_rem, paren, index):
    if open_rem < 0 or closed_rem < open_rem:
        return 
    
    if open_rem == 0 and closed_rem == 0:
        parens_list.append(paren)
    else:
        paren1 = paren[:index] + '(' + paren[index:]
        generate_parens(parens_list, open_rem-1, closed_rem, paren1, index+1)
        paren1 = paren[:index] + ')' + paren[index:]
        generate_parens(parens_list, open_rem, closed_rem-1, paren1, index+1)
    return parens_list




print(get_parens(2))

print(generate_parens([], 2, 2, '', 0))