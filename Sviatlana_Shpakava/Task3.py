# Task 3
s = input()
d = {}
for i in s:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)
print(sorted(d.items())[-3:])
