import math
def nto (n):
    for i in range(2, int(math.sqrt(n)+1), 1):
        if n % i ==0 :
            return False
    return n > 1
t = int(input())
for i in range(t) :
    a, b = map(int, input().split())
    sum =0
    tmp = math.gcd(a, b)
    for i in (str(tmp)) :
        sum += int(i)
    if nto(sum) :
        print("YES")
    else :
        print("NO")