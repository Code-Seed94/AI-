# Git·GitHub 명령어 - 의미 정리

각 명령어의 뜻을 한 줄로 정리한 참고표입니다.

## 1\. Git 시작과 저장소 준비

|명령어|의미|
|-|-|
|`git config --global user.name "이름"`|커밋에 표시할 사용자 이름을 설정합니다.|
|`git config --global user.email "이메일"`|커밋에 표시할 사용자 이메일을 설정합니다.|
|`git config --global --list`|현재 Git 전역 설정을 확인합니다.|
|`git init`|현재 폴더를 Git 저장소로 초기화합니다.|
|`git clone <저장소\\\_URL>`|원격 저장소를 내 컴퓨터로 복사합니다.|
|`git remote -v`|연결된 원격 저장소 주소를 확인합니다.|

## 2\. 파일 확인과 커밋 준비

|명령어|의미|
|-|-|
|`git status`|현재 파일과 브랜치의 변경 상태를 확인합니다.|
|`git add <파일명>`|지정한 파일을 커밋할 준비 영역에 올립니다.|
|`git add .`|현재 폴더의 변경 파일을 모두 커밋 준비 영역에 올립니다.|
|`git diff`|아직 준비 영역에 올리지 않은 변경 내용을 확인합니다.|
|`git diff --staged`|커밋 준비 영역에 올라간 변경 내용을 확인합니다.|
|`git restore --staged <파일명>`|파일을 커밋 준비 영역에서 내립니다.|
|`git restore <파일명>`|커밋하지 않은 파일 변경을 마지막 커밋 상태로 되돌립니다.|

## 3\. 커밋과 기록 확인

|명령어|의미|
|-|-|
|`git commit -m "메시지"`|준비 영역의 변경 내용을 하나의 버전으로 기록합니다.|
|`git log --oneline`|커밋 기록을 한 줄씩 간단히 확인합니다.|
|`git log --oneline --all --graph`|모든 브랜치의 커밋 흐름을 그래프로 확인합니다.|
|`git show <커밋ID>`|특정 커밋의 변경 내용을 확인합니다.|
|`git commit --amend -m "수정 메시지"`|가장 최근 커밋의 내용이나 메시지를 수정합니다.|
|`git reset --soft HEAD\\\~1`|최근 커밋을 취소하고 변경 내용을 준비 상태로 남깁니다.|
|`git revert <커밋ID>`|기존 커밋을 취소하는 새 커밋을 만듭니다.|

## 4\. GitHub 연결과 업로드

|명령어|의미|
|-|-|
|`git remote add origin <저장소\\\_URL>`|현재 저장소를 GitHub 원격 저장소와 연결합니다.|
|`git remote set-url origin <새\\\_URL>`|등록된 GitHub 원격 저장소 주소를 변경합니다.|
|`git branch -M main`|현재 브랜치 이름을 main으로 변경합니다.|
|`git push -u origin main`|main 브랜치를 처음 GitHub에 올리고 추적 관계를 설정합니다.|
|`git push`|로컬 커밋을 연결된 GitHub 브랜치에 업로드합니다.|
|`git fetch origin`|GitHub의 최신 기록을 가져오지만 현재 브랜치에는 반영하지 않습니다.|
|`git pull`|GitHub의 변경 사항을 가져와 현재 브랜치에 반영합니다.|

처음 GitHub에 올리는 명령어 예시:

```bash
git init
git add .
git commit -m "첫 커밋"
git branch -M main
git remote add origin https://github.com/<사용자명>/<저장소명>.git
git push -u origin main
```

## 5\. 브랜치와 협업

|명령어|의미|
|-|-|
|`git branch`|로컬 브랜치 목록을 확인합니다.|
|`git switch -c <브랜치명>`|새 브랜치를 만들고 해당 브랜치로 이동합니다.|
|`git switch <브랜치명>`|기존 브랜치로 이동합니다.|
|`git branch -d <브랜치명>`|병합이 끝난 로컬 브랜치를 삭제합니다.|
|`git merge <브랜치명>`|지정한 브랜치의 변경 내용을 현재 브랜치에 합칩니다.|
|`git stash`|아직 커밋하지 않은 변경 내용을 임시 보관합니다.|
|`git stash pop`|임시 보관한 변경 내용을 다시 적용합니다.|
|`git push -u origin <브랜치명>`|새 브랜치를 GitHub에 올리고 추적 관계를 설정합니다.|
|`git merge --abort`|충돌이 발생한 병합 작업을 취소합니다.|

## 핵심 암기표

|명령어|의미|
|-|-|
|`git status`|확인|
|`git add`|선택|
|`git commit`|기록|
|`git push`|업로드|
|`git pull`|내려받아 반영|
|`git clone`|저장소 복사|
|`git switch`|브랜치 이동|
|`git revert`|커밋 취소 기록|

## 전체 작업 순서

```text
git status                         현재 상태 확인
git add .                         변경 파일 준비
git commit -m "메시지"             변경 내용 기록
git push                          GitHub에 업로드
```

### 새 프로젝트를 처음 업로드할 때

```text
1. git init으로 저장소를 만든다.
2. .gitignore에 .env와 비밀 파일을 등록한다.
3. git add .로 업로드할 파일을 준비한다.
4. git commit -m "첫 커밋"으로 기록한다.
5. git remote add origin <저장소\\\_URL>로 GitHub를 연결한다.
6. git branch -M main으로 기본 브랜치를 지정한다.
7. git push -u origin main으로 GitHub에 업로드한다.
```

### 수정한 프로젝트를 다시 업로드할 때

```text
git pull → 파일 수정 → git status → git add . → git commit -m "메시지" → git push
```

> `.env` 파일에는 API 키나 비밀번호를 넣을 수 있지만, 보안을 위해 GitHub에는 업로드하지 않습니다.

