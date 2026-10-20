# names = ['홍길동','이순신','강감찬']

# id = 1
# for name in nemes:
#     print(f'{id}.{name}')
#     id += 1


# for name in enumerate(names,start=1): # enumerate 를 설명하기 위해 위의 코드 작성/
#                                       # 원래는 0부터인데 1부터 시작하고자 스타트 1을 함
#     print(name)



# test_str = "epoch=1,loss=0.45,acc=88.5"
# print(test_str.split(',')) # 공백 넣으면 공백 콤마는 콤마 반환








# 깨진 로그 라인을 격리하고 완주하는 무중단 AI 학습 로그 파서

raw_logs = [
    "epoch=1,loss=0.45,acc=88.5",
    "epoch=2,loss=invalid,acc=91.0",  # ValueError 발생: 'invalid'는 float 변환 불가
    "epoch=3,loss=0.31",             # KeyError 발생: 'acc' 키 누락
    "epoch=4,loss=0.22,acc=94.2",
]


def parse_training_logs(logs: list[str]) -> list[dict]:
    valid_records = []

    for idx, line in enumerate(logs, start=1):
        try:
            parts = dict(item.split("=") for item in line.split(","))

            record = {
                "epoch": int(parts["epoch"]),
                "loss": float(parts["loss"]),
                "acc": float(parts["acc"]),
            }

        except ValueError as e:
            print(
                f"[Line {idx} 변환 오류] "
                f"숫자 형식이 아닙니다: '{line}' ({e})"
            )

        except KeyError as e:
            print(
                f"[Line {idx} 필드 누락] "
                f"필수 키 {e} 가 없습니다: '{line}'"
            )

        else:
            valid_records.append(record)
            print(
                f"[Line {idx} 정상 수집] "
                f"Epoch {record['epoch']} -> Accuracy: {record['acc']}%"
            )

        finally:
            pass  # 각 라인 검사 완료 후 스트림 상태 점검 위치

    print(
        f"[파서 종료] 총 {len(logs)}건 중 "
        f"{len(valid_records)}건 정상 로드 완료."
    )

    return valid_records


parsed = parse_training_logs(raw_logs)


# 실행 결과:
# [Line 1 정상 수집] Epoch 1 -> Accuracy: 88.5%
# [Line 2 변환 오류] 숫자 형식이 아닙니다: 'epoch=2,loss=invalid,acc=91.0' (could not convert string to float: 'invalid')
# [Line 3 필드 누락] 필수 키 'acc' 가 없습니다: 'epoch=3,loss=0.31'
# [Line 4 정상 수집] Epoch 4 -> Accuracy: 94.2%
# [파서 종료] 총 4건 중 2건 정상 로드 완료.















# 아래는 주석 해석 포함 코드


# 깨진 로그 라인을 격리하고 완주하는 AI 학습 로그 파서
#
# 로그(log):
#   프로그램이 실행되면서 남긴 기록입니다.
#
# 파서(parser):
#   일정한 형식의 데이터를 읽고, 필요한 정보를 구분하여 정리하는 코드입니다.
#
# 이 프로그램은 문자열로 된 학습 기록을 읽어서
# 숫자 데이터가 담긴 딕셔너리로 바꿉니다.
#
# 처리에 성공한 기록만 결과 리스트에 저장하고,
# ValueError 또는 KeyError가 발생한 기록은 안내문을 출력한 뒤 건너뜁니다.


# 1. 처리할 원본 로그들을 리스트에 담습니다.
#
# raw_logs는 우리가 지은 변수 이름입니다.
# raw는 여기서 '아직 가공하지 않은 원본'이라는 뜻으로 사용했습니다.
#
# 대괄호 []는 리스트를 만드는 문법입니다.
# 리스트에는 여러 항목을 순서대로 담을 수 있습니다.
#
# 각 항목은 따옴표로 감싼 문자열입니다.
raw_logs = [

    # 정상 로그입니다.
    #
    # epoch → 전체 학습 데이터를 몇 번째 학습 중인지 나타내는 값
    # loss  → 모델의 예측 오차를 수치로 나타낸 값
    # acc   → accuracy의 줄임말로, 여기서는 정확도(%)를 뜻합니다.
    #
    # 주의:
    # 지금은 줄 전체가 하나의 문자열입니다.
    # 안에 있는 1, 0.45, 88.5도 아직 숫자로 분리된 상태가 아닙니다.
    "epoch=1,loss=0.45,acc=88.5",

    # loss 자리에 숫자 대신 invalid라는 글자가 들어 있습니다.
    # 나중에 float("invalid")를 실행하면 ValueError가 발생합니다.
    "epoch=2,loss=invalid,acc=91.0",

    # epoch와 loss는 있지만 acc가 없습니다.
    # 나중에 딕셔너리에서 acc를 찾으려고 하면 KeyError가 발생합니다.
    "epoch=3,loss=0.31",

    # 정상 로그입니다.
    # 앞선 로그들에 오류가 있어도 이 줄까지 처리하는 것이 목표입니다.
    "epoch=4,loss=0.22,acc=94.2",
]


