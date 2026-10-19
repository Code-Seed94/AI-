# # 은행 보안 클래스 코드
# class DigitalWallet:
#     def __init__(self, owner: str, initial_balance: int = 0):
#         self.owner = owner
#         self.__balance = 0
#         self.balance = initial_balance # setter 검문소를 거쳐 안전하게 초기화
#     @property
#     def balance(self) -> int:
#         return self.__balance
#     @balance.setter
#     def balance(self, amount: int) -> None:
#         if amount < 0:
#             print(f"[보안 경고] 잔액은 음수가 될 수 없습니다! (입력값: {amount}원 -> 거부됨)")
#             return
#         self.__balance = amount

#     def deposit(self, amount: int) -> str:
#         if amount <= 0:
#             return "[오류] 입금액은 0원보다 커야 합니다."
#         self.balance += amount
#         return f"[{self.owner}] {amount:,}원 입금 완료 (현재 잔액: {self.balance:,}원)"
# wallet = DigitalWallet("이코딩", 10000)
# print(wallet.deposit(5000))
# wallet.balance = -99999 # 외부에서 불법 음수 대입 시도 -> setter가 즉시 차단!
# print(f"최종 안전 잔액: {wallet.balance:,}원")
# # 실행 결과:
# # [이코딩] 5,000원 입금 완료 (현재 잔액: 15,000원)
# # [보안 경고] 잔액은 음수가 될 수 없습니다! (입력값: -99999원 -> 거부됨)
# # 최종 안전 잔액: 15,000원




# AI 모델 하이퍼파라미터 컨트롤러와 __str__ 매직 메서드

class ModelConfig:
    def __init__(self, model_name: str, learning_rate: float, epochs: int):
        self.model_name = model_name
        self.__learning_rate = 0.001
        self.learning_rate = learning_rate
        self.epochs = epochs

    @property
    def learning_rate(self) -> float:
        return self.__learning_rate

    @learning_rate.setter
    def learning_rate(self, value: float) -> None:
        if not (0.0 < value <= 1.0):
            print(
                f"[검증 경고] 비정상 학습률({value}) 감지! "
                f"기존 안전값({self.__learning_rate})을 유지합니다."
            )
            return

        self.__learning_rate = value

    def __str__(self) -> str:
        return (
            f"ModelConfig(name='{self.model_name}', "
            f"lr={self.learning_rate}, epochs={self.epochs})"
        )


cfg = ModelConfig("ResNet-50", 0.01, 30)
print(cfg)

cfg.learning_rate = 5.0  # 허용 범위(0 초과, 1.0 이하)를 벗어난 값 대입 시도
print(cfg)


# 실행 결과:
# ModelConfig(name='ResNet-50', lr=0.01, epochs=30)
# [검증 경고] 비정상 학습률(5.0) 감지! 기존 안전값(0.01)을 유지합니다.
# ModelConfig(name='ResNet-50', lr=0.01, epochs=30)





















# 아래는 주석 해석 포함 코드


# AI 모델 하이퍼파라미터 컨트롤러와 __str__ 매직 메서드
#
# 먼저 이 코드가 관리하는 정보를 알아봅시다.
#
# model_name:
#   모델의 이름입니다.
#
# learning_rate:
#   학습률입니다.
#   모델이 학습하면서 내부 값을 얼마나 크게 조정할지 정하는 값입니다.
#   걸음을 얼마나 크게 내디딜지 정하는 '보폭'처럼 생각하면 좋습니다.
#
# epochs:
#   전체 학습 데이터를 몇 차례 학습할지 정하는 값입니다.
#
# learning_rate와 epochs처럼 학습 방식을 조절하기 위해
# 사람이 정하는 설정값을 '하이퍼파라미터'라고 합니다.
#
# 이 코드는 설정을 저장하고 검사하는 예제입니다.


