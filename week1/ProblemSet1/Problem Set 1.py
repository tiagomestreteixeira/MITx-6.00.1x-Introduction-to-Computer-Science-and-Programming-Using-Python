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
s = 'azcbobobegghakl'

longest_substring = ""
if len(s) == 1:
    print("Longest substring in alphabetical order is:", s)

for idx in range(len(s)):
    for idy in range(idx, len(s)):
        print(idy)
        aux_longest_substring = ""
        if idy > 0:
            if s[idy] > s[idy - 1]:
                aux_longest_substring += s[idy]
            else:
                if len(longest_substring) < len(aux_longest_substring):
                    longest_substring = aux_longest_substring
                    break

print("Longest substring in alphabetical order is:", longest_substring)
