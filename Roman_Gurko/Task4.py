def task3_topic6(x):
    c = list(map(lambda y: x.count(y), list(x)))
    d = {int(k): v for k, v in zip(x, c)}
    c = list(d.keys())
    b = list(d.values())
    d = {}
    d.update({c.pop(b.index(max(b))): b.pop(b.index(max(b)))})
    d.update({c.pop(b.index(max(b))): b.pop(b.index(max(b)))})
    d.update({c.pop(b.index(max(b))): b.pop(b.index(max(b)))})
    return d


print(task3_topic6(input()))
