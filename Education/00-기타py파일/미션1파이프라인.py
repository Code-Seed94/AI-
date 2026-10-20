"""미션1.py의 analyze_fizzbuzz를 assert로 검증하는 실행형 파이프라인.

실행: python 미션1파이프라인.py
실패한 assert는 원인과 함께 실행을 중단하며, 종료 코드는 0이 아니다.
assert가 생략되는 python -O 또는 -OO 실행은 허용하지 않는다.
"""

from 미션1 import analyze_fizzbuzz


CATEGORIES = ("FizzBuzz", "Fizz", "Buzz", "Number")
ZERO_COUNTS = dict.fromkeys(CATEGORIES, 0)


def assert_result(limit: int, expected: dict) -> dict:
    """결과의 키, 정수 타입, 음수 여부, 총합, 정확한 값을 검사한다."""
    actual = analyze_fizzbuzz(limit)
    assert type(actual) is dict, f"limit={limit}: dict가 아님: {actual!r}"
    assert set(actual) == set(CATEGORIES), (
        f"limit={limit}: 반환 키가 잘못됨: {actual!r}"
    )
    for category in CATEGORIES:
        value = actual[category]
        # bool도 int의 하위 타입이므로 정확한 타입 비교로 제외한다.
        assert type(value) is int, (
            f"limit={limit}, {category}: int가 아님: {value!r}"
        )
        assert value >= 0, f"limit={limit}, {category}: 음수 카운트: {value}"

    assert sum(actual.values()) == max(0, limit), (
        f"limit={limit}: 누락 또는 중복 집계: {actual!r}"
    )
    assert actual == expected, (
        f"limit={limit}: 기대값={expected!r}, 실제값={actual!r}"
    )
    return actual


def test_non_positive_limits() -> int:
    """0과 다양한 음수에서는 모든 카운트가 0이어야 한다."""
    limits = (-10**12, -100, -15, -5, -1, 0)
    for limit in limits:
        assert_result(limit, ZERO_COUNTS)
    return len(limits)


def test_known_results() -> int:
    """각 분기와 15의 배수 전후를 미리 계산한 정답으로 검증한다."""
    cases = (
        (1, (0, 0, 0, 1)),
        (2, (0, 0, 0, 2)),
        (3, (0, 1, 0, 2)),
        (4, (0, 1, 0, 3)),
        (5, (0, 1, 1, 3)),
        (6, (0, 2, 1, 3)),
        (9, (0, 3, 1, 5)),
        (10, (0, 3, 2, 5)),
        (14, (0, 4, 2, 8)),
        (15, (1, 4, 2, 8)),
        (16, (1, 4, 2, 9)),
        (29, (1, 8, 4, 16)),
        (30, (2, 8, 4, 16)),
        (31, (2, 8, 4, 17)),
        (45, (3, 12, 6, 24)),
        (100, (6, 27, 14, 53)),
        (1000, (66, 267, 134, 533)),
    )
    for limit, values in cases:
        assert_result(limit, dict(zip(CATEGORIES, values)))
    return len(cases)


def test_against_arithmetic_reference() -> int:
    """구현의 분기문을 복제하지 않고 배수 개수 공식과 대조한다."""
    limits = list(range(-20, 301)) + [999, 1001, 9999, 10000, 10001, 100000]
    for limit in limits:
        size = max(0, limit)
        both = size // 15
        expected = {
            "FizzBuzz": both,
            "Fizz": size // 3 - both,
            "Buzz": size // 5 - both,
            "Number": size - size // 3 - size // 5 + both,
        }
        assert_result(limit, expected)
    return len(limits)


def test_each_number_increments_one_category() -> int:
    """숫자 하나를 추가할 때 정확히 해당 분류 하나만 증가해야 한다."""
    cycle = (
        "Number", "Number", "Fizz", "Number", "Buzz",
        "Fizz", "Number", "Number", "Fizz", "Buzz",
        "Number", "Fizz", "Number", "Number", "FizzBuzz",
    )
    previous = assert_result(0, ZERO_COUNTS)
    for limit in range(1, 91):
        category = cycle[(limit - 1) % len(cycle)]
        expected = previous.copy()
        expected[category] += 1
        previous = assert_result(limit, expected)
    return 90


def test_fifteen_number_period() -> int:
    """연속된 15개 정수에서는 분류별 개수가 항상 같아야 한다."""
    block_counts = {"FizzBuzz": 1, "Fizz": 4, "Buzz": 2, "Number": 8}
    for start in range(31):
        before = analyze_fizzbuzz(start)
        expected = {
            category: before[category] + block_counts[category]
            for category in CATEGORIES
        }
        assert_result(start + 15, expected)
    return 31


def test_independent_calls() -> int:
    """반복 호출과 반환값 변경이 다른 호출 결과에 영향을 주면 안 된다."""
    expected = {"FizzBuzz": 1, "Fizz": 4, "Buzz": 2, "Number": 8}
    first = assert_result(15, expected)
    second = assert_result(15, expected)
    assert first is not second, "호출 간 반환 딕셔너리가 공유됨"

    first["FizzBuzz"] = -999
    first["Unexpected"] = 1
    assert second == expected, "이전 반환값의 변경이 다른 결과에 영향을 줌"
    assert_result(15, expected)
    assert_result(0, ZERO_COUNTS)

    empty = assert_result(-1, ZERO_COUNTS)
    empty["Number"] = 999
    assert_result(0, ZERO_COUNTS)
    assert_result(1, {"FizzBuzz": 0, "Fizz": 0, "Buzz": 0, "Number": 1})
    return 1


def run_pipeline() -> int:
    """검증 그룹을 순서대로 실행하고 통과한 시나리오 수를 반환한다."""
    if not __debug__:
        raise RuntimeError("assert 검증이 필요합니다. -O/-OO 옵션 없이 실행하세요.")

    tests = (
        test_non_positive_limits,
        test_known_results,
        test_against_arithmetic_reference,
        test_each_number_increments_one_category,
        test_fifteen_number_period,
        test_independent_calls,
    )
    total = 0
    for test in tests:
        try:
            count = test()
        except AssertionError:
            print(f"[FAIL] {test.__name__}")
            raise
        total += count
        print(f"[PASS] {test.__name__}: {count} scenarios")

    print(f"All {len(tests)} groups passed ({total} scenarios).")
    return total


if __name__ == "__main__":
    run_pipeline()
