### Topic: Exceptions

#### Task 1
Написать функцию, которая возвращает среднее геометрическое для чисел `a` и `b` (не
использовать модуль math). Выполните обработку исключений при помощи `try-except`

#### Task 2
Пусть есть 3 функции которые вызываются в следующей последовательности
bzz -> bar -> foo. В функции `foo()` возникают исключения `ZeroDivisionError` и `IndexError`. 
Перехватите исключение `ZeroDivisionError` в функции `bar`, а `IndexError` в функции `bzz`

```python
def foo(a):
 b = [1, 2, 3]
 x = 5 / a
 y = b[a]
 print(x, a, y)
 
def bar(a):
 foo(a)
 
def bzz(a):
 bar(a)

```