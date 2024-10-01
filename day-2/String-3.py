#문자열 길이 구하기
a = "Life is too short"
# 문자열이 리턴됨
len(a) 
print(len(a))

#문자열 인덱싱과 슬라이싱

#문자열 인덱싱
a = "Life is too short, You need Python"
print(a[3])
# 특정 index 값에 있는 문자를 가져온다.
# index 값은 0부터 시작
print(a[0])
print(a[12])
# 음수 일때는 뒤에서 시작
print(a[-1])

#index가 범위를 벗어날때 오류가남

#문자열 슬라이싱 
# 범위를 ~이상부터:~미만까지 로 정할수있음
print(a[0:4])
# ~이상부터 끝까지를 원할땐 비워두기
print(a[19:])
# ~이상부터 : ~미만까지 : ~간격으로 라는뜻. 2칸씩 읽어줌
print(a[::2])
# 간격이 음수일때는 역으로 읽어줌
print(a[::-1])
# ~미만까지를 음수로 둘수도 있음.
print(a[19:-5])