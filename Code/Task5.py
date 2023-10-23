"""
Напишите программу, которая получает на вход целое число n – количество дней,
и конвертирует n в годы, месяцы и дни.

>>> 398
>>> 1 год, 1 месяц, 3 дня
"""
days = int(input())
years = days // 365
months = (days - years * 365) // 30
days_ = (days - years * 365) - (months * 30)
print(years, months, days_)
