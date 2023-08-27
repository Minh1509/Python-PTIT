import math

n, k = map(int, input().split())
dem = 0

for i in range(10**(k-1), 10**k, 1):
    if math.gcd(i, n) == 1:
        if dem < 10 :
            print(i, end=" ")
            dem+= 1
        else:
            dem = 1
            print()
            print(i, end=" ")
           

# Add a newline character after the loop finishes
print()
