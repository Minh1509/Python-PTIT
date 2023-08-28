import math
def solve(n):
    for i in range( 2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n > 1

for _ in range( int(input())) :
    n = input()
    sum =0
    for i in n :
        sum += int(i) 
    if solve(sum) :
        print("YES")
    else :
        print("NO")