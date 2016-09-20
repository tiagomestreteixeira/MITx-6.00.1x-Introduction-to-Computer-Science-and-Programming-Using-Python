# Problem 1

s = 'dgrgaxwupkxokiolhai'
num_vowels = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        num_vowels += 1

print(num_vowels)

# Problem 2
s = 'azcbobobegghaklbokbob'
num_bobs = 0
for idx in range(len(s)):
    if s[idx] == 'b' and idx >= 2:
        if s[idx - 2] == 'b' and s[idx - 1] == 'o':
            num_bobs += 1
print("Number of times bob occurs is:", num_bobs)

# Problem 3
s = 'pnlongblzgwhsoitwctw'

longest_substring = s[0]
for idx in range(len(s)):
    aux_longest_substring = s[idx]
    for idy in range(idx + 1, len(s)):
        if s[idy] >= s[idy - 1]:
            aux_longest_substring += s[idy]
            if len(longest_substring) < len(aux_longest_substring):
                longest_substring = aux_longest_substring
        else:
            break

print("Longest substring in alphabetical order is:", longest_substring)
