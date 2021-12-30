# Inverse of a number
# https://nados.pepcoding.com/content/eb9863ac-63ac-4b94-881f-0aeb24df0985/0c54b191-7b99-4f2c-acb3-e7f2ec748b2a/ae41ae29-11ca-4ae4-8ec7-72a411fd59b6/2d84b678-b7e8-4aab-ac36-03c4f1540353/2d1dfd98-0591-4bdd-ad75-837ddcde624a/question/c7a2482d-24ce-4d54-ac92-6fe986bbd3d5

# Interchange a number's digit and position from right
# Input = 2134, Output = 1243
# Input: 4 at place 1, 3 at place 2, 1 at place 3 and 2 at place 4 from right
# Output: 3 at place 1, 4 at place 2, 2 at place 1 and 1 at place 4 from right 

def inverse(n):
    # write your code here
    temp = n
    nod = 0
    while temp >= 1:
        nod += 1
        temp = temp/10

    answer = 0    
    pos = 1

    while pos <= nod :
        digit = n % 10
        n = n//10         
        answer += pos * (10**(digit-1))
        pos += 1

    print(answer)



def main():
    n = int(input())
    inverse(n)

if __name__=="__main__":
    main()
