a, b, c = input("Enter 3 No:").split()
a = int(a)
b = int(b)
c = int(c)
if a > b:
    if a > c:
        print(" Gr no is ", a)
    else:
        print(" Gr no is ", c)
else:
    if b > c:
        print(" Gr no is ", b)
    else:
        print(" Gr no is ", c)
