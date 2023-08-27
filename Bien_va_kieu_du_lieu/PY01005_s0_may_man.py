def solve (n) :
    dem4 =0
    dem7=0
    while n > 0:
        tmp = n % 10
        if tmp ==7 :
            dem7 +=1
        if tmp ==4 :
            dem4  +=1
        n //=10
    
    if (dem4 + dem7) == 4 or (dem4 + dem7) == 7:
    
        print("YES")
    else :
        print("NO")
    
n = int(input())
solve(n)


