# Strings are immutable

myString = "Hello"
# The statement myString[0] = "Y" gives an error

# Looping on string
# First way:
s = "abcdefgh"
for index in range(len(s)):
    if s[index] == 'i':
        print("There is an i")

# Second way
for char in s:
    if char == 'i' or char == 'u':
        print("There is an i")

# Suggestion on comparing floats:
aFloat = 3.87583
anotherFloat = 3.875838383838383
if abs(aFloat - anotherFloat) < 0.00001:
    print("they are the same numbers")
else:
    print("they aren't the same number")
