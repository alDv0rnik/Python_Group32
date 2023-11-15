"""
Дан словарь с товарами.
Выведите на экран все товары, цена которых не превышает 100 рублей, а текущий остаток не менее 10 кг
goods = {
     "apple": {"name": "Яблоки", "cost": 25, "kg": 30},
     "pear": {"name": "Груши", "cost": 50, "kg": 10},
     "plum": {"name": "Сливы", "cost": 55, "kg": 25},
     "cherry": {"name": "Вишни", "cost": 99, "kg": 5}
}

"""
goods = {
     "apple": {"name": "Яблоки", "cost": 25, "kg": 30},
     "pear": {"name": "Груши", "cost": 50, "kg": 10},
     "plum": {"name": "Сливы", "cost": 55, "kg": 25},
     "cherry": {"name": "Вишни", "cost": 99, "kg": 5}
}

for key, val in goods.items():
    if val.get("cost") <= 100 and val.get("kg") >= 10:
        print(key)

