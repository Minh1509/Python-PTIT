import math

t = int(input())
for i in range(t) :
    n = (input())
    dao_n = n[::-1]

    if math.gcd(int(n), int(dao_n)) ==1:
        print("YES")
    else :print("NO")

