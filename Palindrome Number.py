n = int(input("Enter a Number:"))
temp = n
rev = 0
while n > 0:
    rem = n % 10
    rev = (rev*10)+rem
    n = n//10
if temp == rev:
    print("Given number is palindrome.")
else:
    print("Given number is not palindrome.")
