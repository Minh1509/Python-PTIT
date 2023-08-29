import math
def nto(n):
    for i in range( 2, int(math.sqrt(n)) +1) :
        if n % i ==0 :
            return False
    return n > 1

def solve(s) :
    sum =0
    for i in range(0, len(s)):
        if (i % 2 ==0 and int(s[i]) % 2 ==1) or ( i % 2 ==1 and int(s[i]) % 2 ==0) :
            return "NO" 
        sum += int(s[i])
    if nto(sum) :
        return "YES"
    return "NO"
for _ in range( int(input())) :
    s = input()
    print(solve(s))