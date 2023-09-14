def solve( n, sum ):
    while n > 0:
        sum *= n % 10
        n //= 10
    return sum

def cmp(a) :
    return sorted(a, key = lambda x : (solve(x, 1), x))

for _ in range( int(input())):
    n = int(input())
    lst = [int(i) for i in input().split()]

    tmp = cmp(lst)
    print(" ".join(map(str, tmp)))