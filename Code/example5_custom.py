# class FileManager:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# def main():
#     with FileManager(filename=filename, mode="a") as file:
#         file.write("Test")
#
#
# if __name__ == '__main__':
#     filename = "text.txt"
#     main()
from contextlib import contextmanager

filename = "text.txt"


@contextmanager
def open_file(filename):
    try:
        file_ = open(filename, "r")
    except FileNotFoundError as err:
        print(err)
    else:
        return file_


with open_file(filename) as file:
    print(file.read())

