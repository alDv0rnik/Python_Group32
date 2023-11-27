keys = ("a", "b", "c", "d", "e") #input()
values = (1, 2, 3, 4, 5) #input()
d = {k: v for k, v in zip(keys, values)}
t = d.popitem()
d1 = {t[0]: t[1]}
d, d1 = d1, d
d.update(d1)
t1 = (list(d.keys())[1], d.pop(list(d.keys())[1]))
d.pop(list(d.keys())[1])
d.update({t1[0]: t1[1]})
d.update({"new_key": "new_value"})
print(d)
