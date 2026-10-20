# class BaristaBot:
#     def __init__(self, bot_name: str, bean_grams: int): # __init__ 은 생성자라고 한다 
#                                                         # 모든 객체지향 언어에는 생성자 메커니즘이 존재한다
#         self.bot_name = bot_name
#         self.bean_grams = bean_grams
#         self.total_cups = 0
#     def brew_espresso(self, cups: int = 1) -> str:
#         required_beans = cups * 18
#         if self.bean_grams < required_beans:
#             return f"[{self.bot_name}] 원두 부족! (필요: {required_beans}g, 현재:{self.bean_grams}g)"
#         self.bean_grams -= required_beans
#         self.total_cups += cups
#         return f"[{self.bot_name}] 에스프레소 {cups}잔 추출 완료! (남은 원두:{self.bean_grams}g, 누적: {self.total_cups}잔)"
# bot = BaristaBot("코덱스바리스타-1호", 50)
# print(bot.brew_espresso(2))
# print(bot.brew_espresso(2))

# # 실행 결과:
# # [코덱스바리스타-1호] 에스프레소 2잔 추출 완료! (남은 원두: 14g, 누적: 2잔)
# # [코덱스바리스타-1호] 원두 부족! (필요: 36g, 현재: 14g)

# # bot2를 추가 해서 이후에 원두가 부족하면 남은 그램수에서 뽑고 더이상 못뽑는 
# # 그램이면 그때 부족이라고 출력되되록 수정해볼 수 있음 



# 은행 보안 클래스 코드
class DigitalWallet:
    def __init__(self, owner: str, initial_balance: int = 0):
        self.owner = owner
        self.__balance = 0
        self.balance = initial_balance # setter 검문소를 거쳐 안전하게 초기화
    @property
    def balance(self) -> int:
        return self.__balance
    @balance.setter
    def balance(self, amount: int) -> None:
        if amount < 0:
            print(f"[보안 경고] 잔액은 음수가 될 수 없습니다! (입력값: {amount}원 -> 거부됨)")
            return
        self.__balance = amount

    def deposit(self, amount: int) -> str:
        if amount <= 0:
            return "[오류] 입금액은 0원보다 커야 합니다."
        self.balance += amount
        return f"[{self.owner}] {amount:,}원 입금 완료 (현재 잔액: {self.balance:,}원)"
wallet = DigitalWallet("이코딩", 10000)
print(wallet.deposit(5000))
wallet.balance = -99999 # 외부에서 불법 음수 대입 시도 -> setter가 즉시 차단!
print(f"최종 안전 잔액: {wallet.balance:,}원")
# 실행 결과:
# [이코딩] 5,000원 입금 완료 (현재 잔액: 15,000원)
# [보안 경고] 잔액은 음수가 될 수 없습니다! (입력값: -99999원 -> 거부됨)
# 최종 안전 잔액: 15,000원







# 아래는 주석 해석 포함 코드


# 은행 보안 클래스 코드
#
# 이 예제의 목표:
#   ① 소유자 이름과 잔액을 저장합니다.
#   ② 잔액을 읽을 수 있게 합니다.
#   ③ 잔액을 음수로 변경하려는 요청을 거절합니다.
#   ④ 입금하면 잔액을 늘립니다.


