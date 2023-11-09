A1 = ['5', '10', 'py']
A2 = ['510', 'Python', 'Java']
A3 = []
for i in range(len(A1)):
    for j in range(len(A2)):
        if A2[i].find(A1[j]) != -1:
            A3.append(A1[j])
print(A3)
