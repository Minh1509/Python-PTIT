from math import sqrt
def nto(n) :
    for i in range( 2, int(sqrt(n)) +1):
        if n % i ==0:
            return False
    return n > 1
n = int(input())
lst = [int(i) for i in input().split()]
m = {}
for i in lst:
    if nto(i) :
        if i in m :
            m[i]+= 1
        else :
            m[i] = 1

for i in m:
    print(str(i) + " "+ str(m[i]))
