A1=['5', '10', '33', 'py']
A2=['510', 'Python', 'Java']
print([row1 for row2 in A2 for row1 in A1 if row1 in row2])
