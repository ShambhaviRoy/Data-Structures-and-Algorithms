# Print prime factors of a number
# https://nados.pepcoding.com/content/eb9863ac-63ac-4b94-881f-0aeb24df0985/0c54b191-7b99-4f2c-acb3-e7f2ec748b2a/ae41ae29-11ca-4ae4-8ec7-72a411fd59b6/2d84b678-b7e8-4aab-ac36-03c4f1540353/2d1dfd98-0591-4bdd-ad75-837ddcde624a/question/9dd7eb3a-d777-42a7-a098-778cd7c89ba0

# Input = 120
# Output = 2 2 2 3 5




def primeFac(n):
    # write your code here

    div = 2
    while div * div <= n:
        while n%div == 0:
            print(div, end = " ")
            n = n/div
        div += 1
    if n != 1:
        print(int(n)) 
    

def main():
    n = int(input())
    primeFac(n)

if __name__=="__main__":
    main()
