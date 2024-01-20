"""
Напишите класс PrintData для работы с виртуальным принтером.
Класс должен содержать функцию print, send_data, send_to_print
В функции send_data необходимо выполнить проверку доступности принтера (через true/false).
В случае false вызвать исключение "принтер не отвечает"

Модифицируйте класс при помощи пользовательского исключения ExceptionPrintSendData(Exception)
и добавьте блок обработки ошибок try-except

"""


class PrintDataSendError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"An error while handling data {self.msg}"


class Printer:
    def __init__(self):
        self.available = False

    def is_available(self):
        return True if self.available else False


class PrintData:
    def __init__(self):
        self.printer = Printer()

    def print_data(self):
        print("Printing data")

    def send_data(self):
        if self.printer.is_available():
            self.send_to_print()
        else:
            raise PrintDataSendError("Printer unavailable")

    def send_to_print(self):
        print("Sending data...")


try:
    print_data = PrintData()
    print_data.send_data()
    print_data.print_data()
except PrintDataSendError as err:
    print(err)