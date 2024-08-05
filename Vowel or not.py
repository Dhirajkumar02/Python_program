s = input("Enter a string:")
i = 0
while i < len(s):
    ch = s[i]
    if ch in "aeiouAEIOU":
        print(s, "contains vowel")
        break
    i += 1
else:
    print(s, "Does not contains any vowel")
