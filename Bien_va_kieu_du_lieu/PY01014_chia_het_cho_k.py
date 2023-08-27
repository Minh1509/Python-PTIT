a, k,n = map(int, input().split())
if n <= a or k > n:
    print("-1")
else:
    tmp = a // k
    for i in range ( k * (tmp+1) , n+1, k) :
        print(( i - a), end= " ")
   
    
        

