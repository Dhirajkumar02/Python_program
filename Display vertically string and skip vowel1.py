Str = input("Enter a string:")
i = 0
while i < len(Str):
    ch = Str[i]
    if ch not in "aeiouAEIOU":
        print(ch)
    i += 1
