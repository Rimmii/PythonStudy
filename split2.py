import os

os.chdir('../chapter3')
a = os.getcwd()
print(a)

data = open('sketch.txt')
for each_line in data:
    (role, line_spoken) = each_line.split(':', 1)
    print(role, end='')
    print(' said:', end='')
    print(line_spoken, end='')

data.close()

#"ValueError: not enough values to unpack (expected 2, got 1)" 오류 발생
#콜론이 없는 경우를 처리하지 못함
