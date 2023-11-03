a = int(input("Your number is "))
root_a = pow(a, 0.5)
print(int(pow(root_a + 1, 2))) if (root_a % 1) == 0 else print(-1)