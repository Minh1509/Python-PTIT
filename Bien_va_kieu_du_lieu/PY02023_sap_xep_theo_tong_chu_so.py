import math
def solve(n, sum):
    while( n > 0) :
        a = n % 10
        sum += a
        n //=10
    return sum
def cmp(a) :
    return sorted(a, key = lambda x: (solve(x, 0), x))
            
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    sorted_lst = cmp(lst)
    print(" ".join(map(str, sorted_lst)))
