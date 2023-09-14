import math
dd = [1] * (10 ** 5) 

def ptich( m) :
    n = m
    ok = True
    for i in range( 2, int(math.sqrt(n)) +1) :
        if n % i == 0 :
            if i < n :
                while( n % i == 0) :
                    n //= i
            else :
                return False
    if n >= m :
        return False
    return True
def solve( ) :
    tmp = 2
    for i in range(2, 10 ** 18 ) :
        if ptich(i) :
             dd[tmp]  = i
             tmp += 1
             
for _ in range( int(input())) :
    n = int( input())
    if dd.count(n) >= 1:
        print(dd.index(n))
    else :
        print("Not in sequence")