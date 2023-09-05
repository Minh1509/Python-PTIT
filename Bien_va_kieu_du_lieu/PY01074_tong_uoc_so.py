limit = 2 * 10**6
def sang(limit) :
    prime = [1] * (limit +1)
    prime[0] = prime[1] = 0
   
    for i in range( 2, int(limit** 0.5) +1):
        if prime[i] ==1 :
            for j in range( i *i , limit +1, i) :
                if prime[j] == 1 :
                    prime[j] = i
    for i in range( 2, limit +1) :
        if prime[i] ==1 :
           prime[i] = i
    return prime
def solve(n) : 
    primes = sang(limit)
    if primes[n] == 0 :
        return n
    sum =0
    while( n != 1) :
        sum += primes[n] 
        n //= primes[n]
    return sum

totalsum =0
t = int(input())
for _ in range(t) :
        n = int(input()) 
        totalsum += solve(n)
print(totalsum)



