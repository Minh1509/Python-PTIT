import math



a, b = map(int, input().split())
for i in range(a, b-1) :
    for j in range(i+1, b) :
        for k in range (j +1, b+1) :
            if math.gcd(i, j) ==1 and math.gcd(i, k) ==1 and math.gcd(j, k) ==1 :
                print("(" , end = "")
                print(i, end = "")
                print(", ", end = "")
                print(j, end = "")
                print(", ", end = "")
                print(k, end= "")
                print(")")
