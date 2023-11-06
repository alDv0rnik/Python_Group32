str_ = input('введите строку ').strip()
str_new=''
for num in range(len(str_)):
    if num%2==0:
        str_new += '_'
    elif str_[num]=='a':
        str_new += 'b'
    else:
        str_new+=str_[num]

print(str_new)
