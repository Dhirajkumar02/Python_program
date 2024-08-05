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
         if ch>=1 and ch<=4:
            print("\nEnter Two Numbers: ", end="")
            numOne = eval(input())
            numTwo = eval(input())

         if ch==1:
            print("\nResult =", numOne+numTwo)
         elif ch==2:
            print("\nResult =", numOne-numTwo)
         elif ch==3:
            print("\nResult =", numOne*numTwo)
         elif ch==4:
            print("\nResult =", numOne/numTwo)
         elif ch==5:
            break
         else:
            print("\nInvalid Input!..Try Again!")
         print("------------------------")
      except ValueError:
         print("\nInvalid Input!..Try Again!")
         print("------------------------")
         continue
   if ch==5:
      break