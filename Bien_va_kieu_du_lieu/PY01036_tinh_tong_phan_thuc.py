import math
t = int(input())
for i in range(t) :
    n = int(input())
    tmp =0
    if n % 2 ==0:
        
        for i in range(2, n+1, 2) :
            tmp += 1/i
    else :
        tmp = 1
        for i in range(3, n+1, 2) :
            tmp += 1/i
    print("{:.6f}".format(tmp))