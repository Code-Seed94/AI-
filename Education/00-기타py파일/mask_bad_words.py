import re


def mask_bad_words(chat_message: str, bad_words: list[str]) -> str:
    """대소문자를 구분하지 않고 모든 금지어 영역을 '*'로 치환한다."""
    # 결과를 저장할 문자 목록을 만들고, 원본 메시지는 검색용으로 유지합니다.
    masked_chars = list(chat_message)

    for bad_word in bad_words:
        # 빈 문자열은 검색하지 않습니다. 공백이 있는 금지어는 그대로 사용합니다.
        if bad_word == "":
            continue

        # 특수문자를 일반 문자로 취급하고 대소문자를 구분하지 않습니다.
        pattern = re.compile(re.escape(bad_word), re.IGNORECASE)
        search_start = 0

        while True:
            # 항상 원본에서 찾아 이전 마스킹이 다음 검색에 영향을 주지 않습니다.
            match = pattern.search(chat_message, search_start)
            if match is None:
                break

            # 일치한 각 문자를 덮어씁니다. 겹치는 영역도 같은 위치에 '*'를 씁니다.
            for index in range(match.start(), match.end()):
                masked_chars[index] = "*"

            # 일치 시작점에서 한 칸만 이동해 서로 겹치는 일치도 찾습니다.
            search_start = match.start() + 1

    # 문자 수와 다른 문자의 위치를 보존하며 최종 문자열을 만듭니다.
    return "".join(masked_chars)


if __name__ == "__main__":
    # 각 항목은 (원본 메시지, 금지어 목록, 기대 결과)입니다.
    test_cases = [
        ("너는 바보야", ["바보"], "너는 **야"),
        ("BAD", ["bad"], "***"),
        ("bAd", ["BaD"], "***"),
        ("바보 바보", ["바보"], "** **"),
        ("badBADbad", ["bad"], "*********"),
        ("바보 BAD", ["바보", "bad"], "** ***"),
        ("왕바보야", ["바보"], "왕**야"),
        ("안녕하세요!", ["바보"], "안녕하세요!"),
        ("", ["bad"], ""),
        ("Hello", [], "Hello"),
        ("Hello", [""], "Hello"),
        ("BAD", ["", "bad", ""], "***"),
        ("Hello", ["", ""], "Hello"),
        ("BAD bad", ["bad", "bad", "BAD"], "*** ***"),
        ("abcde", ["abc", "cde"], "*****"),
        ("abcd", ["ab", "abcd"], "****"),
        ("ababa", ["aba"], "*****"),
        ("v1.2", ["."], "v1*2"),
        ("a*b", ["a*b"], "***"),
        ("I use C++", ["c++"], "I use ***"),
        ("[금지] 허용", ["[금지]"], "**** 허용"),
        ("(bad) BAD", ["(bad)"], "***** BAD"),
        (" BAD,\n바보! ", ["bad", "바보"], " ***,\n**! "),
        ("bad word / bad", ["bad word"], "******** / bad"),
        ("Hello BAD World", ["bad"], "Hello *** World"),
        ("İ BAD", ["bad"], "İ ***"),
        ("😀바보😀", ["바보"], "😀**😀"),
    ]

    for message, bad_words, expected in test_cases:
        original_bad_words = bad_words.copy()
        actual = mask_bad_words(message, bad_words)

        # 기대 결과, 길이 보존, 입력 목록 보존, 목록 순서 독립성을 확인합니다.
        assert actual == expected, (message, bad_words, expected, actual)
        assert len(actual) == len(message)
        assert bad_words == original_bad_words
        assert mask_bad_words(message, bad_words[::-1]) == expected

    print(f"{len(test_cases)} test cases passed (108 assertions).")
