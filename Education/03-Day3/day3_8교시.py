# 답을 찾아보세요
# [Before: 리팩토링 전 — 이상치·결측치 유입 시 즉시 크래시되는 취약한 함수]
def preprocess_legacy(data):
    res = []

    for row in data:
        # 치명적 결함: 'score' 키가 없거나 'N/A' 문자열이면 즉시 프로그램 강제 종료!
        # 치명적 결함: 100점을 초과하는 이상치(120점)도 걸러내지 못하고 1.2로 잘못 정규화함!
        score = float(row["score"])
        res.append(round(score / 100.0, 4))

    return res



# [After: Codex 방어적 리팩토링 후 — 검증 캡슐화 + 예외 체이닝 + 자동 성공률 리포트]

from dataclasses import dataclass


class DataValidationError(Exception):
    """데이터 전처리 검증 실패를 나타내는 커스텀 예외"""
    pass


@dataclass
class PreprocessReport:
    normalized_scores: list[float]
    skipped_rows: list[str]

    @property
    def success_rate(self) -> float:
        total = len(self.normalized_scores) + len(self.skipped_rows)

        return (
            round((len(self.normalized_scores) / total) * 100, 1)
            if total > 0
            else 0.0
        )


class SafeScorePreprocessor:
    def __init__(self, min_score: float = 0.0, max_score: float = 100.0):
        if max_score <= min_score:
            raise ValueError(
                "max_score는 min_score보다 커야 합니다 (ZeroDivision 방지)."
            )

        self.min_score = min_score
        self.max_score = max_score

    def _validate_and_extract(self, row: dict) -> float:
        if "score" not in row or row["score"] is None:
            raise DataValidationError("score 키가 없거나 None입니다.")

        try:
            val = float(row["score"])
        except (ValueError, TypeError) as exc:
            raise DataValidationError(
                f"숫자로 변환할 수 없는 값('{row['score']}')입니다."
            ) from exc

        if not (self.min_score <= val <= self.max_score):
            raise DataValidationError(
                f"허용 범위({self.min_score}~{self.max_score}) 초과: {val}"
            )

        return val

    def transform(self, dataset: list[dict]) -> PreprocessReport:
        normalized = []
        skipped = []
        span = self.max_score - self.min_score

        for idx, row in enumerate(dataset, start=1):
            try:
                raw_val = self._validate_and_extract(row)

            except DataValidationError as err:
                skipped.append(f"Row {idx}: {err}")

            else:
                norm_val = round((raw_val - self.min_score) / span, 4)
                normalized.append(norm_val)

        return PreprocessReport(
            normalized_scores=normalized,
            skipped_rows=skipped,
        )


raw_dataset = [
    {"id": 1, "score": "85.0"},
    {"id": 2, "score": "N/A"},  # 변환 오류 -> 안전 격리
    {"id": 3, "score": 120},    # 범위 초과 -> 안전 격리
    {"id": 4, "score": 92.5},
    {"id": 5},                 # 키 누락 -> 안전 격리
]

processor = SafeScorePreprocessor(0.0, 100.0)
report = processor.transform(raw_dataset)

print("정규화 결과:", report.normalized_scores)
print("제외된 행 로그:", report.skipped_rows)
print(f"전처리 성공률: {report.success_rate}%")


# 실행 결과:
# 정규화 결과: [0.85, 0.925]
# 제외된 행 로그: ["Row 2: 숫자로 변환할 수 없는 값('N/A')입니다.", 'Row 3: 허용 범위(0.0~100.0) 초과: 120.0', 'Row 5: score 키가 없거나 None입니다.']
# 전처리 성공률: 40.0%