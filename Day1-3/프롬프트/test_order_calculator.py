from decimal import Decimal, localcontext
from fractions import Fraction

from order_calculator import calc_order_legacy


# 정상 계산과 앞서 발견한 문제의 회귀 테스트입니다.
valid_cases = [
    ((1, 10000, 2, "NO"), 19000),
    ((1, 10000, 2, "YES"), 16000),
    ((2, 10000, 2, "NO"), 18000),
    ((2, 10000, 2, "YES"), 15000),
    ((3, 10000, 2, "NO"), 16000),
    ((3, 10000, 2, "YES"), 13000),
    ((1, 1000, 1, "YES"), 0),
    ((1, 1.15, 400, "NO"), 437),
    ((1, 2.3, 200, "NO"), 437),
    ((1, Decimal("1.15"), 400, "NO"), 437),
    ((2, 0.1, 100, "NO"), 9),
    ((3, Decimal("0.01"), 1250, "NO"), 10),
    ((1, 199, 1, "NO"), 189),
    ((2, 1, 1, "NO"), 0),
    ((3, 1, 1, "NO"), 0),
    ((1, 0, 1, "NO"), 0),
    ((1, 0, 1, "YES"), 0),
    ((1, Decimal("0.00"), 1, "NO"), 0),
    ((1, 10000, 1, "yes"), 6500),
    ((1, 10000, 1, " YES "), 6500),
    ((1, 10000, 1, "\tNo\n"), 9500),
    ((1, 10000000000000002, 1, "NO"), 9500000000000001),
    ((1, 10**100 + 2, 1, "NO"), (10**100 + 2) * 95 // 100),
    ((1, 10**100 + 2, 1, "YES"), (10**100 + 2) * 95 // 100 - 3000),
    ((1, Decimal("1E+100"), 1, "YES"), 95 * 10**98 - 3000),
    ((1, Decimal("99.9999999999999999999999999999999999999999"), 1, "NO"), 94),
]


invalid_cases = [
    ((True, 10000, 1, "NO"), TypeError),
    ((False, 10000, 1, "NO"), TypeError),
    ((1.0, 10000, 1, "NO"), TypeError),
    (("1", 10000, 1, "NO"), TypeError),
    ((None, 10000, 1, "NO"), TypeError),
    ((0, 10000, 1, "NO"), ValueError),
    ((4, 10000, 1, "NO"), ValueError),
    ((-1, 10000, 1, "NO"), ValueError),
    ((1, 10000, True, "NO"), TypeError),
    ((1, 10000, False, "NO"), TypeError),
    ((1, 10000, 1.5, "NO"), TypeError),
    ((1, 10000, "2", "NO"), TypeError),
    ((1, 10000, None, "NO"), TypeError),
    ((1, 10000, 0, "NO"), ValueError),
    ((1, 10000, -1, "NO"), ValueError),
    ((1, True, 1, "NO"), TypeError),
    ((1, False, 1, "NO"), TypeError),
    ((1, "10000", 1, "NO"), TypeError),
    ((1, None, 1, "NO"), TypeError),
    ((1, 1 + 2j, 1, "NO"), TypeError),
    ((1, -1000, 1, "NO"), ValueError),
    ((1, -1000, -2, "NO"), ValueError),
    ((1, -0.01, 1, "NO"), ValueError),
    ((1, Decimal("-0.01"), 1, "NO"), ValueError),
    ((1, float("nan"), 1, "NO"), ValueError),
    ((1, float("inf"), 1, "NO"), ValueError),
    ((1, float("-inf"), 1, "NO"), ValueError),
    ((1, Decimal("NaN"), 1, "NO"), ValueError),
    ((1, Decimal("sNaN"), 1, "NO"), ValueError),
    ((1, Decimal("Infinity"), 1, "NO"), ValueError),
    ((1, 10000, 1, True), TypeError),
    ((1, 10000, 1, False), TypeError),
    ((1, 10000, 1, None), TypeError),
    ((1, 10000, 1, 1), TypeError),
    ((1, 10000, 1, ""), ValueError),
    ((1, 10000, 1, "Y"), ValueError),
    ((1, 10000, 1, "MAYBE"), ValueError),
    ((1, 10000, 1, " yes no "), ValueError),
]


def run_tests():
    for args, expected in valid_cases:
        actual = calc_order_legacy(*args)
        assert type(actual) is int and actual == expected, (args, expected, actual)

    for args, expected_error in invalid_cases:
        try:
            calc_order_legacy(*args)
        except Exception as error:
            assert type(error) is expected_error, (args, type(error), expected_error)
        else:
            raise AssertionError((args, "Expected exception was not raised"))

    # Decimal과 독립적인 Fraction 연산으로 경계값을 교차 검증합니다.
    prices = [0, 1, 19, 20, 21, 199, 2999, 3000, 3001, 10000, 1000000,
              1.15, 2.3, Decimal("99.9999999999999999999999999999999999999999")]
    reference_cases = 0
    for u_type, payment_percent in [(1, 95), (2, 90), (3, 80)]:
        for price in prices:
            for qty in [1, 2, 7]:
                for coupon in ["YES", "NO"]:
                    exact = Fraction(str(price)) * qty * Fraction(payment_percent, 100)
                    if coupon == "YES":
                        exact -= 3000
                    expected = max(0, exact.numerator // exact.denominator)
                    actual = calc_order_legacy(u_type, price, qty, coupon)
                    assert actual == expected, (u_type, price, qty, coupon, expected, actual)
                    reference_cases += 1

    # 호출한 쪽의 정밀도가 낮아도 결과가 정확하고 외부 설정이 유지됩니다.
    with localcontext() as context:
        context.prec = 6
        assert calc_order_legacy(1, 10000000000000002, 1, "NO") == 9500000000000001
        assert context.prec == 6

    print(f"PASS: {len(valid_cases)} valid cases")
    print(f"PASS: {len(invalid_cases)} invalid cases")
    print(f"PASS: {reference_cases} independent reference cases")
    print("PASS: caller precision independence and preservation (2 checks)")


if __name__ == "__main__":
    run_tests()
