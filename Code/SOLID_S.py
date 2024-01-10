"""
У класса должна быть только одна ответственность, выраженная через его методы.
Если класс занимается более чем одной задачей, вам следует разделить эти задачи на отдельные классы.
"""
from pathlib import Path


class FileManager:
    def __init__(self):
        self.path = Path(__file__).parent.resolve()

    def read(self):
        file = open(str(self.path), "r")
        return file

    def write(self):
        file = open(str(self.path)+"/text.txt", "w")
        file.write("test")
        file.close()


class ZipFileManager:

    def zipfile(self):
        pass

    def unzipfile(self):
        pass


fm = FileManager()
fm.write()
