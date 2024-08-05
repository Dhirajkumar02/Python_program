print("Enter the Value of n: ", end="")
n = int(input())

fib = list()
b = 1
c = 0
i = 1
while i <= n:
    if i == 1:
        c = 0
    elif i == 2 or i == 3:
        c = 1
    else:
        a = b
        b = c
        c = a+b
    fib.append(c)
    i = i+1

if len(fib) == 0:
    print("\nOk!")
else:
    print("\nFirst", n, "Terms of Fibonacci Series are:")
    for i in fib:
        print(i, end=" ")