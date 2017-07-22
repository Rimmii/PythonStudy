import pickle
import sys
import os

os.chdir('../chapter3')
a = os.getcwd()
print(a)

def print_lol(the_list, indent = False, level = 0, fh = sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end = '', file = fh)
            print(each_item, file = fh)

man = []
other = []

try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)

        except ValueError:
            pass

    data.close()

except IOError:
    print('The data file is missing!')

new_man = []

try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)

except IOError as err:
    print('File error: ' + str(err))

except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))


print_lol(new_man)
print(new_man[0])
print(new_man[-1])
