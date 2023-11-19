# Task 7
m, n = [int(input()) for _ in 'mn']
tort = {input().lower() for _ in range(m)}
[print("Есть" if input().lower() in tort else "Отсутствует") for _ in range(n)]
