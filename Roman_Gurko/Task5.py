def get_shorty(x):
    """
    :param x: string with spaces
    :return: minimal length of word in x-string
    """
    lens = list(map(lambda y: len(y), x.split()))
    d = {k: v for k, v in zip(x.split(), lens)}
    return min(d.values())


print(get_shorty(input()))
