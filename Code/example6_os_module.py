import os


BASE_DIR = os.path.dirname(__file__)
print(os.path.dirname(__file__))
print(os.path.abspath(__file__))
print(os.path.basename(__file__))

os.mkdir(os.path.join(BASE_DIR, 'new_dir'))