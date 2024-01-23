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
def open_file(filename, mode):
    try:
        file_ = open(filename, mode)
        if mode == "r":
           yield file_.read()
    except FileNotFoundError as err:
        print(err)
    else:
        file_.close()


with open_file(filename, "r") as file:
    print(file)

