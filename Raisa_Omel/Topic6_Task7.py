lst=[]
for i in range(int(input('введите количество продуктов '))):
    lst.append(input('продукт ').split())

lst_ = []
for i in range(int(input('введите количество ингрудиентов '))):
    elem=input('ингредиент ').split()
    lst_.append('есть' if elem in lst else 'отсутствует')

print(*lst_, sep='\n')