# 1. 모델 설정을 담을 설계도를 정의합니다.
#
# class는 관련 정보와 기능을 묶는 문법입니다.
# ModelConfig는 우리가 지은 클래스 이름입니다.
#
# 클래스가 설계도라면, 이 설계도로 만든 실제 대상은 '객체'입니다.
#
# 콜론(:) 아래에 들여쓴 코드들이 이 클래스에 속합니다.
class ModelConfig:

    # 2. 객체를 처음 만들 때 실행할 초기화 메서드입니다.
    #
    # def는 함수를 정의하는 문법입니다.
    # 클래스 안에 정의한 함수는 '메서드'라고 부릅니다.
    #
    # __init__:
    #   객체가 만들어질 때 자동으로 실행됩니다.
    #   앞뒤의 밑줄은 각각 2개입니다.
    #
    # self:
    #   지금 만들고 있는 객체 자신을 가리킵니다.
    #
    # model_name: str:
    #   모델 이름을 문자열로 전달받습니다.
    #
    # learning_rate: float:
    #   학습률을 실수로 전달받습니다.
    #   float는 0.01처럼 소수점을 포함할 수 있는 숫자 자료형입니다.
    #
    # epochs: int:
    #   학습 반복 횟수를 정수로 전달받습니다.
    #
    # : str, : float, : int는 '타입 힌트'입니다.
    # 기대하는 값의 종류를 알려 주며, 자동으로 입력값을 검사하지는 않습니다.
    #
    # 세 매개변수에 기본값이 없으므로 객체를 만들 때 모두 전달해야 합니다.
    def __init__(self, model_name: str, learning_rate: float, epochs: int):

        # =는 오른쪽 값을 왼쪽에 저장하는 '대입' 기호입니다.
        #
        # 오른쪽 model_name:
        #   호출할 때 전달받은 이름입니다.
        #
        # 왼쪽 self.model_name:
        #   이 객체가 계속 가지고 있을 이름 정보입니다.
        #
        # 이렇게 객체에 저장하는 정보를 '속성'이라고 부릅니다.
        self.model_name = model_name

        # 실제 학습률을 보관할 내부 속성을 먼저 만듭니다.
        # 우선 0.001을 저장해 둡니다.
        #
        # __learning_rate처럼 앞에 밑줄이 2개 붙으면
        # 파이썬은 이름을 내부적으로 바꾸어 관리합니다.
        # 이 동작을 '이름 맹글링'이라고 합니다.
        #
        # 내부 속성을 실수로 건드리는 일을 줄이는 장치이며,
        # 외부 접근을 완전히 차단하는 보안 기능은 아닙니다.
        #
        # 0.001은 내부에 먼저 넣어 두는 값입니다.
        # learning_rate 매개변수의 기본값을 정한 것은 아닙니다.
        self.__learning_rate = 0.001

        # 전달받은 학습률을 설정합니다.
        #
        # 여기서는 self.__learning_rate가 아닌
        # self.learning_rate에 값을 대입했습니다.
        #
        # 아래에서 learning_rate에 setter를 연결했으므로
        # 이 대입은 setter를 자동으로 실행합니다.
        #
        # 입력이 허용 범위라면 그 값으로 변경하고,
        # 범위를 벗어나면 기존 값 0.001을 유지합니다.
        self.learning_rate = learning_rate

        # 전달받은 학습 반복 횟수를 객체에 저장합니다.
        self.epochs = epochs

    # 3. 학습률을 '읽을 때' 실행할 메서드를 정의합니다.
    #
    # @로 시작하는 문법을 '데코레이터'라고 합니다.
    # 바로 아래 메서드에 특별한 사용 방식을 연결합니다.
    #
    # @property를 붙이면 괄호 없이 속성처럼 읽을 수 있습니다.
    #
    # 사용 예:
    #   cfg.learning_rate
    #
    # 이렇게 값을 읽어 주는 역할을 'getter'라고 부릅니다.
    @property
    def learning_rate(self) -> float:

        # -> float는 실수 값을 반환한다는 타입 힌트입니다.
        #
        # return은 결과를 호출한 곳에 돌려주고 메서드를 끝냅니다.
        # 여기서는 내부에 저장된 현재 학습률을 반환합니다.
        return self.__learning_rate

    # 4. 학습률을 '변경할 때' 실행할 메서드를 정의합니다.
    #
    # @learning_rate.setter는 위에서 만든 learning_rate 속성에
    # 값을 대입할 때 사용할 메서드를 연결합니다.
    #
    # 사용 예:
    #   cfg.learning_rate = 0.05
    #
    # 이때 오른쪽 값 0.05가 아래의 value로 전달됩니다.
    #
    # getter와 같은 이름을 사용하는 이유는
    # 하나의 속성에 읽기와 변경 규칙을 함께 연결하기 위해서입니다.
    @learning_rate.setter
    def learning_rate(self, value: float) -> None:

        # value는 새로 설정하려는 학습률입니다.
        #
        # -> None은 유용한 결과값을 반환하지 않는다는 타입 힌트입니다.
        # 이 메서드의 목적은 입력값을 검사하고 학습률을 변경하는 것입니다.

        # 5. 새 학습률이 허용 범위에 들어가는지 검사합니다.
        #
        # 괄호 안부터 읽어 봅시다.
        #
        #   0.0 < value <= 1.0
        #
        # 다음 두 조건을 모두 만족해야 참입니다.
        #
        #   ① value가 0.0보다 크다.
        #   ② value가 1.0보다 작거나 같다.
        #
        # 예:
        #   value가 0.01 → 참
        #   value가 1.0  → 참
        #   value가 0.0  → 거짓
        #   value가 5.0  → 거짓
        #
        # not은 참과 거짓을 뒤집습니다.
        # 따라서 전체 조건은 '허용 범위에 들어가지 않는다면'입니다.
        #
        # 이 범위는 이 예제에서 정한 검사 규칙입니다.
        # 모든 AI 모델의 학습률에 공통으로 적용되는 절대 규칙은 아닙니다.
        if not (0.0 < value <= 1.0):

            # 조건이 참이면 경고를 출력합니다.
            #
            # print는 괄호 안의 내용을 화면에 출력합니다.
            # 괄호 안에서는 긴 코드를 여러 줄로 나누어 적을 수 있습니다.
            print(

                # f"..."는 문자열 안에 실제 값을 넣는 문법입니다.
                # {value} 자리에 설정하려던 학습률이 들어갑니다.
                #
                # 끝의 공백은 다음 문장과 한 칸 띄우기 위한 것입니다.
                f"[검증 경고] 비정상 학습률({value}) 감지! "

                # 현재 저장된 학습률을 안내문에 넣습니다.
                #
                # 나란히 적은 두 문자열은 자동으로 이어 붙습니다.
                # 코드가 두 줄이어도 화면에는 한 문장으로 출력됩니다.
                f"기존 안전값({self.__learning_rate})을 유지합니다."
            )

            # setter를 여기서 끝냅니다.
            # 값을 적지 않은 return은 None을 반환합니다.
            #
            # 아래의 저장 코드는 실행되지 않으므로
            # 기존 학습률이 그대로 유지됩니다.
            return

        # 6. 이 줄까지 왔다면 허용 범위 검사에 통과한 것입니다.
        # 새 값을 실제 학습률 저장 공간에 넣습니다.
        #
        # 여기서 self.learning_rate = value라고 쓰면
        # 같은 setter를 다시 호출하게 됩니다.
        # 따라서 실제 저장은 self.__learning_rate에 직접 합니다.
        self.__learning_rate = value

    # 7. 객체를 사람이 읽기 좋은 문자열로 표현하는 방법을 정의합니다.
    #
    # __str__은 파이썬이 특별한 상황에서 사용하는 메서드입니다.
    # 이런 메서드를 '매직 메서드' 또는 '던더 메서드'라고 부릅니다.
    #
    # 대표적으로 다음 상황에서 사용됩니다.
    #
    #   print(cfg)
    #   str(cfg)
    #
    # __str__은 반드시 문자열을 반환해야 합니다.
    # 이 안에서 print만 하고 끝내면 필요한 문자열을 반환하지 못합니다.
    def __str__(self) -> str:

        # 괄호는 긴 문자열 표현식을 여러 줄로 나누기 위해 사용했습니다.
        return (

            # 모델 이름을 문자열에 넣습니다.
            #
            # 작은따옴표와 쉼표도 화면에 그대로 표시되는 문자입니다.
            # 마지막 공백은 다음 내용과 띄어 쓰기 위한 것입니다.
            f"ModelConfig(name='{self.model_name}', "

            # lr은 learning rate를 줄여서 표시한 이름입니다.
            #
            # self.learning_rate를 읽을 때 getter가 실행됩니다.
            # self.epochs에는 저장된 학습 반복 횟수가 들어 있습니다.
            #
            # 위 문자열과 이어 붙여 하나의 문자열을 반환합니다.
            f"lr={self.learning_rate}, epochs={self.epochs})"
        )


