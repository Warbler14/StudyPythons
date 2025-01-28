string_text = "Python is Amazing"

print(string_text.lower())
print(string_text.upper())
print(string_text[0].isupper())
print(len(string_text))
print(string_text.replace("Python", "Java"))
# print(string_text)

index = string_text.index("n")
print(str(index))

index = string_text.index("n", index + 1)
print(str(index))

print(string_text.find("n"))
print(string_text.find("Java"))
# print(string_text.index("Java"))

print(string_text.count("n"))

number = 10
day = "three"
print("I eat %d apples." % number)
print("I ate %d apples. so I was sick for %s days." % (number, day))