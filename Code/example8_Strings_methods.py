a = "½⅓¼⅕⅙"
b = "1245"
c = "124asdf5!!"
d = "123457"
f = "Asdsdfsdf"

# isdigit() isnumeric()
print(b.isdigit())
print(c.isdigit())
print(b.isnumeric())
print(a.isdigit())
print(a.isnumeric())

# c = chr(189)
# print(c)
# isalnum()
print(c.isalnum())
print(d.isdecimal())
print(f.isalpha())
print(f.islower())

# split() replace()
text = "Python, is, easy"
text1 = text.replace(" ", "").replace("Python", "Java").replace("easy", "hard")
lst = text1.split(",")
print(text1)
print(lst)

# count
print(text.count("is"))

# find index
print(text.find("is"))
# print(text.index("W"))


text2 = "askjdh"
text3 = "AsKjDH"
print(text2.upper())
print(text3.lower())
print(text2.capitalize())
print(text3.swapcase())
print(text3.title())

# strip
print(text2)
print(text2.strip())

# startwith endwith
print(text2.startswith("b"))
print(text2.endswith("h"))

