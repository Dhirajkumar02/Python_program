Str = input("Enter a string:")
i = 0
while i < len(Str):
    ch = Str[i]
    i += 1
    if ch in "aeiouAEIOU":
        pass
    else:
        print(ch)


