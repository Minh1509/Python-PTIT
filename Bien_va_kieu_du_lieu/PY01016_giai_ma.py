t = int( input())
for i in range(t):
    s = input()
    for i in range (1,len(s), 2):
        k = int(s[i])
        for j in range(k):
            print(s[i-1], end = '')
    print('\n')
  