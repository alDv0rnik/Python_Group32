from string import Template

# % - оператор
name = "John"
age = 23
s = "My name is %s"%(name)
s_ = "I'm %d years old"%(age)
print(s)
print(s_)

# шаблоны
temp = Template("$name - is my name")
print(temp.substitute(name=name))


# format()
s1 = "My name is {0} and I'm {1} years old".format(name, age)
s2 = "My name is {name} and I'm {age} years old".format(name=name, age=age)
s3 = "My name is {0} and I'm {age} years old".format(name, age=age)

print(s1)
print(s2)
print(s3)

# f-string

s4 = f"My name is {name} and I'm {age + 2} years old"
print(s4)


BASE_URL = "https://weather.com/city/{}"

city = input()
weather = BASE_URL.format(city)
print(weather)
