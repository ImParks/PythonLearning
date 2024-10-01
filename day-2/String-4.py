#문자열 포매팅

#숫자 바로 대입
# 숫자일땐 d
a = "I eat %d apples." % 3
print(a)

# 문자 바로대입
# 문자일때 s
b = "I eat %s apples." % "five"
print(b)

# 변수 대입.
number = 3
c = "I eat %d apples." % number
print(c)

#복수 변수대입
day = "three"
d = "I eat %d apples. so I was sick for %s days." % (number,day)
print(d)

# 문자열 포맷 코드
# %s : 문자열
# %c : 문자열 1개
# %d : 정수
# %f : 부동소수
# %o : 8진수
# %x : 16진수
# %% : Literal%(문자 % 자체)

#팁 : %s 만 사용해도어떤 형태의 값이든 변환하여 집어넣기 가능
e = "I eat %s apples. so I was sick for %s days." % (number,day)
print(e)

#포맷 코드와 숫자 함께 사용하기

#문자열 전체 길이가 %10s <- 이 걸로인해 10칸으로 정해짐
#문자가 뒤로 오고 전체 길이가 10칸
f = "%10s" %"hi"
print(f)
#문자가 앞으로오고 전체 길이가 10칸
g = "%-10s" %"hi"
print(g)