# 2. 로그를 처리하는 함수를 정의합니다.
#
# def는 함수를 정의하는 문법입니다.
# parse_training_logs는 우리가 지은 함수 이름입니다.
#
# logs:
#   함수를 호출할 때 전달받을 데이터를 가리키는 매개변수입니다.
#
# : list[str]:
#   문자열들을 담은 리스트를 기대한다는 타입 힌트입니다.
#
# -> list[dict]:
#   딕셔너리들을 담은 리스트를 반환한다는 타입 힌트입니다.
#
# 타입 힌트 자체가 입력값이나 반환값을 자동으로 검사하지는 않습니다.
#
# 콜론(:) 아래에 들여쓴 코드들이 함수에 속합니다.
def parse_training_logs(logs: list[str]) -> list[dict]:

    # 3. 정상적으로 처리한 기록을 담을 빈 리스트를 만듭니다.
    #
    # valid는 '유효한', records는 '기록들'이라는 뜻입니다.
    # 처음에는 성공한 기록이 없으므로 []로 시작합니다.
    valid_records = []

    # 4. 로그를 한 줄씩 꺼내서 처리합니다.
    #
    # for는 반복문입니다.
    # logs의 항목들을 순서대로 사용합니다.
    #
    # enumerate는 각 항목에 번호를 붙여 줍니다.
    # start=1은 번호를 1부터 시작하라는 뜻입니다.
    #
    # enumerate(logs, start=1)이 제공하는 값의 모습:
    #
    #   (1, 첫 번째 로그 문자열)
    #   (2, 두 번째 로그 문자열)
    #   (3, 세 번째 로그 문자열)
    #   (4, 네 번째 로그 문자열)
    #
    # idx, line은 이 두 값을 각각 나누어 받습니다.
    # 이렇게 여러 값을 이름별로 나누어 받는 것을 '언패킹'이라고 합니다.
    #
    # idx  → 현재 로그의 번호
    # line → 현재 로그 문자열
    #
    # 이 번호는 로그의 순번입니다.
    # 문자열 안의 epoch 값을 읽어서 만든 번호는 아닙니다.
    for idx, line in enumerate(logs, start=1):

        # 5. 오류가 발생할 수 있는 작업을 try 안에 작성합니다.
        #
        # 파이썬에서는 실행 중 발생하는 오류를 '예외'라고 부릅니다.
        #
        # try 안에서 예외가 발생하면
        # 그 아래의 except 중 해당 예외를 처리할 곳으로 이동합니다.
        try:

            # 6. 한 줄의 문자열을 딕셔너리로 바꿉니다.
            #
            # 첫 번째 로그를 예로 들어 안쪽부터 살펴봅시다.
            #
            # line:
            #   "epoch=1,loss=0.45,acc=88.5"
            #
            # ① line.split(",")
            #
            # split은 지정한 문자를 기준으로 문자열을 나눕니다.
            # 쉼표를 기준으로 나누면 다음 리스트가 됩니다.
            #
            #   ["epoch=1", "loss=0.45", "acc=88.5"]
            #
            # ② for item in line.split(",")
            #
            # 나눈 문자열을 하나씩 item이라는 이름으로 사용합니다.
            #
            # ③ item.split("=")
            #
            # 각 문자열을 다시 등호 기준으로 나눕니다.
            #
            #   "epoch=1"   → ["epoch", "1"]
            #   "loss=0.45" → ["loss", "0.45"]
            #   "acc=88.5"  → ["acc", "88.5"]
            #
            # ④ dict(...)
            #
            # dict는 이런 두 항목짜리 묶음들을 받아 딕셔너리를 만듭니다.
            # 각 묶음의 첫 번째 항목은 키, 두 번째 항목은 값이 됩니다.
            #
            # 결과:
            #   {"epoch": "1", "loss": "0.45", "acc": "88.5"}
            #
            # 괄호 안의 '표현식 for ...'는 제너레이터 표현식입니다.
            # 필요한 묶음을 하나씩 만들어 dict에 전달합니다.
            #
            # 여기까지 처리해도 딕셔너리의 값은 여전히 문자열입니다.
            parts = dict(item.split("=") for item in line.split(","))

            # 7. 필요한 값을 꺼내 숫자로 변환합니다.
            #
            # 중괄호 {} 안에 '키: 값'을 적으면 딕셔너리를 만듭니다.
            # 딕셔너리는 이름표인 '키'와 그에 연결된 '값'을 저장합니다.
            record = {

                # parts["epoch"]는 epoch 키에 연결된 값을 꺼냅니다.
                #
                # 첫 번째 로그에서는 "1"을 가져옵니다.
                # int("1")은 문자열 "1"을 정수 1로 바꿉니다.
                "epoch": int(parts["epoch"]),

                # float는 값을 실수로 변환합니다.
                #
                # float("0.45") → 숫자 0.45
                #
                # 두 번째 로그에서는 float("invalid")가 되어
                # ValueError가 발생합니다.
                "loss": float(parts["loss"]),

                # acc 값도 실수로 변환합니다.
                #
                # float("88.5") → 숫자 88.5
                #
                # 세 번째 로그에는 acc 키가 없습니다.
                # 따라서 parts["acc"]에서 KeyError가 발생합니다.
                "acc": float(parts["acc"]),
            }

            # 첫 번째 로그가 성공적으로 처리되면 record는 다음과 같습니다.
            #
            #   {"epoch": 1, "loss": 0.45, "acc": 88.5}
            #
            # parts와 달리 값들이 실제 숫자로 바뀌었습니다.
            #
            # 중간에 예외가 발생하면 딕셔너리 생성과 대입이 완료되지 않고
            # 해당 예외를 처리하는 except로 이동합니다.

        # 8. 값 변환 중 발생한 ValueError를 처리합니다.
        #
        # except는 지정한 종류의 예외가 발생했을 때 실행됩니다.
        #
        # ValueError:
        #   작업에 사용할 수 없는 값이 들어왔을 때 발생하는 예외입니다.
        #   이 예제에서는 "invalid"를 실수로 변환하려다가 발생합니다.
        #
        # as e:
        #   발생한 예외 객체를 e라는 이름으로 사용하겠다는 뜻입니다.
        #   예외 객체에는 오류를 설명하는 정보가 들어 있습니다.
        #
        # 참고로 위의 dict 생성 과정에서도 항목이 키와 값 두 개로
        # 나뉘지 않으면 ValueError가 발생할 수 있습니다.
        except ValueError as e:

            # 오류가 발생한 로그의 번호, 원문, 오류 설명을 출력합니다.
            print(

                # f"..."는 문자열 안에 실제 값을 넣는 문법입니다.
                # {idx} 자리에 현재 로그 번호가 들어갑니다.
                f"[Line {idx} 변환 오류] "

                # {line} → 문제가 발생한 원본 로그
                # {e}    → 예외 객체의 오류 설명
                #
                # 나란히 적은 두 문자열은 자동으로 이어 붙습니다.
                # 따라서 코드를 두 줄로 적어도 한 줄로 출력됩니다.
                f"숫자 형식이 아닙니다: '{line}' ({e})"
            )

        # 9. 필요한 키가 없어서 발생한 KeyError를 처리합니다.
        #
        # KeyError는 딕셔너리에 없는 키를 []로 조회할 때 발생합니다.
        #
        # 세 번째 로그에서는 acc 키가 없으므로 이 블록이 실행됩니다.
        # 이때 e에는 누락된 키에 대한 정보가 들어 있습니다.
        except KeyError as e:

            print(
                f"[Line {idx} 필드 누락] "

                # KeyError를 문자열로 표시하면
                # 이 예제에서는 누락된 키가 'acc'처럼 따옴표와 함께 보입니다.
                f"필수 키 {e} 가 없습니다: '{line}'"
            )

        # 10. try 안의 작업이 예외 없이 끝났을 때만 실행합니다.
        #
        # 여기의 else는 if가 아니라 try에 연결된 else입니다.
        #
        # 즉, 위의 문자열 분리와 숫자 변환이 모두 성공했을 때
        # 정상 기록으로 저장하겠다는 뜻입니다.
        #
        # ValueError나 KeyError를 처리한 경우에는 이 부분을 건너뜁니다.
        else:

            # append는 리스트의 맨 뒤에 항목 하나를 추가하는 메서드입니다.
            #
            # 성공적으로 만든 record 딕셔너리를 결과 리스트에 넣습니다.
            # 오류가 난 로그는 이 줄에 도달하지 않으므로 저장되지 않습니다.
            valid_records.append(record)

            # 정상적으로 수집했다는 안내문을 출력합니다.
            print(
                f"[Line {idx} 정상 수집] "

                # record['epoch']는 현재 기록의 에포크 번호입니다.
                # record['acc']는 현재 기록의 정확도입니다.
                #
                # 바깥 문자열은 큰따옴표를 사용하고,
                # 중괄호 안의 딕셔너리 키는 작은따옴표로 적었습니다.
                #
                # ->와 %는 화면에 그대로 표시할 문자입니다.
                f"Epoch {record['epoch']} -> Accuracy: {record['acc']}%"
            )

        # 11. 해당 try문을 빠져나갈 때 실행하는 부분입니다.
        #
        # 정상 처리된 경우에도,
        # 예외를 처리한 경우에도 finally가 실행됩니다.
        #
        # 파일 닫기나 자원 정리처럼 공통으로 마무리할 작업을
        # 작성할 때 사용할 수 있습니다.
        finally:

            # pass는 '아무 작업도 하지 않고 지나가라'는 문법입니다.
            #
            # 파이썬에서는 finally: 아래를 완전히 비워 둘 수 없으므로
            # 아직 작성할 작업이 없을 때 pass를 넣을 수 있습니다.
            #
            # 현재 코드에서는 실제 스트림 상태 점검을 수행하지 않습니다.
            # 나중에 필요한 코드를 넣을 자리로 남겨 둔 것입니다.
            pass

        # 한 줄에 대한 처리가 끝나면 for문이 다음 로그를 꺼냅니다.
        #
        # 오류가 난 경우에도 except에서 처리했으므로
        # 별도의 continue 없이 다음 반복으로 넘어갑니다.
        #
        # 다음 로그를 계속 처리할 수 있게 하는 핵심은
        # 예외를 except에서 처리한 것입니다.
        # pass가 오류를 해결해 주는 것은 아닙니다.

    # 12. 모든 로그를 처리한 뒤 결과를 출력합니다.
    #
    # 이 줄은 for문보다 한 단계 바깥에 있습니다.
    # 따라서 로그마다 실행되는 것이 아니라 반복이 끝난 뒤 한 번 실행됩니다.
    #
    # len(logs):
    #   입력으로 받은 전체 로그 수입니다.
    #
    # len(valid_records):
    #   정상적으로 저장한 기록 수입니다.
    print(
        f"[파서 종료] 총 {len(logs)}건 중 "
        f"{len(valid_records)}건 정상 로드 완료."
    )

    # 13. 정상 기록들을 함수를 호출한 곳에 돌려줍니다.
    #
    # print는 화면에 보여 주는 역할이고,
    # return은 이후 코드에서 사용할 데이터를 전달하는 역할입니다.
    return valid_records


