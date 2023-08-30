s = input()
s = s.lower()
s1 = ".py"
tmp = s.find(s1, len(s) - 3, len(s))
if tmp != -1 :
    print("yes")
else : 
    print("no")