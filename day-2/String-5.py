#.format 이라는 방법으로도 포매팅 가능.
# 문자열안 괄호는 index 값이다.
a = "I eat {0} apples".format(3)
print(a)
# .format으로 복수 포매팅
number = 3
day = "three"
b = "I eat {0} apples. so I was sick for {1} days.".format(number,day)
print(b)

# 변수명으로 포매팅 fromat 안에서 변수 지정
c = "I eat {number} apples. so I was sick for {day} days.".format(number=10,day=3)
print(c) 

# index 포매팅과 변수명으로 하는 포매팅 혼용
d = "I eat {0} apples. so I was sick for {day} days.".format(10,day=3)
print(d) 