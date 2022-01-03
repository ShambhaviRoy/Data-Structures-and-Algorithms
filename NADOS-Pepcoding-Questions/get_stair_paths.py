# Get Stair Paths
# https://nados.pepcoding.com/content/eb9863ac-63ac-4b94-881f-0aeb24df0985/0c54b191-7b99-4f2c-acb3-e7f2ec748b2a/ae41ae29-11ca-4ae4-8ec7-72a411fd59b6/d341a7c9-1269-409c-b851-0bb512289544/b0de95ee-d178-450a-b3a0-325eeaccfa58/question/17c0ada5-3276-4f47-88ea-8fd7e208b73d
# 1. You are given a number n representing number of stairs in a staircase.
# 2. You are standing at the bottom of staircase. You are allowed to climb 1 step, 2 steps or 3 steps in one move.
# 3. Complete the body of getStairPaths function - without changing signature - to get the list of all paths that can be used to climb the staircase up.

# Example Input: 3
# Output: [111, 12, 21, 3]

def get_stair_paths(n):
    if n == 0:
        return ['']
    
    steps = [1, 2, 3]

    answer = []

    for step in steps:
        if (n-step) >= 0:
            rec_ans = get_stair_paths(n-step)
            for el in rec_ans:
                answer.append(str(step) + el)

    return answer
    
    
     
    
if __name__ == "__main__":
    n = int(input())
    ans = get_stair_paths(n)
    print("["+', '.join(ans) + "]")