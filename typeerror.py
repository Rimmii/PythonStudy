try:
    data = open('missing.txt')
    print(data.readline(), end='')

except IOError as err:
    print('File error: ' + err)

finally:
    if 'data' in locals():
        data.close()

#TypeError: must be str, not FileNotFoundError 발생
