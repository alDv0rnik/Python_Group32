A1 = ['5', '10', 'py']
A2 = ['510', 'Python', 'Java']
A3 = []
for elem in range(len(A1)):
    for elem1 in range(len(A2)):
        if A2[elem].find(A1[elem1]) != -1:
            A3.append(A1[elem1])
print(A3)
