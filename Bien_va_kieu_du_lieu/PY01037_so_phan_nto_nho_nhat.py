def uocso(n) :
    count =0
    for i in range(1, n//2 , 1) :
        if n % i ==0:
            count+=1
    return count

def solve(n) :
    max_limited = 10**7
    a = [0] * (max_limited+1)

    for i in range(1, max_limited+1, 1) :
        a[i] = uocso(i)
    
    # luu so phan nguyen to vao list
    tmp =0
    b = []
    for i in range(1, max_limited+1, 1) :
        if a[i] > tmp :
            b.append(i)
            tmp = a[i]
    for i in b :
        if i >= n :
            
            return i
    return None 
        
t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))