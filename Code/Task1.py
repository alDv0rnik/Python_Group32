"""
Написать класс TextProcessor для обработки текстовых данных. Класс должен иметь публичный метод
get_clean_string, который удалит все знаки препинания из строки, которую в него передают
аргументом и приватный метод is_punctuation, который непосредственно проверяет символ на
равенство со знаками пунктуации и возвращает True/False, которые в свою очередь являются
приватным или защищенным атрибутом класса.
"""
import string


class TextProcessor:

    def __init__(self):
        self.__punctuation = string.punctuation

    def __is_punctuation(self, char):
        return True if char in self.__punctuation else False

    def get_clean_string(self, text):
        result = ""
        for i in text:
            if not self.__is_punctuation(i):
                result += i
        return result


# test_string = "Python, Java, Golang!"
# text_proc = TextProcessor()
# print(text_proc.get_clean_string(test_string))
