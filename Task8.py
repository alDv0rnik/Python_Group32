N = int(input("Enter size of list "))
lst = []
for i in range(N):
    lst.append(int(input(f"Enter {i+1}st list item ")))
print(sum(lst) / N)