# 14. 함수를 실행하고 반환된 결과를 저장합니다.
#
# raw_logs를 함수에 전달하면
# 함수 안에서는 그 리스트를 logs라는 매개변수로 사용합니다.
#
# 오른쪽 함수 호출이 먼저 실행됩니다.
# 함수가 정상 기록 리스트를 return하면
# 그 결과를 왼쪽의 parsed라는 변수에 저장합니다.
parsed = parse_training_logs(raw_logs)


# 실제 화면에 출력되는 내용:
#
# [Line 1 정상 수집] Epoch 1 -> Accuracy: 88.5%
# [Line 2 변환 오류] 숫자 형식이 아닙니다: 'epoch=2,loss=invalid,acc=91.0' (could not convert string to float: 'invalid')
# [Line 3 필드 누락] 필수 키 'acc' 가 없습니다: 'epoch=3,loss=0.31'
# [Line 4 정상 수집] Epoch 4 -> Accuracy: 94.2%
# [파서 종료] 총 4건 중 2건 정상 로드 완료.
#
#
# parsed에 저장되는 실제 데이터:
#
# [
#     {"epoch": 1, "loss": 0.45, "acc": 88.5},
#     {"epoch": 4, "loss": 0.22, "acc": 94.2},
# ]
#
# parsed를 출력하는 코드는 없으므로
# 이 리스트 자체가 자동으로 화면에 출력되지는 않습니다.
#
#
# 각 로그가 거친 경로를 정리해 봅시다.
#
# 첫 번째: try 성공 → else에서 저장 → finally
# 두 번째: try에서 ValueError → 해당 except → finally
# 세 번째: try에서 KeyError → 해당 except → finally
# 네 번째: try 성공 → else에서 저장 → finally
#
# 이 코드에서 오류 로그의 '격리'는
# 정상 결과 리스트에 넣지 않고 오류 안내문을 출력하는 방식입니다.
# 오류 로그를 별도의 리스트나 파일에 저장하는 코드는 없습니다.