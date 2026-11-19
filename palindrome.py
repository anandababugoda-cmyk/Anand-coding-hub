'''word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")'''

word = "hello"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


word = "Python"

print(word[::1])   # Forward
print(word[::-1])  # Reverse
print(word[::2])   # Skip every second character
print(word[::-2])  # Reverse and skip every second character