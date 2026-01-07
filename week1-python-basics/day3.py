'''''
Strings in Python
'''''

name = "Aditi"
print(len(name))   # 5

text = "PYTHON"
print(text.lower())   # python

text = "python"
print(text.upper())   # PYTHON

name = "aditi"
print(name.capitalize())   # Aditi

sentence = "hello world"
print(sentence.title())   # Hello World

text = "  hello  "
print(text.strip())   # "hello"

text = "I like Java"
print(text.replace("Java", "Python"))

text = "Python"
print(text.find("t"))   # 2

text = "banana"
print(text.count("a"))   # 3

text = "Python"
print(text.startswith("Py"))   # True

text = "Python"
print(text.endswith("on"))   # True

text = "apple,banana,mango"
print(text.split(","))

fruits = ["apple", "banana", "mango"]
print(", ".join(fruits))

text = "123"
print(text.isdigit())   # True

text = "Python"
print(text.isalpha())   # True

