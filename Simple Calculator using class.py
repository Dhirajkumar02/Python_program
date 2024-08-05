class CodesCracker:
   def add(self, a, b):
      return a+b
   def sub(self, a, b):
      return a-b
   def mul(self, a, b):
      return a*b
   def div(self, a, b):
      return a/b

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

while True:
   while True:
      print("Enter Your Choice (1-5): ", end="")

      try:
         ch = int(input())

         if ch>=1 and ch<=4:
            print("\nEnter Two Numbers: ", end="")
            nOne = float(input())
            nTwo = float(input())
            ob = CodesCracker()

         if ch==1:
            print("\n" +str(nOne)+ " + " +str(nTwo)+ " = " + str(ob.add(nOne, nTwo)))
         elif ch==2:
            print("\n" +str(nOne)+ " - " +str(nTwo)+ " = " + str(ob.sub(nOne, nTwo)))
         elif ch==3:
            print("\n" +str(nOne)+ " * " +str(nTwo)+ " = " + str(ob.mul(nOne, nTwo)))
         elif ch==4:
            print("\n" +str(nOne)+ " / " +str(nTwo)+ " = " + str(ob.div(nOne, nTwo)))
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