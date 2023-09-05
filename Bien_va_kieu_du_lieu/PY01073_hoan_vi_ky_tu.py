def Try(s) :
    global n, dd  
    if len(s) == n :
        print(s) 
        return
    for i in range(n) :
        if dd[i] == 0:
            dd[i] = 1
            Try(s+ str[i])
            dd[i] = 0

str = input()
n = len(str)
dd = [0] * n
Try("")