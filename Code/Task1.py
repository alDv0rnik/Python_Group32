"""
Напишите класс PrintData для работы с виртуальным принтером.
Класс должен содержать функцию print, send_data, send_to_print
В функции send_data необходимо выполнить проверку доступности принтера (через true/false).
В случае false вызвать исключение "принтер не отвечает"

Модифицируйте класс при помощи пользовательского исключения ExceptionPrintSendData(Exception)
и добавьте блок обработки ошибок try-except

"""
class ExceptionPrintData(Exception):
    def __str__(self):
        return "Error of printing data"

# Exception("Printer is not available")
class PrintData:
    def print(self, data):
        if not self.send_to_print():
            raise ExceptionPrintData
        print(f"печать {data}")

    def send_to_print(self):
        return False


p = PrintData()
try:
    p.print(123)
except ExceptionPrintData as err:
    print(f"Printing error: {err}")



