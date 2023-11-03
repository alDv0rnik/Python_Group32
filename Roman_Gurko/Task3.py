import math
num = int(input("Enter your number: "))
if abs(num) > 99:
    print("It is positive three or more digit number" if num else "It is negative three or more digit number")
elif abs(num) > 9:
    print("It is positive two-digit number" if num else "It is negative two-digit number")
elif num != 0:
    print("It is positive one-digit number" if num else "It is negative one-digit number")
else:
    print("ITS ZERO!!!")

