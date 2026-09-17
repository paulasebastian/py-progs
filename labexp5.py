text = input("Enter a string : ")

old = input("Enter character to replace: ")

new = input("Enter new character: ")

replaced = text.replace(old, new)

print("After replacement: ", replaced)

reverse = text[::-1]

print("Reverse string: ", reverse)

if text == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")

char_frequency = {}

for ch in text:
    if ch in char_frequency:
        char_frequency[ch] += 1
    else:
        char_frequency[ch] = 1

print("Character frequency: ")
for ch in char_frequency:
    print(ch, ":", char_frequency[ch])

words = text.split()
word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Word frequency : ")
for word in word_frequency:
    print(word, ":", word_frequency[word])
