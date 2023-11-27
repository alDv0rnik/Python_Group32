m, n = int(input()), int(input())
stash = tuple(input().lower() for _ in range(m))
needs = tuple(input().lower() for _ in range(n))
for i in range(n):
    if needs[i] in stash:
        print("Есть")
    else:
        print("Отсутствует")

