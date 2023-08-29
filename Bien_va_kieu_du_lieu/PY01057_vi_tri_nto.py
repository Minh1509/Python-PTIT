import math
def nto(n) :
    for i in range( 2, int(math.sqrt(n))+1) :
        if n % i ==0 :
            return False
    return n > 1
def check( a) :
    return a == '2' or a == '3' or a == '5' or a== '7'

def solve(s) :
    for i in range(2, len(s) ):
        if nto(i) and check(s[i]) == False:
            return "NO"
        if  check(s[i]) and nto(i) == False:
            return "NO"
    return "YES"

for _ in range( int(input())) :
    n = input()
    print(solve(n))