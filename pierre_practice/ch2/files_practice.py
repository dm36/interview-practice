import os

# open test.txt
cwd = (os.getcwd())
path_to_file = cwd + '/pierre_practice/test.txt'
my_file = open(path_to_file)
print (my_file)
  
# read the file
print (my_file.read())

# seek to the beginning of the file, read the file again
my_file.seek(0)
print (my_file.readlines())

# close the file
my_file.close()

# write to a file
my_file = open(path_to_file, 'w+')
my_file.write('This is a new line')

# seek to the beginning of the file and read
my_file.seek(0)
print (my_file.readlines())

# open test.txt and append new new line
my_file = open(path_to_file, 'a+')
my_file.write('New new line')

# seek to the beginning of the file and read
my_file.seek(0)
print (my_file.readlines())

my_file.seek(0)
for line in open(path_to_file):
    print (line)
