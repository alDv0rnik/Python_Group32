dct={'i': 1,'c': 2, 'a': 3, 'n': 4, 't': 5, 'h': 6}
print(id(dct))
dct_new=dct.copy()
lst=list(dct.keys())
dct.clear()
lst[0], lst[-1] = lst[-1], lst[0]
del lst[1]
for key in lst:
    dct[key]=dct_new[key]

dct['new key']='newvalue'
print(dct_new)
print(dct)
print(id(dct))
