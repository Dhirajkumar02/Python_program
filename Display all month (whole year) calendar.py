import calendar

print("Enter Year: ", end="")
try:
    yy = int(input())
    print()
    mm = 1
    while mm <= 12:
        print(calendar.month(yy, mm))
        mm = mm+1
except ValueError:
    print("\nInvalid Input!")