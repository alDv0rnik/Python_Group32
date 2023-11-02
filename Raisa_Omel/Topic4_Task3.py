num = input('введите число ').strip()
ask=''
sign=''
lenght=len(num)
if '-' in num:
    sign = 'negative'
    lenght-=1
print(sign+" "+str(lenght)+' category' if num!='0' else 'Zero')
