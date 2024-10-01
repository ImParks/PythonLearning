
#총 10칸의 문자가 되고 왼쪽정렬로 문자가 나옴
a = "{0:<10}".format("hi")
print(a)
#오른쪽으로 문자가 나옴
a = "{0:>10}".format("hi")
print(a)
# 캐럿 문자를 사용하면 가운대 정렬이 된다.
a = "{0:^10}".format("hi")
print(a)

#총 10글자로 만들때 빈칸을 = 로 채운다, 다른 문자열로 작성해도됨.
a = "{0:=^10}".format("hi")
print(a)

# 소숫점 표현 
y = 3.42134234
#0.4f <- 소숫점 4자리 까지 출력
a = "{0:0.4f}".format(y)
print(a)

#중괄호 표현
a = "{{ and }}".format()
print(a)

#f 문자열 포매팅
name = '홍길동'
age = 30
a = f'나의 이름은 {name}입니다. 나는 {age}입니다.'
print(a)