# 8. 모델 설정 객체를 만듭니다.
#
# "ResNet-50" → __init__의 model_name
# 0.01        → __init__의 learning_rate
# 30          → __init__의 epochs
#
# self에 해당하는 객체는 파이썬이 자동으로 전달합니다.
# 만들어진 객체를 cfg라는 변수로 가리키게 합니다.
#
# 초기화 과정:
#   ① 모델 이름을 "ResNet-50"으로 저장합니다.
#   ② 내부 학습률을 우선 0.001로 저장합니다.
#   ③ self.learning_rate = 0.01로 setter를 실행합니다.
#   ④ 0.01은 허용 범위이므로 내부 학습률을 0.01로 변경합니다.
#   ⑤ epochs에 30을 저장합니다.
cfg = ModelConfig("ResNet-50", 0.01, 30)


# 9. 현재 설정을 출력합니다.
#
# cfg는 문자열이 아니라 ModelConfig 객체입니다.
# print는 객체를 문자열로 표현하기 위해 __str__을 사용합니다.
#
# __str__이 반환한 문자열:
#   ModelConfig(name='ResNet-50', lr=0.01, epochs=30)
#
# 그 문자열을 print가 화면에 출력합니다.
print(cfg)


# 10. 학습률을 5.0으로 변경하려고 시도합니다.
#
# learning_rate에 값을 대입하므로 setter가 자동으로 실행됩니다.
# value에는 5.0이 전달됩니다.
#
# 조건 계산:
#   0.0 < 5.0 <= 1.0 → 거짓
#   not 거짓          → 참
#
# 따라서 경고를 출력하고 return합니다.
# 실제 학습률을 변경하는 코드는 실행되지 않습니다.
#
# 유지되는 값은 변경 직전의 학습률인 0.01입니다.
# 초기 준비값이었던 0.001로 되돌리는 것은 아닙니다.
cfg.learning_rate = 5.0