# 1. 전자지갑의 설계도를 정의합니다.
#
# class는 관련 데이터와 기능을 묶는 문법입니다.
# DigitalWallet은 우리가 지은 클래스 이름입니다.
#
# 이 설계도로 실제 만든 전자지갑 하나를 '객체'라고 합니다.
# 콜론(:) 아래에 들여쓴 코드들이 이 클래스에 속합니다.
class DigitalWallet:

    # 2. 객체를 처음 만들 때 실행할 초기화 메서드입니다.
    #
    # def는 함수를 정의하는 문법입니다.
    # 클래스 안에 정의한 함수는 '메서드'라고 부릅니다.
    #
    # __init__:
    #   객체가 만들어질 때 자동으로 실행됩니다.
    #
    # self:
    #   지금 다루는 전자지갑 객체 자신을 가리킵니다.
    #
    # owner: str:
    #   소유자 이름을 문자열로 전달받습니다.
    #
    # initial_balance: int = 0:
    #   초기 잔액을 정수로 전달받습니다.
    #   값을 생략하면 0을 사용합니다.
    #
    # : str과 : int는 '타입 힌트'입니다.
    # 기대하는 값의 종류를 알려 주며, 자동 검사 기능은 아닙니다.
    def __init__(self, owner: str, initial_balance: int = 0):

        # =는 오른쪽 값을 왼쪽에 저장하는 '대입' 기호입니다.
        #
        # 오른쪽 owner는 전달받은 값입니다.
        # 왼쪽 self.owner는 이 객체가 계속 가지고 있을 속성입니다.
        self.owner = owner

        # 실제 잔액을 보관할 내부 속성을 먼저 0으로 만듭니다.
        #
        # __balance처럼 앞에 밑줄이 2개 붙으면
        # 파이썬은 이름을 내부적으로 바꾸어 관리합니다.
        # 이 동작을 '이름 맹글링'이라고 합니다.
        #
        # 내부 속성을 실수로 건드리는 일을 줄여 주지만,
        # 외부 접근을 완전히 차단하는 보안 장치는 아닙니다.
        self.__balance = 0

        # 초기 잔액을 설정합니다.
        #
        # 여기서 self.balance에 대입하면
        # 아래에 정의한 setter가 자동으로 실행됩니다.
        #
        # 따라서 처음 전달받은 잔액도 음수인지 검사합니다.
        # 음수라면 변경을 거절하므로 위에서 저장한 0원이 유지됩니다.
        self.balance = initial_balance

    # 3. 잔액을 '읽을 때' 실행할 메서드를 정의합니다.
    #
    # @로 시작하는 이런 문법을 '데코레이터'라고 합니다.
    # 바로 아래 메서드에 특별한 사용 방식을 연결합니다.
    #
    # @property를 붙이면 괄호 없이 속성처럼 읽을 수 있습니다.
    #
    # 사용 예:
    #   wallet.balance
    #
    # 이렇게 값을 읽어 주는 역할을 'getter'라고 부릅니다.
    @property
    def balance(self) -> int:

        # -> int는 정수를 반환한다는 타입 힌트입니다.
        #
        # return은 값을 호출한 곳에 돌려주고 메서드를 끝냅니다.
        # 여기서는 내부에 저장된 실제 잔액을 돌려줍니다.
        return self.__balance

    # 4. 잔액을 '변경할 때' 실행할 메서드를 정의합니다.
    #
    # @balance.setter는 위의 balance 속성에
    # 값을 대입할 때 사용할 메서드를 연결합니다.
    #
    # 예:
    #   wallet.balance = 15000
    #
    # 이때 15000이 아래 메서드의 amount로 전달됩니다.
    @balance.setter
    def balance(self, amount: int) -> None:

        # amount는 새로 설정하려는 잔액입니다.
        # 기존 잔액에 더할 금액이 아니라 '변경 후의 전체 잔액'입니다.
        #
        # -> None은 유용한 결과값을 반환하지 않는다는 타입 힌트입니다.

        # if는 조건문입니다.
        # <는 왼쪽 값이 오른쪽 값보다 작은지 비교합니다.
        #
        # 즉, '새 잔액이 0보다 작다면'이라는 뜻입니다.
        if amount < 0:

            # print는 괄호 안의 내용을 화면에 출력합니다.
            #
            # f"..."는 문자열 안에 실제 값을 넣는 문법입니다.
            # {amount} 자리에 설정하려던 금액이 들어갑니다.
            print(f"[보안 경고] 잔액은 음수가 될 수 없습니다! (입력값: {amount}원 -> 거부됨)")

            # 값을 적지 않은 return은 None을 반환하며 메서드를 끝냅니다.
            #
            # 여기서 끝내므로 아래의 잔액 저장 코드는 실행되지 않습니다.
            # 따라서 기존 잔액이 유지됩니다.
            return

        # 이 줄까지 왔다면 새 잔액이 음수가 아니라는 뜻입니다.
        # 검사에 통과한 값을 실제 저장 공간에 넣습니다.
        #
        # 여기서 self.balance = amount라고 쓰면
        # 같은 setter를 다시 호출하게 됩니다.
        # 따라서 실제 저장은 self.__balance에 직접 합니다.
        self.__balance = amount

    # 5. 입금 기능을 정의합니다.
    #
    # deposit은 '입금하다'라는 뜻으로 지은 이름입니다.
    # 여기의 amount는 이번에 입금할 금액입니다.
    #
    # -> str은 결과 안내문을 문자열로 반환한다는 뜻입니다.
    def deposit(self, amount: int) -> str:

        # <=는 '작거나 같다'는 비교 기호입니다.
        # 입금액이 0원이거나 음수이면 잘못된 요청으로 처리합니다.
        if amount <= 0:

            # 오류 안내문을 반환하고 메서드를 끝냅니다.
            # 이 경우 아래의 잔액 변경 코드는 실행되지 않습니다.
            #
            # return 자체는 화면에 출력하지 않습니다.
            return "[오류] 입금액은 0원보다 커야 합니다."

        # 6. 현재 잔액에 입금액을 더합니다.
        #
        # +=는 기존 값에 오른쪽 값을 더해서 다시 저장하는 문법입니다.
        #
        # 이 코드에서는 다음처럼 풀어 생각할 수 있습니다.
        # self.balance = self.balance + amount
        #
        # balance에는 getter와 setter가 연결되어 있으므로:
        #
        #   ① getter로 현재 잔액을 읽습니다.
        #   ② 읽은 잔액에 입금액을 더합니다.
        #   ③ 계산 결과를 setter에 전달합니다.
        #   ④ setter가 검사한 뒤 실제 잔액을 변경합니다.
        #
        # 예:
        #   현재 잔액 10000 + 입금액 5000 = 새 잔액 15000
        self.balance += amount

        # 7. 입금 완료 안내문을 반환합니다.
        #
        # {self.owner}에는 소유자 이름이 들어갑니다.
        #
        # {amount:,}의 :,는 천 단위 쉼표를 표시하는 형식입니다.
        # 예: 5000 → "5,000"
        #
        # {self.balance:,}는 getter로 잔액을 읽고 쉼표를 붙여 표시합니다.
        # 표시 형식이 바뀌어도 실제 저장된 숫자 자체는 그대로입니다.
        return f"[{self.owner}] {amount:,}원 입금 완료 (현재 잔액: {self.balance:,}원)"


