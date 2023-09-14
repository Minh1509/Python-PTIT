n = int(input())
a = [[]]*n

for i in range(n):
    a[i] = [int(x) for x in input().split()]

k = int(input())
sum1 =0
sum2 =0
for i in range(n):
    for j in range(n) :
        if j < n-i-1 :
            sum1 += a[i][j]
        elif j > n-i-1:
            sum2 += a[i][j]
tmp = abs(sum1- sum2)
if tmp <= k:
    print("YES")
else :
    print("NO")
print(tmp)

