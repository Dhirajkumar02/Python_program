ch = input("Enter a char:")
if "A" <= ch <= "Z":
    print("capital letter")
elif "a" <= ch <= "z":
    print("small letter")
elif "0" <= ch <= "9":
    print("Digit")
else:
    print("symbol")