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