t = int(input())
for _ in range(t) :
    s = input()
    s1 = input()
    i =0
    dem =0
    while i < len(s)  :
        tmp = s.find(s1, i, len(s))
        if tmp != -1 :
            dem += 1
            i = tmp+  len(s1)
        else :
            break
    print(dem)