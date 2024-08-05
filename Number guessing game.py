import random
import math
lower = int(input("Enter lower bound:-"))
upper = int(input("Enter upper bound:-"))
x = random.randint(lower, upper)
print("\n\t You've only", round(math.log(upper-lower+1, 2)),"chances to guess the integer!\n")
count = 0
while count <math.log(upper-lower+1, 2):
    count += 1
    guess = int(input("guess a number:-"))
    if x == guess:
        print("Congratulation! you guessed it right! in ", count, "try")
        break
    elif x > guess:
        print("You guessed too small. Try again! ")
    elif x < guess:
        print("You guessed too large. Try again!")
if count >= math.log(upper-lower+1, 2):
    print("\nThe number is %d" % x)
    print("\nSo sorry! Better Luck Next time!")
