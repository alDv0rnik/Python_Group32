num = int(input('введите число '))
dct={'X':10,'IX':9,'V':5,'IV':4,'I':1}
str_=''
for key, value in dct.items():
    while num>=value:
        str_+=key
        num-=value
print(str_)
