num = int(input('введите число  '))
num0 = num-1
rez=1
while num0>1 and rez==1:
    if num%num0==0:
        rez=0
    num0-=1
print(f'{num} -', 'простое' if rez else 'не простое')

