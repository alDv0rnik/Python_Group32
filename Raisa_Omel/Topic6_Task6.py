lst=[]
for elem in input().lower().split():
    if elem.endswith('.jpg'):
        lst.append(elem)
print(lst)
print(*sorted(list(set(lst)),reverse=False))
