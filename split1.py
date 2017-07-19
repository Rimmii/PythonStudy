import os

os.chdir('../chapter3')
a = os.getcwd()
print(a)

data = open('sketch.txt')
for each_line in data:
    (role, line_spoken) = each_line.split(':')
    print(role, end='')
    print(' said:', end='')
    print(line_spoken, end='')

#이렇게 했을 시, "ValueError: too many values to unpack (expected 2)" 발생
#콜론이 이중으로 나오는 경우를 처리하지 못함
