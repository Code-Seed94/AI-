# 4교시 시작 
# gpt로 이후 코드 작성 요청했음 

# test_users는 딕셔너리 여러 개를 담은 "리스트"
# "리스트" 에서 딕셔너리를 하나씩 꺼내 user에 넣습니다.

for user in test_users: # test_users의 key, value를 user로 할당
    username = user["username"] # user는 딕셔너리 타입이 되었고, 그 중 key인 ["username"]을 username이라는 변수에 할당
    role = user["user_role"] # user는 딕셔너리 타입이 되었고, 그 중 key인 ["user_role"]을 role이라는 변수에 할당
    suspended = user["is_suspended"] # user는 딕셔너리 타입이 되었고, 그 중 key인 ["is_suspended"]을 suspended라는 변수에 할당

# 즉, user에 할당된 각 쌍으로 된 딕셔너리 deta에서 해당하는 각 key ["username"],["user_role"], ["is_suspended"]를 
# username, role, suspended라는 변수에 할당

    if suspended: # suspended가 True인지 확인
        print(f"{username}: 정지된 계정입니다.") # username 변수와 정지 안내 메시지를 한 줄로 출력
        continue # 현재 사용자 검사를 종료하고 다음 user의 반복으로 이동

    message = role_messages.get( # role_messages 딕셔너리에서 역할에 해당하는 메시지를 가져와 message 변수에 할당
        role, # role 변수의 값을 role_messages에서 찾을 key로 사용
        "[오류] 알 수 없는 계정입니다." # role에 해당하는 key가 없을 경우 사용할 기본 메시지
    ) # get 메서드 호출을 종료

    print(f"{username}: {message}")  # username과 역할에 맞는 message를 한 줄로 출력


# suspended가 True이면 정지된 계정이라는 메시지를 출력하고 다음 사용자로 넘어감
# suspended가 False이면 role_messages에서 role에 맞는 권한 메시지를 찾음
# role이 role_messages에 없으면 "[오류] 알 수 없는 계정입니다."를 message에 할당
# 마지막으로 username과 message를 한 줄로 출력



# 브레이크 반대 컨티뉴 
# 컨티뉴 있는 문장은 무시하고 일단 진행
# continus
# continus의 예제
list_a = [1,2,3,4,5,6,7,8,9,10]

for i in list_a:    # list_a의 값을 하나씩 꺼내 i 변수에 할당하며 순환
    if i % 2 == 0:  # i % 2 == 0은 i를 2로 나눈 나머지가 0이므로 짝수인지 확인하는 조건 
                    # 짝 수면 아래 print(i)를 실행하지 않고 다음 숫자로 이동
    # if i % 2 != 0:# i를 2로 나눈 나머지가 0이 아닐때 즉, 홀 수 일때 Ture

    # if i == 5:    # 순환을 계속 5만 제외하고 출력 

        continue    # 조건이 해당하면 현재 회차의 print(i)를 건너뛰고 
                    # 리스트 안에 담긴 다음 숫자로 이동 즉, 처음으로 돌아가서 재시작
    print(i)        # continue에 해당하지 않은 조건의 수만 출력

# continue는 값이 맞는 것을 확인 혹은 아닌 것을 확인해라 라는 조건일 때 
# 그 조건에 해당하면 처음으로 돌아가는 것 즉, 그 아래 줄은 계산하지 않는 것이다


# 4교시 종료





# 점심 시간





