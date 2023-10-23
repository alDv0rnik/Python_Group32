import gc


def make_cycle():
    l = [1, 2, 3, 4]
    l.append(l)


def main():
    for i in range(10):
        make_cycle()

    num = gc.collect()
    print("Unreachable objects: ", num)
    print("Uncollected data: ", gc.garbage)


if __name__ == '__main__':

    print(gc.get_threshold())
    main()
