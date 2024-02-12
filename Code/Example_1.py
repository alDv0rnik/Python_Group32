def concat_v1(s1, s2):
    for i in s1:
        yield i
    for j in s2:
        yield j


seq1 = range(10)
seq2 = range(10, 20)

# print(list(concat_v1(seq1, seq2)))
# print(*concat_v1(seq1, seq2))


def concat_v2(s1, s2):
    yield from s1
    yield from s2


print(*concat_v2(seq1, seq2))