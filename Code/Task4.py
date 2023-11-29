"""
Напишите простейшую функцию-калькулятор, которая будет выполнять с двумя переданными ей числами следующие действия:
сложение, вычитание, умножение и деление с указанной точностью.
Соответственно, функция должна принимать два позиционных числовых аргумента для чисел,
один именованный строковый аргумент op (по умолчанию функция должна выполнять операцию сложения) и
один именованный числовой аргумент prec для требуемой точности результата (по умолчанию три знака после запятой).
В случае деления на ноль функция должна возвращать None,
а при попытке выполнения непредусмотренной операции – сообщение об ошибке «Неподдерживаемый тип операции!».
Выведите на экран результаты вызовов функции с точностью до сотых для числовых выражений:
"""
from typing import Any

OP = "+-*/"


def calculate(a: int, b: int, op="+", prec=3) -> Any:
    # breakpoint()
    if op == "/" and b == 0:
        return None
    if op not in OP:
        return "Неподдерживаемый тип операции!"
    else:
        if op == "-":
            return round(a - b, prec)
        elif op == "+":
            return round(a + b, prec)
        elif op == "/":
            return round(a / b, prec)
        return round(a * b, prec)


print(calculate(1, 4, op="/"))
