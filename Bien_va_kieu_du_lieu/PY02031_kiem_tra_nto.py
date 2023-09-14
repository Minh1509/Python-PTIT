import math
def isPrime(n):
    for i in range( 2, int(math.sqrt(n))+1) :
        if ( n % i ==0) :
            return False
    return n > 1
n , m= list(map(int, input().split()))
a = [[]] * n * m
for i in range(n) :
   
    a[i] = [int(i) for i in input().split()]
for i in range(n) :
    for j in range(m) :
        if isPrime(a[i][j]) :
            a[i][j] =1
        else :
            a[i][j] = 0
for i in range(n) :
    for j in range(m) :
        print(a[i][j], end= " ")
    print() 

