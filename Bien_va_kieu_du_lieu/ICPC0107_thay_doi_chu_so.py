for _ in range(int(input()) ) :
    a, b = input().split()
    x1 = input()
    x2 = input()
    num1 = int(x1.replace(a, b)) + int(x2.replace(a, b))
    num2 = int(x1.replace(b, a)) + int(x2.replace(b, a))
    print(min(num1, num2) ,max (num1, num2))
    print()