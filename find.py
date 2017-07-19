each_line = "I tell you, there's no such thing as a flying circus."
each_line.find(':')

#문자열이 콜론을 갖지 않으므로 find()가 -1를 반환. :찾지못했음

each_line = "I tell you: there's no such thing as a flying circus"
each_line.find(':')

#문자열이 콜론을 갖고 있어 find()가 10을 반환 :양의 인덱스 값을 반환(?)
