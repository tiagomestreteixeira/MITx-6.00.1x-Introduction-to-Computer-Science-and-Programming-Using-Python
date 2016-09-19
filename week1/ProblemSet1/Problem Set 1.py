# Problem 1

s = 'dgrgaxwupkxokiolhai'
num_vowels = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        num_vowels += 1

print(num_vowels)
