"""
Написать класс DataInterface, который будет иметь своим защищенным атрибутом объект класса
TextLoader и публичный метод process_texts, который будет принимать список строк, в цикле
обработает каждую и выведет ее значение в консоль.

"""
from typing import List
from Task2 import TextLoader

strings = ["Python, Java, Golang!", "Python, Java, Gol@ang!"]


class DataInterface:

    def __init__(self):
        self.__text_loader = TextLoader()

    def process_texts(self, string_list: List[str]) -> List[str]:
        result = []
        for string_ in string_list:
            self.__text_loader.set_clean_text(string_)
            result.append(self.__text_loader.clean_string)
        return result


if __name__ == '__main__':
    data_interface = DataInterface()
    print(data_interface.process_texts(strings))