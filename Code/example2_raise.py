from os.path import exists


def open_file(filepath):
    if not exists(filepath):
        raise FileNotFoundError("error")

    print("Open file")


open_file(r"C:\Users\python\PycharmProjects\Python_Group32\Code\test.txt")
