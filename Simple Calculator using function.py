def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
while True:
    while True:
        print("Enter Your Choice (1-5): ", end="")
        try:
            ch = int(input())

            if ch >= 1 and ch <= 4:
                print("\nEnter Two Numbers: ", end="")
                nOne = eval(input())
                nTwo = eval(input())
                
            if ch == 1:
                print("\nResult =", add(nOne, nTwo))
            elif ch == 2:
                print("\nResult =", sub(nOne, nTwo))
            elif ch == 3:
                print("\nResult =", mul(nOne, nTwo))
            elif ch == 4:
                print("\nResult =", div(nOne, nTwo))
            elif ch == 5:
                break
            else:
                print("\nInvalid Input!..Try Again!")
            print("------------------------")

        except ValueError:
            print("\nInvalid Input!..Try Again!")
            print("------------------------")
            continue
    if ch == 5:
        break