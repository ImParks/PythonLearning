
#총 10칸의 문자가 되고 왼쪽정렬로 문자가 나옴
a = "{0:<10}".format("hi")
print(a)
#오른쪽으로 문자가 나옴
a = "{0:>10}".format("hi")
print(a)
# 캐럿 문자를 사용하면 가운대 정렬이 된다.
a = "{0:^10}".format("hi")
print(a)