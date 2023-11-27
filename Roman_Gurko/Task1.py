s = input()
d = {}
for i in range(len(s)):
    d.update({s[i]: s.count(s[i])})
print(d)
