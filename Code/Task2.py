"""
Написать класс TextLoader, который имеет приватным атрибутом text_processor объект класса, что
был создан в задаче 1. Новый класс будет иметь приватный атрибут clean_string и публичный метод
set_clean_text, который будет вызывать метод класса TextProcessor через свой атрибут text_processor и
записывать значение в clean_string. Сам же атрибут clean_string будет иметь property с
дополнительным выводом в консоль того, что выводится уже очищенная строка
"""
from Task1 import TextProcessor


class TextLoader:

    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    @property
    def clean_string(self):
        return self.__clean_string

    def set_clean_text(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text=text)


test_string = "Python, Java, Golang!"
text_loader = TextLoader()
text_loader.set_clean_text(test_string)
print(text_loader.clean_string)