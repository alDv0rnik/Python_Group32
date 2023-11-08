N = int(input("Enter your number: "))
simple = 1
for i in range(2, N - 1):
    if not (N % i):
        simple = 0
        break
print(simple)
