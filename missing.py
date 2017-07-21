try:
    data = open('missing.txt')
    print(data.readline(), end='')

except IOError:
    print('File error')

finally:
    data.close()

#NameError: name 'data' is not defined
#파일이 존재하지 않아 data 파일 객체가 만들어지지 않음. 따라서 close()매서드 호출이 불가능.
