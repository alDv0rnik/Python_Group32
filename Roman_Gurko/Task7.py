text, fragment = input("Enter your string: "), input("Enter the fragment: ")
first = text.find(fragment)
last = text.rfind(fragment)
print(first,last)