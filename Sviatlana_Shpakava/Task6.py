# Task 6
fls = set(input().split())
print(sorted({i.lower() for i in fls if i.lower().endswith('.jpg')}))
