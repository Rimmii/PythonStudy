import os

os.chdir('../chapter3')
a = os.getcwd()
print(a)

if os.path.exists('sketch.txt'):
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said:', end='')
            print(line_spoken, end='')
        except:
            pass

    data.close()

else:
    print('The data file is missing!')