# 8. 이름이 "이코딩"이고 초기 잔액이 10000원인 지갑을 만듭니다.
#
# "이코딩" → __init__의 owner
# 10000    → __init__의 initial_balance
#
# self에 해당하는 객체는 파이썬이 자동으로 전달합니다.
# 생성된 객체를 wallet이라는 변수로 가리키게 합니다.
#
# 초기 잔액 10000원도 setter의 검사를 통과한 뒤 저장됩니다.
wallet = DigitalWallet("이코딩", 10000)


# 9. 5000원을 입금하고 반환된 안내문을 출력합니다.
#
# 안쪽의 wallet.deposit(5000)이 먼저 실행됩니다.
# 잔액이 15000원으로 바뀌고, 완료 안내문이 반환됩니다.
# 바깥쪽 print가 그 안내문을 화면에 출력합니다.
print(wallet.deposit(5000))


# 10. 잔액을 -99999원으로 바꾸려고 시도합니다.
#
# balance에 대입하므로 setter가 실행됩니다.
# setter가 음수를 발견하면 경고를 출력하고 return합니다.
#
# 실제 저장 코드는 실행되지 않으므로 잔액은 15000원으로 유지됩니다.
wallet.balance = -99999


# 11. 최종 잔액을 읽어서 출력합니다.
#
# wallet.balance를 읽을 때 getter가 실행됩니다.
# 반환된 15000을 :, 형식으로 "15,000"으로 표시합니다.
print(f"최종 안전 잔액: {wallet.balance:,}원")


# 실행 결과:
#
# [이코딩] 5,000원 입금 완료 (현재 잔액: 15,000원)
# [보안 경고] 잔액은 음수가 될 수 없습니다! (입력값: -99999원 -> 거부됨)
# 최종 안전 잔액: 15,000원