import os
from os.path import exists

# file = 'my_first_file.txt'
#
# try:
#     os.remove(file)
# except FileNotFoundError:
#     print('File already deleted!')

#---------------------------

file_path = './my_first_file.txt'

if exists(file_path):
    os.remove(file_path)
else:
    print('File already deleted!')