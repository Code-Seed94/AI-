# 7교시 시작

# # 리스트 컴프리핸션 : 반복과 조건을 이용해 새로운 리스트를 한 줄로 간단히 만드는 문법
list_1 = [1,2,3,4,5]

# for i in list_1:
#     if i %2 == 0:
#         result.append(i)

result = [i for i in list_1 if i % 2 == 0] # 위에 3줄을 한줄로 축약

print(result)


ages = [20,15,60,25,30,45,5]
print( [ i for i in ages if i >=20 ])
print(['성인' if i >=20 else '미성년' for i in ages])

# 빈 문자열은 거짓 나머지는 트루
# set()

num = (1,2,3,4,5,6,7,8,1,2,3,4,5)
print(set(num))


# # 람다는 이름 없는 함수, def 없이 사용 가능하다

# # gpt로 만든 코드를 해석하는 시간을 가졌다

# 7교시 종료


