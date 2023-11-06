num = int(input('введите число  '))
summ=0
proiz=1
for i in range(1,num+1):
    proiz*=i
    summ+= proiz if i%2 else proiz * -1
print(summ)
