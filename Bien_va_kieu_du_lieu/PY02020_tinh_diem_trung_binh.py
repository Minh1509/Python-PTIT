n = int(input())
a = [float(i) for i in input().split()]

min_a = min(a)
max_a = max(a)


lst = []
for i in a:
    if i != min_a and i != max_a:
        lst.append(i)

print("{:.2f}".format(sum(lst)/ len(lst)))
