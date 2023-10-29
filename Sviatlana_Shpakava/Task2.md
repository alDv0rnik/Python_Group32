# Task 1
length = 250
velocity = 80
print(length / velocity)

# Task 2
age = str(input())
name = str(input())
string = f"My name is {name} and i am {age}"
print(string)

# Task 3
num = int(input("Только трехзначное число"))
print((num // 10 % 10) + (num // 100) + (num % 10))

# Task 4
import math
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = pow(x1 - x2, 2)
y = pow(y1 - y2, 2)
print(pow((x + y), 0.5))

# TasK 5
snake_case_string = "it_step_course"
snake_case_string = snake_case_string.title()
print(snake_case_string.replace("_", ""))

# Task 6
number = "8(029)321-65-87"
newnumber = "+37529"
print(newnumber + number[6:9] + number[10:12] + number[13:])

# Task 7
funnystring = str(input())
indexstart = funnystring.find("ша", 0)
indexend = funnystring.find("ша", -1)
print(indexstart)
print(indexend)

# Task 8
mystring = "Python - самый простой язык программирования"
print(mystring.count(" "))
print(len(mystring.replace(" ", "")))
