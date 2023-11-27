s = input()
d = {}
for i in range(len(s)):
    d.update({s[i]: s.count(s[i])})
d1 = {}
for i in range(3):
    d1.update({int(list(d.keys())[list(d.values()).index(max(list(d.values())))]): d.pop(str(list(d.keys())[list(d.values()).index(max(list(d.values())))]))})
print(d1)
