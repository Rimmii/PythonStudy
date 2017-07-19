import os

os.chdir('../chapter3')
a = os.getcwd()
print(a)

data = open('sketch.txt')
print(data.readline(), end='')

data.seek(0)
for each_line in data:
    print(each_line, end='')

data.close()
