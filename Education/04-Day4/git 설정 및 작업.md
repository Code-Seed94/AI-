네, 맞습니다. **GitHub 저장소 생성 → 폴더·파일 생성 → 커밋 → 푸시 → 수정·추가 → 새 브랜치 → 병합** 순서입니다.

단, GitHub의 초기 설정 명령어는 **내 컴퓨터의 프로젝트 폴더로 이동한 다음** 실행해야 합니다.

## 1\. 저장소 생성 및 최초 업로드

|명령어|의미|
|-|-|
|GitHub → New repository|GitHub에서 새 저장소 생성|
|`mkdir my-project`|프로젝트 폴더 생성|
|`cd my-project`|생성한 폴더로 이동|
|`git init`|현재 폴더를 Git 저장소로 설정|
|`git branch -M main`|기본 브랜치를 main으로 설정|
|`git remote add origin 저장소URL`|GitHub 저장소 연결|
|`code .`|현재 폴더를 VS Code로 열기|
|VS Code에서 파일 생성·저장|코드 파일 작성 후 `Ctrl + S`|
|`git add .`|변경된 파일 전체 스테이징|
|`git commit -m "first"`|첫 번째 커밋 기록|
|`git push -u origin main`|GitHub에 최초 업로드 및 연결 설정|

## 2\. 기존 파일 수정 및 추가

|명령어|의미|
|-|-|
|`git pull origin main`|작업 전 GitHub main 최신 내용 가져오기|
|VS Code 파일 수정·추가|기존 코드 수정 또는 새 파일 생성 후 저장|
|`git status`|수정·추가된 파일 확인|
|`git add .`|변경사항 전체 스테이징|
|`git commit -m "수정"`|변경사항 커밋|
|`git push`|GitHub에 최신 커밋 업로드|
|`git fetch origin`|GitHub 최신 변경 정보 확인|
|`git diff HEAD origin/main`|로컬 커밋과 원격 main 비교|

## 3\. 새 브랜치 생성 및 작업

|명령어|의미|
|-|-|
|`git switch main`|main 브랜치로 이동|
|`git pull origin main`|최신 main 코드 가져오기|
|`git switch -c bbb/4tt`|새 브랜치 생성 및 이동|
|VS Code 파일 생성·수정|새 브랜치에서 코드 작업 후 저장|
|`git add .`|수정한 파일 스테이징|
|`git commit -m "기능 추가"`|새 브랜치에 커밋|
|`git push -u origin bbb/4tt`|새 브랜치를 GitHub에 최초 업로드|
|`git push`|이후 새 브랜치의 변경사항 업로드|

## 4\. GitHub에서 병합(Merge)

|명령어 / 작업|의미|
|-|-|
|GitHub → Pull requests|병합 요청 메뉴 이동|
|`New pull request`|새 병합 요청 생성|
|`base: main`|변경사항을 받을 브랜치 선택|
|`compare: bbb/4tt`|병합할 새 브랜치 선택|
|`Create pull request`|병합 요청 등록|
|`Merge pull request`|새 브랜치의 내용을 main에 병합|
|`Confirm merge`|병합 확정|
|`git switch main`|VS Code에서 main으로 이동|
|`git pull origin main`|병합된 최신 main 코드 가져오기|
|`git status`|최종 동기화 상태 확인|

## 5\. 핵심 작업 순서

**① 저장소 생성 → Git 연결**

↓

**② 폴더·파일 생성 → 저장**

↓

**③ Add → Commit → Push**

↓

**④ 새 브랜치 생성 → 수정 → Commit → Push**

↓

**⑤ Pull Request → Merge**

↓

**⑥ main 이동 → Pull → 최신 상태 확인**

**주의할 점:** 위 최초 설정은 GitHub에서 README 없이 빈 저장소를 생성한 경우를 기준으로 합니다. GitHub에서 README까지 생성했다면 `git clone 저장소URL`로 가져오는 것이 간단하며, 이미 연결된 저장소에서는 `git init`과 `git remote add origin`을 반복할 필요가 없습니다.

