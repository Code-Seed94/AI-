# # 8교시 시작
# # 디버깅 : 기준 줄을 선택 후  실행 버튼 옆 아래 화살표 클릭 -> 
# # Python Debugger: Debug Python File 클릭 후 노란색 시작 줄 나오면 f11로 한줄 씩 실행하여 결과 확인
# # 실제로 어떻게 진행되는 지 직적 확인하며 이해할 수 있음

import random
ages = random.sample(range(10,50),10) # 10부터 50까지 10개 랜덤 생성
results = [] # 이후에 채워질 빈 리스트
for i in ages:
    if i>= 20:
        results.append('성인')
    else:
        results.append('미성년자')

print(results)

# 리스에서 불량을 모두 지우고 정상만 남도록 하기
items = ['정상','불량','불량','정상']
for item in items: # 불량이 모두 지워지지 않는 오류 발생
# for item in items[:]: # 슬라이스로 데이터 복사하여 문제 해결
      if item == '불량':
          items.remove('불량')

print(f'검수 결과 : {items}')


# 8교시 종료