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
d = "I eat %d apples. so   I was sick for %s days." % (number,day)
print(d)

# 문자열 포맷 코드
# %s : 문자열
# %c : 문자열 1개
# %d : 정수
# %f : 부동소수
# %o : 8진수
# %x : 16진수
# %% : Literal%(문자 % 자체)