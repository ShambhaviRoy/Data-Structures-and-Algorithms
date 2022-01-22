# Given 3 arrays a, b, c of different sizes, find the number of distinct triplets  where p is an element of a, q is an element of b, r is an element of c
# and satisfying the criteria: p <= q and q >= r


def triplets(a, b, c):
    a = list(set(a))
    a.sort()
    b = list(set(b))
    b.sort()
    c = list(set(c))
    c.sort()
    
    ai, bi, ci = 0, 0, 0
    ans = 0
    
    while bi < len(b):
        while ai < len(a) and a[ai] <= b[bi]:
            ai += 1
        while ci < len(c) and c[ci] <= b[bi]:
            ci += 1  
        ans += ai*ci
        bi += 1
    return ans

if __name__ == '__main__':

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])
    lenb = int(lenaLenbLenc[1])
    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))
    arrb = list(map(int, input().rstrip().split()))
    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)
    print('Answer=', ans)

