import os

print(os.path.abspath(__file__))
print(os.path.basename(__file__))
print(os.path.dirname(__file__))
# print(os.system('dir'))
print(os.mkdir(os.path.join(os.path.dirname(__file__), 'new_dir')))