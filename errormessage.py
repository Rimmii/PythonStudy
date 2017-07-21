try:
    data = open('missing.txt')
    print(data.readline(), end='')

except IOError as err:
    print('File error: ' + str(err))

finally:
    if 'data' in locals():
        data.close()

#File error: [Errno 2] No such file or directory: 'missing.txt' 출력