# 11. 현재 설정을 다시 출력합니다.
#
# __str__이 다시 사용됩니다.
# 변경 요청이 거절되었으므로 학습률은 여전히 0.01입니다.
print(cfg)


# 실행 결과:
#
# ModelConfig(name='ResNet-50', lr=0.01, epochs=30)
# [검증 경고] 비정상 학습률(5.0) 감지! 기존 안전값(0.01)을 유지합니다.
# ModelConfig(name='ResNet-50', lr=0.01, epochs=30)
#
#
# 마지막으로 실행 흐름을 연결해 봅시다.
#
# ModelConfig(...)
#   → __init__이 실행되어 초기 정보를 준비합니다.
#
# cfg.learning_rate
#   → getter가 실행되어 현재 학습률을 반환합니다.
#
# cfg.learning_rate = 새값
#   → setter가 실행되어 검사 후 저장하거나 거절합니다.
#
# print(cfg)
#   → __str__이 만든 문자열을 화면에 출력합니다.





























# # 멀티모달 AI 모델 통합 추론 파이프라인

# class BaseAIModel:
#     def __init__(self, name: str, version: str):
#         self.name = name
#         self.version = version

#     def predict(self, input_data: str) -> str:
#         return f"[{self.name} v{self.version}] 기본 추론: {input_data}"


# class VisionClassifier(BaseAIModel): # 클래스 자식(부모)
#     def __init__(self, name: str, version: str, resolution: str):
#         super().__init__(name, version)  # 부모 초기화 코드 재사용
#         self.resolution = resolution

#     def predict(self, input_data: str) -> str:  # 다형성 오버라이딩
#         return (
#             f"[Vision {self.name} ({self.resolution})] "
#             f"이미지 '{input_data}' 분석 결과 -> '고양이 (확률 98.4%)'"
#         )


# class TextSummarizerLLM(BaseAIModel):
#     def __init__(self, name: str, version: str, max_tokens: int):
#         super().__init__(name, version)
#         self.max_tokens = max_tokens

#     def predict(self, input_data: str) -> str:  # 다형성 오버라이딩
#         summary = input_data[:18] + "..." if len(input_data) > 18 else input_data
#         return (
#             f"[LLM {self.name} (max={self.max_tokens})] "
#             f"텍스트 요약 결과 -> '{summary}'"
# )
# pipeline = [BaseAIModel]('base','1,0'),VisionClassifier('vision','1,0','1024'), TextSummarizerLLM('textsumarizer','1,0')
# for obj in pipeline:
#     print(obj.predict('테스트'))

# # 다형성의 위력: 서로 다른 모델 클래스들을 단일 for 루프로 일괄 실행!
# pipeline: list[BaseAIModel] = [
#     VisionClassifier("YOLO-KDT", "8.2", "640x640"),
#     TextSummarizerLLM("Codex-Mini", "2.0", 512),
# ]

# for model in pipeline:
#     print(model.predict("실습 데이터 샘플 입력입니다"))


# 실행 결과:
# [Vision YOLO-KDT (640x640)] 이미지 '실습 데이터 샘플 입력입니다' 분석 결과 -> '고양이 (확률 98.4%)'
# [LLM Codex-Mini (max=512)] 텍스트 요약 결과 -> '실습 데이터 샘플 입력입니다'