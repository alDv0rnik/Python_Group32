"""
Дан список data = ['John_25', 'Sally_19', 'Susan_35', 'Jack_16'], где элемент состоит из Имени(str) и Возраста (int).
Задача - создать список кортежей из указанных параметров. Например, [('John', 25), ('Sally', 19)]
"""
data = ['John_25', 'Sally_19', 'Susan_35', 'Jack_16']
print([tuple(value.split("_")) for value in data])
print([(value.split("_")[0], int(value.split("_")[1])) for value in data])


tpl = tuple()
tpl1 = ()

print(tpl1)
