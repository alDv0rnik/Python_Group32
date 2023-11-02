num = int(input("Number "))
summ = num % 10 + num // 100 + (num // 10 % 10)
print("Answer is", summ)