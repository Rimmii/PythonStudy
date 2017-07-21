try:
    data = open('missing.txt')
    print(data.readline(), end='')

except IOError:
    print('File error')

finally:
    if 'data' in locals():
        data.close()

#File error 출력
