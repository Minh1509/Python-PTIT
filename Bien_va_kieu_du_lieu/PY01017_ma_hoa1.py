t = int(input())
for i in range(t):
    s = input()

    for i in range(0, len(s) - 1):
        if s[i + 1] != s[i]:
            print(s.count(s[i]), end="")
            print(s[i], end= "")

    if(s[len(s)-1] != s[len(s) -2]) :   
        print(s.count(s[len(s)-1]), end= "")
        print(s[len(s) -1] )

