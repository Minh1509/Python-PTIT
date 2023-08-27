import math
def solve(n) :
    print('1 * ', end="")
    for i in range(2, int(math.sqrt(n)+1),1):
        if n % i ==0:
            dem =0
            while n % i ==0:
                n//= i
                dem +=1
            print(i,  end = "")
            print("^", end= "")
            print(dem , end= "")
            if n !=1 :
                print(" * ", end= "")
    if n != 1:
        print(n, end = "")
        print("^1", end = "")
    print()

t = int(input())
for i in range(t) :
    n = int(input())
    solve(n)

