import gc


def make_list():
    lst = [1, 2, 3, 4]
    lst.append(lst)
# print(lst)
# print(lst is lst[-1])


def main():
    for i in range(10):
        make_list()

    num = gc.collect()
    print("Num of unreachable objects: ", num)
    print("Data in garbage: ", gc.garbage)


if __name__ == '__main__':
    main()
    print(gc.get_threshold())

