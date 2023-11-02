num = int(input('введите число '))
lst1=[10,9,5,4,1]
lst2=['X','IX','V','IV','I']
ind=-1
str_=''
for sign in lst1:
    ind+=1
    while num>=sign:
        str_+=lst2[ind]
        num-=sign
print(str_)
