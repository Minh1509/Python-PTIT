from math import gcd
n = int(input())
a = [int(i) for i in input().split()]
a.sort()
for i in range(n-1) :
    for j in range(i+1, n) :
        if gcd(a[i], a[j] )== 1 :
            print(str(a[i]) + " " + str(a[j]))
        