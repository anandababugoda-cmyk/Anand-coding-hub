from pydoc import text


word = "Python"

print(word[0])  # P
print(word[1])  # y
print(word[5])  # n
print(word[0:3])  # Pyt
print(word[2:5])  # tho
print(word[:4])   # Pyth
print(word[2:])   # thon

text = "   python   "
print(text.upper())       # PYTHON
print(text.lower())       # python
print(text.title())       # Python
print(text.capitalize())  # Python
print(text.replace("python", "world"))
print(text.strip())       # Removes spaces at beginning/end


first_name = "Anand"
last_name = "Babu"

full_name = first_name + " " + last_name

print(full_name)

name = "Anand"
age = 30
print(f"My name is {name} and I am {age} years old.")