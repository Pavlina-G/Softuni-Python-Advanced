import os
from os.path import exists

# file = open('./my_first_file.txt', 'w')
# file.write('I just created my first file!')

#----------------------

with open('./my_first_file.txt', 'w') as file:
    file.write('I just created my first file!')

# file.close()
# file_path = './my_first_file.txt'
#
# if exists(file_path):
#     os.remove(file_path)
#
