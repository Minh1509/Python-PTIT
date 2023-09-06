from math import gcd

n = int(input())
a = [int(x) for x in input().split()]
a.sort()

for i in range(n):
    for j in range(i+1,n):
        if a[i] < a[j] and gcd(a[i], a[j]) == 1:
            print(str(a[i]) + " " + str(a[j]))
print()
